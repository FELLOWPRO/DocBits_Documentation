# Calculate Columns with

<figure><img src="../../../../.gitbook/assets/image (294).png" alt="" width="563"><figcaption></figcaption></figure>

## **Doel:**

De workflow-kaart **"Calculate Columns in Table"** wordt gebruikt om berekeningen tussen kolommen in een geselecteerde tabel uit te voeren. Hiermee kunnen gebruikers kolommen selecteren, een wiskundige bewerking toepassen en het resultaat in een opgegeven resultaatkolom opslaan.

## **Onderdelen van de kaart:**

1. **Table Name**
   * **Beschrijving:** Geeft de **tabel** op waarin de kolommen worden berekend.
   * **Detail:** Er wordt een dropdownlijst van alle beschikbare **tabellen** geboden om uit te selecteren.
2. **Column Name (1st Column)**
   * **Beschrijving:** Geeft de **eerste kolom** op die bij de berekening betrokken is.
   * **Detail:** Er wordt een lijst van alle beschikbare **kolommen** geboden om uit te selecteren.
3. **Operation**
   * **Beschrijving:** Definieert de wiskundige bewerking die tussen de geselecteerde kolommen wordt toegepast.
   * **Opties:**
     * **Add (+):** Telt de waarde van de tweede kolom op bij de waarde van de eerste kolom.
     * **Subtract (-):** Trekt de waarde van de tweede kolom af van de waarde van de eerste kolom.
     * **Multiply (\*):** Vermenigvuldigt de waarde in de eerste kolom met de waarde in de tweede kolom.
     * **Divide (/):** Deelt de waarde in de eerste kolom door de waarde in de tweede kolom.
4. **Column Name (2nd Column)**
   * **Beschrijving:** Geeft de **tweede kolom** op die bij de berekening betrokken is.
   * **Detail:** Er wordt een lijst van beschikbare **kolommen** geboden om uit te selecteren.
5. **Result Column**
   * **Beschrijving:** Geeft de **kolom** op waarin het resultaat van de berekening wordt opgeslagen.
   * **Detail:** Er wordt een lijst van beschikbare **kolommen** geboden waarin de berekende waarde wordt opgeslagen.

## **Functionaliteit:**

* **Voorwaarde-evaluatie:**\
  De kaart voert de actie alleen uit als zowel de **"Where"**- als de **"And"**-secties als true worden geëvalueerd.
* **Kolomberekening:**\
  De kaart voert de geselecteerde wiskundige bewerking uit tussen de twee gekozen kolommen.
* **Resultaatopslag:**\
  Het resultaat van de berekening wordt opgeslagen in de geselecteerde **resultaatkolom**.

## **Opzet en configuratie:**

* **Tabel selecteren:**\
  Kies de **tabel** waarin de kolommen worden berekend.
* **Kolommen kiezen:**\
  Selecteer de **eerste kolom** en **tweede kolom** die in de berekening worden gebruikt.
* **Bewerking selecteren:**\
  Kies de wiskundige bewerking (**Add (+)**, **Subtract (-)**, **Multiply (\*)**, **Divide (/)**) die tussen de kolommen wordt toegepast.
* **Resultaatkolom selecteren:**\
  Kies de **resultaatkolom** waarin de berekening wordt opgeslagen.

## **Conclusie:**

De workflow-kaart **"Calculate Columns in Table"** stelt gebruikers in staat dynamische berekeningen tussen kolommen in een tabel uit te voeren en de resultaten in een aangewezen kolom op te slaan. De kaart biedt flexibiliteit om verschillende wiskundige bewerkingen toe te passen en zorgt ervoor dat het resultaat in de opgegeven kolom wordt opgeslagen.
