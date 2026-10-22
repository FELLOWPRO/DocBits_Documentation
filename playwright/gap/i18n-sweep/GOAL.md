# GOAL — localized-screenshot sweep (verbindlich)

## Ziel (ein Satz)

Jede Doku-Seite bekommt in **jeder ihrer Sprachen** Screenshots **in genau dieser
Sprache** — danach gemergt, die Bridge dispatcht, live verifiziert. Bis es
wirklich fertig ist.

## Harte Regeln

- **Eine Sprache zur Zeit.** Kein Batch, kein Sub-Agent-Fan-out.
- **Nach JEDER Seite mergen** (PR → Merge), damit der Fortschritt sichtbar ist.
- **Immer die Bridge dispatchen** (`sync-language-folders.yml`) nach jedem Merge.
- **Cron-Health-Check** stündlich: Bridge-Liveness, Live-Bytes, Worklist-Drift.
- Sprachen = die 9 GitBook-Spaces: en de es fr it nl pl pt zh. **Nie tr/rs.**
- „Alle Sprachen" = diese 9. en ist Referenz, andere 7 neben de/zh.

## Definition of Done

1. Für jede Seite: kein englischer Asset-Ref mehr in Nicht-en-Sprachen.
2. Alle `<asset>-<lang>.png` existieren, sind byte-distinct von en.
3. Live (docs.docbits.com/<space>/…) liefert die Sprach-Blobs.
4. Worklist-Count der Sprache geht **runter**, nie hoch.
5. PROGRESS.md hat pro Seite eine Zeile mit PR-Nr + Live-Status.

## Umfang (Stand 2026-10-18, gemessen)

Zwei Filter reduzieren den Roh-Umfang massiv:

1. **EDI-Previews sind sprachneutral** — `*-preview.png` zeigt den Beleg
   (XML/PDF), nicht die DocBits-UI. Kein Fix.
2. **Kleine Assets (<320×200 px) sind Icons/Glyphen** — sprachneutral.

Danach bleibt pro Sprache (Seiten / echte UI-Bilder):

| lang | Kandidaten roh | echte UI-Seiten | echte UI-Refs |
|---|---|---|---|
| de | 221 | 126 | 545 |
| es | 206 | 116 | 481 |
| fr | 208 | 118 | 473 |
| it | 212 | 118 | 460 |
| nl | 204 | 110 | 469 |
| pl | 216 | 122 | 459 |
| pt | 214 | 118 | 452 |
| zh | 389 | 245 | 852 |
| **Σ** | | **1.073** | **~4.190** |

Dedup: **355 distinct Assets decken 121 de-Seiten** (132 Assets sind über 2
Seiten geteilt; mehrere Bäume sind Dubletten, z. B. `exporting-to-infor` vs
`exporting-to-infor-1`, `analytics-dashboard` vs `/README`).

### Aktuelles Ziel (vom Nutzer gesetzt 2026-10-18)

**Top-20 Seiten von de erledigen, dann Statusbericht.** Kein endloser Lauf.
Danach entscheidet der Nutzer neu.

- Fertig + live: **20 Seiten** (19 + `global-settings/dashboard`).
- Reihenfolge: größte echte UI-Ref-Anzahl, Route zuerst sondieren.

## Arbeitszyklus pro Seite

1. `git fetch origin <lang>` — Branch kann von Parallel-Sessions bewegt sein.
2. Refs + vorhandene `-de`/`-<lang>`-Geschwister prüfen (Ref-Swap vs. Neucapture).
3. Capturen (headless), **jedes Bild ansehen**, Maskieren (Personen, E-Mails,
   Org-UUIDs, Hosts) und objektiv auf 0 Leaks prüfen.
4. Assets kopieren, Refs relativ setzen, korrekte `../`-Tiefe.
5. Commit → Push → PR → Merge → Bridge dispatch.
6. Live verifizieren (Blob aus dem Sprach-Space, distinct von en).
7. PROGRESS.md-Zeile schreiben + committen.
8. Nächste Seite.

## Nicht-Ziele

- Keine Produkt-Fixes (i18n-Lücken der App) — nur notieren, nicht erfinden.
- Keine Screenshots fälschen. Keine leeren/doppelten Bilder shippen.
- Kein Push auf en-Seiten ohne Grund.
