# Barcodetoewijzing

### Overzicht

De instelling **Barcodetoewijzing** (Barcode Assignment) laat DocBits **barcodes in een bestand gebruiken om het in afzonderlijke documenten te scheiden**. Dit is handig wanneer meerdere documenten samen in één grote PDF worden gescand en een barcode aangeeft waar het ene document eindigt en het volgende begint.

Deze instelling is **standaard uitgeschakeld**.

### Wat doet het?

Wanneer deze instelling is ingeschakeld, zoekt DocBits naar barcodes in een binnenkomend bestand met meerdere pagina's en splitst het op de gemarkeerde posities in afzonderlijke documenten. Elk resulterend document wordt vervolgens afzonderlijk verwerkt.

* **Ingeschakeld** — DocBits detecteert barcodes en scheidt een gecombineerd bestand automatisch op basis daarvan in afzonderlijke documenten.
* **Uitgeschakeld** — Het bestand wordt als één document verwerkt; barcodes worden niet gebruikt om het te splitsen.

{% hint style="info" %}
Dit gaat over het **splitsen en toewijzen** van pagina's op basis van barcodes. Het uitlezen van de in een barcode gecodeerde gegevens (bijvoorbeeld voor betalings-QR-codes) wordt apart afgehandeld onder **Bar-Code / QR Code Extraction**.
{% endhint %}

### Voordelen

* **Sneller batchscannen**: Scan een hele stapel documenten in één keer, gescheiden door barcodevellen, in plaats van elk document afzonderlijk te scannen.
* **Minder handmatig sorteren**: DocBits maakt de afzonderlijke documenten voor u, zodat niemand de PDF met de hand hoeft te splitsen.
* **Minder fouten**: Documenten worden elke keer precies op de gemarkeerde posities gescheiden.

### Hoe te gebruiken

1. Ga naar **Instellingen**.
2. Selecteer **Documentverwerking**.
3. Selecteer **Module**.
4. Open de sectie **Documenttype**.
5. Zoek **Barcodetoewijzing** en zet de schakelaar aan.

### Wanneer deze functie gebruiken

* **Scannen met groot volume**: Wanneer u veel documenten samen scant en er barcodescheidingsvellen tussen gebruikt.
* **Gemengde batches**: Wanneer één binnenkomend bestand meerdere verschillende documenten bevat die afzonderlijk moeten worden verwerkt.
* **Laat uitgeschakeld** als uw documenten altijd als afzonderlijke bestanden binnenkomen — splitsen is dan niet nodig.
