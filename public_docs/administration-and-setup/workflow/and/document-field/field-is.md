# Verificare la presenza e il contenuto di un campo

<figure><img src="../../../../.gitbook/assets/workflow_card_condition_docfield_status_v1-it-it.png" alt="Verificare la presenza e il contenuto di un campo, Versione 1" width="634"><figcaption><p>Versione 1</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/workflow_card_condition_docfield_status_v2-it-it.png" alt="Verificare la presenza e il contenuto di un campo, Versione 2" width="634"><figcaption><p>Versione 2</p></figcaption></figure>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-docfield-status/v1/it.mp4" %}

**Video:** Scheda: Campo vuoto o no · 0:49 · [Sottotitoli (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-docfield-status/v1/it.vtt)

<details>

<summary>Trascrizione</summary>

**Campo vuoto o no** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-docfield-status/v1/it.mp4#t=0.25)

La scheda Il campo è controlla se un campo del documento è vuoto. Scegli il campo, per esempio Ordine di acquisto, e lo stato: vuoto o non presente nel documento, oppure presente nel documento e non vuoto.

**Mancante conta come vuoto** · [0:18](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-docfield-status/v1/it.mp4#t=18.716)

Un campo conta come vuoto se non ha valore, solo spazi, una casella non selezionata o un elenco vuoto. Anche un campo non presente nel documento conta come vuoto. Se lo stato corrisponde, la scheda è vera. Altrimenti è falsa.

**Esempio: nessun ordine di acquisto** · [0:34](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-docfield-status/v1/it.mp4#t=34.75)

Per esempio, una fattura senza ordine di acquisto va all'approvatore delle fatture senza ordine. Le fatture con un ordine di acquisto prendono l'altro percorso, per esempio l'abbinamento con l'ordine.

</details>

## Quando usarla

Usare questa scheda per verificare se un campo del documento è vuoto o assente, ad esempio quando una fattura senza numero richiede un controllo aggiuntivo. Si tratta di una condizione; configurare separatamente l’azione successiva.

**Posizione:** Workflow standard → condizioni aggiuntive (AND) → Campo del documento.

## Configurazione — versione 2

| Impostazione | Valore di esempio |
| --- | --- |
| Campo | `invoice_id` — numero di fattura |
| Stato del campo | Vuoto o assente (`field_empty`) |

Selezionare un campo realmente configurato nella propria organizzazione. L’opzione `field_not_empty` verifica se il campo contiene un valore.

<!-- workflow-card-practical-example-20261021 -->

## Esempio pratico

| Valore di esempio | Risultato atteso per `field_empty` |
| --- | --- |
| Campo vuoto o assente | Condizione soddisfatta |
| `DEMO-001` | Condizione non soddisfatta |
| Numero presente ma errato | Condizione non soddisfatta — il campo contiene ancora un valore |

Gli esempi mostrano risultati attesi. Per verificare la validità del numero stesso, aggiungere una condizione adatta al contenuto; questa scheda controlla lo stato del campo. Nella versione 2, gli spazi iniziali e finali vengono rimossi dal testo prima di verificare se il campo è vuoto. Alcune etichette dell’interfaccia sono ancora in inglese nella versione mostrata.

## Video di esempio con un amministratore

Quando uso questa scheda, dove trovarla e come individuare i numeri di fattura mancanti. Gli esempi mostrano i risultati attesi.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-field-status-admin/v1/it.mp4" %}

[Apri il video con sottotitoli italiani](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-field-status-admin/v1/it-theme-v4.html)

[Leggi la trascrizione](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-field-status-admin/v1/it.txt)
