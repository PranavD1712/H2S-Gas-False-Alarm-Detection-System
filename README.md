<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>H2S False Alarm Detection System</title>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Syne:wght@400;600;700;800&family=Inter:wght@300;400;500&display=swap" rel="stylesheet">
<style>
  :root {
    --bg: #080c10;
    --surface: #0d1318;
    --surface2: #111820;
    --border: #1e2d3a;
    --accent: #00d4ff;
    --accent2: #ff6b35;
    --accent3: #39ff14;
    --danger: #ff3b3b;
    --safe: #39ff14;
    --text: #e2eaf2;
    --muted: #5a7a8a;
    --heading: #ffffff;
  }

  * { margin: 0; padding: 0; box-sizing: border-box; }

  html { scroll-behavior: smooth; }

  body {
    font-family: 'Inter', sans-serif;
    background: var(--bg);
    color: var(--text);
    line-height: 1.7;
    overflow-x: hidden;
  }

  /* Animated background grid */
  body::before {
    content: '';
    position: fixed;
    inset: 0;
    background-image: 
      linear-gradient(rgba(0,212,255,0.03) 1px, transparent 1px),
      linear-gradient(90deg, rgba(0,212,255,0.03) 1px, transparent 1px);
    background-size: 40px 40px;
    pointer-events: none;
    z-index: 0;
  }

  .container {
    max-width: 960px;
    margin: 0 auto;
    padding: 0 24px;
    position: relative;
    z-index: 1;
  }

  /* \u2500\u2500 HERO \u2500\u2500 */
  .hero {
    padding: 80px 0 60px;
    text-align: center;
    position: relative;
  }

  .hero-glow {
    position: absolute;
    top: 0; left: 50%;
    transform: translateX(-50%);
    width: 600px; height: 300px;
    background: radial-gradient(ellipse, rgba(0,212,255,0.12) 0%, transparent 70%);
    pointer-events: none;
  }

  .badge-row {
    display: flex;
    justify-content: center;
    gap: 8px;
    flex-wrap: wrap;
    margin-bottom: 32px;
  }

  .badge {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    padding: 4px 12px;
    border-radius: 4px;
    border: 1px solid;
    letter-spacing: 0.5px;
  }
  .badge-blue { color: #60a5fa; border-color: rgba(96,165,250,0.3); background: rgba(96,165,250,0.06); }
  .badge-green { color: #4ade80; border-color: rgba(74,222,128,0.3); background: rgba(74,222,128,0.06); }
  .badge-orange { color: #fb923c; border-color: rgba(251,146,60,0.3); background: rgba(251,146,60,0.06); }

  .hero-eyebrow {
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    color: var(--accent);
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 20px;
  }

  .hero h1 {
    font-family: 'Syne', sans-serif;
    font-size: clamp(2rem, 5vw, 3.4rem);
    font-weight: 800;
    color: var(--heading);
    line-height: 1.1;
    margin-bottom: 20px;
    letter-spacing: -1px;
  }

  .hero h1 span {
    background: linear-gradient(90deg, var(--accent), #7c3aed);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
  }

  .hero-sub {
    font-size: 16px;
    color: var(--muted);
    max-width: 560px;
    margin: 0 auto 36px;
    font-weight: 300;
  }

  .nav-pills {
    display: flex;
    justify-content: center;
    gap: 6px;
    flex-wrap: wrap;
  }

  .nav-pill {
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    color: var(--accent);
    border: 1px solid rgba(0,212,255,0.25);
    padding: 6px 16px;
    border-radius: 100px;
    text-decoration: none;
    transition: all 0.2s;
    background: rgba(0,212,255,0.04);
  }
  .nav-pill:hover {
    background: rgba(0,212,255,0.12);
    border-color: var(--accent);
  }

  /* \u2500\u2500 DIVIDER \u2500\u2500 */
  .divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--border), transparent);
    margin: 0;
  }

  /* \u2500\u2500 SECTION \u2500\u2500 */
  section {
    padding: 64px 0;
    border-bottom: 1px solid var(--border);
  }

  .section-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    color: var(--accent);
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 12px;
  }

  h2 {
    font-family: 'Syne', sans-serif;
    font-size: clamp(1.4rem, 3vw, 2rem);
    font-weight: 700;
    color: var(--heading);
    margin-bottom: 24px;
    letter-spacing: -0.5px;
  }

  h3 {
    font-family: 'Syne', sans-serif;
    font-size: 1.1rem;
    font-weight: 600;
    color: var(--heading);
    margin-bottom: 12px;
  }

  p { color: var(--text); margin-bottom: 16px; font-weight: 300; }

  /* \u2500\u2500 PROBLEM CARDS \u2500\u2500 */
  .problem-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 16px;
    margin-top: 32px;
  }

  .problem-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 20px;
    position: relative;
    overflow: hidden;
  }

  .problem-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, var(--danger), transparent);
  }

  .problem-icon { font-size: 20px; margin-bottom: 10px; }
  .problem-card p { font-size: 14px; color: var(--muted); margin: 0; }

  /* \u2500\u2500 SOLUTION FLOW \u2500\u2500 */
  .pipeline {
    display: flex;
    align-items: center;
    gap: 0;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 20px 24px;
    overflow-x: auto;
    margin: 24px 0;
    flex-wrap: wrap;
    gap: 4px;
  }

  .pipeline-step {
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    color: var(--accent);
    white-space: nowrap;
    padding: 6px 12px;
    background: rgba(0,212,255,0.06);
    border: 1px solid rgba(0,212,255,0.15);
    border-radius: 6px;
  }

  .pipeline-arrow {
    color: var(--muted);
    font-size: 16px;
    padding: 0 4px;
    flex-shrink: 0;
  }

  /* \u2500\u2500 FEATURE GRID \u2500\u2500 */
  .feature-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 20px;
    margin-top: 32px;
  }

  .feature-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 24px;
    transition: border-color 0.2s, transform 0.2s;
  }

  .feature-card:hover {
    border-color: rgba(0,212,255,0.3);
    transform: translateY(-2px);
  }

  .feature-icon {
    font-size: 24px;
    margin-bottom: 14px;
  }

  .feature-card p { font-size: 14px; color: var(--muted); margin: 0; }

  .param-list {
    list-style: none;
    margin-top: 12px;
  }

  .param-list li {
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    color: var(--muted);
    padding: 4px 0;
    border-bottom: 1px solid rgba(255,255,255,0.04);
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .param-list li::before {
    content: '\u25b8';
    color: var(--accent);
    font-size: 10px;
  }

  /* \u2500\u2500 TECH TABLE \u2500\u2500 */
  .tech-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
    gap: 12px;
    margin-top: 24px;
  }

  .tech-chip {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 12px 16px;
    text-align: center;
  }

  .tech-cat {
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 6px;
  }

  .tech-name {
    font-size: 13px;
    font-weight: 500;
    color: var(--text);
  }

  /* \u2500\u2500 METRICS \u2500\u2500 */
  .metrics-row {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 16px;
    margin: 32px 0;
  }

  @media (max-width: 600px) {
    .metrics-row { grid-template-columns: repeat(2, 1fr); }
  }

  .metric-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 24px 16px;
    text-align: center;
    position: relative;
    overflow: hidden;
  }

  .metric-card::after {
    content: '';
    position: absolute;
    bottom: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, var(--accent3), var(--accent));
  }

  .metric-val {
    font-family: 'Syne', sans-serif;
    font-size: 2rem;
    font-weight: 800;
    color: var(--accent3);
    line-height: 1;
    margin-bottom: 6px;
  }

  .metric-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: 1px;
  }

  /* \u2500\u2500 CODE BLOCKS \u2500\u2500 */
  .code-block {
    background: #060a0d;
    border: 1px solid var(--border);
    border-radius: 10px;
    overflow: hidden;
    margin: 20px 0;
  }

  .code-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 10px 16px;
    background: var(--surface);
    border-bottom: 1px solid var(--border);
  }

  .code-dots { display: flex; gap: 6px; }
  .code-dot {
    width: 10px; height: 10px;
    border-radius: 50%;
  }
  .dot-r { background: #ff5f57; }
  .dot-y { background: #febc2e; }
  .dot-g { background: #28c840; }

  .code-lang {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    color: var(--muted);
    letter-spacing: 1px;
  }

  pre {
    padding: 20px;
    overflow-x: auto;
    font-family: 'JetBrains Mono', monospace;
    font-size: 13px;
    line-height: 1.7;
    color: #8fbcbb;
  }

  .k { color: #81a1c1; }
  .s { color: #a3be8c; }
  .c { color: #4c566a; }
  .n { color: #88c0d0; }
  .p { color: #d8dee9; }

  /* \u2500\u2500 API ENDPOINT \u2500\u2500 */
  .endpoint {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    overflow: hidden;
    margin: 24px 0;
  }

  .endpoint-header {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 16px 20px;
    background: var(--surface2);
    border-bottom: 1px solid var(--border);
  }

  .method {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    font-weight: 700;
    padding: 4px 10px;
    border-radius: 4px;
    letter-spacing: 1px;
  }
  .get { background: rgba(74,222,128,0.15); color: #4ade80; }
  .post { background: rgba(96,165,250,0.15); color: #60a5fa; }

  .path {
    font-family: 'JetBrains Mono', monospace;
    font-size: 14px;
    color: var(--text);
  }

  .endpoint-desc {
    padding: 16px 20px;
    font-size: 14px;
    color: var(--muted);
    border-bottom: 1px solid var(--border);
  }

  /* \u2500\u2500 FIELDS TABLE \u2500\u2500 */
  .field-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 13px;
    margin: 16px 0;
  }

  .field-table th {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: 1px;
    padding: 10px 16px;
    text-align: left;
    border-bottom: 1px solid var(--border);
    background: var(--surface2);
  }

  .field-table td {
    padding: 10px 16px;
    border-bottom: 1px solid rgba(30,45,58,0.5);
    color: var(--text);
    vertical-align: top;
  }

  .field-table tr:last-child td { border-bottom: none; }
  .field-table tr:hover td { background: rgba(255,255,255,0.01); }

  .field-name {
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    color: var(--accent);
  }

  .field-type {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    color: #fb923c;
    background: rgba(251,146,60,0.08);
    padding: 2px 6px;
    border-radius: 4px;
    white-space: nowrap;
  }

  /* \u2500\u2500 PROJECT TREE \u2500\u2500 */
  .file-tree {
    background: #060a0d;
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 24px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 13px;
    line-height: 2;
    color: var(--text);
  }

  .tree-dir { color: #60a5fa; }
  .tree-file { color: var(--muted); }
  .tree-comment { color: #2a3f50; }

  /* \u2500\u2500 IMPACT TABLE \u2500\u2500 */
  .impact-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 16px;
    margin: 32px 0;
  }

  .impact-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 20px;
  }

  .impact-before {
    font-size: 12px;
    color: var(--danger);
    margin-bottom: 4px;
  }

  .impact-after {
    font-size: 12px;
    color: var(--safe);
    margin-bottom: 12px;
  }

  .impact-improvement {
    font-family: 'Syne', sans-serif;
    font-size: 1.6rem;
    font-weight: 800;
    color: var(--accent3);
    line-height: 1;
    margin-bottom: 4px;
  }

  .impact-label {
    font-size: 13px;
    color: var(--muted);
  }

  /* \u2500\u2500 BENEFIT LIST \u2500\u2500 */
  .benefit-list {
    list-style: none;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 10px;
    margin-top: 16px;
  }

  .benefit-list li {
    display: flex;
    align-items: flex-start;
    gap: 10px;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 12px 16px;
    font-size: 14px;
  }

  .benefit-list li .check { color: var(--accent3); font-size: 16px; flex-shrink: 0; margin-top: 1px; }

  /* \u2500\u2500 FUTURE \u2500\u2500 */
  .future-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 10px;
    margin-top: 24px;
  }

  .future-item {
    display: flex;
    align-items: center;
    gap: 12px;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 12px 16px;
    font-size: 14px;
    color: var(--muted);
  }

  .future-box {
    width: 14px; height: 14px;
    border: 1px solid var(--border);
    border-radius: 3px;
    flex-shrink: 0;
  }

  /* \u2500\u2500 INSTALL STEPS \u2500\u2500 */
  .install-steps {
    counter-reset: step;
    display: flex;
    flex-direction: column;
    gap: 16px;
    margin-top: 24px;
  }

  .install-step {
    display: flex;
    gap: 16px;
    align-items: flex-start;
  }

  .step-num {
    counter-increment: step;
    width: 32px; height: 32px;
    border-radius: 50%;
    background: rgba(0,212,255,0.1);
    border: 1px solid rgba(0,212,255,0.3);
    color: var(--accent);
    font-family: 'JetBrains Mono', monospace;
    font-size: 13px;
    font-weight: 700;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    margin-top: 2px;
  }

  .step-content { flex: 1; }
  .step-content h4 {
    font-family: 'Syne', sans-serif;
    font-weight: 600;
    color: var(--heading);
    margin-bottom: 8px;
  }

  /* \u2500\u2500 FOOTER \u2500\u2500 */
  footer {
    padding: 48px 0;
    text-align: center;
    position: relative;
    z-index: 1;
  }

  .footer-name {
    font-family: 'Syne', sans-serif;
    font-size: 1.3rem;
    font-weight: 700;
    color: var(--heading);
    margin-bottom: 4px;
  }

  .footer-role {
    font-size: 13px;
    color: var(--muted);
    margin-bottom: 24px;
  }

  .star-cta {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(0,212,255,0.08);
    border: 1px solid rgba(0,212,255,0.25);
    color: var(--accent);
    padding: 10px 24px;
    border-radius: 100px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 13px;
    cursor: pointer;
    text-decoration: none;
    transition: all 0.2s;
  }

  .star-cta:hover {
    background: rgba(0,212,255,0.15);
    border-color: var(--accent);
  }

  .heart { color: var(--danger); }

  /* \u2500\u2500 RESPONSIVE \u2500\u2500 */
  @media (max-width: 640px) {
    .hero { padding: 48px 0 40px; }
    section { padding: 48px 0; }
    .pipeline { flex-direction: column; align-items: flex-start; }
    .pipeline-arrow { transform: rotate(90deg); }
    pre { font-size: 11px; }
    .field-table { font-size: 12px; }
    .field-table th, .field-table td { padding: 8px 10px; }
  }

  @media (max-width: 480px) {
    .metrics-row { grid-template-columns: repeat(2, 1fr); }
    .problem-grid { grid-template-columns: 1fr 1fr; }
  }

  /* Scroll fade-in animation */
  .fade-in {
    opacity: 0;
    transform: translateY(20px);
    transition: opacity 0.5s ease, transform 0.5s ease;
  }
  .fade-in.visible {
    opacity: 1;
    transform: translateY(0);
  }
</style>
</head>
<body>

<!-- \u2500\u2500 HERO \u2500\u2500 -->
<div class="hero">
  <div class="hero-glow"></div>
  <div class="container">
    <div class="badge-row">
      <span class="badge badge-blue">Python 3.8+</span>
      <span class="badge badge-green">Flask 2.0+</span>
      <span class="badge badge-orange">Scikit-learn 1.0+</span>
    </div>
    <p class="hero-eyebrow">Machine Learning \u00b7 Safety Systems</p>
    <h1>H2S False Alarm<br><span>Detection System</span></h1>
    <p class="hero-sub">ML-powered API to classify H2S gas leak alarms as dangerous or false, reducing unnecessary emergency responses in chemical manufacturing.</p>
    <div class="nav-pills">
      <a href="#problem" class="nav-pill">Problem</a>
      <a href="#solution" class="nav-pill">Solution</a>
      <a href="#features" class="nav-pill">Features</a>
      <a href="#performance" class="nav-pill">Performance</a>
      <a href="#install" class="nav-pill">Installation</a>
      <a href="#api" class="nav-pill">API Docs</a>
      <a href="#impact" class="nav-pill">Impact</a>
    </div>
  </div>
</div>

<div class="divider"></div>

<!-- \u2500\u2500 PROBLEM \u2500\u2500 -->
<section id="problem">
  <div class="container fade-in">
    <p class="section-label">01 \u2014 Problem Statement</p>
    <h2>The False Alarm Crisis</h2>
    <p>In chemical manufacturing environments, H2S sensors trigger alarms when detecting potentially hazardous gas leaks. However, <strong>frequent false alarms</strong> create costly operational and safety challenges.</p>
    <div class="problem-grid">
      <div class="problem-card">
        <div class="problem-icon">\ud83d\udea8</div>
        <h3>Emergency Fatigue</h3>
        <p>Unnecessary emergency team deployment on every alarm</p>
      </div>
      <div class="problem-card">
        <div class="problem-icon">\u23f1\ufe0f</div>
        <h3>Productivity Loss</h3>
        <p>Operational delays disrupt production workflows</p>
      </div>
      <div class="problem-card">
        <div class="problem-icon">\ud83d\udcb0</div>
        <h3>Rising Costs</h3>
        <p>Increased maintenance and sanitation expenditure</p>
      </div>
      <div class="
