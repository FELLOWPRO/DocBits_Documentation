# Regels voor het Matchen van Inkooporders

## Introductie: Inkooporders en Beheer van PO-regels

Het matchen van Inkooporders (PO) is een cruciaal proces om consistentie te waarborgen tussen Inkooporders (PO's) en de bijbehorende binnenkomende facturen of goederenontvangsten. Een robuuste set regels is essentieel om een hoge mate van automatische matching te bereiken, fraude te voorkomen en correcte betalingen te garanderen.

Deze configuratiepagina wordt gebruikt om de regels te definiëren en beheren die bepalen _hoe_ PO-regelitems worden gematcht met het bijbehorende binnenkomende document (Factuur, Orderbevestiging).

{% hint style="info" %}
**Vereiste:** de matchregels worden alleen gebruikt wanneer **PO match server side** is ingeschakeld voor het documenttype (Instellingen → Documenttypen → Meer instellingen → Inkooporder). Bij uitgeschakelde schakelaar matched DocBits met zijn ingebouwde matcher (hoeveelheid, eenheidsprijs, artikelnummer, inkoopordernummer) en negeert de regels.
{% endhint %}

***

## Toegang krijgen

1.  Navigeer naar **Instellingen --> Globale instellingen --> Documenttypen**

    <figure><img src="../../../../../../.gitbook/assets/image (31).png" alt=""><figcaption></figcaption></figure>


2.  Selecteer het gewenste documenttype en klik op **Meer instellingen**.

    <figure><img src="../../../../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>


3.  Ga vervolgens naar de sectie Inkooporder en klik op de knop (PO match server side), daarna klik je op Configureer PO Matchregels

    <figure><img src="../../../../../../.gitbook/assets/image (168).png" alt=""><figcaption></figcaption></figure>

***

<figure><img src="../../../../../../.gitbook/assets/Bildschirmfoto 2025-12-09 um 07.43.15.png" alt=""><figcaption></figcaption></figure>

## Globale instellingen (Basisregels)

Deze instellingen vormen het kader dat van toepassing is op alle matchregels:

* **Instelling:** Match Hoeveelheid Op
  * **Doel:** Bepaalt welke hoeveelheid van de inkooporderregel wordt vergeleken met de documentregel — bijvoorbeeld de bestelde hoeveelheid of de **openstaande factuurhoeveelheid** (besteld minus al gefactureerd), wat de gebruikelijke keuze is voor facturen.
  * **Geldige waarden:** Hoeveelheid of andere beschikbare hoeveelheidvelden in het systeem, afhankelijk van de datastructuur (bijv. een alternatief genormaliseerd hoeveelheidveld).
  * **Afhankelijkheid:** Bepaalt de basis voor alle matchregels die hoeveelheid in hun vergelijkingscriteria opnemen.
* **Instelling:** Standaardtolerantie (Standaardtolerantie)
  * **Doel:** Bepaalt hoe ver een numerieke waarde op het document mag afwijken van de waarde op de inkooporder en toch als een match wordt beschouwd. Het compenseert afrondingsverschillen. Het is van toepassing op **elke numerieke kolom** met "Tolerantie toestaan" ingeschakeld — zowel hoeveelheid als eenheidsprijs.
  * **Geldige waarde:** Een decimaal getal. Of dit wordt gelezen als een **absolute waarde** (0,005 = een afwijking tot 0,005 in de vergeleken hoeveelheid of prijs) of als een **percentage** (0,5 = 0,5 % van de vergeleken waarde) wordt ingesteld door het **tolerantietype** van de regels (`value` of `percent`; nieuwe regels gebruiken `value`). Per-item toleranties (zie [Tolerantie-instellingen](purchase-order-tolerance-settings-additional-purchase-order-tolerance.md)) overschrijven de standaardtolerantie voor dat item.
  * **Afhankelijkheid:** Van toepassing op regels die numerieke velden gebruiken voor matching en de optie "Tolerantie toestaan" hebben ingeschakeld.

***

## Regellijst

De Regellijst toont alle beschikbare matchregels en beheert hun uitvoeringsvolgorde.

#### Structuur en Uitvoering

* **Prioriteit:** Dit numerieke veld (bijv. 1, 2, 3) bepaalt de uitvoeringsvolgorde van de regels. Regels met een lagere prioriteitswaarde worden eerst geprobeerd. Dit stelt beheerders in staat een hiërarchie te structureren, meestal beginnend met de meest specifieke en strenge regels (bijv. matchen op zowel regelnummer als artikelnummer) en terugvallend op bredere of minder restrictieve regels.
* **Naam & Beschrijving:** Biedt een duidelijke identificatie en context voor de regel, waarin de primaire criteria worden uitgelegd (bijv. "Standaardregel nr. 1: Match op basis van Regelnr., Artikel-ID en Hoeveelheid").
* **Actief:** Een eenvoudige schakelaar waarmee de regel direct kan worden geactiveerd of gedeactiveerd zonder de configuratie te verwijderen.

**Uitvoeringsstroom:** Het systeem voert matching uit in een cascaderende volgorde. Als een regel (bijv. Prioriteit 1) succesvol een regelitem matched, stopt het proces voor dat item. Als er geen match wordt gevonden, gaat het systeem door naar de volgende regel in de prioriteitsvolgorde (bijv. Prioriteit 2). Elke uitvoering wordt geregistreerd op het document; de **matchgeschiedenis** in het scherm Inkooporder Matching toont welke regel is geprobeerd, welke matchte en welke werden overgeslagen en waarom.

***

## Regelconfiguratie (Detailinstellingen)

Dit gedetailleerde configuratiegebied definieert de specifieke logica en criteria voor een individuele regel.

#### Basisparameters

* **Regeltype:** Specificeert de matchingscardinaliteit.

| Regeltype          | Wat het doet                                                                                                                                                                                             | Typisch gebruik                                                                 |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| **Single match**   | Eén inkooporderregel naar één documentregel. Elke geconfigureerde kolom moet overeenkomen (binnen tolerantie waar toegestaan).                                                                             | De standaard situatie.                                                          |
| **Multi match**    | Meerdere inkooporderregels naar één documentregel, of meerdere documentregels naar één inkooporderregel. Hoeveelheden worden **opgeteld**, de eenheidsprijs wordt vergeleken als een **gemiddelde**, de andere kolommen moeten overeenkomen. | Gesplitste leveringen, één factuurregel die meerdere orderregels dekt.         |
| **Match on total** | Vergelijkt één **bedrag** — meestal het nettobedrag van de documentregel tegen het **totaal** van de inkooporder — en matched de hele inkooporder in één keer.                                            | Leveranciers die één totaalbedrag factureren, servicefacturen, één-regel facturen.|

* **Automatische Match:** Indien ingeschakeld probeert het systeem deze regel volledig automatisch toe te passen. Er is hoge zekerheid vereist in de criteria voor automatische verwerking.
* **Handmatige Match:** Indien ingeschakeld kan deze regel worden gepresenteerd of toegepast door een gebruiker tijdens de handmatige afstemmingsstap, waarbij een vooraf gedefinieerde set vergelijkingscriteria wordt aangeboden om uitzonderingen op te lossen.
* **Fallback:** Een regel die als fallback is gemarkeerd, wordt in een latere fase uitgevoerd, alleen voor de regelparen die na alle reguliere regels nog niet gematcht zijn. Gebruik dit voor de "lossere" regel die moet opvangen wat de strikte regels hebben gemist.

#### Activatievoorwaarden

Een regel kan **activatievoorwaarden** bevatten — uitdrukkingen die waar moeten zijn voordat de regel überhaupt wordt uitgevoerd. Als een voorwaarde onwaar is, wordt de regel **overgeslagen voor dit document** (de matchgeschiedenis toont dit als "niet uitgevoerd" met de reden). De uitdrukkingen gebruiken het aantal regels dat gematcht wordt:

| Uitdrukking               | Betekenis                                                            |
| ------------------------ | ------------------------------------------------------------------- |
| `[[count(po_lines)]]`    | aantal beschikbare inkooporderregels voor matching                  |
| `[[count(table_lines)]]` | aantal regelitems op het document die zijn gemapt voor matching     |

Vergelijk ze met `==`, `!=`, `>`, `>=`, `<`, `<=` en combineer meerdere voorwaarden met `&` (en). Voorbeelden:

* `([[count(po_lines)]] > 1) & ([[count(table_lines)]] > 1)` — alleen voor documenten met meerdere regels aan beide zijden (typisch voor een multi match regel).
* `([[count(po_lines)]] == 1) & ([[count(table_lines)]] == 1)` — alleen voor éénregelige documenten tegenover een éénregelige order.
* `([[count(po_lines)]] >= 1) & ([[count(table_lines)]] >= 1)` — wanneer er iets te matchen is.

{% hint style="warning" %}
Activatievoorwaarden zijn de meest voorkomende reden waarom een regel "niets doet". Een match-on-total regel met de voorwaarde `[[count(table_lines)]] > 1` wordt nooit uitgevoerd voor een éénregelige factuur — en een [transformatie regel](../../transformation-rules.md) die de factuur samenvouwt tot één totaalregel produceert precies zo'n document. Controleer de aantallen in de matchgeschiedenis voordat je de regel zelf wijzigt.
{% endhint %}

#### Kolomvergelijking (Matchcriteria)

Dit is de kerndefinitie van de logica van de regel, waarin wordt gespecificeerd welke velden tussen de documenten moeten overeenkomen.

1. Definiëren van de te vergelijken kolommen:
   * **PO-kolommen:** Het veld afkomstig uit de inkoopordergegevens (bijv. regelnr.).
   * **Geëxtraheerde tabelkolommen:** Het overeenkomstige veld geëxtraheerd of geparseerd uit het binnenkomende document (Factuur/Orderbevestiging) (bijv. `POSITION`).
2. **Vergelijkingstype:** Bepaalt de aard van de vereiste match (bijv. Tt voor Tekst/String vergelijking, die een exacte karakter-voor-karakter overeenkomst vereist; # voor Numerieke vergelijking).
3. **Tolerantie toestaan:** Voor numerieke velden (hoeveelheid, prijs) zorgt het inschakelen van deze optie ervoor dat het systeem de eerder gedefinieerde Globale Standaardtolerantie toepast. Als dit _niet_ is ingeschakeld voor een numeriek veld, moeten de waarden exact overeenkomen.
4. **Negeer bij handmatige match:** Indien aangevinkt wordt dit criterium versoepeld tijdens handmatige interventie. Dit is nuttig voor velden zoals omschrijvingen of interne referenties die licht kunnen variëren, waardoor de gebruiker kleine niet-kritieke afwijkingen kan negeren.

**Welke kolommen kunnen worden vergeleken**

| Kolom                           | Documentzijde                              | Inkooporderzijde                      | Opmerking                                                                                                                                                                                                                       |
| -------------------------------- | ------------------------------------------ | ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Regelnr.                       | `POSITION`                                 | `line_number`                        | Tekst, exact. Alleen nuttig wanneer de leverancier de orderregelnummer op het document afdrukt.                                                                                                                                  |
| Artikelidentificatie            | `ITEM_IDENTIFIER`                          | `item_identifier`                    | Tekst, exact. Artikelnummer of leverancier artikelnummer, ook via de [Leveranciersartikelnummerkaart](supplier-item-number-map-admin-documentation.md).                                                                           |
| Effectieve genormaliseerde hoeveelheid | `QUANTITY_EFFECTIVE_NORMALIZED`            | `quantity_effective_normalized`      | Numeriek. De hoeveelheid geselecteerd door **Match Hoeveelheid Op**, omgezet naar dezelfde eenheid aan beide zijden (eenheidscodeconversie, "per" hoeveelheden).                                                                   |
| Effectieve genormaliseerde eenheidsprijs | `UNIT_PRICE_EFFECTIVE_NORMALIZED`          | `unit_price_effective_normalized`    | Numeriek. De eenheidsprijs per enkele eenheid na kortingen en na **Eenheidsprijs Per** — en, als [Bereken PO eenheidsprijs](calculate-po-unit-price.md) aanstaat, de prijs berekend uit het orderregelbedrag en de hoeveelheid. |
| Nettobedrag                   | `NET_AMOUNT`                               | `total_amount`                       | Numeriek. Gebruikt door match-on-total regels.                                                                                                                                                                                 |

**Voorbeeld: Strenge PO-Matchregel (`DefaultRule#1`)**

Een typische strenge regel combineert verplichte identiteitscontroles met waardebepalingen:

* **Verplichte identiteit:** Regelnr. en Artikelidentificatie moeten exact overeenkomen (Tekstvergelijking, geen tolerantie).
* **Waardecontroles:** Effectieve genormaliseerde hoeveelheid en effectieve genormaliseerde eenheidsprijs moeten overeenkomen (Numerieke vergelijking, tolerantie toegestaan). Alleen als aan alle vier criteria wordt voldaan (met tolerantie voor waarden) wordt een automatische match uitgevoerd.

***

## De standaardregels

Elke organisatie begint met dezelfde standaardregels. Dit is een goede referentie bij het opbouwen van je eigen regels:

| Regel                       | Type / prioriteit                | Vergeleken kolommen                                                       | Activatievoorwaarde                                   |
| -------------------------- | ------------------------------ | ------------------------------------------------------------------------- | ---------------------------------------------------- |
| `DefaultRule#1`            | single match, prioriteit 1       | regelnr., artikelidentificatie, hoeveelheid (tol.), eenheidsprijs (tol.)  | altijd                                               |
| `DefaultMultiMatchRules#1` | multi match, prioriteit 1, fallback | artikelidentificatie, hoeveelheid (tol.), eenheidsprijs (tol.)          | `count(po_lines) > 1` en `count(table_lines) > 1`   |
| `DefaultTotalMatchRules#1` | match on total, prioriteit 1     | nettobedrag ↔ inkoopordertotaal (geen tolerantie)                        | `count(po_lines) >= 1` en `count(table_lines) > 1`  |
| `DefaultRule#2`            | single match, prioriteit 2, fallback | artikelidentificatie, hoeveelheid (tol.), eenheidsprijs (tol.)          | altijd                                               |
| `DefaultRule#3`            | single match, prioriteit 2, fallback | hoeveelheid (tol.), eenheidsprijs (tol.)                                | `count(po_lines) == 1` en `count(table_lines) == 1` |

Van boven naar beneden gelezen: eerst de strenge regel (regelnr. en artikel moeten op het document staan), dan de fallbacks zonder regelnr., dan een laatste redmiddel voor éénregelige documenten die alleen hoeveelheid en prijs vergelijkt.

***

## Impact op het PO Matching Proces

De gedefinieerde regels bepalen direct de efficiëntie en integriteit van de PO-matching workflow:

* **Prioritering en Fallbacks:** De gedefinieerde prioriteit zorgt ervoor dat het systeem eerst de meest betrouwbare matchmethode probeert. Als de strenge, hooggeprioriteerde regels falen, valt het systeem terug op bredere regels, met als doel het aantal uitzonderingen dat naar gebruikers wordt gestuurd te minimaliseren.
* **Beheersen van matchkwaliteit:** Strengere regels (die meer exacte overeenkomsten en minder tolerantie vereisen) resulteren in minder, maar zeer betrouwbare automatische matches. Lossere regels verhogen het automatische matchpercentage maar vergroten het risico op false positives.
* **Afhandeling van uitzonderingen (Handmatige match):** Door regels in te schakelen voor Handmatige match biedt het systeem gestructureerde opties voor gebruikers. Als een transactie niet voldoet aan de automatische matchcriteria, wordt het een uitzondering. De gebruiker kan dan proberen de uitzondering op te lossen door een vooraf gedefinieerde handmatige regel toe te passen, die versoepelde criteria kan hebben (bijv. het negeren van een kleine tekstafwijking volgens de instelling "Negeer bij handmatige match").

## Wat beïnvloedt het resultaat verder

* **Wanneer matching wordt uitgevoerd:** tijdens documentverwerking, wanneer een gebruiker op **Auto PO Match** klikt, en **bij elke opslag** waarbij het inkoopordernummer is gewijzigd of nog nooit eerder is opgezocht (bijvoorbeeld wanneer masterdata het na verwerking invult). Een opslag overschrijft nooit een bestaande match.
* **[Transformatie regels](../../transformation-rules.md)** worden vóór de match uitgevoerd en kunnen de regelitems wijzigen — en daarmee de regelaantallen waar de activatievoorwaarden naar kijken. Een tabelregel die de regels herbouwt behoudt een bestaande match zolang de regels hetzelfde blijven; als het gematchte regels vervangt, wordt de match verwijderd en wordt de naam van de regel als reden getoond.
* **[Bereken PO eenheidsprijs](calculate-po-unit-price.md)** verandert welke eenheidsprijs de regels aan de inkooporderzijde vergelijken.
* **[Tolerantie-instellingen](purchase-order-tolerance-settings-additional-purchase-order-tolerance.md)** en **[uitgeschakelde statussen](purchase-order-disable-statuses.md)** bepalen hoe strikt de vergelijking is en welke inkooporderregels überhaupt worden aangeboden.

## Probleemoplossing

| Symptom                                                           | Wat te controleren                                                                                                                                                                                |
| ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| "Geen match" hoewel elke waarde overeenkomt                      | Open de matchgeschiedenis: welke regel draaide, op welke kolom faalde het (de afwijking wordt per kolom getoond), werd de regel overgeslagen door een activatievoorwaarde?                         |
| Eenheidsprijs matcht niet precies met exact het belastingtarief  | Het inkoopordertotaal bevat belasting; schakel [Bereken PO eenheidsprijs](calculate-po-unit-price.md) in (netto bedrag eerst) of vergelijk het nettobedrag van de regel.                             |
| Een match-on-total regel wordt nooit uitgevoerd                   | De activatievoorwaarde vereist meer dan één documentregel. Stel `[[count(table_lines)]] >= 1` in of vouw de regels niet samen met een transformatie regel.                                         |
| De regels hebben helemaal geen effect                             | **PO match server side** is uitgeschakeld voor het documenttype, of de gewijzigde regels zijn nog een concept — activeer de versie.                                                                |

***

## Pas de PO Matchregels aan

Om de PO Matchregels te bewerken kan de standaardversie worden gekloond door te klikken op **"Configureer versiebeheer"** en gebruik te maken van de optie **"Kloon als concept"** uit de beschikbare kaartopties.

<figure><img src="../../../../../../.gitbook/assets/image (197).png" alt=""><figcaption></figcaption></figure>