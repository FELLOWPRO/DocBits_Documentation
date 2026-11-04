# AI Table

Mit AI Table prüfen Sie extrahierte Positionen, korrigieren Spalten und speichern passende Anweisungen für ein Lieferantenlayout. Wählen Sie unten die Anleitung für Ihre Aufgabe. Structured Output erhält eine eigene Konfigurationsanleitung mit Standard/Ja/Nein, Überschreibungen, Vorschau und einem durchgängigen Beispiel.

* [Einstellungen und Überschreibungen](configuration.md)
* [Structured Output für Tabellen](structured-output.md)
* [Spalten und Korrekturen](columns-and-corrections.md)
* [KI-Anweisungen](ai-instructions.md)
* [AI-Tabellen-Tags](ai-table-tags.md)
* [Extraktion erklären und Fehler eingrenzen](explain-extraction.md)
* [Assistent und Berechtigungen](assistant-and-permissions.md)
* [Videos](videos.md)

<figure><img src="../../../.gitbook/assets/anatomy-ai-table.svg" alt="Isometrische Darstellung eines Tabellenlesers: Ein Lesekopf mit einer Anweisungskassette tastet eine Dokumenttabelle ab, ein Patchfeld steckt jede zurückgegebene Spalte in eine konfigurierte Spalte, und die konfigurierten Spalten stehen als Behälter mit je einem Drehschalter für Use AI mit drei Stellungen da."><figcaption><p>Die KI liest die Tabelle und liefert Spalten zurück. Jede zurückgegebene Spalte wird einer konfigurierten Tabellenspalte zugeordnet (eine zurückgegebene Spalte ohne Zuordnung bleibt ausgeblendet), jede konfigurierte Spalte hat ihre eigene Use-AI-Einstellung (Standard, Ja oder Nein), und die KI-Anweisungen sowie <strong>Als Training speichern</strong> bestimmen, wie die nächsten Dokumente desselben Lieferantenlayouts gelesen werden.</p></figcaption></figure>

## Wann Sie die KI-Tabelle erhalten

* Ein Administrator hat **AI-Tabellen-Extraktion** eingeschaltet (Einstellungen → Dokumentenverarbeitung → Klassifizierung und Extraktion, siehe [Einstellungen für Administratoren](#einstellungen-fur-administratoren)). Ist sie ausgeschaltet, zeigt der Tabellenbereich *Hier wird die KI-Tabelle angezeigt. Aktivieren in …*.
* Prüfen Sie lesbaren Text beziehungsweise die gewählte Vision-Eingabe. Gespeicherte klassische Tabellenregeln können weiterhin den wirksamen Tabellenpfad bestimmen; kontrollieren Sie [den tatsächlich verwendeten Extraktionspfad](../../../overview-and-basics/faq/document-processing/which-extraction-path-was-used.md).
* Einzelne Spalten besitzen eine dreistufige Use-AI-Auswahl. Prüfen Sie daneben die wirksame Quelle und die Lieferantenregeln; Structured Output ersetzt nicht jede regelbasierte Tabelle.

Welche KI-Stufe die Tabelle liest (Fast, Full, Nexus), wird pro Organisation festgelegt und kann pro Lieferant überschrieben werden, siehe Lieferantenspezifisches KI-Modell.

## Die KI-Tabelle im Überblick

<figure><img src="../../../.gitbook/assets/ai-table-overview-de.png" alt="KI Extrahierte Tabelle mit ihren Spaltenüberschriften und vier Zeilen"><figcaption><p>Die zwei Tabs, die KI Extrahierte Tabelle und ihre Spaltenüberschriften.</p></figcaption></figure>

* **Tabs.** *KI Extrahierte Tabelle* zeigt, was die KI gelesen hat. *Extrahierte Tabelle* ist die klassische Tabelle aus trainierten Regeln. Der KI-Tab öffnet sich standardmäßig, wenn das Dokument eine KI-Tabelle hat.
* **Spaltenüberschrift.** Jede Spalte zeigt ihren Namen, ein kleines **Herkunfts**-Symbol (fahren Sie mit der Maus darüber: *KI · Zuordnung*, *KI · Synonym* und so weiter zeigen, wie die KI die Spalte zugeordnet hat), ein **Drei-Punkte**-Menü und, bei einer zugeordneten Spalte, eine **Namensschaltfläche**, mit der Sie ändern können, um welche Spalte es sich handelt.
* **Zeilenschaltflächen.** Das **x** am Zeilenanfang entfernt die Zeile. Per Rechtsklick auf eine Zeile erscheint *Als Zusatzkosten auswählen* / *Als zusätzliche Kosten entfernen*.
* **Symbolleiste im Fußbereich.** Die Symbole am unteren Bildschirmrand fügen Spalten und Zeilen hinzu oder blenden sie aus, siehe [Symbolleiste im Fußbereich](#symbolleiste-im-fussbereich).
* **Karte „Anweisungen für die KI“** unter der Tabelle: Prompt, zusätzliche Spalten, **Änderung testen**, **Anwenden**, **Als Training speichern**, **Löschen**, **Exportieren**, siehe [KI-Anweisungen geben](#ki-anweisungen-geben).

{% hint style="info" %}
Die Spaltenfunktionen arbeiten nur, wenn Sie das Dokument bearbeiten können. Sind sie ausgegraut, ist das Dokument schreibgeschützt oder in einer anderen Sitzung gesperrt. Meldet das rote Banner, dass das Dokument von Ihrem eigenen Benutzer in einer anderen Sitzung gesperrt ist, übernimmt **Freischalten** die Sperre.
{% endhint %}


## Einstellungen für Administratoren

Hier weiterlesen: [Einstellungen und Überschreibungen](configuration.md).

### KI pro Spalte nutzen

Hier weiterlesen: [Structured Output für Tabellen](structured-output.md).

<a id="die-richtige-spalte-wählen-neu-zuordnen"></a>
<a id="die-richtige-spalte-wahlen-neu-zuordnen"></a>
<a id="das-drei-punkte-menü"></a>
<a id="das-drei-punkte-menu"></a>
<a id="symbolleiste-im-fußbereich"></a>

## Eine Spalte ändern

Hier weiterlesen: [Spalten und Korrekturen](columns-and-corrections.md).

<a id="mit-nexus-vorschlagen"></a>
<a id="testen-anwenden-speichern-was-jede-schaltfläche-bewirkt"></a>
<a id="testen-anwenden-speichern-was-jede-schaltflache-bewirkt"></a>

## KI-Anweisungen geben

Hier weiterlesen: [KI-Anweisungen](ai-instructions.md).


## Sehen, was die KI getan hat

Hier weiterlesen: [Extraktion erklären und Fehler eingrenzen](explain-extraction.md).


## Praktische Beispiele

Hier weiterlesen: [Extraktion erklären und Fehler eingrenzen](explain-extraction.md).

<a id="einem-administrator-eine-regel-vorschlagen"></a>

## Der Assistent und die KI-Tabelle

Hier weiterlesen: [Assistent und Berechtigungen](assistant-and-permissions.md).


## Wer darf was

Hier weiterlesen: [Assistent und Berechtigungen](assistant-and-permissions.md).

<a id="1-die-ki-tabelle-lesen"></a>
<a id="2-eine-spalte-korrigieren-und-docbits-anlernen"></a>
<a id="3-zwei-typische-probleme"></a>
<a id="4-das-liest-die-ki-richtig"></a>
<a id="5-der-assistent-und-wer-was-ändern-darf"></a>
<a id="5-der-assistent-und-wer-was-andern-darf"></a>

## Videoserie

Hier weiterlesen: [Videos](videos.md).

## Verwandte Seiten

* [KI-Tabellen-Tags und Anweisungen](ai-table-tags.md)
* [Positionsfelder und Tabellen trainieren](../../../administration-and-setup/setup/document-training/training-line-fields-table-training/README.md)
* [Touchless Intelligence](../../../administration-and-setup/touchless-intelligence.md)
