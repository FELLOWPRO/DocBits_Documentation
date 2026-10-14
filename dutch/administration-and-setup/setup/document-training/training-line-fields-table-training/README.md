# Training Line Fields/Tabel Training

## Tabel Training: Wanneer en Hoe te Gebruiken

DocBits gebruikt standaard op AI gebaseerde tabel extractie, die werkt over verschillende leveranciers. Echter, wanneer je meer controle nodig hebt over hoe regelitems worden geëxtraheerd voor een specifieke leverancier, kun je **Tabel Training** gebruiken om de structuur handmatig te definiëren.

#### **Belangrijk: Leverancier-Specifieke Training**

Tabel training is **specifiek voor elke leverancier**. Als je een tabelindeling traint voor een leverancier, zijn de regels alleen van toepassing op de documenten van die leverancier.\
Andere leveranciers blijven AI-gebaseerde tabel extractie gebruiken, tenzij apart getraind.

#### Wanneer Moet Je Tabel Training Gebruiken?

Gebruik Tabel Training **alleen wanneer de documentindeling stabiel is**, en je consistente, hoogwaardige extractie wilt garanderen. Het is het meest geschikt voor leveranciers die:

* Een **vast factuurformaat** gebruiken in de loop van de tijd.
* **Nauwkeurige mapping** van regelitems naar specifieke velden vereisen.
* **Leveranciers met een hoog volume**, waar consistente automatisering waardevol is.

#### Wanneer Moet Je Geen Tabel Training Gebruiken

Vermijd het gebruik van Tabel Training als:

* De leverancier **vaak hun factuurindeling wijzigt** (bijv. elke paar maanden).
* Je niet regelmatig documenten van die leverancier ontvangt.
* De standaard AI-extractie goed genoeg werkt zonder handmatige training.

In dergelijke gevallen zou het herhaaldelijk opnieuw trainen van de tabel inefficiënt en tijdrovend zijn.

## Hoe het te Gebruiken:

**Trainingsmodus** wordt gebruikt om DocBits te leren hoe regelitems correct moeten worden geëxtraheerd uit de specifieke documentindeling van een leverancier.

Wanneer je in de Trainingsmodus bent, definieer je:

* **Waar de tabel zich bevindt** op het document.
* **Welke gebieden overeenkomen met elke kolom** (bijv. Hoeveelheid, Omschrijving, Eenheidsprijs).

Deze modus creëert een **herbruikbaar extractiesjabloon** voor die leverancier, zodat toekomstige documenten met dezelfde indeling automatisch worden verwerkt — geen noodzaak om opnieuw te trainen.

**Belangrijke Kenmerken:**

* **Gemapte kolommen zijn alleen-lezen** — je kunt de tekst niet handmatig wijzigen.
* Je **kunt geen rijen toevoegen of verwijderen**.
* De focus ligt op **het in kaart brengen van posities**, niet op het corrigeren van waarden.
* Zodra je de tabel en de kolommen hebt gemapt, klik op **"Regels Opslaan"** zodat DocBits leert en deze training toepast op soortgelijke documenten van dezelfde leverancier.

**Correctiemodus** stelt je in staat om **extractiefouten te corrigeren** in de tabelgegevens voor het huidige document. Het wordt gebruikt wanneer DocBits al heeft geprobeerd de tabel te extraheren, maar de resultaten kleine correcties nodig hebben.

Gebruik Correctiemodus wanneer:

* Sommige **waarden ontbreken of verkeerd uitgelijnd zijn**.
* Een **lege of dubbele regel** is geëxtraheerd en moet worden verwijderd.

**Wat Je Kunt Doen in Correctiemodus:**

* **Waarden handmatig aanpassen** in gemapte kolommen (bijv. verkeerd geplaatste items corrigeren).
* **Rijen verwijderen** die geen deel moeten uitmaken van de tabel.
* **Rijen toevoegen** die tijdens de extractie volledig zijn gemist.
