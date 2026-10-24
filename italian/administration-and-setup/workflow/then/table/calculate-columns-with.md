# Calcola colonne con

La scheda applica un’operazione a due colonne di una tabella e salva il risultato in un’altra colonna, per ogni riga.

## Quando e dove utilizzarla

Usala per calcolare gli importi delle righe prima dell’azione successiva del workflow, per esempio **quantità × prezzo unitario**. Aggiungila nella sezione **Poi**, categoria **Tabella**. Prima verifica che le due colonne di ingresso contengano numeri e che i dati siano completi.

<figure><img src="../../../../.gitbook/assets/workflow-card-calc-columns-v2-configured-it-20261024.png" alt="Scheda versione 2: INVOICE_TABLE, Quantità × Prezzo unitario → TOTAL_AMOUNT. L’interfaccia ripete il nome della tabella." width="650"><figcaption><p>Scheda versione 2: INVOICE_TABLE, Quantità × Prezzo unitario → TOTAL_AMOUNT. L’interfaccia ripete il nome della tabella.</p></figcaption></figure>

## Video di amministrazione

**Anteprima · 40 secondi · italiano.** Roberto spiega quando usare la scheda, configura la moltiplicazione e mostra i risultati salvati.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-calc-columns-preview-admin/v1/it.mp4" %}

[Guarda il video con sottotitoli italiani](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-calc-columns-preview-admin/v1/it.html) · [Leggi la trascrizione](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-calc-columns-preview-admin/v1/it.txt)

L’amministratore e la sua voce sono sintetici. La dimostrazione usa l’interfaccia reale di DocBits e una fattura fittizia.

## Configurazione della scheda

| Campo | Selezione dell’esempio |
| --- | --- |
| Tabella | `INVOICE_TABLE` |
| Prima colonna | `QUANTITY` — Quantità |
| Operazione | `*` — moltiplicazione |
| Seconda colonna | `UNIT_PRICE` — Prezzo unitario |
| Colonna del risultato | `TOTAL_AMOUNT` — Importo totale |

Sono disponibili anche `+` (addizione), `-` (sottrazione) e `/` (divisione). L’ordine delle colonne conta per sottrazione e divisione. Seleziona gli identificativi configurati nella tua organizzazione.

<!-- workflow-card-practical-example-20261021 -->

## Esempio pratico

La fattura contiene due righe. Prima del calcolo la colonna del risultato non esiste ancora:

| Riga | Quantità | Prezzo unitario | Risultato salvato in `TOTAL_AMOUNT` |
| --- | ---: | ---: | ---: |
| 1 | 2 | 10 | 20 |
| 2 | 3 | 4 | 12 |

Nella dimostrazione, la scheda crea la colonna del risultato. I valori **20,00** e **12,00** restano visibili dopo aver riaperto la fattura. In questo esempio le colonne di ingresso e gli importi originali di `NET_AMOUNT` vengono conservati. Se la colonna del risultato scelta contiene già valori, il calcolo li sostituisce.

## Controlli e controesempi

- Controlla entrambe le colonne di ingresso e verifica i risultati salvati dopo il calcolo.
- Nell’esempio illustrato, un prezzo mancante può dare zero. Questo zero non dimostra che i dati siano completi: verifica gli ingressi prima di calcolare.
- Un testo come `ABC` al posto di un numero provoca un errore di calcolo. Correggi il valore e verifica di nuovo il caso.
- I casi del prezzo mancante e del testo non numerico nello schema sono risultati attesi per illustrare i controlli; non sono esecuzioni della fattura a due righe mostrata.
