# EDI Struktur-Deskriptor-Datei-Leitfaden

## **1. Überblick**

Die **Struktur-Deskriptor-Datei** definiert, wie sich wiederholende EDI-Segmente (z. B. `N1`–`N4`) zu strukturiertem JSON gruppieren. Sie gewährleistet:

* **Genaue Analyse** von zusammenhängenden Elementen als Einheiten.
* **Konsistente Ausgabe** für nachgelagerte Systeme.

_Für ein vollständiges Beispiel mit Segmentdetails siehe_ [_Struktur-Deskriptor-Beispiel_](edi-structure-descriptor.md)_._

## **2. Zugriff & Grundlegende Bearbeitung**

#### **Dateizugriff**

1.  **Einstellungen** → **Dokumententype** → \[Ihr Dokument (z. B. _Bestellung_)] → **E-Doc.**\


    <div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Ff6zyL0AvmqSvrogZdnox%252Fimage.png%3Falt%3Dmedia%26token%3D6bc9ab55-6ee9-43d1-b576-4c5833c208cf&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=a23de442&#x26;sv=2" alt=""></div>
2. Unter **E-Doc.** wählen Sie Ihr Format (z. B. _EDI_ ).
3.  Klicken Sie auf **Struktur-Deskriptor**.\


    <div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FOuNVhIuYBPJTu4PdMecy%252Fimage.png%3Falt%3Dmedia%26token%3Dd111b34e-0dd9-4436-9df4-f59490ac0d87&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=6e8e9f0e&#x26;sv=2" alt="" width="563"></div>

#### **Entwurfsverwaltung**

* **Entwurf erstellen**: Klicken Sie auf das ✏️ Stiftsymbol, um mit der Bearbeitung zu beginnen.
* **Entwürfe löschen**: Verwenden Sie das 🗑️ Papierkorb-Symbol, um ungenutzte Entwürfe zu entfernen.
* **Änderungen aktivieren**: Klicken Sie auf das ✅ Häkchensymbol, um Ihre Änderungen zu genehmigen und zu veröffentlichen.
  * **Hinweis**: Das Aktivieren einer neuen Version wird die vorherige **automatisch deaktivieren**.

## 3. Vorschau-Funktion (Vorschau analysiertes XML)

Die **Vorschau-Funktion** ermöglicht es Ihnen, zu testen und zu überprüfen, wie eine hochgeladene EDI-Datei unter Verwendung der aktuellen Struktur-Deskriptor-Datei analysiert wird.

#### Verwendung

* Laden Sie eine EDI-Datei über den Standard-Upload-Flow hoch.
* Kopieren Sie die **Dokumenten-ID** der hochgeladenen Datei.
* Navigieren Sie zur Benutzeroberfläche der **Struktur-Deskriptor-Datei**.
*   Öffnen Sie die **Vorschau-Funktion**.\


    <div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F9lddYJl2G4tzpdr9RD5F%252Fimage.png%3Falt%3Dmedia%26token%3Df7663f70-ef10-4e64-bbdc-41048ed8352a&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=36ce2b93&#x26;sv=2" alt="" width="375"></div>
* Geben Sie die **Dokumenten-ID** in das Feld ein und drücken Sie **Test**.
* Die resultierende **strukturierte XML-Ausgabe** wird angezeigt.

Dies ist besonders nützlich zum Debuggen von Zuordnungen und zur Validierung von strukturellen Gruppierungen in Echtzeit.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FBXU6zeFapt7ZIVFl37Iz%252Fimage.png%3Falt%3Dmedia%26token%3D9d51e329-b781-4781-a527-3258f6f933c6\&width=768\&dpr=4\&quality=100\&sign=4ca17281\&sv=2)

## 6. Video-Anleitung

Eine Videoanleitung für diesen Dateityp finden Sie auf der [Videos-Seite.](https://docs.docbits.com/administration-and-setup/settings/global-settings/document-types/edi/edi/edi-videos) Verwenden Sie sie, um die Einrichtung, Bearbeitung und Vorschau zu verfolgen.
