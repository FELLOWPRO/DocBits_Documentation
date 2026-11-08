# Supplier Diagnosis and Issue Clusters

<!-- touchless-admin-video-v2-20261104:start -->
**Video-Kapitel (Prüffassung):** [Wiederkehrende Probleme untersuchen](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence-preview-admin/v2/en.html#chapter=06).
<!-- touchless-admin-video-v2-20261104:end -->

Klicken Sie in der Warteschlange auf einen Lieferanten, um seine Diagnoseseite zu öffnen.

<figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/touchless-supplier-detail.png" alt="Die Seite Supplier Diagnosis mit Ergebnis-Kacheln, Trend und zwei Problemclustern"><figcaption><p>Die Seite Supplier Diagnosis: Ergebnis-Kacheln, Trend mit Zeitraumauswahl und zwei nach erwartetem Zuwachs sortierte Problemcluster. Beispielorganisation mit Demodaten; die Lieferantennamen sind fiktiv.</p></figcaption></figure>

Die Seite zeigt:

Die Ergebnis-Kacheln und die Diagrammsegmente zählen getrennte Dokumentergebnisse. AP touchless bedeutet hier ausschließlich freigegebene Dokumente; die kombinierte AP-Kennzahl im Überblick enthält zusätzlich die reinen Dokumente.

* **Four final-outcome tiles** (Pure touchless, AP touchless, AP assisted, Process exception), jede mit den zugehörigen Dokumenten verlinkt.
* **The trend** mit eigener Zeitraumauswahl: 30 Tage, 90 Tage, 6 Monate, 1 Jahr oder ein eigener Zeitraum (bis zu zwei Jahren). Das ändert nur das Diagramm.
* **Issue clusters** (siehe unten).
* **Change history**: die Änderungen, die Sie für diesen Lieferanten umgesetzt haben, und was sie bewirkt haben.
* **Recent examples**: Beispieldokumente in zwei Tabs: **Needed attention** und **Went touchless**.
* **Diagnose supplier with AI**: analysiert alle Cluster des Lieferanten (Administratoren).

Ein kurzer Hinweis erklärt eine leere Seite, zum Beispiel: _5 Dokumente dieses Lieferanten werden noch verarbeitet und haben noch kein Analyseergebnis._ oder _Alle 40 abgeschlossenen Dokumente dieses Lieferanten liefen touchless: es gibt nichts zu diagnostizieren._

### Issue clusters

Ein **Cluster** fasst die Dokumente eines Lieferanten zusammen, die aus **demselben ersten Grund** angehalten haben. Statt 40 einzelner Probleme sehen Sie „3 Probleme".

<figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/touchless-issue-cluster.png" alt="Eine geöffnete Problemcluster-Karte mit erstem Blocker, empfohlener Änderung und Änderungsvorschlag"><figcaption><p>Eine geöffnete Cluster-Karte: der erste Blocker, <strong>What to change</strong> und ein <strong>Change proposal</strong> mit Risiko, Umfang und offenen Fragen. Hier umfasst der Cluster 58 Dokumente und ist +18,7 pp wert. Beispielorganisation mit Demodaten; die Lieferantennamen sind fiktiv.</p></figcaption></figure>

**Beispielcluster (illustrativ).**

* **Headline**: _Required field missing_ in der Stufe _Field Validation_
* **Affected**: 28 Dokumente. **Recoverable**: 28 Dokumente. **Expected lift**: +2,8 pp
* **Suspected cause**: der Lieferant druckt die Bestellnummer unterhalb der Tabelle, wo die Extraktion nicht hinsieht
* **What to check next**: die gedruckte Bestellnummer mit dem extrahierten Wert vergleichen und die Extraktionskonfiguration dieses Lieferanten prüfen, bevor eine Änderung vorgeschlagen wird
* **Owner**: Consultant. **Confidence**: Medium. **Source**: Hypothesis

Was eine Cluster-Karte zeigt:

| Teil                                       | Bedeutung                                                                                                                                                                                                                                               |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **First blocker** und **stage**            | Der Grund und die Pipeline-Stufe, in der die Dokumente anhalten. Es gibt mehr als 30 Gründe, zum Beispiel _Supplier not identified_, _Purchase order not found_, _Unit price outside PO tolerance_, _Rejected by the ERP_, _E-invoice validation failed_  |
| **Affected / Recoverable / Expected lift** | Wie viele Dokumente, wie viele zurückgewonnen werden können, wie viele Prozentpunkte das bringen würde                                                                                                                                                   |
| **Suspected cause / Confirmed cause**      | Was DocBits für den Grund hält (oder eine Person bestätigt hat)                                                                                                                                                                                         |
| **Evidence** und **Missing evidence**      | Worauf der Befund beruht und was DocBits **nicht** feststellen konnte. Lesen Sie **Missing evidence**, bevor Sie dem Rest vertrauen                                                                                                                      |
| **What to change**                         | Konkrete Schritte mit **Open**-Links zu den Einstellungen. Ein Chip nennt den Typ: _Configuration change_, _Master data change_, _Supplier template change_, _Process change_, _Supplier action needed_, _Not fixable_                                      |
| **Owner**                                  | DocBits, Customer, Consultant, Supplier oder Unassigned. Der Chip nennt den Eigentümer des Änderungsvorschlags; nur wenn die Vorschläge der Karte voneinander abweichen, fällt er auf den Eigentümer des gesamten Clusters zurück                                 |
| **Sample documents**                       | Echte Dokumente des Clusters zum Ansehen                                                                                                                                                                                                                |

**Fixable in DocBits** und **Supplier action only** werden in zwei Gruppen gezeigt. Bei _Supplier action only_ ändert nichts in DocBits das Ergebnis: der Lieferant muss das Dokument korrigieren und erneut senden.

### Woher stammt eine Empfehlung

Jede Ursache nennt ihre **Quelle**, damit Sie einen abgeleiteten Befund von einer Vermutung unterscheiden können:

| Quelle                             | Bedeutung                                                                                              |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------ |
| **Deterministic** / **Rule-based** | Eine Regel hat sie aus der aufgezeichneten Pipeline-Evidenz abgeleitet. Kein Sprachmodell war beteiligt |
| **Hypothesis**                     | Ein Sprachmodell hat sie aus der Cluster-Evidenz vorgeschlagen. Behandeln Sie sie als Hinweis und prüfen Sie sie, bevor Sie handeln |
| **Confirmed**                      | Eine Person hat die Evidenz geprüft und die Ursache bestätigt                                          |

KI-Texte werden in der Sprache Ihrer Organisation geschrieben. Wurde ein Cluster in einer anderen Sprache analysiert, verwenden Sie **Analyse in this language**.

## Wer muss eine Abweichung in den Quelldaten beheben?

Setzen Sie **AP assisted** nicht mit einem Extraktionsfehler gleich. Trennen Sie bei jedem Beispieldokument das Verarbeitungsergebnis von der bestätigten Ursache:

| Evidenz | Untersuchen oder beheben |
| --- | --- |
| Die Rechnung enthält einen Wert, den DocBits anders extrahiert hat | Extraktionskonfiguration oder Lieferantenvorlage |
| Die Extraktion stimmt mit der Rechnung überein, die Infor-Bestellung hat aber einen bestätigt falschen Preis, eine falsche Menge oder Einheit | Daten im Quellsystem; die Buchhaltung stimmt sich mit dem Einkauf oder dem Eigentümer der Stammdaten ab |
| Infor ist korrekt, DocBits hat aber eine alte oder unvollständige Kopie | Import oder ERP-Integration |
| Rechnung und Quellwerte weichen voneinander ab, der vereinbarte Wert ist aber nicht geklärt | Fachliche Klärung; die Ursache bleibt unbestätigt |

Ein kleiner Eingriff der Buchhaltung kann die Rechnung abschließen und trotzdem ein wiederkehrendes Problem in den Quelldaten offen lassen. Halten Sie sowohl die unmittelbare Maßnahme als auch die dauerhafte Korrektur fest. Der Cluster allein belegt nicht den früheren Inhalt von Infor. Siehe das [ausgearbeitete Infor-Beispiel](touchless-po-matching-diagnosis.md#worked-example-correct-extraction-different-infor-data).

## Cluster beim PO-Abgleich

Ist der erste Blocker eines Clusters ein Grund aus dem PO-Abgleich (zum Beispiel _PO item mismatch_ oder _Purchase order not found_), zeigt die Cluster-Karte, wie DocBits versucht, die Rechnung der Bestellung zuzuordnen. Siehe [PO Matching Diagnosis](touchless-po-matching-diagnosis.md).

Siehe [Touchless with MCP](touchless-mcp.md) für die Aufrufe der Abgleichswerkzeuge und die Einordnung menschlicher Aktionen.

## Verwandte Seiten

* [Touchless Intelligence](./)
* [PO Matching Diagnosis](touchless-po-matching-diagnosis.md)
* [Document Trace](touchless-document-trace.md)
* [Change Proposals and Reports](touchless-change-proposals.md)

<!-- Documentation review 2026-11-04: extraction quality vs process outcomes; KPI and terminal-outcome definitions checked against DocBits_API c51f350c728acb8ac964098d15f7b006bce273f4, module/automation_intelligence/kpi.py and bucket.py. Existing native screenshots retained and checked separately from illustrative examples. -->

<!-- Completion review 2026-11-04: owned synthetic PO examples, MCP schema/read evidence, human-action classification, KPI labels and screenshot proof limits. -->
