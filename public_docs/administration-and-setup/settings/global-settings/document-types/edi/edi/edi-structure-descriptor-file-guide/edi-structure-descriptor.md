# EDI Structuur beschrijving

Het primaire doel van de structuur beschrijving is om de elementen van een EDI-bericht op een logische en georganiseerde manier te schetsen, waardoor het gemakkelijker wordt om de gegevens te beheren en te parseren. Door nauwkeurig de hiërarchie van het bericht weer te geven.

### Elementen van de structuur beschrijving

**N1** – Bevat de volgende velden:

* **N1** – Naam of Identificatie van de entiteit (bijv., partij, organisatie).
* **N2** – Aanvullende naam informatie (meestal een secundaire naam voor de entiteit).
* **N3** – Adresinformatie (meestal het straatadres).
* **N4** – Geografische locatie (stad, staat, postcode, land).

**N9** – Bevat het volgende veld:

* **N9** – Referentie identificatie (bijv., inkoopordernummer of controle nummer).
* **Loops:**
  * **MSG01** – Bevat het volgende veld:
    * **MSG01** – Vrije tekstbericht (meestal een opmerking of speciale instructie met betrekking tot de transactie).

**IT1** – Bevat de volgende velden:

* **IT1** – Regelitem identificatie (bijv., artikelnummer of productcode).
* **QTY** – Hoeveelheid van het item in de transactie (bijv., bestelde of verzonden eenheden).
* **TXI** – Belastinginformatie (bijv., belastingtarieven, bedragen of classificaties voor het item).
* **REF** – Referentie informatie (bijv., lotnummer, serienummer of andere identificatoren met betrekking tot het item).
* **Loops:**
  * **SAC** – Kan herhaald worden en bevat de volgende velden:
    * **SAC** – Service, promotie, toelage of kosteninformatie (bijv., extra kosten of kortingen met betrekking tot het item).
    * **TXI** – Belastinginformatie met betrekking tot SAC (bijv., belastingen op kosten of toelagen).

**SAC** – Bevat de volgende velden:

* **SAC** – Service, promotie, toelage of kosteninformatie (kan onafhankelijk worden gebruikt of binnen de IT1-loop om extra kosten/kortingen te vertegenwoordigen).
* **TXI** – Belastinginformatie met betrekking tot SAC (bijv., belastingen op kosten of toelagen).

### Hier is het volledige voorbeeld van een structuur beschrijving in een JSON-formaat:

```
{
    "N1": {
        "fields": [
            "N1",  
            "N2",   
            "N3",   
            "N4"    
        ]
    },
    "N9": {
        "fields": [
            "N9"    
        ],
        "loops": {
            "MSG01": {
                "fields": [
                    "MSG01"   
            }
        }
    },
    "IT1": {
        "fields": [
            "IT1",   
            "QTY",   
            "TXI",   
            "REF"    
        "loops": {
            "SAC": {
                "fields": [
                    "SAC",   
                    "TXI"    
        }
    },
    "SAC": {
        "fields": [
            "SAC",   
            "TXI"    
        ]
    }
}
```
