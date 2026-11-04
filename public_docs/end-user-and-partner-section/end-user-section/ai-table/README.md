# AI Table

Met AI Table controleert u geëxtraheerde regels, corrigeert u kolommen en bewaart u instructies voor een leverancierslay-out. Kies de passende handleiding. Structured Output krijgt een eigen handleiding met Standaard/Ja/Nee, afwijkingen, voorbeeldweergave en een uitgewerkt voorbeeld.

* [Instellingen en sjabloonafwijkingen](configuration.md)
* [Structured Output voor tabellen](structured-output.md)
* [Kolommen en correcties](columns-and-corrections.md)
* [AI-instructies](ai-instructions.md)
* [AI Tabel Tags](ai-table-tags.md)
* [Extractie uitleggen en problemen onderzoeken](explain-extraction.md)
* [Assistent en rechten](assistant-and-permissions.md)

## Wanneer u de AI-tabel krijgt

* Een beheerder heeft **AI-tabel extractie** ingeschakeld (Instellingen → Documentverwerking → Classificatie en extractie, zie [Instellingen voor beheerders](#instellingen-voor-beheerders)). Als deze uitstaat, toont het tabelgebied *AI-tabel wordt hier weergegeven. Inschakelen in …*.
* Controleer leesbare tekst of de gekozen Vision-invoer. Opgeslagen klassieke regels kunnen nog steeds het gebruikte pad bepalen; controleer [welk extractiepad werkelijk is gebruikt](../../../overview-and-basics/faq/document-processing/which-extraction-path-was-used.md).
* Iedere kolom heeft een Use AI-keuze met drie toestanden. Controleer ook de werkelijke bron en leveranciersregels; Structured Output vervangt niet iedere tabel die uit regels komt.

Welke AI-tier de tabel leest (Fast, Full, Nexus) wordt per organisatie ingesteld en kan per leverancier worden overschreven, zie Leverancierspecifiek AI-model voor Veld- en Tabelextractie.

## De AI-tabel in één oogopslag

<figure><img src="../../../.gitbook/assets/ai-table-overview-nl.png" alt="AI-geëxtraheerde tabel met kolomkoppen en vier rijen"><figcaption><p>De twee tabbladen, de AI-geëxtraheerde tabel en de bijbehorende kolomkoppen.</p></figcaption></figure>

* **Tabbladen.** *AI-geëxtraheerde tabel* is wat de AI heeft gelezen. *Geëxtraheerde tabel* is de klassieke tabel uit getrainde regels. Het AI-tabblad wordt standaard geopend wanneer het document een AI-tabel heeft.
* **Kolomkop.** Elke kolom toont zijn naam, een klein **oorsprongssymbool** (houd de muisaanwijzer erop: *AI · kaartweergave*, *AI · synoniem* en dergelijke vertellen u hoe de AI de kolom heeft gekoppeld), een **menu met drie puntjes** en, bij een gekoppelde kolom, een **naamknop** waarmee u kunt wijzigen om welke kolom het gaat.
* **Rijknoppen.** Het **x** aan het begin van een rij verwijdert die rij. Klik met de rechtermuisknop op een rij voor *Selecteer als extra kosten* / *Verwijderen als extra kosten*.
* **Werkbalk onderaan.** De pictogrammen onderaan het scherm voegen kolommen en rijen toe of verbergen ze, zie [Werkbalk onderaan](#werkbalk-onderaan).
* **Kaart Instructies voor de AI** onder de tabel: prompt, extra kolommen, **Test wijziging**, **Toepassen**, **Opslaan als training**, **Verwijderen**, **Exporteren**, zie [Geef de AI instructies](#geef-de-ai-instructies).

{% hint style="info" %}
De kolomfuncties werken alleen wanneer u het document kunt bewerken. Als ze grijs zijn, is het document alleen-lezen of in een andere sessie vergrendeld. Als de rode banner meldt dat het document door uw eigen gebruiker in een andere sessie is vergrendeld, neemt **Ontgrendelen** de vergrendeling over.
{% endhint %}


## Instellingen voor beheerders

Lees hier verder: [Instellingen en sjabloonafwijkingen](configuration.md).

### AI gebruiken per kolom

Lees hier verder: [Structured Output voor tabellen](structured-output.md).

<a id="de-juiste-kolom-kiezen-herkoppelen"></a>
<a id="het-menu-met-drie-puntjes"></a>
<a id="werkbalk-onderaan"></a>

## Een kolom wijzigen

Lees hier verder: [Kolommen en correcties](columns-and-corrections.md).

<a id="voorstellen-met-nexus"></a>
<a id="testen-toepassen-opslaan-wat-elke-knop-doet"></a>

## Geef de AI instructies

Lees hier verder: [AI-instructies](ai-instructions.md).


## Zien wat de AI heeft gedaan

Lees hier verder: [Extractie uitleggen en problemen onderzoeken](explain-extraction.md).


## Praktische voorbeelden

Lees hier verder: [Extractie uitleggen en problemen onderzoeken](explain-extraction.md).

<a id="een-regel-voorstellen-aan-uw-beheerder"></a>

## De Assistent en de AI-tabel

Lees hier verder: [Assistent en rechten](assistant-and-permissions.md).


## Wie kan wat doen

Lees hier verder: [Assistent en rechten](assistant-and-permissions.md).

## Gerelateerde pagina's

* [AI Tabel Tags](ai-table-tags.md)
* [Training Line Fields/Tabel Training](../../../administration-and-setup/setup/document-training/training-line-fields-table-training/README.md)
* [Touchless Intelligence](../../../administration-and-setup/touchless-intelligence.md)
