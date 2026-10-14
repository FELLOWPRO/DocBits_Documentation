# Hotfixes 8. September 2026

> Abgleich von Bestellungen: Was sich mit den am 8. September 2026 bereitgestellten Hotfixes geändert hat. Das unten beschriebene Verhalten ist in der Entwicklungsumgebung aktiv und erreicht mit den nächsten Upgrades Stage, Sandbox und Produktion.

## Abgleich von Bestellungen

- **Der Abgleich bleibt beim Speichern erhalten.** Ein Bestellabgleich, den eine Transformationsregel früher bei jedem Speichern stillschweigend verworfen hat (Regeln, die die Positionen neu aufbauen), wird jetzt beibehalten, solange die Regel dieselben Positionen erzeugt. Wenn eine Regel tatsächlich abgeglichene Positionen ersetzt, protokolliert das Dokument die Regel und der Bildschirm benennt sie.
- **Der Abgleich wird beim Speichern erneut ausgeführt.** Wenn sich die Bestellnummer im Dokument ändert – oder wenn Stammdaten sie nach der Verarbeitung ausgefüllt haben und noch kein Abgleich durchgeführt wurde – wird beim Speichern das Dokument sofort abgeglichen. Ein bestehender Abgleich wird durch ein Speichern niemals überschrieben.
- **Der Bildschirm zeigt an, warum kein Abgleich vorliegt.** Der Bildschirm „Bestellabgleich“ zeigt einen Satz über dem Bestellbereich an: keine Bestellnummer, Bestellung im ERP nicht gefunden, noch nicht nachgeschlagen, geladen aber nicht verbunden, keine Position passt, keine Tabelle, Tabellenspalten nicht zugeordnet, keine offenen Positionen mehr. Zurückgestellte Kandidaten werden mit dem Grund aufgelistet (zum Beispiel eine Rechnungsnummer, die in die Bestellspalte eingelesen wurde).
- **Ein verworfener Abgleich wird nie als gespeichert gemeldet.** Wenn der Server einen Abgleich nicht beibehält, stellt der Bildschirm ihn wieder her, markiert das Dokument als ungespeichert und meldet die Ablehnung mit dem Grund anstelle von „gespeichert“.
- **Die Abgleichhistorie zeigt die Transformationsregeln.** Die Abgleichhistorie eines Dokuments enthält jetzt einen Schritt _Transformationsregeln_ vor der ersten Abgleichstufe, der die ausgeführten Regeln auflistet und angibt, ob eine davon den Abgleich verworfen hat. Administratoren erhalten einen Link zur Regel.
- **Bestell-Einheitspreis aus dem Nettobetrag.** Mit aktivierter Option _Bestell-Einheitspreis berechnen_ wird der Preis jetzt zuerst aus dem **Netto**betrag der Bestellposition abgeleitet und nur aus dem Gesamtbetrag, wenn kein Nettobetrag vorliegt. Bestellungen von Infor enthalten die Steuer im Positionsgesamtbetrag; netto bepreiste Rechnungen wurden früher als „Einheitspreis unterabgeglichen“ genau um den Steuersatz angezeigt. Der berechnete Preis wird bei jedem Abgleich aktualisiert, sodass bestehende Dokumente ohne erneutes Laden der Bestellung profitieren.
- **Rechnungsnummern werden nicht mehr mit Bestellnummern verwechselt.** Ein Kandidat aus einer Positionsspalte oder einem früheren Nachschlagevorgang, der der eigenen Rechnungsnummer des Dokuments entspricht, wird zurückgestellt.

## Dokumentation

- Neue Seite [Transformationsregeln](../../administration-and-setup/settings/global-settings/document-types/transformation-rules.md).
- [Regeln für den Bestellabgleich](../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-matching-rules.md) behandelt jetzt Regeltypen, Aktivierungsbedingungen, Fallback-Regeln, das Standardregelset, Toleranztypen und die wirksamen Spalten.
- [Bestell-Einheitspreis berechnen](../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/calculate-po-unit-price.md) beschreibt die Netto-Betragsberechnung.
- [Bildschirm Bestellabgleich](../../end-user-and-partner-section/end-user-section/purchase-order-matching/README.md) erklärt die Meldungen „Warum gibt es keinen Abgleich“ und die Abgleichhistorie.