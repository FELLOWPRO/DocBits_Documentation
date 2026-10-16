# Verbinden via Alleen-Lezen Database

Deze gids begeleidt u bij het verbinden van **DocBits' Alleen-Lezen Database met Power BI Desktop** met behulp van de **PostgreSQL ODBC-driver**. Het behandelt driverinstallatie, ODBC-configuratie, Power BI-integratie en geplande vernieuwing.

{% embed url="https://youtu.be/O1MtuXf_R_M" %}
{% endembed %}


#### 1. Installeer de PostgreSQL ODBC-driver

* Download de nieuwste PostgreSQL ODBC-driver (**psqlODBC**) van de officiële site:
  * [https://www.postgresql.org/ftp/odbc/releases/](https://www.postgresql.org/ftp/odbc/releases/)
* Voer het installatieprogramma uit en volg de installatiewizard.

#### 2. Configureer de ODBC-gegevensbron

* Open **ODBC-gegevensbronbeheer (64-bits)** via Configuratiescherm of Windows Zoeken.
* Ga naar het tabblad **Systeem DSN** en klik op **Toevoegen**.
* Selecteer **PostgreSQL Unicode(x64)** driver uit de lijst en klik op **Voltooien**.
* Vul de vereiste velden in met inloggegevens van:\
  **DocBits → Instellingen → Documentverwerking → Module → AI Dashboard → Alleen-Lezen DB Toegang**

<figure><img src="../../.gitbook/assets/connect_read_only_4.png" alt=""><figcaption></figcaption></figure>

**Vereiste Velden:**

* **Naam:** Een naam voor de verbinding (bijv. `Sandbox-Read_Only`)
* **Server:** Kopieer de hostwaarde uit DocBits
* **Poort:** Kopieer de poortwaarde uit DocBits
* **Database:** Kopieer de databasenaam uit DocBits
* **Gebruikersnaam:** Kopieer de gebruikersnaam uit DocBits
* **Wachtwoord:** Kopieer het wachtwoord uit DocBits
* **SSL-modus:** Stel in op **Require** (zorgt voor versleutelde communicatie)

#### 3. Verbind Alleen-Lezen DB met Power BI

* Open **Power BI Desktop**.
*   Selecteer **Gegevens ophalen** → **ODBC** → **Verbinden**.

    <figure><img src="../../.gitbook/assets/Screenshot 2025-05-19 163621.png" alt=""><figcaption></figcaption></figure>
* Selecteer uit de DSN-lijst uw geconfigureerde bron (bijv. `Sandbox-Read_Only`).

<figure><img src="../../.gitbook/assets/connect_read_only_3.png" alt=""><figcaption></figcaption></figure>

* Klik op **OK**. Voer inloggegevens opnieuw in indien gevraagd.
  * <mark style="color:red;">**Opmerking:**</mark> Als u de fout **“wachtwoordverificatie mislukt voor gebruiker”** ziet, probeer dan uw wachtwoord in te voeren verpakt in **accolades `{}`**.

#### 4. Gegevens Laden en Transformeren

* In het deelvenster **Navigator**, vouw de schemalijst uit.
* Open het **`public`** schema.
* Selecteer de tabellen die u wilt importeren.

![](../../.gitbook/assets/connect_read_only_1.png)        ![](../../.gitbook/assets/connect_read_only_2.png)

* Kies:
  * **Laden** → Importeer direct in Power BI
  * **Gegevens Transformeren** → Open Power Query voor vormgeven en filteren vóór laden

#### 5. Visualiseer Uw Gegevens

* Gebruik het Power BI-rapportcanvas om dashboards te bouwen.
* Sleep velden, voeg slicers toe, kies grafiektypen en pas DAX-berekeningen toe.
* Gebruik **Power Query Editor** om gegevens op te schonen of samen te voegen voordat u visuals maakt.
* Referentie: [Power BI Documentatie](https://learn.microsoft.com/en-us/power-bi/?utm_source=chatgpt.com)

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

<div><figure><img src="../../.gitbook/assets/Screenshot 2025-05-13 at 12.23.07.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/Screenshot 2025-05-13 at 12.23.17.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/Screenshot 2025-05-13 at 12.23.26.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/Screenshot 2025-05-13 at 12.23.34.png" alt=""><figcaption></figcaption></figure></div>