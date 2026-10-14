# Stamgegevens opzoeken

{% embed url="https://youtu.be/hn_bkeUMxJg" %}
{% endembed %}

Met **Stamgegevens opzoeken** (zijbalk: **Lookup Master Data**) kunt u de stamgegevens bekijken en beheren die DocBits gebruikt om uit documenten geëxtraheerde gegevens te valideren tegen uw ERP-systeem. Dit is essentieel voor nauwkeurige PO matching, leveranciersvalidatie en het automatisch invullen van velden. Open de pagina via **Instellingen → Documentverwerking → Lookup Master Data**.

<figure><img src="../../../.gitbook/assets/master_data_lookup_overview.png" alt="Stamgegevens opzoeken"><figcaption><p>Pagina Stamgegevens opzoeken – gegevensbronnen en de gegevenstabel</p></figcaption></figure>

## Gegevensbronnen

Het linkerpaneel toont vier categorieën gegevensbronnen:

| Bron | Beschrijving |
|------|--------------|
| **BOD Input Data** | Gegevens die via Infor-BOD-berichten (Business Object Document) worden ontvangen. |
| **ERP API Data** | Gegevens die rechtstreeks via een API uit uw ERP-systeem worden opgehaald. Klik op het tandwielpictogram om de API-verbinding te configureren. |
| **Imported** | Handmatig geïmporteerde gegevens (bijvoorbeeld via een CSV-upload). Klik op het **+**-pictogram om nieuwe gegevens toe te voegen. |
| **DocBits Master Data** | Interne stamgegevens die binnen DocBits worden beheerd. |

## Gegevenstabel

Wanneer u een gegevensbron selecteert, worden de bijbehorende gegevens rechts geopend in een doorzoekbare, sorteerbare tabel:

* **Tabbladen** – elk tabblad is een type stamgegevens (bijvoorbeeld Leverancier, Inkooporder, Artikel).
* **Zoeken** – filter op kolom (**Search by column**) of zoek op tekst (**Search String**).
* **Acties** – kolomlabels bijwerken, lege kolommen verbergen, aliassen bijwerken of de gegevens als CSV downloaden.
* **Paginering** – navigeer met de paginabesturingselementen door grote gegevenssets.

De tabellen Leverancier en Inkooporder bevatten kolommen zoals Leverancier-ID, Leveranciersnaam, Adres, Bank Id, PO-nummer, Artikel-ID, Omschrijving, Aantal, Eenheidsprijs, Totaalbedrag, Valuta en Status, plus eventuele aangepaste velden.

## Instellingen

Klik linksonder in het gegevensbronnenpaneel op **Settings** (tandwielpictogram) om de stamgegevens-instellingen te openen.

<figure><img src="../../../.gitbook/assets/master_data_lookup_settings.png" alt="Instellingen voor Stamgegevens opzoeken"><figcaption><p>Instellingen voor Supplier BOD en het verwijderen van inkooporders</p></figcaption></figure>

### Supplier BOD

**Allow Multiple Supplier Accounts Sync**

* **Ingeschakeld**: een enkele leverancier kan meerdere `<FinancialParty>`-elementen in de BOD hebben (vaak vanwege meerdere IBAN's of financiële rekeningen). Alle `<FinancialParty>`-vermeldingen worden geëxtraheerd en opgeslagen in de leverancierstabel, zodat meerdere financiële attributen kunnen worden opgeslagen.
* **Uitgeschakeld**: alleen het laatst gevonden `<FinancialParty>`-element voor de leverancier wordt geëxtraheerd. Eerdere financiële attributen (bijvoorbeeld extra IBAN's) worden genegeerd en alleen de gegevens van het laatste voorkomen worden opgeslagen.

### Purchase Order Deletion Assistant

**Delete Purchase Order After** – kies wanneer afgesloten inkooporders moeten worden verwijderd. Na de geselecteerde periode worden de records automatisch verwijderd.

{% hint style="info" %}
Lees hoe u stamgegevens in DocBits laadt onder [Stamgegevens importeren](../../../infor-integration-and-configuration/importing-customer-master-data/).
{% endhint %}
