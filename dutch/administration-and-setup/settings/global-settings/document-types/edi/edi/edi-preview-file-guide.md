# EDI Voorbeeldbestand Gids

## 1. Overzicht

Het **Voorbeeldbestand** bepaalt hoe gestructureerde XML-gegevens worden weergegeven in een menselijk leesbaar, op PDF lijkend formaat. Het combineert **HTML en CSS** voor visuele presentatie en gebruikt **XSLT** `**select**` **statements** om dynamisch gegevens in te voegen vanuit de aangepaste XML. Dit voorbeeld wordt weergegeven tijdens **veldvalidatie** en wordt ook opgenomen wanneer documenten worden geëxporteerd naar **IDM**.

## 2. Doel en Functie

* Converteert machineleesbare aangepaste XML naar een visueel opgemaakt voorbeeld (PDF).
* Maakt mensvriendelijke beoordeling en validatie van geëxtraheerde gegevens mogelijk.
* Zorgt voor consistente weergave van belangrijke documentvelden zoals koppen, tabellen, totalen, enz.
* Gebouwd met behulp van **HTML + CSS** voor lay-out en ontwerp, en **XSLT** voor het binden van gegevens aan de lay-out.

## 3. Toegang & Basisbewerking

#### **Toegang tot het bestand:**

1.  Ga naar **Instellingen** → **Documenttype** → _\[Uw Document (bijv. Inkooporder)]_ → **E-Doc**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Ff6zyL0AvmqSvrogZdnox%252Fimage.png%3Falt%3Dmedia%26token%3D6bc9ab55-6ee9-43d1-b576-4c5833c208cf\&width=768\&dpr=4\&quality=100\&sign=a23de442\&sv=2)
2. Onder het tabblad **E-Doc**, selecteer uw formaat (bijv. **EDI**).
3.  Klik op **Voorbeeld** om het bestand te bekijken of te bewerken.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fdo1R389GeSqFuZKLD0OP%252Fimage.png%3Falt%3Dmedia%26token%3D930903d4-44af-4188-b015-c60c2dd9d9ab\&width=768\&dpr=4\&quality=100\&sign=77bbb2ce\&sv=2)

#### **Conceptbeheer:**

* **Maak een Concept:** Klik op het ✏️ potloodpictogram.
* **Verwijder Concepten:** Gebruik het 🗑️ prullenbakpictogram om ongebruikte concepten te verwijderen.
* **Wijzigingen Activeren:** Klik op het ✅ vinkje om een versie te publiceren.
  * **Opmerking**: Het activeren van een nieuwe versie zal de vorige versie **automatisch deactiveren**.

## 4. HTML/XSLT/CSS Editor

Het **Voorbeeldbestand** wordt bewerkt in een speciale editor die HTML, XSLT en CSS ondersteunt.

* **HTML** definieert de structuur van het uitvoerdocument (bijv. tabellen, divs, lay-out).
* **CSS** controleert de opmaak (bijv. lettertypen, afstand, kleuren, uitlijning).
*   **XSLT** `**select**` **statements** worden gebruikt om velden dynamisch in te vullen vanuit de aangepaste XML, zoals:

    Copy

    ```
    <xsl:value-of select="/PURCHASE_ORDER/PURCHASE_ORDER_NUMBER/text()" />
    ```
* U kunt ook **XSLT-logica** gebruiken (`<xsl:if>`, `<xsl:for-each>`, enz.) om conditionele weergave te behandelen of over regelitems te itereren.

## 5. Voorbeeldfunctie (Uitvoer Renderen)

De Voorbeeldfunctie stelt u in staat te testen en te verifiëren hoe een EDI-document wordt weergegeven met het huidige Voorbeeldbestand.

#### **Gebruik:**

* Upload een EDI-bestand via het standaard uploadproces.
* Kopieer de **Document-ID** van het geüploade bestand.
* Navigeer naar de **Voorbeeld** interface.
* Open de **Voorbeeldfunctie**.\
  \
  &#x20;![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F9lddYJl2G4tzpdr9RD5F%252Fimage.png%3Falt%3Dmedia%26token%3Df7663f70-ef10-4e64-bbdc-41048ed8352a\&width=300\&dpr=4\&quality=100\&sign=36ce2b93\&sv=2)
* Voer de Document-ID in en klik op **Test**.
* Het weergegeven PDF-stijl voorbeeld zal worden getoond met behulp van de HTML/CSS/XSLT-configuratie.

Deze functie is cruciaal voor het debuggen van gegevensbindings, het verfijnen van de lay-out en het zorgen dat het document zowel nauwkeurig als visueel duidelijk is voor gebruikers en downstream systemen zoals **IDM**.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FJH103tnbqZjuimpOniVg%252Fimage.png%3Falt%3Dmedia%26token%3D4e63cc09-b0de-488f-bdd0-ee5a9246a371\&width=768\&dpr=4\&quality=100\&sign=bfff5bba\&sv=2)

## 6. Video Walkthrough

Een videogids voor dit bestandstype is beschikbaar op de [Videopagina.](https://docs.docbits.com/administration-and-setup/settings/global-settings/document-types/edi/edi/edi-videos) Gebruik het om stap voor stap de installatie, bewerking en voorbeeldweergave te volgen.
