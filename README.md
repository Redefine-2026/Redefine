# REDEFINE

Landing page for **REDEFINE**, a 24-hour designathon run by the IEEE Computer Society.

**16–17 September · 08:00 → 08:00 · Sarojini Naidu Gallery · teams of 1–4 · ₹150 per ticket**

Take something familiar, question everything about it, and build something better.

## What's here

| Path | What it is |
|---|---|
| `index.html` | The page. Loads the artwork from `assets/`. |
| `assets/desktop.svg` | The desktop artwork (1440×1024), exported from Figma. |
| `assets/mobile.svg` | The mobile artwork (402×874). |
| `logo.png` | Event logo — favicon, header mark, link preview. |
| `design/` | The original untouched Figma exports. |
| `src/` | Page source, split into `head.part` (styles) and `body.part` (markup + script). |
| `dist/redefine-single.html` | The whole page as one file, artwork inlined as data URIs. Host it anywhere, no other files needed. |

## Editing

Edit `src/head.part` or `src/body.part`, then:

```sh
python3 src/build.py
```

That regenerates both `index.html` and `dist/redefine-single.html`, so the two can't drift apart. Don't edit `index.html` directly — the build overwrites it.

## How the page works

The opening screen is the Figma artwork itself, placed as an image and swapped for the mobile export under 760px. Transparent hotspots sit on top at coordinates read from the SVG, so REGISTER and the TIMELINE / TRACKS / TEAM UP / FAQ labels are clickable and stay aligned at any width. Hovering one hides the system cursor and shows a glowing pen instead — on fine pointers only.

REGISTER opens a chooser that routes to the right VIT portal:

- VIT students → `vconnect.vit.ac.in/vtopconnect/login`
- Everyone else → `web.vit.ac.in/gravitasexternal/login`

Below the artwork: a live countdown to the opening bell, the brief, tracks, timeline, judging criteria, team sizing and FAQ.

No build tooling, no dependencies. The only external request is the Google Fonts stylesheet (Archivo Black, Archivo, JetBrains Mono).

## The prize pool is hidden, not deleted

Every mention is commented out rather than removed, so it comes back without rewriting anything. Search `src/body.part` for `PRIZE POOL` — there are five places:

1. The nav link
2. The stats tile (swap it back in for the "4 / Judging criteria" tile)
3. The whole `<section id="prize">`
4. The final call to action's line
5. The footer

Uncomment what you want, put the real figure in place of `₹ _ _ _ _ _`, then run the build. The styles it needs are still in `src/head.part`, marked with the same tag.

## Still to fill in

- Check-in time, checkpoint format, and results timing (marked TBA on the timeline)
- A contact address for the footer
