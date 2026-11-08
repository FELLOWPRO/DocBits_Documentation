# Appearance

Met **Appearance** kan een beheerder de DocBits-omgeving van de organisatie een eigen uiterlijk geven: kleuren, hoekradius, dichtheid en lettertype. Iedereen in de organisatie ziet het resultaat — in lichte en donkere modus — na de volgende herlaadbeurt. De lay-out en wat een functie doet veranderen nooit, alleen hoe het wordt weergegeven.

> **Toegang:** Appearance is een pagina die alleen voor beheerders is. Open **Settings → Organization & Access → Appearance**.

<!-- screenshot: /settings/appearance light -->

## Wie het kan wijzigen

Alleen organisatiebeheerders kunnen **Settings → Appearance** openen en een thema opslaan of resetten. Alle anderen in de organisatie zien alleen het resultaat.

## Wat er op de pagina staat

De pagina is verdeeld in een editor links en een live voorbeeld rechts.

| Onderdeel | Wat het bevat |
|---|---|
| **General** | De naam van het thema, het lettertype, de hoekradius en de dichtheid. |
| **Colors** | De tabbladen Light en Dark, per kleur een kleurkiezer plus een hex-veld, gegroepeerd in Surfaces, Brand, Neutrals, Status en Charts. Een alleen-lezen paneel 'Derived colours' eronder toont kleuren die DocBits voor u berekent (hover-toestanden, focusringen en dergelijke) op basis van de kleuren hierboven. |
| **Advanced overrides** | Eén regel `--token: value` per item, voor het zeldzame geval dat de bedieningselementen voor kleur, radius, dichtheid en lettertype hierboven niet toereikend zijn — zie [Advanced overrides](#advanced-overrides). |

### Kleuren wijzigen

Elke kleur heeft een kleurvak (klik erop om de kleurkiezer van uw browser te openen) en daarnaast een hex-veld waarin u kunt typen of plakken. Laat een kleur leeg om de DocBits-standaard voor dat token te behouden — het kleurvak toont dan een gestippelde rand. Schakel boven de kleurenlijst tussen de tabbladen **Light** / **Dark** om de andere modus in te stellen; een kleur die u in donkere modus niet instelt, behoudt zijn eigen DocBits-standaard voor donker en neemt de lichte waarde niet over.

{% hint style="info" %}
Kleuren worden als hex ingevoerd (`#2388ae` of `#2388aeaa` met alpha). Er is geen invoer voor kleurnamen of `rgb()`.
{% endhint %}

### Hoekradius, dichtheid en lettertype

* **Corner radius** — `None`, `Small`, `Medium` (standaard), `Large` of `Extra large`. Bepaalt hoe rond kaarten, buttons, invoervelden en dialoogvensters in de hele app zijn.
* **Density** — `Compact`, `Comfortable` (standaard) of `Spacious`. Bepaalt de hoogte van buttons, invoervelden en tabelrijen en de basistekstgrootte.
* **Font** — een korte lijst meegeleverde lettertypen (Geist is de DocBits-standaard; ook Inter, Roboto, IBM Plex Sans, Source Sans 3, Nunito Sans, Manrope, Kanit of het systeemlettertype van de bezoeker). Elk lettertype is al meegeleverd, er hoeft niets te worden geüpload.

### Advanced overrides

Voor een design token dat de bedieningselementen hierboven niet rechtstreeks aanbieden (bijvoorbeeld een specifieke rijhoogte in een tabel) voegt u een regel toe onder **Advanced overrides**:

```
--table-row-h: 30px
```

Eén override per regel, `--token: value`. Een ongeldige regel — een onbekend token, een token dat niet kan worden aangepast, of een waarde die niet past bij wat het token verwacht — wordt onder het vak als fout gemeld en niet toegepast; al het andere op de pagina wordt gewoon opgeslagen.

## Voorbeeld

Elke wijziging werkt het paneel **Preview** rechts meteen bij, zonder te beïnvloeden wat anderen zien — het raakt nooit de actieve app of het opgeslagen thema. Het voorbeeld heeft eigen tabbladen: een overzicht met licht en donker naast elkaar, en daarna aparte pagina's met buttons, formuliervelden, oppervlakken en statusindicatoren, zodat u contrast en leesbaarheid kunt controleren in de delen van de interface die het gevoeligst zijn voor kleur.

<!-- screenshot: /settings/appearance dark -->

Maakt een wijziging het thema ongeldig (zie hieronder), dan blijft het voorbeeld de laatst geldige versie tonen in plaats van te breken.

## Opslaan en resetten

* **Save** schrijft het thema voor de hele organisatie. De knop is grijs totdat er echt iets is gewijzigd en het thema geldig is.
* **Reset** vraagt om bevestiging en verwijdert daarna het thema van de organisatie volledig; iedereen keert terug naar het DocBits-standaardthema. Dit kan op de pagina niet ongedaan worden gemaakt — de kleuren moeten handmatig opnieuw worden ingevoerd (of opnieuw geïmporteerd, zie hieronder) als de organisatie ze terug wil.
* Een mislukte opslag of reset (bijvoorbeeld door een validatieprobleem) toont het probleem boven de editor en laat de pagina zoals die was; er wordt niets toegepast.

Er zijn geen contrastcontroles vóór het opslaan — zie [Tips](#tips) hieronder.

## Exporteren en importeren

* **Export** downloadt het thema dat nu in de editor wordt getoond (opgeslagen of niet) als `.json`-bestand, vernoemd naar het thema.
* **Import** leest een `.json`-themabestand en laadt het in de editor. Het moet nog steeds worden beoordeeld en opgeslagen om effect te hebben — importeren alleen verandert niet wat iemand ziet. Een ongeldig of te groot bestand (meer dan 32 KB) wordt met een fout geweigerd en er verandert niets.

Exporteren is een handige manier om een thema te bewaren voordat u gaat experimenteren, of om het uiterlijk van de ene organisatie naar de andere te kopiëren.

## Wat gebruikers zien

Na het opslaan geldt het thema voor de hele applicatie — elke pagina, in lichte en donkere modus — voor elk lid van de organisatie, na de volgende herlaadbeurt (niet meteen voor andere open sessies). Een gebruiker die de organisatie nog nooit heeft geladen, ziet de DocBits-standaard totdat de instellingen van de organisatie één keer zijn geladen; daarna neemt het thema het over.

Resetten brengt iedereen bij de volgende herlaadbeurt terug naar het DocBits-standaarduiterlijk, precies alsof er nooit een organisatiethema is ingesteld.

## Tips

* **Controleer het contrast in beide modi.** De editor waarschuwt niet voor combinaties met weinig contrast (bijvoorbeeld een lichte merkkleur met lichte tekst). Gebruik de lichte en donkere panelen van het voorbeeld om te controleren of tekst leesbaar blijft voordat u opslaat.
* **Laat statuskleuren met rust, tenzij u een reden hebt ze te wijzigen.** Destructive (fouten), success, warning en info behouden hun betekenis in de hele app — ze wijzigen kan ervoor zorgen dat een fout op het eerste gezicht op een succes lijkt. Wijzig de merkkleur en laat statuskleuren op hun standaardwaarde, tenzij de organisatie meer nodig heeft dan het gebruikelijke rood/groen/amber/blauw.
* **Begin met een volledig palet.** Het huidige thema exporteren of beginnen vanaf de DocBits-standaard geeft elke basiskleur een waarde om van te bewerken, in plaats van te raden welke tokens bestaan.
* **Een themawijziging geldt voor elke gebruiker in de organisatie, meteen bij de volgende herlaadbeurt.** Er is geen stap waarin u het voorbeeld alleen aan een deel van de gebruikers laat zien; test het resultaat zelf in licht en donker voordat u het team zegt dat het klaar is.
