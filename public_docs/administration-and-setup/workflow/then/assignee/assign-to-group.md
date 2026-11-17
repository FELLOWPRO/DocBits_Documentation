# Assegna al gruppo

<figure><img src="../../../../.gitbook/assets/workflow_card_doc_group_assign_v2-it-it.png" alt="Assegna al gruppo, Versione 2" width="634"><figcaption><p>Versione 2</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/workflow_card_doc_group_assign_v3-it-it.png" alt="Assegna al gruppo, Versione 3" width="634"><figcaption><p>Versione 3</p></figcaption></figure>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-assign-group/v1/it.mp4" %}

**Video:** Scheda: Assegna il documento a un gruppo · 0:52 · [Sottotitoli (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-assign-group/v1/it.vtt)

<details>

<summary>Trascrizione</summary>

**Assegna il documento a un gruppo** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-assign-group/v1/it.mp4#t=0.25)

La scheda Assegnare al gruppo dà il documento a un gruppo, per esempio Accounts payable. La versione tre, scelta con l'etichetta della versione, aggiunge una seconda impostazione: se una tabella delle decisioni può scegliere il gruppo al suo posto.

**Albero decisionale: prima il gruppo della tabella** · [0:21](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-assign-group/v1/it.mp4#t=21.683)

Con l'albero decisionale attivo, la scheda prende il gruppo restituito da una scheda tabella delle decisioni precedente nel Workflow. Se la tabella non ha restituito alcun gruppo, il gruppo sulla scheda riceve il documento. La versione due assegna sempre il gruppo sulla scheda.

**Esempio: gruppo dalla tabella, riserva sulla scheda** · [0:39](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-assign-group/v1/it.mp4#t=39.716)

Per esempio, una tabella delle decisioni restituisce il gruppo del fornitore e la scheda di assegnazione lo usa. Senza gruppo dalla tabella, Accounts payable riceve la fattura.

</details>

## Scopo:

La scheda di workflow **"Assign to Group"** facilita l'assegnazione dei documenti a un **gruppo** specifico all'interno del sistema. Ciò garantisce che il documento venga elaborato dal team appropriato, semplificando il workflow. Potenziata nelle versioni successive, introduce la funzionalità decision tree per l'assegnazione dinamica dei gruppi.

## Componenti della scheda:

1. **Gruppi**
   * **Descrizione:** Specifica il **gruppo** a cui verrà assegnato il documento.
   * **Dettaglio:** Selezionato da un menu a discesa dei **gruppi** disponibili.

## **Componenti aggiuntivi nella Versione 3**

1. **Decision Tree (solo Versione 3)**
   * **Descrizione:** Consente l'utilizzo di una decision tree per determinare dinamicamente il **gruppo** a cui assegnare il documento.
   * **Opzioni:**
     * **True:** Abilita l'elaborazione della decision tree.
     * **False:** Disabilita l'elaborazione della decision tree.

## Funzionalità:

* **Valutazione della condizione:** La scheda esegue la sua azione solo se sia la sezione **"Quando"** che la sezione **"E"** risultano vere.
* **Assegnazione del documento:** Assegna il documento al **gruppo** selezionato. Nella **Versione 3**, la **albero decisionale** determina dinamicamente il gruppo di destinazione se abilitata.

## Configurazione e impostazione:

* **Seleziona il Gruppo:** Scegli il **gruppo** dal menu a discesa a cui assegnare il documento.
* **Utilizza l'albero decisionale (solo versione 3):** Abilita questa opzione se la **albero decisionale** deve essere utilizzata per l'assegnazione dinamica.

## Conclusione:

La scheda di workflow **"Assign to Group"** automatizza l'assegnazione dei documenti a **gruppi** predefiniti, migliorando il coordinamento del team. La **Versione 3** introduce la possibilità di assegnare dinamicamente i gruppi in base alla logica della decision tree.

<!-- workflow-card-practical-example-20261021 -->

## Esempio pratico

**Quando utilizzarlo:** Inserisci un documento in una coda di revisione condivisa.

**Configurazione:** Seleziona il gruppo configurato `Demo Finance`.

**Risultato atteso e controesempio:** Il documento viene assegnato al gruppo selezionato. Si tratta di un'assegnazione di documenti, non di una promessa di creazione di un'attività o di un'e-mail aggiuntiva.

Questa è una configurazione illustrativa e il risultato atteso. Utilizza campi, utenti e gruppi configurati nella tua organizzazione di test; non si afferma che questo esempio sia stato eseguito.
