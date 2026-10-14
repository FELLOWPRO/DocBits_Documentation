# EDI-Transformationsdatei-Anleitung

## 1. Überblick

Die **Transformationsdatei** definiert, wie das strukturierte XML, das mit der **Strukturdeskriptordatei** erstellt wurde, in ein benutzerdefiniertes XML-Format umgewandelt wird, das den spezifischen Dokumententypen oder Formularanforderungen Ihrer Organisation entspricht.

Diese Transformation wird mithilfe von **XSLT (Extensible Stylesheet Language Transformations)** durchgeführt, die im DocBits-Interface mit dem **XSLT-Editor** erstellt und gewartet werden können.

## 2. Zweck und Funktion

* Wandelt das **Zwischen-XML** (Ausgabe des Strukturdeskriptors) in ein **endgültiges XML** um, das mit Ihrem Dokumentschema übereinstimmt.
* Ermöglicht die Flexibilität, um verschiedene EDI-Partnerformate und interne Systemanforderungen anzupassen.
* Wird mit **XSLT-Regeln** erstellt, die es Ihnen ermöglichen, Zuordnungen, Wertformatierungen, bedingte Logik und Struktur zu definieren.

## 3. Zugriff und grundlegende Bearbeitung

#### Dateizugriff

1.  Gehen Sie zu **Einstellungen → Dokumententyp** → \[Ihr Dokument (z. B. _Bestellung_)] → **E-Dok.**

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F1yCRagLzRFmy2hPRDDc1%252Fimage.png%3Falt%3Dmedia%26token%3D020874a9-1eae-4965-9dd2-c23461fc5884\&width=768\&dpr=4\&quality=100\&sign=5e53a730\&sv=2)
2. Wählen Sie unter dem **E-Dok**-Tab Ihr Format aus (z. B. **EDI**).
3.  Klicken Sie auf **Transformation**, um anzuzeigen oder zu bearbeiten.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FZtaE4dZT9E1exWMZ5FCI%252Fimage.png%3Falt%3Dmedia%26token%3D787868b4-47b4-455e-9a26-112f692b91f3\&width=768\&dpr=4\&quality=100\&sign=460124f1\&sv=2)

#### Entwurfsverwaltung

* **Entwurf erstellen**: Klicken Sie auf das ✏️ Stiftsymbol.
* **Entwürfe löschen**: Verwenden Sie das 🗑️ Papierkorb-Symbol, um nicht verwendete Entwürfe zu entfernen.
* **Änderungen aktivieren**: Klicken Sie auf das ✅ Häkchen, um eine Version zu veröffentlichen.
  * **Hinweis**: Das Aktivieren einer neuen Version deaktiviert die vorherige **automatisch**.

## 4. XSLT-Editor

Die Transformationsdatei wird mithilfe eines integrierten **XSLT-Editors** bearbeitet, der Syntaxhervorhebung und Validierung unterstützt.

* Fügen Sie Vorlagen hinzu, um spezifische Pfade aus dem Eingabe-XML auf die gewünschte Struktur abzubilden.
* Verwenden Sie bedingte Logik (z. B. `<xsl:if>`, `<xsl:choose>`) zur Behandlung optionaler oder variabler Datenformate.
* Wenden Sie Formatierungsfunktionen bei Bedarf an (z. B. Zeichenkettenmanipulation, Datumsformatierung).

## 5. Vorschau-Funktion (Vorschau des transformierten XML)

Die **Vorschau-Funktion** ermöglicht es Ihnen, zu testen und zu überprüfen, wie eine hochgeladene EDI-Datei mithilfe der aktuellen **Transformationsdatei** verarbeitet wird.

#### Verwendung

* Laden Sie eine EDI-Datei über den Standard-Upload-Flow hoch.
* Kopieren Sie die **Dokumenten-ID** der hochgeladenen Datei.
* Navigieren Sie zur **Transformationsdatei**-Schnittstelle.
*   Öffnen Sie die **Vorschau-Funktion**.\


    <div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F9lddYJl2G4tzpdr9RD5F%252Fimage.png%3Falt%3Dmedia%26token%3Df7663f70-ef10-4e64-bbdc-41048ed8352a&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=36ce2b93&#x26;sv=2" alt="" width="375"></div>
* Geben Sie die **Dokumenten-ID** in das Feld ein und drücken Sie **Test**.
* Die resultierende **transformierte XML-Ausgabe** wird angezeigt.

Dies ist besonders nützlich zum Debuggen von XSLT-Zuordnungen und zur Sicherstellung, dass die endgültige XML-Struktur Ihren Formatanforderungen entspricht.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FWbwwmXgp6nRPIb1zBpgj%252Fimage.png%3Falt%3Dmedia%26token%3Dab5766f1-45bf-484e-9aa4-ab3059705591\&width=768\&dpr=4\&quality=100\&sign=46905864\&sv=2)

## 6. Video-Anleitung

Eine Videoanleitung für diesen Dateityp finden Sie auf der [Videos-Seite.](https://docs.docbits.com/administration-and-setup/settings/global-settings/document-types/edi/edi/edi-videos) Verwenden Sie sie, um die Einrichtung, Bearbeitung und Vorschau zu verfolgen.
