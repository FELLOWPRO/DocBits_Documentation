# EDI Transformatiebestand Gids

## 1. Overzicht

Het **Transformatiebestand** bepaalt hoe de gestructureerde XML—gemaakt met behulp van het **Structuur Descriptor Bestand**—wordt omgezet in een aangepast XML-formaat dat overeenkomt met de specifieke documenttype- of formuliereisen van uw organisatie.

Deze transformatie wordt uitgevoerd met behulp van **XSLT (Extensible Stylesheet Language Transformations)**, die kunnen worden gemaakt en onderhouden via de **XSLT Editor** in de DocBits-interface.

## 2. Doel en Functie

* Transformeert de **tussenliggende XML** (output van de Structuur Descriptor) naar een **definitieve XML** die overeenkomt met uw documentenschema.
* Maakt flexibiliteit mogelijk om verschillende EDI-partnerformaten en interne systeemvereisten aan te passen.
* Opgebouwd met **XSLT-regels**, waarmee u mappings, waardeopmaak, voorwaardelijke logica en structuur kunt definiëren.

## 3. Toegang & Basisbewerking

#### Toegang tot het Bestand

1.  Ga naar **Instellingen → Documenttype** → \[Uw Document (bijv., _Inkooporder_)] → **E-Doc.**

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F1yCRagLzRFmy2hPRDDc1%252Fimage.png%3Falt%3Dmedia%26token%3D020874a9-1eae-4965-9dd2-c23461fc5884\&width=768\&dpr=4\&quality=100\&sign=5e53a730\&sv=2)
2. Onder het tabblad **E-Doc** selecteert u uw formaat (bijv., **EDI**).
3.  Klik op **Transformatie** om te bekijken of te bewerken.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FZtaE4dZT9E1exWMZ5FCI%252Fimage.png%3Falt%3Dmedia%26token%3D787868b4-47b4-455e-9a26-112f692b91f3\&width=768\&dpr=4\&quality=100\&sign=460124f1\&sv=2)

#### Conceptbeheer

* **Maak een Concept**: Klik op het ✏️ potloodpictogram.
* **Concepten Verwijderen**: Gebruik het 🗑️ prullenbakpictogram om ongebruikte concepten te verwijderen.
* **Wijzigingen Activeren**: Klik op het ✅ vinkje om een versie te publiceren.
  * **Opmerking**: Het activeren van een nieuwe versie zal de vorige versie **automatisch deactiveren**.

## 4. XSLT Editor

Het Transformatiebestand wordt bewerkt met behulp van een ingebedde **XSLT Editor** die syntaxmarkering en validatie ondersteunt.

* Voeg sjablonen toe om specifieke paden van de invoer-XML naar de gewenste structuur te mappen.
* Gebruik voorwaardelijke logica (bijv., `<xsl:if>`, `<xsl:choose>`) om optionele of variabele gegevensformaten te verwerken.
* Pas opmaakfuncties toe indien nodig (bijv., stringmanipulatie, datumopmaak).

## 5. Voorbeeldfunctie (Voorbeeld Getransformeerde XML)

De **Voorbeeldfunctie** stelt u in staat om te testen en te bekijken hoe een geüpload EDI-bestand wordt verwerkt met behulp van het huidige **Transformatiebestand**.

#### Gebruik

* Upload een EDI-bestand via de standaard uploadstroom.
* Kopieer de **Document-ID** van het geüploade bestand.
* Navigeer naar de interface van het **Transformatiebestand**.
*   Open de **Voorbeeldfunctie**.\


    <div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F9lddYJl2G4tzpdr9RD5F%252Fimage.png%3Falt%3Dmedia%26token%3Df7663f70-ef10-4e64-bbdc-41048ed8352a&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=36ce2b93&#x26;sv=2" alt="" width="375"></div>
* Voer de **Document-ID** in het veld in en druk op **Test**.
* De resulterende **getransformeerde XML-uitvoer** wordt weergegeven.

Dit is vooral handig voor het debuggen van XSLT-mappings en om ervoor te zorgen dat de uiteindelijke XML-structuur voldoet aan uw opmaakeisen.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FWbwwmXgp6nRPIb1zBpgj%252Fimage.png%3Falt%3Dmedia%26token%3Dab5766f1-45bf-484e-9aa4-ab3059705591\&width=768\&dpr=4\&quality=100\&sign=46905864\&sv=2)

## 6. Video Doorloop

Een videogids voor dit bestandstype is beschikbaar op de [Videopagina.](https://docs.docbits.com/administration-and-setup/settings/global-settings/document-types/edi/edi/edi-videos) Gebruik het om de installatie, bewerking en voorbeeldweergave te volgen.
