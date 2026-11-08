# AI Model

## Overzicht

Met de instelling **AI Model** bepaalt u welk AI-model standaard wordt gebruikt voor **veldextractie** en **tabelextractie** tijdens de documentverwerking.\
Gebruik de huidige modelkiezer en de tabel met sjabloonvoorkeuren om de organisatie-instelling en de overrides te beoordelen. Raadpleeg voor kosten de informatie in uw omgeving en uw abonnementsvoorwaarden.

## Zo opent u het

1.  Ga naar **Settings** → **Document Types** → **Classification and Extraction** → **General**

    <figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/site-complete-global-ai-model-options-en.png" alt="Huidige extractie-instellingen en het menu AI Model: Full, Fast, Nexus, Nexus Flash, Auto en Auto Nexus. Waarden van de privétabel zijn afgeschermd; er is geen model geselecteerd en geen voorkeur verwijderd."><figcaption><p>Huidige extractie-instellingen en het menu AI Model: Full, Fast, Nexus, Nexus Flash, Auto en Auto Nexus. Waarden van de privétabel zijn afgeschermd; er is geen model geselecteerd en geen voorkeur verwijderd.</p></figcaption></figure>
2.  Vouw **Extraction** uit en zoek de instelling **AI Model**.



## AI-modelopties

Het huidige menu biedt **Full**, **Fast**, **Nexus**, **Nexus Flash**, **Auto** en **Auto Nexus**. Dit zijn namen van productniveaus. Beschikbare opties, onderliggende modellen en tokenkosten kunnen veranderen; controleer de informatie in uw huidige omgeving en uw abonnementsvoorwaarden in plaats van te vertrouwen op een historische naam van een providermodel of een vaste prijs.

<figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/dbdc-3-six-model-options-en-20261031.png" alt="Huidige dropdown AI Model met Full, Fast, Nexus, Nexus Flash, Auto en Auto Nexus"><figcaption><p>Detail van de zes extractieniveaus in het huidige ontwikkelmenu. Openen en sluiten van het menu liet de bestaande selectie ongewijzigd.</p></figcaption></figure>

| Optie | Wat u met representatieve documenten controleert |
| --- | --- |
| **Full** | Extractieresultaten bij complexe lay-outs, verwerkingstijd en kosten. |
| **Fast** | Resultaten en verwerkingstijd bij dagelijkse documenten; de naam is geen garantie voor elk document. |
| **Nexus** | Vergelijk deze alternatieve optie met dezelfde documentselectie. |
| **Nexus Flash** | Controleer zowel kwaliteit als latentie op uw werkelijke lay-outs. |
| **Auto** | Controleer de resultaten en kosten van automatische selectie. |
| **Auto Nexus** | Controleer de resultaten en kosten van de automatische selectie van Nexus. |

Als het huidige extractiesjabloon geen override heeft, valt de modelinstelling terug op de configuratie van de organisatie. Een niet-ingestelde leveranciersspecifieke waarde betekent niet automatisch Fast. Vergelijk een vaste steekproef voordat u van model wisselt; een modelwissel alleen garandeert geen veldvalidatie, PO-afstemming, goedkeuring of succesvolle export.



## Tabel met AI-modeltoewijzing

Het **validatiescherm** biedt een ingang voor een leveranciersspecifiek model. De override wordt opgeslagen voor de organisatie en het huidige extractiesjabloon (`tfidf_id`); het werkt niet zonder meer elk sjabloon of historisch document van dezelfde leverancier bij.\
\
Zie voor meer informatie de bijbehorende documentatie [hier](../../../../end-user-and-partner-section/end-user-section/validation-screen/supplier-specific-ai-model-for-field-and-table-extraction.md).

De toewijzingstabel vat sjabloongerelateerde extractievoorkeuren samen. De kolommen verschillen per productversie; gebruik de huidige koppen om leverancierskoppeling, model, extractieopties en auditinformatie te bekijken:

* **Supplier ID** – De unieke identificatie van de leverancier
* **AI Model** – Het niveau dat voor dit sjabloonitem is ingesteld
* **Use Structured Extraction (AI)**, indien aanwezig – De voorkeur voor gestructureerde extractie van dit item
* **E-Text** – Geeft aan of de functie E-Text is ingeschakeld
* **Created By / Modified By / Created On / Modified On** – Wie het item heeft ingesteld en wanneer
* **Action** – Bevat de optie om het item te verwijderen



### Item verwijderen – sjabloonoverrides verwijderen

Voordat een beheerder een item verwijdert, moet hij het bijbehorende extractiesjabloon en alle voorkeuren daarin vaststellen. Verwijderen kan meerdere overrides van het sjabloon weghalen, niet alleen de modelinstelling:

1.  Klik in de kolom **Action** naast het leveranciersitem op de drie puntjes en kies **Delete**.


2.  Er verschijnt een bevestigingsdialoog — bevestig dat u het item wilt verwijderen.



Na het verwijderen leest de verdere verwerking de geldende organisatieconfiguratie en terugvalwaarden voor dit sjabloon. Andere sjablonen van dezelfde leverancier kunnen eigen overrides behouden. Verwijderen verwerkt historische documenten niet automatisch opnieuw. Voor deze handleiding is geen item verwijderd en is geen daaruit volgende extractie uitgevoerd.

## Instellingen en overrides

Structured Output heeft een eigen organisatie-/sjablooninstelling, los van het modelniveau. Wijzig die onder More options bij het document; bevestiging slaat de override op en start dat document opnieuw. De indicatoren in de instellingenlijst zijn alleen-lezen. Het verwijderen van een voorkeursitem kan meerdere overrides tegelijk weghalen. [Structured Output voor tabellen](../../../../end-user-and-partner-section/end-user-section/ai-table/structured-output.md).
