# Caso 8b, 9b: Quantità fuori tolleranza (Approvato), Prezzo unitario fuori tolleranza (Approvato)

Lo scenario seguente illustra una mappatura configurata, non un modello predefinito di cui sia stata verificata la distribuzione. L’output effettivo, gli importi, i segni e i tipi di documento dipendono dalle regole e dalle espressioni `conflict_resolution` attive, dalla mappatura di esportazione e dalle decisioni di approvazione. Qualsiasi nota di debito o di credito descritta è subordinata a tale configurazione; l’esempio non ne garantisce l’emissione automatica né la conformità legale.

## Scenario:

Sia la quantità che il prezzo unitario non rientrano nell'intervallo di tolleranza ma sono stati approvati.

## Azione:

Il sistema elabora la transazione utilizzando i valori della fattura sia per la quantità che per il prezzo unitario, applicando eventuali rettifiche o addebiti di riga necessari.

## Esempio:

* **Purchase Order (PO):**
  * Quantity: 200 units
  * Prezzo unitario: $25.00 per unità
  * Total Amount: $5,000.00
* **Invoice Received:**
  * Quantità: 220 unità (tolleranza esterna del 10%, approvata)
  * Prezzo unitario: $27.00 per unità (tolleranza esterna dell'8%, approvata)
  * Total Amount: $5,940.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±5%
  * Tolleranza prezzo unitario: ±2%

Poiché sia la quantità (220 unità) che il prezzo unitario ($27.00) non rientrano nei limiti di tolleranza accettabili ma sono stati approvati, il sistema:

1. **Accetta la quantità approvata:** Il sistema accetta la quantità fatturata di 220 unità poiché è stata approvata nonostante sia al di fuori dell'intervallo di tolleranza.
2. **Accetta il prezzo unitario approvato:** Il sistema accetta il prezzo unitario fatturato di $27.00 per unità poiché è stato approvato nonostante sia al di fuori dell'intervallo di tolleranza.
3. **Calcola l'importo totale:** Il sistema calcola l'importo totale in base ai valori della fattura approvati:
   * **Importo totale = Quantità × Prezzo unitario**
   * **Importo totale = 220 unità × $27.00 per unitàà = $5,940.00**
4. **Applica le rettifiche necessarie o gli addebiti di riga:** Se applicabile, il sistema può applicare eventuali addebiti o rettifiche di linea aggiuntivi in base alle politiche dell'organizzazione per la gestione delle variazioni approvate.
5. **Elabora la fattura:** Il sistema elabora la fattura utilizzando i valori approvati sia per la quantità che per il prezzo unitario, finalizzando la transazione all'importo totale di $5,940.00.

Questo approccio garantisce che la transazione venga elaborata in base alle variazioni approvate, consentendo flessibilità pur mantenendo registri finanziari accurati.
