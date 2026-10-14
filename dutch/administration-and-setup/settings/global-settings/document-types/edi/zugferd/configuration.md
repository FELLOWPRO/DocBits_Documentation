# ZUGFeRD-configuratie

{% embed url="https://youtu.be/AxrHNEmmXtg" %}
DocBits E-Invoice Tutorial: Process XRechnung / ZUGFeRD (Factur-X), Validate Data & Automate Workflows
{% endembed %}

## **Ondersteunde versies van ZUGFeRD**

DocBits ondersteunt alle belangrijke versies van ZUGFeRD, waaronder:

* **1.0**
* **2.0**
* **2.1** (voldoet aan FACTUR-X 1.0.05)
* **2.2**
* **2.3** (voldoet aan FACTUR-X 1.07.2)
* **2.3.2**

#### Standaardactivering en wijziging

De ZUGFeRD-standaard is standaard altijd actief, maar u kunt er indien nodig wijzigingen in aanbrengen.

### **Stappen om ZUGFeRD-instellingen te wijzigen:**

1. Navigeer naar **Settings → Global Settings → Document Types → Invoice**.
2. Klik op **E-Doc**.\\
3. Er verschijnt een lijst met alle beschikbare e-docs.
4. Zoek de **ZUGFeRD**-versie die u wilt wijzigen.\\

## **Configuratie van transformatie en XML-pad:**

In de **transformatie-instellingen** kunt u het pad definiëren waarmee specifieke informatie in het XML-bestand wordt gevonden en in een nieuwe structuur wordt opgeslagen, zodat de gegevens gemakkelijker toegankelijk zijn.\
<mark style="color:red;">**Opmerking**</mark>: Als u deze functionaliteit gebruikt, moet u in de **Preview** en het **Extraction Path** de nieuw aangemaakte XML-paden gebruiken, niet de oorspronkelijke XML-paden.

### **Stappen om het transformatiebestand te wijzigen:**

1. Open de **Transformation**.
2. Maak een nieuw concept aan door op het **potloodpictogram** te klikken.
3. Selecteer het nieuw aangemaakte concept.
4. Maak een nieuw veld aan of wijzig een bestaand veld.
5. Stel het gewenste pad voor gegevensextractie in.
6. Klik op **Save**.

### Belangrijke opmerkingen:

* Het **preview-bestand** wordt alleen gebruikt voor **FACTUR-X** en niet voor **ZUGFeRD**. ZUGFeRD gebruikt de oorspronkelijke **PDF**.

## Configuratie van de preview-PDF

De **Preview PDF Configuration** wordt gebruikt om een voor gebruikers leesbare versie van het document te genereren. U kunt deze met HTML aanpassen aan uw wensen.

### **Stappen om het preview-bestand te wijzigen:**

1. Open de **Preview**.
2. Maak een nieuw concept aan door op het **potloodpictogram** te klikken.
3. Selecteer het nieuw aangemaakte concept.
4. Maak een nieuw veld aan of wijzig een bestaand veld.
5. Stel het gewenste pad voor gegevensextractie in.
6. Klik op **Save**.

## Configuratie van extractiepaden

De **Extraction Paths Configuration** wordt gebruikt om gegevens te extraheren en velden op het **validatiescherm** te vullen, zoals de factuurtabel of velden die in de factuurlay-out zijn geconfigureerd.

### **Stappen om** **extractiepaden** **te wijzigen**:

1. Open de **Extraction Paths**.
2. Maak een nieuw concept aan door op het **potloodpictogram** te klikken.
3. Selecteer het nieuw aangemaakte concept.
4. Maak een nieuw veld aan of wijzig een bestaand veld.
5. De linkerkant vertegenwoordigt de **DocBits-veld-ID**, die u kunt vinden onder **Settings → Global Settings → Document Types → Invoice → Fields**.\\
6. De rechterkant vertegenwoordigt het **pad naar het veld** dat in de Transformation is aangemaakt.
7. Klik op **Save**.

Door deze stappen te volgen, zorgt u voor nauwkeurige gegevensextractie en -validatie voor ZUGFeRD-facturen.
