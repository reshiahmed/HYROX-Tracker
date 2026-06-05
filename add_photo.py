import os

html_files = [f for f in os.listdir('.') if f.startswith('hyrox-') and f.endswith('.html')]

head_target = "</head>"
head_replacement = """<script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
</head>"""

summary_target = """    </div>
  `;
  wrap.classList.add('visible');"""

summary_replacement = """    </div>
    <div style="text-align:center; margin-top: 16px;">
      <button id="savePhotoBtn" style="background:#f0c000; color:#000; border:none; padding:12px 24px; border-radius:8px; font-weight:800; text-transform:uppercase; letter-spacing:1px; cursor:pointer; font-size:13px; display:inline-flex; align-items:center; gap:8px; transition:transform 0.1s ease;">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
        Save as Photo
      </button>
    </div>
  `;
  wrap.classList.add('visible');
  
  document.getElementById('savePhotoBtn').addEventListener('click', function() {
    const btn = this;
    const originalText = btn.innerHTML;
    btn.innerHTML = "Saving...";
    btn.disabled = true;
    
    setTimeout(() => {
      html2canvas(document.querySelector('.summary'), { backgroundColor: '#0a0a0a', scale: 2 }).then(canvas => {
        const link = document.createElement('a');
        link.download = 'hyrox-summary.png';
        link.href = canvas.toDataURL('image/png');
        link.click();
        
        btn.innerHTML = originalText;
        btn.disabled = false;
      });
    }, 100);
  });"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "html2canvas.min.js" not in content:
        content = content.replace(head_target, head_replacement)
        content = content.replace(summary_target, summary_replacement)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
