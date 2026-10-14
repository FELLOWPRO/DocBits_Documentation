# Flusso Documento

Il **Flusso Documento** mostra i passaggi di elaborazione di un documento. Usalo per vedere quali passaggi sono stati completati, quale è in attesa e quanto tempo è durata l'elaborazione. L'esempio qui sotto usa una fattura sintetica nella Sandbox inglese.

## Aprire dal Dashboard

Nel **Dashboard**, trova il documento. Nella colonna **Azioni**, seleziona i tre puntini, quindi **Flusso Documento**. L'opzione apre il flusso di quel documento; non lo modifica.

<figure><img src="../../../.gitbook/assets/document-flow-dashboard-menu-en.png" alt="Dashboard in inglese con il menu Azioni aperto per una fattura sintetica; Document flow è elencato sotto Assign to."><figcaption>Scegli Flusso Documento dal menu Azioni del documento.</figcaption></figure>

## Aprire dalla Validazione Campo

Apri il documento. Nella **Validazione Campo**, seleziona i tre puntini nella barra delle azioni a destra, quindi **Flusso Documento** sotto **More options**.

<figure><img src="../../../.gitbook/assets/document-flow-validation-menu-en.png" alt="Schermata Validazione Campo in inglese con il menu More options e la voce Document Flow accanto a una fattura sintetica."><figcaption>Lo stesso flusso è disponibile dalla vista del documento.</figcaption></figure>

## Leggere il flusso

**Process Statistics** sulla sinistra riepiloga il numero di passaggi, i passaggi completati e in attesa, i riavvii, il tempo totale, lo stato corrente e l'avanzamento complessivo. Ogni card numerata mostra un passaggio di elaborazione e il suo stato attuale. Scorri verso il basso per vedere i passaggi successivi.

<figure><img src="../../../.gitbook/assets/document-flow-overview-en.png" alt="Flusso Documento in inglese con Process Statistics a sinistra e le prime card numerate dei passaggi: Imported, Document Imported e OCR."><figcaption>I primi passaggi del flusso di una fattura sintetica.</figcaption></figure>

<figure><img src="../../../.gitbook/assets/document-flow-later-steps-en.png" alt="Flusso Documento in inglese dopo lo scorrimento verso il basso; le card successive includono Classification, Field Extraction, Table Extraction, Transformer, Metadata Populator, Lookup Data e Validator."><figcaption>Scorri per seguire la sequenza attraverso i passaggi successivi.</figcaption></figure>

Seleziona la card di un passaggio per aprire **Step Details** sulla sinistra. Mostra il modulo e il suo stato. Sulla destra può aprirsi anche un pannello **Task Logs**; i dettagli del log dipendono da ciò che è disponibile per quel task. Seleziona **×** in Step Details per chiudere il pannello.

<figure><img src="../../../.gitbook/assets/document-flow-step-details-en.png" alt="Flusso Documento in inglese con la card OCR selezionata; Step Details sotto Process Statistics mostra Module OCR e Status Completed."><figcaption>Step Details spiega lo stato del modulo selezionato.</figcaption></figure>
