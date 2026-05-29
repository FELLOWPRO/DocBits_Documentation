# Hybride PDF-XML-extractie overslaan

### Overzicht

De instelling **Hybride PDF-XML-extractie overslaan** (Skip Hybrid PDF XML Extraction) bepaalt hoe DocBits **hybride PDF's** verwerkt — PDF-facturen met een ingebedde gestructureerde e-factuur (ZUGFeRD / Factur-X). Ze beslist of de **gestructureerde XML in de PDF** het leidende document voor de automatische verwerking is, of dat de **PDF zelf** via OCR als primair document wordt verwerkt.

Deze instelling is vooral relevant voor **klanten in de VS**. Anders dan in de EU/Duitsland kent de Verenigde Staten geen algemene B2B-verplichting voor e-facturatie, dus VS-organisaties willen de PDF doorgaans als de primaire, voor mensen leesbare factuur behandelen — ook wanneer een tegenpartij een ZUGFeRD/Factur-X-bestand met ingebedde XML stuurt.

### Wat doet het?

Een ZUGFeRD/Factur-X-bestand is één PDF die ook een machineleesbare XML-factuur bevat. Standaard detecteert DocBits die ingebedde XML en gebruikt deze als leidende bron voor de extractie (gestructureerd elektronisch pad).

* **Uitgeschakeld (standaard)** — DocBits detecteert de ingebedde e-factuur-XML en verwerkt het document via het **gestructureerde elektronische pad**. De XML is de leidende factuur. Dit is het juridisch correcte gedrag voor de EU/Duitsland, waar de gestructureerde e-factuur de relevante factuur is en de PDF slechts een visualisatie / leeskopie.
* **Ingeschakeld** — DocBits **negeert de ingebedde XML** en stuurt het document naar de **PDF-processor (OCR)**. De PDF wordt het primaire verwerkingsdocument. Dit is de gebruikelijke keuze voor **VS-organisaties** die PDF-first-verwerking willen.

{% hint style="info" %}
Deze instelling heeft alleen invloed op **hybride PDF's** (ZUGFeRD / Factur-X = een `.pdf` met ingebedde XML). Een puur XRechnung/EDI-bestand dat als `.xml` wordt geüpload, wordt altijd via het gestructureerde elektronische pad verwerkt — er is geen PDF die het primaire document kan worden.
{% endhint %}

### Audit & compliance — het origineel blijft altijd behouden

Het inschakelen van deze instelling **verwijdert de e-factuur niet**. Het oorspronkelijke artefact blijft altijd behouden:

* De oorspronkelijke ZUGFeRD/Factur-X-**PDF — inclusief de ingebedde XML — blijft opgeslagen** en downloadbaar. Er wordt niets verwijderd uit de opgeslagen kopie van het document.
* De verwerking verandert alleen **welke inhoud de extractie aandrijft** (PDF/OCR versus ingebedde XML), niet wat er wordt gearchiveerd.

Zo kan een VS-organisatie de PDF als primair verwerken terwijl de gestructureerde e-factuur beschikbaar blijft voor audit.

{% hint style="warning" %}
Laat deze instelling voor EU/Duitse organisaties **uitgeschakeld**. Volgens de e-facturatieregels van 2025 is een gestructureerde e-factuur (ZUGFeRD/Factur-X, XRechnung) de juridisch relevante factuur; een gewone PDF is slechts een leeskopie. De PDF als primair verwerken in plaats van de gestructureerde gegevens is niet passend wanneer er een geldige e-factuur aanwezig is.
{% endhint %}

### Hoe te gebruiken

1. **De instelling openen**:
   * Ga naar **Instellingen**.
   * Selecteer **Documentverwerking**.
   * Selecteer **Module**.
   * Open de sectie **Documenttype**.
   * Zoek **Hybride PDF-XML-extractie overslaan** en zet de schakelaar aan.
2. **De modus kiezen**:
   * **VS- / PDF-first-organisaties** → schakel in zodat ZUGFeRD/Factur-X-PDF's via OCR als primair document worden verwerkt.
   * **EU/Duitse organisaties** → laat uitgeschakeld zodat de gestructureerde e-factuur het leidende document blijft.
3. **Verifiëren**:
   * Upload een ZUGFeRD/Factur-X-PDF en controleer het verwerkingsresultaat — met de schakelaar aan wordt het als een gewone PDF (OCR) behandeld; met de schakelaar uit worden de ingebedde e-factuurgegevens geëxtraheerd.

### Wanneer deze functie gebruiken

* **VS-klanten / geen e-factuurverplichting**: schakel in zodat de vertrouwde PDF het primaire verwerkingsdocument is terwijl de ingebedde e-factuur gearchiveerd blijft.
* **Gemengde/PDF-first-workflows**: schakel in wanneer downstream-processen, validatie of beoordeling afhankelijk zijn van de PDF-lay-out in plaats van de XML.
* **EU/Duitse compliance**: laat uitgeschakeld zodat gestructureerde e-factuurgegevens de verwerking aandrijven, zoals vereist.
