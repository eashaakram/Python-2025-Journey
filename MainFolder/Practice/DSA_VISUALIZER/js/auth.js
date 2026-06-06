/* ================================================================
   auth.js  —  Login & Signup validation, localStorage users
   Author : Easha Akram
   ================================================================ */

/* ─── Regex patterns ─────────────────────────────────────── */
const RX_EMAIL = /^[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.(com|pk|edu|org|net|gov|co|io|me)$/i;
const RX_PHONE = /^03\d{9}$/;
const RX_CNIC  = /^\d{13}$/;

/* ─── Helpers ────────────────────────────────────────────── */
const $ = id => document.getElementById(id);
const v  = el => (el ? el.value.trim() : "");

function setErr(input, msg) {
  if (!input) return false;
  input.classList.add("err"); input.classList.remove("ok");
  const e = input.closest(".field")?.querySelector(".ferr");
  if (e) { e.textContent = msg; e.classList.add("show"); }
  return false;
}
function clearF(input) {
  if (!input) return true;
  input.classList.remove("err"); input.classList.add("ok");
  const e = input.closest(".field")?.querySelector(".ferr");
  if (e) e.classList.remove("show");
  return true;
}

function showAlert(elId, msg, type = "error") {
  const el = $(elId);
  if (!el) return;
  el.textContent = msg;
  el.className = `auth-alert show ${type}`;
}

/* ─── Password strength ──────────────────────────────────── */
function pwStrength(pw) {
  let s = 0;
  if (pw.length >= 8) s++;
  if (/[A-Z]/.test(pw)) s++;
  if (/[a-z]/.test(pw)) s++;
  if (/[0-9]/.test(pw)) s++;
  if (/[^A-Za-z0-9]/.test(pw)) s++;
  const map = [
    { w: 0,   lbl: "",           col: "" },
    { w: 20,  lbl: "Very Weak",  col: "#ef4444" },
    { w: 40,  lbl: "Weak",       col: "#f59e0b" },
    { w: 60,  lbl: "Fair",       col: "#eab308" },
    { w: 80,  lbl: "Strong",     col: "#10b981" },
    { w: 100, lbl: "Very Strong",col: "#00d4ff" },
  ];
  return map[Math.min(s, 5)];
}

/* ─── Eye toggle ─────────────────────────────────────────── */
function initEyes() {
  const OPEN  = `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>`;
  const CLOSE = `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24"/><line x1="1" y1="1" x2="23" y2="23"/></svg>`;

  document.querySelectorAll(".eye-btn").forEach(btn => {
    const inp = $(btn.dataset.target);
    if (!inp) return;
    btn.innerHTML = OPEN;
    btn.addEventListener("click", () => {
      const hidden = inp.type === "password";
      inp.type    = hidden ? "text" : "password";
      btn.innerHTML = hidden ? CLOSE : OPEN;
      inp.focus();
    });
  });
}

/* ================================================================
   LOGIN PAGE
   ================================================================ */
function initLogin() {
  const form   = $("loginForm");
  if (!form) return;

  const emailIn = $("email");
  const passIn  = $("password");

  function vEmail() {
    if (!v(emailIn))              return setErr(emailIn, "Email is required.");
    if (!RX_EMAIL.test(v(emailIn))) return setErr(emailIn, "Enter a valid email  e.g. user@example.com");
    return clearF(emailIn);
  }
  function vPass() {
    if (!v(passIn)) return setErr(passIn, "Password is required.");
    return clearF(passIn);
  }

  emailIn?.addEventListener("blur",  vEmail);
  emailIn?.addEventListener("input", () => { if (v(emailIn)) vEmail(); });
  passIn?.addEventListener("blur",   vPass);
  passIn?.addEventListener("input",  () => { if (v(passIn)) vPass(); });

  function doLogin() {
    const ok = vEmail() & vPass();
    if (!ok) { form.querySelector(".err")?.focus(); return; }

    const email = v(emailIn).toLowerCase();
    const pw    = passIn.value;

    /* Demo login shortcut */
    if (email === "demo@dsa.com" && pw === "Demo@1234") {
      Shell.session.set({ name: "Demo Student", email });
      redirect();
      return;
    }

    const users = JSON.parse(localStorage.getItem("dsa_users") || "[]");
    const match = users.find(u => u.email === email && u.password === pw);

    if (match) {
      Shell.session.set({ name: match.full_name, email: match.email });
      redirect();
    } else {
      showAlert("loginAlert", "✗  Invalid email or password.  Try: demo@dsa.com / Demo@1234", "error");
    }
  }

  function redirect() {
    const next = new URLSearchParams(location.search).get("next") || "topics.html";
    showAlert("loginAlert", "✓  Login successful — redirecting…", "success");
    setTimeout(() => { location.href = next; }, 900);
  }

  form.addEventListener("submit", e => { e.preventDefault(); doLogin(); });

  $("demoBtn")?.addEventListener("click", () => {
    emailIn.value = "demo@dsa.com";
    passIn.value  = "Demo@1234";
    doLogin();
  });
}

/* ================================================================
   SIGNUP PAGE
   ================================================================ */
function initSignup() {
  const form = $("signupForm");
  if (!form) return;

  const F = {
    name:    $("full_name"),
    email:   $("email"),
    phone:   $("phone"),
    cnic:    $("cnic"),
    dob:     $("dob"),
    pass:    $("password"),
    confirm: $("confirm_password"),
  };

  /* Strength meter */
  const strFill = $("str-fill");
  const strLbl  = $("str-lbl");
  F.pass?.addEventListener("input", () => {
    const s = pwStrength(F.pass.value);
    if (strFill) { strFill.style.width = s.w + "%"; strFill.style.background = s.col; }
    if (strLbl)  { strLbl.textContent = s.lbl; strLbl.style.color = s.col; }
  });

  /* Validators */
  const validators = {
    name:    () => v(F.name).length >= 2 ? clearF(F.name) : setErr(F.name, "Full name is required."),
    email:   () => {
      if (!v(F.email)) return setErr(F.email, "Email is required.");
      if (!RX_EMAIL.test(v(F.email))) return setErr(F.email, "Enter a valid email address.");
      return clearF(F.email);
    },
    phone:   () => RX_PHONE.test(v(F.phone))
                   ? clearF(F.phone)
                   : setErr(F.phone, "Format must be 03XXXXXXXXX (11 digits)."),
    cnic:    () => RX_CNIC.test(v(F.cnic))
                   ? clearF(F.cnic)
                   : setErr(F.cnic, "CNIC must be exactly 13 digits, no dashes."),
    dob:     () => F.dob?.value ? clearF(F.dob) : setErr(F.dob, "Date of birth is required."),
    pass:    () => {
      if (!F.pass?.value)        return setErr(F.pass, "Password is required.");
      if (F.pass.value.length < 8) return setErr(F.pass, "At least 8 characters required.");
      if (pwStrength(F.pass.value).w < 60) return setErr(F.pass, "Too weak — add uppercase, number and symbol.");
      return clearF(F.pass);
    },
    confirm: () => {
      if (!F.confirm?.value)               return setErr(F.confirm, "Please confirm your password.");
      if (F.confirm.value !== F.pass?.value) return setErr(F.confirm, "Passwords do not match.");
      return clearF(F.confirm);
    },
  };

  Object.entries(F).forEach(([k, inp]) => {
    if (!inp || !validators[k]) return;
    inp.addEventListener("blur",  validators[k]);
    inp.addEventListener("input", () => { if (v(inp) || k==="dob") validators[k](); });
  });

  form.addEventListener("submit", e => {
    e.preventDefault();
    const allOk = Object.values(validators).map(fn => fn()).every(Boolean);
    if (!allOk) { form.querySelector(".err")?.focus(); return; }

    /* Age check (≥ 15) */
    const dob   = new Date(F.dob.value);
    const today = new Date();
    let age = today.getFullYear() - dob.getFullYear();
    if (today.getMonth() < dob.getMonth() ||
        (today.getMonth() === dob.getMonth() && today.getDate() < dob.getDate())) age--;
    if (age < 15) {
      showAlert("signupAlert", "✗  You must be at least 15 years old to register.", "error");
      return;
    }

    const users = JSON.parse(localStorage.getItem("dsa_users") || "[]");
    if (users.find(u => u.email === v(F.email).toLowerCase())) {
      showAlert("signupAlert", "✗  An account with this email already exists.", "error");
      return;
    }

    users.push({
      full_name: v(F.name),
      email:     v(F.email).toLowerCase(),
      phone:     v(F.phone),
      cnic:      v(F.cnic),
      dob:       F.dob.value,
      password:  F.pass.value,
    });
    localStorage.setItem("dsa_users", JSON.stringify(users));
    showAlert("signupAlert", "✓  Account created! Redirecting to login…", "success");
    setTimeout(() => { location.href = "login.html"; }, 1200);
  });
}

/* ─── Boot ────────────────────────────────────────────────── */
document.addEventListener("DOMContentLoaded", () => {
  initEyes();
  initLogin();
  initSignup();
});