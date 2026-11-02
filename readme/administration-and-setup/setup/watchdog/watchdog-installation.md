# WatchDog-Installation

<figure><img src="../../../.gitbook/assets/watchdog-installation-infographic.svg" alt="Installationsschritte für WatchDog"><figcaption></figcaption></figure>

> **Empfohlen:** Verwenden Sie die unten beschriebene moderne Einrichtung. WatchDog-Konfigurationen werden jetzt direkt in der DocBits-Anwendung erstellt — lokale Konfigurationsdateien sind nicht mehr nötig.

## Voraussetzungen

* Windows Server oder Windows 10/11
* Administratorzugriff
* Netzwerkverbindung zur DocBits-API
* DocBits-API-Schlüssel (verfügbar unter Settings → WatchDog → General Tab)

## Installationsschritte

### 1. Erforderliche Ordner anlegen

Legen Sie ein Hauptverzeichnis und Unterordner für WatchDog an:

```
C:\WatchDog\              ← WatchDog executable
C:\WatchDog\Import\       ← Watch folder for incoming documents
C:\WatchDog\Processed\    ← Success folder for processed documents
C:\WatchDog\Export\        ← Export folder for exported files
```

> **Hinweis:** Es wird empfohlen, lokale Pfade zu verwenden. UNC-Netzwerkpfade (z. B. `\\server\share`) werden unterstützt, erfordern für eine zuverlässige Dateierkennung aber unter Umständen einen Polling Observer.

### 2. WatchDog herunterladen

Laden Sie `WatchDog.exe` aus der DocBits-Anwendung herunter:

**Settings → Document Processing → WatchDog → General Tab → Download**

Legen Sie die heruntergeladene Datei `WatchDog.exe` in `C:\WatchDog\` ab.

### 3. API-Verbindung konfigurieren

Öffnen Sie die **Eingabeaufforderung (CMD)** als **Administrator** und führen Sie Folgendes aus:

```powershell
cd C:\WatchDog
WatchDog.exe -api YOUR_API_KEY
```

Dadurch wird WatchDog mit Ihrer DocBits-Organisation verbunden und ruft die Konfigurationen automatisch ab.

### 4. Als Windows-Dienst installieren

```powershell
WatchDog.exe install
```

### 5. Dienst starten

```powershell
WatchDog.exe start
```

### 6. Konfigurationen in DocBits erstellen

Navigieren Sie in DocBits zu **Settings → Document Processing → WatchDog → Configurations Tab**:

* Klicken Sie auf **New Import Configuration**, um Überwachungsordner einzurichten
* Klicken Sie auf **New Export Configuration**, um Exportziele einzurichten

> **Wichtig:** Export-Konfigurationen erfordern einen **Dokumenttyp**. Alle Konfigurationen werden zentral in DocBits verwaltet, nicht in lokalen Konfigurationsdateien.

### 7. Automatischen Start einrichten

1. Öffnen Sie die **Dienste** (`Win + R` → `services.msc`)
2. Suchen Sie **WatchDog** in der Dienstliste
3. Doppelklicken Sie, um die Eigenschaften zu öffnen
4. Setzen Sie den **Starttyp** auf **Automatisch (Verzögerter Start)**
5. Klicken Sie auf **OK**

## Installation überprüfen

Prüfen Sie nach der Installation den WatchDog-Status in DocBits:

**Settings → WatchDog → General Tab**

<figure><img src="../../../.gitbook/assets/watchdog_v2_01.png" alt="Registerkarte „General“ von WatchDog — Dienststatus"><figcaption></figcaption></figure>

* ✅ **Online** — WatchDog ist verbunden und sendet Heartbeats
* Version, letzter Neustart und Systeminformationen sollten sichtbar sein

## Befehlsreferenz

| Befehl | Beschreibung |
| :--- | :--- |
| `WatchDog.exe -api KEY` | API-Schlüssel konfigurieren |
| `WatchDog.exe install` | Als Windows-Dienst installieren |
| `WatchDog.exe start` | Dienst starten |
| `WatchDog.exe stop` | Dienst beenden |
| `WatchDog.exe debug` | Im Konsolenmodus ausführen (zur Fehlersuche) |
| `WatchDog.exe remove` | Dienst deinstallieren |
| `WatchDog.exe --version` | Aktuelle Version anzeigen |
| `WatchDog.exe --list-folders` | Konfigurierte Überwachungsordner auflisten |
| `WatchDog.exe --add-folder PATH` | Überwachungsordner hinzufügen |
| `WatchDog.exe --remove-folder PATH` | Überwachungsordner entfernen |

---

## Legacy: V1-Konfiguration (veraltet)

Die folgende V1-Einrichtungsmethode mit lokalen Konfigurationsdateien ist **veraltet**. Verwenden Sie stattdessen die oben beschriebene moderne, API-basierte Einrichtung.

<details>
<summary>V1-Einrichtung (zum Aufklappen klicken)</summary>

### WatchDog in DocBits konfigurieren (V1)

1. **Auf die WatchDog-Einstellungen zugreifen**
   * Navigieren Sie zu **Settings → Document Processing → WatchDog**
2. **Ordnereinstellungen**
   * Definieren Sie die Pfade: `C:/WatchDog/Read` und `C:/WatchDog/Processed`

   <figure><img src="../../../.gitbook/assets/watchdog_folder_settings.png" alt="WatchDog-Ordnereinstellungen"><figcaption></figcaption></figure>

3. **Allgemeine Einstellungen**
   * Wählen Sie Dokumenttypen aus und konfigurieren Sie das Exportziel

   <figure><img src="../../../.gitbook/assets/watchdog_general_settings_doctypes.png" alt="Allgemeine WatchDog-Einstellungen"><figcaption></figcaption></figure>

4. **Export-Konfigurationen**
   * Zeigt die konfigurierten Exporte für die On-Premise-Verarbeitung an

   <figure><img src="../../../.gitbook/assets/watchdog_export_configurations_list.png" alt="WatchDog-Export-Konfigurationen"><figcaption></figcaption></figure>

5. **Konfiguration herunterladen**
   * Laden Sie `watchdog-config.json` herunter und legen Sie die Datei in `C:\WatchDog\` ab

   <figure><img src="../../../.gitbook/assets/watchdog_download_configuration.png" alt="Konfiguration herunterladen"><figcaption></figcaption></figure>

</details>
