/* ================================================================
   shell.js  —  Header · Footer · Session · Auth-guard
   Author : Easha Akram
   ================================================================

   USAGE: add <script src="js/shell.js"></script> at the END of <body>.

   Pages call Shell.init({ guard: true }) if they require login.
   ================================================================ */

const INSTRUCTOR = "Easha Akram";
const YEAR       = new Date().getFullYear();

/* ── Session helpers  ───── */
const Session = {
  get()  { try { return JSON.parse(localStorage.getItem("dsa_session")); } catch { return null; } },
  set(u) { localStorage.setItem("dsa_session", JSON.stringify(u)); },
  clear(){ localStorage.removeItem("dsa_session"); },
};

/* ── Current page filename ────────────────────────────────── */
function currentFile() {
  return location.pathname.split("/").pop() || "index.html";
}

/* ── Relative path prefix ─────────────────────────────────── */
function base() {
  return "";
}

/* ── Build Header ─────────────────────────────────────────── */
function buildHeader() {
  const user = Session.get();
  const cur  = currentFile();
  const B    = base();

  // For login/signup pages - show simplified header
  if (cur === 'login.html' || cur === 'signup.html') {
    return `
<header id="site-header" role="banner">
  <a href="${B}index.html" class="hd-brand" aria-label="DSA Learn home">
    <div class="brand-box" aria-hidden="true">EA</div>
    <span>DSA&nbsp;<span class="accent">Learn</span></span>
  </a>
  <div class="hd-instructor" aria-label="Instructor">
    <div class="inst-dot" aria-hidden="true"></div>
    Instructor : <strong>${INSTRUCTOR}</strong>
  </div>
</header>`;
  }

  // For index.html - show simplified header (no auth buttons)
  if (cur === 'index.html') {
    return `
<header id="site-header" role="banner">
  <a href="${B}index.html" class="hd-brand" aria-label="DSA Learn home">
    <div class="brand-box" aria-hidden="true">EA</div>
    <span>DSA&nbsp;<span class="accent">Learn</span></span>
  </a>
  <div class="hd-instructor" aria-label="Instructor">
    <div class="inst-dot" aria-hidden="true"></div>
    Instructor : <strong>${INSTRUCTOR}</strong>
  </div>
</header>`;
  }

  // Navigation links for logged in users
  let linksHTML = '';
  if (user) {
    const navLinks = [
      { file: "topics.html",     label: " Topics"     },
      { file: "sorting.html",    label: " Sorting"    },
      { file: "searching.html",  label: " Searching"  },
      { file: "linkedlist.html", label: " Linked List" },
      { file: "queue.html",      label: " Queue"      },
      { file: "trees.html",      label: " Trees"      },
    ];
    linksHTML = `<ul class="hd-nav" role="list">${
      navLinks.map(l =>
        `<li><a href="${B}${l.file}" class="${cur === l.file ? "active" : ""}">${l.label}</a></li>`
      ).join("")
    }</ul>`;
  }

  // Auth buttons
  let authHTML = '';
  if (user) {
    authHTML = `<div class="hd-auth">
      <span class="user-greeting">👋 ${user.name?.split(" ")[0] || user.email?.split("@")[0]}</span>
      <button class="btn btn-outline btn-sm" id="hd-logout-btn">🚪 Sign out</button>
    </div>`;
  } else if (cur !== 'login.html' && cur !== 'signup.html' && cur !== 'index.html') {
    authHTML = `<div class="hd-auth">
      <a href="${B}login.html" class="btn btn-outline btn-sm">🔐 Log in</a>
      <a href="${B}signup.html" class="btn btn-primary btn-sm">📝 Sign up</a>
    </div>`;
  }

  // Regular header for protected pages
  return `
<header id="site-header" role="banner">
  <a href="${B}index.html" class="hd-brand" aria-label="DSA Learn home">
    <div class="brand-box" aria-hidden="true">EA</div>
    <span>DSA&nbsp;<span class="accent">Learn</span></span>
  </a>
  ${linksHTML}
  <div class="hd-instructor" aria-label="Instructor">
    <div class="inst-dot" aria-hidden="true"></div>
    Instructor : <strong>${INSTRUCTOR}</strong>
  </div>
  ${authHTML}
</header>`;
}

/* ── Build Footer ─────────────────────────────────────────── */
function buildFooter() {
  const cur = currentFile();
  const B = base();
  
  // For login/signup pages - simplified footer
  if (cur === 'login.html' || cur === 'signup.html') {
    return `
<footer id="site-footer" role="contentinfo">
  <span class="ft-brand">DSA&nbsp;<span>Learn</span></span>
  <span>© ${YEAR} &nbsp;·&nbsp; Developed by <strong style="color:var(--cyan)">Easha Akram</strong></span>
  <div class="ft-right">
    <span style="font-family:var(--mono);font-size:.7rem;color:var(--text-3)">Interactive DSA Visualizer</span>
  </div>
</footer>`;
  }
  
  // Full footer for other pages
  return `
<footer id="site-footer" role="contentinfo">
  <div class="footer-content">
    <div class="footer-brand">
      <span class="ft-brand">DSA&nbsp;<span>Learn</span></span>
      <p class="footer-desc">Interactive Data Structures & Algorithms Visualizer</p>
    </div>
    <div class="footer-links">
      <div class="footer-col">
        <h4>Algorithms</h4>
        <a href="${B}sorting.html">Sorting</a>
        <a href="${B}searching.html">Searching</a>
      </div>
      <div class="footer-col">
        <h4>Data Structures</h4>
        <a href="${B}linkedlist.html">Linked List</a>
        <a href="${B}queue.html">Queue</a>
        <a href="${B}trees.html">Trees</a>
      </div>
      <div class="footer-col">
        <h4>Account</h4>
        <a href="${B}login.html">Login</a>
        <a href="${B}signup.html">Sign Up</a>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© ${YEAR} &nbsp;·&nbsp; Developed by <strong style="color:var(--cyan)">Easha Akram</strong></span>
      <span class="ft-version">v2.0</span>
    </div>
  </div>
</footer>`;
}

/* ── Mount header and footer ──────────────────────────────── */
function mountShell() {
  // Remove existing header/footer if any (to avoid duplicates)
  const existingHeader = document.getElementById('site-header');
  const existingFooter = document.getElementById('site-footer');
  if (existingHeader) existingHeader.remove();
  if (existingFooter) existingFooter.remove();
  
  // Insert header at the beginning
  document.body.insertAdjacentHTML("afterbegin", buildHeader());

  // Insert footer at the end
  document.body.insertAdjacentHTML("beforeend", buildFooter());

  // Logout button handler
  const logoutBtn = document.getElementById("hd-logout-btn");
  if (logoutBtn) {
    logoutBtn.addEventListener("click", (e) => {
      e.preventDefault();
      Session.clear();
      location.href = base() + "index.html";
    });
  }
}

/* ── Auth guard (protects pages that need login) ──────────── */
function authGuard() {
  const session = Session.get();
  const cur = currentFile();
  const protectedPages = ['topics.html', 'sorting.html', 'searching.html', 'linkedlist.html', 'queue.html', 'trees.html'];
  
  if (protectedPages.includes(cur)) {
    if (!session || !session.email) {
      location.href = base() + "login.html?next=" + encodeURIComponent(cur);
      return false;
    }
  }
  return true;
}

/* ── Public API ───────────────────────────────────────────── */
const Shell = {
  init(opts = {}) {
    if (opts.guard) {
      const allowed = authGuard();
      if (!allowed) return;
    }
    if (document.readyState === 'loading') {
      document.addEventListener("DOMContentLoaded", mountShell);
    } else {
      mountShell();
    }
  },
  session: Session,
  INSTRUCTOR,
};