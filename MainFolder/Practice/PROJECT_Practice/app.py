"""
app.py  –  Easha Aqram | DSA Learning Platform
Flask back-end: routing, SQL (SQLite via sqlite3), session management.
"""

import os
import re
import sqlite3
from functools import wraps
from datetime import datetime

import bcrypt
from flask import (Flask, render_template, request, redirect,
                   url_for, session, jsonify, g, flash)

# ── App Configuration ─────────────────────────────────────────
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "easha-akram-dsa-secret-2024")

DATABASE = os.path.join(os.path.dirname(__file__), "database.db")
INSTRUCTOR = "Easha Akram"

# ── Database Helpers ──────────────────────────────────────────
def get_db():
    """Return a per-request SQLite connection stored on Flask's g object."""
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE, detect_types=sqlite3.PARSE_DECLTYPES)
        g.db.row_factory = sqlite3.Row
        g.db.execute("PRAGMA foreign_keys = ON")
    return g.db

@app.teardown_appcontext
def close_db(error=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()

def init_db():
    """Initialise database from schema.sql (run once)."""
    schema = os.path.join(os.path.dirname(__file__), "schema.sql")
    with app.app_context():
        db = get_db()
        with open(schema, "r") as f:
            db.executescript(f.read())
        db.commit()

# ── Auth Decorator ────────────────────────────────────────────
def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if "user_id" not in session:
            flash("Please log in to continue.", "warning")
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated

# ── Validation Helpers ────────────────────────────────────────
EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

def validate_signup(username, email, password):
    errors = {}
    if not username or len(username.strip()) < 3:
        errors["username"] = "Username must be at least 3 characters."
    if not EMAIL_RE.match(email):
        errors["email"] = "Enter a valid email address."
    if len(password) < 6:
        errors["password"] = "Password must be at least 6 characters."
    return errors

# ── Routes ────────────────────────────────────────────────────

@app.route("/")
def index():
    db = get_db()
    topics = db.execute(
        "SELECT * FROM topics ORDER BY category, difficulty"
    ).fetchall()

    # Group by category
    categories = {}
    for t in topics:
        categories.setdefault(t["category"], []).append(dict(t))

    user = None
    if "user_id" in session:
        user = db.execute(
            "SELECT id, username, email FROM users WHERE id = ?",
            (session["user_id"],)
        ).fetchone()

    return render_template("index.html",
                           instructor=INSTRUCTOR,
                           categories=categories,
                           user=user,
                           year=datetime.now().year)


@app.route("/login", methods=["GET", "POST"])
def login():
    if "user_id" in session:
        return redirect(url_for("dashboard"))

    error = None
    if request.method == "POST":
        email    = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        db = get_db()
        # SQL: fetch user by email
        row = db.execute(
            "SELECT id, username, password FROM users WHERE email = ?",
            (email,)
        ).fetchone()

        if row and bcrypt.checkpw(password.encode(), row["password"]):
            session.clear()
            session["user_id"]   = row["id"]
            session["username"]  = row["username"]
            return redirect(url_for("dashboard"))
        else:
            error = "Invalid email or password."

    return render_template("login.html",
                           instructor=INSTRUCTOR,
                           error=error,
                           year=datetime.now().year)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if "user_id" in session:
        return redirect(url_for("dashboard"))

    errors = {}
    form   = {}
    if request.method == "POST":
        form["username"] = request.form.get("username", "").strip()
        form["email"]    = request.form.get("email", "").strip().lower()
        password         = request.form.get("password", "")

        errors = validate_signup(form["username"], form["email"], password)

        if not errors:
            db = get_db()
            # SQL: check for duplicate email or username
            existing = db.execute(
                "SELECT id FROM users WHERE email = ? OR username = ?",
                (form["email"], form["username"])
            ).fetchone()

            if existing:
                errors["email"] = "An account with that email or username already exists."
            else:
                # Hash password with bcrypt
                hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
                # SQL: insert new user
                db.execute(
                    "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
                    (form["username"], form["email"], hashed)
                )
                db.commit()
                flash("Account created! Please log in.", "success")
                return redirect(url_for("login"))

    return render_template("signup.html",
                           instructor=INSTRUCTOR,
                           errors=errors,
                           form=form,
                           year=datetime.now().year)


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


@app.route("/dashboard")
@login_required
def dashboard():
    db      = get_db()
    user_id = session["user_id"]

    # SQL: get all topics with completion status for this user
    topics = db.execute("""
        SELECT t.*, COALESCE(up.completed, 0) AS completed
        FROM   topics t
        LEFT JOIN user_progress up
               ON up.topic_id = t.id AND up.user_id = ?
        ORDER  BY t.category, t.difficulty
    """, (user_id,)).fetchall()

    total     = len(topics)
    completed = sum(1 for t in topics if t["completed"])

    categories = {}
    for t in topics:
        categories.setdefault(t["category"], []).append(dict(t))

    user = db.execute(
        "SELECT id, username, email, created_at FROM users WHERE id = ?",
        (user_id,)
    ).fetchone()

    return render_template("dashboard.html",
                           instructor=INSTRUCTOR,
                           user=user,
                           categories=categories,
                           total=total,
                           completed=completed,
                           year=datetime.now().year)


@app.route("/topic/<slug>")
@login_required
def topic(slug):
    db      = get_db()
    user_id = session["user_id"]

    # SQL: fetch topic by slug
    t = db.execute(
        "SELECT * FROM topics WHERE slug = ?", (slug,)
    ).fetchone()
    if not t:
        return redirect(url_for("dashboard"))

    progress = db.execute(
        "SELECT completed FROM user_progress WHERE user_id=? AND topic_id=?",
        (user_id, t["id"])
    ).fetchone()

    completed = progress["completed"] if progress else 0

    return render_template("topic.html",
                           instructor=INSTRUCTOR,
                           topic=dict(t),
                           completed=completed,
                           year=datetime.now().year)


# ── API Endpoints ─────────────────────────────────────────────

@app.route("/api/progress", methods=["POST"])
@login_required
def update_progress():
    """Mark a topic as completed or not for the logged-in user."""
    data     = request.get_json(force=True)
    topic_id = data.get("topic_id")
    completed = int(bool(data.get("completed", True)))

    if not topic_id:
        return jsonify({"error": "topic_id required"}), 400

    db      = get_db()
    user_id = session["user_id"]

    # SQL: upsert progress record
    db.execute("""
        INSERT INTO user_progress (user_id, topic_id, completed, updated_at)
        VALUES (?, ?, ?, CURRENT_TIMESTAMP)
        ON CONFLICT(user_id, topic_id)
        DO UPDATE SET completed=excluded.completed, updated_at=excluded.updated_at
    """, (user_id, topic_id, completed))
    db.commit()

    return jsonify({"status": "ok", "completed": completed})


@app.route("/api/validate-email", methods=["POST"])
def api_validate_email():
    """Check if an email is already registered (used by signup JS)."""
    email = (request.get_json(force=True) or {}).get("email", "").strip().lower()
    db    = get_db()
    row   = db.execute(
        "SELECT id FROM users WHERE email = ?", (email,)
    ).fetchone()
    return jsonify({"taken": bool(row)})


# ── Entry Point ───────────────────────────────────────────────
if __name__ == "__main__":
    if not os.path.exists(DATABASE):
        init_db()
        print("✓ Database initialised.")
    app.run(debug=True, port=5000, use_reloader=False)