# Importare gli elementi di costo M3 per l'estrazione delle tabelle

Quando DocBits segnala, all'apertura di un documento, che gli elementi di costo non sono configurati correttamente, controlla sia i dati importati degli elementi di costo sia l'impostazione dell'estrazione delle tabelle. Questa guida mostra dove preparare i dati e dove verificarli in DocBits. Il significato del messaggio è descritto in [Elementi di costo non configurati correttamente](../../../overview-and-basics/faq/infor-m3-m3-integration/costing-elements-are-not-properly-configured.-please-ask-your-admin-to-configure-it..md).

## 1. Preparare l'esportazione M3

1. Nel tuo ambiente M3 apri **PPS280** e seleziona le righe degli elementi di costo necessarie alla tua organizzazione. I menu e le righe disponibili dipendono dal tuo tenant M3 e dalle tue autorizzazioni.
2. Se la schermata M3 offre **Tools → Export to Excel**, esporta le righe selezionate o tutte le righe necessarie. Controlla l'ambito prima di esportare: la finestra storica mostrata sotto ha un numero massimo di righe.
3. Conserva l'esportazione originale. Lavora su una copia, così puoi confrontare ogni colonna mappata con la sua origine M3.

<figure><img src="../../../.gitbook/assets/m3-pps280-tools-export-example.png" alt="Esempio M3 storico: finestra PPS280 Costing Element con il menu Tools aperto e la voce Export to Excel"><figcaption><p>Esempio M3 storico: individua l'azione di esportazione nel tuo tenant.</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/m3-export-to-excel-dialog-example.png" alt="Finestra M3 storica Export to Excel con le opzioni per le righe selezionate, tutte le righe e il formato dei dati"><figcaption><p>Esempio M3 storico: scegli righe e formato consapevolmente.</p></figcaption></figure>

## 2. Preparare un file CSV per DocBits

Mappa l'esportazione su questi nomi di colonna prima di salvarla come file CSV. Fai verificare a chi amministra M3 il significato di ogni colonna di origine: le posizioni delle lettere in un'esportazione Excel non sono un'interfaccia stabile.

| Colonna DocBits | Valore da controllare nell'esportazione M3 |
| --- | --- |
| `costing_element` | Codice dell'elemento di costo |
| `description` | Nome leggibile dell'elemento |
| `charge_operator` | Operatore di addebito |
| `charge_type` | Tipo di addebito |
| `distribution_method` | Metodo di distribuzione |
| `distribution_type` | Tipo di distribuzione |
| `charge_sequence_number` | Numero di sequenza, se la tua configurazione lo fornisce |

Rimuovi dalla copia CSV le colonne non pertinenti. Prima dell'importazione controlla alcune righe, compresi i caratteri speciali e i valori vuoti. L'immagine seguente è un **esempio di foglio di calcolo M3 più vecchio**, non un modello di importazione DocBits.

<figure><img src="../../../.gitbook/assets/m3-costing-element-spreadsheet-example.png" alt="Foglio di calcolo M3 storico con codici e nomi degli elementi di costo e altre colonne di origine"><figcaption><p>Usa il foglio di calcolo solo per riconoscere i dati di origine; mappa le sue colonne in base al significato.</p></figcaption></figure>

## 3. Importare in DocBits

1. Apri **Impostazioni → Elaborazione dei documenti → Ricerca di dati anagrafici**. Questa pagina è descritta in [Ricerca dei dati anagrafici](../../../administration-and-setup/settings/document-processing/master-data-lookup.md).
2. Nel gruppo **Importato** seleziona l'icona con il segno più. Si apre la finestra **Caricare CSV**.
3. Inserisci `costing_element` in **Tipo di dati** e seleziona il tuo file CSV in **File**.
4. Imposta **Delimitatore** sul separatore usato dal tuo file. La finestra attuale mostra all'inizio il punto e virgola: non dare per scontato che il tuo file usi la virgola.
5. Prima di caricare, verifica con chi amministra DocBits le opzioni **Sul conflitto**, **Sostituire tutti** e **Generazione automatica dell'ID**. Queste scelte possono modificare dati già importati. **Annulla** chiude la finestra senza importare; **Caricare** avvia l'importazione dopo che file e opzioni sono stati controllati.
6. Dopo l'importazione apri la nuova voce sotto **Importato** e controlla che i codici e i nomi attesi degli elementi di costo siano visibili.

<figure><img src="../../../.gitbook/assets/dbdc-1230-lookup-master-data-it-20261113.png" alt="Pagina italiana attuale Ricerca di dati anagrafici in DocBits con i gruppi Dati di ingresso BOD, Dati API ERP, Importato e Dati anagrafici DocBits e l'icona con il segno più accanto a Importato"><figcaption><p>L'icona con il segno più accanto a Importato apre la finestra per caricare un file CSV.</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/dbdc-1230-upload-csv-it-20261113.png" alt="Finestra italiana attuale Caricare CSV con i campi Tipo di dati, File, Delimitatore e Sul conflitto e le caselle Sostituire tutti e Generazione automatica dell'ID"><figcaption><p>Tipo di dati e File sono ancora vuoti in questo esempio; il Delimitatore mostra il valore predefinito. Controlla le opzioni di sostituzione prima di caricare.</p></figcaption></figure>

## 4. Controllare l'impostazione dell'estrazione

Apri **Impostazioni → Elaborazione dei documenti → Classificazione ed Estrazione → Estrazione** e cerca l'interruttore **Estrazione della tabella per l'elemento di costo**. Verifica che l'interruttore sia attivo per i tipi di documento che stai provando. Una panoramica delle impostazioni di questa pagina è in [Classificazione ed estrazione](../../../administration-and-setup/settings/document-processing/classification-and-extraction/README.md). Riapri poi un documento adatto e controlla che il messaggio originale non compaia più. Se il messaggio rimane, comunica a chi amministra DocBits il tipo di documento, il codice dell'elemento di costo e il testo esatto del messaggio.

<figure><img src="../../../.gitbook/assets/dbdc-1230-extraction-setting-it-20261113.png" alt="Scheda Estrazione della pagina italiana Impostazioni Classificazione ed Estrazione con l'interruttore Estrazione della tabella per l'elemento di costo"><figcaption><p>L'interruttore Estrazione della tabella per l'elemento di costo si trova nella sezione Estrazione.</p></figcaption></figure>

Le schermate DocBits attuali in questa guida provengono da un ambiente di test con dati di esempio inventati. Durante la preparazione della guida non sono state importate esportazioni M3 né file CSV: controlla quindi il risultato dell'importazione nel tuo ambiente. Gli esempi M3 più vecchi mostrano schermate di un sistema di terzi e restano indipendenti dalla lingua dell'interfaccia DocBits.
