# EDI Extraction Paths Bestandsgids

## 1. Overzicht

Het **Extraction Paths-bestand** bepaalt hoe gegevens worden geëxtraheerd uit de **gestructureerde XML** naar specifieke documentvelden en tabellen binnen de interface. Het koppelt **veld-ID's** aan **XPath-uitdrukkingen**, die worden geëvalueerd om waarden uit de XML te halen en in de overeenkomstige documentvelden te plaatsen. Dit bestand speelt een cruciale rol bij het garanderen dat geëxtraheerde gegevens correct verschijnen tijdens veldvalidatie en downstream verwerking.

## 2. Doel en Functie

* Koppelt elk documentveld en tabelkolom aan een specifieke locatie in de gestructureerde XML met behulp van XPath-uitdrukkingen.
* Zorgt ervoor dat de juiste waarden worden ingevuld in velden zoals `order_number`, `supplier_name` en `total_amount`.
* Ondersteunt zowel **enkele velden** (via een `fields` object) als **tabellen** (via een `tables` array met rijpaden en kolomkoppelingen).
* Maakt nauwkeurige controle mogelijk over hoe gegevens worden opgehaald uit de XML, inclusief het gebruik van XPath-functies zoals `sum()`.

Voorbeeld veldkoppeling:

Copy

```
"order_number": "//PURCHASE_ORDER/PURCHASE_ORDER/text()"
```

## 3. Toegang & Basisbewerking

#### **Toegang tot het bestand:**

1.  Ga naar **Instellingen** → **Documenttype** → _\[Uw Document (bijv. Inkooporder)]_ → **E-Doc**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Ff6zyL0AvmqSvrogZdnox%252Fimage.png%3Falt%3Dmedia%26token%3D6bc9ab55-6ee9-43d1-b576-4c5833c208cf\&width=768\&dpr=4\&quality=100\&sign=a23de442\&sv=2)
2. Onder het tabblad **E-Doc** selecteert u uw formaat (bijv. **EDI**).
3.  Klik op **Extraction Paths** om het bestand te bekijken of te bewerken.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FawwG5QnErp1yy1eYHrlX%252Fimage.png%3Falt%3Dmedia%26token%3D46a6d8b3-52d2-4c13-bc72-1a74955efd9f\&width=768\&dpr=4\&quality=100\&sign=e612882b\&sv=2)

#### **Conceptbeheer:**

* **Maak een Concept:** Klik op het ✏️ potloodpictogram.
* **Verwijder Concepten:** Gebruik het 🗑️ prullenbakpictogram om ongebruikte concepten te verwijderen.
* **Wijzigingen Activeren:** Klik op het ✅ vinkje om een versie te publiceren.
  * **Opmerking**: Het activeren van een nieuwe versie zal de vorige versie **automatisch deactiveren**.

## 4. Editor & Syntax

Het Extraction Paths-bestand is geschreven in **JSON** en bevat twee hoofdcomponenten:

* **fields**: Een woordenboek waarbij elke sleutel een veld-ID is en elke waarde een XPath-uitdrukking is die bepaalt hoe de gegevens moeten worden geëxtraheerd.
* **tables**: Een lijst met tabeldefinities die het volgende omvatten:
  * `name`: Het ID van de tabel.
  * `row_path`: Een XPath die elke rij van de tabel identificeert.
  * `columns`: Een lijst met kolomkoppelingen (`name`, `path`).

U kunt ook XPath-functies (bijv. `sum()`) en uitdrukkingen gebruiken om waarden dynamisch te berekenen uit herhalende elementen.

Copy

```
jsonCopyEdit"total_net_amount": "sum(//PURCHASE_ORDER/ORDER_LINES/ORDER_LINE/SUB_TOTAL)"
```

## 5. Voorbeeldfunctie (Evaluatie-extractie)

De **Voorbeeldfunctie** stelt u in staat om te simuleren hoe de extractiepaden zich zullen gedragen met een echt geüpload document.

**Gebruik:**

* Upload een EDI-bestand via het standaard uploadproces.
* Kopieer de **Document-ID**.
* Ga naar de **Extraction Paths** interface.
* Open de **Voorbeeldfunctie**.\
  \
  &#x20;![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F9lddYJl2G4tzpdr9RD5F%252Fimage.png%3Falt%3Dmedia%26token%3Df7663f70-ef10-4e64-bbdc-41048ed8352a\&width=300\&dpr=4\&quality=100\&sign=36ce2b93\&sv=2)
* Voer de Document-ID in en klik op **Test**.
* Het resultaat toont hoe elk veld en elke tabel wordt ingevuld op basis van de geconfigureerde paden.

Deze functie is essentieel om te controleren of uw XPath-uitdrukkingen correct zijn gedefinieerd en de verwachte waarden ophalen voordat het concept wordt geactiveerd.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F81uvH6FFVBJsSZucanWY%252Fimage.png%3Falt%3Dmedia%26token%3Dde3ba545-1ee3-44b2-a629-9660d80174f2\&width=768\&dpr=4\&quality=100\&sign=43c8b507\&sv=2)

## 6. Video Walkthrough

Een videogids voor dit bestandstype is beschikbaar op de [Videopagina.](https://docs.docbits.com/administration-and-setup/settings/global-settings/document-types/edi/edi/edi-videos) Gebruik het om de installatie, bewerking en voorbeeldweergave te volgen.
