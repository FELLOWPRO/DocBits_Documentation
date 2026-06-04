# Assign document to matching sub organization

<figure><img src="../../../../.gitbook/assets/image (303).png" alt="" width="563"><figcaption></figcaption></figure>

## **Scopo:**

La scheda di workflow **"Assign Document to Matching Sub-Organization Based on Field"** assegna un documento a una sotto-organizzazione in modo dinamico, in base a un campo specificato nel documento. Se non viene trovata alcuna sotto-organizzazione corrispondente, la scheda utilizza una sotto-organizzazione di riserva predefinita.

## **Componenti della scheda:**

1. **Field Name**
   * **Descrizione:** Specifica il campo del documento da utilizzare per determinare la sotto-organizzazione corrispondente.
   * **Dettaglio:** La scheda cerca un valore nel campo specificato per abbinarlo a una sotto-organizzazione disponibile.
2. **Sub-Organization (Fallback)**
   * **Descrizione:** Definisce la sotto-organizzazione di riserva da utilizzare se non viene trovata alcuna corrispondenza nel campo specificato.
   * **Dettaglio:** Se il valore del campo non corrisponde a nessuna sotto-organizzazione, il documento verrà assegnato alla sotto-organizzazione di riserva selezionata.

## **Funzionalità:**

* **Valutazione della condizione:**\
  La scheda esegue la sua azione solo se sia la sezione **"Where"** che la sezione **"And"** risultano vere.
* **Assegnazione dinamica:**\
  La scheda verifica il valore del campo specificato e assegna il documento alla sotto-organizzazione che corrisponde a tale valore.
* **Meccanismo di riserva:**\
  Se non viene trovata alcuna sotto-organizzazione corrispondente, il documento viene assegnato alla sotto-organizzazione di riserva.

## **Configurazione e impostazione:**

* **Seleziona il Field Name:**\
  Scegli il campo del documento che contiene il valore da abbinare a una sotto-organizzazione.
* **Seleziona la Sub-Organization di riserva:**\
  Scegli la sotto-organizzazione che verrà utilizzata se non viene trovata alcuna corrispondenza nel campo del documento.

## **Conclusione:**

La scheda di workflow **"Assign Document to Matching Sub-Organization Based on Field"** offre flessibilità instradando dinamicamente i documenti alla sotto-organizzazione appropriata, con un'opzione di riserva aggiuntiva per garantire che nessun documento rimanga non assegnato.
