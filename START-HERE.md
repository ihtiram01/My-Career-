# Start here

Five pages, all built from the markdown in `docs/`.

---

## Just want to read them?

Open `index.html`. Everything links from there. Works from a folder, from
Google Drive, from a USB stick — no internet needed after the fonts load once.

---

## Want to add a page?

Three steps. No code.

1. Copy `docs/_TEMPLATE.md` to `docs/my-page.md`
2. Edit it — the top part sets the title and colour, the rest is your content
3. Run `python3 build/build.py`

A page appears, and a card appears on the home page automatically. Nothing else
to edit.

### The markdown shape

```markdown
## Section heading
### Card title
- status: becomes a labelled row
- Any other line becomes a bullet
- master: 44, 46      ← links to the knowledge index
```

`##` starts a section. `###` starts a card. `-` makes a line. That is the whole
format.

### Colours

`blue` `orange` `green` `aqua` `violet` `red` `rose` `yellow` `bronze` `slate`
— or any hex code.

---

## Want to add files?

Drop PDFs, certificates or your CV into `files/` and rebuild. They appear on the
home page with their size. Anything over 25 MB will not deploy to Cloudflare.

---

## Want it online?

See `DEPLOY.md`. Roughly 15 minutes of clicking, once.

---

## The one rule

**Never edit the HTML.** Edit the markdown in `docs/` and rebuild. The HTML is
regenerated every time and your changes to it are silently thrown away.
