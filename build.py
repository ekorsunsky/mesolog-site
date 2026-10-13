"""Builds the static pages (shared header/footer). Run: python3 build.py"""
from pathlib import Path

SUPPORT = "support@mesolog.fit"
UPDATED = "October 13, 2026"

def page(name, title, desc, body, current=""):
    cur = ' aria-current="page"'
    nav = "".join(
        f'<a href="{href}"{cur if key == current else ""}{cls}>{label}</a>'
        for key, href, label, cls in [
            ("home", "/", "Home", ' class="hide-sm"'), ("support", "/support/", "Support", ""),
            ("privacy", "/privacy/", "Privacy", ""), ("terms", "/terms/", "Terms", ' class="hide-sm"')])
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="https://mesolog.fit/assets/icon-512.png">
<link rel="icon" href="/assets/favicon.png">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700&family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/style.css">
</head>
<body>
<header class="site-header"><div class="wrap">
  <a class="brand" href="/" aria-label="Mesolog home"><picture><source srcset="/assets/mark-light.svg" media="(prefers-color-scheme: light)"><img src="/assets/mark.svg" alt=""></picture><span class="wordmark">MESO<span>LOG</span></span></a>
  <nav aria-label="Main">{nav}</nav>
</div></header>
<main>
{body}
</main>
<footer class="site-footer"><div class="wrap">
  <span>© 2026 Mesolog. Made for lifters who train in blocks.</span>
  <nav aria-label="Footer"><a href="/support/">Support</a><a href="/privacy/">Privacy Policy</a><a href="/terms/">Terms of Use</a><a href="mailto:{SUPPORT}">{SUPPORT}</a></nav>
</div></footer>
</body>
</html>
"""
    out = Path(name)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html)

home = """
<div class="hero"><div class="wrap">
  <div>
    <p class="eyebrow">Hypertrophy block training</p>
    <h1>Train in blocks. Log in seconds. Watch every lift climb.</h1>
    <p class="lede">Mesolog plans each mesocycle from your 1RMs, shows today's target weight for every exercise, and turns each week into a clear next step. Built for real gym sessions: one tap logs the target, the timer runs itself, and your Apple Watch follows along.</p>
    <div class="cta-row">
      <span class="button" aria-disabled="true">Coming soon to the App Store</span>
      <a class="button secondary" href="/support/">Questions?</a>
    </div>
    <p class="note">For iPhone, iPad, Mac and Apple Watch. Free.</p>
  </div>
  <div class="hero-art"><img src="/assets/icon-512.png" alt="Mesolog app icon" width="320" height="320"></div>
</div></div>

<section><div class="wrap">
  <h2>A block, week by week</h2>
  <p class="intro">Every exercise gets a sets × reps scheme. Mesolog turns your 1RM into the final week's goal and builds up to it, so each week has a target you can actually hit. Blocks can run from 2 to 8 weeks, and you set the progression.</p>
  <div class="weeks" role="list">
    <div class="week" role="listitem"><b>65%</b><span>Week 1 · RPE 6</span></div>
    <div class="week" role="listitem"><b>85%</b><span>Week 2 · RPE 8</span></div>
    <div class="week" role="listitem"><b>95%</b><span>Week 3 · RPE 9</span></div>
    <div class="week" role="listitem"><b>Goal</b><span>Week 4 · RPE 9.5</span></div>
  </div>
</div></section>

<section><div class="wrap">
  <h2>Everything a training block needs</h2>
  <p class="intro">Designed around how lifters actually train: fast at the gym, thorough afterwards.</p>
  <div class="grid">
    <div class="card"><span class="tag">Log</span><h3>One tap, done</h3><p>Tap the weight to fill in today's target, change it if you need to, and mark missed reps set by set. The target stays on screen while you type.</p></div>
    <div class="card"><span class="tag">Plan</span><h3>Blocks that build themselves</h3><p>Start a new block from the last one: rep ranges move along the wave, stale exercises get swap ideas, and 1RMs go up where you earned it.</p></div>
    <div class="card"><span class="tag">Review</span><h3>End-of-block review</h3><p>Volume by week, every lift against its targets, and suggested 1RM updates you can apply with one tap.</p></div>
    <div class="card"><span class="tag">Watch</span><h3>Apple Watch companion</h3><p>Starting your workout on iPhone opens it on your wrist. Log with the Digital Crown, see heart rate and calories, and pause or finish from either device.</p></div>
    <div class="card"><span class="tag">Gym</span><h3>Every machine, its own track</h3><p>Hotel gym leg press or your usual one? Each machine keeps its own 1RM, history and setup notes, with photos of the seat settings.</p></div>
    <div class="card"><span class="tag">Health</span><h3>Readiness at a glance</h3><p>Sleep, HRV and resting heart rate from Apple Health, plus weight, body fat and steps, including your treadmill, without double counting.</p></div>
    <div class="card"><span class="tag">Time</span><h3>A timer that takes care of itself</h3><p>Finish a cardio warm-up and Mesolog offers to start lifting. Pause, restart or finish, and the session is saved to Apple Health.</p></div>
    <div class="card"><span class="tag">Sync</span><h3>Your data on every device</h3><p>Sign in with your email to use the same training log on iPhone, iPad and Mac, whatever Apple ID each device uses. Or keep it all in your own iCloud.</p></div>
    <div class="card"><span class="tag">Import</span><h3>Bring your spreadsheet</h3><p>Already train from an Excel plan? Import it, or start from a template. Export any block back to Excel whenever you like.</p></div>
  </div>
</div></section>
"""

privacy = f"""
<div class="doc"><div class="wrap">
<h1>Privacy Policy</h1>
<p class="updated">Last updated {UPDATED}</p>

<p>Mesolog is a training log. We built it to keep your information on your devices and under your control. We don't show ads, we don't use analytics or tracking, and we never sell or share your data.</p>

<h2>Short version</h2>
<ul>
  <li>Your training data is stored on your device.</li>
  <li>If you <strong>choose</strong> to sync, it's stored in your own iCloud account (Apple) or in your Mesolog account (our database), depending on what you pick.</li>
  <li>Data from Apple Health stays on your device. It is never uploaded to our servers.</li>
  <li>You can delete your account and everything in it from inside the app at any time.</li>
</ul>

<h2>What the app stores</h2>
<p>Your training plan and logs: exercises, one-rep maxes, blocks, the weights and reps you log, notes, machine setup notes and photos, workout times, and any peptide or supplement schedule you enter. Also the answers you give during set-up (sex, age, bodyweight, training experience), which are used only to estimate starting weights.</p>

<h2>Where it's stored</h2>
<table>
  <tr><th>Option</th><th>Where your data lives</th></tr>
  <tr><td>No sync (default)</td><td>Only on the device.</td></tr>
  <tr><td>iCloud sync</td><td>On the device and in your private iCloud database, operated by Apple under Apple's privacy policy. We cannot see it.</td></tr>
  <tr><td>Mesolog account</td><td>On the device and in our cloud database (hosted by Supabase), so it can sync to your other devices. Only your signed-in account can read it, enforced by row-level security in the database.</td></tr>
</table>

<h2>Your account</h2>
<p>If you create an account, we collect your email address to sign you in. Sign-in codes are emailed through our email provider (Resend). We use your email only to sign you in and to answer you if you contact us. We don't send marketing email.</p>

<h2>Apple Health</h2>
<p>With your permission, Mesolog reads sleep, heart rate variability, resting heart rate, body weight, body fat, steps, walking distance and workouts from Apple Health to show your readiness, your steps and your progress, and to notice when a cardio warm-up ends. It writes your finished strength workouts to Apple Health. Health data:</p>
<ul>
  <li>is read and used on your device only, and is not uploaded to our servers or included in account sync;</li>
  <li>is never used for advertising, never sold, and never shared with third parties;</li>
  <li>can be turned off at any time in the Health app (Sharing → Apps → Mesolog).</li>
</ul>

<h2>Apple Music</h2>
<p>If you turn on the music player, Mesolog controls playback with Apple's music player and looks up album artwork. Nothing about your listening is stored by us.</p>

<h2>Camera and photos</h2>
<p>Photos you take of machine setups are stored with your training data (on the device, and in iCloud or your account if you sync).</p>

<h2>Sharing</h2>
<p>We don't sell, rent or share your data. The only services that process it on our behalf are the ones named above (Supabase for account storage, Resend for sign-in email), and only to run the features you use. We'll disclose information only if the law requires it.</p>

<h2>Deleting your data</h2>
<ul>
  <li><strong>Account:</strong> Settings → Account → Delete account removes your account and every record stored with it, permanently.</li>
  <li><strong>Device:</strong> deleting the app removes its data from the device.</li>
  <li><strong>iCloud:</strong> manage or delete it in your device's iCloud settings.</li>
</ul>

<h2>Children</h2>
<p>Mesolog is not directed at children under 13, and we don't knowingly collect information from them.</p>

<h2>Changes</h2>
<p>If this policy changes, we'll update this page and the date at the top. Significant changes will also be noted in the app's release notes.</p>

<h2>Contact</h2>
<p>Questions or requests: <a href="mailto:{SUPPORT}">{SUPPORT}</a>.</p>
</div></div>
"""

terms = f"""
<div class="doc"><div class="wrap">
<h1>Terms of Use</h1>
<p class="updated">Last updated {UPDATED}</p>

<p>These terms apply to the Mesolog app and this website. By using Mesolog you agree to them, together with Apple's standard <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">Licensed Application End User License Agreement</a>.</p>

<h2>Not medical advice</h2>
<p>Mesolog is a logging and planning tool. Target weights, one-rep-max estimates, readiness information and any peptide, supplement or dosing calculator are informational only. They are not medical, nutritional or training advice, and they don't replace a doctor or a qualified coach. Talk to a medical professional before starting a training program or taking any substance, and stop exercising if you feel pain, dizziness or shortness of breath.</p>

<h2>Train safely</h2>
<p>Lifting weights carries a risk of injury. You're responsible for choosing weights you can handle with good form, using spotters and safety equipment, and following your gym's rules.</p>

<h2>Your data</h2>
<p>You own your training data. How we handle it is described in the <a href="/privacy/">Privacy Policy</a>. Keep your own backups (Settings → Backup → Back up now) if your data is important to you.</p>

<h2>Your account</h2>
<p>Keep access to your email address secure; anyone who can read it can sign in to your account. Don't misuse the service or try to access other people's data.</p>

<h2>No warranty</h2>
<p>Mesolog is provided "as is", without warranties of any kind. To the extent the law allows, we aren't liable for any injury, loss or damage that results from using the app.</p>

<h2>Changes</h2>
<p>We may update these terms; the date above shows the latest version.</p>

<h2>Contact</h2>
<p><a href="mailto:{SUPPORT}">{SUPPORT}</a></p>
</div></div>
"""

support = f"""
<div class="doc"><div class="wrap">
<h1>Support</h1>
<p class="updated">Email <a href="mailto:{SUPPORT}">{SUPPORT}</a>, and include the version from Settings → App version. We usually reply within two business days.</p>

<h2>Common questions</h2>
<details><summary>How are target weights worked out?</summary>
<p>Each sets × reps scheme has a %1RM range. The last week's goal is your 1RM × the middle of that range, rounded to your weight increment. Earlier weeks are a percentage of the goal (65 / 85 / 95% for a 4-week block). Change the percentages and RPE in Settings → Weekly progression, for any block length.</p></details>
<details><summary>How do I use Mesolog on my iPad or Mac too?</summary>
<p>Go to Settings → Account and sign in with your email on each device. Your training syncs within a few seconds. Devices on the same Apple ID can use iCloud sync instead.</p></details>
<details><summary>I didn't get the sign-in code.</summary>
<p>Check Junk or Spam for a message from Mesolog. Codes expire after a few minutes; tap "Send a new code" to get another.</p></details>
<details><summary>Why doesn't the Apple Watch app open when I start a workout?</summary>
<p>Your Watch needs to be on your wrist and unlocked, and the Watch app needs Health permission: open Mesolog on the Watch once and tap Start workout to grant it. Settings → Apple Health on the iPhone shows the result of the last attempt.</p></details>
<details><summary>I trained on a different machine. Will it mess up my numbers?</summary>
<p>No. Pick the machine on the exercise card before logging. Each machine has its own 1RM and history, and weeks logged on another machine can be moved with "Move here".</p></details>
<details><summary>How do I delete my account?</summary>
<p>Settings → Account → Delete account. It permanently removes your account and all data stored with it.</p></details>
<details><summary>Can I import my spreadsheet?</summary>
<p>Yes: Settings → Import from Excel. "Get the Excel template" gives you a file in the exact format, with instructions.</p></details>
</div></div>
"""

page("index.html", "Mesolog: Hypertrophy Training",
     "Plan mesocycles from your 1RMs, log every set in seconds and review each block. For iPhone, iPad, Mac and Apple Watch.", home, "home")
page("privacy/index.html", "Privacy Policy · Mesolog", "How Mesolog handles your data: on your device by default, no ads, no tracking.", privacy, "privacy")
page("terms/index.html", "Terms of Use · Mesolog", "Terms of use for the Mesolog app.", terms, "terms")
page("support/index.html", "Support · Mesolog", "Help with Mesolog: answers to common questions and how to contact us.", support, "support")
page("404.html", "Not found · Mesolog", "Page not found.", '<div class="doc"><div class="wrap"><h1>Page not found</h1><p><a href="/">Back to Mesolog</a></p></div></div>')
print("built")
