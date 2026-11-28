# Quantità esportata nell'unità di misura base

L'interruttore **Export quantity in base unit of measure** si trova nella sezione **Purchase Order** dei **More Settings** di un tipo di documento. Modifica la quantità e il prezzo unitario che l'esportazione verso Infor LN scrive per le righe di ordine abbinate.

Aprilo in **Settings → Document Types**, seleziona l'icona a ingranaggio (**More Settings**) sulla scheda del tipo di documento ed espandi **Purchase Order**.

## Cosa fa l'interruttore

* **Off:** DocBits esporta la quantità e il prezzo unitario nell'unità della fattura.
* **On:** DocBits converte la quantità e il prezzo unitario di ogni riga di ordine abbinata nell'unità di misura base di quella riga, usando il relativo fattore di conversione, e scrive il codice dell'unità base invece del codice dell'unità fatturata.

Una riga senza fattore di conversione viene esportata invariata, quindi un fattore mancante non blocca l'esportazione.

{% hint style="info" %}
La conversione vale solo per l'esportazione verso Infor LN. Gli altri destinatari dell'esportazione mantengono l'unità fatturata.
{% endhint %}

## Quando usarlo

Attiva l'interruttore quando l'istanza Infor LN si aspetta quantità d'ordine nell'unità di misura base. La conversione usa il fattore memorizzato sulla riga d'ordine, non un fattore che DocBits calcola dall'anagrafica articoli.

Le impostazioni possono influire sui documenti in produzione. Verifica il risultato con un documento di prova prima di salvare la modifica in produzione. L'interruttore cambia i valori esportati; non cambia il modo in cui vengono abbinate le righe di fattura e d'ordine.

## Pagine correlate

* [Ordine di acquisto](README.md)
* [Esporta righe di PO non corrispondenti](export-not-matched-po-lines.md)
* [Esportazione alternativa](alternate-export.md)

<!-- Documentation review 2026-11-27: switch label, help text and behaviour checked against DocBits_Web src/pages/Settings/Components/DocTypes/PO.vue on origin/sandbox-nova (DOP-53, commit feb262ab89, contained in the deployed NOVA build 11.24.8). -->
