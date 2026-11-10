# Gids voor het EDI Structure Descriptor-bestand

## 1. Overzicht

Het **Structure Descriptor**-bestand is een **JSON**-bestand dat bepaalt hoe terugkerende EDI-segmenten (bijvoorbeeld `N1`–`N4`) worden gegroepeerd tot gestructureerde uitvoer. Het is de eerste stap in de EDI-verwerking:

* **Nauwkeurig parsen** van samenhangende segmenten als afzonderlijke eenheden.
* **Consistente uitvoer** voor de [Transformation](../edi-transformation-file-guide.md) en stroomafwaartse systemen.

_Voor een volledig voorbeeld met segmendetails, zie_ [_Structure Descriptor Example_](edi-structure-descriptor.md)_._

## 2. Toegang en basisbewerking

#### **Het bestand openen**

1. Ga naar **Settings** → **Document Types** en open **E-Doc** voor het documenttype dat u wilt configureren (bijvoorbeeld _Purchase Order_). U hebt beheerdersrechten nodig binnen uw organisatie om deze bestanden te bewerken.

    <!-- dbdc-139-edi-sd-list-en.png --><figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/dbdc-139-edi-sd-list-en.png" alt="Engelstalige Sandbox E-Doc-pagina met het uitgeklapte EDI-formaat en de rij STRUCTURE DESCRIPTOR JSON boven TRANSFORMATION, PREVIEW en EXTRACTION PATHS"><figcaption>Open E-Doc voor uw documenttype; het EDI-formaat vermeldt de bijbehorende configuratiebestanden.</figcaption></figure>

2. Klap het formaat **EDI** uit. De configuratiebestanden worden samen vermeld: **STRUCTURE DESCRIPTOR**, **TRANSFORMATION**, **PREVIEW** en **EXTRACTION PATHS**.
3. Klik op de rij **STRUCTURE DESCRIPTOR**, herkenbaar aan **JSON**, om het bestand te openen.

#### **Concepten beheren**

De linkerkolom toont de lijst met **Version** van het bestand. De versie die als **Active** is gemarkeerd, is de versie die DocBits gebruikt.

* **Een concept aanmaken**: klik op het ✏️ potloodpictogram naast de actieve versie om te beginnen met bewerken. Het actieve bestand zelf kan niet rechtstreeks worden bewerkt.
* **Concepten verwijderen**: gebruik het 🗑️ prullenbakpictogram om ongebruikte concepten te verwijderen.
* **Wijzigingen activeren**: klik op het ✅ vinkje-pictogram bij een concept om uw wijzigingen goed te keuren en te publiceren.
  * <mark style="color:red;">**Note**</mark>: het activeren van een nieuwe versie **deactiveert automatisch** de vorige versie.

<!-- dbdc-139-edi-sd-detail-en.png --><figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/dbdc-139-edi-sd-detail-en.png" alt="Engelstalige Sandbox-editor voor Structure Descriptor JSON met links de versielijst waarin versie 1 als Active staat en een potloodpictogram om een concept aan te maken"><figcaption>Het Structure Descriptor-bestand met de versielijst; met het potlood maakt u een concept aan dat u kunt bewerken.</figcaption></figure>

## 3. Preview-functie (geparseerde uitvoer bekijken)

Met de **Preview-functie** test u hoe een geüpload EDI-bestand wordt geparseerd met de Structure Descriptor die op dat moment wordt getoond, nog voordat u een wijziging activeert.

#### Gebruik

* Upload een EDI-bestand via de gebruikelijke uploadprocedure.
* Kopieer de **Document ID** van het geüploade bestand.
* Open het bestand **Structure Descriptor** zoals hierboven beschreven.
* Klik rechtsboven op **Preview** om het testpaneel te openen.

    <div align="left"><!-- dbdc-139-edi-sd-preview-en.png --><figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/dbdc-139-edi-sd-preview-en.png" alt="Engelstalige Sandbox-pagina van Structure Descriptor met het geopende Preview-testpaneel, met het invoerveld Document Id en de knop Test" width="560"><figcaption>Het testpaneel: voer een Document ID in en klik op Test.</figcaption></figure></div>

* Voer de **Document ID** in het veld in en klik op **Test**.
* De resulterende **gestructureerde uitvoer** wordt naast de editor weergegeven.

Dit is vooral handig om mappings te debuggen en structuurgroeperingen in realtime te valideren. U hebt een representatief EDI-document van uw eigen formaat nodig; het getoonde resultaat is afhankelijk van het geüploade bestand.

## 4. Videowalkthrough

Een videohandleiding voor dit bestandstype vindt u op de [pagina Video's.](../edi-videos.md)\
Gebruik deze om de installatie, het bewerken en het bekijken van de Preview stap voor stap te volgen.

De beelden tonen een bestaande configuratie en versie. Instellingen verschillen per documenttype en formaat. Valideer wijzigingen in een concept voordat u ze activeert.
