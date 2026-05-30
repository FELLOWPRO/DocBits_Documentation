# Barcodetoewijzing

### Overzicht

De instelling **Barcodetoewijzing** (Barcode Assignment) voegt een barcodehulpmiddel toe aan het **validatiescherm voor documenten**. Het leest de barcodes en QR-codes die in een document worden gevonden en laat u **hun waarden aan de velden van het document toewijzen** — bijvoorbeeld een order-, referentie- of pakbonnummer uit een barcode invullen in plaats van het te typen.

Deze instelling is **standaard uitgeschakeld**.

### Wat u krijgt als u het inschakelt

Zodra de instelling is ingeschakeld, verschijnt er een nieuwe **barcodeknop** (een QR-code-pictogram) in de werkbalk aan de rechterkant van het **validatiescherm** (`/field_validation_v1/…`). Deze knop is het startpunt van de hele functie — zonder de instelling blijft het pictogram verborgen.

<figure><img src="../../../../.gitbook/assets/barcode_assignment_validation_icon.png" alt="Het barcodepictogram (QR-code) in de validatiewerkbalk"><figcaption><p>Wanneer de instelling is ingeschakeld, verschijnt het barcodepictogram in de validatiewerkbalk.</p></figcaption></figure>

Hier ziet u het pictogram in context op het validatiescherm, naast het document dat wordt gecontroleerd:

<figure><img src="../../../../.gitbook/assets/barcode_assignment_validation_screen.png" alt="Validatiescherm met het barcodepictogram beschikbaar"><figcaption><p>Het validatiescherm — het barcodepictogram (gemarkeerd, rechter werkbalk) wordt alleen getoond wanneer Barcodetoewijzing is ingeschakeld.</p></figcaption></figure>

### Hoe barcodes worden gelezen

DocBits detecteert de barcodes tijdens de documentverwerking en biedt hun gedecodeerde waarden aan voor toewijzing. Eén document kan meerdere barcodetypes bevatten — bijvoorbeeld een **QR-code**, een **Code 128** en een **EAN-13** — die elk een andere waarde coderen, zoals een ordernummer, een factuurnummer of een leveranciers-GLN.

<figure><img src="../../../../.gitbook/assets/barcode_assignment_demo_invoice.png" alt="Demofactuur met meerdere barcodetypes"><figcaption><p>Voorbeeld van een DocBits-demofactuur met drie barcodetypes (QR-code → ordernummer, Code 128 → factuurnummer, EAN-13 → leveranciers-GLN), die elk een waarde coderen die u aan een veld kunt toewijzen.</p></figcaption></figure>

{% hint style="info" %}
Welke barcodetypes worden gedetecteerd, wordt bepaald door de instelling **Bar-Code / QR Code Extraction** (`Barcode Extraction Types`). Als het dialoogvenster *“no barcodes extracted found”* toont, zorg er dan voor dat barcode-extractie is ingeschakeld en dat de verwachte types (bijv. `QRCODE`, `CODE128`, `EAN13`) zijn geselecteerd. Zie [Bar-Code / QR Code Extraction](bar-code-qr-code-extraction/README.md).
{% endhint %}

### Het dialoogvenster Barcodetoewijzing gebruiken

1. Open een document op het **validatiescherm**.
2. Klik op het **barcodepictogram** in de rechter werkbalk.
3. Het dialoogvenster **Barcodetoewijzing** toont elke barcode die DocBits in het document heeft gedetecteerd, weergegeven als `Barcode <n> : <waarde>`.

<figure><img src="../../../../.gitbook/assets/barcode_assignment_dialog.png" alt="Dialoogvenster Barcodetoewijzing met de gedetecteerde barcodes"><figcaption><p>Het dialoogvenster Barcodetoewijzing toont elke gedetecteerde barcode met een vervolgkeuzelijst om het doelveld te kiezen.</p></figcaption></figure>

4. Open voor elke barcode de vervolgkeuzelijst en kies het veld waarin de waarde moet komen.

<figure><img src="../../../../.gitbook/assets/barcode_assignment_field_options.png" alt="Het doelveld kiezen voor een barcode"><figcaption><p>Elke barcode kan aan elk willekeurig documentveld worden toegewezen — bijv. Ordernummer, Factuurnummer, Leveranciers-ID.</p></figcaption></figure>

5. Zodra u een veld selecteert, wordt dat veld gevuld met de waarde van de barcode.

<figure><img src="../../../../.gitbook/assets/barcode_assignment_field_mapped.png" alt="Barcode toegewezen aan het veld Ordernummer"><figcaption><p>Na het selecteren van een veld (hier Ordernummer) wordt het veld gevuld met de barcodewaarde.</p></figcaption></figure>

### Hoe in te schakelen

1. Ga naar **Instellingen**.
2. Selecteer **Documentverwerking**.
3. Selecteer **Module**.
4. Open de sectie **Documenttype**.
5. Zoek **Barcodetoewijzing** en zet de schakelaar aan.

<figure><img src="../../../../.gitbook/assets/barcode_assignment_toggle.png" alt="Schakelaar Barcodetoewijzing"><figcaption><p>De schakelaar Barcodetoewijzing in Instellingen → Documentverwerking → Module.</p></figcaption></figure>

### Voordelen

* **Snellere, foutloze invoer**: Neem waarden rechtstreeks uit een barcode over in plaats van ze met de hand te lezen en te typen.
* **Minder typefouten**: Een gescande waarde is precies wat er in de barcode is gecodeerd.
* **U houdt de controle**: U bepaalt tijdens de validatie welke barcode in welk veld komt.

### Wanneer deze functie gebruiken

* **Documenten met barcodes**: Wanneer uw documenten barcodes/QR-codes bevatten waarvan de waarden in specifieke velden horen (bijv. order- of referentienummers).
* **Handmatige validatieworkflows**: Wanneer iemand documenten controleert en velden snel uit barcodes wil vullen.
* **Laat uitgeschakeld** als uw documenten geen bruikbare barcodes hebben, of als u alleen de automatische barcode-/QR-**extractie** nodig hebt — zie [Bar-Code / QR Code Extraction](bar-code-qr-code-extraction/README.md).

{% hint style="info" %}
**Dit is bedoeld om een barcode-/QR-waarde uit te lezen en deze tijdens de validatie aan een veld toe te wijzen.** Het automatisch extraheren van gestructureerde gegevens uit betaalcodes (zoals Swiss QR Bill of GiroCode) — en het splitsen van een bestand met meerdere pagina's bij barcodescheidingspagina's — worden afgehandeld door een **andere** instelling: [Bar-Code / QR Code Extraction](bar-code-qr-code-extraction/README.md).
{% endhint %}
