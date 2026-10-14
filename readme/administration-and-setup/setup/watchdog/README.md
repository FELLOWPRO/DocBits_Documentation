# WatchDog

<figure><img src="../../../.gitbook/assets/watchdog-overview-infographic.svg" alt="Overzicht van WatchDog"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/watchdog-infographic-en.png" alt="Infographic over WatchDog"><figcaption></figcaption></figure>

**WatchDog** is een Windows-gebaseerde on-premise service die lokale mappen controleert op binnenkomende documenten, deze ter verwerking uploadt naar de DocBits Cloud en voltooide documenten terug exporteert naar lokale mappen of ERP-systemen.

## Belangrijkste functies

* **Automatische mapbewaking** — bewaakt lokale paden en UNC-netwerkpaden op nieuwe PDF's
* **Ondersteuning voor meerdere configuraties** — meerdere import-/exportconfiguraties per instantie
* **6 exportmethoden** — Local Folder, Infor IDM, Infor BOD, ION API, GLS840MI, REST API
* **Auto-Update** — automatische versie-updates met rollback bij een fout
* **Beheer op afstand** — herstarten, bijwerken en configureren via de DocBits-UI

## Snelstart

<figure><img src="../../../.gitbook/assets/watchdog_v2_01.png" alt="Tabblad General van WatchDog"><figcaption></figcaption></figure>

### 1. WatchDog downloaden

Download `WatchDog.exe` via **Settings → Document Processing → WatchDog → General Tab** in de DocBits-applicatie.

### 2. Configureren met API Key

Open de **opdrachtprompt als beheerder** en voer uit:

```powershell
WatchDog.exe -api YOUR_API_KEY
```

> **Opmerking:** De API Key is beschikbaar in uw DocBits-instellingen op het tabblad WatchDog General. Hiermee koppelt u WatchDog aan uw DocBits-organisatie.

### 3. Installeren als Windows-service

```powershell
WatchDog.exe install
WatchDog.exe start
```

### 4. Configuraties maken in DocBits

Alle import- en exportconfiguraties worden rechtstreeks in de **DocBits-applicatie** gemaakt:

**Settings → Document Processing → WatchDog → Configurations Tab**

* **Import Configurations** — definieer bewaakte mappen en documenttypen
* **Export Configurations** — definieer exportbestemmingen, XSLT-templates en exportmethoden

> **Belangrijk:** Voor exportconfiguraties is een **documenttype** (`doc_type`) vereist. Configuraties zonder documenttype worden geweigerd.

### 5. Automatisch starten (optioneel)

Om WatchDog automatisch bij het opstarten te laten starten:

1. Open **Services** (`Win + R` → `services.msc`)
2. Zoek **WatchDog** in de lijst
3. Stel **Startup Type** in op **Automatic (Delayed Start)**

## Opdrachtenoverzicht

| Opdracht | Beschrijving |
| :--- | :--- |
| `WatchDog.exe -api KEY` | API Key configureren en verbinden met DocBits |
| `WatchDog.exe install` | Installeren als Windows-service |
| `WatchDog.exe start` | De service starten |
| `WatchDog.exe stop` | De service stoppen |
| `WatchDog.exe debug` | Uitvoeren in consolemodus voor probleemoplossing |
| `WatchDog.exe --version` | Huidige versie tonen |
| `WatchDog.exe --list-folders` | Geconfigureerde bewaakte mappen weergeven |
| `WatchDog.exe remove` | De service verwijderen |

## Meer informatie

* [WatchDog-installatie](watchdog-installation.md)
* [WatchDog-configuratie](watchdog-v2-configuration.md)
* [WatchDog Admin FAQ](watchdog-admin-faq.md)
