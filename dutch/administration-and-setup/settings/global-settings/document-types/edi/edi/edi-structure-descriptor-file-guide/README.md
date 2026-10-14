# EDI Structuur Descriptor Bestand Gids

## **1. Overzicht**

Het **Structuur Descriptor Bestand** bepaalt hoe herhalende EDI-segmenten (bijv. `N1`–`N4`) worden gegroepeerd in gestructureerde JSON. Het zorgt voor:

* **Nauwkeurige parsing** van gerelateerde elementen als enkele eenheden.
* **Consistente output** voor downstream systemen.

_Voor een volledig voorbeeld met segmentdetails, zie_ [_Structuur Descriptor Voorbeeld_](edi-structure-descriptor.md)_._

## **2. Toegang & Basisbewerking**

#### **Toegang tot het Bestand**

1.  **Instellingen** → **Documenttype** → \[Uw Document (bijv., _Inkooporder_)] → **E-Doc.**

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Ff6zyL0AvmqSvrogZdnox%252Fimage.png%3Falt%3Dmedia%26token%3D6bc9ab55-6ee9-43d1-b576-4c5833c208cf\&width=768\&dpr=4\&quality=100\&sign=a23de442\&sv=2)
2. Onder **E-Doc**, selecteer uw formaat (bijv., _EDI_ ).
3.  Klik op **Structuur Descriptor**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FOuNVhIuYBPJTu4PdMecy%252Fimage.png%3Falt%3Dmedia%26token%3Dd111b34e-0dd9-4436-9df4-f59490ac0d87\&width=768\&dpr=4\&quality=100\&sign=6e8e9f0e\&sv=2)

#### **Conceptbeheer**

* **Maak een Concept**: Klik op het ✏️ potloodpictogram om te beginnen met bewerken.
* **Concepten Verwijderen**: Gebruik het 🗑️ prullenbakpictogram om ongebruikte concepten te verwijderen.
* **Wijzigingen Activeren**: Klik op het ✅ vinkje om uw wijzigingen goed te keuren en te publiceren.
  * **Opmerking**: Het activeren van een nieuwe versie zal de vorige versie **automatisch deactiveren**.

## 3. Voorbeeldfunctie (Voorbeeld Geparset XML)

De **Voorbeeldfunctie** stelt u in staat om te testen en te bekijken hoe een geüpload EDI-bestand wordt geparseerd met behulp van het huidige Structuur Descriptor Bestand.

#### Gebruik

* Upload een EDI-bestand via de standaard uploadflow.
* Kopieer de **Document-ID** van het geüploade bestand.
* Ga naar de interface van het **Structuur Descriptor Bestand**.
*   Open de **Voorbeeldfunctie.**\


    <div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F9lddYJl2G4tzpdr9RD5F%252Fimage.png%3Falt%3Dmedia%26token%3Df7663f70-ef10-4e64-bbdc-41048ed8352a&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=36ce2b93&#x26;sv=2" alt="" width="375"></div>
* Voer de **Document-ID** in het veld in en druk op **Test**.
* De resulterende **gestructureerde XML-uitvoer** wordt weergegeven.

Dit is vooral handig voor het debuggen van mappings en het valideren van structurele groeperingen in realtime.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FBXU6zeFapt7ZIVFl37Iz%252Fimage.png%3Falt%3Dmedia%26token%3D9d51e329-b781-4781-a527-3258f6f933c6\&width=768\&dpr=4\&quality=100\&sign=4ca17281\&sv=2)

## 6. Video Doorloop

Een videogids voor dit bestandstype is beschikbaar op de [Video's pagina.](https://docs.docbits.com/administration-and-setup/settings/global-settings/document-types/edi/edi/edi-videos) Gebruik het om mee te doen met de installatie, bewerking en voorbeeldweergave.
