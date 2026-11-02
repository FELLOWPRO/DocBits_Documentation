# TransactionConfig Pro Template

## Configurazione dell’elaborazione dei documenti finanziari

_TransactionConfig Pro Template_ documenta esempi di mappatura per fatture, note di debito e note di credito. Il gestore delle regole può usare regole ed espressioni `conflict_resolution` configurate per determinare le azioni di elaborazione. Questa documentazione non dimostra che un modello predefinito sia distribuito nel proprio ambiente.

Le mappature dei campi, i tipi di transazione e le decisioni del flusso devono essere configurati per l’integrazione Infor M3/LN interessata. Gli esempi spiegano tale configurazione; non garantiscono risultati esatti, un’integrazione senza adattamenti o la conformità agli standard finanziari internazionali.

### Aree di configurazione

* **Mappatura:** Definire i campi di origine e destinazione per ogni tipo di transazione e verificare i dati risultanti.
* **Personalizzazione:** Configurare le regole del processo aziendale e delle approvazioni.
* **Automazione:** Automatizzare solo le decisioni espressamente coperte dalle regole e dalle espressioni attive.
* **Integrazione:** Verificare la mappatura di esportazione e i requisiti del sistema Infor M3/LN di destinazione.
* **Conformità:** Esaminare separatamente i requisiti contabili e fiscali; la sola configurazione non garantisce la conformità legale.

## Casi illustrativi di risoluzione dei conflitti

Lo scenario seguente illustra una mappatura configurata, non un modello predefinito di cui sia stata verificata la distribuzione. L’output effettivo, gli importi, i segni e i tipi di documento dipendono dalle regole e dalle espressioni `conflict_resolution` attive, dalla mappatura di esportazione e dalle decisioni di approvazione. Qualsiasi nota di debito o di credito descritta è subordinata a tale configurazione; l’esempio non ne garantisce l’emissione automatica né la conformità legale.

### [Casi 1, 2, 3: Quantità e prezzo unitario entro tolleranza](case-1-2-3-quantity-and-unit-price-within-tolerance.md)

**Scenario:** Quantità e prezzo fatturati rientrano nelle tolleranze configurate rispetto al PO.

**Azione illustrativa:** La mappatura illustrativa accetta i valori fatturati e calcola quantità × prezzo unitario.

### [Casi 4, 5: Quantità entro tolleranza, prezzo fuori tolleranza (approvato)](case-4-5-quantity-within-tolerance-unit-price-outside-tolerance-approved.md)

**Scenario:** La quantità è entro tolleranza; lo scostamento di prezzo è fuori tolleranza ed è approvato.

**Azione illustrativa:** La mappatura illustrativa usa il prezzo del PO e assegna la differenza approvata a un onere di riga, se configurato.

### [Caso 6: Quantità entro tolleranza, prezzo sotto il limite (rifiutato)](case-6-quantity-within-tolerance-unit-price-outside-negative-tolerance-rejected.md)

**Scenario:** La quantità è entro tolleranza; il prezzo è inferiore all’intervallo consentito ed è rifiutato.

**Azione illustrativa:** La mappatura illustrativa usa il prezzo del PO. Lo scostamento con segno non è automaticamente una nota di credito; tipo e segno della rettifica dipendono dalla mappatura.

### [Caso 7: Quantità entro tolleranza, prezzo sopra il limite (rifiutato)](case-7-quantity-within-tolerance-unit-price-outside-tolerance-positive-rejected.md)

**Scenario:** La quantità è entro tolleranza; lo scostamento positivo di prezzo è rifiutato.

**Azione illustrativa:** La mappatura illustrativa usa il prezzo del PO. Qualsiasi nota o rettifica della differenza dipende dalla mappatura di esportazione.

### [Casi 8a, 9a: Quantità fuori tolleranza (approvata), prezzo entro tolleranza](case-8a-9a-quantity-outside-tolerance-approved-unit-price-within-tolerance.md)

**Scenario:** Lo scostamento di quantità è approvato e il prezzo resta entro tolleranza.

**Azione illustrativa:** La mappatura illustrativa usa la quantità fatturata approvata e il prezzo unitario della fattura.

### [Caso 11a: Quantità sopra il limite (rifiutata), prezzo entro tolleranza](case-11a-quantity-outside-tolerance-positive-rejected-unit-price-within-tolerance.md)

**Scenario:** La quantità supera la tolleranza ed è rifiutata; il prezzo è entro tolleranza.

**Azione illustrativa:** La mappatura illustrativa usa la quantità approvata e mantiene il prezzo. Il trattamento dell’eccedenza dipende dalle regole configurate.

### [Caso 10a: Quantità sotto il limite (rifiutata), prezzo entro tolleranza](case-10a-quantity-outside-tolerance-negative-rejected-unit-price-within-tolerance.md)

**Scenario:** La quantità è sotto la tolleranza ed è rifiutata; il prezzo è entro tolleranza.

**Azione illustrativa:** La mappatura illustrativa usa la quantità approvata e mantiene il prezzo unitario.

### [Casi 8b, 9b: Quantità e prezzo fuori tolleranza (approvati)](case-8b-9b-quantity-outside-tolerance-approved-unit-price-outside-tolerance-approved.md)

**Scenario:** Entrambi gli scostamenti di quantità e prezzo sono approvati.

**Azione illustrativa:** La mappatura illustrativa usa i valori fatturati approvati e gli oneri o le rettifiche di riga espressamente configurati.

### [Caso 10b: Quantità sotto il limite e prezzo fuori tolleranza (rifiutati)](case-10b-quantity-outside-tolerance-negative-rejected-unit-price-outside-tolerance-rejected.md)

**Scenario:** Né lo scostamento negativo di quantità né quello di prezzo sono approvati.

**Azione illustrativa:** La mappatura illustrativa usa i valori del PO o quelli approvati. Le note di debito o di credito richiedono la mappatura e la decisione di approvazione corrispondenti.

### [Caso 11b: Quantità sopra il limite e prezzo fuori tolleranza (rifiutati)](case-11b-quantity-outside-tolerance-positive-rejected-unit-price-outside-tolerance-rejected.md)

**Scenario:** Lo scostamento positivo di quantità e quello di prezzo sono rifiutati.

**Azione illustrativa:** La mappatura illustrativa usa i valori approvati del PO; il trattamento delle eccedenze dipende dalla configurazione attiva.

### [Casi 12, 13: Onere di riga per unità entro tolleranza](charge-per-unit-within-tolerance.md)

**Scenario:** L’onere di riga per unità rientra nella tolleranza configurata rispetto al PO.

**Azione illustrativa:** La mappatura illustrativa accetta l’onere di riga fatturato senza rettifiche.

### [Caso 14: Onere di riga per unità fuori tolleranza (approvato)](charge-per-unit-outside-tolerance-approved-1.md)

**Scenario:** L’onere di riga per unità è fuori tolleranza ed è approvato.

**Azione illustrativa:** La mappatura illustrativa applica l’onere di riga approvato.

### [Caso 15: Onere di riga per unità fuori tolleranza (rifiutato)](charge-per-unit-outside-tolerance-rejected.md)

**Scenario:** L’onere di riga per unità è fuori tolleranza ed è rifiutato.

**Azione illustrativa:** La mappatura illustrativa usa l’onere di riga del PO o quello approvato. Qualsiasi nota per la differenza dipende dalla mappatura di esportazione.

### [Casi 12, 13: Onere di testata per unità entro tolleranza](case-12-13-header-charge-charge-per-unit-within-tolerance.md)

**Scenario:** L’onere di testata per unità rientra nella tolleranza configurata rispetto al PO.

**Azione illustrativa:** La mappatura illustrativa applica l’onere di testata fatturato senza rettifiche.

### [Caso 14: Onere di testata per unità fuori tolleranza (approvato)](charge-per-unit-outside-tolerance-approved.md)

**Scenario:** L’onere di testata per unità è fuori tolleranza ed è approvato.

**Azione illustrativa:** La mappatura illustrativa applica l’onere di testata approvato.

### [Caso 15: Onere di testata per unità fuori tolleranza (rifiutato)](case-15-header-charge-charge-per-unit-outside-tolerance-rejected.md)

**Scenario:** L’onere di testata per unità è fuori tolleranza ed è rifiutato.

**Azione illustrativa:** La mappatura illustrativa usa l’onere di testata del PO o quello approvato. Qualsiasi nota separata dipende dal trattamento configurato.

### [Righe fiscali](tax-lines.md "mention")

**Scenario:** Gli importi fiscali della fattura e del PO differiscono.

**Azione illustrativa:** La mappatura illustrativa usa aliquote e importi approvati. La configurazione va verificata rispetto ai requisiti fiscali applicabili; l’esempio non garantisce la conformità legale.
