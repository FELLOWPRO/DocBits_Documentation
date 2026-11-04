# Verbinding maken via Alleen-lezen Database

Deze handleiding leidt u door het verbinden van de **Alleen-lezen Database van DocBits met Power BI Desktop** met behulp van de **PostgreSQL ODBC-stuurprogramma**. Het behandelt stuurprogramma-installatie, ODBC-configuratie, Power BI-integratie en geplande vernieuwing.

{% embed url="https://youtu.be/O1MtuXf_R_M" %}
{% endembed %}


### 1. Installeer de PostgreSQL ODBC-stuurprogramma

* Download het nieuwste PostgreSQL ODBC-stuurprogramma (**psqlODBC**) van de officiële site:
  * [https://www.postgresql.org/ftp/odbc/releases/](https://www.postgresql.org/ftp/odbc/releases/)
* Voer de installatie uit en volg de installatiewizard.

### 2. Configureer de ODBC-gegevensbron

* Open **ODBC-gegevensbronbeheerder (64-bits)** via het Configuratiescherm of Windows Zoeken.
* Ga naar het tabblad **Systeem-DSN** en klik op **Toevoegen**.
* Selecteer de **PostgreSQL Unicode(x64)** stuurprogramma uit de lijst en klik op **Voltooien**.
* Vul de vereiste velden in met referenties van: **DocBits → Instellingen → Documentverwerking → Module → AI-dashboard → Alleen-lezen DB-toegang**

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FupCHowPUuMJ8hO9Y36EY%252Fconnect_read_only_4.png%3Falt%3Dmedia%26token%3D3eb69744-6696-41e2-90be-63295b9b6f6d\&width=768\&dpr=4\&quality=100\&sign=647db68c\&sv=2)

**Vereiste velden:**

* **Naam:** Een naam voor de verbinding (bijv., `Sandbox-Read_Only`)
* **Server:** Kopieer de hostwaarde van DocBits
* **Poort:** Kopieer de poortwaarde van DocBits
* **Database:** Kopieer de databasenaam van DocBits
* **Gebruikersnaam:** Kopieer de gebruikersnaam van DocBits
* **Wachtwoord:** Kopieer het wachtwoord van DocBits
* **SSL-modus:** Instellen op **Vereisen** (zorgt voor versleutelde communicatie)

### 3. Verbind Alleen-lezen DB met Power BI

* Open **Power BI Desktop**.
*   Selecteer **Gegevens ophalen** → **ODBC** → **Verbinden**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F1aIDfi4Rj6WD9oXsvUjt%252FScreenshot%25202025-05-19%2520163621.png%3Falt%3Dmedia%26token%3D4ec15da7-fa79-4b9e-a83b-cb4b0a545cfd\&width=768\&dpr=4\&quality=100\&sign=59fba2e3\&sv=2)
* Selecteer uit de DSN-lijst uw geconfigureerde bron (bijv., `Sandbox-Read_Only`).

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FKPDLjfDw2SRYvzvFKWXq%252Fconnect_read_only_3.png%3Falt%3Dmedia%26token%3Dc67c1362-7f63-479e-a373-974d198f5eb7\&width=768\&dpr=4\&quality=100\&sign=f001e759\&sv=2)

* Klik op **OK**. Voer indien gevraagd opnieuw referenties in.
  * **Opmerking:** Als u de foutmelding **“wachtwoordverificatie mislukt voor gebruiker”** ziet, probeer dan uw wachtwoord in te voeren tussen **accolades** `**{}**`.

### 4. Gegevens laden en transformeren

* In het **Navigator**-paneel, breid de schemalijst uit.
* Open het `**public**` schema.
* Selecteer de tabellen die u wilt importeren.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FSmtEspL1H6ieOJhtDwYb%252Fconnect_read_only_1.png%3Falt%3Dmedia%26token%3Dd402a928-175e-4904-bd21-592ff114fad7\&width=300\&dpr=4\&quality=100\&sign=464e3a3d\&sv=2) ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F3Phea1Pf3ZBJtMzw3rxi%252Fconnect_read_only_2.png%3Falt%3Dmedia%26token%3D94037886-57e3-440d-bf08-61cd37c65b98\&width=300\&dpr=4\&quality=100\&sign=5ead9fe9\&sv=2)

* Kies:
  * **Laden** → Direct importeren in Power BI
  * **Gegevens transformeren** → Open Power Query voor vormgeving en filteren voordat u laadt

### 5. Visualiseer uw gegevens

* Gebruik het Power BI-rapportcanvas om dashboards te bouwen.
* Sleep velden, voeg slicers toe, kies diagramtypen en pas DAX-berekeningen toe.
* Gebruik **Power Query Editor** om gegevens schoon te maken of te koppelen voordat u visuals maakt.
* Referentie: [Power BI-documentatie](https://learn.microsoft.com/en-us/power-bi/?utm_source=chatgpt.com)

### 6. Geplande vernieuwing inschakelen (Optioneel)

**Opmerking:** **Vereist Power BI Pro of Premium + Gateway**

* Om uw rapporten gesynchroniseerd te houden met ClickHouse:
* Publiceer uw `.pbix`-bestand naar **Power BI Service**.
* Installeer de **Power BI Gateway** (Standaardmodus) op een machine met netwerktoegang tot ClickHouse.
* In Power BI Service:
  * Ga naar uw dataset → **Instellingen** → **Geplande vernieuwing**
  * Koppel uw DSN en verstrek referenties
* Meer informatie [hier](https://learn.microsoft.com/en-us/power-bi/connect-data/service-gateway-deployment-guidance).

### 7. Voorbeelddashboards & Gegevensweergaven

![](<../../.gitbook/assets/example_4 (1).avif>)![](<../../.gitbook/assets/example_3 (1).avif>)![](<../../.gitbook/assets/example_2 (1).avif>)![](<../../.gitbook/assets/example_1 (1).avif>)
