import re
import os

with open("hyrox-checklist.html", "r", encoding="utf-8") as f:
    base_html = f.read()

pages = [
    {
        "filename": "hyrox-open-doubles.html",
        "title": "HYROX Open Doubles – Practice Checklist",
        "title_main": "HYROX <em>Open Doubles</em>",
        "summary_footer": "HYROX Doubles · Men’s Open · Practice Run",
        "key": "hyrox_open_doubles_v1",
        "run": "Together · Target 5:00–5:30/km",
        "st1": "500 m each · Switch once",
        "st2": "152 kg · 25 m each · Switch at halfway",
        "st3": "103 kg · 25 m each · Hand over hand",
        "st4": "40 m each · Alternate every 10 m",
        "st5": "500 m each · Switch once",
        "st6": "2 × 24 kg each · Full 200 m together",
        "st7": "20 kg · 50 m each · Switch at halfway",
        "st8": "6 kg ball · 3 m target · 50 reps each"
    },
    {
        "filename": "hyrox-open-singles.html",
        "title": "HYROX Open Singles – Practice Checklist",
        "title_main": "HYROX <em>Open Singles</em>",
        "summary_footer": "HYROX Singles · Men’s Open · Practice Run",
        "key": "hyrox_open_singles_v1",
        "run": "Solo run · Target 5:00–5:30/km",
        "st1": "1000 m SkiErg",
        "st2": "152 kg · 50 m Push",
        "st3": "103 kg · 50 m Pull",
        "st4": "80 m Burpee Broad Jumps",
        "st5": "1000 m Row",
        "st6": "2 × 24 kg · 200 m Carry",
        "st7": "20 kg · 100 m Lunges",
        "st8": "6 kg ball · 3 m target · 100 reps"
    },
    {
        "filename": "hyrox-pro-doubles.html",
        "title": "HYROX Pro Doubles – Practice Checklist",
        "title_main": "HYROX <em>Pro Doubles</em>",
        "summary_footer": "HYROX Doubles · Men’s Pro · Practice Run",
        "key": "hyrox_pro_doubles_v1",
        "run": "Together · Target 4:45–5:15/km",
        "st1": "500 m each · Switch once",
        "st2": "202 kg · 25 m each · Switch at halfway",
        "st3": "153 kg · 25 m each · Hand over hand",
        "st4": "40 m each · Alternate every 10 m",
        "st5": "500 m each · Switch once",
        "st6": "2 × 32 kg each · Full 200 m together",
        "st7": "30 kg · 50 m each · Switch at halfway",
        "st8": "9 kg ball · 3 m target · 50 reps each"
    },
    {
        "filename": "hyrox-pro-singles.html",
        "title": "HYROX Pro Singles – Practice Checklist",
        "title_main": "HYROX <em>Pro Singles</em>",
        "summary_footer": "HYROX Singles · Men’s Pro · Practice Run",
        "key": "hyrox_pro_singles_v1",
        "run": "Solo run · Target 4:45–5:15/km",
        "st1": "1000 m SkiErg",
        "st2": "202 kg · 50 m Push",
        "st3": "153 kg · 50 m Pull",
        "st4": "80 m Burpee Broad Jumps",
        "st5": "1000 m Row",
        "st6": "2 × 32 kg · 200 m Carry",
        "st7": "30 kg · 100 m Lunges",
        "st8": "9 kg ball · 3 m target · 100 reps"
    }
]

for p in pages:
    content = base_html
    # Update title
    content = re.sub(r'<title>.*?</title>', f'<title>{p["title"]}</title>', content)
    # Update title-main
    content = re.sub(r'<div class="title-main">HYROX <em>Doubles</em></div>', f'<div class="title-main">{p["title_main"]}</div>', content)
    # Update summary footer
    content = re.sub(r'<div class="summary-footer">HYROX Doubles · Men’s Open · Practice Run</div>', f'<div class="summary-footer">{p["summary_footer"]}</div>', content)
    # Update KEY
    content = re.sub(r"const KEY = 'hyrox_v4';", f"const KEY = '{p['key']}';", content)
    
    # Update sections detail
    content = re.sub(r"id:'run\d'.*?detail:'[^']+'", lambda m: m.group(0).split("detail:'")[0] + f"detail:'{p['run']}'", content)
    
    content = re.sub(r"id:'st1'.*?detail:'[^']+'", lambda m: m.group(0).split("detail:'")[0] + f"detail:'{p['st1']}'", content)
    content = re.sub(r"id:'st2'.*?detail:'[^']+'", lambda m: m.group(0).split("detail:'")[0] + f"detail:'{p['st2']}'", content)
    content = re.sub(r"id:'st3'.*?detail:'[^']+'", lambda m: m.group(0).split("detail:'")[0] + f"detail:'{p['st3']}'", content)
    content = re.sub(r"id:'st4'.*?detail:'[^']+'", lambda m: m.group(0).split("detail:'")[0] + f"detail:'{p['st4']}'", content)
    content = re.sub(r"id:'st5'.*?detail:'[^']+'", lambda m: m.group(0).split("detail:'")[0] + f"detail:'{p['st5']}'", content)
    content = re.sub(r"id:'st6'.*?detail:'[^']+'", lambda m: m.group(0).split("detail:'")[0] + f"detail:'{p['st6']}'", content)
    content = re.sub(r"id:'st7'.*?detail:'[^']+'", lambda m: m.group(0).split("detail:'")[0] + f"detail:'{p['st7']}'", content)
    content = re.sub(r"id:'st8'.*?detail:'[^']+'", lambda m: m.group(0).split("detail:'")[0] + f"detail:'{p['st8']}'", content)
    
    with open(p["filename"], "w", encoding="utf-8") as f:
        f.write(content)

