# Touchless mit MCP erklären und verbessern

<!-- touchless-admin-video-v2-20261104:start -->
**Video-Kapitel (Prüffassung):** [Kennzahlen über MCP abfragen](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence-preview-admin/v2/de.html#chapter=12).
<!-- touchless-admin-video-v2-20261104:end -->

Die folgenden Abläufe verwenden Werkzeuge, die DocBits MCP tatsächlich anbietet. Unterscheiden Sie Lesen und Erklären vom Schreiben. Prüfen Sie Organisation, Rolle, Dokumenttyp, Zeitraum und Datenstand; erfinden Sie keine fehlenden Nachweise.

<figure><img src="../../../.gitbook/assets/touchless-owned-po-price-de.png" alt="Echte englische Dev-Ansicht einer eigenen fiktiven Bestellung: 10 × 9 = 90. Dies ist der Quellvergleich für die MCP-Diagnose, kein Screenshot eines MCP-Clients und kein Nachweis einer erfolgreichen Auslesung oder Verarbeitung."><figcaption><p>Echte englische Dev-Ansicht einer eigenen fiktiven Bestellung: 10 × 9 = 90. Dies ist der Quellvergleich für die MCP-Diagnose, kein Screenshot eines MCP-Clients und kein Nachweis einer erfolgreichen Auslesung oder Verarbeitung.</p></figcaption></figure>

## Touchless über MCP erklären

> Erkläre Pure Touchless, reine Freigabeergebnisse und die kombinierte AP-Quote für Rechnungen der letzten 30 Tage. Nenne Zähler, Nenner, laufende und ausgeschlossene Dokumente, Umfang und Datenstand. Halte die Korrektheit der Auslesung davon getrennt.

Verwenden Sie `touchless_get_summary` mit `period: "30d"` und `doc_type: "INVOICE"`. Verwenden Sie für einen Teilprozess nur Segmentfelder und Werte, die `touchless_list_segments` tatsächlich zurückgibt. Vergleichen Sie Dashboard und MCP mit derselben Organisation, demselben Dokumenttyp, Segment und Zeitraum; lesen Sie `data_as_of`.

**Geprüftes Dev-Gegenbeispiel:** Drei neu hochgeladene Testrechnungen waren noch `IN_PROGRESS`. Die Zusammenfassung lieferte `population.total: 3`, `population.in_progress: 3`, `population.eligible: 0` und `official_touchless_rate.ap_pct: null`. Es war noch keine Quote messbar. Das ist weder 0 % Auslesegenauigkeit noch 100 % Touchless. Die Eignung der Zusammenfassung bezieht sich hier auf die abgeschlossene KPI-Grundgesamtheit; ein einzelner Verlauf kann zugleich `eligible: true` und `bucket_final: false` zeigen.

Die MCP-Beispiele auf diesen fünf Seiten verwenden direkte, auf Dev geprüfte DocBits-MCP-Werkzeuge. Es gelten Organisation und Rolle Ihres verbundenen Kontos; eine Verfügbarkeit in einer anderen Oberfläche oder einer zusätzlichen Werkzeug-Freigabeliste ist mit diesem Test nicht belegt.

## FAQ

**DocBits hat alles korrekt ausgelesen. Warum ist die Rechnung AP assisted?**
Touchless misst den gesamten Prozess. Falsche oder veraltete Infor-Daten können auch bei korrekter Auslesung eine aufgezeichnete Korrektur oder einen manuellen Neustart erfordern. Prüfen Sie Originalrechnung, die von DocBits ausgelesenen Werte und die importierten Quelldaten getrennt.

**Sagt AP assisted, ob DocBits oder Infor die Arbeit verursacht hat?**
Nein. Es hält den Eingriff fest, nicht die Verantwortung. Nutzen Sie den Dokumentverlauf sowie das zugrunde liegende Dokument und die Quelldaten, um die Ursache zu bestätigen.

**Die Quoten zeigen einen Strich (—).** Im Zeitraum hat kein Dokument ein Endergebnis erreicht, oder es wurden weniger Dokumente als das Minimum gemessen. Dokumente, die noch in Bearbeitung sind, werden nicht gezählt.

**Der Tab fehlt.** Bitten Sie Ihren Administrator, das Modul zu aktivieren und Ihrer Rolle den Tab **Analytics dashboard** freizugeben.

**Ein Dokument zählt als bearbeitet, obwohl es diesmal ohne Eingriff durchlief.** Es wurde in einem früheren Lauf bearbeitet (eine Korrektur oder ein Neustart). Die Quote zählt die Arbeit, die tatsächlich stattgefunden hat.

**Warum ändert sich die Zahl nach einigen Stunden?** Das ERP bestätigt einen Export möglicherweise erst Stunden nach dem Versand. Das Ergebnis wird alle 15 Minuten neu berechnet.

**Ändert die KI von sich aus etwas?** Nein. Die KI schreibt nur Erklärungen. Eine Einstellung ändert sich erst, nachdem ein Administrator sie in der Vorschau geprüft und angewendet hat.

## Abweichungen über MCP untersuchen

> Prüfe Bestellnummer, Importstatus und die tatsächlich aktiven Abgleichsregeln dieser Rechnung. Trenne Auslesung, veralteten Import, falsche Quelldaten und fehlende Konfiguration. Ändere noch nichts.

1. Vergleichen Sie Original, `get_extracted_fields` und `get_extracted_tables`, bevor Sie eine korrekte Auslesung behaupten.
2. Verwenden Sie `get_po_sync_status` mit `po_number: "TL20261104X1-PO02"` und `language: "en"`. Der Dev-Test bestätigte einen verarbeiteten Import und eine vorhandene Bestellung. Das belegt die Ankunft, nicht die fachliche Richtigkeit oder den aktuellen Infor-Datensatz.
3. Verwenden Sie `touchless_get_document_trace` und `touchless_explain_po_match` mit derselben `doc_id`. Lesen Sie die tatsächliche Engine, die aktive Regelversion, Spalten und wirksamen Toleranzen. Nutzen Sie bei einem tatsächlich zurückgegebenen Fehlermuster dessen `issue_signature` in `touchless_get_po_match_evidence`.
4. Fehlende Nachweise bleiben als solche erhalten: unser neuer Testtyp lieferte `state: "none_published"` und `parse_error: "no published rule set"` sowie leere Auslesefelder. Ein Preis- oder Mengenblocker oder ein erfolgreicher Abgleich war damit nicht belegt. Ein allgemeiner Entscheidungsablauf ersetzt diese fehlenden Prüfungen nicht.
5. Beheben Sie die bestätigte Ursache und prüfen Sie neue Rechnungen. Eine menschliche Korrektur oder ein Neustart bleibt auch nach einem Erfolg relevant; ein endgültiger ERP-Fehler hat als Ausnahme Vorrang, und ein nicht abgeschlossenes Dokument liegt außerhalb des Quotennenners.

Halten Sie für einen vollständigen Fall das Original, die Auslesung vor der Korrektur, importierte und aktuelle Quellwerte mit Importzeitpunkt, die tatsächlichen Regeln, die AP-Aktion und das Endergebnis fest. Fehlende Nachweise bleiben offen.

## Die Nachweise über MCP lesen

> Untersuche diese Rechnung, ohne sie zu ändern. Vergleiche Original, aktuelle Felder und Tabellen. Erkläre die aufgezeichneten Schritte und Läufe und benenne fehlende historische Auslesenachweise.

| Werkzeug, jeweils mit derselben `doc_id` | Nachweis und Grenze |
| --- | --- |
| `get_extracted_fields` | Aktuelle Kopffelder und Konfidenz; kein historischer Stand |
| `get_extracted_tables` | Tatsächliche Tabellen und Zeilen; kein Nachweis, dass sie mit dem Original übereinstimmen |
| `touchless_get_document_trace` | Aufgezeichnete Ergebnisse, Eingriffe, Schritte und Läufe |
| `touchless_explain_pipeline` | Erklärung des belegten Verarbeitungspfads; füllt fehlende Nachweise nicht auf |

**Beobachtete Gegenprobe:** Unsere neue Testrechnung hatte einen `passed`-Schritt der Kopfdatenextraktion, aber `extracted_field_count: 0`, acht leere Pflichtfelder und keine Tabelle. Die Feldvalidierung blockierte mit `REQUIRED_FIELD_MISSING`. Der Assistent muss fehlende Auslesung oder fehlende Konfiguration untersuchen, statt aus einem grünen Schritt eine korrekte Auslesung oder aus abweichenden Quellwerten einen belegten Preisblocker abzuleiten.

### Zählt eine MCP-Aktion als menschlicher Eingriff?

Eine reine Leseprüfung ändert keine Rechnung. Andere MCP-Werkzeuge können Felder schreiben, validieren oder einen Neustart auslösen. Die Einordnung hängt vom aufgezeichneten Ereignis ab und davon, ob sein Akteur ein Mensch oder ein Systemkonto ist. Ein API-Schlüssel kann als Systemkonto handeln; „über MCP ausgeführt“ allein belegt weder einen menschlichen Eingriff noch Pure Touchless. Verwenden Sie niemals Systemzugangsdaten, um menschliche Nacharbeit zu verdecken.

Prüfen Sie nach einer Dokumentaktion `human_touched`, `human_touch_source`, `human_restart_count`, `business_approval_touched`, den finalen Status und die Läufe. Eine reine fachliche Freigabe ist von einer gespeicherten Korrektur, einer manuellen Validierung oder einem menschlichen Neustart zu unterscheiden.

## Lieferanten priorisieren und eine dauerhafte Verbesserung über MCP belegen

> Ordne die Lieferanten, die die meisten Touchless-Rechnungen verlieren. Trenne Auslesefehler, Abweichungen der importierten Quelle und Prozesseinstellungen. Schlage für jede bestätigte Ursache eine Maßnahme und eine prüfbare Erfolgskontrolle vor; ändere noch nichts.

1. Verwenden Sie `touchless_rank_supplier_opportunities` mit `period: "30d"`, `doc_type: "INVOICE"`, `order_by_field: "lost_docs"`, `order_by_direction: "desc"`. Mit `search` suchen Sie nach Lieferantennummer oder Name; `limit` und `offset` blättern durch die Ergebnisse.
2. Übergeben Sie den zurückgegebenen `supplier_key` unverändert an `touchless_diagnose_supplier`. Verwenden Sie `window: 30` für aktuelle Probleme oder 90, um wiederkehrende Probleme zu untersuchen.
3. Übergeben Sie ein tatsächlich zurückgegebenes `issue_signature` an `touchless_get_issue_cluster`. Prüfen Sie Beispieldokumente und fehlende Nachweise, bevor Sie die Ursache bestätigen. Erfinden Sie keine Kennungen.
4. Lassen Sie mit `touchless_get_recommendations` eine unterstützte Maßnahme erklären. Der erwartete Zuwachs ist eine Schätzung; überlappende Fehlermuster dürfen nicht einfach addiert werden.
5. Prüfen Sie nach der Behebung neue, vergleichbare Rechnungen und die [Änderungsmessung](touchless-change-proposals.md). Zuvor bearbeitete Rechnungen werden nicht rückwirkend Pure Touchless.

Bei korrekter Auslesung und veralteten Bestellungen korrigieren Sie Quelldaten und Import. Bei einer Abweichung zwischen Original und Auslesung untersuchen Sie die Extraktionskonfiguration. Eine durch Richtlinie vorgeschriebene Freigabe ist ein eigenes erfolgreiches AP-Touchless-Ergebnis. Eine leere Rangliste ist kein Beweis, dass es keine Probleme gibt: unsere drei laufenden Testrechnungen ergaben noch kein bewertetes Lieferantenergebnis. Prüfen Sie Umfang, Datenstand, Lieferantenerkennung und abgeschlossenes Volumen.

## Vorschau, Anwendung und Messung über MCP

> Erkläre die bestätigte Ursache und liste die unterstützten Vorschläge auf. Zeige die Vorschau der ausgewählten Änderung mit ihrem Umfang und ihren Risiken. Wende nur diese gewählte Änderung an und prüfe danach die gespeicherte Einstellung, die Änderungshistorie und die messbare Wirkung.

| Schritt | Werkzeug und tatsächlich zurückgegebene Kennungen | Was es belegt |
| --- | --- | --- |
| List | `touchless_list_change_proposals`, optional `issue_signature`, `window: "30d"`, `lang: "en"` | Verfügbare Vorschläge; keine Einstellung gespeichert |
| Preview | `touchless_preview_change` mit der zurückgegebenen `proposal_id` und passender `issue_signature` | Konkreter Umfang und ein gebundener `preview_token`, wenn zulässig |
| Apply selected change | `touchless_apply_change` mit denselben IDs, `preview_token`, `overrides` und `window` | **Schreibt** die unterstützte Einstellung; eine erfolgreiche Antwort liefert eine `change_id` |
| Read effect | `touchless_verify_change` mit dieser `change_id` und demselben `window` | Vorher/Nachher-Messung; weiterhin mindestens 20 geeignete abgeschlossene Dokumente je Zeitraum nötig |

Übernehmen Sie IDs und Token aus echten Antworten. Ein Token, der einen Wert in der Vorschau zeigt, kann keinen anderen Wert anwenden. Eine abgelaufene, verbotene oder unvollständige Vorschau ist kein Nachweis einer angewendeten Änderung. Reine Lesewerkzeuge und das Anwenden dürfen nicht als gleichwertig beschrieben werden. Diese Tabelle erklärt die Werkzeugfolge; sie behauptet nicht, dass die Demo einen Vorschlag ausgeführt oder einen Zuwachs gemessen hat.

**Beispiel Konfiguration:** Prüfen Sie nach einer bestätigten Konfigurationskorrektur den tatsächlich gespeicherten Wert und neue Rechnungen. 52 % vorher und 61 % nachher sind ein beobachteter Unterschied von 9 Prozentpunkten, kein Beweis dafür, dass allein diese Änderung ihn verursacht hat. **Beispiel Quelldaten:** Eine falsche Infor-Bestellung benötigt eine fachliche Korrektur und einen geprüften Import. `touchless_apply_change` ist kein allgemeines Werkzeug zum Schreiben in Infor. Erweitern Sie keine Toleranzen, um falsche Quelldaten zu verdecken.

Der Berichtsscreenshot zeigt Empfehlungen und geschätzte Wirkung, nicht die Anwendung oder eine Rücknahme. Eine erfolgreiche Anwendung braucht eine Erfolgsmeldung und einen Eintrag in der Historie. Undo ist nur verfügbar, wenn der gewählte Vorschlag es unterstützt; prüfen Sie die tatsächlich wiederhergestellte Einstellung. Das Neuladen der Historie wendet keine Einstellung an, und eine Rücknahme löscht frühere Dokumenteingriffe nicht.

## Weiterführende Seiten

* [Touchless Intelligence](./)
* [Kennzahlen und Berechnung](../../touchless-metrics.md)
* [Dashboard bedienen](touchless-dashboard.md)
* [Praxisbeispiele: Preis und Menge](touchless-examples.md)
* [Lieferantendiagnose und Fehlermuster](../../touchless-supplier-diagnosis.md)
* [Bestellabgleich-Diagnose](../../touchless-po-matching-diagnosis.md)
* [Dokumentverlauf](touchless-document-trace.md)
* [Änderungsvorschläge und Berichte](touchless-change-proposals.md)

<!-- Documentation review 2026-11-04: extraction quality vs process outcomes; KPI and terminal-outcome definitions checked against DocBits_API c51f350c728acb8ac964098d15f7b006bce273f4, module/automation_intelligence/kpi.py and bucket.py. Existing native screenshots retained and checked separately from illustrative examples. -->
<!-- Completion review 2026-11-04: owned synthetic PO examples, MCP schema/read evidence, human-action classification, KPI labels and screenshot proof limits. -->
