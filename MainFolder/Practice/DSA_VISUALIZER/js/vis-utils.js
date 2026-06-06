/* ================================================================
   vis-utils.js  —  Shared visualizer utilities
   Author : Easha Akram
   ================================================================ */

/* ── Parse comma-separated int array ─────────────────────── */
function parseArray(str, sorted = false) {
  const a = str.split(",").map(s => parseInt(s.trim(), 10)).filter(n => !isNaN(n));
  return sorted ? [...a].sort((x,y) => x-y) : a;
}

/* ── Render bar array ─────────────────────────────────────── */
function renderBars(containerId, arr, opts = {}) {
  const { 
    hi = new Set(),           // highlight (comparing)
    found = new Set(),        // found element
    range = null,             // range highlight
    sorted = new Set(),       // sorted elements
    swapping = null,          // [index1, index2] for swap animation
    active = new Set(),       // active elements
    comparing = new Set()     // comparing elements
  } = opts;
  
  const c = document.getElementById(containerId);
  if (!c) return;
  if (!arr.length) { 
    c.innerHTML = `<div class="empty-st">Empty</div>`; 
    return; 
  }
  
  c.innerHTML = arr.map((val, i) => {
    let cls = "bar-box";
    
    // Check for swapping (highest priority)
    if (swapping && (swapping[0] === i || swapping[1] === i)) {
      cls += " swapping";
    }
    // Check for comparing
    else if (comparing.has(i)) {
      cls += " comparing";
    }
    // Check for active
    else if (active.has(i)) {
      cls += " hi";
    }
    // Check for found
    else if (found.has(i)) {
      cls += " found";
    }
    // Check for sorted
    else if (sorted.has(i)) {
      cls += " sorted";
    }
    // Check for range
    else if (range && i >= range[0] && i <= range[1]) {
      cls += " range";
    }
    // Check for hi (backward compatibility)
    else if (hi.has(i)) {
      cls += " hi";
    }
    
    return `<div class="arr-bar">
      <div class="${cls}">${val}</div>
      <div class="bar-idx">[${i}]</div>
    </div>`;
  }).join("");
}

/* ── Sleep ────────────────────────────────────────────────── */
const sleep = ms => new Promise(r => setTimeout(r, ms));

/* ── Status message ──────────────────────────────────────── */
function setStatus(elId, msg, type = "info") {
  const el = document.getElementById(elId);
  if (!el) return;
  el.className = `vis-status vs-${type}`;
  el.textContent = msg;
}

/* ── Stat chip value ─────────────────────────────────────── */
function setStat(id, val) {
  const el = document.getElementById(id);
  if (el) el.textContent = val;
}

/* ── Speed slider → ms delay ─────────────────────────────── */
function speedMs(sliderVal) {
  return Math.round(1500 - Number(sliderVal) * 1400); // ~100ms – ~1500ms
}

/* ── Render linked list / queue nodes ────────────────────── */
function renderNodes(containerId, nodes, opts = {}) {
  const { front = -1, rear = -1 } = opts;
  const c = document.getElementById(containerId);
  if (!c) return;
  if (!nodes.length) { c.innerHTML = `<div class="empty-st">Empty</div>`; return; }
  c.innerHTML = nodes.map((v, i) => {
    const isFront = i === front && front !== -1;
    const isRear  = i === rear  && rear  !== -1;
    const cls = "node-box" + (isFront ? " n-front" : isRear ? " n-rear" : "");
    const lbl = isFront ? "FRONT" : isRear ? "REAR" : "";
    const arrow = (i < nodes.length - 1) ? `<span class="narr">→</span>` : "";
    return `<div class="${cls}">
      ${lbl ? `<div class="nlbl">${lbl}</div>` : ""}
      ${v !== null && v !== undefined ? v : ""}
    </div>${arrow}`;
  }).join("");
}