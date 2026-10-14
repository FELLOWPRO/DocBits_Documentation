# WatchDog Configuratie

Deze handleiding legt uit hoe u de WatchDog-service binnen de DocBits-applicatie configureert. Alle configuraties worden rechtstreeks beheerd onder **Instellingen → Documentverwerking → WatchDog**.

<figure><img src="../../../.gitbook/assets/watchdog-v2-config-infographic.svg" alt="WatchDog Configuration Overview"><figcaption></figcaption></figure>

---

## 1. Tabblad General

Het tabblad General bevat installatie-instructies, downloadlinks en update-instellingen.

<figure><img src="../../../.gitbook/assets/watchdog_v2_01.png" alt="WatchDog General Tab"><figcaption></figcaption></figure>

### 1.1 Download en installatie

* Download de nieuwste `WatchDog.exe` rechtstreeks via het tabblad General
* Kopieer de getoonde API Key
* Voer de configuratieopdracht uit in een opdrachtprompt met Administrator-rechten:

```powershell
WatchDog.exe -api YOUR_API_KEY
```

### 1.2 Schema voor automatische updates

| Optie | Interval |
| :--- | :--- |
| On Startup Only | Eenmalig controleren bij het opstarten |
| Hourly | Elke 3600 seconden |
| Daily | Elke 86400 seconden |
| Weekly | Elke 604800 seconden |

---

## 2. Tabblad Configurations

Maak import- en exportconfiguraties aan en beheer ze. Alle configuraties worden rechtstreeks in DocBits aangemaakt, lokale configuratiebestanden zijn niet nodig.

<figure><img src="../../../.gitbook/assets/watchdog_v2_03.png" alt="WatchDog Configurations Overview"><figcaption></figcaption></figure>

### 2.1 Importconfiguraties

Definieer waar WatchDog naar nieuwe documenten zoekt.

<figure><img src="../../../.gitbook/assets/watchdog_v2_02.png" alt="WatchDog Import Configuration"><figcaption></figcaption></figure>

| Veld | Beschrijving |
| :--- | :--- |
| **Name** | Weergavenaam van deze configuratie |
| **Watch Folder** | Map die op nieuwe documenten wordt bewaakt (verplicht) |
| **Success Folder** | Waarheen bestanden na een geslaagde import worden verplaatst |
| **Document Type** | INVOICE, CREDIT\_NOTE, PURCHASE\_ORDER enzovoort |
| **Sub-Organisation** | Optioneel: documenten naar een specifieke suborganisatie routeren |

### 2.2 Exportconfiguraties

Definieer hoe en waarheen verwerkte documenten worden geëxporteerd.

> **Belangrijk:** Exportconfiguraties **vereisen nu een documenttype** (`doc_type`). Configuraties zonder documenttype worden door het systeem geweigerd.

| Veld | Beschrijving |
| :--- | :--- |
| **Name** | Weergavenaam van deze configuratie |
| **Document Type** | Verplicht: INVOICE, CREDIT\_NOTE enzovoort |
| **Export Method** | Hoe documenten worden geëxporteerd (zie hieronder) |
| **Export Folder** | Doelmap voor mapexports |
| **Execution Order** | Prioriteit wanneer meerdere configuraties overeenkomen (standaard: 1) |
| **XSLT Template** | Optioneel: sjabloon voor XML-transformatie |

### 2.3 Exportmethoden

| Methode | Beschrijving |
| :--- | :--- |
| **Folder (watcher)** | PDF + XML exporteren naar een lokale map |
| **Infor IDM** | Uploaden naar Infor Document Management |
| **Infor BOD** | BOD-XML versturen naar Infor ERP / SAP of M3 |
| **ION API** | Infor ION API-endpoints aanroepen |
| **GLS840MI** | M3-batchverwerking (via REST API) |
| **REST API** | Versturen naar een externe API met ION OAuth-authenticatie |

<figure><img src="../../../.gitbook/assets/watchdog_v2_04.png" alt="WatchDog Export Configuration"><figcaption></figcaption></figure>

### 2.4 Verwerkingsopties

* **Barcode Divider:** Documenten van meerdere pagina's automatisch splitsen op basis van barcodes
* **DocBits Operator:** Taken voor browserautomatisering inschakelen

---

## 3. Tabblad Status

Bewaak de status en activiteit van de WatchDog-service.

<figure><img src="../../../.gitbook/assets/watchdog_v2_status.png" alt="WatchDog Service Status"><figcaption></figcaption></figure>

### Statusinformatie

| Veld | Beschrijving |
| :--- | :--- |
| **Online/Offline** | Actuele verbindingsstatus (drempel van 30 s voor de heartbeat) |
| **Version** | Geïnstalleerde WatchDog-versie |
| **Version First Seen** | Wanneer deze versie voor het eerst werd gemeld |
| **Last Restart** | Tijdstip van de laatste herstart van de service |
| **Auto-Update Enabled** | Of automatische updates actief zijn |
| **Latest Version** | Nieuwste beschikbare versie |
| **Latest Version Checked At** | Wanneer voor het laatst is gecontroleerd op de nieuwste versie |
| **System Info** | Installatiepad, vrij RAM-geheugen, vrije schijfruimte |

### Statusindicator

| Status | Betekenis |
| :--- | :--- |
| ✅ **Online** | WatchDog is verbonden en actief |
| ⚠️ **Offline** | Al 30+ seconden geen heartbeat ontvangen |
| ❌ **Not Installed** | WatchDog heeft nog nooit verbinding gemaakt met deze organisatie |

---

## 4. Tabblad Logs

Bekijk alle WatchDog-gebeurtenissen die in OpenSearch zijn opgeslagen.

<figure><img src="../../../.gitbook/assets/watchdog_v2_05.png" alt="WatchDog Logs"><figcaption></figcaption></figure>

* Filter op datum, gebeurtenistype of trefwoorden
* Gebeurtenistypen: `FILE_IMPORT_STARTED`, `FILE_IMPORT_COMPLETED`, `FILE_IMPORT_FAILED`, `EXPORT_STARTED`, `EXPORT_COMPLETED`, `EXPORT_FAILED`, `FOLDER_VALIDATION_FAILED`, `CONFIG_LOADED`, `SERVICE_RESTART_INITIATED`, `SERVICE_RESTART_COMPLETED`

---

## 5. Tabblad XSLT Templates

Beheer de XSLT-transformatiesjablonen die voor XML-exports worden gebruikt.

<figure><img src="../../../.gitbook/assets/watchdog_v2_06.png" alt="XSLT Templates List"><figcaption></figcaption></figure>

* XSLT-sjablonen uploaden en bewerken
* **Live validatie**: test sjablonen met voorbeeld-XML inclusief veldanalyse
* Sjablonen koppelen aan exportconfiguraties
* Gebruiksaantal bekijken (welke configuraties elk sjabloon gebruiken)

<figure><img src="../../../.gitbook/assets/watchdog_v2_07.png" alt="XSLT Template Editor"><figcaption></figcaption></figure>

---

## 6. Tabblad Export Configurations

Overzicht van alle actieve exportconfiguraties met verbindingsstatus.

* Bewaak het tijdstip van de laatste geslaagde verbinding
* Beheer configuraties direct in de lijst (bewerken, kopiëren, verwijderen)
* Kopieer configuraties in bulk naar andere suborganisaties
