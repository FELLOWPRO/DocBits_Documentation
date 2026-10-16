---
description: Hoe PowerBI te configureren
---

# Verbinden via ClickHouse

Deze gids begeleidt u bij het verbinden van **ClickHouse** met **Power BI Desktop** met behulp van de **ODBC-driver**. Het behandelt driverinstallatie, ODBC-configuratie, Power BI-integratie en het instellen van gegevensvernieuwing.

{% embed url="https://youtu.be/O1MtuXf_R_M" %}

#### 1. Installeer de ClickHouse ODBC-driver

* Download de nieuwste **ClickHouse ODBC-driver** van:
  * [ClickHouse GitHub - clickhouse-odbc](https://github.com/ClickHouse/clickhouse-odbc)
* Voer het installatieprogramma uit en volg de installatiewizard.

#### 2. Configureer de ODBC-gegevensbron

* Open **ODBC-gegevensbronbeheer (64-bits)** via Configuratiescherm of Windows Zoeken.
* Ga naar het tabblad **Systeem DSN** en klik op **Toevoegen**.
* Selecteer **ClickHouse ODBC Driver** uit de lijst en klik op **Voltooien**.
*   Vul de vereiste velden in. U kunt de benodigde informatie vinden in:

    **DocBits** → **Instellingen** → **Documentverwerking** → **Module** → **AI Dashboard** → **ClickHouse Direct Access**

    <figure><img src="../../.gitbook/assets/image (440).png" alt=""><figcaption></figcaption></figure>

    **Vereiste Velden:**

    * **Naam**: Een naam voor de verbinding (bijv. `ClickHouse_Prod`)
    * **Beschrijving**: Een korte beschrijving voor uw referentie (optioneel)
    * **Host**: Kopieer de hostwaarde uit DocBits
    * **Poort**: Kopieer de poortwaarde uit DocBits
    * **Database**: Kopieer de databasenaam uit DocBits
    * **Gebruikersnaam**: Kopieer de gebruikersnaam uit DocBits
    * **Wachtwoord**: Kopieer het wachtwoord uit DocBits

#### 3. Verbind ClickHouse met Power BI

* Open **Power BI Desktop**.
* Selecteer **Gegevens ophalen** → **ODBC** → **Verbinden**.
* Selecteer uit de DSN-lijst uw geconfigureerde bron (bijv. `ClickHouse_Prod`).
* Klik op **OK**. Voer inloggegevens opnieuw in indien gevraagd.

#### 4. Gegevens Laden en Transformeren

* In het deelvenster **Navigator**, blader en selecteer de tabellen of weergaven om te importeren.
* Kies:
  * **Laden**: om direct te importeren
  * **Gegevens Transformeren**: om Power Query te openen voor gegevensvormgeving

#### 5. Visualiseer Uw Gegevens

* Gebruik het rapportcanvas om visualisaties te bouwen.
* Sleep velden, voeg slicers toe, kies grafiektypen en gebruik **DAX**-expressies indien nodig.
* Gebruik **Power Query Editor** om uw ClickHouse-gegevens op te schonen of te draaien voordat u visuals bouwt.
* PowerBI documentatie: [https://learn.microsoft.com/en-us/power-bi/](https://learn.microsoft.com/en-us/power-bi/)

#### 6. Schakel Geplande Vernieuwing In (Optioneel)

<mark style="color:red;">**Opmerking:**</mark> **Vereist Power BI Pro of Premium + Gateway**

* Om uw rapporten gesynchroniseerd te houden met ClickHouse:
* Publiceer uw `.pbix`-bestand naar **Power BI Service**.
* Installeer de **Power BI Gateway** (Standaardmodus) op een machine met netwerktoegang tot ClickHouse.
* In Power BI Service:
  * Ga naar uw dataset → **Instellingen** → **Geplande Vernieuwing**
  * Wijs uw DSN toe en geef inloggegevens op
* Meer informatie [hier](https://learn.microsoft.com/en-us/power-bi/connect-data/service-gateway-deployment-guidance).

#### 7. Voorbeelddashboards & Gegevensweergaven
