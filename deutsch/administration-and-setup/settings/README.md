# Einstellungen

<figure><img src="../../.gitbook/assets/settings_overview.png" alt="Übersicht der Einstellungen"><figcaption><p>Übersichtsseite der Einstellungen</p></figcaption></figure>

Der Bereich „Settings“ ist Ihre zentrale Anlaufstelle für die Konfiguration von DocBits. Er ist in fünf Hauptbereiche gegliedert:

## 1. Organisation & Zugriff

Verwalten Sie Ihr Unternehmensprofil und steuern Sie, wer worauf zugreifen darf.

* **Company Information**: Geben Sie Firmenname, Adresse, Steuernummer und weitere rechtliche Kennungen ein.
* **Users**: Fügen Sie Benutzerkonten hinzu, bearbeiten oder deaktivieren Sie sie und weisen Sie Rollen zu (Admin, System Admin).
* **Sub-Organizations**: Erstellen und verwalten Sie Unterorganisationen für Setups mit mehreren Gesellschaften.
* **Groups and Permissions**: Definieren Sie Benutzergruppen und konfigurieren Sie detaillierte Berechtigungen für jede Gruppe.

## 2. Dokumentenverarbeitung

Konfigurieren Sie, wie Dokumente importiert, verarbeitet und exportiert werden.

* **Documents Expiry**: Legen Sie Regeln für das automatische Löschen von Dokumenten fest (z. B. Löschung nach 48 Stunden, 1 Woche usw.).
* **Document Types**: Definieren und konfigurieren Sie die Dokumenttypen, die DocBits verarbeitet (Rechnungen, Bestellungen, Lieferscheine usw.), einschließlich Felder, Tabellenspalten, Skripte und mehr.
* **Import**: Richten Sie ein, wie Dokumente in DocBits gelangen, per E-Mail (IMAP/Office 365), FTP oder Datei-Upload. Konfigurieren Sie Dateitypen und Seitenlimits.
* **Rule Management**: Definieren Sie Regeln zur Konfliktlösung für den Abgleich von Rechnungen mit Bestellungen, einschließlich Toleranzeinstellungen und Genehmigungsworkflows.
* **OCR Settings**: Konfigurieren Sie Qualitätsschwellenwerte der optischen Zeichenerkennung (OCR), die Nutzung von E-Text, die AI-OCR-Version und das Verhalten der Tabellenextraktion.
* **Classification and Extraction**: Richten Sie Dokumenttrennung, Betragsformatierung, Methoden der Tabellenextraktion, Klassifizierungsregeln und KI-Modelle ein.
* **Lookup Master Data**: Konfigurieren Sie, wie extrahierte Daten anhand der Stammdaten aus Ihrem ERP-System (z. B. Lieferantenkonten, Bestellungen) validiert werden.
* **List of Values**: Erstellen und verwalten Sie vordefinierte Wertelisten für Dropdown-Felder und die Datenvalidierung.
* **Export**: Konfigurieren Sie, wie und wohin verarbeitete Dokumente gesendet werden, per Webhook, SFTP, SMB oder Infor-Integrationen (IDM, ION, M3, Infor ERP / SAP).
* **Module**: Aktivieren oder deaktivieren Sie optionale Funktionen wie PO Dashboard, Auto Accounting, Supplier Portal, Workflow Builder, QR-Code Extraction und mehr.
* **Decision Trees**: Erstellen Sie regelbasierte Entscheidungslogik mit einem visuellen Designer. Unterstützt mehrere Policies (Unique, First, Priority, Collect usw.).
* **Agent Setup**: Erstellen und verwalten Sie Automatisierungs-Agenten und Kommunikationskanäle für automatisierte Workflows der Dokumentenverarbeitung.

## 3. Kommunikation & Benachrichtigungen

Steuern Sie, wie DocBits mit Benutzern kommuniziert und eingehende E-Mails verarbeitet.

* **Email Notification**: Konfigurieren Sie E-Mail-Benachrichtigungen für Ereignisse der Dokumentenverarbeitung und Statusänderungen.
* **Email Templates**: Erstellen und verwalten Sie wiederverwendbare E-Mail-Vorlagen für Benachrichtigungen, nach Dokumenttyp organisiert.
* **Email Ingestion**: Konfigurieren Sie, wie eingehende E-Mails automatisch klassifiziert und in Dokumente umgewandelt werden. Enthält Regeln für Klassifizierung, Feldextraktion, Verarbeitung, Absenderverwaltung und Training, organisiert nach Dokumenttyp (Orders, Invoices, Quotes, Delivery Notes, COA, PO Confirm).

## 4. System & Administration

Überwachen Sie den Systemzustand, verwalten Sie Integrationen und sorgen Sie für Sicherheit.

* **Integration & SSO**: Konfigurieren Sie API-Schlüssel für externe Integrationen und richten Sie Single Sign-On (SSO) mit Identitätsanbietern ein.
* **Watchdog**: Richten Sie den Watchdog-Dienst für den automatischen Dokumentenimport aus lokalen Verzeichnissen ein.
* **Dashboard**: Passen Sie das Verhalten des Dashboards an, einschließlich Filter, Exporteinstellungen, Aktionsberechtigungen und Optionen zur Statusanzeige.
* **Activity Logging**: Sehen Sie Systemereignisprotokolle in Echtzeit ein, gefiltert nach Schweregrad (Debug, Info, Warning, Error), Zeitraum und Dienst.
* **Analytics**: Greifen Sie auf detaillierte Analyse-Dashboards zu, darunter Logs Analytics, Auth-Security-Überwachung und API Metrics mit Real User Monitoring (RUM).
* **Access Audit**: Aktivieren und prüfen Sie Audit-Trails, die alle Aktionen zum Erstellen, Aktualisieren und Löschen in Ihrer Organisation für Compliance und Sicherheit nachverfolgen.
* **System Licenses**: Zeigen Sie Informationen zu API-Lizenzen und deren Nutzung an und verwalten Sie sie.
* **Cache Management**: Konfigurieren Sie automatische Intervalle (TTL) zum Leeren der Caches für Received Delivery, Purchase Order und Task/Notification.
* **Fulltext Search Settings**: Konfigurieren Sie die Volltextsuche über Ihre Dokumente und Daten (erfordert, dass das Modul Fulltext Search aktiviert ist).

## 5. Lieferanteneinstellungen

Konfigurieren Sie das Supplier Portal und verwalten Sie lieferantenbezogene Workflows.

* **Supplier General Settings**: Richten Sie die Einladungsfelder des Lieferantenportals ein, konfigurieren Sie Workflow-Status (Not Invited, Open, Pending Registration, Approved, Rejected) und verwalten Sie die Genehmigungseinstellungen.
* **Email Templates**: Erstellen und verwalten Sie E-Mail-Vorlagen speziell für die Kommunikation mit Lieferanten.
* **Supplier Layout**: Passen Sie Layout und Erscheinungsbild des Supplier Portal an.
* **Export Configuration**: Konfigurieren Sie, wie Lieferantendaten in externe Systeme exportiert werden.
* **Supplier Group**: Erstellen und verwalten Sie Lieferantengruppen, um Ihre Lieferanten zu kategorisieren und zu organisieren.
* **User and Supplier Group Mapping**: Verknüpfen Sie interne Benutzer mit bestimmten Lieferantengruppen, um Sichtbarkeit und Zugriff zu steuern.
