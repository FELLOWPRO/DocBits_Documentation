# Test: bestandsimport 1

## Doel

Deze tests zijn bedoeld om ervoor te zorgen dat ons bestandsimportsysteem correct werkt. We testen specifiek de import van PDF- en TIFF-bestanden in het systeem, om ervoor te zorgen dat ze met succes worden verwerkt en opgeslagen.

#### Testvoorbereiding en opruimen

* **Setup:**
  * Vóór elke test registreren we een installatiebericht.
  * **Opschonen:** Na elke test ruimen we op door alle documenten die door de testgebruiker zijn gemaakt uit de database te verwijderen om ervoor te zorgen dat overgebleven gegevens geen invloed hebben op volgende tests.

#### Testscenario’s

1. **Import PDF File:**
   * **Test voor PDF-import (`test_import_pdf`):**
     * Importeer een PDF-bestand (`FellowBananaInvoice.pdf`) in het systeem.
     * **Verwachte uitkomst:** Het bestand zou met succes moeten worden geïmporteerd, waarbij een document ID wordt geretourneerd.
2. **Import TIFF File:**
   * **Test voor TIFF-import (`test_import_tiff`):**
     * Importeer een TIFF-bestand (`TIFF_FILE.TIF`) in het systeem.
     * **Verwachte uitkomst:** Het bestand zou met succes moeten worden geïmporteerd, waarbij een document ID wordt geretourneerd.

## Gedetailleerde uitleg van elke test

* **Instellen en opruimen:**
  * **Logging:** Voor elke test wordt een installatie- en opschoonbericht vastgelegd.
  * **Database opruimen (`clean_documents`):** Verwijdert alle documenten die door de testgebruiker zijn gemaakt uit de database om de status schoon te houden.
*   **Bestandimporttests:**

    **Import PDF File:**

    * **Gebruiker laden:** Laad de testgebruiker.
    * **Bestandspad:** Geef het pad op naar het PDF bestand (`tests/files/pdfs/FellowBananaInvoice.pdf`).
    * **Bestand importeren:** Gebruik de klasse `FileImporter` om het bestand PDF te importeren.
    * **Reactie controleren:** Zorg ervoor dat het antwoord een lijst is met een succesbericht en een document ID.

    **Import TIFF File:**

    * **Gebruiker laden:** Laad de testgebruiker.
    * **Bestandspad:** Geef het pad op naar het TIFF bestand (`tests/files/pdfs/TIFF_FILE.TIF`).
    * **Bestand importeren:** Gebruik de klasse `FileImporter` om het bestand TIFF te importeren.
    * **Reactie controleren:** Zorg ervoor dat het antwoord een lijst is met een succesbericht en een document ID.

## Codestructuur

* **Logger:** Wordt gebruikt om foutopsporingsberichten te loggen tijdens installatie, opschoning en testuitvoering.
* **Database Helper:** Voert query's uit zonder resultaten te retourneren voor opschoning.
* **Bestandimporteur:** Verwerkt de import van bestanden in het systeem.
* **Fixtures:** `set_up` armatuur om de installatie en opruiming voor tests te beheren.
* **Tests:**
  * `test_import_pdf`: Tests waarbij een PDF-bestand wordt geïmporteerd.
  * `test_import_tiff`: Tests waarbij een TIFF-bestand wordt geïmporteerd.

#### Samenvatting

Deze tests zorgen ervoor dat onze functionaliteit voor het importeren van bestanden werkt zoals verwacht voor zowel PDF- als TIFF-bestanden. Door deze aanpak te volgen, verifiëren we dat bestanden correct worden geïmporteerd en dat het systeem zonder problemen verschillende bestandstypen kan verwerken.
