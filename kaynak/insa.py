"""kaynak/sablon.html -> public/index.html

Kullanım (repo kökünde):  python3 kaynak/insa.py
- {{LOGO}} yer tutucusuna kaynak/logo-ic.svgfrag eklenir (logo vektörü).
- kaynak/head.html (doctype, SEO meta, JSON-LD) başa eklenir.
"""
from pathlib import Path

kok = Path(__file__).resolve().parent.parent
sablon = (kok / "kaynak/sablon.html").read_text()
logo = (kok / "kaynak/logo-ic.svgfrag").read_text()
head = (kok / "kaynak/head.html").read_text()

s = sablon.replace("{{LOGO}}", logo)
i = s.index("</style>") + len("</style>")
bas = s[:i].replace('<meta name="claude:viewport-fit-sides" content="cover">\n', "")
html = head + bas + "\n</head>\n<body>\n" + s[i:].lstrip() + "\n</body>\n</html>\n"
(kok / "public/index.html").write_text(html)
print("public/index.html yazıldı,", len(html), "bayt")
