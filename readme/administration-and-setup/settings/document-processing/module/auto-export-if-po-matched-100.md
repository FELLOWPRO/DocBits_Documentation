# Esportazione automatica con corrispondenza PO al 100%

### Panoramica

L’opzione **Auto Export if PO matched 100%**, nel modulo degli ordini di acquisto (PO), consente a una corrispondenza completa con il PO di autorizzare l’avanzamento della fattura o del documento corrente verso l’esportazione automatica. L’ordine di acquisto è il riferimento di confronto; questa opzione non esporta l’ordine stesso.

### Funzionamento

Quando è attiva, viene verificato il risultato dell’abbinamento del documento corrente al PO. Una corrispondenza del 100% soddisfa questa condizione, ma non garantisce un’esportazione immediata. La convalida del documento, il flusso di esportazione configurato, le approvazioni necessarie e le attività in sospeso possono ancora bloccare o ritardare l’esportazione. Una corrispondenza incompleta blocca l’esportazione automatica in base a questa condizione.

### Vantaggi

* **Efficienza:** Può ridurre gli interventi manuali per le fatture completamente abbinate al PO che soddisfano anche gli altri requisiti.
* **Controllo:** Aggiunge il risultato dell’abbinamento al PO come condizione di esportazione.
* **Tempi:** Può accelerare l’elaborazione delle fatture idonee; il momento dell’esportazione dipende dalle altre condizioni del flusso.

### Utilizzo

1. **Attivare la funzione:**
   * Aprire **Impostazioni** → **Elaborazione documenti** → **Modulo** → **Ordine di acquisto**.
   * Attivare il selettore **Auto Export if PO matched 100%**.

<figure><img src="../../../../.gitbook/assets/100%PO.png" alt="Pagina delle impostazioni con la navigazione Elaborazione documenti e la tabella di esportazione che mostra le colonne Tipo, Sotto-Organizzazioni, Titolo e Metodo Di Esportazione"><figcaption></figcaption></figure>

2. **Monitorare l’elaborazione:**
   * Controllare gli stati di abbinamento, convalida ed esportazione della fattura corrente.
   * Se non viene esportata nonostante una corrispondenza del 100%, verificare la configurazione di esportazione, le approvazioni e le attività in sospeso.
3. **Verificare la configurazione:**
   * Assicurarsi che i criteri di abbinamento e le impostazioni di esportazione corrispondano al flusso previsto.
   * Esaminare regolarmente le fatture esportate e le eccezioni.

### Quando utilizzarla

* **Volumi elevati di fatture:** Quando molte fatture possono essere abbinate in modo affidabile agli ordini di acquisto.
* **Acquisti ricorrenti:** Quando quantità, prezzi e altri criteri sono stabili.
* **Elaborazione urgente:** Quando le fatture idonee devono avanzare automaticamente dopo il soddisfacimento di tutte le condizioni.

Quando l’abbinamento agli ordini è attivo per il tipo di documento, l’opzione separata `ALLOW_AUTO_EXPORT_FOR_NON_MATCHABLE_PO_LINES` consente anche lo stato `NO_MATCHABLE_PO_LINES`. Non autorizza in generale gli altri stati di abbinamento incompleto.
