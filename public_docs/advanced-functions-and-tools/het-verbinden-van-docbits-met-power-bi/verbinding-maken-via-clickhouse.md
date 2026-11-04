# Verbinding maken via ClickHouse

Deze handleiding leidt u door het verbinden van **ClickHouse** met **Power BI Desktop** met behulp van de **ODBC-stuurprogramma**. Het behandelt stuurprogramma-installatie, ODBC-configuratie, Power BI-integratie en het instellen van gegevensverversing.

{% embed url="https://youtu.be/O1MtuXf_R_M" %}
{% endembed %}


### 1. Installeer de ClickHouse ODBC-stuurprogramma

* Download de nieuwste **ClickHouse ODBC-stuurprogramma** van:
  * [ClickHouse GitHub - clickhouse-odbc](https://github.com/ClickHouse/clickhouse-odbc)
* Voer de installatie uit en volg de installatiewizard.

### 2. Configureer de ODBC-gegevensbron

* Open **ODBC-gegevensbronbeheerder (64-bits)** via het Configuratiescherm of Windows Zoeken.
* Ga naar het tabblad **Systeem-DSN** en klik op **Toevoegen**.
* Selecteer **ClickHouse ODBC-stuurprogramma** uit de lijst en klik op **Voltooien**.
*   Vul de vereiste velden in. U kunt de benodigde informatie vinden in:

    **DocBits** → **Instellingen** → **Documentverwerking** → **Module** → **AI-dashboard** → **Directe toegang tot ClickHouse**

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FNkgb8IJ4dQVRnJ4gpqH0%252Fimage.png%3Falt%3Dmedia%26token%3D27d97e71-dd81-488a-851f-e7d659ad4992\&width=768\&dpr=4\&quality=100\&sign=88a4a589\&sv=2)

    **Vereiste velden:**

    * **Naam**: Een naam voor de verbinding (bijv., `ClickHouse_Prod`)
    * **Beschrijving**: Een korte beschrijving voor uw referentie (optioneel)
    * **Host**: Kopieer de hostwaarde van DocBits
    * **Poort**: Kopieer de poortwaarde van DocBits
    * **Database**: Kopieer de databasenaam van DocBits
    * **Gebruikersnaam**: Kopieer de gebruikersnaam van DocBits
    * **Wachtwoord**: Kopieer het wachtwoord van DocBits

### 3. Verbind ClickHouse met Power BI

* Open **Power BI Desktop**.
*   Selecteer **Gegevens ophalen** → **ODBC** → **Verbinden**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F1aIDfi4Rj6WD9oXsvUjt%252FScreenshot%25202025-05-19%2520163621.png%3Falt%3Dmedia%26token%3D4ec15da7-fa79-4b9e-a83b-cb4b0a545cfd\&width=768\&dpr=4\&quality=100\&sign=59fba2e3\&sv=2)
*   Selecteer in de DSN-lijst uw geconfigureerde bron (bijv., `ClickHouse_Prod`).

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FgDWq5vmtqfAGAQEY0SAX%252FScreenshot%25202025-05-19%2520163823.png%3Falt%3Dmedia%26token%3D443435ac-82ba-40de-a4d1-17611afebb6a\&width=768\&dpr=4\&quality=100\&sign=c0c7d7ae\&sv=2)
* Klik op **OK**. Voer indien nodig opnieuw referenties in.

### 4. Gegevens laden en transformeren

* In het **Navigator**-paneel, blader en selecteer de tabellen of weergaven om te importeren.
* Kies:
  * **Laden**: om direct te importeren
  *   **Gegevens transformeren**: om Power Query te openen voor gegevensvormgeving

      ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F2lrWi9PduJgVQGHQMmhX%252FScreenshot%25202025-05-19%2520164134.png%3Falt%3Dmedia%26token%3D135c45ad-a7ca-4f01-a2f0-07998397f4d9\&width=768\&dpr=4\&quality=100\&sign=e27f4d93\&sv=2)

### 5. Visualiseer uw gegevens

* Gebruik het rapportcanvas om visualisaties te maken.
* Sleep velden, voeg slicers toe, kies diagramtypen en gebruik **DAX**-expressies indien nodig.
* Maak gebruik van **Power Query Editor** om uw ClickHouse-gegevens schoon te maken of te draaien voordat u visuals maakt.
* PowerBI-documentatie: [https://learn.microsoft.com/en-us/power-bi/](https://learn.microsoft.com/en-us/power-bi/)

### 6. Geplande verversing inschakelen (Optioneel)

**Opmerking:** **Vereist Power BI Pro of Premium + Gateway**

* Om uw rapporten in sync te houden met ClickHouse:
* Publiceer uw `.pbix`-bestand naar **Power BI Service**.
* Installeer de **Power BI Gateway** (Standaardmodus) op een machine met netwerktoegang tot ClickHouse.
* In Power BI Service:
  * Ga naar uw dataset → **Instellingen** → **Geplande verversing**
  * Koppel uw DSN en verstrek referenties
* Meer informatie [hier](https://learn.microsoft.com/en-us/power-bi/connect-data/service-gateway-deployment-guidance).

### 7. Voorbeeld Dashboards & Gegevensweergaven

![](../../.gitbook/assets/example_4.avif)![](../../.gitbook/assets/example_3.avif)![](../../.gitbook/assets/example_2.avif)![](../../.gitbook/assets/example_1.avif)
