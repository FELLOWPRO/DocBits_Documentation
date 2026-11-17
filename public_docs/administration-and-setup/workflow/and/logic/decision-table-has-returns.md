# La tabella decisionale restituisce risultati

<figure><img src="../../../../.gitbook/assets/workflow_card_condition_decision_tree_data_v2-it-it.png" alt="La tabella decisionale restituisce risultati, Versione 2" width="634"><figcaption><p>Versione 2</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/workflow_card_condition_decision_tree_data_v3-it-it.png" alt="La tabella decisionale restituisce risultati, Versione 3" width="634"><figcaption><p>Versione 3</p></figcaption></figure>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-decision-table/v1/it.mp4" %}

**Video:** Scheda: Tabella delle decisioni con valori restituiti · 0:49 · [Sottotitoli (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-decision-table/v1/it.vtt)

<details>

<summary>Trascrizione</summary>

**Tabella delle decisioni con valori restituiti** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-decision-table/v1/it.mp4#t=0.25)

La scheda Tabella delle decisioni contiene valori restituiti esegue la tabella per il documento. Scegli la tabella, per esempio Example approvers, e se memorizzare i dati restituiti per le schede successive.

**Una riga corrispondente significa vero** · [0:17](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-decision-table/v1/it.mp4#t=17.416)

Se una riga della tabella corrisponde al documento, la scheda è vera. Se nessuna riga corrisponde, è falsa. I dati memorizzati servono alle schede successive, come le schede di assegnazione. Un Workflow conserva solo l'ultimo risultato memorizzato.

**Esempio: approvatori da una tabella** · [0:34](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-decision-table/v1/it.mp4#t=34.983)

Per esempio, la tabella trova gli approvatori per l'importo della fattura e li memorizza, e la scheda successiva assegna loro la fattura. Se la tabella non trova nessuno, la scheda è falsa e l'assegnazione non parte.

</details>

## **Scopo:**

Questa scheda DocBits verifica se una decision table specificata restituisce valori per un determinato documento e determina se i dati restituiti debbano essere utilizzati nei passaggi successivi del workflow. Garantisce che i workflow possano adattarsi dinamicamente in base agli esiti della decision table.

## **Funzionalità:**

* **Validazione della decision table:** Questa scheda verifica se la decision table selezionata fornisce valori di ritorno per il documento in elaborazione.
* **Selezione della decision table:** Gli utenti specificano il nome della decision table da verificare.
* **Utilizzo dei dati di ritorno:** Gli utenti possono specificare se utilizzare i dati di ritorno nelle schede successive con un'impostazione **Booleano**:
  * **True:** I dati di ritorno sono disponibili e verranno utilizzati nei passaggi successivi del workflow.
  * **False:** I dati di ritorno non verranno utilizzati e il workflow procede senza di essi.

## **Utilizzo:**

Questa scheda è ideale per i workflow che coinvolgono logica condizionale o processi decisionali basati su regole predefinite in una decision table. Garantisce un'integrazione fluida degli output della decision table nei processi di workflow.

## **Scenario di esempio:**

* Un utente configura la scheda per verificare i valori di ritorno della decision table **"Regole per il trattamento delle fatture"**. Il valore **Booleano** è impostato su **True**, a indicare che i dati di ritorno (es. i requisiti di approvazione) verranno utilizzati nelle schede successive per guidare le decisioni del workflow.

Utilizzando la scheda "Decision Table Check", le organizzazioni possono migliorare la flessibilità dei workflow, semplificare l'elaborazione basata su regole e garantire coerenza nel processo decisionale tra i workflow automatizzati.
