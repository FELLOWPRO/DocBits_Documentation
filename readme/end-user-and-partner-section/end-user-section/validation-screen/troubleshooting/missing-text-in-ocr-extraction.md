# Ontbrekend Tekst in OCR Extractie

## **Probleem**

In sommige gevallen kan het lijken alsof tekst ontbreekt in de **OCR-weergave**, wat voorkomt dat deze kan worden geëxtraheerd met behulp van de extractiefunctie.

<figure><img src="../../../../.gitbook/assets/s150-troubleshooting_ocr_5-nl.png" alt="Velden van een fictieve factuur controleren."><figcaption><p>Velden van een fictieve factuur controleren.</p></figcaption></figure>

Om dit te verifiëren, klik op de knop **OCR-weergave** in de werkbalk aan de rechterkant. Als de tekst daar niet verschijnt, betekent dit dat deze niet beschikbaar is voor extractie.

<figure><img src="../../../../.gitbook/assets/s150-troubleshooting_ocr_6-nl.png" alt="OCR-weergave van herkende tekst op de fictieve factuur."><figcaption><p>OCR-weergave van herkende tekst op de fictieve factuur.</p></figcaption></figure>

## **Oorzaak**

De meest waarschijnlijke oorzaak is dat de tekst die je probeert te extraheren deel uitmaakt van een afbeelding (bijv. een logo of gescande sectie) binnen het document.\
Wanneer de E-tekst functie is ingeschakeld, wordt tekst die op afbeeldingen of logo's verschijnt niet opgenomen in de geëxtraheerde tekstlaag. Als gevolg hiervan kan deze tekst niet worden benaderd of geëxtraheerd via de standaard extractielogica.

## **Oplossing**

Om dit probleem op te lossen, schakel je de functie E-tekst uit—ofwel voor de [specifieke leverancier](missing-text-in-ocr-extraction.md#e-tekst-uitschakelen-voor-een-specifieke-leverancier) of voor de [hele organisatie](missing-text-in-ocr-extraction.md#e-tekst-uitschakelen-voor-de-hele-organisatie). Zodra E-tekst is gedeactiveerd, zal DocBits uitsluitend op OCR vertrouwen, dat in staat is om tekst uit afbeeldingen en logo's binnen het document te extraheren.

### **E-tekst Uitschakelen voor een Specifieke Leverancier**

1. Open een document van de specifieke leverancier in de **Veldvalidatie**.
2.  Klik op het menu met drie stippen in de werkbalk aan de rechterkant.

<figure><img src="../../../../.gitbook/assets/s150-troubleshooting_ocr_2-nl.png" alt="Menu met extra opties bij veldvalidatie."><figcaption><p>Menu met extra opties bij veldvalidatie.</p></figcaption></figure>

3.  Vink **Gebruik E-tekst indien beschikbaar** uit.

<figure><img src="../../../../.gitbook/assets/s150-troubleshooting_ocr_3-nl.png" alt="Optie voor elektronische tekst in het documentmenu."><figcaption><p>Optie voor elektronische tekst in het documentmenu.</p></figcaption></figure>

4.  Klik op **Toevoegen** om de verwerking voor het document opnieuw te starten.

<figure><img src="../../../../.gitbook/assets/s150-troubleshooting_ocr_4-nl.png" alt="Bevestiging vóór wijziging van het gebruik van elektronische tekst."><figcaption><p>Bevestiging vóór wijziging van het gebruik van elektronische tekst.</p></figcaption></figure>

### E-tekst Uitschakelen voor de Hele Organisatie

1.  Ga naar **Instellingen → Documentverwerking → OCR-instellingen**.

<figure><img src="../../../../.gitbook/assets/s150-settings_ocr-nl.png" alt="OCR-instellingen in de Nederlandstalige interface."><figcaption><p>OCR-instellingen in de Nederlandstalige interface.</p></figcaption></figure>

2.  Onder **Algemene OCR-instellingen**, vink de optie **Gebruik E-tekst indien beschikbaar** uit.

<figure><img src="../../../../.gitbook/assets/s150-troubleshooting_ocr_1-nl.png" alt="Algemene OCR-instellingen met de optie voor elektronische tekst."><figcaption><p>Algemene OCR-instellingen met de optie voor elektronische tekst.</p></figcaption></figure>

De afbeeldingen gebruiken een fictieve factuur met beschikbare OCR-tekst. Ze tonen interfacecontroles, geen gereproduceerd incident met ontbrekende tekst.
