# NOVA — Hauptversion — 4. November 2026 (geplant)

**Verfügbarkeit von NOVA R1.1:** Seit dem **16. Oktober 2026** in der Sandbox verfügbar. Der Produktionsrelease ist für den **4. November 2026** geplant.

**Sandbox-Serviceversionen: Stand 16. Oktober 2026**

NOVA umfasst alle Funktionen, die zuvor als Beta in VESTA verfügbar waren, nun als reguläre Funktionen, ergänzt um geführte Dokumentenvalidierung, weitere Möglichkeiten zur Automatisierungsverbesserung, klarere E-Rechnungsprüfungen und bessere Steuerung von Importen und Dokumentenverarbeitung. Diese Hinweise beschreiben die kundenseitigen Erweiterungen in den unten aufgeführten Serviceversionen im Vergleich zum zuletzt veröffentlichten [VESTA-Hotfix, R1.0.15 vom 14. Oktober 2026](incremental-updates-14-october-2026.md), einschließlich früherer VESTA-Hotfixes.

Der Versionsstand nennt die Builds, auf die sich diese Hinweise beziehen. Informationen zur Verfügbarkeit in Ihrer Sandbox- oder Produktionsumgebung und zum Wechsel zwischen Release-Kanälen finden Sie im [DocBits-Release-Lebenszyklus](../docbits-release-lifecycle-strategy.md). Funktionen mit einem Schalter auf Organisations- oder Dokumenttypebene müssen weiterhin von einem Administrator aktiviert werden.

## Ehemalige VESTA-Beta-Funktionen: in NOVA enthalten <a href="#former-vesta-beta-features-included-in-nova" id="former-vesta-beta-features-included-in-nova"></a>

**Alle ehemaligen VESTA-Beta-Funktionen sind in der NOVA-Sandbox als reguläre Funktionen enthalten.** Für Kunden, die die VESTA-Beta nicht genutzt haben, erweitert dies die ihrem Team verfügbaren Funktionen, einschließlich **Layouts verwalten**, [**Benutzerdefinierte Validierungsregeln**](../../administration-and-setup/settings/global-settings/document-types/custom-validation-rules.md) und [**Transformationsregeln**](../../administration-and-setup/settings/global-settings/document-types/transformation-rules.md). Organisationseinstellungen, Dokumenttyp-Schalter und Zugriffsrechte gelten weiterhin.

Dieselben ehemaligen Beta-Funktionen werden mit dem **nächsten VESTA-Hotfix, geplant für den [11. November 2026](vesta-hotfix-11-november-2026.md)**, zu regulären VESTA-Funktionen. Diese Ankündigung deckt die ehemaligen VESTA-Beta-Funktionen ab; die folgenden Abschnitte beschreiben zusätzlich weitere NOVA-Erweiterungen und -Verbesserungen.

## Was NOVA für Kunden bietet <a href="#what-nova-adds-for-customers" id="what-nova-adds-for-customers"></a>

Der folgende Vergleich umfasst neu verfügbare ehemalige Beta-Funktionen, neue Fähigkeiten und Erweiterungen bestehender Funktionen. Der VESTA-Ausgangsstand enthält Funktionalität, die nur in der Beta verfügbar war; deren Aufnahme in den regulären NOVA-Funktionsumfang ist eine kundenseitige Release-Änderung.

| Funktion | VESTA-Ausgangsstand (einschließlich Beta) | Was Kunden mit NOVA gewinnen |
| --- | --- | --- |
| **Ehemalige Beta-Funktionen nutzen** | Funktionen über VESTA-Beta verfügbar | **Reguläre NOVA-Funktionen:** alle ehemaligen VESTA-Beta-Funktionen sind enthalten. Ihre reguläre VESTA-Einführung ist für den Hotfix am 11. November 2026 geplant. |
| **Hilfe bei der Dokumentenvalidierung** | Einstellungs-Assistent und Header-Feld-Prüfung | **Neuer Validierungsassistent:** blockierende Felder identifizieren, zum relevanten Wert springen, vorgeschlagene Korrekturen prüfen und den Chat in einem separaten Fenster offenhalten. |
| **Automatisierung durch alltägliche Korrekturen verbessern** | Touchless-Intelligence-Dashboard, Lieferanten-Diagnose und Änderungsvorschläge | **Neuer Prüf- und Messprozess:** Verbesserungsanfragen einreichen, gelernte Regelvorschläge prüfen, betroffene Dokumentennachweise einsehen, Potenziale priorisieren und Ergebnisse nach Aktivierung messen. |
| **E-Rechnungsfehler verstehen und beheben** | E-Dokumentenprüfungen, Regelkatalog und XML-Viewer | **Erweiterte E-Rechnungsvalidierung:** Berichte nach Validierungsstufe gruppiert, Richtliniensteuerung und Änderungshistorie, Ablehnung aus dem Bericht und XML-Inspektion innerhalb unterstützter PDF-Rechnungen. |
| **FTP/SFTP-Importe steuern** | Importverbindungen und Aufbewahrung oder Archivierung von Quelldateien | **Neue geführte Einrichtung und Steuerung:** Verbindungsassistent, schrittweise Protokolle, konfigurierbare Wiederholungen und Fehlerbenachrichtigungen sowie Löschung von Quelldateien nach erfolgreichem Import. |
| **Mit Regeln und Layouts arbeiten** | Regel-Engines, Ausführungsprotokolle und Transformationen nach Stammdatenabfrage; Verwaltungspanels erforderten einen Beta-Link | **Breiterer Zugriff und bessere Werkzeuge:** Verwaltungspanels direkt öffnen, Ziel-Layouts durchsuchen und in der Vorschau anzeigen, den Layout-Editor eines Dokuments öffnen und die Layout-Auswahl-Ausführung protokollieren. |
| **Im Einstellungs-Assistent handeln** | Settings-Chat, Vorschau/Bestätigung/Rückgängig und proaktive Import-Statuswarnungen | **Zusätzliche Aktionen:** fehlerhafte Verbindungen verwalten, Deaktivierungshistorie einsehen, ausgewählte Konfigurationselemente ändern, eine inaktive Validierungsregel aus dem Katalog erstellen und Seiten-Erklärungen anzeigen. |
| **Dokumentenverarbeitung steuern** | Seitenlimits der Organisation und Dokumentneustart | **Neue Auswahlmöglichkeiten pro Dokument:** Neustart mit gewählter Seitenanzahl, Anzeige verarbeiteter Seiten im Verhältnis zur Gesamtzahl und Auswahl, ob ausgeblendete Felder extrahiert werden. |
| **Komplexe Lieferungen abgleichen** | Bestellabgleich und manuelle Zeilenverknüpfung | **Flexiblerer Abgleich:** Zeilen in beide Richtungen auswählen, optional jede abgeglichene Dokumenten-Unterzeile beibehalten und Exportanfragen nach konfigurierten Zeilenspalten gruppieren. |
| **Exportierte und abgeschlossene Arbeit getrennt halten** | Bestehende Export- und Finished-Workflows | **Neue Statussteuerungen:** Verwenden Sie Exported für die Nachbearbeitung, sperren Sie optional Finished-Dokumente und finden Sie Dokumente, die durch das Workflow-Ausführungslimit zurückgehalten werden. |

### Funktionen aktivieren, die eine Konfiguration erfordern

* **Validierungsassistent:** Ein Organisationsadministrator aktiviert ihn unter **Einstellungen → Unternehmensinformationen → Assistenten**. Er ist vom Einstellungs-Assistenten getrennt und ist bis zur Aktivierung deaktiviert.
* **Verbesserungsprüfung und Beratungsberichte:** Erfordern Organisationsadministrator-Rechte und Zugriff auf Analytics. Gelernte Vorschläge setzen frühere Korrekturen voraus. Für ein Messergebnis müssen genügend Daten vorliegen und der Nachbeobachtungszeitraum abgeschlossen sein.
* **Regel- und Layoutsteuerungen:** Die Aktivierungsschalter pro Dokumenttyp gelten weiterhin. NOVA macht die Verwaltungspanels ohne Beta-Link zugänglich.
* **Optionale Verarbeitungseinstellungen:** Konfigurieren Sie FTP-Bereinigung und Wiederholungsversuche pro Verbindung. Die Aufschlüsselung in Unterpositionen bei Eins-zu-viele-Zuordnungen und die Sperre abgeschlossener Dokumente müssen ausdrücklich aktiviert werden.

Informationen zur Verfügbarkeit in Ihrer Umgebung und zum Wechsel des Release-Kanals finden Sie im [Release-Lebenszyklus](../docbits-release-lifecycle-strategy.md).

## Funktionsvideos ansehen <a href="#watch-the-feature-videos" id="watch-the-feature-videos"></a>

Verwenden Sie diese Walkthroughs ergänzend zu den Versionshinweisen, um die zugehörigen Funktionen und deren Konfiguration zu verstehen. Videos, die auf Deutsch verfügbar sind, sind unten verlinkt; andere Videos sind eindeutig als Englisch gekennzeichnet.

* [Die richtige Automatisierung wählen – einschließlich der Einordnung von Bestellabgleichregeln](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/choose-automation/v1/de.mp4)
* [Transformationsregeln](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/transformation-rules/v1/de.mp4)
* [Benutzerdefinierte Validierungsregeln](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/custom-validation-rules/v1/de.mp4)
* [Layouts und Auswahlregeln](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/layouts/v1/de.mp4)
* [Touchless Intelligence](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence/v1/de.mp4)
* [E-Rechnungs-Validierung](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/einvoice-validation/v1/de.mp4)
* [Benutzer und Administratorzugriff](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/users/v1/de.mp4)
* [Unterorganisationen](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/sub_organizations/v1/de.mp4)

### AI Table: sechs kurze Videos

Diese Videos sind auf Englisch. Sehen Sie sich die gesamte Serie an oder wählen Sie das benötigte Thema.

1. [Die AI-Tabelle lesen](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/ai-table-part1/v1/en.mp4)
2. [Eine Spalte korrigieren und DocBits daraus lernen lassen](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/ai-table-part2/v1/en.mp4)
3. [Drei typische Probleme](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/ai-table-part3/v1/en.mp4)
4. [Rabatt-, Steuer- und Nullmengenzeilen](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/ai-table-part4/v1/en.mp4)
5. [Was die AI bereits korrekt liest](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/ai-table-part5/v1/en.mp4)
6. [Der Assistent und wer was ändern kann](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/ai-table-part6/v2/en.mp4)

Screenshots und detaillierte Anweisungen finden Sie im [AI-Table-Handbuch](../../end-user-and-partner-section/end-user-section/ai-table/README.md).

## Validierungsassistent: Hilfe zum Dokument vor Ihnen

* **Herausfinden, was den Fortschritt blockiert.** Fragen Sie, warum ein Dokument nicht fortgesetzt werden kann. Der Assistent identifiziert die betroffenen Felder, erklärt das Problem und bietet einen Sprung zum Feld oder zur Tabellenzelle. Er verwendet das aktuelle Dokument und die Zugriffsrechte des Benutzers.
* **Vorgeschlagene Korrekturen im Kontext prüfen.** Wo unterstützt, können Prüfer einen vorgeschlagenen Feld- oder Tabellenwert anwenden, einen Stammdatenkandidaten verwenden, eine Suche wiederholen oder den zugehörigen Abgleichsbildschirm öffnen. Formularänderungen unterliegen weiterhin dem normalen Prüf- und Speicherprozess des Dokuments. Schreibgeschützte Dokumente und Benutzer ohne Bearbeitungsrecht erhalten keine Bearbeitungsfunktionen.
* **Fragen zu Abgleich und Buchhaltung stellen.** Der Assistent kann den Bestellabgleichs- oder Buchhaltungskontext erläutern, wenn er auf diesen Bildschirmen geöffnet wird. Änderungen am Validierungsformular werden auf dem Validierungsbildschirm vorgenommen.
* **Eine Verbesserung vor der Anwendung verstehen.** Erläuterungen setzen eine vorgeschlagene Regel oder Einstellung in Bezug zu den tatsächlichen Werten des Dokuments. Sie können ein Diagramm und, sofern verfügbar, eine gesprochene Erklärung in der Sprache des Benutzers enthalten. Die Vorschläge beziehen sich auf das aktuelle Dokument.
* **Chat in einem separaten Fenster nutzen.** Die Konversation kann beim Prüfen des Dokuments in ein eigenes Fenster ausgelagert werden. Aktionen, die das Formular ändern, bleiben im Dokumentfenster.
* **Mehr Details hinter extrahierten Werten sehen.** Die Wertursprung-Ansicht ergänzt Details wie OCR versus PDF-Textebene, Extraktionsregel-Zuordnung und den Lookup, der einen Wert geliefert hat. Die AI-Table-Erklärung liefert konkretere Einrichtungsempfehlungen und übersichtlichere Zählungen.

Ein Organisationsadministrator aktiviert den Validierungsassistenten unabhängig vom Einstellungs-Assistenten unter **Einstellungen → Unternehmensinformationen → Assistenten**.

## Wiederholte Korrekturen in Automatisierungsverbesserungen umwandeln

Das bestehende [Touchless Intelligence](../../administration-and-setup/touchless-intelligence.md)-Dashboard erhält einen Prüf- und Nachverfolgungsprozess:

* **Gelernte Regelvorschläge.** Wiederholte manuelle Korrekturen können eine [Transformationsregel](../../administration-and-setup/settings/global-settings/document-types/transformation-rules.md) vorschlagen. Administratoren sehen, was die Regel schreiben würde, die unterstützenden Beispiele und die Dokumente, bei denen sie einen vom Team akzeptierten Wert ersetzen würde. Ein Vorschlag wird geprüft, bevor er zu einer aktiven Regel wird.
* **Verbesserungsanfragen von Prüfern.** Benutzer können im Dokumentassistenten einen Verbesserungsvorschlag einreichen, den ein Administrator in Touchless Intelligence prüft. Erklärung und Entscheidung bleiben zusammen mit der Anfrage gespeichert.
* **Messen, was nach der Aktivierung passiert ist.** Für unterstützte Transformationsregeln vergleicht DocBits manuelle Korrekturen vor und nach der Aktivierung und zeigt die Touchless-Rate daneben an. Die Messung verwendet 14-Tage-Perioden und erkennt unzureichende Daten, statt eine Verbesserung zu erfinden. Eine Änderung der Regel startet eine neue Messung für diese Revision.
* **Beratungsbericht.** Administratoren können eine nach Priorität geordnete Übersicht der Verbesserungsmöglichkeiten für Extraktion, Stammdaten, Bestellabgleich, Buchhaltung, Einstellungen und Verarbeitungsablauf erstellen. Die geschätzte Wirkung bleibt als Schätzung gekennzeichnet, bis sie gemessen wurde.
* **Lieferantenbezogene Abgleichempfehlungen.** Wiederholte Lieferanten- und Artikelabgleichprobleme können Vorschläge für Toleranzen oder [Bestellabgleichregeln](../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-matching-rules.md) liefern. Die Empfehlung unterscheidet eine fehlende Bestellung von einem Regel- oder Toleranzproblem.
* **Zusammenfassungen zur Nachverfolgung.** Eine wöchentliche Übersicht für Administratoren fasst offene Verbesserungsanfragen, die wichtigsten Verbesserungspotenziale und abgeschlossene Messungen zusammen, wenn es etwas zu berichten gibt. Antragsteller können benachrichtigt werden, sobald ein Messergebnis vorliegt.

## Einstellungs-Assistent: zusätzliche Aktionen und Seitenerklärungen

Der [Einstellungs-Assistent](../../administration-and-setup/settings/global-settings/company-information/settings-assistant.md), einschließlich proaktiver Warnungen zum Zustand von E-Mail- und FTP-Importen, wurde bereits in VESTA ausgeliefert. NOVA ergänzt diese Funktionen um weitere Aktionen und Kontextinformationen:

* **Verbindungsaktionen aus einer Statuswarnung.** Öffnen Sie die betroffene Verbindung, prüfen Sie die angebotene Aktion und bestätigen Sie diese im Assistenten. Statuswarnungen lassen sich auch ausblenden. Die grundlegenden Warnkarten pro Importkanal sowie ihre Fehler- und Wiederholungsinformationen sind bereits in VESTA vorhanden.
* **Sichtbare Deaktivierungshistorie.** Wo aufgezeichnet, zeigt ein deaktivierter Import an, wann er deaktiviert wurde und von wem.
* **Zusätzliche geprüfte Aktionen.** Administratoren können unterstützte Änderungen wie das Aktivieren von Dokumenttypen, das Umbenennen einer Gruppe, das Ändern des Suchmodus eines Lookup-Felds, das Löschen eines Felds oder das Erstellen einer inaktiven benutzerdefinierten Validierungsregel aus dem Katalog in der Vorschau ansehen und bestätigen.
* **Fehlgeschlagene Importverbindungen verwalten.** Unterstützte Karten können eine Verbindung nach Bestätigung deaktivieren oder löschen. Umkehrbare Aktionen bieten eine Rückgängig-Funktion; eine dauerhafte Löschung wird als solche gekennzeichnet.
* **Seitenerklärungen.** Ausgewählte Einstellungsseiten bieten Videos mit Untertiteln und Transkripten, einschließlich Layouts, Benutzer, Unterorganisationen, Transformationsregeln und E-Rechnungs-Validierung, sofern eine Sprachversion verfügbar ist.

## Regeln und Layouts: direkter Zugriff und bessere Diagnose

* **Ehemalige Beta-Steuerungen werden reguläre Funktionen.** Layoutverwaltung, [Benutzerdefinierte Validierungsregeln](../../administration-and-setup/settings/global-settings/document-types/custom-validation-rules.md) und [Transformationsregeln](../../administration-and-setup/settings/global-settings/document-types/transformation-rules.md) sind in den erweiterten Einstellungen des Dokumenttyps in NOVA ohne Beta-Link sichtbar. Ihre Aktivierungsschalter bleiben unter Administratorkontrolle. Diese Steuerungen sind im geplanten VESTA-Hotfix vom 11. November 2026 zusammen mit allen anderen ehemaligen VESTA-Beta-Funktionen enthalten.
* **Nützlichere Regeldiagnose.** Layout-Auswahlregeln erhalten eine Option **Ausführung protokollieren**. Die Regelsuche akzeptiert Regel-IDs, und das Öffnen eines Editors lädt die aktuell gespeicherte Regel. Das bestehende Regelausführungsprotokoll bleibt der Ort, um zu prüfen, was ausgeführt wurde.
* **Layouts mit mehr Kontext auswählen und öffnen.** Ziel-Layouts durchsuchen, deren Inhalt in der Vorschau anzeigen und das Ziel direkt aus einer Auswahlregel öffnen. Genehmigungs-Auswahlregeln akzeptieren korrekt die unterstützten Genehmigungs-Layout-Typen. Administratoren erhalten zudem eine Verknüpfung von der Dokumentenvalidierung zum Layout-Editor des jeweiligen Dokumenttyps.
* **Mehrere Bedingungswerte auswählen.** Bedingungen wie **ist einer von** unterstützen mehrere ausgewählte Werte.
* **Felder zur Duplikaterkennung schneller finden.** Das Feldauswahlmenü in den Duplikateinstellungen des Dokumenttyps ist durchsuchbar.

Transformationen nach der Stammdatenabfrage, das grundlegende Regel-Ausführungsprotokoll, breitere Regel-Editoren und die Korrekturen zum Klonen von Standardregeln sind bereits in der VESTA-Basisversion implementiert. NOVA führt diese Funktionalität fort und stellt die früheren Beta-Verwaltungsfunktionen als reguläre Funktionen bereit.

Informationen zu Einrichtungsschritten, Beispielen und Tests finden Sie unter [Benutzerdefinierte Validierungsregeln](../../administration-and-setup/settings/global-settings/document-types/custom-validation-rules.md) und [Transformationsregeln](../../administration-and-setup/settings/global-settings/document-types/transformation-rules.md). Informationen zur Auswahl des Layouts für ein Dokument finden Sie unter [Layout-Auswahlregeln](../../administration-and-setup/settings/global-settings/document-types/layout-manager/layout-selection-rules.md).

## E-Rechnungs-Validierung: klarere Befunde und Richtliniensteuerung

* **Ein nach Validierungsstufen gegliederter Bericht.** Befunde werden in Syntax-, Schema-, Geschäftsregeln-, Kreuzprüfung- und länderspezifische Regeln gruppiert, mit zusätzlichen Gruppen für weitere Standards-Prüfungen und Wertprüfungen. Meldungen und Zusammenfassungen verwenden die Sprache des Benutzers, sofern Übersetzungen verfügbar sind.
* **Vollständigere Prüfungen und klarere Ergebnisse.** Der aktualisierte Validator und der Bericht unterscheiden zwischen Fehlern, Warnungen und dem wirksamen Schweregrad nach Anwendung der organisationsspezifischen Konfiguration. Die Seite heißt **E-Rechnungs-Validierung**.
* **Richtlinien nach Dokumenttyp.** Administratoren können prüfen, ob die E-Rechnungs-Validierung aktiviert ist und ob Fehler die Verarbeitung blockieren. Die Richtlinienansicht identifiziert Subtyp-Überschreibungen, und Richtlinienänderungen werden in einer Änderungshistorie erfasst.
* **XML in einer PDF-Rechnung einsehen.** Der XML-Viewer kann das eingebettete XML in unterstützten ZUGFeRD/Factur-X-PDFs lesen, die von einem Befund referenzierte Position öffnen und zum Dokument zurückkehren.
* **Ablehnung mit dokumentiertem Grund.** Ein berechtigter Prüfer kann ein Dokument direkt aus dem Validierungsbericht ablehnen, sofern es die Voraussetzungen dafür erfüllt. Aus den festgestellten Fehlern bereitet der Bericht eine Begründung vor, die der Prüfer vor der Bestätigung kontrolliert.
* **Weitere Formatkorrekturen.** EDNA-Utility-CII-Rechnungen werden erkannt, und Korrekturen an der XRechnung-Umsatzsteuer-Zuordnung verbessern, wie relevante Rechnungswerte in DocBits-Felder gelangen.

Siehe [E-Dokumenten-Validierungsregeln](../../administration-and-setup/settings/document-processing/e-documents/validation-rules.md).

## FTP/SFTP- und E-Mail-Importe

* **Geführte FTP/SFTP-Einrichtung.** Der Verbindungsassistent trennt Serverdetails, Importoptionen und Konfiguration. Verbindungstests und klarere Fehlermeldungen helfen Administratoren, eine fehlerhafte Verbindung oder einen fehlenden Quellordner zu identifizieren.
* **Importprotokolle nach Schritt.** Den Fortschritt einer Datei durch den FTP-Import nachverfolgen, einschließlich Upload und der konfigurierten Aktion für die Quelldatei.
* **Wiederholungsversuche und Benachrichtigungen konfigurieren.** Legen Sie die Abstände zwischen weiteren Versuchen, die Gesamtdauer der Wiederholungen und die Benachrichtigungsempfänger fest. Nach Ablauf dieses Zeitfensters kann die Verbindung automatisch deaktiviert werden und eine Benachrichtigung an die Empfänger erfolgen. Der Assistent zeigt den Hinweis zur Deaktivierung an.
* **Löschen nach erfolgreichem Import.** Zusätzlich zum Aufbewahren oder Archivieren von Quelldateien können Administratoren wählen, diese nach einem erfolgreichen Import vom FTP/SFTP-Server zu löschen. Archivieren und Löschen sind separate Alternativen.
* **Zuverlässigere Importwiederherstellung.** Überlappende FTP-Läufe werden daran gehindert, dieselbe Quelldatei zweimal hochzuladen. Beim Bearbeiten einer Verbindung bleibt das gespeicherte Passwort erhalten, es sei denn, es wird ersetzt. Die E-Mail-Behandlung markiert eine Nachricht nicht zum Löschen, wenn das Kopieren fehlgeschlagen ist.
* **Unterstützung für signierte E-Mails.** Opaque signierte S/MIME-Nachrichten mit Rechnungen können entpackt statt übersprungen werden.
* **E-Mail-Konfigurationshistorie und -status.** Importeinstellungen zeigen an, wer eine Konfiguration zuletzt gespeichert oder aktiviert hat. Der E-Mail-Eingangsschalter spiegelt den gespeicherten aktiven Status wider, einschließlich einer neu gespeicherten Konfiguration.

Siehe [FTP-Import](../../end-user-and-partner-section/end-user-section/how-to-import-documents/ftp.md) und [FTP-Importverbindung testen](../../administration-and-setup/settings/document-processing/import/test-ftp-import-connection.md).

## Dokumentenverarbeitung und Extraktion

* **Neustart mit gewählter Seitenanzahl.** Das Dashboard bietet eine Neustartaktion, mit der Prüfer festlegen können, wie viele Seiten für das jeweilige Dokument verarbeitet werden sollen, innerhalb der tatsächlichen Seitenanzahl.
* **Verarbeitungslimit einsehen.** Das Dashboard kann bei Dokumenten mit einem Verarbeitungslimit die verarbeiteten Seiten im Verhältnis zur Gesamtzahl anzeigen. Die Organisationseinstellung **Zu verarbeitende Seiten** befindet sich im Abschnitt Dokumentenverarbeitung unter **Klassifizieren & Extrahieren**.
* **Extraktion ausgeblendeter Felder steuern.** Administratoren können über die Einstellung **Ausgeblendete Felder extrahieren** festlegen, ob ausgeblendete Felder an der Extraktion teilnehmen.
* **Schnelleres Arbeiten bei größeren Stapeln.** Neustarts von Dokumentenstapeln, CSV-Importe von Stammdaten, PDF-Verarbeitung und regelbasierte Feldextraktion erhalten Leistungsverbesserungen.
* **Robustere KI-Extraktion.** Zeitüberschreitungen werden als solche gemeldet. Bei unterstützten Modellfehlern kann die Verarbeitung auf ein anderes verfügbares Modell zurückgreifen. Weitere Korrekturen betreffen wiederholte Schlüssel in KI-Ausgaben, konfigurierte Feldsynonyme und leer gespeicherte Tabellendefinitionen.
* **Gerade eingegebene Werte behalten.** Beim Speichern einer Tabellenzelle bleibt der eingegebene Wert erhalten, auch wenn Sie zuvor nicht an eine andere Stelle klicken. Datumsangaben mit durch OCR falsch erkannten Monatsnamen werden zuverlässiger verarbeitet.

## Bestellabgleich, Genehmigung und Export

Der [Leitfaden zu Bestellabgleichregeln](../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-matching-rules.md) erläutert, wie der regelbasierte Abgleich aktiviert, Abgleichstypen und Toleranzen konfiguriert, die Ausführungsreihenfolge festgelegt und Regelversionen verwaltet werden.

* **Abgleich in beide Richtungen.** Dokumentpositionen auswählen und mit Bestellpositionen verbinden, oder von den Bestellpositionen aus starten. Dies ist nützlich, wenn viele Lieferscheinpositionen einer Bestellposition zugeordnet sind.
* **Details bei Eins-zu-viele-Zuordnungen erhalten.** Wenn mehrere Dokumentpositionen einer Bestellposition zugeordnet sind, kann die Abgleichkonfiguration nun für jede Dokumentposition eine eigene Unterposition erhalten. Diese Option ist standardmäßig deaktiviert. Der generische API-Export kann Anfragen nach konfigurierten Positionsspalten gruppieren, etwa für Lieferungen oder Container, die getrennte Datensätze im Zielsystem benötigen.
* **Fallback für letzte Position konfigurieren.** Organisationen können steuern, ob die verbleibende Dokument- und Bestellposition durch den Einzelposition-Fallback abgeglichen werden darf.
* **Genauerer Abgleich und bessere Anzeige.** Korrekturen erhalten die richtige Preisbasis bei Abgleichen mit umgerechneten Verpackungseinheiten, übernehmen den Status der Bestellposition in Lieferplanzeilen und zeigen eingegangene Mengen aus Wareneingangspositionen an.
* **Vorzeitige Genehmigung und doppelte Arbeit verhindern.** Die endgültige Genehmigung wird blockiert, während relevante Bestellabweichungen nicht genehmigt sind. Wiederholte Workflow-Ausführungen erstellen keine weitere offene Aufgabe für dieselbe Gruppe, und Prüfungen auf doppelte Exporte werden vor der Genehmigung durchgeführt.
* **Exported von Finished trennen.** Exportaktionen können den Status nach einem erfolgreichen Export auswählen. **Exported** hat ein eigenes Dashboard-Badge. Organisationen, die die Sperre für abgeschlossene Dokumente aktivieren, verhindern, dass reguläre Workflows oder Neustarts abgeschlossene Dokumente erneut öffnen; autorisierte Überschreibungen werden protokolliert.
* **Einfachere Fehlersuche in Workflows.** Ein Dashboard-Filter findet Dokumente, die durch das Workflow-Ausführungslimit zurückgehalten werden. Workflow-Ausführungen lassen sich in einem Popup prüfen; bei einer abgelehnten Statusänderung wird der aktuelle Dokumentstatus genannt.
* **Weitere Exportkorrekturen.** M3-Validierung und Genehmigungswiederholungen werden angepasst, und bedingte Lieferantenexportkonfigurationen werden korrekt behandelt.

## Tägliche Benutzerfreundlichkeit und Zugriff

* **Zuverlässigere Navigation.** Für geänderte Dokumentadressen gibt es Weiterleitungen von den alten Links. NOVA-Direktlinks behalten den vorgesehenen Release-Kanal auch während der Anmeldung bei. Die Fortschrittsanzeige zeigt, welcher Seitenteil gerade geladen wird.
* **Persönliche Arbeitseinstellungen.** Die Spaltenreihenfolge der Bestellungen wird pro Benutzer gespeichert, und der Genehmigungsbildschirm merkt sich das geöffnete Seitenpanel des Benutzers.
* **Zuverlässigere Aufgaben- und Dashboard-Ansichten.** Aufgaben ohne Bearbeiter können aufgelistet, geöffnet und zugewiesen werden. Das Aufgabenboard wird neu geladen, wenn die ausgewählte Organisation bereit ist, benutzerdefinierte Dashboard-Datumsbereiche werden korrekt angewendet, und doppelte Dokumentzeilen werden vermieden.
* **Bessere Beschriftungen und Protokolle.** Administratoren können Übersetzungsschlüssel für Felder und Tabellenspalten bearbeiten. Dokumentprotokollspalten können in der Größe angepasst werden, benutzerdefinierte Dashboard-Spalten verarbeiten Feldkennungen mit gemischter Groß-/Kleinschreibung, und lange Beschriftungen und Dateinamen werden konsistenter dargestellt.
* **Benachrichtigungsbereich.** E-Mail-Regeln für Dokumentstatus können auf eine Unterorganisation beschränkt werden.
* **Lieferanten-Onboarding.** Magic-Links zur Registrierung im Lieferantenportal bleiben **21 Tage statt 7 Tage** gültig. Administratoren können außerdem die Überschrift für Upload-Fehler eines Dateifelds in einem Lieferanten-Layout konfigurieren.
* **Zuverlässigkeit der Anmeldung.** Die SAML-Anmeldung verwendet keine abgelaufenen oder widerrufenen Sitzungen mehr. Die Management-Anmeldung unterstützt den erforderlichen MFA-Schritt, und inaktive Mitgliedschaften können keine neue Einladung zum Festlegen eines Passworts erhalten.
* **Idea-Board-Bilder.** Hochgeladene Bilder werden getrennt von der Ideenbeschreibung gespeichert und bereitgestellt, was die Bildverarbeitung verbessert.
* **Gesteuerter Kanalwechsel.** Die Einstellung für den Release-Kanal kann schreibgeschützt gemacht werden, wenn der Wechsel für die Umgebung nicht aktiviert ist. Die Verfügbarkeit entnehmen Sie bitte der Release-Ankündigung.

## Verbundene Assistenten und Integrationstools

Für Organisationen und Partner, die die DocBits MCP-Integration nutzen, stellt NOVA Tools bereit, um aufgelöste Validierungsregeln aufzulisten, eine Regel gegen ein Dokument zu testen, ohne Änderungen zu speichern, und die gespeicherten Nachweise zur Regelausführung zu erläutern. Verbundene Assistenten können außerdem Verbesserungsanfragen auflisten und eine von Administratoren autorisierte Genehmigung über denselben Review-Prozess wie in der Web-App einreichen. Bestehende Organisations- und Dokumentberechtigungen gelten weiterhin.

## Bereits in VESTA vorhandene Funktionen

NOVA übernimmt auch die unten aufgeführten Funktionen. Wo der Zugriff zuvor auf die VESTA-Beta beschränkt war, ist die reguläre Verfügbarkeit Teil dieses NOVA-Releases und für den VESTA-Hotfix am 11. November 2026 geplant. Die Liste beschreibt die früheren Funktionen zusammen mit den oben erläuterten Verfügbarkeitsänderungen und Erweiterungen:

* Der ursprüngliche Einstellungs-Assistent, seine Dokumentationssuche, der grundlegende Vorschau-/Bestätigungs-/Rückgängig-Machen-Flow und proaktive E-Mail-/FTP-Import-Statuswarnungen.
* Die KI-Stufen Fast, Full, Nexus und Auto sowie die Vision-Modus-Einstellung.
* Die Header-Feld-Prüfung und der ursprüngliche Wert-Herkunftsbericht.
* Die erste Touchless-Intelligence-Veröffentlichung, Lieferanten-Diagnose, Massenanalyse und das Bestellentscheidungsdiagramm.
* Die zugrunde liegenden Regel-Engines für Validierung, Transformation und Layoutauswahl, Transformationen nach der Stammdatenabfrage und das grundlegende Regelausführungsprotokoll.
* Frühere Verbesserungen der Dashboard-Suche, MFA, verifizierte E-Mail-Domains der Organisation, Toleranzen für Zuschläge und die Erhöhung des Workflow-Ausführungslimits auf 50.

Siehe den [VESTA-Hotfix vom 14. Oktober](incremental-updates-14-october-2026.md), den [Hotfix vom 15. September](incremental-updates-15-september-2026.md) und die [früheren Release Notes](README.md#vesta-hotfix-releases) für die VESTA-Release-Historie.

## NOVA-Serviceversionen

Dies sind die Versionen und Bereitstellungszeitpunkte des **seit dem 16. Oktober 2026 verfügbaren NOVA-Sandbox-Builds**. Der Produktionsrelease ist für den **4. November 2026** geplant; dieser Sandbox-Versionsstand legt die endgültigen Produktionsversionen nicht fest. Die Zeitstempel beziehen sich auf die Bereitstellung der einzelnen Services.

| Service | Version | Bereitstellungszeitstempel |
| --- | --- | --- |
| API Service | `13.26.5` | 16.10.2026 11:57:49 |
| Auth Bridge | `0.5.11` | 08.10.2026 10:56:15 |
| Auth Service | `1.84.3` | 16.10.2026 12:19:50 |
| Auto Accounting | `1.23.6` | 15.09.2026 09:42:57 |
| Barcode Service | `1.20.3` | 15.10.2026 14:17:18 |
| Docflow Service | `2.13.9` | 15.10.2026 16:14:37 |
| Docnet Service | `1.59.1` | 12.10.2026 00:59:12 |
| Email Service | `1.44.4` | 16.10.2026 11:44:58 |
| Extraction Service | `1.63.1` | 15.10.2026 19:34:17 |
| FTP Service | `1.37.4` | 15.10.2026 10:42:01 |
| Fulltext Service | `1.46.1` | 12.10.2026 05:16:16 |
| Ideas Service | `0.5.6` | 14.10.2026 12:06:00 |
| OCR Service | `1.11.8` | 12.10.2026 01:00:00 |
| Operator Service | `1.45.0` | 12.10.2026 09:35:25 |
| PO Match Service | `1.65.7` | 14.10.2026 16:14:20 |
| Web App | `10.72.2` | 16.10.2026 12:04:41 |

Die Versionsnummern entwickeln sich auf beiden Kanälen unabhängig voneinander. Eine höhere Nummer bedeutet daher nicht automatisch eine neue Kundenfunktion. Die geprüften Änderungen an Auto Accounting, Barcode, Docnet, Fulltext, OCR und Operator dienen der Wartung oder einer zuverlässigeren Verarbeitung; sie führen in diesem Vergleich keinen eigenen neuen Arbeitsablauf für Kunden ein. Aktualisierungen von Auth Bridge verbessern die Zuverlässigkeit der regionsübergreifenden Kontosynchronisation.
