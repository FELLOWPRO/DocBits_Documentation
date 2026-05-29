# Barcodetoewijzing

### Overzicht

De instelling **Barcodetoewijzing** (Barcode Assignment) voegt een barcodehulpmiddel toe aan het **validatiescherm voor documenten**. Het leest de barcodes en QR-codes die in een document worden gevonden en laat u **hun waarden aan de velden van het document toewijzen** — bijvoorbeeld een referentie-, order- of pakbonnummer uit een barcode invullen in plaats van het te typen.

Deze instelling is **standaard uitgeschakeld**.

### Wat doet het?

Wanneer deze instelling is ingeschakeld, verschijnt er tijdens het valideren van een document een kleine **barcodeknop** (een QR-code-pictogram) in de werkbalk. Als u erop klikt, worden de barcodes getoond die DocBits in het document heeft gevonden, en kunt u elke barcode aan een veld koppelen. Het veld wordt dan gevuld met de uit de barcode gelezen waarde.

* **Ingeschakeld** — De barcodeknop wordt getoond op het validatiescherm. U kunt de barcodes in het document uitlezen en hun waarden aan velden toewijzen.
* **Uitgeschakeld** — De knop is verborgen en barcodewaarden worden tijdens de validatie niet aangeboden voor toewijzing.

{% hint style="info" %}
**Dit is bedoeld om een barcode-/QR-waarde uit te lezen en deze tijdens de validatie aan een veld toe te wijzen.** Het automatisch extraheren van gestructureerde gegevens uit betaalcodes (zoals Swiss QR Bill of GiroCode) — en het splitsen van een bestand met meerdere pagina's bij barcodescheidingspagina's — worden afgehandeld door een **andere** instelling: [Bar-Code / QR Code Extraction](bar-code-qr-code-extraction/README.md).
{% endhint %}

### Voordelen

* **Snellere, foutloze invoer**: Neem waarden rechtstreeks uit een barcode over in plaats van ze met de hand te lezen en te typen.
* **Minder typefouten**: Een gescande waarde is precies wat er in de barcode is gecodeerd.
* **U houdt de controle**: U bepaalt tijdens de validatie welke barcode in welk veld komt.

### Hoe te gebruiken

1. Ga naar **Instellingen**.
2. Selecteer **Documentverwerking**.
3. Selecteer **Module**.
4. Open de sectie **Documenttype**.
5. Zoek **Barcodetoewijzing** en zet de schakelaar aan.
6. Klik daarna tijdens het valideren van een document op de **barcodeknop** in de werkbalk en wijs de gedetecteerde barcodewaarden toe aan de bijbehorende velden.

### Wanneer deze functie gebruiken

* **Documenten met barcodes**: Wanneer uw documenten barcodes/QR-codes bevatten waarvan de waarden in specifieke velden horen (bijv. order- of referentienummers).
* **Handmatige validatieworkflows**: Wanneer iemand documenten controleert en velden snel uit barcodes wil vullen.
* **Laat uitgeschakeld** als uw documenten geen bruikbare barcodes hebben, of als u alleen de automatische barcode-/QR-**extractie** nodig hebt — zie [Bar-Code / QR Code Extraction](bar-code-qr-code-extraction/README.md).
