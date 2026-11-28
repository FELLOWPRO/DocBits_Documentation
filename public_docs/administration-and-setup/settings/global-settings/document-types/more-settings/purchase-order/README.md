# Bestellung

Die Karte **Purchase Order** in den **More Settings** eines Dokumenttyps steuert, wie Dokumente dieses Typs mit Bestellungen abgeglichen werden. Einstellungen gelten jeweils für einen Dokumenttyp; öffnen Sie daher zuerst den Dokumenttyp, den Sie ändern möchten, unter **Settings → Document Types**.

So finden Sie die Einstellungen für eine Rechnung:

1. Öffnen Sie **Settings → Document Types**.
2. Suchen Sie die Karte **Invoice** und wählen Sie ihr Zahnradsymbol (**More Settings**).
3. Öffnen Sie den Abschnitt **Purchase Order**, um die Optionen für Abgleich und Validierung zu prüfen.

<figure><img src="../../../../../../.gitbook/assets/dbdc226228-invoice-card-en-20261030.png" alt="English Invoice document type card with the More Settings gear at the upper right"><figcaption><p>Die Karte Invoice in der aktuellen englischen Dev-Testumgebung. Über das Zahnradsymbol öffnen Sie More Settings; die übrigen Bedienelemente gelten für den Dokumenttyp.</p></figcaption></figure>

<figure><img src="../../../../../../.gitbook/assets/dbdc226-po-section-en-20261030.png" alt="Closed Purchase Order section labelled PO Matching and Validation"><figcaption><p>Der Abschnitt Purchase Order in More Settings, geschlossen dargestellt. Klappen Sie die Kopfzeile auf, um die Optionen zu sehen; für diese Aufnahme wurde keine Einstellung geändert.</p></figcaption></figure>

Beginnen Sie mit den Abgleichregeln und Toleranzen und passen Sie dann das Verhalten rund um Abgleich und Export an:

* [Regeln für die Übereinstimmung von Bestellungen](purchase-order-matching-rules.md) und [Einstellungen zur Toleranz von Bestellungen / Zusätzliche Toleranz für Bestellungen](purchase-order-tolerance-settings-additional-purchase-order-tolerance.md) legen fest, wie Rechnungs- und Bestellzeilen verglichen werden.
* [Optionen für Auto Match & Export](auto-match-and-export-options.md), [Export nicht übereinstimmender PO-Zeilen](export-not-matched-po-lines.md) und [Alternativer Export](alternate-export.md) behandeln, was nach einem Abgleich geschieht.
* [Exportmenge in Basismaßeinheit](export-quantity-in-base-unit-of-measure.md) rechnet die exportierte Menge und den Stückpreis für den Infor-LN-Export in die Basismaßeinheit um.
* [Auftragstabelle im Layout-Builder](po-table-in-layout-builder.md), [Verbrauchter PO-Zeilenstatus](consumed-po-line-status.md) und [PO-Stückpreis berechnen](calculate-po-unit-price.md) ändern, was Benutzer in der Abgleichansicht sehen.
* [Automatische Prüfung auf PO-Aktualisierungen](auto-check-for-po-updates.md), [PO-Deaktivierungsstatus](purchase-order-disable-statuses.md) und [Aktualisieren des Dokuments Bestellstatus](update-document-purchase-order-status.md) steuern, wie Bestelldaten und Status aktuell gehalten werden.
* [Lieferantenartikelnummer-Zuordnung - Admin-Dokumentation](supplier-item-number-map-admin-documentation.md) und die allgemeine Seite [Bestellung](purchase-order.md) liefern weiteren Hintergrund.

Einstellungen können Live-Dokumente betreffen. Prüfen Sie Änderungen mit einem Testdokument, bevor Sie sie in der Produktion speichern.

Diese Übersicht zeigt, wo die Einstellungen zu finden sind. Sie prüft keinen abgeschlossenen PO-Abgleich und keinen Export.
