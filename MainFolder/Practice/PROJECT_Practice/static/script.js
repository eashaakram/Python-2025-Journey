/**
 * static/script.js  –  Esha Aqram | DSA Learning Platform
 * Real-time form validation + UI interactions
 */

/* ── Helpers ───────────────────────────────────────────────── */

const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

/**
 * Show an error message below an input.
 * @param {HTMLElement} input
 * @param {string}      message   – pass "" to clear
 */
function setError(input, message) {
  const wrapper = input.closest('.form-group') || input.parentElement;
  let errEl = wrapper.querySelector('.form-error');
  if (!errEl) {
    errEl = document.createElement('span');
    errEl.className = 'form-error';
    input.closest('.input-wrapper')
      ? input.closest('.input-wrapper').insertAdjacentElement('afterend', errEl)
      : input.insertAdjacentElement('afterend', errEl);
  }

  if (message) {
    errEl.innerHTML = `<svg width="11" height="11" viewBox="0 0 16 16" fill="currentColor">
      <path d="M8 1a7 7 0 1 0 0 14A7 7 0 0 0 8 1zm0 3.5a.75.75 0 0 1 .75.75v3.5a.75.75 0 0 1-1.5 0v-3.5A.75.75 0 0 1 8 4.5zm0 7a.875.875 0 1 1 0-1.75.875.875 0 0 1 0 1.75z"/>
    </svg>${message}`;
    errEl.classList.add('visible');
    input.classList.remove('is-valid');
    input.classList.add('is-invalid');
  } else {
    errEl.classList.remove('visible');
    input.classList.remove('is-invalid');
  }
}

function setValid(input) {
  setError(input, '');
  input.classList.add('is-valid');
}

/* ── Password Visibility Toggle ───────────────────────────── */

function initPasswordToggles() {
  document.querySelectorAll('.toggle-password').forEach(btn => {
    const targetId = btn.dataset.target;
    const input    = document.getElementById(targetId);
    if (!input) return;

    const eyeOpen = `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/>
    </svg>`;
    const eyeClosed = `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24"/>
      <line x1="1" y1="1" x2="23" y2="23"/>
    </svg>`;

    btn.innerHTML = eyeOpen;

    btn.addEventListener('click', () => {
      const isHidden = input.type === 'password';
      input.type     = isHidden ? 'text' : 'password';
      btn.innerHTML  = isHidden ? eyeClosed : eyeOpen;
      btn.setAttribute('aria-label', isHidden ? 'Hide password' : 'Show password');
      input.focus();
    });
  });
}

/* ── Password Strength Meter ──────────────────────────────── */

function getPasswordStrength(password) {
  if (!password) return { score: 0, label: '', color: '' };

  let score = 0;
  if (password.length >= 6)  score++;
  if (password.length >= 10) score++;
  if (/[A-Z]/.test(password)) score++;
  if (/[0-9]/.test(password)) score++;
  if (/[^A-Za-z0-9]/.test(password)) score++;

  const levels = [
    { label: '',          color: '' },
    { label: 'Weak',      color: '#f85149' },
    { label: 'Fair',      color: '#d29922' },
    { label: 'Good',      color: '#58a6ff' },
    { label: 'Strong',    color: '#39d353' },
    { label: 'Very Strong', color: '#39d353' },
  ];

  return { score, ...levels[Math.min(score, 5)] };
}

function updateStrengthMeter(input) {
  const wrapper  = input.closest('.form-group');
  if (!wrapper)  return;

  let bar   = wrapper.querySelector('.strength-bar-fill');
  let label = wrapper.querySelector('.strength-label');
  if (!bar || !label) return;

  const { score, label: lbl, color } = getPasswordStrength(input.value);
  const pct = Math.min((score / 5) * 100, 100);

  bar.style.width           = pct + '%';
  bar.style.backgroundColor = color || 'transparent';
  label.textContent         = lbl;
  label.style.color         = color || 'var(--text-muted)';
}

/* ── Email Validation ─────────────────────────────────────── */

function validateEmail(input) {
  const val = input.value.trim();
  if (!val) {
    setError(input, 'Email address is required.');
    return false;
  }
  if (!EMAIL_RE.test(val)) {
    setError(input, 'Enter a valid email  (e.g. user@example.com)');
    return false;
  }
  setValid(input);
  return true;
}

/* ── Password Validation ──────────────────────────────────── */

function validatePassword(input) {
  const val = input.value;
  if (!val) {
    setError(input, 'Password is required.');
    return false;
  }
  if (val.length < 6) {
    setError(input, 'Password must be at least 6 characters.');
    return false;
  }
  setValid(input);
  return true;
}

/* ── Username Validation ──────────────────────────────────── */

function validateUsername(input) {
  const val = input.value.trim();
  if (!val) {
    setError(input, 'Username is required.');
    return false;
  }
  if (val.length < 3) {
    setError(input, 'Username must be at least 3 characters.');
    return false;
  }
  if (!/^[a-zA-Z0-9_]+$/.test(val)) {
    setError(input, 'Only letters, numbers, and underscores.');
    return false;
  }
  setValid(input);
  return true;
}

/* ── Login Form ────────────────────────────────────────────── */

function initLoginForm() {
  const form     = document.getElementById('loginForm');
  if (!form)     return;

  const emailIn  = document.getElementById('email');
  const passIn   = document.getElementById('password');

  // real-time events
  if (emailIn) {
    emailIn.addEventListener('input',  () => { if (emailIn.value) validateEmail(emailIn); });
    emailIn.addEventListener('blur',   () => validateEmail(emailIn));
  }
  if (passIn) {
    passIn.addEventListener('input',  () => { if (passIn.value) validatePassword(passIn); });
    passIn.addEventListener('blur',   () => validatePassword(passIn));
  }

  form.addEventListener('submit', e => {
    const v1 = validateEmail(emailIn);
    const v2 = validatePassword(passIn);
    if (!v1 || !v2) {
      e.preventDefault();
      const firstInvalid = form.querySelector('.is-invalid');
      if (firstInvalid) firstInvalid.focus();
    }
  });
}

/* ── Signup Form ───────────────────────────────────────────── */

function initSignupForm() {
  const form    = document.getElementById('signupForm');
  if (!form)    return;

  const userIn  = document.getElementById('username');
  const emailIn = document.getElementById('email');
  const passIn  = document.getElementById('password');

  let emailDebounceTimer = null;

  if (userIn) {
    userIn.addEventListener('input', () => { if (userIn.value) validateUsername(userIn); });
    userIn.addEventListener('blur',  () => validateUsername(userIn));
  }

  if (emailIn) {
    emailIn.addEventListener('input', () => {
      if (!emailIn.value) return;
      validateEmail(emailIn);
      // debounce server-side duplicate check
      clearTimeout(emailDebounceTimer);
      emailDebounceTimer = setTimeout(() => {
        if (!EMAIL_RE.test(emailIn.value)) return;
        fetch('/api/validate-email', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ email: emailIn.value.trim().toLowerCase() })
        })
        .then(r => r.json())
        .then(data => {
          if (data.taken) setError(emailIn, 'An account with this email already exists.');
        })
        .catch(() => { /* network errors: ignore, server validates anyway */ });
      }, 600);
    });
    emailIn.addEventListener('blur', () => validateEmail(emailIn));
  }

  if (passIn) {
    passIn.addEventListener('input', () => {
      validatePassword(passIn);
      updateStrengthMeter(passIn);
    });
    passIn.addEventListener('blur', () => validatePassword(passIn));
  }

  form.addEventListener('submit', e => {
    const v1 = userIn  ? validateUsername(userIn)  : true;
    const v2 = emailIn ? validateEmail(emailIn)    : true;
    const v3 = passIn  ? validatePassword(passIn)  : true;

    if (!v1 || !v2 || !v3) {
      e.preventDefault();
      const firstInvalid = form.querySelector('.is-invalid');
      if (firstInvalid) firstInvalid.focus();
    }
  });
}

/* ── Mark Topic Complete (Dashboard / Topic page) ─────────── */

function initProgressButtons() {
  document.querySelectorAll('[data-complete-btn]').forEach(btn => {
    btn.addEventListener('click', async () => {
      const topicId  = parseInt(btn.dataset.topicId, 10);
      const complete = btn.dataset.state !== 'completed';

      btn.disabled = true;
      btn.classList.add('btn--loading');

      try {
        const res = await fetch('/api/progress', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ topic_id: topicId, completed: complete })
        });

        if (res.ok) {
          btn.dataset.state = complete ? 'completed' : 'pending';

          if (complete) {
            btn.textContent = '✓  Completed';
            btn.classList.replace('btn-outline', 'btn-primary');
          } else {
            btn.textContent = 'Mark as Complete';
            btn.classList.replace('btn-primary', 'btn-outline');
          }

          // update dot if on dashboard
          const dot = document.querySelector(`[data-dot="${topicId}"]`);
          if (dot) dot.style.display = complete ? 'block' : 'none';

          // update progress bar
          updateProgressBar();
        }
      } catch (err) {
        console.error(err);
      } finally {
        btn.disabled = false;
        btn.classList.remove('btn--loading');
      }
    });
  });
}

function updateProgressBar() {
  const total  = parseInt(document.getElementById('totalTopics')?.textContent  || '0', 10);
  const doneEl = document.getElementById('completedTopics');
  if (!doneEl || !total) return;

  let done = document.querySelectorAll('[data-complete-btn][data-state="completed"]').length;
  doneEl.textContent = done;

  const pct = total ? Math.round((done / total) * 100) : 0;
  const bar = document.querySelector('.progress-bar-fill');
  if (bar) bar.style.width = pct + '%';

  const pctEl = document.getElementById('progressPct');
  if (pctEl) pctEl.textContent = pct + '%';
}

/* ── Flash message auto-dismiss ──────────────────────────── */

function initFlashMessages() {
  document.querySelectorAll('.alert[data-auto-dismiss]').forEach(el => {
    setTimeout(() => {
      el.style.transition = 'opacity 0.4s ease';
      el.style.opacity    = '0';
      setTimeout(() => el.remove(), 400);
    }, 4000);
  });
}

/* ── Init on DOM ready ────────────────────────────────────── */

document.addEventListener('DOMContentLoaded', () => {
  initPasswordToggles();
  initLoginForm();
  initSignupForm();
  initProgressButtons();
  initFlashMessages();
});
