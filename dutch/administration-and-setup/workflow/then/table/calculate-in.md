# Calculate in



<figure><img src="../../../../.gitbook/assets/image (295).png" alt="" width="563"><figcaption></figcaption></figure>

## **Doel:**

Met de workflow-kaart **"Calculate with Regex Dependency"** kunnen gebruikers berekeningen tussen kolommen in een geselecteerde tabel uitvoeren, met een toegevoegde voorwaarde op basis van een reguliere-expressie-(regex)-patroon dat op een afhankelijkheidskolom wordt toegepast. Als het patroon overeenkomt, wordt de berekening uitgevoerd en wordt het resultaat in de opgegeven resultaatkolom opgeslagen.

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
     * **Subtract (-):** Trekt de waarde van de tweede kolom af van de eerste kolom.
     * **Multiply (\*):** Vermenigvuldigt de waarde van de eerste kolom met de waarde in de tweede kolom.
     * **Divide (/):** Deelt de waarde van de eerste kolom door de tweede kolom.
4. **Column Name (2nd Column)**
   * **Beschrijving:** Geeft de **tweede kolom** op die bij de berekening betrokken is.
   * **Detail:** Er wordt een lijst van alle beschikbare **kolommen** geboden om uit te selecteren.
5. **Column Name (Dependency)**
   * **Beschrijving:** Geeft de **afhankelijkheidskolom** op waarop het regex-patroon wordt toegepast.
   * **Detail:** Er wordt een lijst van alle beschikbare **kolommen** geboden voor patroonmatching.
6. **Regex Pattern**
   * **Beschrijving:** Definieert het **regex-patroon** dat wordt gebruikt om met de afhankelijkheidskolom te matchen.
   * **Detail:** Als de waarde in de afhankelijkheidskolom overeenkomt met het regex-patroon, wordt de berekening uitgevoerd.
7. **Result Column**
   * **Beschrijving:** Geeft de **resultaatkolom** op waarin het berekeningsresultaat wordt opgeslagen.
   * **Detail:** Dit kan een nieuwe of bestaande kolom zijn waarin de berekende waarde wordt opgeslagen.

## **Functionaliteit:**

* **Voorwaarde-evaluatie:**
  * De kaart voert de actie alleen uit als zowel de **"Where"**- als de **"And"**-secties als true worden geëvalueerd.
  * De kaart voert de actie alleen uit als de waarde in de afhankelijkheidskolom overeenkomt met het opgegeven **regex-patroon**.
* **Kolomberekening:**\
  Als het regex-patroon overeenkomt, voert de kaart de geselecteerde wiskundige bewerking uit tussen de twee gekozen kolommen.
* **Resultaatopslag:**\
  Het resultaat van de berekening wordt opgeslagen in de geselecteerde **resultaatkolom**.

## **Opzet en configuratie:**

* **Tabel selecteren:**\
  Kies de **tabel** waarin de kolommen worden berekend.
* **Kolommen kiezen:**\
  Selecteer de **eerste kolom** en **tweede kolom** die in de berekening worden gebruikt.
* **Bewerking selecteren:**\
  Kies de wiskundige bewerking (**Add (+)**, **Subtract (-)**, **Multiply (\*)**, **Divide (/)**) die tussen de kolommen wordt toegepast.
* **Afhankelijkheidskolom selecteren:**\
  Kies de **afhankelijkheidskolom** waarop het regex-patroon wordt toegepast.
* **Regex-patroon definiëren:**\
  Voer het **regex-patroon** in waarmee de afhankelijkheidskolom moet overeenkomen.
* **Resultaatkolom selecteren:**\
  Kies de **resultaatkolom** waarin de berekende waarde wordt opgeslagen.

## **Conclusie:**

De workflow-kaart **"Calculate with Regex Dependency"** biedt een krachtige manier om berekeningen met voorwaardelijke logica uit te voeren op basis van een regex-patroon. Dit zorgt ervoor dat alleen rijen waarin de afhankelijkheidskolom overeenkomt met het opgegeven patroon de opgegeven berekening ondergaan, en dat het resultaat in de gekozen resultaatkolom wordt opgeslagen.
