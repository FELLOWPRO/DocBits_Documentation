# EDI-Vorschau-Datei-Leitfaden

## 1. Überblick

Die **Vorschau-Datei** definiert, wie strukturierte XML-Daten in ein menschenlesbares, PDF-ähnliches Format gerendert werden. Sie kombiniert **HTML und CSS** für die visuelle Darstellung und verwendet **XSLT** `**select**` **Anweisungen**, um Daten aus dem benutzerdefinierten XML dynamisch einzufügen. Diese Vorschau wird während der **Feldvalidierung** angezeigt und ist auch beim Export von Dokumenten nach **IDM** enthalten.

## 2. Zweck und Funktion

* Konvertiert maschinenlesbares benutzerdefiniertes XML in eine visuell formatierte Vorschau (PDF).
* Ermöglicht eine benutzerfreundliche Überprüfung und Validierung der extrahierten Daten.
* Stellt sicher, dass wichtige Dokumentenfelder wie Überschriften, Tabellen, Summen usw. konsistent gerendert werden.
* Aufbau mit **HTML + CSS** für Layout und Design und **XSLT** zur Bindung von Daten an das Layout.

## 3. Zugriff und grundlegende Bearbeitung

#### **Zugriff auf die Datei:**

1.  Gehe zu **Einstellungen** → **Dokumententyp** → _\[Ihr Dokument (z. B. Bestellung)]_ → **E-Dok**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Ff6zyL0AvmqSvrogZdnox%252Fimage.png%3Falt%3Dmedia%26token%3D6bc9ab55-6ee9-43d1-b576-4c5833c208cf\&width=768\&dpr=4\&quality=100\&sign=a23de442\&sv=2)
2. Wähle unter dem **E-Dok**-Tab dein Format aus (z. B. **EDI**).
3.  Klicke auf **Vorschau**, um die Datei anzuzeigen oder zu bearbeiten.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fdo1R389GeSqFuZKLD0OP%252Fimage.png%3Falt%3Dmedia%26token%3D930903d4-44af-4188-b015-c60c2dd9d9ab\&width=768\&dpr=4\&quality=100\&sign=77bbb2ce\&sv=2)

#### **Entwurfsverwaltung:**

* **Entwurf erstellen:** Klicke auf das ✏️ Stiftsymbol.
* **Entwürfe löschen:** Verwende das 🗑️ Papierkorb-Symbol, um ungenutzte Entwürfe zu entfernen.
* **Änderungen aktivieren:** Klicke auf das ✅ Häkchen, um eine Version zu veröffentlichen.
  * **Hinweis**: Das Aktivieren einer neuen Version deaktiviert automatisch die vorherige.

## 4. HTML/XSLT/CSS-Editor

Die **Vorschau-Datei** wird in einem dedizierten Editor bearbeitet, der HTML, XSLT und CSS unterstützt.

* **HTML** definiert die Struktur des Ausgabedokuments (z. B. Tabellen, Divs, Layout).
* **CSS** steuert das Styling (z. B. Schriftarten, Abstände, Farben, Ausrichtung).
*   **XSLT** `**select**` **Anweisungen** werden verwendet, um Felder aus dem benutzerdefinierten XML dynamisch zu befüllen, wie z. B.:

    Copy

    ```
    <xsl:value-of select="/PURCHASE_ORDER/PURCHASE_ORDER_NUMBER/text()" />
    ```
* Du kannst auch **XSLT-Logik** (`<xsl:if>`, `<xsl:for-each>`, usw.) verwenden, um bedingte Anzeige zu handhaben oder über Zeilenpositionen zu iterieren.

## 5. Vorschaufunktion (Ausgabe rendern)

Die Vorschaufunktion ermöglicht es dir, zu testen und zu überprüfen, wie ein EDI-Dokument mit der aktuellen Vorschau-Datei gerendert wird.

#### **Verwendung:**

* Lade eine EDI-Datei über den Standard-Upload-Prozess hoch.
* Kopiere die **Dokumenten-ID** der hochgeladenen Datei.
* Navigiere zur **Vorschau**-Schnittstelle.
* Öffne die **Vorschaufunktion**.\
  \
  ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F9lddYJl2G4tzpdr9RD5F%252Fimage.png%3Falt%3Dmedia%26token%3Df7663f70-ef10-4e64-bbdc-41048ed8352a\&width=300\&dpr=4\&quality=100\&sign=36ce2b93\&sv=2)\\
* Gib die Dokumenten-ID ein und klicke auf **Test**.
* Die gerenderte Vorschau im PDF-Stil wird unter Verwendung des HTML/CSS/XSLT-Setups angezeigt.

Diese Funktion ist entscheidend für das Debuggen von Datenbindungen, die Verfeinerung des Layouts und die Sicherstellung, dass das Dokument sowohl für Benutzer als auch für nachgelagerte Systeme wie **IDM** genau und visuell klar ist.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FJH103tnbqZjuimpOniVg%252Fimage.png%3Falt%3Dmedia%26token%3D4e63cc09-b0de-488f-bdd0-ee5a9246a371\&width=768\&dpr=4\&quality=100\&sign=bfff5bba\&sv=2)

## 6. Videoanleitung

Eine Videoanleitung für diesen Dateityp ist auf der [Videos-Seite](https://docs.docbits.com/administration-and-setup/settings/global-settings/document-types/edi/edi/edi-videos) verfügbar. Verwende sie, um die Einrichtung, Bearbeitung und Vorschau zu verfolgen.
