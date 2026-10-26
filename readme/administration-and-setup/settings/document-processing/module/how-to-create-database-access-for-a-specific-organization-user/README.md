# Datenbankzugriff für einen bestimmten Organisationsbenutzer erstellen

### **1. Bei DocBits anmelden** <a href="#id-1.-login-to-the-docbits" id="id-1.-login-to-the-docbits"></a>

1. Rufen Sie die Anmeldeseite Ihrer Anwendung auf.
2. Geben Sie Ihre Anmeldedaten (Benutzername und Passwort) ein, um sich anzumelden.

### **2. Die Einstellungen öffnen** <a href="#id-2.-access-the-settings" id="id-2.-access-the-settings"></a>

1. Suchen Sie nach der Anmeldung das Symbol **Settings** (Zahnrad ⚙️) in der linken Seitenleiste.
2. Klicken Sie auf **Settings**, um das Konfigurationsfenster des Systems zu öffnen.

### **3. Das Modul „Document Processing“ öffnen** <a href="#id-3.-open-the-document-processing-module" id="id-3.-open-the-document-processing-module"></a>

1. Suchen Sie in den **Settings** den Abschnitt **Document Processing**.
2. Suchen Sie unter **Document Processing** die Option **Module** und klicken Sie darauf.
   * Damit öffnet sich die zugehörige Modulkonfigurationsseite, auf der Sie mit der Erstellung des Benutzers für die Datenbank fortfahren können.

### 4. Schritte zum Aktivieren und Aufrufen des KI-Dokument- und Datenbankbenutzers: <a href="#id-4.-steps-to-enable-and-access-the-ai-document-and-database-user" id="id-4.-steps-to-enable-and-access-the-ai-document-and-database-user"></a>

1. **Funktionen umschalten**:
   * Mit den Schaltern auf der rechten Seite aktivieren oder deaktivieren Sie bestimmte Funktionen:
     * **AI Document Warehouse**: Schalten Sie diese Option ein, um Zugriff auf KI-bezogene Funktionen zu erhalten.
     * **DB Access**: Schalten Sie diese Option ein, um dem Benutzer Datenbankzugriff zu gewähren.
2. **Datenbank-Zugangsdaten**:
   * Das Dashboard zeigt die folgenden Details zur Datenbankverbindung an:
     * **Username**: Ein eindeutiger Benutzername wird angezeigt.
     * **Password**: Stellen Sie sicher, dass das Passwort sicher gespeichert oder kopiert wird.
     * **Database**: Der Name der Datenbank.
     * **Host**: Der Hostname.
     * **Port**: Der Port.
     * **SSL Mode:** Die Verbindung erfordert `sslmode=require` für eine sichere Kommunikation.
3. **Zugangsdaten kopieren**:
   * Mit den Kopiersymbolen neben den einzelnen Feldern kopieren Sie die Zugangsdaten schnell zur Verwendung in Ihrem Datenbank-Client oder Ihrer Anwendung.
4. **Verbindung über DBeaver**:
   * Verbindung über Host
     * Wählen Sie PostgreSQL.
     * Füllen Sie die erforderlichen Informationen aus.
     * Wechseln Sie auf den Tab SSL und aktivieren Sie „Use SSL“. Scrollen Sie nach unten zu SSL mode und wählen Sie „require“.
   * Verbindung über URL
     * Füllen Sie die erforderlichen Informationen aus:\n - ersetzen Sie Host durch die bereitgestellten Host-Informationen\n - ersetzen Sie Port durch die bereitgestellten Port-Informationen\n - ersetzen Sie Database durch die bereitgestellten Datenbank-Informationen\n - wählen Sie für Username die bereitgestellten Benutzernamen-Informationen\n - wählen Sie für Password die bereitgestellten Passwort-Informationen
5. **Verbindung testen**:
   * Klicken Sie auf die Schaltfläche **„Test Connection“**, um sicherzustellen, dass die Zugangsdaten und Verbindungsdetails korrekt sind.
   * Wenn der Test erfolgreich ist, fahren Sie mit dem Verbinden fort.
6. **Datenbank erkunden**:
   * Navigieren Sie nach dem Verbinden in Ihrem Datenbank-Client zum Bereich **Schema** oder **Tables**.
   * Prüfen Sie die verfügbaren Tabellen.
