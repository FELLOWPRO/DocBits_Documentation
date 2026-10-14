# Weitere Einstellungen

## Übersicht

Im Abschnitt "Weitere Einstellungen" finden Sie verschiedene Optionen für einzelne Belegtypen. Sobald eine Einstellung aktiviert ist, gilt sie nur für diesen speziellen Belegtyp. Diese Seite bietet einen kurzen Überblick über die Funktionen der einzelnen Einstellungen.

## Zugriff

1.  Navigieren Sie zu **Ayarlar** → **Globale Einstellungen** → **Belegtypen**.

    <figure><img src="../../../../../.gitbook/assets/disablpe_po_status_1.png" alt=""><figcaption></figcaption></figure>
2.  Wählen Sie den gewünschten Belegtyp aus und klicken Sie auf **Weitere Einstellungen**.

    <figure><img src="../../../../../.gitbook/assets/Calculate_PO_unit_price_2.png" alt=""><figcaption></figcaption></figure>

## Tabellenextraktion

* **Tabellenvalidierung überspringen**: Ermöglicht die Umgehung des Standard-Validierungsprozesses für Tabellendaten. Diese Option ist in Szenarien nützlich, in denen eine flexible Datenhandhabung erforderlich ist oder wenn bestimmte Validierungsschritte übersprungen werden können, um die Leistung bei der Datenverarbeitung zu verbessern.

## Dublettenerkennung

* [**Erkennung doppelter Belege**](duplicate-document-handling.md): Hier können Sie doppelte Belege erkennen und verarbeiten.

## In Prüfung (In Review)

* **Formular "In Prüfung" entwerfen**: Konfigurieren Sie das Layout von Prüfformularen mit dem **Layout Builder**. Dieses Layout bestimmt, wie Inhalte während des Belegprüfprozesses präsentiert werden. Detaillierte Anweisungen zur Verwendung des **Layout Builders** finden Sie [hier](../../../../setup/document-types/layout-builder.md).

## Ablehnen (Reject)

* **Ablehnungsformular entwerfen**: Konfigurieren Sie mit dem **Layout Builder** das Layout für das Ablehnungsformular, das während des Belegprüfprozesses angezeigt wird. Detaillierte Anweisungen zur Verwendung des **Layout Builders** finden Sie [hier](../../../../setup/document-types/layout-builder.md).

## PDF-Exportformat

* **Export-Dateiformat**: Ermöglicht die Festlegung des PDF-Formats, das beim Exportieren von Belegen verwendet werden soll.

## Genehmigung (Approval)

* **Vor dem Export genehmigen**: Stellt sicher, dass Belege genehmigt werden müssen, bevor sie aus dem System exportiert werden können. Sie können auch das Layout des Genehmigungsbildschirms mit dem **Layout Builder** konfigurieren. Detaillierte Anweisungen zur Verwendung des **Layout Builders** finden Sie [hier](../../../../setup/document-types/layout-builder.md).
* **Vor dem Export genehmigen V2**: Aktiviert Approval V2, das die Verwendung dynamischer Felder anstelle statischer Felder unterstützt. Sie können das Layout des Genehmigungsbildschirms ebenfalls mit dem **Layout Builder** anpassen. Detaillierte Anweisungen zur Verwendung des **Layout Builders** finden Sie [hier](../../../../setup/document-types/layout-builder.md).
* **Zweitgenehmigung**: Fügt eine zusätzliche Genehmigungsebene für eine verbesserte Validierung und eine größere Kontrolle über die Belegverarbeitung hinzu. Sie können das Layout des Genehmigungsbildschirms ebenfalls mit dem **Layout Builder** anpassen. Detaillierte Anweisungen zur Verwendung des **Layout Builders** finden Sie [hier](../../../../setup/document-types/layout-builder.md).
* [**Genehmigungsstempel**](approval/approval-stamp.md): Fügt dem Beleg einen Stempel hinzu, wenn er genehmigt wird.
* [**Genehmigungshistorie**](approval/approval-history.md): Ermöglicht die Anzeige der Genehmigungshistorie sowohl im Genehmigungsbildschirm als auch in der Feldvalidierung.

## Bestellung (Purchase Order)

* [**PO-Tabelle im Layout Builder**](purchase-order/po-table-in-layout-builder.md): Ermöglicht die Einbindung von Bestellungstabellen in den Layout Builder für angepasste Beleglayouts.
* [**Automatisches Prüfen auf PO-Updates**](purchase-order/auto-check-for-po-updates.md): Wenn aktiviert, zeigt das System im Bildschirm für den Bestellabgleich einen visuellen Indikator an, wenn eine Bestellung aktualisiert wurde, und fordert die Benutzer auf, die Daten zu aktualisieren.
* **PO-Daten automatisch aktualisieren**: Durch die Aktivierung werden die Bestelldaten automatisch aktualisiert, wenn neue Daten verfügbar sind.
* [**Status verbrauchter PO-Positionen**](purchase-order/consumed-po-line-status.md): Diese Einstellung verbessert den Bildschirm für den Bestellabgleich durch Farbcodierung der Bestellungspositionen.
* [**PO-Einzelpreis berechnen**](purchase-order/calculate-po-unit-price.md): Ermöglicht die Berechnung des PO-Einzelpreises anhand des Nettobetrags und der Menge, anstatt ihn zu extrahieren.
* [**Bestellung**](purchase-order/purchase-order.md): Schaltet um, ob der Beleg im Bildschirm für den Bestellabgleich verarbeitet werden soll. Sie können auch angeben, auf welchem Mengenbegriff der Abgleichprozess basieren soll.
* [**Nicht abgeglichene PO-Positionen exportieren**](purchase-order/export-not-matched-po-lines.md): Diese Funktion steuert den Export von Bestellungspositionen. Wenn deaktiviert, werden nur abgeglichene Positionen exportiert. Wenn aktiviert, werden alle Bestellungspositionen exportiert, auch wenn sie nicht mit einer Auftragsbestätigungsposition abgeglichen wurden.
* [**PO-Toleranzeinstellung**](purchase-order/purchase-order-tolerance-settings-additional-purchase-order-tolerance.md): Mit dieser Funktion können Sie Toleranzstufen für Menge und Einzelpreis festlegen, um geringfügige Abweichungen zu akzeptieren, ohne sie als Nichtübereinstimmung zu markieren.
* [**Zusätzliche PO-Toleranzeinstellung**](purchase-order/purchase-order-tolerance-settings-additional-purchase-order-tolerance.md#einstellung-zur-konfiguration-zusatzlicher-bestelltoleranzeinstellungen): Mit dieser Funktion können Sie zusätzliche Toleranzstufen für Fracht, Gebühren und Steuern festlegen.
* [**Alternativer Export**](purchase-order/alternate-export.md): Ermöglicht die Einrichtung eines alternativen Exports für bestimmte Status.
* [**PO-Status deaktivieren**](purchase-order/purchase-order-disable-statuses.md): Ermöglicht es, bestimmte Status von der Berücksichtigung im Abgleichprozess auszuschließen.
* **Bereits abgeglichene Positionen ignorieren**: Durch die Aktivierung werden Positionen, die bereits abgeglichen wurden, bei einem neuen Abgleichprozess übersprungen.
* [**Belegbestellstatus aktualisieren**](purchase-order/update-document-purchase-order-status.md): Wenn aktiviert, wird die Spalte "PO-Status" auf dem Dashboard automatisch aktualisiert, wenn sich der Status der Bestellung ändert.
* [**Mapping der Lieferantenartikelnummer**](purchase-order/supplier-item-number-map-admin-documentation.md): Eine Dienstprogrammeinstellung, die Lieferantenartikelnummern internen Artikelnummern zuordnet und so die Genauigkeit in der Bestands- und Bestellverwaltung gewährleistet.
