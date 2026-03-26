# WatchDog Installatie

<figure><img src="../../.gitbook/assets/watchdog-infographic-nl.png" alt="WatchDog Infographic"><figcaption></figcaption></figure>

### Configureren van WatchDog in DocBits

1. **Toegang tot WatchDog-instellingen**
   * Navigeer naar **Instellingen → Documentverwerking → WatchDog**.
2. **Mapinstellingen**
   * Definieer de paden waar WatchDog documenten vindt en verwerkt.
   *   De mappaden moeten overeenkomen met die tijdens de installatie zijn aangemaakt:

       * `C:/WatchDog/Read`
       * `C:/WatchDog/Processed`

       ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FzG1EFmtSO4AxZjWir401%252Fimage.png%3Falt%3Dmedia%26token%3Dc356e023-8cfb-4f45-b863-b27c5af1d9df&width=768&dpr=4&quality=100&sign=1b1ae0c4&sv=2)
   * <mark style="color:red;">**Opmerking:**</mark> **Het wordt aanbevolen om lokale paden te gebruiken. Deze moeten overeenkomen met de mappen in de DocBits-installatie**
3. **Algemene instellingen**
   *   Selecteer de documenttypes die verwerkt moeten worden door de bijbehorende selectievakjes aan te vinken


       ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FZbCt5UHd37PdNZsVItdt%252Fimage.png%3Falt%3Dmedia%26token%3Db3c3f203-0f60-42a0-bd56-ee70c204f5e8&width=768&dpr=4&quality=100&sign=becd5e31&sv=2)
   * **Barcode-scheiding:** Wanneer ingeschakeld, activeert het de barcode-scheiding.
   * **DocBits-operator:** Wanneer ingeschakeld, opent het een Chrome-browser op de achtergrond voor de DocBits-operator.
   * **Exportbestemming:** Stelt de exportbestemming in.
     * **Infor:** Documenten worden geëxporteerd naar Infor.
     * **Exportmap:** Documenten worden geëxporteerd naar een gedefinieerde map die hieronder kan worden geconfigureerd.
4. **Exportconfiguraties**
   * Toont alle geconfigureerde exports voor **on-premise verwerking**.
   *   Toont de tijdstempel van de **laatste succesvolle verbinding** voor elke configuratie.


       ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FRvK5qn6EggWJxcSYNP5J%252Fimage.png%3Falt%3Dmedia%26token%3D195b9cc6-c5ac-4ee6-90da-b3ee9696ee30&width=768&dpr=4&quality=100&sign=3bc11ec5&sv=2)
5. **bod_mapping-configuratie (Optioneel)**
   * <mark style="color:red;">**Vereiste velden:**</mark> Voordat u aangepaste metadata-mappingen toevoegt, moet u de volgende twee waarden definiëren
     * **`file_name`**
     * **`pdf_path`**
   *   Klik op **Rij toevoegen** om metadata-mappingen te definiëren.


       ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FlzUqcr51kq18OrmYAR8X%252Fimage.png%3Falt%3Dmedia%26token%3D3035122b-f1d3-44cc-bfe6-5230943bd77d&width=768&dpr=4&quality=100&sign=e98d5a1b&sv=2)
   * **Waarde:** Geeft de veldnaam voor de metadata aan.
   * **Pad:** De XPath-expressie die naar de XML-gegevens wijst die aan het veld moeten worden toegewezen.
   * **Prullenbakpictogram:** Wordt gebruikt om een specifieke rij te verwijderen.
6. **Download de configuratie**
   * Sla de configuratie op
   *   Download de configuratie


       ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FZXiz4KB7QpnaqD9XwX3o%252Fimage.png%3Falt%3Dmedia%26token%3D04c9f8dc-7d79-443f-9ce4-6d4214edc98b&width=768&dpr=4&quality=100&sign=574a4218&sv=2)

### WatchDog Installatiehandleiding

1. **Maak vereiste mappen aan**
   * Maak een hoofdmap aan: `C:/WatchDog`
   * Maak binnen `C:/WatchDog` de volgende submappen aan: **Opmerking**: deze moeten overeenkomen met de mappen in DocBits
     * `C:/WatchDog/Read`
     * `C:/WatchDog/Processed`
   * <mark style="color:red;">**Opmerking:**</mark> **Het wordt aanbevolen om lokale paden te gebruiken. Deze moeten overeenkomen met de mappen in de DocBits-configuratie**
2. **Download WatchDog**
   * Download de nieuwste versie van `WatchDog.exe` van: [https://github.com/Fellow-Consulting-AG/WatchDog](https://github.com/Fellow-Consulting-AG/WatchDog)
   * Plaats het gedownloade `WatchDog.exe`-bestand in `C:/WatchDog`.
   * Plaats het gedownloade `watchdog-config.json`-bestand in `C:/WatchDog`.
   * Open de `watchdog-config.json` en wijzig de **config_path.**
   * In dit voorbeeld:
     * `"config_path": "C:/WatchDog/watchdog-config.json"`
3. **Installeer WatchDog**
   * Open **Opdrachtprompt (CMD)** met **Administrator-rechten**.
   * Navigeer naar de WatchDog-map
   *   Voer de volgende opdracht uit om WatchDog te installeren:

       `WatchDog.exe install`
4. **Start de WatchDog-service**
   *   Voer de volgende opdracht in CMD uit:

       `WatchDog.exe start`
5. **Stel opstarttype in**
   * Open **Diensten** (Druk op `Win + R`, typ `services.msc` en druk op **Enter**).
   * Zoek **WatchDog** in de lijst met services.
   * Dubbelklik om de eigenschappen te openen.
   * Stel **Opstarttype** in op **Automatisch (Vertraagd starten)**.
   * Klik op **OK**.