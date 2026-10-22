# Angebotsvergleichskarten

<figure><img src="../../../.gitbook/assets/workflow-card-qa-20261021-category-4a7af1d99c73-de.png" alt="Verfügbare Karten der ausgewählten Kategorie. Füllen Sie die Platzhalter vor der Verwendung aus. Einzelne Beschriftungen dieser Kartenversion sind in der Oberfläche noch unübersetzt oder fachlich ungenau. Die Erläuterungen auf dieser Seite verwenden die passenden Begriffe."><figcaption><p>Verfügbare Karten der ausgewählten Kategorie. Füllen Sie die Platzhalter vor der Verwendung aus. Einzelne Beschriftungen dieser Kartenversion sind in der Oberfläche noch unübersetzt oder fachlich ungenau. Die Erläuterungen auf dieser Seite verwenden die passenden Begriffe.</p></figcaption></figure>

Diese Und-Bedingungen verwenden die im Dokument verfügbaren Angebots- oder Lieferantenartikeldaten. Konfigurieren und testen Sie sie, nachdem die erforderlichen Angebotsdaten geladen wurden. Eine übereinstimmende Artikelkennung allein beweist nicht, dass der Preis oder die Maßeinheit korrekt sind.

## Wählen Sie den Scheck aus

| Kartentyp | Überprüfung und Konfiguration |
| --- | --- |
| `CONDITION_QUOTES_ITEM_NUMBER_COMPARISON` | Prüft die Artikelkennung anhand der Artikelpreisdaten. Wählen Sie die von der Karte angebotenen Vergleichs- und Alle/Alle-Felder aus. |
| `CONDITION_SPECIFY_SUPPLIER_TYPE` | Vergleicht den Lieferantentyp aus den Angebotsdaten mit `supplier_type`. Hierbei handelt es sich um eine Lieferantenklassifizierungsprüfung, nicht um einen Preisvergleich. |
| `CONDITION_QUOTE_SUPPLIER_ITEM_NUMBER_EXISTS` | Prüft, ob die Artikel-ID des Lieferanten in den Artikelpreisdaten vorhanden ist oder nicht; Wählen Sie den Operator und Alle/Alle. Fehlende Angebots- oder Artikeldaten müssen im Protokoll untersucht werden. |
| `CONDITION_QUOTE_PRICE_MATCH` | Vergleicht einen Stückpreis mit dem ausgewählten Lieferantenpreis: `ManagedPrice` oder `LastPrice`. Wählen Sie „Alle/Alle“ und den numerischen Vergleichsoperator. Zeilen ohne vergleichbare Nummer auf einer Seite werden übersprungen und protokolliert; Ist keine Zeile vergleichbar, meldet die Karte fehlende Belegdaten. |
| `CONDIITON_UNIT_OF_MEASURE_EQUAL` | Prüft die Maßeinheit anhand der zugehörigen Daten. Der technische Typ enthält einen Rechtschreibfehler; Ändern Sie es nicht im gespeicherten Workflow-JSON. Ein in verschiedenen Einheiten ausgedrückter Preis bedarf gesonderter Aufmerksamkeit. |
| `CONDITION_ITEM_QUOTES_TO_CONTRACTED_PRICE` | Vergleicht angebotene und vertraglich vereinbarte Preise. Version 3 fügt Any/All hinzu; siehe unten. |

Sichtbare Beschriftungen können je nach Release und UI-Sprache unterschiedlich sein. Wählen Sie anhand der tatsächlichen Prüfung aus, nicht nur anhand des Kategorienamens. Beispielsweise kann der angebotene Artikelpreis unter „Logik“ angezeigt werden, während die anderen Angebotsprüfungen unter „Mit Angebotspreis vergleichen“ angezeigt werden.

## Angegebener Artikelpreis: Version 3

Wählen Sie den Gleichheits- oder Ungleichheitsoperator und ob jede verglichene Linie oder jede verglichene Linie diesen erfüllen muss:

- `match_any`: Eine erfolgreiche Vergleichslinie ist ausreichend.
- `match_all`: Jede verglichene Zeile muss den ausgewählten Operator erfüllen.

Version 2 behält das Verhalten „Alle“ bei. Eine nicht festgelegte Einstellung „Alle/Alle“ in Version 3 greift auf „Alle“ zurück und wird protokolliert. Eine Karte ohne vergleichbare Zeilen meldet fehlende Daten; Das Fehlen eines Preises ist kein Beweis für Gleichheit oder Ungleichheit. Untersuchen Sie übersprungene Zeilen und deren fehlende Seite im Protokoll.

Beispielsweise liefern zwei vergleichbare Linien bei Gleichheit die Ergebnisse „wahr“ und „falsch“. Alle Pässe; Alles scheitert. Bei Ungleichheit ändert sich zuerst das Vergleichsergebnis für jede Zeile, und „Any/All“ kombiniert dann diese Ergebnisse. Das endgültige All-Ergebnis wird nicht invertiert, um Any zu implementieren.

## Testfälle

Verwenden Sie genaue Artikel- und Lieferanten-IDs, die beabsichtigte Preisquelle und passende Einheiten. Testen Sie, dass alle Zeilen übereinstimmen, ein gemischtes Ergebnis, keine vergleichbaren Preise, fehlende Angebotsdaten und eine falsche Lieferanten-ID. Überprüfen Sie sowohl das Vergleichsergebnis als auch die übersprungenen Zeilen. Halten Sie die Genehmigung bzw. Ausfuhr hinter den tatsächlich erforderlichen betriebswirtschaftlichen Prüfungen zurück; Eine erfolgreiche Identifikatorprüfung ist keine vollständige Beschaffungsvalidierung.

Siehe [PO Matching](../and/compare-with-purchase-order/po-matching-complete-guide.md) für Bestellvergleiche und [Workflow-Protokolle](../workflow-logs.md) für die Fehlerbehebung.






<!-- workflow-card-complete-example-20261021 condition_quotes_item_number_comparison -->

### Beispiel für den Artikelnummernvergleich

**Konfiguration:** Bereiten Sie zwei vergleichbare Angebotszeilen vor: Lieferantenartikel `DEMO-S1` wird Artikel `DEMO-I1` auf beiden Seiten zugeordnet; Die Lieferantenposition `DEMO-S2` hat die Dokumentposition `DEMO-I2` und die Matrixposition `DEMO-I9`. Wählen Sie Gleichheit und `match_all`.

**Erwartetes Ergebnis und Gegenbeispiel:** Das Bedingungsergebnis ist falsch mit `match_all`, da eine vergleichbare Artikelnummer abweicht. Das Ergebnis stimmt mit `match_any`, da die erste Artikelnummer übereinstimmt. Bei der Suche wird die Artikelnummer des Lieferanten verwendet. Ein Matrixeintrag ohne Artikelnummer wird übersprungen und protokolliert; Wenn keine Zeile vergleichbar ist, ist das Bedingungsergebnis falsch. Ein Datumsbereichsprotokoll allein ist keine separate Gültigkeitsbedingung.

Dies ist eine beispielhafte Testkonfiguration und das erwartete Ergebnis. es wurde nicht ausgeführt. Verwenden Sie die in Ihrer Testorganisation konfigurierten Daten und Empfänger.

<!-- workflow-card-complete-example-20261021 condition_quote_supplier_item_number_exists -->

### Beispiel für die Existenz eines Lieferantenartikels

**Konfiguration:** Das Dokument hat die Lieferantenartikelnummern `DEMO-S1` und `DEMO-S2`; Die geladenen Artikelpreisdaten des Lieferanten enthalten nur `DEMO-S1`. Wählen Sie den Anwesenheitsoperator und `match_all`.

**Erwartetes Ergebnis und Gegenbeispiel:** Das Bedingungsergebnis ist falsch mit `match_all` und wahr mit `match_any`. Beim Abwesenheitsoperator ist die zweite Zeile ein positives Abwesenheitsergebnis. Die Existenz beweist nicht, dass der Artikelpreis, die Einheit oder die Lieferantenklassifizierung korrekt sind. Laden Sie zuerst gültige Angebotsdaten und prüfen Sie die Fehler aufgrund fehlender Daten.

Dies ist eine beispielhafte Testkonfiguration und das erwartete Ergebnis. es wurde nicht ausgeführt. Verwenden Sie die in Ihrer Testorganisation konfigurierten Daten und Empfänger.

<!-- workflow-card-complete-example-20261021 condition_quote_price_match -->

### Beispiel für Lieferantenpreise

**Konfiguration:** Für zwei übereinstimmende Linien wählen Sie `ManagedPrice`, Gleichheit und `match_all`. Die Dokumentenpreise betragen `10` und `12`; Die entsprechenden verwalteten Preise sind `10` und `13`, in passenden Währungen und Einheiten.

**Erwartetes Ergebnis und Gegenbeispiel:** Das Bedingungsergebnis ist falsch mit `match_all` und wahr mit `match_any`. Der Wechsel zu `LastPrice` nutzt eine andere Quelle und muss unabhängig getestet werden. Eine Zeile ohne vergleichbaren numerischen Preis wird übersprungen und protokolliert; Wenn keine Zeile vergleichbar ist, meldet die Karte fehlende Dokumentdaten und keine Gleichheit.

Dies ist eine beispielhafte Testkonfiguration und das erwartete Ergebnis. es wurde nicht ausgeführt. Verwenden Sie die in Ihrer Testorganisation konfigurierten Daten und Empfänger.

<!-- workflow-card-complete-example-20261021 condition_specify_supplier_type -->

### Beispiel für die Lieferantenklassifizierung

**Konfiguration:** Wählen Sie Lieferantentyp `Contract`. Bereiten Sie zwei geladene Angebotslieferanteneinträge vor, wobei `managed_class` gleich `contract` ist.

**Erwartetes Ergebnis und Gegenbeispiel:** Die Bedingung ist wahr, wenn jeder geladene Eintrag diese Klassifizierung hat. Die Bedingung ist falsch, wenn ein Eintrag die Klassifizierung `managed` hat. Der auswählbare `Nonmanaged`-Wert wird vom Backend auf `unmanaged` normalisiert. Diese Klassifizierung hat nichts mit der Rechtsform des Lieferanten zu tun. Fehlende Angebotsdaten sind keine Übereinstimmung.

Dies ist eine beispielhafte Testkonfiguration und das erwartete Ergebnis. es wurde nicht ausgeführt. Verwenden Sie die in Ihrer Testorganisation konfigurierten Daten und Empfänger.

<!-- workflow-card-complete-example-20261021 condiiton_unit_of_measure_equal -->

### Beispiel für eine Maßeinheit

**Konfiguration:** Bereite zugeordnete Angebotszeilen mit der Belegeinheit `EA` und der Vergleichseinheit `EA` des Lieferanten vor. Wähle Gleichheit und `match_all`. Behalte die zu prüfende Kartenversion bei.

**Erwartetes Ergebnis und Gegenbeispiel:** Die Bedingung gilt für übereinstimmende vergleichbare Einheiten; Eine zweite vergleichbare Zeile mit `KG` anstelle von `EA` macht die Bedingung mit `match_all` falsch. Fehlende Vergleichseinheiten werden übersprungen und protokolliert; Wenn keine vergleichbar ist, meldet die Karte fehlende Daten. Version 3 wendet möglicherweise die konfigurierte Einheitenzuordnung an. Überprüfen Sie diese Zuordnung daher separat. Matching-Preise allein ergeben noch keine Matching-Einheiten.

Dies ist eine beispielhafte Testkonfiguration und das erwartete Ergebnis. es wurde nicht ausgeführt. Verwenden Sie die in Ihrer Testorganisation konfigurierten Daten und Empfänger.
