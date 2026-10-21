# PO-Vergleiche: Richtung, Toleranz und Kartenversionen

<figure><img src="../../../.gitbook/assets/workflow-card-qa-20261021-category-72e8f3204ac8-de.png" alt="Verfügbare Karten der ausgewählten Kategorie. Füllen Sie die Platzhalter vor der Verwendung aus."><figcaption><p>Verfügbare Karten der ausgewählten Kategorie. Füllen Sie die Platzhalter vor der Verwendung aus.</p></figcaption></figure>

PO-Vergleichskarten vergleichen eine ausgewählte Seite mit einer Referenzseite. Die Referenz bestimmt die Basis für eine prozentuale Toleranz. Führen Sie zunächst den Bestellabgleich durch und wählen Sie dann den Vergleich, den Operator, Alle/Alle und die für die jeweilige Karte erforderliche Toleranz aus.

## Vergleichsrichtungen

| Gespeicherte Option | Vergleichsseite | Referenzseite |
| --- | --- | --- |
| `po_document` | Bestellung | Dokument |
| `received_document` | Empfangene Daten | Dokument |
| `po_received` | Bestellung | Empfangene Daten |
| `document_po` | Dokument | Bestellung |
| `document_received` | Dokument | Empfangene Daten |
| `received_po` | Empfangene Daten | Bestellung |

Die Empfangsseite ergibt sich aus den abgeglichenen Bestelldaten. Ein erhaltener Vergleich auf der Einheitspreiskarte kann anhand von Mengen einen vergleichbaren Betrag ableiten; es handelt sich nicht um einen direkten Vergleich einer Menge mit einem Währungspreis. Verwenden Sie bei der Überprüfung der Berechnung die von dieser Karte im Protokoll aufgezeichneten Werte.

## Warum die Richtung wichtig ist

Für eine Referenz von `100` und einen Vergleichswert von `110` entspricht eine prozentuale Toleranz von `5` `5` um die Referenz. Wenn das Dokument die Referenz ist und sein Wert bearbeitet werden kann, ändert sich durch die Änderung des Dokuments auch diese Toleranzbasis. Wählen Sie die Referenz bewusst aus, insbesondere für die automatische Freigabe.

Durch Umkehren der Seiten werden die Ordnungsoperatoren umgekehrt: `>` wird zu `<`, `>=` wird zu `<=` und umgekehrt. Gleichheit und Ungleichheit behalten ihre Bedeutung. Fahren Sie mit einem Bediener nicht um, ohne auch die gewählten Seiten zu prüfen.

Versionen, die die Vergleichsmigration enthalten, verschieben betroffene gespeicherte Karten von `po_document` nach `document_po` und von `received_document` nach `document_received`, während der Anordnungsoperator umgekehrt wird. Die betroffenen Versionen sind Quantity-Tolerance V4, Order-Confirmation-to-PO V4 und Unit-Price V4/V5. Der kombinierte Preis-/Mengenunterschied ist von dieser gespeicherten Kartenmigration ausgeschlossen. Überprüfen Sie die gespeicherte Konfiguration und testen Sie ihr Geschäftsergebnis nach einer Veröffentlichung. Machen Sie es nicht ein zweites Mal manuell rückgängig.

## Kartenversionen zum Einzelpreis

| Version | Konfiguration |
| --- | --- |
| v3 | Verwendet das frühere Vergleichsverhalten. Gehen Sie nicht davon aus, dass dadurch die neueren Richtungs- und Toleranzfelder offengelegt werden. |
| v4 | Fügt die vergleichsseitige Auswahl hinzu. |
| v5 | Beinhaltet Alle/Alle, Operator, Toleranzbetrag, Toleranztyp und Auswahl auf der Vergleichsseite. |

Wählen Sie eine absolute Toleranz für einen festen Betrag und eine prozentuale Toleranz für eine Abweichung relativ zur ausgewählten Referenz. Nutzen Sie den von der Karte angebotenen Operator; Genaue Gleichheit und das Einhalten einer Toleranz sind unterschiedliche Entscheidungen. Es gibt keine universelle Geschäftstoleranz, die für jeden Lieferanten oder Dokumenttyp geeignet ist.

## Verifizierungsbeispiel

1. Verwenden Sie eine übereinstimmende Bestellreferenz `100` und einen Dokumentwert `110`.
2. Wählen Sie „Dokument zur Bestellung“, einen Vergleich innerhalb der Toleranz, sofern angeboten, und `5` Prozent. Erwarten Sie einen Out-of-Band-Vergleich.
3. Testen Sie die genaue Toleranzgrenze, die Werte auf beiden Seiten und eine fehlende übereinstimmende Bestellung.
4. Überprüfen Sie bei mehreren Zeilen „Any vs. All“ anhand einer bestandenen und einer fehlerhaften Zeile.
5. Überprüfen Sie die verglichenen Werte des Protokolls, die ausgewählten Seiten, den Operator und die Toleranz und überprüfen Sie dann den resultierenden Workflow-Zweig.

Eine nicht übereinstimmende Bestellung, ein nicht numerischer Wert und eine falsche Geschäftsbedingung sind unterschiedliche Ergebnisse. Behandeln Sie fehlende Daten nicht als erfolgreichen Abgleich. Für Gebühren verwenden Sie [Any / All Charges](../and/compare-with-purchase-order/any-all-charges.md), was das Verhalten bei fehlenden Ladungen und v2/v3 separat erklärt.

Fahren Sie mit dem [PO Matching Guide](../and/compare-with-purchase-order/po-matching-complete-guide.md)] und der individuellen Kartenreferenz für die übrigen Felder fort.
