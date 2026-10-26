# Structureren en verbeteren van tabelextractie in DocBits

Zodra een tabel is geëxtraheerd en de initiële kolomtoewijzing is voltooid, kunt u de kwaliteit en structuur van de gegevens verbeteren met behulp van verschillende ingebouwde hulpmiddelen. Deze handleiding leidt u door:

* Rijen groeperen
* Handmatige rijselectie
* Kolommen toewijzen
* Kolomkoppen verfijnen met regex

Deze hulpmiddelen zijn vooral nuttig bij complexe of inconsistente documentindelingen.

## 1. Rijen Groeperen

Documenten zoals facturen of orderbevestigingen bevatten vaak tabelregels waarbij één kolom (bijvoorbeeld een omschrijving) meerdere regels beslaat, terwijl andere kolommen (bijvoorbeeld hoeveelheid of prijs) slechts één regel gebruiken.

Neem dit Duitse factuurvoorbeeld — de kolom "Bezeichnung" (omschrijving) beslaat meerdere rijen:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-improving-table-extraction-with-regex-multiline-doc-nl-20261009.png" alt="Tabel van een Duitse factuur waarin de omschrijving (Bezeichnung) van elke regel meerdere rijen beslaat."><figcaption><p>Een omschrijvingskolom die meerdere rijen beslaat.</p></figcaption></figure>

In eerste instantie extraheert DocBits elke rij afzonderlijk:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-improving-table-extraction-with-regex-initial-extraction-nl-20261009.png" alt="Geëxtraheerde tabel in de weergave Tabel Extractie waarin elke tekstregel van de omschrijving een eigen rij is geworden."><figcaption><p>DocBits extraheert eerst elke rij afzonderlijk.</p></figcaption></figure>

U kunt vervolgens **rijen groeperen op basis van een kolom**, zoals "Positie". Dit voegt gerelateerde regels samen tot één gestructureerde invoer:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-improving-table-extraction-with-regex-grouped-result-nl-20261009.png" alt="Geëxtraheerde tabel waarin de omschrijvingsregels die op Positie zijn gegroepeerd één invoer per positie vormen."><figcaption><p>Na groepering op Positie vormen de gerelateerde regels één invoer.</p></figcaption></figure>

Hoeveel subregels tot één invoer worden samengevoegd en hoe het groeperen zich gedraagt, stelt u in bij de [Geavanceerde instellingen](advanced-settings.md) onder **Minimum gegroepeerde rijen** en **Omgekeerde groepering**.

## 2. Handmatige Rijselectie

In sommige gevallen is de tekst op een document verdeeld over meerdere kolommen binnen één rij, waardoor automatische toewijzing moeilijk is.

Hier is een voorbeeld waarbij de regel "PRAEF" overlapt met **Bezeichnung**, **Menge**, **ME** en **Preis in EUR**:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-improving-table-extraction-with-regex-row-misalignment-nl-20261009.png" alt="Tabel van een factuur met een PRAEF-regel waarvan de tekst over meerdere kolommen loopt."><figcaption><p>Een PRAEF-regel die niet aansluit op de kolomstructuur.</p></figcaption></figure>

### Waarden handmatig toewijzen:

1.  **Schakel de Trainingsmodus in**

    <figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-improving-table-extraction-with-regex-training-mode-nl-20261009.png" alt="Scherm Tabel Extractie met de Trainingsmodus ingeschakeld."><figcaption><p>Trainingsmodus ingeschakeld.</p></figcaption></figure>
2.  **Activeer de Rijgegevensbewerkingsmodus**

    <figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-improving-table-extraction-with-regex-row-edit-mode-nl-20261009.png" alt="Scherm Tabel Extractie met de modus Rijgegevensbewerkingsmodus: Aan en de bijbehorende tooltip zichtbaar."><figcaption><p>Rijgegevensbewerkingsmodus geactiveerd.</p></figcaption></figure>
3.  **Selecteer en Koppel Tekst**\
    Klik op het juiste stuk tekst en wijs het toe aan een **blauwe** kolomkop.

    <figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-improving-table-extraction-with-regex-editable-columns-nl-20261009.png" alt="Geëxtraheerde tabel in de rijgegevensbewerkingsmodus met de blauwe, nog lege kolomkoppen die handmatig kunnen worden toegewezen."><figcaption><p>Blauwe kolomkoppen kunnen handmatig worden ingevuld.</p></figcaption></figure>

> Opmerking: Paarsgekleurde kolommen zijn al systeemtoegewezen en kunnen niet handmatig worden bewerkt.

Dit werk gebeurt in de **rijgegevensbewerkingsmodus** (**Rijgegevensbewerkingsmodus: Aan**). Wat u daar kunt doen en wanneer u die in plaats van de **Trainingsmodus** gebruikt, staat in [Training van regelvelden/tabeltraining](README.md).

## 3. Kolommen Toewijzen

Kolomtoewijzing koppelt uw geëxtraheerde gegevens aan de verwachte kolomkoppen, zodat consistentie en exporteerbaarheid zijn gegarandeerd.

Een kolom toewijzen of opnieuw toewijzen:

1. Klik op de kolomkop in de extractieweergave.
2. Kies de juiste doelkolom uit de vervolgkeuzelijst.

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-improving-table-extraction-with-regex-mapping-dropdown-nl-20261009.png" alt="Geëxtraheerde tabel met de geopende vervolgkeuzelijst van de kolomkop, met de doelkolommen Beschrijving, Artikelnummer, Nettobedrag, Positie, Hoeveelheid, Totaalbedrag, Eenheid en Eenheidsprijs."><figcaption><p>Kies de doelkolom in de vervolgkeuzelijst van de kolomkop.</p></figcaption></figure>

U kunt de toewijzing zo vaak aanpassen als nodig is.

Zie [Tabellen en kolommen definiëren](defining-tables-and-columns.md) voor meer informatie over het maken van tabellen en kolommen.

## 4. Extraheren van Boven / Onder

Sommige documenten zijn zo opgebouwd dat relevante tabelwaarden niet op dezelfde rij als andere gegevens verschijnen. In die gevallen kunt u met DocBits bepalen **vanaf welke rij de gegevens moeten worden geëxtraheerd**:

* **Extraheren van Boven**: Gebruik dit wanneer de waarde voor de huidige rij **in de regel erboven** verschijnt.
* **Extraheren van Onder**: Gebruik dit wanneer de waarde **in de regel eronder** verschijnt.

**Waar u het vindt**

1. Ga naar de **Trainingsmodus**.
2. Klik op de drie puntjes (⋯) op een kolomkop.
3. Kies onder de optie **"Extraheren van"** `Boven` of `Onder`, afhankelijk van de documentindeling.

## 5. Bedrag Formaat

Sommige kolommen, zoals **Hoeveelheid** of **Eenheidsprijs**, bevatten numerieke of datumwaarden die verschillende opmaakconventies kunnen volgen, afhankelijk van de herkomst of locatie van het document. Met DocBits kunt u het formaat opgeven dat deze waarden moeten volgen om nauwkeurige extractie en interpretatie te garanderen.

**Opties voor Bedrag Formaat:**

* Definieer het verwachte getal- of datumformaat voor de kolom, zoals VS (MM/DD/JJJJ, decimaal met punt), Polen (DD.MM.JJJJ, decimaal met komma), Duitsland en andere.
* Dit helpt DocBits om waarden correct te parseren en te standaardiseren, zelfs als het document een andere regionale indeling gebruikt.

**Waar u het vindt**

1. Ga naar de **Trainingsmodus**.
2. Klik op de drie puntjes (⋯) op de kop van een ondersteunde kolom (bijvoorbeeld Hoeveelheid, Eenheidsprijs).
3. Selecteer onder de optie **Bedrag Formaat** het gewenste formaat dat overeenkomt met de locatie van uw document.

## 6. Tabelextractie verbeteren met Regex

## **Wat het doet**

Met deze functie definieert u voor elke tabelkop een regex, waardoor de extractie nauwkeuriger wordt en de juiste resultaten worden gegarandeerd.

## **Hoe u het gebruikt**

1. Open een document van de leverancier waarvoor u een regex wilt definiëren.
2.  Ga naar de weergave **Tabel Extractie**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FDdlNrO6hG6jnEeWU9DuZ%252Fimage.png%3Falt%3Dmedia%26token%3Dca11a537-27a4-4b00-b3e7-f77540c28c2b\&width=768\&dpr=4\&quality=100\&sign=fd47355a\&sv=2)
3. Schakel de **Trainingsmodus** in.
4.  Selecteer de tabelkop die u wilt verfijnen en kies vervolgens **Regex**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fes6PsB9sHHXp0CNRj6YF%252Fimage.png%3Falt%3Dmedia%26token%3D6e31e4db-fd2f-487c-ac19-f1d6add81ad1\&width=768\&dpr=4\&quality=100\&sign=32264560\&sv=2)
5.  Er verschijnt een pop-up waarin u uw regex kunt invoeren en definiëren.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FWB7hjuuyVVAewRqrnhYj%252FiScreen%2520Shoter%2520-%2520Google%2520Chrome%2520-%2520250303135020.jpg%3Falt%3Dmedia%26token%3D6a31253d-18d7-4d8f-a00e-acd89a744127\&width=768\&dpr=4\&quality=100\&sign=d8d2d94a\&sv=2)
6.  Klik op **Valideren** om de regex te controleren en vervolgens op **Wijzigingen Opslaan** om deze toe te passen.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FC4R2o2W10ct1o0oesTLZ%252FiScreen%2520Shoter%2520-%2520Google%2520Chrome%2520-%2520250303135153.jpg%3Falt%3Dmedia%26token%3D43e53a05-53fe-4503-ba51-55c85910bd82\&width=768\&dpr=4\&quality=100\&sign=9ec6eb7b\&sv=2)
7. **Sla de regel op en bevestig** om de wijzigingen toe te passen.

Hoe u getrainde regels blijvend opslaat of verwijdert, staat in [Regels Opslaan en Verwijderen](save-and-delete-rules.md).

## Wanneer u elke functie gebruikt

Gebruik deze hulpmiddelen om de extractienauwkeurigheid te verhogen en handmatig werk te verminderen:

* **Groeperen**: Wanneer een omschrijving of een willekeurige kolom meerdere rijen beslaat en voor de duidelijkheid moet worden samengevoegd.
* **Handmatige Rijselectie**: Wanneer rijen niet netjes zijn gestructureerd en delen van de inhoud in de verkeerde kolommen terechtkomen.
* **Kolommen Toewijzen**: Wanneer de automatisch gedetecteerde kolomnamen niet overeenkomen met uw structuur of verfijning nodig hebben.
* **Regex-regels**: Wanneer tabelkoppen licht variëren tussen documenten van dezelfde leverancier of OCR inconsistenties introduceert.

Gerelateerde handleidingen in dit gebied:

* [Geavanceerde instellingen](advanced-settings.md) – groeperen, kopregels en omgaan met extra rijen.
* [Tabellen en kolommen definiëren](defining-tables-and-columns.md) – tabellen en kolommen maken voor de training.
* [Regels Opslaan en Verwijderen](save-and-delete-rules.md) – een getrainde indeling blijvend toepassen of loslaten.
