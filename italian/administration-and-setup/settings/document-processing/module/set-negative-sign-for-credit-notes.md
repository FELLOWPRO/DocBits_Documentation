# Imposta segno negativo per le note di credito

### Panoramica

L'impostazione **Imposta segno negativo per le note di credito** (Set Negative Sign for Credit Notes) garantisce che le **note di credito** vengano memorizzate con **importi negativi**. Una nota di credito storna o rimborsa parte di una fattura, quindi in contabilità i suoi valori dovrebbero ridurre i totali, ovvero essere negativi. Quando questa impostazione è attiva, DocBits applica automaticamente tale segno negativo.

Questa impostazione è **attivata per impostazione predefinita**.

### Cosa fa?

Quando un documento viene riconosciuto come **nota di credito**, DocBits converte automaticamente i suoi importi in valori negativi durante l'elaborazione. Ciò riguarda i campi monetari, inclusi gli importi netti, gli importi delle imposte e i totali (ad esempio importo netto, importo imposta, importo totale imposta, importo netto totale e importo totale).

* **Attivata (predefinita)** — Gli importi delle note di credito vengono salvati come valori negativi (ad esempio, `150,00` diventa `-150,00`). Le fatture normali non sono interessate.
* **Disattivata** — Gli importi vengono mantenuti esattamente come letti dal documento, senza alcun cambio di segno.

{% hint style="info" %}
Questo vale solo per i documenti identificati come **note di credito**. Le fatture normali rimangono sempre invariate.
{% endhint %}

### Vantaggi

* **Contabilità corretta**: Le note di credito riducono i saldi, quindi i valori negativi sono ciò che i vostri sistemi contabili ed ERP si aspettano.
* **Nessuna modifica manuale**: Il vostro team non deve invertire il segno a mano per ogni nota di credito.
* **Coerenza**: Ogni nota di credito viene trattata allo stesso modo in tutta l'organizzazione.

### Come usarla

1. Vai su **Impostazioni**.
2. Seleziona **Elaborazione documenti**.
3. Seleziona **Modulo**.
4. Apri la sezione **Tipo di documento**.
5. Trova **Imposta segno negativo per le note di credito** e attiva o disattiva l'interruttore.

### Quando usare questa funzione

* **Lasciala attivata** se il tuo sistema contabile o ERP si aspetta che le note di credito arrivino con importi negativi (questa è la configurazione più comune).
* **Disattivala** solo se il tuo sistema a valle gestisce già il segno da sé o si aspetta che gli importi delle note di credito rimangano positivi.
