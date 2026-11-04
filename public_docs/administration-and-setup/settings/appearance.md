# Appearance

**Appearance** lets an administrator give the organisation's copy of DocBits its own look: colours, corner radius, density and font. Everyone in the organisation sees the result — in both light and dark mode — after their next reload. It never changes layout or what a feature does, only how it is drawn.

> **Access:** Appearance is an admin-only page. Open **Settings → Organization & Access → Appearance**.

<!-- screenshot: /settings/appearance light -->

## Who can change it

Only organisation admins can open **Settings → Appearance** and save or reset a theme. Everyone else in the organisation only sees the result.

## What's on the page

The page is split into an editor on the left and a live preview on the right.

| Area | What it holds |
|---|---|
| **General** | The theme's name, the font, the corner radius and the density. |
| **Colors** | Light and dark tabs, one color picker plus a hex field per colour, grouped into Surfaces, Brand, Neutrals, Status and Charts. A read-only "Derived colours" panel underneath shows colours DocBits computes for you (hover states, focus rings and similar) from the colours above. |
| **Advanced overrides** | One `--token: value` line per entry, for the rare case the colour, radius, density and font controls above do not cover — see [Advanced overrides](#advanced-overrides). |

### Changing colours

Each colour has a swatch (click it to open your browser's colour picker) and a hex field next to it you can type or paste into. Leave a colour empty to keep the DocBits default for that token — the swatch shows a dashed border while empty. Switch the **Light** / **Dark** tab above the colour list to set the other mode; a colour you don't set in dark mode keeps its own DocBits default for dark, it does not copy the light value.

{% hint style="info" %}
Colours are entered as hex (`#2388ae` or `#2388aeaa` with alpha). There is no named-colour or `rgb()` input.
{% endhint %}

### Corner radius, density and font

* **Corner radius** — `None`, `Small`, `Medium` (default), `Large` or `Extra large`. Controls how rounded cards, buttons, inputs and dialogs are, app-wide.
* **Density** — `Compact`, `Comfortable` (default) or `Spacious`. Controls the height of buttons, inputs and table rows, and the base text size.
* **Font** — a short list of bundled fonts (Geist is the DocBits default; also Inter, Roboto, IBM Plex Sans, Source Sans 3, Nunito Sans, Manrope, Kanit, or the visitor's own system font). Every font is already bundled, so there is nothing to upload.

### Advanced overrides

For a design token the controls above don't expose directly (for example a specific table row height), add a line under **Advanced overrides**:

```
--table-row-h: 30px
```

One override per line, `--token: value`. An invalid line — an unknown token, a token that can't be customised, or a value that doesn't fit what the token expects — is listed as an error under the box and is not applied; everything else on the page still saves normally.

## Preview

Everything you change updates the **Preview** panel on the right immediately, without affecting what anyone else sees — it never touches the live app or the saved theme. The preview has its own tabs: an overview with both light and dark side by side, then dedicated pages of buttons, form fields, surfaces and status indicators so you can check contrast and legibility across the parts of the UI most sensitive to colour.

<!-- screenshot: /settings/appearance dark -->

If a change makes the theme invalid (see below), the preview keeps showing the last valid version instead of breaking.

## Save and reset

* **Save** writes the theme for the whole organisation. It is greyed out until something has actually changed and the theme is valid.
* **Reset** asks for confirmation, then removes the organisation's theme entirely and returns everyone to the DocBits default theme. This cannot be undone from the page — the colours have to be re-entered by hand (or re-imported, see below) if the organisation wants them back.
* A save or reset that fails (for example, a validation problem) lists the problem above the editor and leaves the page as it was; nothing is applied.

There are no contrast checks before saving — see [Tips](#tips) below.

## Export and import

* **Export** downloads the theme currently shown in the editor (saved or not) as a `.json` file, named after the theme.
* **Import** reads a `.json` theme file and loads it into the editor. It still has to be reviewed and saved to take effect — importing alone does not change what anyone sees. An invalid or oversized file (over 32 KB) is rejected with an error and nothing changes.

Export is a convenient way to back up a theme before experimenting, or to copy one organisation's look to another.

## What users see

Once saved, the theme applies to the whole application — every page, in both light and dark mode — for every member of the organisation, after their next reload (not instantly for other open sessions). A user who has never loaded the organisation before sees the DocBits default until the organisation's settings have loaded once, then the theme takes over.

Resetting returns everyone to the DocBits default look on their next reload, exactly as if no organisation theme had ever been set.

## Tips

* **Check contrast in both modes.** The editor does not warn about low-contrast combinations (for example, a light brand colour with light text). Use the preview's light and dark panels to check text stays readable before saving.
* **Leave status colours alone unless you have a reason to change them.** Destructive (errors), success, warning and info keep their meaning across the whole app — changing them can make an error look like a success at a glance. Change the brand colour and leave status colours at their defaults unless the organisation needs more than a conventional red/green/amber/blue.
* **Start from a full palette.** Exporting the current theme, or starting from the DocBits default, gives every base colour a value to edit from, rather than guessing which tokens exist.
* **A theme change affects every user in the organisation immediately on their next reload.** There is no preview-to-a-subset-of-users step; test the result yourself in light and dark before telling the team it's ready.
