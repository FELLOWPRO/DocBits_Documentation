# EDI Strukturbeschreibung

Das Hauptziel des Strukturdeskriptors besteht darin, die Elemente einer EDI-Nachricht logisch und organisiert darzustellen, um die Daten einfacher verwalten und analysieren zu können. Indem die Hierarchie der Nachricht genau wiedergegeben wird.

### Elemente des Strukturdeskriptors

**N1** – Enthält die folgenden Felder:

* **N1** – Name oder Kennung der Entität (z. B. Partei, Organisation).
* **N2** – Zusätzliche Namensinformationen (in der Regel ein sekundärer Name für die Entität).
* **N3** – Adressinformationen (typischerweise die Straßenadresse).
* **N4** – Geografischer Standort (Stadt, Bundesland, Postleitzahl, Land).

**N9** – Enthält das folgende Feld:

* **N9** – Referenzkennung (z. B. Bestellnummer oder Steuerkennung).
* **Schleifen:**
  * **MSG01** – Enthält das folgende Feld:
    * **MSG01** – Freitextnachricht (in der Regel eine Notiz oder spezielle Anweisung im Zusammenhang mit der Transaktion).

**IT1** – Enthält die folgenden Felder:

* **IT1** – Positionsidentifikator (z. B. Artikelnummer oder Produktcode).
* **QTY** – Menge des Artikels in der Transaktion (z. B. bestellte oder versandte Einheiten).
* **TXI** – Steuerinformationen (z. B. Steuersätze, Beträge oder Klassifizierungen für den Artikel).
* **REF** – Referenzinformationen (z. B. Chargennummer, Seriennummer oder andere Kennungen im Zusammenhang mit dem Artikel).
* **Schleifen:**
  * **SAC** – Kann wiederholt werden und enthält die folgenden Felder:
    * **SAC** – Service-, Werbe-, Zulagen- oder Gebühreninformationen (z. B. zusätzliche Kosten oder Rabatte im Zusammenhang mit dem Artikel).
    * **TXI** – Steuerinformationen zu SAC (z. B. Steuern auf Gebühren oder Zulagen).

**SAC** – Enthält die folgenden Felder:

* **SAC** – Service-, Werbe-, Zulagen- oder Gebühreninformationen (kann unabhängig oder innerhalb der IT1-Schleife verwendet werden, um zusätzliche Gebühren/Rabatte darzustellen).
* **TXI** – Steuerinformationen zu SAC (z. B. Steuern auf Gebühren oder Zulagen).

### Hier ist das vollständige Beispiel einer Strukturbeschreibung im JSON-Format:

```
{
    "N1": {
        "fields": [
            "N1",  
            "N2",   
            "N3",   
            "N4"    
        ]
    },
    "N9": {
        "fields": [
            "N9"    
        ],
        "loops": {
            "MSG01": {
                "fields": [
                    "MSG01"   
            }
        }
    },
    "IT1": {
        "fields": [
            "IT1",   
            "QTY",   
            "TXI",   
            "REF"    
        "loops": {
            "SAC": {
                "fields": [
                    "SAC",   
                    "TXI"    
        }
    },
    "SAC": {
        "fields": [
            "SAC",   
            "TXI"    
        ]
    }
}
```
