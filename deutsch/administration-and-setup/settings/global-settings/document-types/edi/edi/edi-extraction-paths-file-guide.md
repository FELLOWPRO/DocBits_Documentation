# EDI Extraktionspfad-Datei-Leitfaden

## 1. Überblick

Die **Extraktionspfad-Datei** definiert, wie Daten aus dem **strukturierten XML** in spezifische Dokumentfelder und Tabellen innerhalb der Benutzeroberfläche extrahiert werden. Sie ordnet **Feld-IDs** den **XPath-Ausdrücken** zu, die ausgewertet werden, um Werte aus dem XML in die entsprechenden Dokumentfelder zu ziehen. Diese Datei spielt eine entscheidende Rolle dafür, dass extrahierte Daten während der Feldvalidierung und der nachgelagerten Verarbeitung korrekt erscheinen.

## 2. Zweck und Funktion

* Ordnet jedes Dokumentfeld und jede Tabellenspalte einem bestimmten Ort im strukturierten XML mithilfe von XPath-Ausdrücken zu.
* Stellt sicher, dass die richtigen Werte in Felder wie `order_number`, `supplier_name` und `total_amount` eingetragen werden.
* Unterstützt sowohl **einfache Felder** (über ein `fields`-Objekt) als auch **Tabellen** (über ein `tables`-Array mit Zeilenpfaden und Spaltenzuordnungen).
* Ermöglicht eine präzise Kontrolle darüber, wie Daten aus dem XML abgerufen werden, einschließlich der Verwendung von XPath-Funktionen wie `sum()`.

Beispiel für Feldzuordnung:

Copy

```
"order_number": "//PURCHASE_ORDER/PURCHASE_ORDER/text()"
```

## 3. Zugriff und grundlegende Bearbeitung

#### **Dateizugriff:**

1.  Gehe zu **Einstellungen** → **Dokumenttyp** → _\[Ihr Dokument (z. B. Bestellung)]_ → **E-Dok**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Ff6zyL0AvmqSvrogZdnox%252Fimage.png%3Falt%3Dmedia%26token%3D6bc9ab55-6ee9-43d1-b576-4c5833c208cf\&width=768\&dpr=4\&quality=100\&sign=a23de442\&sv=2)
2. Wähle unter dem **E-Dok**-Tab dein Format aus (z. B. **EDI**).
3.  Klicke auf **Extraktionspfade**, um die Datei anzuzeigen oder zu bearbeiten.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FawwG5QnErp1yy1eYHrlX%252Fimage.png%3Falt%3Dmedia%26token%3D46a6d8b3-52d2-4c13-bc72-1a74955efd9f\&width=768\&dpr=4\&quality=100\&sign=e612882b\&sv=2)

#### **Entwurfsverwaltung:**

* **Entwurf erstellen:** Klicke auf das ✏️ Stiftsymbol.
* **Entwürfe löschen:** Verwende das 🗑️ Papierkorb-Symbol, um ungenutzte Entwürfe zu entfernen.
* **Änderungen aktivieren:** Klicke auf das ✅ Häkchen, um eine Version zu veröffentlichen.
  * **Hinweis**: Das Aktivieren einer neuen Version wird die vorherige **automatisch deaktivieren**.

## 4. Editor & Syntax

Die Extraktionspfad-Datei ist in **JSON** geschrieben und enthält zwei Hauptkomponenten:

* **fields**: Ein Wörterbuch, in dem jeder Schlüssel eine Feld-ID und jeder Wert ein XPath-Ausdruck ist, der definiert, wie die Daten extrahiert werden sollen.
* **tables**: Eine Liste von Tabellendefinitionen, die Folgendes enthalten:
  * `name`: Die ID der Tabelle.
  * `row_path`: Ein XPath, der jede Zeile der Tabelle identifiziert.
  * `columns`: Eine Liste von Spaltenzuordnungen (`name`, `path`).

Sie können auch XPath-Funktionen (z. B. `sum()`) und Ausdrücke verwenden, um Werte dynamisch aus wiederholten Elementen zu berechnen.

Copy

```
jsonCopyEdit"total_net_amount": "sum(//PURCHASE_ORDER/ORDER_LINES/ORDER_LINE/SUB_TOTAL)"
```

## 5. Vorschaufunktion (Extraktion auswerten)

Die **Vorschaufunktion** ermöglicht es Ihnen, zu simulieren, wie sich die Extraktionspfade bei einem tatsächlich hochgeladenen Dokument verhalten werden.

**Verwendung:**

* Laden Sie eine EDI-Datei über den Standard-Upload-Prozess hoch.
* Kopieren Sie die **Dokumenten-ID**.
* Gehen Sie zur **Extraktionspfade**-Benutzeroberfläche.
* Öffnen Sie die **Vorschaufunktion**.\
  \
  &#x20;![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F9lddYJl2G4tzpdr9RD5F%252Fimage.png%3Falt%3Dmedia%26token%3Df7663f70-ef10-4e64-bbdc-41048ed8352a\&width=300\&dpr=4\&quality=100\&sign=36ce2b93\&sv=2)
* Geben Sie die Dokumenten-ID ein und klicken Sie auf **Test**.
* Das Ergebnis zeigt, wie jedes Feld und jede Tabelle basierend auf den konfigurierten Pfaden befüllt wird.

Diese Funktion ist entscheidend, um zu überprüfen, ob Ihre XPath-Ausdrücke korrekt definiert sind und die erwarteten Werte abrufen, bevor der Entwurf aktiviert wird.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F81uvH6FFVBJsSZucanWY%252Fimage.png%3Falt%3Dmedia%26token%3Dde3ba545-1ee3-44b2-a629-9660d80174f2\&width=768\&dpr=4\&quality=100\&sign=43c8b507\&sv=2)

## 6. Videoanleitung

Eine Videoanleitung für diesen Dateityp finden Sie auf der [Videos-Seite.](https://docs.docbits.com/administration-and-setup/settings/global-settings/document-types/edi/edi/edi-videos) Verwenden Sie sie, um die Einrichtung, Bearbeitung und Vorschau zu verfolgen.
