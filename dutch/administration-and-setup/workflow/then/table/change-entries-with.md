# Change Entries with

<figure><img src="../../../../.gitbook/assets/image (293).png" alt="" width="563"><figcaption></figcaption></figure>

## **Doel:**

De workflow-kaart **"Change Entries in Table"** wordt gebruikt om vermeldingen in een opgegeven databasetabel bij te werken. Hiermee kunt u een **tabel** en **kolom** selecteren en vervolgens wiskundige bewerkingen (optellen, aftrekken, vermenigvuldigen of delen) op de waarden in die kolom uitvoeren, met een opgegeven waarde.

## **Onderdelen van de kaart:**

1. **Table Name**
   * **Beschrijving:** Geeft de **tabel** op waarin vermeldingen worden bijgewerkt.
   * **Detail:** Er wordt een dropdownlijst van beschikbare **tabellen** geboden, waarmee u de doeltabel voor het bijwerken van vermeldingen kunt selecteren.
2. **Column Name**
   * **Beschrijving:** Geeft de **kolom** binnen de geselecteerde tabel op die wordt bijgewerkt.
   * **Detail:** Er wordt een lijst van alle beschikbare **kolommen** geboden om uit te selecteren.
3. **Operation**
   * **Beschrijving:** Definieert de wiskundige bewerking die op de **kolom**waarden wordt uitgevoerd.
   * **Opties:**
     * **Add (+):** Telt een opgegeven **waarde** op bij de huidige waarde in de geselecteerde kolom.
     * **Subtract (-):** Trekt een opgegeven **waarde** af van de huidige waarde in de geselecteerde kolom.
     * **Multiply (\*):** Vermenigvuldigt de huidige waarde in de geselecteerde kolom met een opgegeven **waarde**.
     * **Divide (/):** Deelt de huidige waarde in de geselecteerde kolom door een opgegeven **waarde**.
4. **Value**
   * **Beschrijving:** Geeft de **waarde** op die in de geselecteerde bewerking wordt gebruikt.
   * **Detail:** Dit is het getal dat wordt opgeteld, afgetrokken, vermenigvuldigd of gedeeld met de vermeldingen in de geselecteerde kolom.

## **Functionaliteit:**

* **Voorwaarde-evaluatie:**\
  De kaart voert de actie alleen uit als zowel de **"Where"**- als de **"And"**-secties als true worden geëvalueerd.
* **Tabelvermelding bijwerken:**\
  De kaart voert de geselecteerde bewerking (**+**, **-**, **\*** of **/**) uit op de waarden in de gekozen **kolom** van de geselecteerde **tabel**, met de opgegeven **waarde**.

## **Opzet en configuratie:**

* **Tabel selecteren:**\
  Kies de **tabel** waarin de wijzigingen worden toegepast.
* **Kolom kiezen:**\
  Selecteer de **kolom** binnen de tabel die u wilt bijwerken.
* **Bewerking selecteren:**\
  Kies de wiskundige bewerking (**+**, **-**, **\***, **/**) die op de waarden van de geselecteerde kolom wordt toegepast.
* **Waarde invoeren:**\
  Geef de **waarde** op die in de geselecteerde bewerking wordt gebruikt.

## **Conclusie:**

De workflow-kaart **"Change Entries in Table"** maakt geautomatiseerde updates van databasevermeldingen mogelijk door een **tabel**, **kolom** en gewenste **wiskundige bewerking** te selecteren. Deze kaart is essentieel voor het uitvoeren van bulkgegevensaanpassingen of berekeningen binnen uw database.
