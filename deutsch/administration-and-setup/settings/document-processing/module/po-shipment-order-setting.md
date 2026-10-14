# PO Versandauftragseinstellung

## **Übersicht**

Der Abschnitt **PO Versandauftrag** bietet eine Aufschlüsselung des Liefer- und Rechnungsstatus für übereinstimmende Artikel der Bestellung. Dieser Abschnitt erscheint im Bildschirm **Bestellungsabgleich**, wenn die Funktion aktiviert ist.

## **Aktivierung**

Um diese Funktion zu aktivieren:

1. Gehe zu **Einstellungen** → **Dokumentenverarbeitung** → **Modul**.
2. Wähle **Bestellung** aus.
3.  Aktiviere die Option **PO Versandbestellung**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F2ZdK2XuCIjc4Hz3W0s5H%252FPO-Shipment-Order-Setting.jpg%3Falt%3Dmedia%26token%3Dbe657223-f04e-4326-a284-bb29bae148e0\&width=768\&dpr=4\&quality=100\&sign=97986166\&sv=2)

## **Wo es erscheint**

Nach der Aktivierung wird der Abschnitt PO Versandbestellung im Interface für den Bestellungsabgleich sichtbar.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F2R9tB3JySdIMk8meRSVZ%252FPO-Shipment-Order-1.jpg%3Falt%3Dmedia%26token%3D70aa50f4-84cd-4a55-b580-037b893d1f5b\&width=768\&dpr=4\&quality=100\&sign=e4619335\&sv=2)

### **PO** Versandauftrag **– Feldbeschreibungen**

* **Artikel-ID** Identifiziert den spezifischen Artikel in der Bestellung.
* **Liefernummer** Referenznummer für die Sendung oder Lieferung.
* **Versandte Menge** Menge, die geliefert oder erhalten wurde.
* **In Rechnung gestellte Menge** Menge, die bereits in Rechnung gestellt wurde.
* **Offene Rechnungsmenge** Menge, die noch für die Rechnungsstellung offen ist (berechnet als _Versandte Menge - In Rechnung gestellte Menge_).
* **Fortschrittsbalken und Prozentsatz**
  * Zeigt an, wie viel der versandten Menge mit Rechnungen übereinstimmt.
  * Beginnt bei 0% für neue Bestellungen.
  * Wird kumulativ über mehrere Rechnungen aktualisiert.
  * Spiegelt den Gesamtfortschritt von in Rechnung gestellten vs. versandten Artikeln wider.
* **Zugesagtes Lieferdatum** Das erwartete Lieferdatum für den Bestellungsartikel.
*   **Verspätungsindikator**

    Zeigt die Anzahl der Tage an, um die die Lieferung verspätet ist, basierend auf dem **Zugesagten Lieferdatum**.
