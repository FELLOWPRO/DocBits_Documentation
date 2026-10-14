---
# SQL Access

<figure><img src="../../.gitbook/assets/sql_direct_access_settings.png" alt="Instellingen voor SQL Direct Access"><figcaption></figcaption></figure>

## Overzicht

In de instellingenmodule van DocBits kunnen beheerders rechtstreeks met SQL toegang krijgen tot de BI-database. Deze functie is bedoeld voor geavanceerd gegevensbeheer en aangepaste rapportagebehoeften.

### Toegang tot SQL Direct Access

Ga in de instellingenmodule naar de sectie SQL Direct Access. Hier vindt u de inloggegevens en toegangsdetails, waaronder gebruikersnaam, wachtwoord, databasenaam en hostinformatie.

* **Gebruikersnaam:** user\_23f3d6
* **Wachtwoord:** _Versleuteld_
* **Database:** demo
* **Host:** zie de schermafbeelding

## **Voorbeeld van toegangsgegevens:**

```sql
SELECT
    COUNT(*),
    status,
    invoice_type
FROM dashboard
GROUP BY
    status,
    invoice_type

```

#### Resultaten van een voorbeeldquery

De volgende resultaten tonen het aantal documenten per status en factuurtype:

* **Ready for Validation:** 71 facturen, 6 ongespecificeerd
* **Pending Confirmation:** 1 ongespecificeerd
* **Finished:** 3 ongespecificeerd, 1 factuur
* **Error:** 2 ongespecificeerd

#### clickhouse-client gebruiken voor toegang via de terminal

Voor ontwikkelaars die liever de terminal gebruiken, kan toegang worden gemaakt via `clickhouse-client`:

```bash
clickhouse-client --host <hostname_or_ip> --port <port> --user <username> --password <your_password> --database <database_name>

```

### Materialized views aanmaken

We raden aan materialized views aan te maken om gegevens vooraf te berekenen en zo de prestaties in analysetools zoals PowerBI te verbeteren:

```sql
SELECT toStartOfWeek(created_on) as week_start, sum(toFloat64OrZero(field_value)) as total_sum
FROM document_extracted_data
WHERE field_name = 'total_amount'
GROUP BY week_start

```

Dit voorbeeld laat zien hoe u totaalbedragen groepeert per week waarin ze zijn aangemaakt, wat handig is voor wekelijkse financiële overzichten of audittrails.

## Aanvullende bronnen

Neem voor verdere hulp of geavanceerde configuraties contact op met ons supportteam of bekijk onze uitgebreide videotrainingen in het helpgedeelte.
