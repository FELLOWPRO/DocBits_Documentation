# Aktualisieren des Dokuments Bestellstatus

## Überblick

Wenn aktiviert, wird die **PO-Status**-Spalte im Dashboard automatisch aktualisiert, wenn sich der Status der Bestellung ändert.

## Wo zu aktivieren

1. Gehe zu: **Einstellungen** → **globale Einstellungen** → **Dokumententyp**
2.  Wähle den gewünschten Dokumententyp aus und klicke auf **Weitere Einstellungen**.\


    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fsd3ebb3IETh7wNSA5flh%252Fimage.png%3Falt%3Dmedia%26token%3D6f1d286b-e006-4b23-9866-9ed37bf2bdaa\&width=768\&dpr=4\&quality=100\&sign=b0f0b121\&sv=2)
3.  Gehe im Abschnitt **Bestellung** zu der Option **Dokument Bestellstatus aktualisieren**.\


    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FSsFkQ46Jd4tn0WGqNSjk%252Fimage.png%3Falt%3Dmedia%26token%3D51ee4f2d-76ae-42b4-a748-f0e9d340b329\&width=768\&dpr=4\&quality=100\&sign=e0f4b1af\&sv=2)

## Wie es funktioniert

Wenn diese Einstellung aktiviert ist, wird die **PO-Status**-Spalte im Dashboard automatisch den aktuellen Status der Bestellung widerspiegeln. Wenn beispielsweise der PO-Status auf _Empfangen_ oder _In Rechnung gestellt_ aktualisiert wird, wird die Dashboard-Spalte entsprechend aktualisiert, um diesen neuen Status anzuzeigen.

<div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FmWZIOi5pqWyeagCfiXgy%252FStatus%2520on%2520Dashboard.jpg%3Falt%3Dmedia%26token%3D3aad59e7-d249-4f07-afa3-c68429128cec&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=6cde440e&#x26;sv=2" alt="" width="375"></div>

## Einrichtung

1. **Aktiviere die Einstellung** Gehe zu der oben genannten Stelle und schalte die Einstellung ein.
2. **Füge die PO-Status-Spalte hinzu (falls nicht sichtbar)** Wenn die **PO-Status**-Spalte noch nicht im Dashboard sichtbar ist:
   *   Gehe zu: **Erweiterte Einstellungen** → **Tabellenspalten für Organisationen festlegen**\


       ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fn6GyECCtvUeKLYd6FkEH%252Fimage.png%3Falt%3Dmedia%26token%3Da023deba-748f-4140-bb33-17483c91f2cf\&width=768\&dpr=4\&quality=100\&sign=164eb544\&sv=2)
   * Füge das Feld aus dem Dokumententyp hinzu, indem du nach **PO-Status** suchst
3. **Konfiguriere die Suchkonfiguration**
   *   Konfiguriere das Statusfeld im Bestellkopf nach folgendem Muster:\


       ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Folrh285NuJO787Udc80C%252Fimage.png%3Falt%3Dmedia%26token%3Def5abe46-fe94-4946-a893-66f7ca21322b\&width=768\&dpr=4\&quality=100\&sign=415e657e\&sv=2)
   * **Hinweis:** **Die Bestellung muss auf Auto Trigger stehen, da Statusaktualisierungen sonst möglicherweise nicht korrekt aktualisiert werden**
   * Weißt du nicht, wie man die **Suchkonfiguration konfiguriert? Hier ist der** [**Suchkonfigurationsleitfaden**](../../../../../setup/document-types/fuzzy-data-configuration-with-master-data.md)
4. **Überprüfen** Empfange oder stelle eine Bestellung in Rechnung und überprüfe dann das Dashboard, um zu bestätigen, dass der Status korrekt aktualisiert wurde.
