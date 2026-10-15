# Weitere Einstellungen

## Übersicht

Unter **Weitere Einstellungen** finden Sie die Optionen, die zu einem einzelnen Dokumenttyp gehören, zum Beispiel zur Rechnung. Eine Einstellung, die Sie hier aktivieren, gilt nur für diesen Dokumenttyp. Die Seite besteht aus einklappbaren Karten, eine pro Thema. Öffnen Sie eine Karte, um ihre Einstellungen zu sehen.

<figure><img src="../../../../../.gitbook/assets/doc-type-settings-overview-de.png" alt="Die Karten der Seite Weitere Einstellungen für den Dokumenttyp Rechnung"><figcaption><p>Die Karten der Seite Weitere Einstellungen, alle eingeklappt.</p></figcaption></figure>

## Zugriff

1. Navigieren Sie zu **Einstellungen** → **Globale Einstellungen** → **Dokumenttypen**.
2. Wählen Sie den Dokumenttyp aus und klicken Sie auf **Weitere Einstellungen**.

Die Brotkrümelnavigation oben auf der Seite zeigt **Einstellungen / Dokumenttypen / Weitere Einstellungen**. Der Einstellungs-Assistent rechts auf der Seite erklärt die Einstellungen der geöffneten Karte.

| Karte | Was Sie dort einstellen |
| ----- | ----------------------- |
| Bestellung | PO-Abgleich, Toleranzen, Export von PO-Positionen, Lieferantenartikelnummern |
| Layouts verwalten | Schalter für die Übersicht Layouts verwalten |
| Benutzerdefinierte Validierungsregeln | Ihre eigenen Validierungsregeln für diesen Dokumenttyp |
| Transformationsregeln | Regeln, die einen Wert lesen, schrittweise ändern und zurückschreiben |
| Genehmigung & Ablehnung | Genehmigungsworkflow sowie die Formulare "In Prüfung" und "Ablehnen" |
| [Vertex Tax Verifizierung](vertex-tax-verification.md) | Das Formular für die Vertex-Steuerprüfung gestalten |
| E-Rechnung Validierung | Validierung von XRechnung-, ZUGFeRD- und Factur-X-Rechnungen |
| Tabelle Extraktion | Validierung extrahierter Tabellen überspringen |
| Einstellungen exportieren | Mehrfachexport, PDF-Format, alternativer Export |
| Duplikaterkennung | Doppelte Dokumente erkennen und blockieren |

## Bestellung

Die Karte **Bestellung** (**PO-Abgleich & Validierung**) steuert, wie Dokumente dieses Typs mit Bestellungen abgeglichen werden.

<figure><img src="../../../../../.gitbook/assets/doc-type-settings-po-options-de.png" alt="Die Karte Bestellung mit ihren Schaltern"><figcaption><p>Die Karte Bestellung mit ihren Optionen.</p></figcaption></figure>

* [**Bestellung**](purchase-order/purchase-order.md): Schaltet um, ob der Beleg im Bildschirm für den Bestellabgleich verarbeitet wird. Sie können auch angeben, auf welcher Menge der Abgleich basiert.
* [**PO-Match serverseitig**](purchase-order/purchase-order-matching-rules.md): Gleicht mit dem konfigurierbaren Regelwerk ab. **PO-Abgleichsregeln konfigurieren** öffnet die [Regelseite](purchase-order/purchase-order-matching-rules.md).
* [**PO-Tabelle im Layout-Builder**](purchase-order/po-table-in-layout-builder.md): Ermöglicht die Einbindung von Bestelltabellen in den Layout-Builder für angepasste Dokumentlayouts.
* [**Automatische Prüfung auf PO-Aktualisierungen**](purchase-order/auto-check-for-po-updates.md): Zeigt im Bildschirm für den Bestellabgleich einen visuellen Indikator an, wenn eine Bestellung aktualisiert wurde, und fordert die Benutzer auf, die Daten zu aktualisieren.
* **Automatische Aktualisierung der PO-Daten**: Aktualisiert die PO-Daten automatisch, wenn neue Daten verfügbar sind. Dieser Schalter gehört zu **Automatische Prüfung auf PO-Aktualisierungen**.
* [**Status der verbrauchten Bestellposition**](purchase-order/consumed-po-line-status.md): Versieht die Bestellpositionen im Abgleichbildschirm mit einer Farbcodierung.
* [**Berechnung des PO-Einzelpreises**](purchase-order/calculate-po-unit-price.md): Berechnet den PO-Einzelpreis anhand des Nettobetrags und der Menge, anstatt ihn zu extrahieren.
* [**Nicht übereinstimmende PO-Zeilen exportieren**](purchase-order/export-not-matched-po-lines.md): Wenn deaktiviert, werden nur abgeglichene Positionen exportiert. Wenn aktiviert, werden alle Bestellpositionen exportiert, auch wenn sie nicht abgeglichen wurden.
* **Bereits übereinstimmende Zeilen ignorieren**: Überspringt Positionen, die bereits abgeglichen wurden, bei einem neuen Abgleichprozess.
* [**Dokumentstatus für Einkaufsbestellung aktualisieren**](purchase-order/update-document-purchase-order-status.md): Aktualisiert die Spalte "PO-Status" auf dem Dashboard, sobald sich der Status der Bestellung ändert.
* [**Automatischen Export für nicht abgleichbare Bestellpositionen zulassen**, **Automatische Zuordnung & Export sichtbar für** und **Verwenden Sie den Nettobetrag der Zeilen für den angezeigten Gesamtbetrag.**](purchase-order/auto-match-and-export-options.md): Legen fest, wer die Verknüpfungen für Auto Match & Export sieht und welche Dokumente automatisch exportiert werden dürfen.

### PO-Toleranzeinstellung

<figure><img src="../../../../../.gitbook/assets/doc-type-settings-po-tolerance-de.png" alt="Der Block PO-Toleranzeinstellung mit Mengen- und Einzelpreistoleranz"><figcaption><p>Toleranz für Menge und Einzelpreis.</p></figcaption></figure>

Mit der [**PO-Toleranzeinstellung**](purchase-order/purchase-order-tolerance-settings-additional-purchase-order-tolerance.md) legen Sie Toleranzstufen für Menge und Einzelpreis fest, damit geringfügige Abweichungen nicht als Nichtübereinstimmung markiert werden. Für jeden Wert wählen Sie den Betrag und die Einheit, entweder einen absoluten **Wert** oder einen Prozentsatz (**%**). Der Block enthält außerdem die [**Zusätzliche PO-Toleranzeinstellung**](purchase-order/purchase-order-tolerance-settings-additional-purchase-order-tolerance.md#einstellung-zur-konfiguration-zusatzlicher-bestelltoleranzeinstellungen) für Fracht, Gebühren und Steuern sowie den [**PO-Deaktivierungsstatus**](purchase-order/purchase-order-disable-statuses.md).

{% hint style="info" %}
Wenn das Dokumenttyp-Attribut `CUSTOM_RANGE_FOR_PO_TOLERANCE` aktiviert ist, stammen die Toleranzen für Einzelpreis und Menge aus diesen Dokumenttyp-Einstellungen und nicht aus dem Regelwerk. Das Regeldiagramm auf der [Seite zu den PO-Abgleichsregeln](purchase-order/purchase-order-matching-rules.md) zeigt in diesem Fall einen Hinweis an.
{% endhint %}

### Lieferantenartikelnummernkarte

<figure><img src="../../../../../.gitbook/assets/doc-type-settings-po-supplier-item-map-de.png" alt="Die Tabelle der Lieferantenartikelnummernkarte"><figcaption><p>Die Lieferantenartikelnummernkarte.</p></figcaption></figure>

Die [**Lieferantenartikelnummernkarte**](purchase-order/supplier-item-number-map-admin-documentation.md) ordnet Lieferantenartikelnummern Ihren internen Artikelnummern zu, sodass Positionen auch dann übereinstimmen, wenn der Lieferant eigene Nummern verwendet. Suchen Sie nach Spalte, um einen Eintrag zu finden.

## Layouts verwalten, Benutzerdefinierte Validierungsregeln und Transformationsregeln

Drei Karten befinden sich direkt unter der Karte Bestellung:

* **Layouts verwalten** schaltet die Übersicht Layouts verwalten für diesen Dokumenttyp ein. Siehe den [Layout Manager](../layout-manager/README.md).
* **Benutzerdefinierte Validierungsregeln** schaltet Ihre eigenen Validierungsregeln ein. **Validierungsregeln verwalten** öffnet sie. Siehe [Benutzerdefinierte Validierungsregeln](../custom-validation-rules.md).
* **Transformationsregeln** schaltet die Transformationsregeln ein. **Transformationsregeln verwalten** öffnet sie. Siehe [Transformationsregeln](../transformation-rules.md).

<figure><img src="../../../../../.gitbook/assets/doc-type-settings-rule-toggles-de.png" alt="Die Karten Layouts verwalten, Benutzerdefinierte Validierungsregeln und Transformationsregeln"><figcaption><p>Die drei Karten mit ihren Schaltern.</p></figcaption></figure>

## Genehmigung und Ablehnung

Die Karte **Genehmigung & Ablehnung** enthält den Genehmigungsworkflow und die Formulare, die Benutzer sehen, wenn sie ein Dokument prüfen oder ablehnen.

<figure><img src="../../../../../.gitbook/assets/doc-type-settings-approval-de.png" alt="Die Karte Genehmigung und Ablehnung"><figcaption><p>Die Karte Genehmigung &#x26; Ablehnung.</p></figcaption></figure>

* **Erste Genehmigung**: Dokumente müssen genehmigt werden, bevor sie exportiert werden können. **Design-Genehmigungsformular** öffnet den **Layout Builder** für den Genehmigungsbildschirm.
* **Vor dem Export genehmigen V2**: Aktiviert Approval V2, das dynamische Felder anstelle statischer Felder unterstützt.
* **Zweite Genehmigung**: Fügt eine zusätzliche Genehmigungsebene hinzu.
* [**Genehmigungsstempel**](approval/approval-stamp.md): Fügt dem Dokument einen Stempel hinzu, wenn es genehmigt wird.
* [**Genehmigungsverlauf**](approval/approval-history.md): Zeigt den Genehmigungsverlauf im Genehmigungsbildschirm und in der Feldvalidierung an.
* **Entwerfen des Überprüfungsformulars**: Konfiguriert das Layout des Prüfformulars mit dem **Layout Builder**.
* **Entwerfen Sie das Ablehnungsformular**: Konfiguriert das Layout des Ablehnungsformulars mit dem **Layout Builder**.

Zum **Layout Builder** siehe den [Layout Manager](../layout-manager/README.md).

## Vertex Tax Verifizierung

Die Karte **Vertex Tax Verifizierung** enthält **Steuerprüfung für Design Vertex**. Sie öffnet den Layout Builder für das Formular, das Benutzer sehen, wenn DocBits die Steuer des Lieferanten mit der von Vertex berechneten Steuer vergleicht. Siehe [Vertex Tax Verifizierung](vertex-tax-verification.md) für die Integration, die Toleranz und das Ergebnis.

## E-Rechnung Validierung

Die Karte **E-Rechnung Validierung** schaltet die Validierung eingehender E-Rechnungen ein und legt fest, ob der Lieferant benachrichtigt wird, wenn eine Rechnung abgelehnt wird. Siehe [E-Rechnung Validierung](../../../document-processing/e-documents/validation-rules.md).

## Tabelle Extraktion

<figure><img src="../../../../../.gitbook/assets/doc-type-settings-table-extraction-de.png" alt="Die Karte Tabelle Extraktion"><figcaption><p>Die Karte Tabelle Extraktion.</p></figcaption></figure>

* **Tabellenvalidierung überspringen**: Umgeht die Standardvalidierung von Tabellendaten. Verwenden Sie diese Option, wenn eine flexible Datenhandhabung erforderlich ist oder wenn bestimmte Validierungsschritte übersprungen werden können, um die Leistung zu verbessern.

## Einstellungen exportieren

<figure><img src="../../../../../.gitbook/assets/doc-type-settings-export-settings-de.png" alt="Die Karte Einstellungen exportieren"><figcaption><p>Die Karte Einstellungen exportieren.</p></figcaption></figure>

* **Mehrfachexport**: Erlaubt es, ein Dokument mehr als einmal zu exportieren.
* **PDF-Format exportieren**: **Dateiformat exportieren** legt das PDF-Format fest, das beim Export von Dokumenten verwendet wird, zum Beispiel **Originaldokument**.
* [**Alternativer Export**](purchase-order/alternate-export.md): Richtet einen alternativen Export für einen ausgewählten Dokumentstatus ein. Wählen Sie den **Status** und die **Exportkonfiguration**, die dafür ausgeführt wird, und schalten Sie die Einstellung dann ein.

## Duplikaterkennung

<figure><img src="../../../../../.gitbook/assets/doc-type-settings-duplicate-detection-de.png" alt="Die Karte Duplikaterkennung"><figcaption><p>Die Karte Duplikaterkennung.</p></figcaption></figure>

Die Karte enthält **Erkennung von doppelten Dokumenten** mit den Feldern, die festlegen, was als Duplikat gilt, und dem Intervall, in dem Dokumente verglichen werden, sowie die Optionen **Erkennung doppelter Rechnungen**, **Export doppelter Dokumente blockieren** und **Steuerfreie Zeile ignorieren**. Alle drei tragen die Kennzeichnung **Empfohlen**. Siehe [Erkennung doppelter Belege](duplicate-document-handling.md), wie ein markiertes Dokument behandelt wird.
