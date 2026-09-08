#!/usr/bin/env python3
"""Builds the REDEFINE landing page from src/head.part + src/body.part.

  python3 src/build.py

Writes index.html (links assets/, small) and dist/redefine-single.html
(everything inlined as data URIs — one file you can host anywhere).
"""
import base64, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
head = (ROOT / "src/head.part").read_text()
body = (ROOT / "src/body.part").read_text()

def durl(rel, mime):
    return "data:%s;base64,%s" % (mime, base64.b64encode((ROOT / rel).read_bytes()).decode())

DOC = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="REDEFINE — a 24-hour designathon by IEEE Computer Society. 16–17 September, Sarojini Naidu Gallery. Teams of 1–4, ₹150 per ticket.">
<meta name="theme-color" content="#0B0B0C">
<meta property="og:title" content="REDEFINE">
<meta property="og:description" content="A 24-hour designathon by IEEE Computer Society. Take something familiar, question everything about it, and build something better.">
<meta property="og:image" content="logo.png">
<meta property="og:type" content="website">
<link rel="icon" href="logo.png">
{head}
<style>*,*::before,*::after{{box-sizing:border-box}}img{{max-width:100%}}[hidden]{{display:none!important}}</style>
</head>
<body>
{body}
</body>
</html>
'''

# ---- index.html: links the artwork, stays small -------------------------
linked = body.replace("__DESK__", "assets/desktop.svg").replace("__MOB__", "assets/mobile.svg")
(ROOT / "index.html").write_text(DOC.format(head=head, body=linked))

# ---- dist/redefine-single.html: everything inlined ----------------------
inline = (body
    .replace("__DESK__", durl("assets/desktop.svg", "image/svg+xml"))
    .replace("__MOB__",  durl("assets/mobile.svg",  "image/svg+xml"))
    .replace('<img alt="" id="hdrLogo">',
             '<img alt="" id="hdrLogo" src="%s">' % durl("assets/logo-256.png", "image/png")))
(ROOT / "dist").mkdir(exist_ok=True)
(ROOT / "dist/redefine-single.html").write_text(DOC.format(head=head, body=inline))

print("built index.html and dist/redefine-single.html")
