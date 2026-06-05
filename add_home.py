import os

html_files = [f for f in os.listdir('.') if f.startswith('hyrox-') and f.endswith('.html')]

target1 = """  <div class="header-top">
    <div>"""

replacement1 = """  <div class="header-top">
    <div style="display:flex; align-items:center; gap: 14px;">
      <a href="index.html" style="text-decoration:none; display:flex; align-items:center; justify-content:center; width:36px; height:36px; border-radius:8px; background:#141414; border:1px solid #2e2e2e; transition:all 0.15s ease;" onmouseover="this.style.borderColor='#f0c000'" onmouseout="this.style.borderColor='#2e2e2e'" aria-label="Home">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#f0c000" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
      </a>
      <div>"""

target2 = """    </div>
    <div class="header-right">"""

replacement2 = """      </div>
    </div>
    <div class="header-right">"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if target1 in content and target2 in content:
        content = content.replace(target1, replacement1)
        content = content.replace(target2, replacement2)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)

