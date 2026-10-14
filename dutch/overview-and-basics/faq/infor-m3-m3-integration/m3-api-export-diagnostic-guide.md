# M3 API Export Diagnostic Guide

### 1. Initiële Setup

Voordat u begint met het oplossen van problemen, zorg ervoor dat u bekend bent met de verwachte invoer voor het M3-eindpunt waaraan u werkt.

#### 1.1 Toegang tot M3 API-documentatie

* Log in op **M3**.
* Ga naar **API-sectie → API-documentatie**.
* Zoek en selecteer het relevante eindpunt (bijv. `APS450MI` voor factuurgerelateerde exports).
* Kies de juiste functie (bijv. `Toevoegen`).

#### 1.2 Begrijp API-vereisten

* Bekijk alle **vereiste velden** in de API-documentatie.
* Let op belangrijke velden zoals:
  * `DIVI`
  * `ACDT` (boekingsdatum)
  * `CUCD` (valutacode)
  * `SINO` (leveranciersfactuurnummer)
* Bevestig veld **gegevenstypen**, **hoofdlettergebruik** en **opmaakregels** (bijv. `JJJJ-MM-DD` voor datums).

### 2. Testen van API-oproepen rechtstreeks in M3

Deze stap verifieert dat de M3 API zich gedraagt zoals verwacht met behulp van handmatige invoer.

#### 2.1 Genereer een testverzoek in M3

* In de M3 API-documentatietool:
  * Vul testgegevens in voor vereiste velden.
  * Klik op **Uitvoeren** om het verzoek uit te voeren.
  * Kopieer de resulterende **cURL** en **JSON-body**.

#### 2.2 Debuggen met behulp van Postman

* Open **Postman** en maak een nieuw **POST**-verzoek.
* Plak de JSON-body of cURL.
* Voeg de benodigde headers toe (bijv. autorisatie).
* Klik op **Verzenden** en observeer het resultaat:
  * `200 OK`: Het verzoek was succesvol.
  * Fout: Bekijk het bericht voor details over wat er misging.

### 3. Vergelijken van M3 API met DocBits-mapping

Nadat u heeft bevestigd dat de API werkt met testgegevens, vergelijk deze met wat DocBits daadwerkelijk verzendt.

#### 3.1 Exporteer voorbeeldgegevens van DocBits

*   Open de **DocBits API-documentatie**:

    Gebruik het eindpunt **/export/get\_infor\_export\_api\_json**.
* Voer het **Document-ID** in van een problematisch document.
* Voer de export uit om de **JSON-payload** te bekijken die DocBits naar M3 zal sturen.

#### 3.2 Vergelijk API-payloads

* Plaats de **M3 test JSON** en de **DocBits export JSON** naast elkaar.
* Controleer op:
  * **Veldnamen**: Zorg ervoor dat namen _exact_ overeenkomen, inclusief hoofdlettergebruik (`DIVI` ≠ `divi`).
  * **Gegevenstypen**: Controleer of strings, getallen en datums correct zijn opgemaakt.
  * **Ontbrekende velden**: Identificeer eventuele velden aanwezig in het verzoek van M3 maar ontbrekend in DocBits.

### 4. Problemen oplossen van veelvoorkomende problemen

| Probleem                                           | Waarschijnlijke oorzaak                    | Oplossing                                                                 |
| -------------------------------------------------- | ------------------------------------------ | ------------------------------------------------------------------------- |
| Ontbrekende veldfout                               | Een vereist veld is niet gemapt in DocBits | Voeg het ontbrekende veld toe in de DocBits exportconfiguratie.           |
| Hoofdlettergebruik veld komt niet overeen (`DIVI`) | M3 is hoofdlettergevoelig                  | Gebruik de juiste hoofdlettergebruik in de veldtoewijzing.                |
| Ongeldige `accountingDate`-indeling                | Verkeerde of ontbrekende datum             | Pas aan naar de verwachte indeling door M3 (bijv. `JJJJ-MM-DD`).          |
| Onverwachte API-fout                               | Extra of niet-herkende velden              | Vergelijk met bekende werkende payloads en maak onnodige gegevens schoon. |

### 5. Als problemen aanhouden

Als het probleem niet is opgelost na het volgen van de bovenstaande stappen:

1. **Documenteer** het probleem:
   * Foutmelding en statuscode
   * Voorbeeld M3-verzoek en DocBits export JSON
2. **Vat samen** uw probleemoplossing:
   * Wat u heeft geprobeerd
   * Belangrijkste verschillen waargenomen tussen test- en mislukte payloads
3. **Schakel hulp in van** een ontwikkelaar:
   * Inclusief alle gegevens en bevindingen
   * Markeer vermoedelijke probleemgebieden
