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

## Umfang (Stand 2026-10-18)

- Fertig + live: **19 Seiten** (18 de + 1 zh) + 8×3 e-mail-templates + 8 ui-redesign.
- **Nicht** zu fixen (Objekt sprachneutral): **92 de Seiten EDI-Preview-only**
  (XRechnung/ZUGFeRD/Facturae/…-Previews zeigen den Beleg, nicht die UI).
- Offen de real: **~93 UI-Seiten**. Dann es fr it nl pl pt zh.

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
