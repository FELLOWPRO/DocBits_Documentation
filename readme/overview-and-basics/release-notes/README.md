# Release-Notizen

> **Neueste Hotfix-Version:** [Hotfixes 12.–25. August 2026](incremental-updates-12-25-august-2026.md): Was sich mit dem Produktions-Upgrade vom 25. August 2026 geändert hat, von strengerer Trennung zwischen Organisationen bis zur Gutschrift-Erkennung bei E-Rechnungen. Alle Hotfix-Seiten finden Sie in der Navigation unter Release-Notizen.

## **Release R1.0 23./24. Mai 2026**

> **Sandbox-Verfügbarkeit:** 28. April 2026

### Neue Funktionen:

* **Activity Logging / Access Audit:**\
  Detailliertes Aktivitätsprotokoll und Access-Audit-Trail in der gesamten Anwendung für Compliance und Überwachung. Verschiedene Protokollierungstypen für alle Microservices und basierend auf Zeitraum.

* **Globale Schnellsuche:**\
  Drücken Sie Cmd+K / Ctrl+K von überall in der App, um in über 200 Routen und mehr als 40 In-Page-Funktionen zu suchen. Zeigt die Top-8-Ergebnisse mit Fuzzy-Matching, Navigation per Pfeiltasten und Links zur vollständigen App Index Page.

* **Sitemap (App Index Page):**\
  Durchsuchbare Indexseite, die jede navigierbare Seite und In-Page-Funktion (Dialoge, Seitenleisten, Panels) in DocBits katalogisiert. Organisiert in 18 Kategorien mit Typfiltern, Kategorie-Pills, URL-synchronisierter Suche und berechtigungsbasierten Einträgen, die für Nicht-Administratoren als gesperrt angezeigt werden.

* **Analytics Dashboard:**\
  Umfassende Analysen zur Dokumentenverarbeitung mit Executive Overview, API Metrics, Quality Metrics, Processing Performance, Document Flow Analytics, Activity Log, Event Log und Audit Trail.

* **Dashboard-Exportfunktion:**\
  Neue Dashboard-Exportfunktion, die einen Listenexport in den Formaten CSV oder XLSX ermöglicht.

* **Full-Text Search / DocSearch:**\
  KI-gesteuerte Vektorsuche über alle indizierten Dokumente mit Echtzeit-Lieferantenfilterung, "Find Similar"-Funktion und konfigurierbaren Indexierungseinstellungen.

* **Supplier Delivery Statistics:**\
  Neue Ansichten mit Einblicken in lieferantenbezogene Metriken der Dokumentenverarbeitung.

* **Debug Collector:**\
  Drücken Sie Ctrl+Shift+P, um einen vollständigen Debug-Snapshot zu erfassen, einschließlich API-Aufrufen, WebSocket-Status, Fehlern, Konsolen-Logs, Performance-Metriken und Umgebungsinformationen. Snapshots können in die Zwischenablage kopiert oder direkt als Support-Ticket mit einem HTML-formatierten Bericht und angehängter JSON-Datei gesendet werden.

* **AI Agents (DocNet):**\
  Autonome Hintergrundagenten, die eingehende E-Mails automatisch verarbeiten — Dokumente klassifizieren, extrahieren und weiterleiten, ohne manuelles Eingreifen. Agenten arbeiten zugewiesene Aufgaben selbstständig ab und eskalieren über Genehmigungsanfragen an Benutzer, wenn menschliches Urteilsvermögen erforderlich ist. Enthält ein dediziertes Agent-Dashboard zur Überwachung von Aktivität und Performance.

* **Neue E-Dokumente:**\
  Über 80 neue globale E-Invoice-Typen und mehr als 40 neue Formate, darunter XRechnung 3.0.2, ZUGFeRD 2.2/2.3.2, Factur-X-Varianten und Asia-Pacific PINT Credit Notes. 100 % Klassifizierungs- und Extraktionsabdeckung.

* **AI Script Chat:**\
  KI-gestützter Chat-Assistent für die grundlegende Skriptentwicklung mit Echtzeit-Streaming-Antworten.

* **Script Versioning:**\
  Vollständige Versionshistorie für Skripte mit Änderungsverfolgung, Vergleichs- und Wiederherstellungsfunktionen. Bietet Versionsverwaltung für Skripte ähnlich wie bei E-Docs.

* **Exporthistorie in Dashboard Actions:**\
  Zugriff auf die Exporthistorie eines Dokuments direkt aus dem Dashboard-Aktionsmenü.

* **Generic API Exporter (APS450, GLS840):**\
  Konfigurierbares generisches API-Exportziel über eine Mapping-File-Konfiguration für flexible Integration mit externen Systemen. Unterstützung für APS450 und GLS840 wurde implementiert.

* **Mehrere Export-Konfigurationen:**\
  Unterstützung für mehrere aktive Export-Konfigurationen pro Dokumententyp mit Ausführungsreihenfolge und einer Re-Export-Schaltfläche zum Wiederholen ab dem fehlgeschlagenen Schritt.

* **Neue Watchdog-Version:**\
  Vollständige Überarbeitung der WatchDog Settings-Seite. Neue Quality-of-Life-Funktionen wurden hinzugefügt, darunter der aktuelle WatchDog Status, Anleitung und Befehle für die Installation, XSLT-Template-Konfiguration und eine Einstellung für Autoupdate. Außerdem wurde die Funktionalität implementiert, dass WatchDog mehrere Konfigurationen gleichzeitig verarbeiten kann.

* **Vertex-Integration:**\
  Consumer Use Tax-Integration über Vertex für automatisierte Steuerberechnung und Compliance während der Dokumentenverarbeitung.

* **UI-Redesign & Einstellungs-Überarbeitung:**\
  Umfassende UI-Auffrischung in der gesamten Anwendung. Neu gestaltete Login- und Auth-Seiten. Neu gestalteter Einstellungsbereich mit einklappbarer Seitenleiste, organisierten Unterkategorien, ankerbasierter Navigation, Kontext-Hilfe-Panel und Status-Tracking-Badges. UI-Änderungen bei Dokumentenskripten. Neue UI für Document Flow. Verbesserte List of Values-UI.

* **Idea Board:**\
  Feature-Request-Board, auf dem Benutzer neue Funktionen, Verbesserungen, benötigte Bugfixes usw. einreichen, diskutieren und abstimmen können — mit Rich-Text-Editor und Bildunterstützung.

* **API Key Management:**\
  Dedizierte Einstellungsseite zum Erstellen, Anzeigen und Verwalten mehrerer API-Schlüssel.

* **Master Data Lookup-Suchfunktion:**\
  Verbesserte Suchfunktionen für Stammdaten durch geeignete Suchoptionen basierend auf den ausgewählten Feldern.

* **User Activity Chart:**\
  Visuelles Diagramm, das Muster der Benutzeraktivität und Engagement-Metriken anzeigt. Dashboard für Login-Aktivität mit Trendvergleichsdiagrammen, täglicher/wöchentlicher Aggregation und GeoLite2-basierter Geolokalisierung.

* **User Login History:**\
  Users Detail View mit Login-Historie.

* **Anpassbare Seitenleiste:**\
  Drag-and-drop-Neuanordnung, Umschalter zum Ein-/Ausblenden und Pin-to-top für Menüeinträge der Seitenleiste. Einstellungen werden pro Benutzer persistiert, mit einer "Reset to default"-Option. Feature-Flags werden berücksichtigt.

* **Video Carousel:**\
  Autoplay-Video-Carousel auf der Prepare-Dashboard-Seite, das kurze animierte Produkt-Tipp-Videos zeigt (Global Search, Keyboard Shortcuts, Document Upload, Table Customization). Zweispaltiges Layout mit Videos links und Dashboard-Vorbereitung rechts. Auto-Redirect pausiert, während Benutzer Videos ansehen.

* **Advanced Workflow Designer:**\
  Visueller, knotenbasierter Automatisierungs-Builder mit Drag-and-Drop-Canvas für mehrstufige Verarbeitungspipelines. Unterstützt Wait-Steps, parallele Pfade, wiederverwendbare Templates, Or-Condition-Cards, manuelle Test-/Run-Schaltfläche, "Test from Here"-Teilausführung und Ausführungslogs pro Knoten mit visueller Flow-Hervorhebung, die genau zeigt, welche Knoten ausgeführt wurden.

* **Workflow KPI Dashboard:**\
  Dashboard mit Kennzahlen zur Überwachung der Workflow-Ausführung.

* **Workflow Partner Card SDK:**\
  SDK für Drittanbieter-Entwickler zum Erstellen benutzerdefinierter Workflow-Karten, mit KI-gestützter Überprüfung, Sandbox-Validierung und Getting-Started-Dokumentation.

* **Workflow Test Manager:**\
  Automatisierter Test-Manager für Workflows, der Administratoren ermöglicht, Tests einzeln oder im Massenbetrieb zu erstellen und auszuführen.

### Verbesserungen:

* **Datenbank (alle Module) — Migration von ID-Spalten:**\
  Alle "ID"-Datenbankspalten in DocBits wurden intern von Zeichenketten auf einen dedizierten ID-Typ (UUID7) migriert. Die zugrunde liegende Postgres-Datenbank wurde auf V18 migriert, um diese Verbesserung zu unterstützen.

* **Dokumentenverarbeitung — Weitere Verbesserungen:**\
  Die Exportlogik in Bezug auf die maximale Anzahl zu berücksichtigender Seiten wurde geändert — jetzt wird das gesamte Dokument exportiert. Während der Dokumentenvalidierung hat der Benutzer die Möglichkeit, das Standardlimit für die maximale Seitenanzahl für dieses spezifische Dokument zu überschreiben. Die Berechnung des Pending Document Counter wurde verbessert.

* **Service-Versionen, Status & Bereitstellungsdatum:**\
  Der Service-Verfügbarkeitsstatus wird im "Service Versions"-Popup bereitgestellt.

* **Spracherweiterung:**\
  Unterstützung auf 22 Sprachen erweitert, mit aktualisierter Sprachauswahl.

* **Access-Control-Design auf Feldebene:**\
  Neu gestaltete/verbesserte Zugriffssteuerung mit klarerem Aktivierungszustand, Zugriff auf Feldebene, konsistenter Regelbehandlung und vereinfachten gruppenbasierten Berechtigungen. Behebt Regelkonflikte zwischen Access Control und View Permissions, zeigt den Import-Owner in der UI an und wendet die Zugriffssteuerung konsistent auf Feldvalidierung, KI-extrahierte Tabellen und alle Ansichten an.

* **Activity Stream für alle Bildschirme:**\
  Der Activity Stream ist jetzt auf allen Dokumentenverarbeitungs-Bildschirmen verfügbar (Ready for Validation, PO Matching, Accounting, Quote Details, Reject) — nicht nur bei Pending Approval. Auf eine konsistente Position im rechten Panel auf allen Bildschirmen verschoben.

* **Document-Flow-Seite:**\
  Dedizierte Seite zur Visualisierung und Nachverfolgung des Dokumentenverarbeitungsflusses, die Statusübergänge und Fortschritt durch die Pipeline anzeigt.

* **Dual Monitor Mode (Globale Benutzereinstellung):**\
  Dual Monitor Mode wurde in eine globale Benutzereinstellung verschoben und bleibt über Sitzungen hinweg bestehen.

* **Layout-Builder-Verbesserungen:**\
  Unterstützung für versteckte und schreibgeschützte Felder mit visuellen Indikatoren, größenveränderlichem Panel-Trennstrich und Einstellungen zur Feldlänge. Anwenden des Default Layouts auf mehrere Origins, ohne jedes einzeln öffnen zu müssen.

## **Release HotFix 3 16. April 2026**

### DocBits-Verbesserungen:

* **QR-Code-Extraktion für polnische Rechnungen:**\
  DocBits unterstützt jetzt die QR-Code-Extraktion speziell für polnische Rechnungen und verbessert damit die automatisierte Datenerfassung für Dokumente aus Polen.

### Bugfixes:

* Behoben: Auto-Export schlug fehl, wenn PO Matching bereits stattgefunden hatte, die Bestellung aber nicht mit dem Dokument verknüpft war.
* Behoben: Einzelpreise wurden bei Rechnungen mit Verpackungseinheiten (VPE) falsch gerundet.
* Behoben: Export-Fehlermeldungen von ION/MEC (z. B. Acknowledge.PurchaseOrder-Fehler) wurden in DocBits nicht angezeigt, und der Status "Exported" wurde angezeigt, obwohl der Export fehlgeschlagen war.
* Behoben: Der Einzelpreis auf dem Approval Screen war falsch, wenn AI Table Extraction verwendet wurde.
* Behoben: Das Total Matching-Skript warf einen Fehler auf dem Validierungsbildschirm.
* Behoben: Die Dokumentenverarbeitung schlug mit einem Fehler fehl ("UserAuthentication object has no setter for 'org_id'").
* Behoben: Table Training funktionierte bei bestimmten Lieferanten nicht; Spalten landeten in versteckten Spalten statt in den zugeordneten Feldern.
* Behoben: PO Matching schlug bei großen Rechnungen (10+ Seiten) fehl, weil das Größenlimit für Multipart-Requests überschritten wurde.
* Behoben: Skriptbefüllte Spaltenwerte wurden nach einem Dokument-Neustart nicht beibehalten.
* Behoben: Der "Ignore Table Validation"-Toggle wurde in der UI als aktiv (grün) angezeigt, war im Hintergrund jedoch deaktiviert.
* Behoben: Die Dokumentenqualität war nach dem Import deutlich reduziert.
* Behoben: Microservice-Versionen und Bereitstellungsdaten wurden in der App nach einem vollständigen Deployment-Push über Umgebungen hinweg inkonsistent angezeigt.
* Behoben: Die Barcode-Extraktion schlug aufgrund eines Fehlers beim Erstellen des User-Authentication-Objekts aus Task-Daten fehl.
* Behoben: Kontaktdaten von Lieferanten wurden beim Speichern im Supplier Portal geleert.
* Behoben: Dokumente liefen beim Export in einen NoneType-Fehler.
* Behoben: Der E-Mail-Body wurde nicht einbezogen, wenn die erste angehängte Datei ein PNG- oder JPEG-Bild war.
* Behoben: Der E-Mail-Body fehlte bei mehreren Dokumenten.
* Behoben: Der DocBits Operator "ai-exporting" lieferte keine Exportergebnisse in den Zielsystemen (LN/D3).

## **Release HotFix 2 31. März 2026**

### DocBits-Verbesserungen:

* **Hybride PDF-Verarbeitung — Benutzergesteuerte XML-Extraktion:**\
  Wenn ein PDF eingebettete XML-Daten enthält, können Benutzer jetzt wählen, ob DocBits die eingebetteten XML-Daten für die Extraktion verwenden oder das Dokument als Standard-PDF verarbeiten soll. Dies gibt Organisationen die volle Kontrolle darüber, wie hybride Dokumente verarbeitet werden, und stellt sicher, dass die für ihren Workflow am besten geeignete Extraktionsmethode angewendet wird.

* **AP Assignment Code auf dem Approval Screen:**\
  Die AP Manager Approval-Seite enthält jetzt ein AP Assignment Code-Feld, integriert mit Infor M3 CRS620. Dies ermöglicht es Genehmigern, Assignment Codes direkt während des Genehmigungsprozesses zu überprüfen und zu bestätigen, ohne zu externen Systemen wechseln zu müssen.

* **PO-Gesamtabgleich mit Dokumentensumme:**\
  DocBits unterstützt jetzt den Abgleich der Bestellsumme mit der Gesamtsumme auf dem Dokument und bietet eine zusätzliche Validierungsebene beim PO-Matching, um Abweichungen früher im Prozess zu erkennen.

* **Aktualisierung von Lieferanten-Artikelnummer und VPE:**\
  DocBits unterstützt jetzt die Aktualisierung der Felder Lieferanten-Artikelnummer und VPE (Verpackungseinheit) während der Dokumentenverarbeitung, wobei die Werte beim Export zurück nach M3 synchronisiert werden.

* **Verbesserte Dokument-Layout-Klassifizierung:**\
  Die Dokument-Layout-ID (tfidf_id) wird jetzt nur basierend auf dem Kopftext generiert, ohne Fußzeilentext. Dies verbessert die Klassifizierungsgenauigkeit, indem verhindert wird, dass Fußzeileninhalte die Dokumenttyp-Erkennung beeinflussen.

* **Export & Next Button:**\
  Ein neuer "Export & Next"-Button wurde hinzugefügt, der es Benutzern ermöglicht, das aktuelle Dokument zu exportieren und sofort zum nächsten in der Warteschlange überzugehen, was den Überprüfungs- und Export-Workflow optimiert.

* **Genehmigungsprozess für Kostenrechnungen:**\
  Der Genehmigungsprozess für Kostenrechnungen wurde mit verbesserter Routing- und Validierungslogik erweitert.

### Fehlerbehebungen:

* Ein Problem wurde behoben, bei dem der Infor SFTP-Export aufgrund eines falschen Library-Befehls mit einem Fehler fehlschlug.
* Ein Problem wurde behoben, bei dem boolesche Checkboxen nicht auf dem Approval Screen angezeigt werden konnten.
* Ein Problem wurde behoben, bei dem UNMU-Nachrichten gesendet wurden, obwohl keine Abweichungen in der Bestelleinheit vorlagen.
* Ein Problem wurde behoben, bei dem die Umsatzsteuer auf dem PO-Matching-Bildschirm fälschlicherweise als Zuschlag klassifiziert wurde, was zu einem negativen offenen Betrag führte.
* Ein Problem wurde behoben, bei dem der Export fehlschlug, wenn die Bestelleinheit nicht in der Auftragsbestätigung festgelegt war, aber in der Bestellung vorhanden war.
* Ein Problem wurde behoben, bei dem der E-Mail-Text bei mehreren Dokumenten fehlte.
* Ein Problem wurde behoben, bei dem die Lieferanten-Artikelnummer auf dem Approval Screen nicht sichtbar war und Aktualisierungen nicht an M3 gesendet wurden.
* Ein Problem wurde behoben, bei dem der Lieferantenexport zu Infor einen Fehler zurückgab.
* Ein Problem wurde behoben, bei dem PO-Matching während der Verarbeitung Fehler produzierte.
* Ein Problem wurde behoben, bei dem die `findAll`-Funktion in Dokumentskripten nicht korrekt funktionierte.
* Ein Problem wurde behoben, bei dem die Watchdog-Spalte "Updated By" fälschlicherweise den Fellow Admin-Benutzer anstelle des tatsächlichen Benutzers anzeigte.
* Ein Problem wurde behoben, bei dem BOD-Mapping in der Watchdog-UI nicht konfiguriert werden konnte.
* Ein Problem wurde behoben, bei dem Zuschläge fälschlicherweise als offene Beträge anstatt als Zuschläge angezeigt wurden.
* Ein Problem wurde behoben, bei dem der automatische Abgleich bei mehrzeiligen Rechnungen trotz vorhandener Abgleichskonfiguration nicht funktionierte.
* Ein Problem wurde behoben, bei dem ein Bindestrich ("-") in der Artikelnummer beim PO-Matching für die Bestellung berücksichtigt, aber auf der Rechnung ignoriert wurde, was zu einer falschen Abweichung führte.
* Ein Problem wurde behoben, bei dem sowohl PDF- als auch XML-Dateien in den Exportordner hochgeladen wurden, obwohl der "Export PDF"-Schalter deaktiviert war.
* Ein Problem wurde behoben, bei dem ein fehlender Status auf der Workflow-Karte verhinderte, dass Dokumente den Workflow durchliefen.
* Ein Problem wurde behoben, bei dem die Dokumentqualität nach dem Import erheblich verschlechtert war.
* Ein Problem wurde behoben, bei dem der PO-Match-Bildschirm einen Fehler auslöste ("Cannot read properties of null").
* Ein Problem wurde behoben, bei dem die Standard-Werteliste nicht bearbeitet werden konnte.
* Ein Problem wurde behoben, bei dem der Workflow den Feldstatus nicht korrekt lesen konnte, was zu einer fehlerhaften Weiterleitung führte.
* Ein Problem wurde behoben, bei dem eingehende E-Mail-Importe mit einem Fehler fehlschlugen.
* Ein Problem wurde behoben, bei dem fehlende Positionen beim Export nicht korrekt in M3 ankamen.
* Ein Problem wurde behoben, bei dem codierte und genehmigte Rechnungen gelegentlich nicht über die APS110-API auf den Status "genehmigt" in M3 aktualisiert wurden.
* Ein Problem mit der Multi-Banking-Konfiguration wurde behoben, die nicht korrekt funktionierte.
* Mehrere Probleme mit der Anzeige und dem Speicherverhalten von geteilten Dashboards wurden behoben.
* Ein Problem wurde behoben, bei dem das Feld Lieferanten-Artikelnummer auf 30 Zeichen begrenzt war, was die Speicherung längerer Werte verhinderte.
* Ein Problem wurde behoben, bei dem Stückpreis- und Stückpreis-pro-Werte beim Export einen Fehler verursachten.
* Ein Problem wurde behoben, bei dem PO-Positionen mit einem ausgeschlossenen Status (z. B. "Closed") auf dem PO-Matching-Bildschirm trotz Ausschluss durch Matching-Regeln weiterhin gezogen und abgeglichen werden konnten.

### Konfigurationsänderungen:

* E-Mail-Vorlagen wurden aktualisiert, um den "Go to Task"-Button zu entfernen.
* Skripte und Pflichtfeld-Einstellungen für Kostenelemente wurden angepasst.

## **Release HotFix 1 16. März 2026**

### DocBits-Verbesserungen:

* **Dokumenthistorie im SFTP-Export:**\
  DocBits unterstützt jetzt die Einbeziehung der vollständigen Dokumenthistorie als Teil der exportierten XML-Nutzlast beim Export über SFTP. Diese Funktion ist über die Export Settings konfigurierbar und stellt nachgelagerten Systemen einen vollständigen Audit-Trail aller Statusänderungen und Aktionen zur Verfügung, die an einem Dokument in DocBits vorgenommen wurden — einschließlich wer die Änderung vorgenommen hat, wann sie erfolgte und was der vorherige und aktuelle Status war. Dies ist besonders wertvoll für Compliance, Nachverfolgbarkeit und operative Analyse.
* **Zuschlagsaktualisierung bei Auftragsbestätigung für Infor On Premise:**\
  Infor On Premise-Kunden können jetzt Auftragsbestätigungen mit Zuschlägen direkt in DocBits verarbeiten. Die Zuschläge werden vollständig über den Export aktualisiert, wodurch der End-to-End-Auftragsbestätigungsprozess nahtlos wird und manuelle Anpassungen im nachgelagerten System entfallen.
*   **Standard-Layout auf alle Origins anwenden:**\
    Ein neuer **Apply Default Layout to Origins**-Button wurde im Layout-Konfigurationsbildschirm eingeführt. Administratoren können jetzt das Standard-Layout mit einer einzigen Aktion auf alle Origins innerhalb einer Organisation übertragen, wodurch der zeitaufwändige manuelle Prozess des Kopierens und Einfügens von Layout-JSON für jede Origin einzeln entfällt. Dies ist besonders nützlich beim Onboarding neuer Kunden, bei dem mehrere Origins konsistent konfiguriert werden müssen.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/image%20(5).png)
*   **Dokumenttyp-Auswahl für FTP-Import:**\
    FTP-Import-Konfigurationen unterstützen jetzt die ordnerspezifische Dokumenttyp-Zuweisung. Bei der Konfiguration eines FTP-Imports können Benutzer angeben, welcher Dokumenttyp — wie Rechnung oder Auftragsbestätigung — auf alle aus diesem Ordner importierten Dokumente angewendet werden soll. Dokumente werden beim Import automatisch klassifiziert, wodurch eine manuelle Dokumenttyp-Zuweisung nach der Aufnahme entfällt. Dies unterstützt Organisationen, die mehrere Dokumenttypen über verschiedene Unterorganisationen und Ordner verwalten.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/image%20(4).png)
* **Export nach GLS840 für Infor On Premise:**\
  DocBits unterstützt jetzt den Export von Dokumenten in das GLS840-Programm für Infor On Premise-Kunden und erweitert damit die Palette der unterstützten Exportziele für On-Premise-Umgebungen.
*   **UI-Verbesserungen für Watchdog und Export-Konfiguration:**\
    Die Watchdog-Konfigurations- und Export-Konfigurationsbildschirme wurden mit einer verbesserten Benutzeroberfläche aktualisiert, die ein übersichtlicheres Layout und eine intuitivere Erfahrung für Administratoren bietet, die diese Einstellungen verwalten.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/image%20(1).png)

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/image%20(2).png)

### Fehlerbehebungen:

* Ein Problem wurde behoben, bei dem Benutzer mit gültigen Anzeigerechten keine Dokumente anzeigen konnten — die Berechtigungslogik wurde mit einer Zugriffsebenen-Prüfung anstelle des bisherigen gruppenbasierten Filteransatzes überarbeitet.
* Die Ausnahmebehandlung wurde in mehreren Bereichen der Anwendung für mehr Stabilität verbessert.
* Ein Problem wurde behoben, bei dem boolesche Spaltentypen während der Feldextraktion nicht korrekt verarbeitet wurden.
* Ein asynchrones Authentifizierungsproblem im Datei-Upload-Endpunkt wurde behoben.
* UI-Anzeigeprobleme für die PO-Tabelle auf dem Validierungsbildschirm wurden behoben.
* Die Skriptvorlage wurde aktualisiert, um Änderungsverfolgungs-Kommentare für bessere Nachvollziehbarkeit einzubeziehen.
* Ein Problem mit Dropdown-Feldern wurde behoben, die sich auf dem Validierungsbildschirm nicht korrekt verhielten.
* Ein Problem wurde behoben, bei dem das Unterorganisations-Feld beim Aktualisieren von Dokumentzuweisungen vom Dashboard nicht vorausgefüllt war.

## **Release Winter Summit 10. Dezember 2025**

### DocBits-Verbesserungen:

*   **Erweiterte Anpassung der PO-Matching-Regeln:**\
    DocBits bietet nun eine präzisere und anpassbarere Kontrolle über Bestellabgleichsregeln. Administratoren können genau festlegen, welche Spalten während des Abgleichsprozesses für jeden Dokumenttyp ausgewertet werden sollen, um sicherzustellen, dass nur die relevantesten Felder berücksichtigt werden. Zusätzlich können Toleranzen auf Spaltenebene definiert werden, was eine größere Flexibilität bei der Behandlung kleinerer Abweichungen ermöglicht. Jede Regel kann so konfiguriert werden, dass sie für manuellen Abgleich, automatischen Abgleich oder beides gilt, wodurch Teams die Möglichkeit erhalten, den Abgleichsworkflow genau an ihre betrieblichen Anforderungen anzupassen. Diese Verbesserungen erhöhen die Anpassungsfähigkeit und Präzision des Bestellabgleichsprozesses erheblich.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/release_notes_12_2025_3.png)
*   **Unterstützung für mehrere Finanzkonten von Lieferanten:**\
    DocBits unterstützt nun die Verwaltung mehrerer Finanzkonten für Lieferanten über die von Infor bereitgestellte RemitToPartyMaster BOD. Diese Verbesserung ermöglicht es Organisationen, mehrere Zahlungsempfänger-Kontodatensätze für einen einzelnen Lieferanten zu verwalten, was die Flexibilität und Genauigkeit bei der Zahlungsabwicklung verbessert. Eine neue Konfigurationseinstellung wurde eingeführt, um diese Funktion zu aktivieren oder zu deaktivieren, sodass Administratoren die Funktion basierend auf ihren betrieblichen Anforderungen aktivieren können.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/release_notes_12_2025_1.png)
*   **Benutzerzugriff auf OCR-Extraktionsergebnisse hinzugefügt:**\
    Die Schaltfläche **OCR-Ansicht** auf dem Feldvalidierungsbildschirm ist jetzt für alle Benutzer verfügbar, die Validierungszugriff haben, und nicht mehr nur auf Administratoren beschränkt. Mit diesem Update kann jeder autorisierte Benutzer OCR-Extraktionsergebnisse direkt überprüfen, was die Validierung der Datengenauigkeit erleichtert und die Überwachung der gesamten OCR-Leistung verbessert. Diese Verbesserung fördert größere Transparenz und verbessert die Effizienz des Validierungsworkflows.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/release_notes_12_2025_2.png)
* **Dynamisches Spalten-Rendering in Genehmigungsbildschirmen:**\
  Verbesserte Genehmigungsansichten zur dynamischen Anzeige nur der Spalten, die für den Vergleich in den Datenbankeinstellungen jeder Organisation konfiguriert sind. Zuvor erschienen einige organisationsspezifische Spalten leer, wenn sie nicht für den Vergleich konfiguriert waren, was zu Verwirrung führte. Jetzt zeigen Genehmigungsansichten nur Felder an, die aktiv verglichen werden. Dies bietet klarere, organisationsspezifische Genehmigungsbildschirme ohne leere oder irrelevante Spalten.
* **Bestelltypfeld zur Stammdatensuche hinzugefügt**:\
  Die Bestellkopfliste enthält nun eine Spalte "Bestelltyp" in der Stammdatensuche, die zusätzliche Kategorisierungsmöglichkeiten bietet.
* **Verbesserungen am Dashboard für benutzerdefinierte Filter:**\
  Die Dashboard-Freigabefunktion wurde verbessert, um freigegebenen Benutzern mehr Flexibilität zu bieten. Personen, für die Dashboards freigegeben wurden, können jetzt die Dashboard-Filter anpassen und bearbeiten, sodass sie die angezeigten Informationen an ihre spezifischen Bedürfnisse anpassen können. Diese Verbesserung unterstützt ein personalisierteres und interaktiveres Betrachtungserlebnis und stellt sicher, dass Benutzer die für ihre Aufgaben relevantesten Dateneinblicke einfach verfeinern können.
* **Anpassbare Präfixe für Genehmigungsbildschirmspalten:**\
  Eine neue konfigurierbare Option wurde eingeführt, um Präfixe vor Dokumentspalten auf Genehmigungsbildschirmen anzuzeigen. Diese Funktion kann direkt im Layout-Builder verwaltet werden und gibt Administratoren die volle Kontrolle darüber, ob Präfixe angezeigt werden und auf welche Dokumenttypen sie angewendet werden. Durch Aktivierung dieser Option erhalten Benutzer einen klareren Kontext und eine verbesserte Lesbarkeit beim Überprüfen von Dokumenten während des Genehmigungsprozesses.

### Allgemeine Verbesserungen

* Verbesserte Fehlerprotokollierung für schlecht trainierte Tabellen bei der Tabellenextraktion.
* Eine Freigabegrenze für Dashboards von bis zu 10 Benutzern oder 5 Gruppen wurde hinzugefügt, zusammen mit einer klaren Fehlermeldung, wenn die Grenze erreicht ist.
* Verbesserte Fehlerbehandlung für benutzerdefinierte Dashboards, wenn ein Benutzer versucht, ein Dashboard mit einem Namen zu erstellen, der bereits existiert.

### Fehlerbehebungen:

* Ein Problem wurde behoben, bei dem E-Mails erfolgreich aus dem Abschnitt Lieferantendetails gesendet zu werden schienen, aber nicht an Empfänger zugestellt wurden.
* Ein Problem wurde behoben, bei dem Dropdown-Felder, die zu Genehmigungs-/Ablehnungsbildschirmen hinzugefügt wurden, nicht angezeigt wurden.
* Ein Problem wurde behoben, bei dem alle exportierten Dokumente als zuletzt aktualisiert vom falschen Benutzer markiert wurden.
* Ein Problem wurde behoben, bei dem Dokumente den Status "Workflow in Bearbeitung" anzeigten, aber keine Workflows ausgeführt wurden und das Protokoll leer blieb.
* Ein Problem wurde behoben, bei dem nicht verwandte Benutzer Dokumenten zum Exportzeitpunkt zugewiesen wurden, ohne daran gearbeitet zu haben.
* Ein Problem wurde behoben, bei dem Benutzer mit korrekten Berechtigungen zugewiesene Dokumente nicht ablehnen konnten und Fehler erhielten.
* Ein Problem wurde behoben, bei dem Dokumentfluss-Symbole für einige Organisationen nicht angezeigt wurden.
* Ein Problem wurde behoben, bei dem ein Popup erschien, wenn Dokumente per Drag & Drop auf das Dashboard hochgeladen wurden.
* Ein Problem wurde behoben, bei dem E-TEXT-Flags in der Benutzeroberfläche als aktiviert angezeigt wurden, obwohl die API-Antwort alle Werte als falsch anzeigte.
* Ein Problem wurde behoben, bei dem ein Fehler auftrat, wenn Dokumente mit leeren Seiten hochgeladen wurden.
* Ein Problem wurde behoben, bei dem Aufgaben-Hyperlinks in E-Mail-Benachrichtigungen Benutzer nicht zum richtigen Genehmigungsbildschirm weiterleiteten.
* Ein Problem wurde behoben, bei dem die Auswahl der übergreifenden Unterorganisation dazu führte, dass die Stammdatenabfrage keine Lieferanten anzeigte. Benutzer können nun korrekt organisationsübergreifende Lieferantendaten anzeigen.

## Release Autumn Summit 22. Oktober 2025

### DocBits-Verbesserungen:

*   **Verbesserungen im E-Mail-Vorlagendesign:**

    Der E-Mail-Vorlagen-Editor wurde neu gestaltet, um eine klarere Struktur und ein reibungsloseres Erlebnis zu bieten. Die Auswahl von Dokumentfeldern ist jetzt intuitiver, und Anhänge können direkt in Vorlagen eingefügt werden. Diese Verbesserungen machen es schneller und einfacher, professionelle, maßgeschneiderte E-Mails zu erstellen.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fdv4oDlfkRyD0W9yWGAA4%252Fimage.png%3Falt%3Dmedia%26token%3D14bf7ebd-d886-4758-8184-d7b94447518a\&width=768\&dpr=4\&quality=100\&sign=88405d9c\&sv=2)
*   **Dashboard-Verbesserungen:**

    Das Dashboard wurde erweitert, um die Navigation und Anpassung zu verbessern. Mit neuen Registerkarten können Benutzer schneller zwischen verschiedenen Dokumenttypen wechseln und so die Zeit für die Suche nach der richtigen Ansicht verkürzen.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FmpO7WSIrkL0I8Rje3HQt%252Fimage.png%3Falt%3Dmedia%26token%3D77d03fe7-e626-4645-b191-e332715a25fb\&width=768\&dpr=4\&quality=100\&sign=93fa9925\&sv=2)
*   **Benutzerdefinierte Filter-Dashboards:**

    Darüber hinaus können Dashboards jetzt nach individuellen Vorlieben angepasst und gefiltert werden. Diese benutzerdefinierten Dashboards können auch mit Kollegen geteilt werden, um die Erstellung konsistenter teamweiter Berichtsansichten zu erleichtern.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fn5rPvGnRltT3mTIDoJwV%252Fimage.png%3Falt%3Dmedia%26token%3D22d065e3-81eb-4f16-828c-7f9134c25b1b\&width=768\&dpr=4\&quality=100\&sign=eb11d3a3\&sv=2)
*   **E-Mail-Benachrichtigungsprotokolle:**

    Eine neue Protokollfunktion steht für alle E-Mail-Benachrichtigungen zur Verfügung. Benutzer können jetzt eine Historie der gesendeten Benachrichtigungen überprüfen, was es einfacher macht, Lieferungen zu überprüfen und Probleme zu beheben, wenn E-Mails nicht empfangen werden.
*   **E-Rechnungsunterstützung: e-SLOG 1.6 & 2.0:**

    Die Unterstützung für zusätzliche E-Rechnungsformate wurde eingeführt. Das System kann jetzt e-SLOG-Versionen 1.6 und 2.0 verarbeiten und generieren, was die Kompatibilität mit Partnern und behördlichen Anforderungen erweitert.
*   **Duplikaterkennungsverbesserungen:**

    Die Duplikaterkennung wurde mit zwei leistungsstarken Konfigurationsoptionen aktualisiert. Das **Duplikaterkennungsintervall** ermöglicht es Ihnen, einen Zeitraum festzulegen, um Duplikate genauer zu überprüfen, während die Einstellung **Export von Duplikaten verbieten** automatisch das Exportieren von Dokumenten verhindert, die als Duplikate erkannt wurden. Zusammen bieten diese Verbesserungen mehr Kontrolle und gewährleisten eine höhere Datenpräzision.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FXHRKTmuSxTlDt9lDEkE7%252Fimage.png%3Falt%3Dmedia%26token%3D96b56af6-c644-4b0f-a488-8bc16a03c11f\&width=768\&dpr=4\&quality=100\&sign=9b723b7f\&sv=2)
*   **Entscheidungsbaum-Verbesserungen:**

    Entscheidungsbäume sind jetzt vielseitiger und können Dokumentfeldwerte zurückgeben. Dies ermöglicht eine fortschrittlichere Automatisierungslogik, die Workflows basierend auf tatsächlichen Dokumentdaten Entscheidungen treffen lässt.
*   **Neue Workflow-Karten:**

    Zwei neue Workflow-Karten erweitern die Automatisierungsmöglichkeiten. Die erste ermöglicht es Ihnen zu überprüfen, ob ein Dokument zu einer bestimmten Unterorganisation gehört, was die Handhabung von Multi-Entity-Setups erleichtert. Die zweite führt eine Lieferdatumstoleranzprüfung ein, die Liefertermine gegen das aktuelle Datum in Arbeitstagen vergleicht, um die Verwaltung und Durchsetzung von Lieferanforderungen effektiver zu gestalten.
*   **CSV-Exportverbesserungen:**

    Die CSV-Exportfunktion wurde erheblich verbessert. Anstatt nur die auf der aktuellen Seite angezeigten Dokumente zu exportieren, exportiert das System jetzt alle Dokumente in einem Datensatz. Jeder Export erstellt einen Protokolleintrag, und die resultierende CSV wird automatisch per E-Mail gesendet, was einen vollständigeren und zuverlässigeren Exportprozess bietet.
*   **Zeitrahmen für den Löschvorgang von Bestellungen:**

    Eine neue Konfigurationsoption ermöglicht es Administratoren, einen Zeitrahmen für das Löschen von Bestellungen festzulegen. Diese Verbesserung bietet Flexibilität und Kontrolle über die Datenaufbewahrungspolitik und stellt sicher, dass Bestellungen nur entfernt werden, wenn dies angemessen ist.

### Fehlerbehebungen

* Ein Problem wurde behoben, bei dem alte Daten beim Exportieren von Dokumenten enthalten waren.
* Der Filter für Exportfehler wurde korrigiert, der zuvor auch andere Status angezeigt hatte.
* Ein Tabellenvalidierungsfehler wurde behoben, bei dem "Stückpreis" Fehler auslöste, "Stückpreis pro" jedoch nicht, obwohl die Werte korrekt waren.
* Ein Problem wurde behoben, bei dem das Hinzufügen einer neuen Spalte zum Dashboard fehlschlug.
* Ein Problem wurde behoben, bei dem Aufgaben in der Dashboard-Aufgabenspalte nicht sichtbar waren.
* Das zufällige Sortierverhalten wurde behoben, sodass Listen jetzt einer konsistenten Reihenfolge folgen.
* Ein Problem wurde behoben, bei dem das Ändern der Spaltenbreite nicht gestoppt werden konnte.
* Ein Fehler wurde behoben, der das manuelle Zeilenabgleichen im PO-Matching-Bildschirm verhinderte.
* Ein Problem wurde behoben, bei dem die E-Mail-Anhangsoption nach dem Speichern zurückgesetzt wurde.
* Ein Problem wurde behoben, bei dem die automatische Kontierung anfangs Datenbank-IDs anzeigte, wenn sie zum ersten Mal geöffnet wurde.
* Das unscharfe Feldverhalten wurde korrigiert, sodass Werte nicht mehr falsch überschrieben werden.
* Ein Problem wurde behoben, bei dem Felder in der automatischen Kontierung nach dem Löschen des Inhalts verschwanden.
* Ein Fehler wurde behoben, bei dem der Benutzer "Vorname" und "Nachname" im Einstellungspopup nicht umbenennen konnte.
* Ein Problem wurde behoben, bei dem Dokumente im Status "Workflow in Bearbeitung" stecken bleiben konnten.
* Ein Menüsymbolfarbenproblem wurde behoben, bei dem ausgewählte Organisationsfarben nicht korrekt angewendet wurden.
* Ein Problem wurde behoben, bei dem QR-Codes manchmal nicht erkannt wurden.
* Ein Problem wurde behoben, bei dem Konten nicht mit der Rücktaste entfernt werden konnten, um ein anderes einzugeben.
* Ein Sprachproblem wurde behoben, nachdem nach dem Produktionspush eingeloggt wurde.

## Release Summer Bloom Juni 2025

### DocBits Verbesserungen:

* **Filteroption für E-Mail-Importprotokoll:** Benutzer haben jetzt die Möglichkeit, die Importprotokolle zu filtern und die Tabelle zu sortieren, um einen klareren und effizienteren Überblick zu erhalten. Diese Verbesserung vereinfacht den Prozess der Identifizierung und Verwaltung von E-Mail-Einträgen, verbessert die Fehlersuche und das allgemeine Protokollmanagement.
*   **Mehrsprachige Unterstützung für Wertelisten:** Wir haben die mehrsprachigen Funktionen für die Wertelisten erweitert. Administratoren können jetzt Bezeichnungen in mehreren Sprachen definieren, um sicherzustellen, dass die korrekte Bezeichnung basierend auf den Systemspracheinstellungen des Benutzers automatisch angezeigt wird. Diese Verbesserung fördert eine bessere Zugänglichkeit und Lokalisierung und erleichtert es Benutzern weltweit, mit der Plattform in ihrer Muttersprache zu interagieren.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fw0aRFGUP9FAyqyiV5mtE%252Fimage.png%3Falt%3Dmedia%26token%3Da0e6db9b-1dd3-497b-938b-30ae52b55fad\&width=768\&dpr=4\&quality=100\&sign=b66949c7\&sv=2)
* **Benutzerdetailverbesserungen in den Einstellungen:** Die Einstellungsschnittstelle zeigt jetzt umfassende Benutzerinformationen an. Administratoren können problemlos Gruppenzugehörigkeiten, Unterorganisationsdetails und zusätzliche Schlüsseldaten anzeigen, um eine bessere Verwaltung von Benutzerrollen und ein klareres Verständnis der Teamstrukturen zu ermöglichen.
* **Automatische Buchhaltungsinformationen auf dem Genehmigungsbildschirm:** Der Genehmigungsbildschirm zeigt jetzt automatische Buchhaltungsdetails neben Rechnungsinformationen an. Diese Verbesserung bietet tiefere Einblicke in Transaktionsdaten, erleichtert den Überprüfungsprozess und trägt zu fundierteren Entscheidungen bezüglich Rechnungen bei.
* **Aufgabenzähler für Dokumente auf der Dashboard-Ansicht:** Dokumente auf dem Dashboard können jetzt offene Aufgaben anzeigen, die mit ihnen verbunden sind, und die Gesamtzahl der ausstehenden Aufgaben anzeigen. Diese Funktion bietet Benutzern einen schnellen Überblick über ausstehende Aktionen, verbessert das Aufgabenmanagement und die Arbeitsabläufe.
* **Lieferantenbasierte KI-Modellauswahl:** Benutzer können jetzt das KI-Modell für die Datenauslese auf Lieferantenbasis auswählen. Diese Verbesserung ermöglicht eine fein abgestimmte Optimierung und gewährleistet eine bessere Extraktionsgenauigkeit für verschiedene Lieferanten, was zu einer Verbesserung der Gesamtergebnisse bei der Datenverarbeitung führt. [Weitere Informationen](https://docs.docbits.com/end-user-and-partner-section/end-user-section/validation-screen#supplier-based-ai-model)
* **Verbesserte Workflow-Protokolle für Entscheidungsbaumkarten:** Die Protokolle zeigen jetzt die Ausgabe des Entscheidungsbaums an, was es einfacher macht, nachzuvollziehen und zu verstehen, wie Entscheidungen innerhalb von Arbeitsabläufen getroffen wurden.
*   **Einführung eines neuen automatisierten Test-Setups zur Verbesserung der Systemfunktionalität und -stabilität:**

    Wir freuen uns, die Implementierung eines neuen automatisierten Testsystems bekannt zu geben, das entwickelt wurde, um die Gesamtfunktionalität und Zuverlässigkeit unserer Plattform zu verbessern. Dieses neue Setup führt konsistente, gründliche Überprüfungen unseres Systems durch, um Probleme zu identifizieren, bevor sie sich auf Ihre Erfahrung auswirken. Durch die Automatisierung dieser Tests können wir schnell auf potenzielle Probleme reagieren und die höchsten Qualitätsstandards für unser System aufrechterhalten.
* **Implementierung der Microservices-Architektur:** Wir haben die Plattform umstrukturiert, indem wir Kernkomponenten in dedizierte Microservices aufgeteilt haben. Diese architektonische Änderung verbessert die Skalierbarkeit, die Leistung des Systems und ermöglicht schnellere, modularere Entwicklungs- und Bereitstellungszyklen.
*   **Schritt-für-Schritt-Anleitung:** Eine geführte Schritt-für-Schritt-Anleitung steht jetzt zur Verfügung, um Benutzern zu helfen, sich einfacher durch verschiedene Teile der Anwendung zu navigieren und zu verstehen. Dies ist besonders nützlich für die Einarbeitung neuer Benutzer oder die Erkundung von unbekannten Funktionen.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FwrgjrN07rIbIHELm0M5J%252Fimage.png%3Falt%3Dmedia%26token%3Dc0efeedb-74d3-4045-b386-32347ef6f938\&width=768\&dpr=4\&quality=100\&sign=ba1377b5\&sv=2)
* **Verbesserungen am Entscheidungsbaum:** Es wurden Verbesserungen an der Benutzeroberfläche des Entscheidungsbaums vorgenommen, einschließlich einer intuitiveren Funktion zum Hinzufügen von Zeilen - jetzt oben im Baum -, um die Wartung und Bearbeitung zu vereinfachen.
* **DocOperator, DocNet und Erweiterungstools:** Neue KI-gestützte Tools wie DocOperator und DocNet helfen dabei, wiederkehrende Aufgaben zu automatisieren, die Effizienz zu steigern und den manuellen Aufwand in Dokumenten-Workflows zu reduzieren.
*   **Vorschauoption für elektronische Dokumente:** Eine Vorschauoption wurde für elektronische Dokumente (eDocs) hinzugefügt, die es Benutzern ermöglicht, Änderungen direkt in den Einstellungen zu testen und anzuzeigen, bevor sie bereitgestellt werden.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FJk6p8EDzpVFYcA39IGHz%252Fimage.png%3Falt%3Dmedia%26token%3De0cc3fcd-dda3-4d54-bdea-ec9853cf47cb\&width=768\&dpr=4\&quality=100\&sign=d4558e6f\&sv=2)
* **Neue Sprachunterstützung – Chinesisch:** DocBits unterstützt jetzt Chinesisch und erweitert die Zugänglichkeits- und Lokalisierungsoptionen für Benutzer auf globalen Märkten.
* **Verbessertes Aufgaben-Dashboard:** Das Aufgaben-Dashboard wurde verbessert, um eine größere Anzahl von Aufgaben gleichzeitig anzuzeigen, was Benutzern einen klareren Überblick verschafft und die Aufgabenverfolgung verbessert.
*   **PO-Abgleichsverbesserungen:**

    Hinzufügen von visuellen Indikatoren für verschiedene Abgleichszustände

    Neue Einstellung, um bereits abgeglichene PO-Positionen pro Dokumenttyp zu ignorieren

    Verbesserte automatische Überprüfung von PO-Aktualisierungen, um Konsistenz sicherzustellen
* **Layout-Builder-Verbesserungen:** Sie können jetzt sowohl nach Feldnamen als auch nach Feldtiteln suchen, um die Konfiguration und Lokalisierung von Layoutkomponenten schneller und einfacher zu gestalten.
* **Export- und Weiter-Button im Genehmigungsbildschirm:** Ein neuer Button wurde dem Genehmigungsbildschirm hinzugefügt, der es Benutzern ermöglicht, ein Dokument zu exportieren und automatisch zum nächsten in der Warteschlange "Bereit zur Validierung" fortzufahren.
* **Neue Workflow-Karten:** Neue Workflow-Karten wurden eingeführt, darunter solche für die Ausführung von Workflows bei neuen Bestellungen und angebotsbezogenen Ereignissen. Diese bieten mehr Automatisierungsoptionen.
*   **Watchdog-Verbesserungen:** Die Watchdog-Konfiguration wurde in die Hauptanwendungs-Benutzeroberfläche verschoben, um das Management zu erleichtern. Es wurden auch zusätzliche Funktionen eingeführt, um eine bessere Übersicht und Steuerung zu ermöglichen.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FMHotfPG2e9zQHmphSM46%252Fimage.png%3Falt%3Dmedia%26token%3Dddd51783-b6db-4e24-bdf4-13fbed12ec3d\&width=768\&dpr=4\&quality=100\&sign=e4673df5\&sv=2)
* **Linienablehnungsverbesserungen:** Das Ablehnen eines Positionsartikels erfordert jetzt, dass Benutzer einen Grund angeben, um eine bessere Rückverfolgbarkeit und Verantwortlichkeit in Überprüfungs-Workflows sicherzustellen.
* **Lieferanten-KI-Modellliste in den Einstellungen:** Eine neue Ansicht in den Einstellungen zeigt die den spezifischen Lieferanten zugewiesenen KI-Modelle an, zusammen mit einer Option zum Zurücksetzen. Dies verbessert die Transparenz und Verwaltbarkeit von lieferantenbasierten KI-Konfigurationen.
*   **Dokumentenprotokollverbesserungen:** Die Dokumentenprotokolle enthalten jetzt detailliertere Informationen zur Unterstützung einer besseren Prüfung und Fehlerbehebung.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FrpoqkVrrEnufVoYyv06W%252Fimage.png%3Falt%3Dmedia%26token%3D3d2ca7c1-93d2-4f79-a5a0-77d5acfafdc6\&width=768\&dpr=4\&quality=100\&sign=5e720823\&sv=2)
* **PNG- und JPG-Unterstützung:** Sie können jetzt PNG- und JPG-Dateien hochladen, die automatisch in das PDF-Format für die Verarbeitung konvertiert werden.
* **IDM-Exportdokumentformatkonfiguration:** Das Exportformat für PDFs in IDM kann jetzt konfiguriert werden, um Benutzern mehr Kontrolle darüber zu geben, wie Dokumente generiert werden.
* **Neuer eDoc-Typ – EDIFACT INVOIC02:** Wir unterstützen jetzt den elektronischen Dokumententyp EDIFACT INVOIC02, um die Kompatibilität mit standardisierten Rechnungsformaten zu erweitern.

### Fehlerbehebungen:

* Behoben: Ein Problem, bei dem Aufgaben nicht auf dem Validierungs-/Genehmigungsbildschirm angezeigt wurden.
* Positionierung des Next/Previous-Buttons wurde behoben, sodass er statisch bleibt.
* Behoben: Scrollprobleme in den Skript- und Entscheidungsbaumansichten, um sicherzustellen, dass Aktionsbuttons beim Scrollen stationär bleiben.
* Entfernt: Das Feld Ursprungsland aus E-Rechnungen.
* Behoben: Ein Problem mit dem Aufgabenanzähler, der eine ungenaue Anzahl von Aufgaben anzeigte.
* Hinzugefügt: Fehlende Übersetzungen.
* Korrigiert: Benutzerdefinierte Felder zeigen jetzt beschreibende Namen anstelle von IDs.
* Behoben: Ein Problem, bei dem Dokumente mit einem falschen Dateinamen heruntergeladen wurden.
* Behoben: Sortierinkonsistenzen in der Rechnungszeilentabelle beim PO-Abgleich.
* Behoben: Ein Problem, das die Funktionalität der Aufgabenerstellung beeinträchtigte.
* Behoben: Ein Problem im PO-Abgleich, bei dem die Sortierung der Rechnungstabelle zurückgesetzt wurde, wenn eine Zeile abgeglichen wurde.
* Behoben: Automatische Buchhaltungsprobleme, indem sichergestellt wurde, dass Buchungsreferenzen korrekt aufgeteilt werden, wenn ein Betrag geteilt wird.
* Aktualisiert: Informationen zum ClickHouse-Host.
* Behoben: Ein Problem, bei dem doppelte Dokumente nicht als Duplikate erkannt wurden.
* Behoben: Exportprobleme aufgrund von zu langen Buchungsreferenzen.
* Behoben: Ein Problem, bei dem Kontrollkästchen, die als schreibgeschützt markiert waren, nicht schreibgeschützt waren.
* Behoben: Ein Problem, bei dem Benutzer zweimal einer Unterorganisation hinzugefügt werden konnten.
* Behoben: Ein Problem, bei dem das Ändern der Unterorganisation für ein Dokument dazu führte, dass der zugewiesene Benutzer oder die zugewiesene Gruppe zurückgesetzt wurde.
* Behoben: Einige Probleme mit der Auto-Buchhaltungsoberfläche.
* Behoben: Ein Problem, bei dem Benutzer keine FTP-Konfiguration hinzufügen konnten.
* Behoben: Ein Problem mit dem SSO-Login.
* Behoben: Einige Probleme im Zusammenhang mit eingehenden E-Mails.
* Behoben: Ein Problem, bei dem Dokumente einen falschen Namen erhielten, wenn sie heruntergeladen wurden.
* Behoben: Ein Problem, bei dem der Entscheidungsbaum ein falsches Ergebnis zurückgibt.​

## Release Hot Fix Winter Frost 10. April 2025

### DocBits Verbesserungen:

* **Verbesserte** **`set_column_date_value`** **Script-Funktion:** Die `set_column_date_value` Funktion unterstützt jetzt die `skip_weekend` Option, die es ermöglicht, dass Datumswerte automatisch Wochenenden überspringen, wenn sie angewendet werden.
* **Verbesserte Unterstützung für Datei-Uploads:** PNG- und JPEG-Dateien können jetzt direkt hochgeladen werden und werden automatisch in das PDF-Format konvertiert, um die Dokumentenverarbeitung zu optimieren.
* **Verbesserungen der Watchdog-Funktionalität:**
  * Unterstützt jetzt den Export nach **Enaio** für eine bessere Systemintegration.
  * Verbesserte Parsing-Fähigkeiten zum Extrahieren von Informationen aus `Sync.ContentDocument` XML-Strukturen, was eine effizientere Datenverarbeitung ermöglicht.

### Fehlerbehebungen

* Ein Problem mit einer Script-Funktion wurde behoben.
* Ein Problem wurde gelöst, bei dem Bestellungen nach ihrer Aktualisierung einen falschen Status hatten.

### Release Hot Fix Winter Frost 11. März 2025

#### DocBits Verbesserungen:

* **Verbesserte Datenextraktion:** Eine Option wurde hinzugefügt, um die **Bestellnummer** oder **Artikelnummer** aus einer Zeile darüber oder darunter zu extrahieren.
* **Erweiterter Zugriff auf Cross Sub-Organizations:** Nicht-Admin-Benutzer können jetzt auch auf die Funktion **Cross Sub-Organizations** zugreifen.

#### **Fehlerbehebungen:**

* Ein Problem wurde behoben, bei dem Benutzer nicht zu einer Gruppe hinzugefügt werden konnten.
* Ein Problem mit E-Mail-Importfehlern wurde behoben.
* Ein Problem mit dem Feldtraining bei Dokumenten mit mehr als einer Seite wurde behoben.
* Ein Problem wurde behoben, bei dem Skripte nicht richtig funktionierten.
* Ein Problem wurde behoben, bei dem die Dokumentendaten nicht korrekt angezeigt wurden.
* Ein Problem bei der Einstellung Automatische Prüfung auf PO-Aktualisierungen wurde behoben.
* Ein Problem behoben, bei dem die Abonnement-Token falsch angezeigt wurden
* Ein Problem gelöst, bei dem der Aufgabenbildschirm eine veraltete Dokumentversion anzeigte
* Ein Problem behoben, das dazu führte, dass Dokumente ihren Status nicht änderten

Release Winter Frost – 22. Januar 2025\\

### Neue Funktionen

#### Unterstützung für ZUGFeRD 2.1 und neuer

DocBits unterstützt nun vollständig die ZUGFeRD-Versionen 2.1 und höher, was eine nahtlose Handhabung und Verarbeitung elektronischer ZUGFeRD-konformer Rechnungen ermöglicht. Die Integration stellt Folgendes sicher:

* **Kompatibilität:** DocBits kann ZUGFeRD-Rechnungen sowohl in ihrer strukturierten (XML) als auch unstrukturierten (PDF) Form verwalten und erfüllt dabei EU-Standards wie EN 16931 für E-Rechnungen.
* **Effizienz:** Benutzer können ZUGFeRD-E-Rechnungen mühelos importieren, validieren und Daten extrahieren. Dadurch werden manuelle Dateneingaben minimiert und die Bearbeitungszeit verkürzt.
* **Flexibilität:** Egal ob Basis-, Komfort- oder Extended-Profil innerhalb des ZUGFeRD-Standards – DocBits bietet die passenden Werkzeuge für jede Komplexitätsstufe von Rechnungen.
* **Zukunftssicherheit:** Durch die Unterstützung neuerer ZUGFeRD-Versionen bleibt DocBits stets konform mit den sich ändernden E-Rechnungsrichtlinien in den EU-Mitgliedstaaten und darüber hinaus.

### Externe API-Integration zur verbesserten Dokumentenverarbeitung

DocBits bietet nun die Möglichkeit, externe APIs bei der Dokumentenverarbeitung einzubinden, um Vollständigkeit und Genauigkeit der extrahierten Daten zu erhöhen. Diese Erweiterung reduziert den manuellen Aufwand erheblich, indem fehlende Felder in Echtzeit mit aktuellen Informationen aus vertrauenswürdigen Quellen gefüllt werden. So können Dokumente schneller und konsistenter verarbeitet werden.

### Cross Sub-Organisations Access (Zugriff auf mehrere Unterorganisationen)

Für Organisationen, die mit mehreren Unterorganisationen arbeiten, führt DocBits eine neue Funktion namens Cross Sub-Organisations ein. Damit können Administratoren die Dokumentenverwaltung für alle Unterorganisationen unter einem Dach vereinheitlichen.

* Admin-Benutzer können Dokumente aus allen Unterorganisationen einsehen, ohne zwischen ihnen wechseln zu müssen.
* Diese zentrale Sicht erlaubt es Administratoren, alle Dokumente zugleich zu überblicken und schnell zu finden, was sie benötigen.

<figure><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F7ACd08FD5ORqjs15FD1L%252FCrossSubOrganisations.png%3Falt%3Dmedia%26token%3Daeab8cc8-e1dc-495e-ac45-10a10c5fbf29&#x26;width=768&#x26;dpr=2&#x26;quality=100&#x26;sign=b1383f40&#x26;sv=2" alt=""><figcaption></figcaption></figure>

### Dokumentensichtbarkeit basierend auf Gruppenberechtigungen

DocBits erweitert die Steuerung der Dokumentensichtbarkeit, um den Zugriff für Nicht-Admin-Benutzer präziser zu regeln. Dank gruppenbasierter Berechtigungen können Administratoren festlegen, welche Dokumente für welche Benutzer bzw. Gruppen sichtbar sind.

• Admin-Benutzer können Dokumente bestimmten Gruppen zuweisen.

• Nur Mitglieder der jeweiligen Gruppe sehen die zugeordneten Dokumente.

<figure><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FyQ8h5SjkjoY861mevbiD%252FGroup%2520Based%2520Permission.png%3Falt%3Dmedia%26token%3D7f6ef368-1f27-4241-bfad-9ead54119586&#x26;width=768&#x26;dpr=2&#x26;quality=100&#x26;sign=6d0957ba&#x26;sv=2" alt=""><figcaption></figcaption></figure>

### Sequentieller Workflow und Freigabehistorie

Mit der neuen Funktion Sequentieller Workflow und Freigabehistorie steigert DocBits die Effizienz bei der Dokumentenverarbeitung und fördert die Nachverfolgbarkeit von Aktionen.

#### Sequentielle Workflow-Steuerung:

* Dokumente können in einer festgelegten Reihenfolge an mehrere Benutzer zur Prüfung oder Freigabe übergeben werden.
* Jeder beteiligte Benutzer erhält eine Benachrichtigung, sobald er an der Reihe ist, was Missverständnisse und Verzögerungen reduziert.
* Workflows lassen sich individuell an die Geschäftsprozesse anpassen.\\

Dadurch erhalten Benutzer nur die für ihre Aufgaben relevanten Dokumente, was für einen fokussierten und sicheren Workflow sorgt.

#### Freigabehistorie:

* Ein vollständiges Protokoll aller Aktionen steht in den Ansichten „Validierung“ und „Freigabe“ zur Verfügung.
  * Es enthält Benutzeraktionen (z. B. „freigegeben“, „abgelehnt“)
  * Zeitstempel
  * Kommentare/Notizen.
* Die Historie erhöht die Transparenz und dient als Prüfpfad für Compliance und Fehlersuche.

<figure><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FdoXNLPvi6N4iGyHaLBiV%252FApproval%2520History.png%3Falt%3Dmedia%26token%3D9ca81a61-7649-4064-8b74-931ce0487007&#x26;width=768&#x26;dpr=2&#x26;quality=100&#x26;sign=4067ed8c&#x26;sv=2" alt=""><figcaption></figcaption></figure>

#### SFTP/FTP-Dokumentenarchiv-Erweiterung

Diese Neuerung baut auf der bestehenden Importfunktionalität von DocBits auf und bietet eine unkomplizierte Methode, Dateien nach ihrer Verarbeitung zu archivieren.

• Eine neue Einstellung in der FTP-Importkonfiguration ermöglicht es, das Archivieren von Dateien zu aktivieren oder zu deaktivieren.

• Nach erfolgreicher Verarbeitung werden die Dateien automatisch in einem definierten Ordner auf dem SFTP/FTP-Server abgelegt (falls die Option aktiviert ist).

So bleiben verarbeitete Dateien archiviert, ohne die aktiven Importverzeichnisse zu überfüllen.

Mehrere Steuerbereiche für Steuertypen und Export zu Infor LN

Mit dieser Funktion erweitert DocBits die Handhabung von Steuerinformationen, indem sie detaillierte Klassifizierung und den Export der Daten an Infor LN ermöglicht (z. B. volle Steuer, reduzierte Steuer, steuerfrei). Dies unterstützt komplexe Steuerstrukturen und verbessert die Integration in Buchhaltungssysteme.

\\

<figure><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FreOhCz7IXoNej2VRdkpt%252FSFTPArchieve.png%3Falt%3Dmedia%26token%3D90b802f5-670e-476f-99e8-847efefc376e&#x26;width=768&#x26;dpr=2&#x26;quality=100&#x26;sign=44ac45e8&#x26;sv=2" alt=""><figcaption></figcaption></figure>

### Mehrfache Steuerbereiche pro Steuertyp:

* DocBits unterstützt jetzt mehrere Steuerbereiche unter jedem Steuertyp wie:
  * Voller Steuersatz (z. B. Standard-Mehrwertsteuer).
  * Reduzierter Steuersatz (z. B. für bestimmte Güter oder Dienstleistungen).
  * Steuerfrei (z. B. Ausnahmen für bestimmte Transaktionen).
* Diese Unterteilung ermöglicht eine präzise Kategorisierung von Steuerbeträgen und gewährleistet die Einhaltung von Vorschriften und Buchhaltungsstandards.

#### Dynamische Auto-Accounting-Integration:

* Die relevanten Steuerbereiche werden auf dem Auto-Accounting-Bildschirm automatisch anhand der während der Dokumentenverarbeitung extrahierten Daten angezeigt.
* Benutzer können Steuerbuchungen ohne manuelle Nachberechnung oder erneute Eingabe schnell validieren und anpassen.

#### Export zu Infor LN:

* Steuerdaten einschließlich aller relevanten Bereiche und Klassifizierungen werden nahtlos an Infor LN exportiert, um die Konsistenz zwischen DocBits und dem ERP-System sicherzustellen.
* Exportierte Daten werden mit den entsprechenden Kostenzeilen in Infor LN verknüpft, was eine klare Nachverfolgbarkeit und genaue Finanzberichterstattung ermöglicht.

<figure><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FxLvKHYq3zfdXkF36sy1u%252FMultipleTaxLInes.png%3Falt%3Dmedia%26token%3Db1e1e1df-546b-48e7-9dc9-e64de55376b6&#x26;width=768&#x26;dpr=2&#x26;quality=100&#x26;sign=76515c28&#x26;sv=2" alt=""><figcaption></figcaption></figure>

<figure><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FOvvtRhwfcoMX26GHx30O%252FMultipleTaxLineAuto%2520Accounting.png%3Falt%3Dmedia%26token%3D370213a4-f361-42e5-9cc4-ca1304fdb3c8&#x26;width=768&#x26;dpr=2&#x26;quality=100&#x26;sign=f37fe5f5&#x26;sv=2" alt=""><figcaption></figcaption></figure>

### Dashboard-Verbesserungen

DocBits hat wesentliche Aktualisierungen im Dashboard vorgenommen, die sich auf Benutzerfreundlichkeit, Effizienz und bessere Datenübersicht konzentrieren. Zu den Verbesserungen gehören ein neuer “Assigned To Group”-Filter und ein optimiertes UI für Dokumentenprotokolle (Document Logs), damit Benutzer einfacher interagieren und Dokumente verwalten können.

### PO Matching-Verbesserungen

Um den Prozess des Abgleichs von Bestellpositionen (PO) mit Rechnungen zu vereinfachen, hat DocBits zahlreiche Verbesserungen in der PO-Matching-Ansicht implementiert.

**Strg + Klick für einzelne Zeilenauswahl:**

* Benutzer können mit gedrückter Strg-Taste auf spezifische Zeilen klicken, um mehrere, nicht zusammenhängende Zeilen auszuwählen.

**Shift + Klick für Bereichsauswahl:**

* Wird die Shift-Taste gedrückt gehalten, so kann über den Klick auf eine erste und eine letzte Zeile ein zusammenhängender Bereich ausgewählt werden.

**Automatische Erkennung veralteter Daten:**

* Ist die zu einer Rechnung gehörige Bestellinformation veraltet (basierend auf den Systemeinstellungen), wird ein Symbol angezeigt, um den Benutzer darauf hinzuweisen. So erkennen Anwender schnell, ob es sich um veraltete Daten handelt, die eventuell nicht den neuesten Stand wiedergeben.

### Bug-Fixes

* Ein Problem wurde behoben, um sicherzustellen, dass bei den Auto-Accounting-Prozessen alle möglichen Werte korrekt angezeigt werden.
* Das Benutzerinterface der Workflow-Logs wurde verbessert, um die Navigation und Bedienung intuitiver zu gestalten.
* Die Dokumentenfelder zeigen nun weitere Informationen wie erforderliche oder ausgeblendete Flags direkt in der Benutzeroberfläche an.
* Die Beschreibungen von Gruppen sind in den Gruppeneinstellungen nun sichtbar.
* Die Zeichenlängenbeschränkung für Gruppennamen wird beim Erstellen angezeigt, um Fehler zu vermeiden.
* Probleme mit der Testfunktion im Entscheidungsbaum und Übersetzungsinkonsistenzen wurden beseitigt.
* Die Suchfunktion in den Workflow-Logs wurde verbessert, um präzisere und effektivere Ergebnisse zu liefern.
* Ein Fehler wurde behoben, der verhinderte, dass Benutzer versehentlich E-Dokument-Entwürfe löschen konnten.
* Verschiedene Fehler im E-Mail-Importprozess wurden korrigiert, um eine reibungslose Integration und Datenverarbeitung zu gewährleisten.
* Probleme beim Speichern von KI-generierten Tags wurden behoben, sodass die Daten konsistent erhalten bleiben.
* Ein Sortierfehler, der beim Seitenwechsel im Dashboard auftrat, wurde behoben.
* Der Dokumentenzähler zeigt nun korrekt die Anzahl der von DocBits verarbeiteten Dokumente an.
* Verbesserte Übersetzungen in der gesamten Anwendung steigern die Benutzerfreundlichkeit in verschiedenen Sprachen.

## Release Hot Fix Feast 17. Dezember 2024

DocBits-Verbesserungen:

Erweiterungen beim E-Mail-Import

Benutzer können jetzt XML- und EDI-Dateien nahtlos über die E-Mail-Importfunktion importieren.

Release Hot Fix Feast 27. November 2024

### DocBits-Verbesserungen:

• Erweiterte PO-Optimierung

• Optimierter Speichervorgang: Der Speichervorgang findet jetzt nur statt, nachdem der Benutzer den Abgleich abgeschlossen hat, um redundante Speicherungen zu reduzieren und die Effizienz zu steigern.

• Erweiterter asynchroner Export

Die Exportfunktionalität wird nun asynchron ausgeführt, was für reibungslosere Abläufe und ein insgesamt verbessertes Benutzererlebnis sorgt.

\\

#### Workflow-Verbesserungen

Die Workflow-Funktionalität wurde aktualisiert, um ein besseres Nutzererlebnis zu bieten:

• Verbesserte Protokolle: Die Workflow-Protokolle verfügen jetzt über eine übersichtlichere und intuitivere Oberfläche, die das Überprüfen und Verstehen von Prozessdetails erleichtert.

• Optimierte Reaktionsfähigkeit: Die Workflow-Ausführungsprozesse wurden für schnellere und zuverlässigere Performance optimiert, um Aufgaben zügiger abzuschließen und Verzögerungen zu minimieren.

#### Verbessertes Anwendungs-Caching

Wir haben erweiterte Caching-Strategien im gesamten System implementiert, um Daten schneller abzurufen und Ladezeiten zu verkürzen. Diese Verbesserungen sorgen für eine flüssigere Navigation und ein noch reaktionsschnelleres Benutzererlebnis, insbesondere bei häufig genutzten Funktionen.

#### Dashboard- und UI-Upgrades

• Dashboard-Verbesserungen: Das Dashboard wurde mit einem optimierten Layout und zusätzlichen Funktionen überarbeitet, um die Navigation zu vereinfachen und die Sichtbarkeit wichtiger Kennzahlen zu erhöhen.

• UI-Verbesserungen: Die Benutzeroberfläche der gesamten Anwendung wurde moderner und intuitiver gestaltet, sodass Benutzer ihre Aufgaben mit minimalem Aufwand erledigen können.

### Fehlerbehebungen:

• Die Fuzzy-Logik wurde optimiert, um eine genauere und zuverlässigere Datenbefüllung nach der Extraktion zu gewährleisten.

• Bekannte Probleme im Zusammenhang mit Gruppen und Berechtigungen wurden behoben, was ein reibungsloses Zugriffsmanagement und eine funktionierende Rollenzuweisung sicherstellt.

• Inkonsistenzen in Übersetzungen wurden beseitigt, sodass die Anwendung klarer und lokalisierter ist.

• Layout-Probleme wurden behoben, um eine konsistente und optimierte Benutzeroberfläche in allen Konfigurationen zu gewährleisten.

• Fehler in der Stammdatensuche wurden korrigiert, was eine genaue und zuverlässige Datenabfrage sicherstellt.

• Störungen bei der E-Mail-Import-Funktion in allen verfügbaren Optionen wurden behoben, um einen fehlerfreien Betrieb zu ermöglichen.

## Änderungen vom 4. November 2024

## Neue Funktionen:

## Verbesserungen beim E-Mail-Import

IMAP-E-Mail-Einstellungen wurden so konfiguriert, um Benachrichtigungen über Importergebnisse automatisch zu senden. Erfolgreiche Importbenachrichtigungen bestätigen die erfolgreiche Verarbeitung von Dateien, während Fehlermeldungen die Dateinamen und spezifische Fehlerdetails für eine schnelle Fehlersuche enthalten.

<figure><img src="../.gitbook/assets/docbits_error_approval.png" alt="Fehler Genehmigung Rechnung Einstellungen E-Mail Import Bestellung Übersicht"><figcaption></figcaption></figure>

## Überarbeitung der Stammdatenabfrage

Die Einstellungen zur Stammdatenabfrage wurden überarbeitet und verfeinert, um eine schnellere und genauere Abfrage verschiedener Stammdatentypen zu ermöglichen. Diese Verbesserung optimiert den Datenzugriff, indem Stammdaten in unterschiedliche Kategorien organisiert werden, was die Sucheffizienz und -genauigkeit erheblich steigert. Benutzer können nun die relevanten Daten schneller finden, was die Produktivität in der Anwendung verbessert.

<figure><img src="../.gitbook/assets/image2.png" alt=""><figcaption></figcaption></figure>

## Leistungsverbesserungen

Ein robustes Caching-System wurde implementiert, um die Anwendungsleistung erheblich zu steigern, insbesondere bei hohen Anfragen. Diese Verbesserung reduziert die Serververarbeitungszeit, indem häufig abgerufene Daten vorübergehend gespeichert werden, was schnellere Antwortzeiten und ein reibungsloseres Benutzererlebnis ermöglicht. Das neue Caching-System verwaltet den erhöhten Datenverkehr effizient und sorgt für zuverlässige und konstante Leistung, selbst in Spitzenlastzeiten.

## Verbesserung der Dokumentensperrfunktion

Die Funktionalität zum Sperren von Dokumenten wurde verbessert, um gleichzeitige Bearbeitung zu verhindern, die Datenintegrität zu gewährleisten und Konflikte zu minimieren. Dokumente werden nun während der aktiven Bearbeitung automatisch gesperrt, wobei den Benutzern klare Hinweise gegeben werden, wenn ein Dokument in Verwendung ist, und andere daran gehindert werden, Änderungen vorzunehmen, bis die Bearbeitung abgeschlossen ist. Diese Verbesserung optimiert die kollaborativen Arbeitsabläufe und verringert das Risiko von Datenüberschreibungen.

## Verbesserungen bei Navigation und Benutzererfahrung

* **Breadcrumb-Navigation**: Breadcrumbs wurden auf den Seiten der Anwendung hinzugefügt, um die Navigation zu verbessern, sodass Benutzer leicht zurückverfolgen und zu vorherigen Abschnitten zurückkehren können. Dies ermöglicht ein intuitiveres Surferlebnis.
* **Optimierte Benutzeroberfläche**: Die Pop-up-Benachrichtigung "neue Version" wurde entfernt, um einen reibungsloseren, ununterbrochenen Arbeitsablauf zu schaffen. Ablenkungen werden reduziert und die allgemeine Benutzerfreundlichkeit verbessert.

## Fehlerbehebungen:

* Benutzerbezogene Probleme, wie z.B. Anhangsfehler von verschlüsselten oder signierten E-Mails, wurden behoben.
* Probleme mit der Kartenanzeige und dem Ablauf wurden behoben.
* Routing-Probleme mit den Schaltflächen "Nächste/Vorherige" wurden behoben.
* Fehler im Zusammenhang mit Entscheidungstabellen wurden behoben.
* Die Benutzeroberfläche für das Passwortfeld wurde überarbeitet, um die Benutzerfreundlichkeit zu verbessern.
* Probleme mit nicht korrekt angezeigten Aufgabenzähler wurden behoben
* Benutzeroberflächenproblem mit der KI-Tabelle wurde behoben.
* Fehler bei der Dokumentenextraktion während des Tabellentrainings wurden behoben.
* Warnung wurde hinzugefügt, wenn ein PO während der Umformatierung übereinstimmt. Es wird sichergestellt, dass übereinstimmende Zeilen entfernt werden.
* Das Datumsformat wurde korrigiert, um sicherzustellen, dass Daten korrekt nach Tages- und Wochenfiltern geladen, und Dokumenttypen ordnungsgemäß angezeigt werden.
* Die Anzeige von Dokumenten auf Dual-Monitoren wurde korrigiert.
* Problem, bei dem das Trennen einer PO-Zeile alle Zeilen entfernt hat, wurde behoben.
* Falsche Übersetzungen in der gesamten Anwendung wurden behoben.
* Problem, bei dem lange Beschreibungen im Regelmanagement Scrollen in der Liste verursachte, wurde behoben.
* Fehlende "Zuweisen"-Funktionalität für Nicht-Admin-Benutzer wurde wiederhergestellt.
