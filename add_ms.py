import os

html_files = [f for f in os.listdir('.') if f.startswith('hyrox-') and f.endswith('.html')]

target_fmt = """function fmt(s) {
  const h = Math.floor(s / 3600);
  const m = Math.floor((s % 3600) / 60);
  const sec = Math.floor(s % 60);
  if (h > 0) return String(h).padStart(2,'0')+':'+String(m).padStart(2,'0')+':'+String(sec).padStart(2,'0');
  return String(m).padStart(2,'0')+':'+String(sec).padStart(2,'0');
}

function fmtTotal(s) {
  const h = Math.floor(s / 3600);
  const m = Math.floor((s % 3600) / 60);
  const sec = Math.floor(s % 60);
  return String(h).padStart(2,'0')+':'+String(m).padStart(2,'0')+':'+String(sec).padStart(2,'0');
}"""

replacement_fmt = """function fmt(s) {
  const h = Math.floor(s / 3600);
  const m = Math.floor((s % 3600) / 60);
  const sec = Math.floor(s % 60);
  const ms = Math.floor((s % 1) * 100);
  const msStr = String(ms).padStart(2,'0');
  if (h > 0) return String(h).padStart(2,'0')+':'+String(m).padStart(2,'0')+':'+String(sec).padStart(2,'0')+'.'+msStr;
  return String(m).padStart(2,'0')+':'+String(sec).padStart(2,'0')+'.'+msStr;
}

function fmtTotal(s) {
  const h = Math.floor(s / 3600);
  const m = Math.floor((s % 3600) / 60);
  const sec = Math.floor(s % 60);
  const ms = Math.floor((s % 1) * 100);
  return String(h).padStart(2,'0')+':'+String(m).padStart(2,'0')+':'+String(sec).padStart(2,'0')+'.'+String(ms).padStart(2,'0');
}"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "function fmt(s)" in content:
        content = content.replace(target_fmt, replacement_fmt)
        content = content.replace("setInterval(tick, 500)", "setInterval(tick, 30)")
        content = content.replace("00:00:00", "00:00:00.00")
        content = content.replace("--:--", "--:--.--")
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
