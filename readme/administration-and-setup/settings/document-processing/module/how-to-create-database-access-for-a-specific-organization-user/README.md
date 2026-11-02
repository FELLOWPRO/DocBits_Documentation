# Databasetoegang aanmaken voor een specifieke organisatiegebruiker

### **1. Log in bij DocBits** <a href="#id-1.-login-to-the-docbits" id="id-1.-login-to-the-docbits"></a>

1. Ga naar de aanmeldpagina van uw applicatie.
2. Voer uw inloggegevens (gebruikersnaam en wachtwoord) in om u aan te melden.

### **2. Open de Instellingen** <a href="#id-2.-access-the-settings" id="id-2.-access-the-settings"></a>

1. Zoek na het aanmelden het pictogram **Settings** (tandwiel ⚙️) in de zijbalk links.
2. Klik op **Settings** om het systeemconfiguratiepaneel te openen.

### **3. Open de module Documentverwerking** <a href="#id-3.-open-the-document-processing-module" id="id-3.-open-the-document-processing-module"></a>

1. Zoek in de **Settings** het onderdeel **Document Processing**.
2. Zoek onder **Document Processing** de optie **Module** en klik erop.
   * Hiermee opent u de bijbehorende modulepagina waar u verder kunt gaan met het aanmaken van een gebruiker voor de database.

### 4. Stappen om de AI Document- en databasegebruiker in te schakelen en te openen: <a href="#id-4.-steps-to-enable-and-access-the-ai-document-and-database-user" id="id-4.-steps-to-enable-and-access-the-ai-document-and-database-user"></a>

1. **Functies in-/uitschakelen**:
   * Gebruik de schakelaars aan de rechterkant om specifieke functies in of uit te schakelen:
     * **AI Document Warehouse**: Schakel dit in om toegang tot AI-gerelateerde functies te krijgen.
     * **DB Access**: Schakel dit in om de gebruiker databasetoegang te geven.
2. **Databasegegevens**:
   * Het dashboard toont de volgende databaseverbindingsgegevens:
     * **Username**: Er wordt een unieke gebruikersnaam weergegeven
     * **Password**: Zorg ervoor dat het wachtwoord veilig wordt opgeslagen of gekopieerd.
     * **Database**: De naam van de database
     * **Host**: De hostnaam
     * **Port**: De poort
     * **SSL Mode:** De verbinding vereist `sslmode=require` voor beveiligde communicatie.
3. **Gegevens kopiëren**:
   * Gebruik de kopieerpictogrammen naast elk veld om de gegevens snel te kopiëren voor gebruik in uw databaseclient of applicatie.
4. **Verbinding via DBeaver**:
   * Verbinden via Host
     * kies PostgreSQL
     * Vul de vereiste gegevens in
     * ga naar het tabblad SSL en vink Use SSL aan. Ga omlaag naar SSL mode en selecteer require
   * Verbinden via URL
     * Vul de vereiste gegevens in:\n - vervang Host door de verstrekte hostgegevens\n - vervang Port door de verstrekte poortgegevens\n - vervang Database door de verstrekte databasegegevens\n - selecteer voor Username de verstrekte gebruikersnaam\n - selecteer voor Password het verstrekte wachtwoord
5. **Test de verbinding**:
   * Klik op de knop **"Test Connection"** om te controleren of de gegevens en verbindingsdetails correct zijn.
   * Als de test slaagt, gaat u verder met verbinden.
6. **Verken de database**:
   * Navigeer na het verbinden in uw databaseclient naar het gedeelte **schema** of **tables**.
   * Controleer de beschikbare tabellen.
