# Release-Notizen

## **Release Spring Spark 13. Mai 2026**

Sandbox-Verfügbarkeit: 27.–29. April 2026

### DocBits-Verbesserungen:

*   **Advanced Workflow Designer:**\
    DocBits führt einen völlig neuen Advanced Workflow Designer ein — einen visuellen, knotenbasierten Automatisierungs-Builder, der die vollständige Workflow-Orchestrierung ermöglicht. Über eine intuitive Drag-and-Drop-Oberfläche können Administratoren DocBits-Workflow-Karten zu komplexen, mehrstufigen Verarbeitungspipelines verbinden. Jeder Knoten auf der Arbeitsfläche stellt eine Aktion oder einen Entscheidungspunkt dar, und die Verbindungen zwischen den Knoten definieren den Dokumentenfluss durch die Pipeline. Der Designer unterstützt Warteknoten für zeitgesteuerte Verzögerungen, parallele Pfade, bei denen alle oder einzelne Zweige abgeschlossen sein müssen, bevor fortgefahren wird, sowie die Möglichkeit, beliebige Kombinationen von integrierten oder von Partnern erstellten Karten zu verketten. Workflows können als wiederverwendbare Vorlagen gespeichert, zwischen Umgebungen importiert und exportiert sowie direkt im Designer getestet werden, bevor sie live geschaltet werden. Der Editor bietet eine Arbeitsfläche mit Einrastfunktion und Mini-Map-Navigation für große Workflows, Tastaturkürzel zum Kopieren und Einfügen, Echtzeit-Validierung mit Fehlerhervorhebung während des Erstellens sowie Schutz vor gleichzeitiger Bearbeitung, um das Überschreiben von Änderungen durch andere Benutzer zu verhindern. Detaillierte Ausführungsprotokolle ermöglichen die Überwachung pro Knoten, sodass Administratoren genau nachverfolgen können, wie jeder Schritt in einem Workflow ausgeführt wurde und wo Probleme aufgetreten sind.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/release_may_2026_advanced_workflow_designer.png)

*   **Workflow Designer Verbesserungen:**\
    Der bestehende Workflow Designer wurde um If/Else-Verzweigungslogik erweitert, die anspruchsvollere entscheidungsbasierte Workflows ermöglicht. Mehrere neue Bedingungskarten wurden hinzugefügt, die das Spektrum der verfügbaren Automatisierungslogik weiter ausbauen. Ein neuer Workflow Test Manager ermöglicht es Administratoren, automatisierte Tests für Workflows einzeln oder alle auf einmal zu erstellen und auszuführen, um sicherzustellen, dass Änderungen vor der Bereitstellung wie erwartet funktionieren. Der Workflow-Bereich enthält nun auch ein KPI-Dashboard mit wichtigen Kennzahlen zur Workflow-Ausführungsleistung.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/release_may_2026_workflow_branching.png)

*   **DocNet AI Agents:**\
    DocBits enthält jetzt DocNet AI Agents — intelligente, autonome Agenten, die im Hintergrund laufen und Dokumentenverarbeitungsaufgaben wie Bestellabgleich und Rechnungsvalidierung übernehmen. Agenten arbeiten unabhängig, bearbeiten zugewiesene Aufgaben und eskalieren nur dann an Benutzer, wenn menschliches Urteilsvermögen erforderlich ist. Wenn ein Agent auf eine Ausnahme stößt oder eine Bestätigung benötigt, erstellt er eine Genehmigungsanfrage, die direkt im Posteingang des Benutzers erscheint, sodass nichts übersehen wird, ohne dass eine ständige Überwachung erforderlich ist. Agenten können sich untereinander koordinieren, Unteraufgaben delegieren und Arbeit in Missionen und Projekte für komplexe mehrstufige Prozesse organisieren. Ein dediziertes Agenten-Dashboard bietet vollständige Transparenz über Agentenaktivitäten, Leistungskennzahlen und Audit-Protokolle, sodass Administratoren überwachen können, was die Agenten tun und wie effizient sie arbeiten. Echtzeit-Benachrichtigungen halten Benutzer auf dem Laufenden, wenn Agenten Aufgaben abschließen oder Elemente zur Überprüfung markieren.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/release_may_2026_docnet_ai_agents.png)

*   **Partner Card SDK:**\
    Ein neues Partner Card SDK ermöglicht es Drittentwicklern und Partnern, benutzerdefinierte Workflow-Karten für DocBits zu erstellen. Partner können Kartenpakete zur Validierung und Überprüfung hochladen, Karten aus GitHub-Repositories importieren und Einreichungen über eine dedizierte Card SDK-Einstellungsseite verwalten. Ein KI-gestütztes Überprüfungssystem bewertet eingereichte Karten automatisch hinsichtlich Qualität und Compliance. Das SDK umfasst beispielbasierte Downloads mit Kartenauswahldialogen, Verhaltensvalidierung in einer Sandbox-Umgebung und umfassende Einstiegsdokumentation. Das Card SDK ist durch Lizenzprüfungen geschützt und nun für alle Benutzer sichtbar, nicht nur für Administratoren.

*   **Full-Text Search / DocSearch:**\
    Eine neue Volltextsuchfunktion wurde zu DocBits hinzugefügt, die durch KI-gesteuerte Vektorsuche angetrieben wird. Benutzer können über alle indizierten Dokumente hinweg suchen, mit Echtzeit-Lieferantenfilterung und einer „Find Similar"-Funktion, um Dokumente zu finden, die einem ausgewählten ähneln. Eine dedizierte Einstellungsseite ermöglicht es Administratoren, die KI-Datenindizierung, Vektorspeichereinstellungen zu konfigurieren und den Indizierungsfortschritt in Echtzeit zu überwachen. Der Zugang zu DocSearch wird über Abonnementpläne verwaltet.

*   **E-Invoice Format-Erweiterung:**\
    DocBits hat die Unterstützung elektronischer Rechnungsformate erheblich erweitert — mit über 80 neuen globalen E-Rechnungstypen und mehr als 40 neuen Formaten. Neu unterstützte Formate umfassen unter anderem Taiwan EGUI, Thailand E-Tax, India GST Credit Note, SPS Commerce RSX 7.7.4, XRechnung 3.0.2, ZUGFeRD 2.2 und 2.3.2, Factur-X Varianten, Uruguay CFE, Ecuador SRI Retención, SVEFAKTURA 1.0, EHF 3.0, OIOUBL, Finvoice und Asia-Pacific PINT Credit Notes. DocBits erreicht nun 100 % Klassifizierungs- und Extraktionsabdeckung für alle unterstützten elektronischen Dokumentformate.

*   **Login Analytics:**\
    Ein neues Login Analytics Dashboard gibt Administratoren vollständige Transparenz über Login-Aktivitäten in der gesamten Organisation. Das Dashboard umfasst Vergleichsdiagramme, die Login-Trends im Zeitverlauf zeigen, tägliche und wöchentliche Aggregationsansichten sowie GeoLite2-basierte Geolokalisierung, um zu sehen, woher Anmeldungen stammen. Dies bietet eine schnelle Möglichkeit, ungewöhnliche Anmeldemuster zu erkennen und die Kontosicherheit zu überwachen.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/release_may_2026_login_analytics.png)

*   **Analytics Dashboard:**\
    Ein umfassendes Dokumentenverarbeitungs-Analysemodul wurde eingeführt, mit mehreren Dashboard-Ansichten einschließlich Executive Overview, API Metrics, Quality Metrics und Processing Performance. Document Flow Analytics bietet Kennzahlen auf Organisationsebene zu Dokumentenverarbeitungszeiten und Statusübergängen. Ein vollständiges Activity Log- und Event Log-System ermöglicht es Administratoren, Ereignisdaten zu durchsuchen, zu filtern und zu exportieren — mit Diagrammvisualisierungen und JSON-Syntaxhervorhebung. Eine Audit Trail-Funktion bietet eine detaillierte Änderungsverfolgung mit Popup-Details für jede Änderung.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/release_may_2026_analytics_dashboard.png)

*   **Verbesserungen der Zugriffssteuerung:**\
    Die Zugriffssteuerung wurde auf die gesamte Anwendung angewendet und deckt den Feldvalidierungsbildschirm, KI-extrahierte Tabellen und mehrere weitere Ansichten ab. Administratoren haben nun die Möglichkeit, die Zugriffssteuerung bei Bedarf global zu deaktivieren. Das Design der Zugriffssteuerung wurde für ein konsistenteres und intuitiveres Erlebnis über alle Bildschirme hinweg überarbeitet.

*   **Layout Builder Verbesserungen:**\
    Der Layout Builder unterstützt jetzt ausgeblendete und schreibgeschützte Felder mit visuellen Indikatoren, sodass Administratoren leichter erkennen können, welche Felder für Benutzer sichtbar und bearbeitbar sind. Ein größenveränderbarer Teiler zwischen den Bereichen verbessert die Arbeitsplatzflexibilität, und Feldlängeneinstellungen bieten eine präzisere Kontrolle über Dateneingabefelder.

*   **Exportverlauf in Dashboard-Aktionen:**\
    Benutzer können nun den Exportverlauf eines Dokuments direkt über das Dashboard-Aktionsmenü aufrufen, was die Überprüfung vergangener Exportversuche beschleunigt, ohne die Hauptansicht verlassen zu müssen.

*   **Export-Verbesserungen:**\
    Exportkonfigurationen unterstützen jetzt eine Ausführungsreihenfolge, mit der Administratoren die Sequenz festlegen können, in der mehrere Exportmethoden verarbeitet werden. Eine neue Re-Export-Schaltfläche auf Fehlerbildschirmen ermöglicht es Benutzern, ab dem fehlgeschlagenen Schritt erneut zu exportieren, anstatt den gesamten Prozess neu zu starten. DocBits unterstützt außerdem jetzt das GLS840MI API-Exportziel, mit einer aktualisierten Benutzeroberfläche zur Verwaltung mehrerer aktiver Exportkonfigurationen pro Dokumenttyp.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/release_may_2026_export_improvements.png)

*   **Script Versioning & AI Chat:**\
    Dokumentskripte unterstützen jetzt eine vollständige Versionshistorie, die es Administratoren ermöglicht, Änderungen nachzuverfolgen, Versionen zu vergleichen und frühere Skriptversionen wiederherzustellen. Standardskripte sind vor versehentlichen Bearbeitungen geschützt, und Skriptnamen können inline mit Breadcrumb-Navigation bearbeitet werden. Felder können jetzt programmgesteuert über die neue set\_is\_readonly-Funktion als schreibgeschützt festgelegt werden. Ein neuer KI-gestützter Chat-Assistent unterstützt bei der Skriptentwicklung mit Echtzeit-Streaming-Antworten.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/release_may_2026_script_versioning.png)

*   **API Key Management:**\
    Eine neue API Key Management-Seite in den Integrationseinstellungen ermöglicht es Administratoren, mehrere API-Schlüssel zu erstellen, anzuzeigen und zu verwalten — mit Redis-basiertem Caching für optimale Leistung.

*   **Idea Board:**\
    Eine neue Idea Board-Funktion ermöglicht es Benutzern, Feature-Ideen und Vorschläge einzureichen, zu diskutieren und darüber abzustimmen. Das Board enthält einen Rich-Text-Editor mit Bild-Upload-Unterstützung, Kommentarfunktion und Abstimmungsmöglichkeit.

*   **Lieferantenstatistiken:**\
    Neue Ansichten für Lieferantenstatistiken bieten Einblicke in lieferantenbezogene Kennzahlen der Dokumentenverarbeitung.

*   **Spracherweiterung:**\
    DocBits unterstützt jetzt 22 Sprachen, erweitert gegenüber der bisherigen Auswahl. Die Sprachauswahl wurde mit einem 4-Spalten-Rasterlayout aktualisiert, und Benutzer können ihre bevorzugte Sprache jetzt direkt in ihren Benutzereinstellungen festlegen.

*   **Abonnementplan-Redesign:**\
    Der Abonnementplan-Picker wurde mit verbesserter Token-Informationsanzeige und einer neuen DocNet-Nutzungszeile in der Abonnementtabelle neu gestaltet.

*   **Dual Monitor Mode:**\
    Der Dual Monitor Mode wurde in eine globale Benutzereinstellung verschoben und ist damit sitzungsübergreifend zugänglich und persistent für Benutzer, die mit mehreren Bildschirmen arbeiten.

*   **Unscharfe Suche für deutsche Sonderzeichen:**\
    Die Suchfunktion unterstützt jetzt korrekt deutsche Sonderzeichen (Umlaute), sodass Suchen nach Wörtern wie „Rechnungsnummer" auch Treffer mit alternativen Zeichendarstellungen liefern.

*   **Verbesserungen bei E-Mail-Benachrichtigungen:**\
    Die Parameterersetzung in E-Mail-Vorlagen wurde verbessert, mit besserer Empfängervalidierung und Berücksichtigung von Benutzereinstellungen.

*   **Kreditverbrauchsüberwachung:**\
    Organisationen können ihren KI-Kreditverbrauch jetzt im Zeitverlauf mit Filteroptionen einsehen und verfolgen, was eine bessere Transparenz über Verbrauchsmuster bietet.

### Allgemeine Verbesserungen:

*   Der Einstellungsbereich wurde mit einer einklappbaren Seitenleiste, organisierten Unterkategorien und ankerbasierter Navigation für schnelleren Zugriff neu gestaltet. Ein Kontext-Hilfepanel bietet Inline-Anleitungen, und Statusverfolgungsabzeichen zeigen die Konfigurationsvollständigkeit auf einen Blick.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/release_may_2026_settings_redesign.png)

* Dokumente mit Barcodes werden jetzt zuverlässiger aufgeteilt, mit besserer Behandlung von Randfällen und Fehlerwiederherstellung.
* Der PO-Abgleich erkennt und konvertiert jetzt automatisch Stückpreise beim Aufteilen abgeglichener Positionen, wodurch manuelle Korrekturen reduziert werden.
* Dokumente bleiben nicht mehr während der Extraktion hängen — ein neues Statusverfolgungssystem stellt sicher, dass jedes Dokument die Pipeline durchläuft.
* Bei Extraktionsfehlern liefert DocBits jetzt klarere Fehlermeldungen mit Schritt-für-Schritt-Details, um die Fehlerbehebung zu beschleunigen.
* Die allgemeine Anwendungsleistung wurde mit schnelleren Antwortzeiten über alle Bildschirme hinweg verbessert.
* Auto Accounting-Regeln unterstützen jetzt nummernbasierte Filterung für präzisere Abgleichsbedingungen.

### Fehlerbehebungen:

* Ein Problem wurde behoben, bei dem der benutzerdefinierte Dashboard-Name nicht mit dem Dashboard-Symbol ausgerichtet war.
* Ein Problem wurde behoben, bei dem das Dashboard Spalten anzeigte, die nicht in der Konfiguration der sichtbaren Spalten enthalten waren.
* Ein Problem wurde behoben, bei dem der ausgewählte Tab-Name nicht auf dem Dashboard angezeigt wurde.
* Ein Problem wurde behoben, bei dem das Popup „Neue Version verfügbar" bei jedem Wechsel der Unterorganisation erschien.
* Ein Problem wurde behoben, bei dem die Einstellung „Dokumente pro Seite" nach dem Aktualisieren der Seite nicht beibehalten wurde.
* Ein Problem wurde behoben, bei dem die Dokumentenanzahl im Dashboard nicht korrekt aktualisiert wurde.
* Ein Problem wurde behoben, bei dem Benutzer fälschlicherweise die Fehlermeldung „Dashboard existiert bereits" erhielten.
* Ein Problem wurde behoben, bei dem das Bestätigungs-Popup für Massenlöschung nicht angezeigt wurde.
* Mehrere Probleme mit der Anzeige und dem Speicherverhalten von geteilten Dashboards wurden behoben.
* Ein Problem wurde behoben, bei dem Dokumenttabellen auf dem Validierungsbildschirm nicht angezeigt wurden.
* Ein Problem wurde behoben, bei dem eine falsche Fehlermeldung für ungültige PDF-Dateien angezeigt wurde.
* Ein Problem wurde behoben, bei dem die Spaltengrößenänderung hinter den Zeilen-Aktionsschaltflächen erschien.
* Ein Problem wurde behoben, bei dem falsche Werte für Nettobetrag, Steuerbetrag und Steuersatz extrahiert wurden.
* Ein Problem wurde behoben, bei dem Exportkonfigurationen nicht ohne Angabe eines Dokumenttyps erstellt werden konnten, wenn dieser als optional markiert war.
* Ein Problem wurde behoben, bei dem ein Duplikatkonfigurationsfehler beim Hinzufügen neuer Exportkonfigurationen auftrat.
* Ein Problem wurde behoben, bei dem Fehler beim Erstellen mehrerer Exportkonfigurationen auftraten.
* Ein Problem wurde behoben, bei dem der Konfigurationstitel nach Auswahl von Watchdog als Exporttyp gelöscht wurde.
* Ein interner Serverfehler beim Erstellen von Infor-Exportkonfigurationen wurde behoben.
* Ein Problem wurde behoben, das den Mehrfach-Neustart exportierter Dokumente verhinderte.
* Ein Problem wurde behoben, bei dem einige Einstellungsseiten nicht gefunden werden konnten.
* Ein Problem wurde behoben, bei dem der Watchdog-Download-Link einen Fehler zurückgab.
* Ein Problem wurde behoben, bei dem die Schaltfläche „List of Values erstellen" keine Aktion auslöste.
* Ein Problem wurde behoben, bei dem Gruppenbeschreibungen nicht angezeigt wurden.
* Ein Problem wurde behoben, bei dem der Passwortvalidierungsstatus nach dem Abbrechen einer Benutzerbearbeitung bestehen blieb.
* Ein Problem wurde behoben, bei dem Dokumente im Status „Pending Watcher Export" nicht anklickbar waren.
* Ein Problem wurde behoben, bei dem doppelte Lookup-Konfigurationen erstellt werden konnten.
* Ein Problem wurde behoben, bei dem die Benutzersortierung nicht korrekt funktionierte.
* Ein Anzeigeproblem wurde behoben, bei dem der gesamte Anwendungstext in Blau erschien.
* Ein Problem wurde behoben, bei dem die Sprachformatanzeige inkonsistent war.
* Ein Problem wurde behoben, bei dem die Spracheinstellung leer erschien, wenn keine Präferenz ausgewählt war.
* Ein Problem wurde behoben, bei dem die Groß-/Kleinschreibung des Firmennamens ignoriert wurde.
* Ein Problem wurde behoben, bei dem die Suche für Gruppen und Berechtigungen nicht funktionierte.
* Ein Problem wurde behoben, bei dem die Benutzer-löschen-Aktion den Benutzer nicht ordnungsgemäß löschte.
* Ein Problem wurde behoben, bei dem Dokumentfluss-Symbole nicht sichtbar waren.
* Ein interner Serverfehler beim Speichern von E-Mail-Vorlagen wurde behoben.
* Ein Problem wurde behoben, bei dem doppelte Variablen in E-Mail-Vorlagen-Betreffzeilen eingefügt wurden.
* Ein Fehler beim Speichern von eingehenden E-Mail-Kontodetails wurde behoben.
* Ein Problem wurde behoben, bei dem Dokumente nach dem Hochladen im Status „Neu" hängen blieben.
* Ein Problem wurde behoben, bei dem Tabellenspalten nach dem Deaktivieren und erneuten Aktivieren nicht verfügbar waren.
* Ein Problem wurde behoben, bei dem die Erstellung von Entscheidungsbäumen für benutzerdefinierte Dokumenttypen fehlschlug.
* Ein Problem wurde behoben, bei dem die Tabellenextraktion keine Ergebnisse lieferte.
* Ein Problem wurde behoben, bei dem der Dokumenttyp CREDIT\_NOTE nicht korrekt erkannt wurde.
* Ein Problem wurde behoben, bei dem Benutzer ohne Administratorrechte alle erstellten Aufgaben einsehen konnten.
* Ein Problem wurde behoben, bei dem das Popup der Unterorganisation nach Drag-and-Drop-Datei-Upload nicht geschlossen wurde.
* Ein Problem wurde behoben, bei dem Zeitraumfilter nicht korrekt angewendet wurden.
* Ein Problem mit der Datums- und Zeitkonvertierung in das US-Format wurde behoben.
* Ein Problem wurde behoben, bei dem Workflows in der falschen Reihenfolge ausgelöst wurden — die Workflow-Ausführung verwendet jetzt eine korrekte Dokumentensperrung und Warteschlangenpriorisierung.

## **Release HotFix 2 31. März 2026**

### DocBits-Verbesserungen:

* **Hybride PDF-Verarbeitung — Benutzergesteuerte XML-Extraktion:**\
  Wenn ein PDF eingebettete XML-Daten enthält, können Benutzer jetzt wählen, ob DocBits die eingebetteten XML-Daten für die Extraktion verwenden oder das Dokument als Standard-PDF verarbeiten soll. Dies gibt Organisationen die volle Kontrolle darüber, wie hybride Dokumente verarbeitet werden, und stellt sicher, dass die für ihren Workflow am besten geeignete Extraktionsmethode angewendet wird.

* **AP Assignment Code auf dem Approval Screen:**\
  Die AP Manager Approval-Seite enthält jetzt ein AP Assignment Code-Feld, integriert mit Infor M3 CRS620. Dies ermöglicht es Genehmigern, Assignment Codes direkt während des Genehmigungsprozesses zu überprüfen und zu bestätigen, ohne zu externen Systemen wechseln zu müssen.

### Fehlerbehebungen:

* Ein Problem wurde behoben, bei dem der Infor SFTP-Export aufgrund eines falschen Library-Befehls mit einem Fehler fehlschlug.
* Ein Problem wurde behoben, bei dem boolesche Checkboxen nicht auf dem Approval Screen angezeigt werden konnten.
* Ein Problem wurde behoben, bei dem UNMU-Nachrichten gesendet wurden, obwohl keine Abweichungen in der Bestelleinheit vorlagen.
* Ein Problem wurde behoben, bei dem die Umsatzsteuer auf dem PO-Matching-Bildschirm fälschlicherweise als Zuschlag klassifiziert wurde, was zu einem negativen offenen Betrag führte.
* Ein Problem wurde behoben, bei dem der Export fehlschlug, wenn die Bestelleinheit nicht in der Auftragsbestätigung festgelegt war, aber in der Bestellung vorhanden war.
* Ein Problem wurde behoben, bei dem der E-Mail-Text bei mehreren Dokumenten fehlte.
* Ein Problem wurde behoben, bei dem die Lieferanten-Artikelnummer auf dem Approval Screen nicht sichtbar war und Aktualisierungen nicht an M3 gesendet wurden.
* Ein Problem wurde behoben, bei dem die Zuordnung von Unterorganisationen in der Produktion nicht korrekt funktionierte.
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
