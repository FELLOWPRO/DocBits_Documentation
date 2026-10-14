# Strukturierung und Verbesserung der Tabellenauswertung in DocBits

Sobald eine Tabelle extrahiert und die initiale Spaltenzuordnung abgeschlossen ist, können Sie die Qualität und Struktur der Daten mithilfe mehrerer integrierter Tools verbessern. Dieser Leitfaden führt Sie durch:

* Gruppierung von Zeilen
* Manuelle Zeilenauswahl
* Spaltenzuordnung
* Header-Verfeinerung mit Regex

Diese Tools sind besonders hilfreich bei komplexen oder inkonsistenten Dokumentlayouts.

## 1. Gruppierung von Zeilen

Dokumente wie Rechnungen oder Auftragsbestätigungen enthalten oft Tabelleneinträge, bei denen eine Spalte (z. B. eine Beschreibung) mehrere Zeilen umfasst, während andere Spalten (z. B. Menge oder Preis) nur eine Zeile verwenden.

Nehmen Sie dieses Beispiel einer deutschen Rechnung - die Spalte "Bezeichnung" erstreckt sich über mehrere Zeilen:

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FVino2M4Esor3IRHGqBd5Brx7_lKPIwEOlRYBHzMXw4WoacFNW39hbWuwoUNGocubx4Bh9_BvUBqZSWA4U_NmU8FBw4Q1_AiTASgMx-2MLKvsHLJY057oqyks0fQ5b7mI577JTX5rBKdEG90O9F5TcoU\&width=768\&dpr=4\&quality=100\&sign=ae0bd75a\&sv=2)

Zunächst extrahiert DocBits jede Zeile separat:

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FUX5OdkW59HPVROnNzSeZbDw4NYTPbfayDLIXBQi0pwHzUEJ1B5t7I9uKBNc0dmOB3Cile8Xv6AdgVXuUd0aMbQFGWagBCEetw8P-N4zgG_cGTjWHhpDtGQZg27UZKdCDJ5FeEDJgFAYtTB8kZrMSdho\&width=768\&dpr=4\&quality=100\&sign=b6990876\&sv=2)

Anschließend können Sie **Zeilen basierend auf einer Spalte gruppieren**, wie z. B. "Position". Dadurch werden zusammenhängende Zeilen zu einem einzigen strukturierten Eintrag zusammengeführt:

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FPxA6h2udUuYd1YmHV97t-bzfZzipFpdA5t8gjpGXWx9sA-I4tW3tYwD28icv88UEmitz0EAaWuGkU5ZwqAjcQnoOkmg9u1AcBJW3nITU6eFa0foHB-AQPb0qv0AWaaEwM6WvwaEcAODEUzKtvRZOMN0\&width=768\&dpr=4\&quality=100\&sign=36b99bc7\&sv=2)

## 2. Manuelle Zeilenauswahl

In einigen Fällen ist der Text auf einem Dokument über mehrere Spalten in einer Zeile verteilt, was eine automatische Zuordnung erschwert.

Hier ist ein Beispiel, bei dem die Zeile "PRAEF" **Bezeichnung**, **Menge**, **ME** und **Preis in EUR** überlappt:

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FLbVbmfdOBpeCWDftPvW0qjEHjbLmWYRrAGTZHVW8VEHQTEvl5GoqH2wkFE5iUOySmF50b1V8CDAZhfMzPTeMQscmc61SDKaqSCW-y0Z7fjlwOjhtjxWD44oCsgHmwrgrBD4cuEGgn9JY_UX3t9jRlPs\&width=768\&dpr=4\&quality=100\&sign=5ff4a2e1\&sv=2)

Zeilenverschiebung

### Wie man Werte manuell zuweist:

1.  **Training-Modus aktivieren**

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2F4D8iCXk0p_Mur8bX_11ne_2iA-GOxoFi2OQWlSEvrH1auoE0ksnYXpZx3Pw3PUJJRZJN85dnQlSSBB369FfafXAy8adjFZcnepQnODSaaIj69cxtUKFAXPgn5eyPE6jbJuzStJALMgumlt49Z1Pv3FY\&width=768\&dpr=4\&quality=100\&sign=232c58a9\&sv=2)
2.  **Aktivieren des Zeilenbearbeitungsmodus**\


    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2F8YQmo_WRuKKVjk1a_eoxSBiQr0GncuS4BmCA0aI9aOlrbsIvdj8dZlurxxBHp2lH4ozT4HPWw9qYDW7xLQ7u2DSyU8DrNzSBC7LjzKLTDJ2tudY9a_DENDoK5Aya6L1hcf1WF1RD92S_DzhGVV4Gh6Q\&width=768\&dpr=4\&quality=100\&sign=8fc5c089\&sv=2)


3.  **Text auswählen und zuordnen** Klicken Sie auf das richtige Textstück und weisen Sie es einem **blauen** Spaltenkopf zu.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2Fi2tlbwl9qFE0clthaoRPe7kcPRiURCvemuLEjBK4uAnfsR4auXbftMfEY1ZW5WXwezTBVSG5hbNRkddwIeLtrgJUvZoeKGdPKN8f75O_dPdIWkm4EFALfAj-evDUI3UKrgNOTNjF37C1bBLtE95OA1w\&width=768\&dpr=4\&quality=100\&sign=842a42\&sv=2)

> Hinweis: Violett markierte Spalten sind bereits systemmäßig zugeordnet und können nicht manuell bearbeitet werden.

## 3. Spaltenzuordnung

Die Spaltenzuordnung verknüpft Ihre extrahierten Daten mit den erwarteten Spaltenüberschriften, um Konsistenz und Exportierbarkeit sicherzustellen.

Um eine Spalte zuzuordnen oder neu zuzuordnen:

1. Klicken Sie auf den Spaltenheader in der Extraktionsansicht.
2. Wählen Sie die korrekte Zielspalte aus dem Dropdown-Menü.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FX_65pCWrI4HMFr_aiA0eoSDp-yIYy49lULzAZaiIgnr0aIowlLSed21MuehkGLs4UIdQousdfhiZi5pnQtpZ0uUn6dxlzii7WPQvov-kN1_Jimsi6U6zowOLxjBzZzZ47kaRhduAVBd_Ya9QQtXTpJ4\&width=768\&dpr=4\&quality=100\&sign=4e2a3bdc\&sv=2)

Sie können die Zuordnung so oft anpassen, wie es erforderlich ist.

## 4. Extrahieren von oben / unten

Einige Dokumente sind so strukturiert, dass relevante Tabellenwerte nicht in derselben Zeile wie andere Daten erscheinen. In solchen Fällen ermöglicht DocBits Ihnen zu steuern, **von wo die Daten extrahiert werden sollen**:

* **Von oben extrahieren**: Verwenden Sie dies, wenn der Wert für die aktuelle Zeile **in der Zeile darüber** erscheint.
* **Von unten extrahieren**: Verwenden Sie dies, wenn der Wert **in der Zeile unterhalb** der aktuellen Zeile erscheint.

**Wo Sie es finden**

1. Betreten Sie den **Training-Modus**.
2. Klicken Sie auf die drei Punkte (⋯) auf einem Spaltenheader.
3. Wählen Sie unter der Option **"Extrahieren von"** `Oben` oder `Unten`, abhängig vom Dokumentenlayout.

## 5. Betragsformat

Einige Spalten, wie **Menge** oder **Stückpreis**, enthalten numerische oder Datumsangaben, die je nach Herkunft oder Sprachraum des Dokuments unterschiedlichen Formatkonventionen folgen können. DocBits ermöglicht es Ihnen, das Format festzulegen, dem diese Werte folgen sollen, um eine genaue Extraktion und Interpretation sicherzustellen.

**Betragsformatoptionen:**

* Definieren Sie das erwartete Zahlen- oder Datumsformat für die Spalte, wie z. B. US (MM/TT/JJJJ, Dezimaltrennzeichen mit Punkt), Polen (TT.MM.JJJJ, Dezimaltrennzeichen mit Komma), Deutschland und andere.
* Dies hilft DocBits, Werte korrekt zu analysieren und zu standardisieren, auch wenn das Dokument ein anderes regionales Format verwendet.

**Wo Sie es finden**

1. Betreten Sie den **Training-Modus**.
2. Klicken Sie auf die drei Punkte (⋯) im Header einer unterstützten Spalte (z. B. Menge, Stückpreis).
3. Wählen Sie unter der Option **Betragsformat** das gewünschte Format entsprechend dem Sprachraum Ihres Dokuments aus.

## 6. Verbesserung der Tabellenauswertung mit Regex

## **Was es tut**

Diese Funktion ermöglicht es Ihnen, für jede Tabellenüberschrift ein Regex zu definieren, um die Extraktionsgenauigkeit zu verbessern und korrekte Ergebnisse sicherzustellen.

## **Wie man es benutzt**

1. Öffnen Sie ein Dokument vom Lieferanten, für den Sie ein Regex definieren möchten.
2.  Navigieren Sie zur Ansicht **Tabellenauswertung**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FDdlNrO6hG6jnEeWU9DuZ%252Fimage.png%3Falt%3Dmedia%26token%3Dca11a537-27a4-4b00-b3e7-f77540c28c2b\&width=768\&dpr=4\&quality=100\&sign=fd47355a\&sv=2)
3. Aktivieren Sie den **Training-Modus**.
4.  Wählen Sie die Tabellenüberschrift, die Sie verfeinern möchten, und wählen Sie dann **Regex**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fes6PsB9sHHXp0CNRj6YF%252Fimage.png%3Falt%3Dmedia%26token%3D6e31e4db-fd2f-487c-ac19-f1d6add81ad1\&width=768\&dpr=4\&quality=100\&sign=32264560\&sv=2)
5.  Es erscheint ein Popup, in dem Sie Ihr Regex eingeben und definieren können.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FWB7hjuuyVVAewRqrnhYj%252FiScreen%2520Shoter%2520-%2520Google%2520Chrome%2520-%2520250303135020.jpg%3Falt%3Dmedia%26token%3D6a31253d-18d7-4d8f-a00e-acd89a744127\&width=768\&dpr=4\&quality=100\&sign=d8d2d94a\&sv=2)
6.  Klicken Sie auf **Validieren**, um das Regex zu überprüfen, und dann auf **Änderungen speichern**, um es anzuwenden.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FC4R2o2W10ct1o0oesTLZ%252FiScreen%2520Shoter%2520-%2520Google%2520Chrome%2520-%2520250303135153.jpg%3Falt%3Dmedia%26token%3D43e53a05-53fe-4503-ba51-55c85910bd82\&width=768\&dpr=4\&quality=100\&sign=9ec6eb7b\&sv=2)
7. **Regel speichern und bestätigen**, um die Änderungen anzuwenden.

## Wann Sie jedes Feature verwenden sollten

Verwenden Sie diese Tools, um die Extraktionsgenauigkeit zu erhöhen und manuelle Arbeit zu reduzieren:

* **Gruppierung**: Wenn eine Beschreibung oder eine Spalte über mehrere Zeilen verläuft und für Klarheit kombiniert werden muss.
* **Manuelle Zeilenauswahl**: Wenn Zeilen nicht sauber strukturiert sind und Teile des Inhalts in falsche Spalten fallen.
* **Spaltenzuordnung**: Wenn die automatisch erkannten Spaltennamen nicht mit Ihrer Struktur übereinstimmen oder verfeinert werden müssen.
* **Regex-Regeln**: Wenn Tabellenüberschriften in Dokumenten desselben Lieferanten leicht variieren oder OCR Unstimmigkeiten einführt.
