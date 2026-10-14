# Structureren en Verbeteren van Tabel Extractie in DocBits

Zodra een tabel is geëxtraheerd en de initiële kolommapping is voltooid, kunt u de kwaliteit en structuur van de gegevens verbeteren met behulp van verschillende ingebouwde tools. Deze gids loodst u door:

* Groeperen van rijen
* Handmatige rijselectie
* Kolommapping
* Headerverfijning met behulp van regex

Deze tools zijn vooral nuttig bij het omgaan met complexe of inconsistente lay-outs van documenten.

## 1. Groeperen van Rijen

Documenten zoals facturen of orderbevestigingen bevatten vaak tabelvermeldingen waarbij één kolom (bijv. een beschrijving) meerdere regels beslaat, terwijl andere kolommen (bijv. hoeveelheid of prijs) slechts één regel gebruiken.

Neem bijvoorbeeld deze Duitse factuur - de kolom "Bezeichnung" (beschrijving) beslaat meerdere rijen:

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FVino2M4Esor3IRHGqBd5Brx7_lKPIwEOlRYBHzMXw4WoacFNW39hbWuwoUNGocubx4Bh9_BvUBqZSWA4U_NmU8FBw4Q1_AiTASgMx-2MLKvsHLJY057oqyks0fQ5b7mI577JTX5rBKdEG90O9F5TcoU\&width=768\&dpr=4\&quality=100\&sign=ae0bd75a\&sv=2)

In eerste instantie extraheren DocBits elke rij afzonderlijk:

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FUX5OdkW59HPVROnNzSeZbDw4NYTPbfayDLIXBQi0pwHzUEJ1B5t7I9uKBNc0dmOB3Cile8Xv6AdgVXuUd0aMbQFGWagBCEetw8P-N4zgG_cGTjWHhpDtGQZg27UZKdCDJ5FeEDJgFAYtTB8kZrMSdho\&width=768\&dpr=4\&quality=100\&sign=b6990876\&sv=2)

Vervolgens kunt u **rijen groeperen op basis van een kolom**, zoals "Positie." Dit combineert gerelateerde regels tot één gestructureerde vermelding:

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FPxA6h2udUuYd1YmHV97t-bzfZzipFpdA5t8gjpGXWx9sA-I4tW3tYwD28icv88UEmitz0EAaWuGkU5ZwqAjcQnoOkmg9u1AcBJW3nITU6eFa0foHB-AQPb0qv0AWaaEwM6WvwaEcAODEUzKtvRZOMN0\&width=768\&dpr=4\&quality=100\&sign=36b99bc7\&sv=2)

## 2. Handmatige Rijselectie

In sommige gevallen is de tekst op een document verdeeld over meerdere kolommen in één rij, waardoor het moeilijk is om automatisch toe te wijzen.

Hier is een voorbeeld waar de regel "PRAEF" overlapt met **Bezeichnung**, **Menge**, **ME**, en **Preis in EUR**:

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FLbVbmfdOBpeCWDftPvW0qjEHjbLmWYRrAGTZHVW8VEHQTEvl5GoqH2wkFE5iUOySmF50b1V8CDAZhfMzPTeMQscmc61SDKaqSCW-y0Z7fjlwOjhtjxWD44oCsgHmwrgrBD4cuEGgn9JY_UX3t9jRlPs\&width=768\&dpr=4\&quality=100\&sign=5ff4a2e1\&sv=2)

### Hoe waarden handmatig toewijzen:

1.  **Training Mode inschakelen**

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2F4D8iCXk0p_Mur8bX_11ne_2iA-GOxoFi2OQWlSEvrH1auoE0ksnYXpZx3Pw3PUJJRZJN85dnQlSSBB369FfafXAy8adjFZcnepQnODSaaIj69cxtUKFAXPgn5eyPE6jbJuzStJALMgumlt49Z1Pv3FY\&width=768\&dpr=4\&quality=100\&sign=232c58a9\&sv=2)
2.  **Activeer Rijbewerkingsmodus**

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2F8YQmo_WRuKKVjk1a_eoxSBiQr0GncuS4BmCA0aI9aOlrbsIvdj8dZlurxxBHp2lH4ozT4HPWw9qYDW7xLQ7u2DSyU8DrNzSBC7LjzKLTDJ2tudY9a_DENDoK5Aya6L1hcf1WF1RD92S_DzhGVV4Gh6Q\&width=768\&dpr=4\&quality=100\&sign=8fc5c089\&sv=2)
3.  **Selecteer en Koppel Tekst** Klik op het juiste stuk tekst en wijs het toe aan een **blauwe** kolomkop.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2Fi2tlbwl9qFE0clthaoRPe7kcPRiURCvemuLEjBK4uAnfsR4auXbftMfEY1ZW5WXwezTBVSG5hbNRkddwIeLtrgJUvZoeKGdPKN8f75O_dPdIWkm4EFALfAj-evDUI3UKrgNOTNjF37C1bBLtE95OA1w\&width=768\&dpr=4\&quality=100\&sign=842a42\&sv=2)

> Opmerking: Paarsgekleurde kolommen zijn al systeemtoegewezen en kunnen niet handmatig worden bewerkt.

## 3. Kolommen Mappen

Kolommapping koppelt uw geëxtraheerde gegevens aan de verwachte kolomkoppen, zodat consistentie en exporteerbaarheid worden gegarandeerd.

Om een kolom te mappen of opnieuw te mappen:

1. Klik op de kolomkop in de extractieweergave.
2. Kies de juiste doelkolom uit de vervolgkeuzelijst.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FX_65pCWrI4HMFr_aiA0eoSDp-yIYy49lULzAZaiIgnr0aIowlLSed21MuehkGLs4UIdQousdfhiZi5pnQtpZ0uUn6dxlzii7WPQvov-kN1_Jimsi6U6zowOLxjBzZzZ47kaRhduAVBd_Ya9QQtXTpJ4\&width=768\&dpr=4\&quality=100\&sign=4e2a3bdc\&sv=2)

U kunt de mapping zo vaak aanpassen als nodig is.

## 4. Boven / Onder Extraheren

Sommige documenten zijn gestructureerd op een manier waarbij relevante tabelwaarden niet op dezelfde rij verschijnen als andere gegevens. In deze gevallen kunt u met DocBits bepalen **vanaf welke rij de gegevens moeten worden geëxtraheerd**:

* **Boven extraheren**: Gebruik dit wanneer de waarde voor de huidige rij **in de regel erboven** verschijnt.
* **Onder extraheren**: Gebruik dit wanneer de waarde **in de regel eronder** de huidige rij verschijnt.

**Waar te vinden**

1. Ga naar **Training Mode**.
2. Klik op de drie puntjes (⋯) op een kolomkop.
3. Onder de optie **"Extraheren van"**, kies `Boven` of `Onder` afhankelijk van de lay-out van het document.

## 5. Bedrag Formaat

Sommige kolommen, zoals **Hoeveelheid** of **Eenheidsprijs**, bevatten numerieke of datumwaarden die verschillende opmaakconventies kunnen volgen, afhankelijk van de oorsprong of locatie van het document. DocBits stelt u in staat om de opmaak te specificeren die deze waarden moeten volgen om een nauwkeurige extractie en interpretatie te garanderen.

**Opties voor Bedrag Formaat:**

* Definieer het verwachte nummer- of datumformaat voor de kolom, zoals VS (MM/DD/JJJJ, decimaal met punt), Polen (DD.MM.JJJJ, decimaal met komma), Duitsland en anderen.
* Dit helpt DocBits om waarden correct te parseren en standaardiseren, zelfs als het document een andere regionale opmaak gebruikt.

**Waar te vinden**

1. Ga naar **Training Mode**.
2. Klik op de drie puntjes (⋯) op de kop van een ondersteunde kolom (bijv. Hoeveelheid, Eenheidsprijs).
3. Onder de optie **Bedrag Formaat**, selecteer het gewenste formaat dat overeenkomt met de locatie van uw document.

## 6. Verbeteren van Tabel Extractie met Regex

## **Wat het Doet**

Deze functie stelt u in staat om voor elke tabelkop een regex te definiëren, waardoor de extractie nauwkeuriger wordt en de juiste resultaten worden gegarandeerd.

## **Hoe het te Gebruiken**

1. Open een document van de leverancier waarvoor u een regex wilt definiëren.
2.  Ga naar de **Tabel Extractie** weergave.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FDdlNrO6hG6jnEeWU9DuZ%252Fimage.png%3Falt%3Dmedia%26token%3Dca11a537-27a4-4b00-b3e7-f77540c28c2b\&width=768\&dpr=4\&quality=100\&sign=fd47355a\&sv=2)
3. Schakel **Training Mode** in.
4.  Selecteer de tabelkop die u wilt verfijnen, kies vervolgens **Regex**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fes6PsB9sHHXp0CNRj6YF%252Fimage.png%3Falt%3Dmedia%26token%3D6e31e4db-fd2f-487c-ac19-f1d6add81ad1\&width=768\&dpr=4\&quality=100\&sign=32264560\&sv=2)
5.  Er verschijnt een pop-up waar u uw regex kunt invoeren en definiëren.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FWB7hjuuyVVAewRqrnhYj%252FiScreen%2520Shoter%2520-%2520Google%2520Chrome%2520-%2520250303135020.jpg%3Falt%3Dmedia%26token%3D6a31253d-18d7-4d8f-a00e-acd89a744127\&width=768\&dpr=4\&quality=100\&sign=d8d2d94a\&sv=2)
6.  Klik op **Valideren** om de regex te controleren, klik vervolgens op **Wijzigingen Opslaan** om deze toe te passen.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FC4R2o2W10ct1o0oesTLZ%252FiScreen%2520Shoter%2520-%2520Google%2520Chrome%2520-%2520250303135153.jpg%3Falt%3Dmedia%26token%3D43e53a05-53fe-4503-ba51-55c85910bd82\&width=768\&dpr=4\&quality=100\&sign=9ec6eb7b\&sv=2)
7. **Sla de regel op en bevestig** om de wijzigingen toe te passen.

## Wanneer elk kenmerk te gebruiken

Gebruik deze tools om de extractie nauwkeurigheid te verhogen en handmatig werk te verminderen:

* **Groeperen**: Wanneer een beschrijving of een kolom meerdere rijen beslaat en moet worden gecombineerd voor duidelijkheid.
* **Handmatige Rijselectie**: Wanneer rijen niet schoon gestructureerd zijn en delen van de inhoud in de verkeerde kolommen vallen.
* **Kolommapping**: Wanneer de automatisch gedetecteerde kolomnamen niet overeenkomen met uw structuur of verfijning nodig hebben.
* **Regex Regels**: Wanneer tabelkoppen lichtjes variëren tussen documenten van dezelfde leverancier of OCR inconsistenties introduceert.
