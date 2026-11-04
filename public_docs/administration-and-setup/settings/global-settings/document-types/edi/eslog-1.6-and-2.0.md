# eSLOG 1.6 e 2.0

**eSLOG 1.6** e **eSLOG 2.0** compaiono come formati di fattura elettronica separati in DocBits. Scegli la versione utilizzata dalle fatture slovene in arrivo. Gli screenshot mostrano l'interfaccia italiana in un'organizzazione di documentazione di prova. I nomi, le versioni, le date e gli autori esistenti sono mascherati; le immagini non dimostrano che una fattura di una delle due versioni sia stata elaborata con successo.

## Trovare le configurazioni

1. Vai su **Impostazioni → Tipi di Documento → Fattura → E-Doc**.
2. Espandi **E-SLOG 1.6** oppure **E-SLOG 2.0**. Ogni formato ha tre voci proprie.

<figure><img src="../../../../../.gitbook/assets/dbdc-106-eslog-16-native-it-20261101.png" alt="Elenco E-Doc italiano E-SLOG 1.6 con tre righe di configurazione; nomi, versioni e date esistenti mascherati"><figcaption>E-SLOG 1.6: dall’alto in basso, Trasformazione, Anteprima e Percorsi di estrazione. Questa vista di prova contiene due righe Predefinito e una riga Personalizzato esistente. Nomi, versioni e date sono mascherati.</figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/dbdc-106-eslog-20-native-it-20261101.png" alt="Elenco E-Doc italiano E-SLOG 2.0 con tre righe di configurazione; nomi, versioni e date esistenti mascherati"><figcaption>E-SLOG 2.0: voci separate per gli stessi tre passaggi, qui tutte contrassegnate come Predefinito. Nomi, versioni e date sono mascherati.</figcaption></figure>

| Voce | Cosa controlla | Guida successiva |
| --- | --- | --- |
| **TRANSFORMATION (XSLT)** | Converte i dati sorgente del formato in XML strutturato. | [Trasformazione](edi/edi-transformation-file-guide.md) |
| **PREVIEW (XSLT)** | Definisce la vista leggibile del documento. | [Anteprima](edi/edi-preview-file-guide.md) |
| **EXTRACTION PATHS (JSON)** | Mappa i valori XML nei campi e nelle tabelle di DocBits. | [Percorsi di estrazione](edi/edi-extraction-paths-file-guide.md) |

Fai clic su una riga per vederne le versioni e la configurazione. **Predefinito** identifica la voce fornita; **Personalizzato** una variante propria dell'organizzazione. **Ultima modifica a** mostra quando quella voce è stata modificata l'ultima volta. Il pulsante **Nuovo** apre il modulo per una voce di configurazione aggiuntiva. Il menu a tre punti di una voce predefinita offre **Personalizzazione**, che crea una copia specifica dell'organizzazione, e **Cancellare** (visibile agli amministratori). Verifica bene la riga selezionata prima di usare Cancellare.

<figure><img src="../../../../../.gitbook/assets/dbdc-106-eslog-version-panel-native-it-20261101.png" alt="Pannello Version italiano della configurazione standard E-SLOG 1.6 con badge Attivo e matita; numero di versione, data e autore mascherati"><figcaption>Il pannello <strong>Version</strong> della configurazione standard E-SLOG 1.6: il badge <strong>Attivo</strong> identifica la versione attiva, con la matita accanto. Numero di versione, data e autore sono mascherati.</figcaption></figure>

All'interno di una configurazione, la matita accanto a una versione attiva crea una bozza. Verifica una bozza con il pannello di prova **Anteprima** e un ID documento caricato rappresentativo prima di attivarla con il segno di spunta. L'icona del cestino di una bozza rimuove quella bozza. I nomi dei campi e i percorsi XML effettivi dipendono dal tuo file eSLOG; usa la guida corrispondente qui sopra per i dettagli dell'editor.
