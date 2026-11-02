---
description: "Scaricare fattura sintetica, workflow JSON, input, aspettative e risposte reali di test."
---

# Pacchetto di formazione sui workflow

Usare il pacchetto con il [caso Advanced](advanced-workflow-case-study.md). Comprende fattura sintetica, workflow importabile, sette input documentali completi, aspettative indipendenti e risposte reali salvate. Chiavi tecniche e nomi dei percorsi restano identici in tutte le lingue.

{% file src="../../.gitbook/assets/workflow-training-kit-v2.zip" %}
Pacchetto di formazione con esempi e risultati
{% endfile %}

## Contenuto e formati

| File | Utilizzo |
| --- | --- |
| `training-invoice.pdf` | Fattura sintetica: 1500 EUR netti, 285 EUR d’imposta, totale 1785 EUR. Non pagabile. |
| `advanced-workflow.json` | Importare disattivato con **Import Workflow**; nessuna variabile globale, limitato a Fattura e numero esatto di formazione. |
| `*-input.json` | Dati completi per **Advanced Test → Custom Data**. |
| `expectations.json` | Percorsi, messaggi di stato e risultati attesi; specifica funzionale, non file da caricare in Test Manager. |
| `*-result.json` | Risposte reali Dev con risultati e messaggi; riferimenti privati all’organizzazione sostituiti. |
| `prepare_inputs.py` | Sostituisce l’organizzazione sintetica nelle due posizioni richieste. |
| `verify_results.py` | Verifica le risposte rispetto ad aspettative indipendenti. Richiede Python 3, nessuna chiave d’accesso. |

## Utilizzo

1. Estrarre lo ZIP e leggere le istruzioni incluse.
2. Importare il workflow nell’organizzazione di test e verificarne la disattivazione.
3. Individuare l’ID della propria organizzazione di test ed eseguire localmente:

```bash
python3 prepare_inputs.py --org-id YOUR_TEST_ORGANIZATION_UUID --out prepared
python3 verify_results.py
```

4. Usare i file di `prepared/` nella finestra Advanced. Non sostituire un ID documentale sintetico con una fattura cliente in corso.
5. Verificare i sette casi nella [tabella dei risultati](advanced-workflow-case-study.md). Le variazioni d’importo sono intenzionali e non modificano la fattura allegata.

I dati includono `id`, `org_id`, `doc_type`, `status` ed `extracted_data` con `layout.groups`, `fields` e `tables`. L’organizzazione iniziale e quella in `extracted_data` devono corrispondere all’account collegato. Un valore senza la relativa definizione nel layout può non essere letto come campo documentale esistente.

## Ambito dell’esercizio

Le aspettative controllano percorsi, testo di instradamento, messaggi di stato e nodi finali, oltre allo stato documentale. Non equivalgono al confronto di stato di uno scenario Test Manager salvato.

Un test Advanced riuscito conferma l’elaborazione degli input forniti. Le azioni simulate non sono assegnazioni, email o consegne reali. L’attivazione richiede un ingresso evento appropriato e un’esecuzione reale verificata separatamente. Vedere [Quando viene eseguito il mio workflow?](workflow-execution-model.md).

## WF-03: Esercizio e collaudo

Estrarre v2, adattare l’organizzazione con prepare_inputs.py ed eseguire verify_results.py. decision-table-setup.json guida la configurazione e acceptance-record-template.json è un modello di verbale; nessuno importa workflow. Confermare lo stato inattivo prima dell’importazione.

[Percorso](workflow-learning-path.md)
