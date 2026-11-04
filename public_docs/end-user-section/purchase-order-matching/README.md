# Bestellnummer Abgleich Bildschirm

## Übersicht

Im **Bestellnummer Abgleich** Bildschirm können Sie die Positionen, die aus Ihrem Dokument extrahiert wurden, mit denen vergleichen, die im **Infor-System** gespeichert sind, wobei die Bestellnummer als Referenz dient.

Sie können:

* **Unterschiede** zwischen extrahierten und gespeicherten Daten sofort erkennen
* **Toleranzen festlegen**, um akzeptable Abweichungen zuzulassen
* **Bestimmte Status** von Infor ignorieren, falls erforderlich
* Das Dokument nach einem erfolgreichen Abgleich **genehmigen und exportieren**
* Das Dokument **ablehnen**, wenn die Daten die erforderlichen Validierungskriterien nicht erfüllen

Diese Seite führt Sie durch den Prozess des Bestellnummer Abgleichs und erklärt alle verwandten Funktionen, die in diesem Abschnitt verfügbar sind.

## Werkzeuge im Bestellnummer Abgleich Bildschirm

Oben im Bestellnummer Abgleich Bildschirm finden Sie mehrere Werkzeuge – wie **Speichern**, **Automatischer Abgleich**, **Exportieren** und andere –, die den Abgleichsprozess unterstützen.\
Eine detaillierte Beschreibung jedes Werkzeugs und seiner Funktionalität finden Sie [hier](../../end-user-and-partner-section/end-user-section/purchase-order-matching/purchase-order-matching-tools.md).

![](../../.gitbook/assets/po_match_tools_0_de.png)

## Filter und Hinzufügen von Bestellnummern

Sie können nach bestimmten Bestellnummern suchen, indem Sie die Nummer in das Suchfeld eingeben.\
Für eine verfeinerte Filterung klicken Sie auf das Symbol auf der rechten Seite der Suchleiste, um spezifische Kriterien für Ihre Suche auszuwählen.

![](../../.gitbook/assets/po_match_3_de.png)

Die folgenden Filteroptionen stehen zur Verfügung, um Ihnen bei der Verfeinerung Ihrer Suche nach Bestellungen zu helfen:

* **Schlüsselwort** – Nach Bestellnummern filtern.
* **Lieferant** – Nach Lieferantennamen oder -ID filtern.
* **Nach Datum** – Bestellungen anzeigen, die nach einem bestimmten Datum erstellt wurden.
* **Vor Datum** – Bestellungen anzeigen, die vor einem bestimmten Datum erstellt wurden.
* **Mindestbestellwert** – Nach Mindestbestellwert filtern.
* **Maximaler Bestellwert** – Nach maximalem Bestellwert filtern.
* **Sortieren nach** – Attribut auswählen, nach dem die Ergebnisse sortiert werden sollen (z. B. Datum, Betrag).
* **Richtung sortieren** – Sortierreihenfolge wählen: aufsteigend oder absteigend.
* **Anzahl der anzuzeigenden Datensätze** – Definieren, wie viele Ergebnisse pro Seite angezeigt werden sollen.
* **Mehr** – Zusätzliche Filteroptionen umfassen:
  * **Nummer der Lieferung**
  * **Packzettel-Nummer**
  * **Artikel-ID**

Nachdem Sie Ihre Filter konfiguriert haben, klicken Sie auf **Anwenden**, um sie anzuwenden, oder auf **Löschen**, um alle Filtereinstellungen zurückzusetzen.

Die übereinstimmenden Bestellungen werden basierend auf den angewendeten Filtern angezeigt.\
Sie können entweder:

* Die Filter anpassen und erneut suchen oder
* Doppelklicken Sie auf einen Bestellposten, um ihn zum Bestellnummer Abgleich Bildschirm hinzuzufügen.

![](../../.gitbook/assets/po_match_5_de.png)

## Bestellnummern auswählen und Spalten anordnen

Sie können zwischen einzelnen Bestellungen wechseln, um deren jeweilige Positionen anzuzeigen, indem Sie auf die Bestellnummer oben in der Tabelle klicken.

Sie können auch die Spalten innerhalb jeder Bestellansicht anordnen, indem Sie sie einfach per Drag & Drop in Ihre bevorzugte Reihenfolge ziehen.

![](../../.gitbook/assets/po_match_7_de.png)

Um bestimmte Spalten dauerhaft auszublenden, verwenden Sie die [**Spalten der PO-Tabelle für die Organisation festlegen**](./#spalten-der-po-tabelle-fur-organisationen-festlegen) Funktion.

## Spalten der PO-Tabelle für Organisationen festlegen

Sie haben die Möglichkeit, bestimmte Spalten in der Bestelltabelle auszublenden oder anzuzeigen, indem Sie auf das Spalteneinstellungs-Symbol (siehe unten) klicken.\
Diese Einstellung ist sowohl im **Bestellnummer Abgleich** Bildschirm als auch im Menü **Erweiterte Bestellsuche** verfügbar.

![](<../../.gitbook/assets/po_tools_new_10_de (1).png>)

Zusätzliche Details finden Sie [hier](../../end-user-and-partner-section/end-user-section/purchase-order-matching/purchase-order-matching-tools.md#spalten-der-po-tabelle-fur-die-organisation-festlegen).

## Bestellnummer mit Infor neu synchronisieren

Um die Daten in **DocBits** mit den Daten von **Infor** zu synchronisieren, klicken Sie auf die **Aktualisieren**-Schaltfläche neben der Bestellnummer über der Tabelle.

![](../../.gitbook/assets/po_match_8_de.png)

Wenn Ihr Abgleichprozess auf dem Attribut **Empfangene Lieferung Offene Menge** basiert, haben Sie auch die Möglichkeit, eine **manuelle Synchronisierung** durchzuführen, wie im Detail [hier](../../end-user-and-partner-section/end-user-section/purchase-order-matching/purchase-order-matching-tools.md#daten-synchronisieren) beschrieben.

![](../../.gitbook/assets/po_tools_new_7_de.png)

## Wie abgleichen?

Um einen Bestellposten mit einem aus dem Dokument extrahierten Posten abzugleichen, haben Sie drei Optionen:

1. **Drag and Drop**\
   Ziehen Sie den gewünschten Bestellposten und lassen Sie ihn auf den entsprechenden Posten in der extrahierten Tabelle fallen.
2. **Rechtsklick und Verbinden**
   * Klicken Sie mit der rechten Maustaste auf den Bestellposten, den Sie abgleichen möchten, und wählen Sie **Für Abgleich auswählen**.
   * Klicken Sie dann mit der rechten Maustaste auf den entsprechenden Posten in der extrahierten Tabelle und wählen Sie **Verbinden**.
3.  **Automatischer Abgleich**

    Klicken Sie auf die Schaltfläche **Automatischer Abgleich**, um das System automatisch zu versuchen, alle Posten basierend auf den extrahierten und Bestelldaten abzugleichen.

    ![](../../.gitbook/assets/po_tools_new_5_de.png)

Sie können auch **mehrere Bestellposten** auswählen und diese mit einem **einzelnen Posten** in der extrahierten Tabelle abgleichen. Für weitere Details klicken Sie [hier](./#mehrfachabgleiche).

## Welche Spalten werden abgeglichen?

Der Bestellnummer Abgleich Prozess gleicht nur bestimmte Spalten ab. Die folgende Liste zeigt, welche Spalten abgeglichen werden, sofern verfügbar. Wenn keine [Toleranz](./#toleranzen-akzeptieren) festgelegt ist, werden die Spalten nur abgeglichen, wenn sie eine exakte (100%) Übereinstimmung aufweisen.

* [Menge](./#menge) (Menge | Empfangene Menge | Empfangene Lieferung Offene Menge)
* Einzelpreis
* Bestellnummer
* Artikelnummer/Lieferantenartikel-ID
* Bestätigtes Lieferdatum

### Menge

Sie haben drei Optionen für den Abgleich der Menge.

* Menge
* Empfangene Menge
* Empfangene Lieferung Offene Menge

Sie können diese Option in **Einstellungen → Globale Einstellungen → Dokumenttypen → Weitere Einstellungen → Bestellabschnitt → Bestellnummer** festlegen.

Die ausgewählte Mengenoption bestimmt, welche **Spalte für die Bestellmenge** während des Abgleichprozesses verwendet wird.

## **Status der verbrauchten Bestellposition**

Diese Funktion fügt den Bestellpositionen Farbcodierungen hinzu, um ihren Abgleichstatus auf einen Blick einfacher identifizieren zu können. Weitere Informationen finden Sie auf der [**Seite zum Status der verbrauchten Bestellposition**](../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/consumed-po-line-status.md).

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FNoof3pErQqAvAWZpo4Fd%252Fimage.png%3Falt%3Dmedia%26token%3D21a15672-8e84-4e22-a0f2-8b65bcbfda54\&width=768\&dpr=4\&quality=100\&sign=4a68abca\&sv=2)

## **Abschnitt** Versandauftrag

Dieser Abschnitt bietet einen visuellen Überblick darüber, wie viel für jedes Bestellposition geliefert und in Rechnung gestellt wurde. Es hilft, den Rechnungsfortschritt mithilfe von Mengenwerten und einer Fortschrittsleiste zu verfolgen.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F2R9tB3JySdIMk8meRSVZ%252FPO-Shipment-Order-1.jpg%3Falt%3Dmedia%26token%3D70aa50f4-84cd-4a55-b580-037b893d1f5b\&width=768\&dpr=4\&quality=100\&sign=e4619335\&sv=2)

Weitere Details finden Sie auf der [**Seite zur Versandauftrags-Einstellung**](../../administration-and-setup/settings/document-processing/module/po-shipment-order-setting.md).

## Toleranzen akzeptieren

Sie können akzeptable Toleranzniveaus während des Abgleichprozesses festlegen.\
Standardmäßig werden nur exakte (100%) Übereinstimmungen als gültig betrachtet.

Wenn Toleranzen in den Systemeinstellungen konfiguriert sind, können Sie diese für die zulässigen Attribute direkt in der **Extrahierten Tabelle** unter der Spalte **Aktionen** anpassen.

![](../../.gitbook/assets/po_match_11_de.png)

Für weitere Informationen zur Konfiguration und Verwendung von Toleranzen siehe die [detaillierte Dokumentation](../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-tolerance-settings-additional-purchase-order-tolerance.md).

## Rabatte

Wenn Rabatte in Ihrer extrahierten Tabelle vorhanden sind, werden sie automatisch auf den Einzelpreis vor dem Abgleich angewendet – es sei denn, es werden [Mehrfachabgleiche](./#mehrfachabgleiche) verwendet. Weitere Informationen zu Rabatten finden Sie [hier](../../end-user-and-partner-section/end-user-section/purchase-order-matching/discounts.md).

## Status deaktivieren

Sie können bestimmte Zeilen mit bestimmten Status vom Abgleich ausschließen. Für weitere Informationen siehe die [detaillierte Dokumentation](../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-disable-statuses.md).

## Abgeglichene Zeilen überprüfen

Mehrere Indikatoren stehen zur Verfügung, um Ihnen zu helfen zu überprüfen, ob ein Posten erfolgreich abgeglichen wurde oder nicht.

### Bestelltabelle

![](../../.gitbook/assets/po_match_14_de.png)

* Dieses Symbol zeigt an, dass der Bestellposten erfolgreich abgeglichen wurde.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F2vcst2wCfyck9Z7ak4eO%252Fguide_po_2.png%3Falt%3Dmedia%26token%3D78f7a224-ba6b-4027-b6a0-61e5502fd7c2\&width=768\&dpr=4\&quality=100\&sign=e0d60903\&sv=2)

* Dieses Symbol zeigt an, dass der Bestellposten eine Abweichung enthält.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FAb1A9PwBhrvfAf5q7f5w%252Fguide_po_5.png%3Falt%3Dmedia%26token%3D6616b59d-ffa4-4202-9382-3ac8ecd8b913\&width=768\&dpr=4\&quality=100\&sign=dd476496\&sv=2)

### Extrahierte Tabelle aus dem Dokument

*   Dieses Symbol zeigt an, dass der Posten erfolgreich abgeglichen wurde. Sie können über das Symbol fahren, um den entsprechenden Bestellposten hervorzuheben.

    ![](../../.gitbook/assets/po_match_15_de.png)
*   Dieses Symbol zeigt an, dass der Posten eine Abweichung enthält. Sie können über das Symbol fahren, um den entsprechenden Bestellposten hervorzuheben und die Spalten anzuzeigen, in denen Abweichungen auftreten.

    ![](../../.gitbook/assets/po_match_new_4_de.png)

## Mehrfachabgleiche

Der Mehrfachabgleich ermöglicht es, mehrere Zeilen aus einer Tabelle mit einer einzelnen Zeile in der entsprechenden (entgegengesetzten) Tabelle abzugleichen.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/po_match_20.png)

Diese Funktion ist besonders nützlich für Szenarien, in denen Details über mehrere Positionen verteilt sind.

### Abgleichkriterien

Zeilen werden als übereinstimmend betrachtet, wenn die folgenden aggregierten Bedingungen erfüllt sind:

* **Stückpreis**:\
  Der durchschnittliche Stückpreis der mehreren Zeilen wird berechnet und mit dem Stückpreis in der entgegengesetzten Tabelle verglichen.
* **Menge**:\
  Die Summe der Mengen über die abgeglichenen Zeilen muss mit der Menge in der entgegengesetzten Tabelle übereinstimmen.
* **Zusätzliche Anforderungen**:\
  Alle zusätzlichen [Abgleichkriterien](./#welche-spalten-werden-abgeglichen) müssen ebenfalls erfüllt sein.

Wenn ein einzelner Posten mit mehreren Zeilen abgeglichen wird, können Sie detaillierte Informationen anzeigen, indem Sie auf das Plus (+) Symbol neben dem jeweiligen Posten klicken.

Dies erweitert die Ansicht, um alle abgeglichenen Einträge anzuzeigen, und hilft Ihnen, mehrere Abgleiche effektiv zu überprüfen und zu verwalten.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FXueoHfU6EiDKaWBKJL2X%252Fpo_match_19.png%3Falt%3Dmedia%26token%3D9b947abd-5fbc-45e7-8e55-8b38746b5e32\&width=768\&dpr=4\&quality=100\&sign=191a712\&sv=2)

![](../../.gitbook/assets/po_match_18_de.png)

## PO-Verbindungen entfernen

Um eine Verbindung zwischen einem Bestellposten und einem extrahierten Posten zu entfernen, klicken Sie einfach auf das **X**-Symbol neben dem abgeglichenen Paar.\
Sobald entfernt, wird die Verbindung aufgehoben und der Posten wird wieder für den Abgleich verfügbar.

![](../../.gitbook/assets/po_match_new_2_de.png)

## Berechnung

Unter der Tabelle mit den Informationen, die aus Ihrem Dokument extrahiert wurden, finden Sie einfache Berechnungen, um zu überprüfen, ob die Gesamterfassungen übereinstimmen.

![](<../../.gitbook/assets/po_rules_1_de (1).png>)

### Erfasste Buchungen:

Der Wert der erfassten Buchungen ergibt sich aus dem Nettobetrag, der aus dem Dokument extrahiert wurde.

```
Erfasste Buchungen = Nettobetrag insgesamt (aus dem Dokument extrahiert)
```

### Abgestimmte Summe:

Dieser Wert wird berechnet, indem der **Einzelpreis** × **Menge** für alle Posten summiert wird, die erfolgreich mit den Posten aus der Bestellnummer abgeglichen wurden.

```
 Abgestimmte Summe = Summe von (Einzelpreis × Menge) für alle abgeglichenen Posten
```

### **Gebühren:**

Alle anfallenden Gebühren werden in diesem Abschnitt aufgeführt, falls vorhanden.\
Für weitere Details siehe die [detaillierte Dokumentation](../../admin-section/settings/document-processing/classification-and-extraction/table-extraction-for-costing-element.md).

```
Gebühren = Kostenelement
```

### Offener Betrag:

Die resultierende Differenz wird hier angezeigt und wie folgt berechnet:

```
Offener Betrag = Erfasste Buchungen - Abgestimmte Summe - Kostenelement
```

## Dokument zur Validierung anzeigen

Auf der rechten Seite des **Bestellnummer Abgleich** Bildschirms können Sie das Dokument zur Unterstützung bei der Validierung anzeigen.

![](../../.gitbook/assets/po_new_1_de.png)

**Funktionen der Dokumentenansicht Toolbar:**

* Durchblättern der Dokumentseiten, um den Inhalt zu überprüfen.
* Klicken Sie auf den Dateinamen, um den vollständigen Validierungsbildschirm zu öffnen.
* Geben Sie eine Seitenzahl ein und drücken Sie die Eingabetaste, um direkt zu dieser Seite zu springen.
* Verwenden Sie die Plus (+) und Minus (–) Tasten, um in das Dokument hinein- oder herauszuzoomen.
*   Klicken Sie auf die Schaltfläche ganz rechts, um das Dokument in einem separaten Fenster zu öffnen, was besonders nützlich ist, wenn Sie mit mehreren Bildschirmen arbeiten.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F8nUElRimoIOprR5yV5lN%252Fpo_match_10.png%3Falt%3Dmedia%26token%3De0d6924c-127f-4333-95f9-1b32d52b0da5\&width=768\&dpr=4\&quality=100\&sign=4f8161e4\&sv=2)

## Änderungen speichern:

Um Ihre Änderungen zu speichern, klicken Sie auf die Schaltfläche **Speichern** in der Toolbar.\
Wenn Sie die Seite ohne Speichern verlassen, gehen alle Fortschritte, die während des Abgleichprozesses gemacht wurden, verloren.

![](<../../.gitbook/assets/po_tools_new_12 (1).png>)

## Dokument exportieren

Nachdem Sie alle Positionen abgeglichen und deren Richtigkeit validiert haben, können Sie das Dokument exportieren, indem Sie auf die Schaltfläche **Exportieren** in der Toolbar klicken.

* Ein Klick auf den kleinen Pfeil neben der Schaltfläche **Exportieren** zeigt alle verfügbaren Exportoptionen an.
* Ein Klick auf **Exportieren** direkt löst die Standard-Exportoption aus (die erste in der Liste).

![](<../../.gitbook/assets/po_tools_new_8_de (1).png>)
