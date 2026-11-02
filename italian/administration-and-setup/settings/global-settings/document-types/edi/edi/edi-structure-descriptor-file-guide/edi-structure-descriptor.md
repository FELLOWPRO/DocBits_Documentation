# Descrittore della struttura EDI

L'obiettivo principale del descrittore della struttura è quello di delineare gli elementi di un messaggio EDI in modo logico e organizzato, rendendo più facile gestire e analizzare i dati. Riflettendo accuratamente la gerarchia del messaggio.

### Elementi del descrittore della struttura

**N1** – Contiene i seguenti campi:

* **N1** – Nome o identificatore dell'entità (ad esempio, parte, organizzazione).
* **N2** – Informazioni aggiuntive sul nome (di solito un nome secondario per l'entità).
* **N3** – Informazioni sull'indirizzo (tipicamente l'indirizzo stradale).
* **N4** – Posizione geografica (città, stato, codice postale, paese).

**N9** – Contiene il seguente campo:

* **N9** – Identificatore di riferimento (ad esempio, numero dell'ordine d'acquisto o numero di controllo).
* **Cicli:**
  * **MSG01** – Contiene il seguente campo:
    * **MSG01** – Testo del messaggio libero (di solito una nota o istruzione speciale relativa alla transazione).

**IT1** – Contiene i seguenti campi:

* **IT1** – Identificatore della riga (ad esempio, numero dell'articolo o codice prodotto).
* **QTY** – Quantità dell'articolo nella transazione (ad esempio, unità ordinate o spedite).
* **TXI** – Informazioni fiscali (ad esempio, aliquote fiscali, importi o classificazioni per l'articolo).
* **REF** – Informazioni di riferimento (ad esempio, numero di lotto, numero di serie o altri identificatori relativi all'articolo).
* **Cicli:**
  * **SAC** – Può ripetersi e contiene i seguenti campi:
    * **SAC** – Informazioni su servizi, promozioni, sconti o oneri (ad esempio, costi aggiuntivi o sconti relativi all'articolo).
    * **TXI** – Informazioni fiscali relative a SAC (ad esempio, tasse su oneri o sconti).

**SAC** – Contiene i seguenti campi:

* **SAC** – Informazioni su servizi, promozioni, sconti o oneri (può essere utilizzato indipendentemente o all'interno del ciclo IT1 per rappresentare oneri/sconti aggiuntivi).
* **TXI** – Informazioni fiscali relative a SAC (ad esempio, tasse su oneri o sconti).

### Ecco l'esempio completo di un descrittore della struttura in formato JSON:

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
