# Test: verbinding voor FTP-import

#### Doel

Deze tests zorgen ervoor dat ons FTP importsysteem correct werkt. We verifiëren dat we een nieuwe FTP importverbinding kunnen toevoegen, testen de verbinding, activeren/deactiveren deze en ruimen deze daarna op.

{% embed url="https://grafana.polydocs.io/d-solo/b6ad3a9c-260c-46a3-9ade-47691e743d4d/docbits?from=1715746603760&orgId=1&panelId=84&refresh=1m&to=1715768203760" %}

## Testscenario’s

1. **Setup:**
   * **Omgevingsvariabelen:** Laad noodzakelijke details zoals FTP serverinformatie en referenties uit omgevingsvariabelen.
2.  **FTP Connection Tests:**

    **Nieuwe verbinding toevoegen:**

    * **Test Nieuwe toevoegen FTP Verbinding importeren (`test_add_new_ftp_import_connection`):**
      * Voeg een nieuwe FTP importverbinding toe met de opgegeven inloggegevens en servergegevens.
      * **Verwachte uitkomst:** De verbinding zou met succes moeten worden toegevoegd.

    **Deactivate Connection:**

    * **Test deactiveren FTP Verbinding importeren (`test_deactivate_ftp_import_connection`):**
      * Deactiveer de nieuw toegevoegde FTP importverbinding.
      * **Verwachte uitkomst:** De verbinding zou met succes moeten worden gedeactiveerd.

    **Test Connection:**

    * **Test van de FTP-verbinding (`test_test_ftp_connection`):**
      * Test of de FTP importverbinding succesvol verbinding kan maken met de FTP server.
      * **Verwachte uitkomst:** De verbinding zou met succes moeten worden getest.

    **Verbinding controleren in lijst:**

    * **Testcontrole FTP Verbinding in lijst (`test_check_ftp_connection_in_list`):**
      * Controleer of de nieuw toegevoegde FTP importverbinding aanwezig is in de lijst met verbindingen.
      * **Verwachte uitkomst:** De verbinding moet in de lijst worden gevonden.

    **Controleer verbinding gedeactiveerd:**

    * **Testcontrole FTP Verbinding gedeactiveerd (`test_check_ftp_connection_deactivated`):**
      * Controleer of de importverbinding FTP in de lijst als inactief is gemarkeerd.
      * **Verwachte uitkomst:** De verbinding moet inactief zijn.

    **Testmap toevoegen:**

    * **Test Testmap toevoegen aan verbinding (`test_add_test_folder_to_connection`):**
      * Voeg een standaardmap (testmap) toe aan de FTP importverbinding.
      * **Verwachte uitkomst:** De standaardmap zou met succes moeten worden toegevoegd.

    **Reactivate Connection:**

    * **Test opnieuw activeren FTP Verbinding importeren (`test_reactivate_ftp_import_connection`):**
      * Activeer de eerder gedeactiveerde FTP importverbinding opnieuw.
      * **Verwachte uitkomst:** De verbinding zou met succes opnieuw moeten worden geactiveerd.

    **Controleer verbinding opnieuw geactiveerd:**

    * **Testcontrole FTP Verbinding opnieuw geactiveerd (`test_check_ftp_connection_reactivated`):**
      * Controleer of de importverbinding FTP in de lijst als actief is gemarkeerd.
      * **Verwachte uitkomst:** De verbinding moet actief zijn.

    **Cleanup:**

    * **Testopschoning FTP Importeren (`test_cleanup_ftp_import`):**
      * Verwijder de importverbinding FTP om op te ruimen na de tests.
      * **Verwachte uitkomst:** De verbinding zou met succes moeten worden verwijderd.

## Gedetailleerde uitleg van elke test

* **Installatie en initialisatie:**
  * **Initialiseer gedeelde gegevens:** Bereid gedeelde gegevens voor op tests.
* **FTP Connection Tests:**
  * **Nieuwe verbinding toevoegen:** Voeg een nieuwe FTP importverbinding toe met de opgegeven inloggegevens en servergegevens.
  * **Verbinding deactiveren:** Deactiveer de nieuw toegevoegde FTP importverbinding.
  * **Verbinding testen:** Test of de importverbinding FTP succesvol verbinding kan maken met de FTP-server.
  * **Verbinding controleren in lijst:** Controleer of de nieuwe FTP importverbinding aanwezig is in de lijst met verbindingen.
  * **Controleer verbinding gedeactiveerd:** Controleer of de importverbinding FTP in de lijst als inactief is gemarkeerd.
  * **Testmap toevoegen:** Voeg een standaardmap (testmap) toe aan de FTP importverbinding.
  * **Verbinding opnieuw activeren:** Heractiveer de eerder gedeactiveerde FTP importverbinding.
  * **Controleer of de verbinding weer actief is:** Zorg ervoor dat de FTP importverbinding in de lijst als actief is gemarkeerd.
  * **Opschonen:** Verwijder de FTP importverbinding om op te ruimen na de tests.

\\
