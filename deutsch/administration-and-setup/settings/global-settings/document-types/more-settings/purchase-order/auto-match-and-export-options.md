# Optionen für Auto Match & Export

Drei Einstellungen am Ende der Karte **Bestellung** legen fest, wer die Verknüpfungen für den PO-Abgleich sieht und welche Dokumente nach einem Abgleich selbstständig exportiert werden dürfen. Sie gelten jeweils für einen Dokumenttyp.

<figure><img src="../../../../../../.gitbook/assets/doc-type-settings-po-options-de.png" alt="Die Karte Bestellung der Dokumenttyp-Einstellungen mit allen PO-Optionen"><figcaption><p>Die Karte Bestellung. Die drei folgenden Optionen sind die letzten drei Zeilen.</p></figcaption></figure>

## Automatischen Export für nicht abgleichbare Bestellpositionen zulassen

Der automatische Export nach dem PO-Abgleich setzt normalerweise ein **vollständig abgeglichenes** Dokument voraus. Wenn dieser Schalter aktiviert ist, dürfen auch Dokumente mit dem Status **Keine abgleichbaren Bestellpositionen** automatisch exportiert werden. Dieser Status bedeutet, dass die Bestellung keine Positionen hat, mit denen die Rechnung abgeglichen werden kann.

* **Aus (Standard):** Nur vollständig abgeglichene Dokumente werden automatisch exportiert.
* **Ein:** Vollständig abgeglichene Dokumente und Dokumente ohne abgleichbare Bestellpositionen werden automatisch exportiert.

Der Schalter spielt nur dann eine Rolle, wenn Dokumente automatisch exportiert werden, zum Beispiel mit [**Automatischer Export, wenn PO zu 100% übereinstimmt**](../../../../document-processing/module/auto-export-if-po-matched-100.md) oder einer DocFlow-Exportkarte. Er ändert nicht, wie Positionen abgeglichen werden.

## Automatische Zuordnung & Export sichtbar für

Der Bildschirm für den PO-Abgleich enthält die Aktion **Auto Match & Export**. Sie gleicht das Dokument ab und exportiert es direkt nach dem Abgleich. Diese Einstellung steuert, wer die Aktion erhält:

| Wert | Wer die Aktion sieht |
| ---- | -------------------- |
| **Nur Administrator** (Standard) | Administratoren |
| **Alle Benutzer** | Jeder Benutzer, der den Bildschirm für den PO-Abgleich öffnen kann |

Administratoren sehen die Aktion immer. Die Einstellung schaltet die Funktion nicht ein. Das Modul [**Automatischer Export, wenn PO zu 100% übereinstimmt**](../../../../document-processing/module/auto-export-if-po-matched-100.md) muss für die Organisation aktiv sein.

## Verwenden Sie den Nettobetrag der Zeilen für den angezeigten Gesamtbetrag.

Der Bildschirm für den PO-Abgleich kann die **Abgestimmte Summe** aus dem **Nettobetrag** der abgeglichenen Rechnungspositionen berechnen, statt sie zu errechnen. Diese Einstellung steuert, wer diese Berechnung einschalten kann:

| Wert | Wer den Schalter sieht |
| ---- | ---------------------- |
| **Nur Administrator** (Standard) | Administratoren |
| **Alle Benutzer** | Jeder Benutzer, der den Bildschirm für den PO-Abgleich öffnen kann |

Wenn der Schalter eingeschaltet ist, verwendet die Abgestimmte Summe die Nettobetrag-Werte direkt aus den abgeglichenen Rechnungspositionen.
