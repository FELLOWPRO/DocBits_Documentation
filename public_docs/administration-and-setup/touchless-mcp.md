# Touchless mit MCP erklären und verbessern

<!-- touchless-admin-video-20261104:start -->
**Video-Kapitel (Prüffassung):** [Mit MCP erklären](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence-preview-admin/v1/de.html#chapter=10).
<!-- touchless-admin-video-20261104:end -->

Die folgenden Abläufe verwenden tatsächlich angebotene DocBits-MCP-Werkzeuge. Lesen und Erklären sind von schreibenden Aufrufen zu unterscheiden. Prüfen Sie Organisation, Rolle, Dokumenttyp, Zeitraum und Datenstand; fehlende Evidenz bleibt offen.

<figure><img src="../.gitbook/assets/touchless-owned-po-price-de.png" alt="Echte deutsche Dev-Ansicht einer eigens angelegten fiktiven Bestellung: 10 × 9 = 90. Sie ist der Quellvergleich für die MCP-Diagnose, kein Screenshot eines MCP-Clients und kein Nachweis erfolgreicher Auslesung oder Verarbeitung."><figcaption><p>Echte deutsche Dev-Ansicht einer eigens angelegten fiktiven Bestellung: 10 × 9 = 90. Sie ist der Quellvergleich für die MCP-Diagnose, kein Screenshot eines MCP-Clients und kein Nachweis erfolgreicher Auslesung oder Verarbeitung.</p></figcaption></figure>

## Touchless über MCP erklären

Mit einem verbundenen DocBits-MCP-Zugang können Sie dieselben fachlichen Fragen stellen wie im Dashboard. Beginnen Sie mit einer Auswertung ohne Änderungen:

> Erkläre mir für Rechnungen der letzten 30 Tage Pure Touchless, reine AP-Freigaben und die kombinierte AP-Touchless-Quote. Nenne Zähler, Nenner, ausgeschlossene und laufende Dokumente sowie den Datenstand. Trenne die Quote von der Auslesegenauigkeit.

Dazu dient `touchless_get_summary` mit `period: "30d"` und `doc_type: "INVOICE"`. Für einen Teilprozess verwenden Sie zusätzlich die von `touchless_list_segments` tatsächlich angebotenen Segmentfelder und Werte. Vergleichen Sie Dashboard und MCP nur mit derselben Organisation, demselben Dokumenttyp, Zeitraum und Segment; prüfen Sie jeweils `data_as_of`.

**Geprüftes Dev-Beispiel mit eigenen Testdaten:** Drei neu hochgeladene Rechnungen waren noch `IN_PROGRESS`. Die Rückgabe enthielt `population.total: 3`, `population.in_progress: 3`, `population.eligible: 0` und `official_touchless_rate.ap_pct: null`. Daraus folgt **noch keine berechenbare Quote**. Melden Sie weder „0 % Auslesegenauigkeit“ noch „100 % Touchless“, nur weil drei Uploads angekommen sind. Das `eligible` der Zusammenfassung bezeichnet hier die abgeschlossene KPI-Grundgesamtheit; ein einzelner Dokumentverlauf kann zugleich `eligible: true` und `bucket_final: false` ausweisen.

Die folgenden Seiten zeigen die nächsten Fragen: [Lieferanten priorisieren](touchless-supplier-diagnosis.md), [ein Dokument erklären](touchless-document-trace.md), [Bestellabweichungen prüfen](touchless-po-matching-diagnosis.md) und [Verbesserungen kontrolliert umsetzen](touchless-change-proposals.md).

MCP-Aufrufe laufen mit den Rechten des verbundenen Kontos. Organisationskontext und Rolle müssen passen. Die hier beschriebenen direkten MCP-Leseaufrufe wurden auf Dev geprüft; die Verfügbarkeit in einer anderen Oberfläche oder einer zusätzlichen Tool-Freigabeliste ist damit nicht zugesichert.

## Bestellabweichungen mit MCP untersuchen

> Prüfe die Bestellnummer dieser Rechnung. Ist der Import verarbeitet? Welche Werte und welche tatsächlich aktive Regel entscheiden den Abgleich? Trenne korrekte Auslesung, veralteten Import, falsche Quelle und fehlende Konfiguration. Ändere noch nichts.

1. Lesen Sie Original, `get_extracted_fields` und `get_extracted_tables`, bevor Sie eine richtige Auslesung behaupten.
2. Prüfen Sie die konkrete Bestellnummer mit `get_po_sync_status`, zum Beispiel `po_number: "TL20261104X1-PO02"`, `language: "de"`. Im Dev-Test meldete der Aufruf einen verarbeiteten Import und eine vorhandene Bestellung. Das belegt die Ankunft des Imports, nicht dessen fachliche Richtigkeit und nicht den aktuellen Stand in Infor.
3. Lesen Sie `touchless_get_document_trace` und `touchless_explain_po_match` mit derselben `doc_id`. Prüfen Sie tatsächliche Engine, aktive Regelversion, Vergleichsspalten und wirksame Toleranz. Bei einem gelieferten Cluster verwenden Sie dessen echte `issue_signature` für `touchless_get_po_match_evidence`.
4. Stoppen Sie bei fehlender Evidenz: Für den neuen Test-Dokumenttyp lieferte die Erklärung `state: "none_published"` und `parse_error: "no published rule set"`. Zusammen mit den noch leeren Auslesefeldern war damit **kein nachgewiesener Preis- oder Mengenblocker** und kein erfolgreicher Abgleich vorhanden. Auch ein angezeigter allgemeiner Ablauf ersetzt diese fehlenden Nachweise nicht.
5. Korrigieren Sie die bestätigte Ursache und prüfen Sie neue Rechnungen. Wird die aktuelle Rechnung von AP manuell korrigiert oder neu gestartet, bleibt dieser Eingriff bei erfolgreichem Abschluss relevant. Bei einem endgültigen Fehler gilt die Prozessausnahme; laufende Dokumente gehören noch nicht in den Quotennenner.

## Beispiel: Original, Auslesung und Verlauf mit MCP vergleichen

> Prüfe diese Rechnung, ohne sie zu ändern. Vergleiche Original, aktuelle Kopffelder und Tabellen. Erkläre den ersten belegten Blocker und die bisherigen Läufe. Sage ausdrücklich, wenn die ursprüngliche Auslesung vor einem Eingriff nicht mehr belegt ist.

| Aufruf | Was er liefert | Was er allein nicht beweist |
| --- | --- | --- |
| `get_extracted_fields` mit `doc_id` | Aktuelle Kopffelder, Werte und Konfidenzen | Historische Werte vor einer Korrektur oder vollständige Richtigkeit |
| `get_extracted_tables` mit `doc_id` | Vorhandene Tabellen, Zeilen und Werte | Übereinstimmung mit dem Original oder mit der Bestellung |
| `touchless_get_document_trace` mit `doc_id` | Ergebnis, Eingriffe, Läufe und aufgezeichnete Stufen | Nicht aufgezeichnete Arbeit in Infor |
| `touchless_explain_pipeline` mit `doc_id` | Erklärung des belegten Verarbeitungspfads | Automatisch bewiesene Grundursache bei fehlender Evidenz |

**Tatsächlich beobachteter Gegencheck:** Bei einer neuen Testrechnung meldete die Stufe `header_extraction` den Status `passed`, zugleich aber `extracted_field_count: 0`. `get_extracted_fields` lieferte acht leere Pflichtfelder; `get_extracted_tables` meldete keine Tabelle. Die Pflichtfeldprüfung blockierte mit `REQUIRED_FIELD_MISSING`. Ein Assistent muss hier fehlende Auslesewerte erklären und die Extraktionskonfiguration prüfen. Er darf aus dem grünen Stufenstatus keine richtige Auslesung und aus den abweichenden Bestellwerten noch keinen belegten Preisblocker ableiten.

### Zählt eine MCP-Aktion als AP-Eingriff?

Lesen und Erklären ändern die Rechnung nicht. Ein MCP-Zugang kann aber auch schreibende Werkzeuge bereitstellen. Korrekturen, manuelle Validierung und Neustarts sind deshalb gesondert zu beurteilen. Maßgeblich sind die tatsächlich aufgezeichnete Aktion und ihre Zuordnung zu einem Menschen oder Systemkonto. Ein API-Schlüssel kann als Systemkonto auftreten; „über MCP ausgeführt“ bedeutet allein weder menschlicher Eingriff noch Pure Touchless.

Prüfen Sie anschließend im Dokumentverlauf `human_touched`, `human_touch_source`, `human_restart_count`, `business_approval_touched`, den finalen Status und die Laufhistorie. Verwenden Sie keinen Systemzugang, um menschliche Nacharbeit bei der Kennzahl auszublenden. Eine reine fachliche Freigabe ist von einer gespeicherten Korrektur oder einem manuellen Neustart zu unterscheiden.

## Lieferanten über MCP priorisieren und Verbesserungen ableiten

> Welche Lieferanten verlieren im letzten Monat die meisten Touchless-Rechnungen? Prüfe zuerst die größten belegten Ursachen. Trenne Auslesefehler, abweichende Quelldaten und Prozessregeln. Schlage je Ursache eine Maßnahme und einen prüfbaren Erfolgsnachweis vor; ändere noch nichts.

1. Rufen Sie `touchless_rank_supplier_opportunities` mit `period: "30d"`, `doc_type: "INVOICE"`, `order_by_field: "lost_docs"` und `order_by_direction: "desc"` auf. Mit `search` suchen Sie gezielt nach Lieferantennummer oder Name. `limit` und `offset` steuern die Ergebnis-Seiten.
2. Übernehmen Sie den zurückgegebenen `supplier_key` unverändert in `touchless_diagnose_supplier`. Verwenden Sie für die aktuelle Lage `window: 30`; prüfen Sie mit 90 Tagen, ob die Ursache dauerhaft vorkommt.
3. Öffnen Sie ein tatsächlich geliefertes `issue_signature` mit `touchless_get_issue_cluster`. Kontrollieren Sie Beispieldokumente und die fehlende Evidenz. Verwenden Sie keine frei erfundene Signatur.
4. Lassen Sie mit `touchless_get_recommendations` die bestätigte Ursache und eine passende Maßnahme erklären. Ein erwarteter Zuwachs bleibt eine Schätzung. Überlappende Cluster dürfen Sie nicht einfach addieren.
5. Prüfen Sie nach der Behebung neue, vergleichbare Rechnungen und die [Änderungsmessung](touchless-change-proposals.md). Bereits manuell bearbeitete Rechnungen werden dadurch nicht rückwirkend Pure Touchless.

**Beispiel für die Entscheidung:** Sind Preis und Menge richtig ausgelesen, aber die importierten Bestellungen veraltet, lautet die Maßnahme „Bestellimport und Quellwerte korrigieren“. Sind Beträge bereits gegenüber dem Original falsch, prüfen Sie stattdessen Extraktion und Konfiguration. Ist nur eine fachliche Freigabe vorgeschrieben, ist das kein Auslesefehler und bei erfolgreichem Abschluss weiterhin AP Touchless.

Eine leere Rangliste ist kein Beweis, dass es keine Probleme gibt. Im Dev-Test mit drei noch laufenden Rechnungen war die Rangliste leer; daraus war noch keine abgeschlossene Lieferantenquote berechenbar. Prüfen Sie Datenstand, Filter, Lieferantenzuordnung und genügend abgeschlossene Dokumente.

## Verbesserungen über MCP: erst erklären, dann gezielt ändern

> Erkläre die wichtigsten bestätigten Ursachen. Liste unterstützte Änderungsvorschläge und zeige zuerst die Vorschau. Begründe Umfang und Risiken. Wende erst die konkret ausgewählte Änderung an und prüfe danach gespeicherten Wert, Änderungshistorie und messbare Wirkung.

| Schritt | MCP-Werkzeug und wichtige Eingaben | Ergebnis und Grenze |
| --- | --- | --- |
| Vorschläge lesen | `touchless_list_change_proposals`, optional `issue_signature`, `window: "30d"`, `lang: "de"` | Liefert vorhandene Vorschläge; speichert keine Konfiguration |
| Vorschau prüfen | `touchless_preview_change` mit dem zurückgegebenen `proposal_id` und derselben `issue_signature` | Zeigt den konkreten Umfang und liefert bei einer zulässigen Vorschau einen gebundenen `preview_token` |
| Ausgewählte Änderung speichern | `touchless_apply_change` mit genau diesen IDs, dem `preview_token` und denselben `overrides` und `window` wie in der Vorschau | **Schreibender Aufruf:** ändert die unterstützte Einstellung und liefert bei Erfolg eine `change_id` |
| Wirkung lesen | `touchless_verify_change` mit dieser `change_id` und demselben `window` | Liest die Vorher/Nachher-Messung; genügend geeignete abgeschlossene Dokumente bleiben erforderlich |

Übernehmen Sie IDs und Token aus echten Rückgaben. Eine Vorschau für einen Wert darf nicht zum Anwenden eines anderen Werts verwendet werden. Ist die Vorschau abgelaufen, nicht erlaubt oder unvollständig, ist kein erfolgreicher Änderungsfall belegt. Die Tabelle beschreibt den Werkzeugablauf; sie zeigt keine im Demo-Fall ausgeführte Änderung und keinen gemessenen Zuwachs.

**Beispiel „dauerhaft besser“:** Eine bestätigte Fehlkonfiguration verursacht wiederholt manuelle Eingriffe. Sie prüfen einen vorhandenen Vorschlag, speichern genau diese Änderung und kontrollieren anschließend neue Rechnungen. Erst eine Messung mit mindestens 20 geeigneten abgeschlossenen Dokumenten je Zeitraum liefert einen Vorher/Nachher-Wert. Steigt die AP-Touchless-Quote von 52 auf 61 %, sind das 9 Prozentpunkte beobachteter Unterschied, keine bewiesene alleinige Wirkung der Änderung.

**Beispiel „richtige Quelle“:** Eine falsche Bestellung in Infor benötigt eine fachliche Quellenkorrektur und einen geprüften Import. Dafür ist `touchless_apply_change` kein allgemeines Infor-Schreibwerkzeug. Bestätigen Sie zunächst den vereinbarten Preis, korrigieren Sie die verantwortliche Quelle und prüfen Sie den Import sowie die Ergebnisse neuer Rechnungen. Vergrößern Sie keine Toleranz, nur um falsche Quelldaten durchzulassen.

## Weiterführende Seiten

* [Touchless Intelligence](touchless-intelligence.md)
* [Kennzahlen und Berechnung](touchless-metrics.md)
* [Dashboard bedienen](touchless-dashboard.md)
* [Praxisbeispiele: Preis und Menge](touchless-examples.md)
* [Touchless Intelligence: Lieferantendiagnose und Fehlermuster](touchless-supplier-diagnosis.md)
* [Touchless Intelligence: Bestellabgleich-Diagnose](touchless-po-matching-diagnosis.md)
* [Touchless Intelligence: Dokumentverlauf](touchless-document-trace.md)
* [Touchless Intelligence: Änderungsvorschläge und Berichte](touchless-change-proposals.md)

<!-- Source notes (not shown): screenshots come from the dev test organisation with synthetic demo data (seed script) and fictional supplier names; the PO matching decision flow is illustrated on the matching-diagnosis subpage. facts read from the doc2app code (TouchlessIntelligence pages and components) and the dev UI on 14 Oct 2026; NOVA gates the tab with its own organisation flag, VESTA with the Analytics module. Consulting report export format not verified, so no export is described. -->
<!-- Doku-Prüfung 04.11.2026: Auslesequalität getrennt von Prozessergebnissen; Kennzahlen und Endergebnisse gegen DocBits_API c51f350c728acb8ac964098d15f7b006bce273f4, module/automation_intelligence/kpi.py und bucket.py, geprüft. Bestehende deutsche Originalaufnahmen getrennt von den Schulungsbeispielen geprüft. -->
<!-- Completion review 2026-11-04: AP actions, original-value evidence, overlapping KPI labels, sequential blockers and screenshot proof limits checked. -->
