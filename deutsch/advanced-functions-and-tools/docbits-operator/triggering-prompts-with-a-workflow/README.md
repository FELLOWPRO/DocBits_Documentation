# Auslösen von Aufforderungen mit einem Workflow

Dieser Leitfaden erläutert, wie Sie einen DocBits-Workflow konfigurieren, um automatisch eine gespeicherte Aufforderung auszulösen. Dadurch können Sie Operator-Aufforderungen in Dokumentenverarbeitungsabläufe integrieren, ohne manuelle Eingaben.

## Schritt 1: Erstellen einer Aufforderung

Bevor Sie eine Aufforderung mit einem Workflow verknüpfen:

* Stellen Sie sicher, dass Ihre Aufforderung bereits erstellt wurde
* Fügen Sie alle erforderlichen **Variablen** im Aufforderungstext ein

Wenn Sie Hilfe beim Schreiben oder Speichern von Aufforderungen benötigen, lesen Sie den [Leitfaden zum Schreiben von Aufforderungen](../prompt-writing-guide.md) und die [Übersicht des Operator-Interfaces](../).

## Schritt 2: Einrichten des Workflows

Bevor Sie die Operator-Aufforderungskarte konfigurieren, stellen Sie sicher, dass Ihr Workflow ordnungsgemäß erstellt wurde.

1. Navigieren Sie zur **Workflow-Builder** im DocBits-Interface
2. Erstellen Sie einen neuen Workflow oder öffnen Sie einen vorhandenen
3. Definieren Sie die **Auslösebedingungen** - diese bestimmen, wann der Workflow gestartet wird (z. B. Dokumententyp, Status, Feldpräsenz usw.)
4. Fügen Sie die erforderlichen **Aktionsschritte** bei Bedarf zu Ihrem Workflow hinzu

<div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fd3qJJhFDHTXDUfUedjaF%252Fimage.png%3Falt%3Dmedia%26token%3D310f9e9c-9e79-4987-af01-2d914f1abbe7&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=873cf566&#x26;sv=2" alt="" width="375"></div>

## Schritt 3: Konfigurieren der Operator-Aufforderungskarte im Workflow

Im Workflow-Builder verwenden Sie die **Operator-Aufforderungskarte**, um eine Aufforderung zu konfigurieren, die ausgeführt werden soll, wenn die Bedingungen des Workflows erfüllt sind.

<div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fg11jtpdL4j3mJveYvWSX%252Fimage.png%3Falt%3Dmedia%26token%3Db208669e-b6a8-4879-b08b-d9ba353e908d&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=974876f7&#x26;sv=2" alt="" width="375"></div>

### Wichtige Konfigurationsoptionen

* **Skript:** Wählen Sie die gespeicherte **Organisationsaufforderung** aus, die ausgeführt werden soll
* **Skriptdaten (Variablen):** Wenn die ausgewählte Aufforderung Variablen enthält, definieren Sie hier ihre Werte mithilfe von Schlüssel-Wert-Paaren
  * Wenn eine Variable hier leer gelassen wird, versucht das System, sie automatisch **aus dem Dokument zu befüllen**
  * Damit dies funktioniert, muss der Variablenname in der Aufforderung genau mit der **Feld-ID** des Dokumentattributs übereinstimmen
* **Maximale Schritte:** Definieren Sie die maximale Anzahl von Schritten, die der Operator während dieser Aufforderung ausführen darf
* **Maximale Wiederholungen:** Legen Sie fest, wie oft das System die Aufforderung im Falle eines Fehlers wiederholen soll
* **Ausführungsmodus:** Wählen Sie, ob die Aufforderung ausgeführt werden soll:
  * **In der Cloud**
  * **Vor Ort** (erforderlich, wenn Ihr ERP- oder Zielsystem lokal gehostet wird)
