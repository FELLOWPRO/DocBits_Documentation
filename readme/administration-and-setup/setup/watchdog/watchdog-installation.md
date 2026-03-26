# WatchDog Installation

<figure><img src="../../../.gitbook/assets/watchdog-infographic-de.png" alt="WatchDog Infographic"><figcaption></figcaption></figure>

### Konfigurieren von WatchDog in DocBits

1. **Zugriff auf die WatchDog-Einstellungen**
   * Navigieren Sie zu **Einstellungen → Dokumentenverarbeitung → WatchDog**.
2. **Ordnereinstellungen**
   * Definieren Sie die Pfade, in denen WatchDog Dokumente findet und verarbeitet.
   *   Die Ordnerpfade sollten mit denen übereinstimmen, die während der Installation erstellt wurden:

       * `C:/WatchDog/Read`
       * `C:/WatchDog/Processed`

       ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FzG1EFmtSO4AxZjWir401%252Fimage.png%3Falt%3Dmedia%26token%3Dc356e023-8cfb-4f45-b863-b27c5af1d9df\&width=768\&dpr=4\&quality=100\&sign=1b1ae0c4\&sv=2)
   * <mark style="color:red;">**Hinweis:**</mark>**&#x20;Es wird empfohlen, lokale Pfade zu verwenden. Diese sollten mit den Ordnern in der DocBits-Installation übereinstimmen.**
3. **Allgemeine Einstellungen**
   *   Wählen Sie die zu verarbeitenden Dokumenttypen aus, indem Sie die entsprechenden Kontrollkästchen aktivieren.

       ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FZbCt5UHd37PdNZsVItdt%252Fimage.png%3Falt%3Dmedia%26token%3Db3c3f203-0f60-42a0-bd56-ee70c204f5e8\&width=768\&dpr=4\&quality=100\&sign=becd5e31\&sv=2)
   * **Barcode-Trenner:** Wenn aktiviert, ermöglicht das Trennen von Barcodes.
   * **DocBits-Betreiber:** Wenn aktiviert, öffnet einen Chrome-Browser im Hintergrund für den DocBits-Betreiber.
   * **Exportziel:** Legt das Exportziel fest.
     * **Infor:** Dokumente werden nach Infor exportiert.
     * **Exportordner:** Dokumente werden in einen definierten Ordner exportiert, der weiter unten konfiguriert werden kann.
4. **Exportkonfigurationen**
   * Zeigt alle konfigurierten Exporte für **lokale Verarbeitung** an.
   *   Zeigt den Zeitstempel der **letzten erfolgreichen Verbindung** für jede Konfiguration an.

       ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FRvK5qn6EggWJxcSYNP5J%252Fimage.png%3Falt%3Dmedia%26token%3D195b9cc6-c5ac-4ee6-90da-b3ee9696ee30\&width=768\&dpr=4\&quality=100\&sign=3bc11ec5\&sv=2)
5. **bod\_mapping-Konfiguration (Optional)**
   * <mark style="color:red;">**Erforderliche Felder:**</mark> Bevor Sie benutzerdefinierte Metadatenzuordnungen hinzufügen, müssen Sie die folgenden zwei Werte definieren
     * **`file_name`**
     * **`pdf_path`**
   *   Klicken Sie auf **Zeile hinzufügen**, um Metadatenzuordnungen zu definieren.

       ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FlzUqcr51kq18OrmYAR8X%252Fimage.png%3Falt%3Dmedia%26token%3D3035122b-f1d3-44cc-bfe6-5230943bd77d\&width=768\&dpr=4\&quality=100\&sign=e98d5a1b\&sv=2)
   * **Wert:** Gibt den Feldnamen für die Metadaten an.
   * **Pfad:** Der XPath-Ausdruck, der auf die XML-Daten zeigt, die dem Feld zugeordnet werden sollen.
   * **Mülleimer-Symbol:** Wird verwendet, um eine bestimmte Zeile zu löschen.
6. **Konfiguration herunterladen**
   * Konfiguration speichern
   *   Konfiguration herunterladen

       ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FZXiz4KB7QpnaqD9XwX3o%252Fimage.png%3Falt%3Dmedia%26token%3D04c9f8dc-7d79-443f-9ce4-6d4214edc98b\&width=768\&dpr=4\&quality=100\&sign=574a4218\&sv=2)

### WatchDog Installationsanleitung

1. **Erforderliche Ordner erstellen**
   * Erstellen Sie ein Hauptverzeichnis: `C:/WatchDog`
   * Erstellen Sie im Verzeichnis `C:/WatchDog` die folgenden Unterordner: **Hinweis:** Diese sollten mit den Ordnern in DocBits übereinstimmen.
     * `C:/WatchDog/Read`
     * `C:/WatchDog/Processed`
   * <mark style="color:red;">**Hinweis:**</mark>**&#x20;Es wird empfohlen, lokale Pfade zu verwenden. Diese sollten mit den Ordnern in der DocBits-Konfiguration übereinstimmen.**
2. **WatchDog herunterladen**
   * Laden Sie die neueste Version von `WatchDog.exe` von: [https://github.com/Fellow-Consulting-AG/WatchDog](https://github.com/Fellow-Consulting-AG/WatchDog)
   * Platzieren Sie die heruntergeladene Datei `WatchDog.exe` in `C:/WatchDog`.
   * Platzieren Sie die heruntergeladene Datei `watchdog-config.json` in `C:/WatchDog`.
   * Öffnen Sie die `watchdog-config.json` und ändern Sie den **config\_path.**
   * In diesem Beispiel:
     * `"config_path": "C:/WatchDog/watchdog-config.json"`
3. **WatchDog installieren**
   * Öffnen Sie die **Eingabeaufforderung (CMD)** mit **Administratorrechten**.
   * Navigieren Sie zum WatchDog-Ordner
   *   Führen Sie den folgenden Befehl aus, um WatchDog zu installieren:

       `WatchDog.exe install`
4. **Starten Sie den WatchDog-Dienst**
   *   Führen Sie den folgenden Befehl in CMD aus:

       `WatchDog.exe start`
5. **Starttyp festlegen**
   * Öffnen Sie **Dienste** (Drücken Sie `Win + R`, geben Sie `services.msc` ein und drücken Sie **Enter**).
   * Suchen Sie **WatchDog** in der Dienstliste.
   * Doppelklicken Sie, um die Eigenschaften zu öffnen.
   * Setzen Sie den **Starttyp** auf **Automatisch (verzögerter Start)**.
   * Klicken Sie auf **OK**.
