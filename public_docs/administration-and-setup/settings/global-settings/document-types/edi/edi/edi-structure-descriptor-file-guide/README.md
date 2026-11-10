# Guida al file Structure Descriptor per EDI

## 1. Overview

Il **Structure Descriptor File** è un file **JSON** che definisce come i segmenti EDI ripetuti (ad esempio `N1`–`N4`) vengono raggruppati in un output strutturato. È il primo passaggio dell'elaborazione EDI:

* **Analisi accurata** dei segmenti correlati come singole unità.
* **Output coerente** per la [Transformation](../edi-transformation-file-guide.md) e per i sistemi a valle.

_Per un esempio completo con il dettaglio dei segmenti, vedere_ [_Structure Descriptor Example_](edi-structure-descriptor.md)_._

## 2. Access & Basic Editing

#### **Accesso al file**

1. Andare in **Settings** → **Document Types** e aprire **E-Doc** per il tipo di documento che si desidera configurare (ad esempio _Purchase Order_). Per modificare questi file è necessario disporre dei diritti di amministratore nella propria organizzazione.

    <!-- dbdc-139-edi-sd-list-en.png --><figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/dbdc-139-edi-sd-list-en.png" alt="Pagina E-Doc dell'ambiente Sandbox in inglese con il formato EDI espanso e la riga STRUCTURE DESCRIPTOR JSON elencata sopra TRANSFORMATION, PREVIEW ed EXTRACTION PATHS"><figcaption>Aprire E-Doc per il proprio tipo di documento; il formato EDI elenca i relativi file di configurazione.</figcaption></figure>

2. Espandere il formato **EDI**. I suoi file di configurazione sono elencati insieme: **STRUCTURE DESCRIPTOR**, **TRANSFORMATION**, **PREVIEW** ed **EXTRACTION PATHS**.
3. Fare clic sulla riga **STRUCTURE DESCRIPTOR**, contrassegnata come **JSON**, per aprirla.

#### **Gestione delle bozze**

La colonna di sinistra mostra l'elenco delle **Version** del file. La versione contrassegnata come **Active** è quella utilizzata da DocBits.

* **Creare una bozza**: fare clic sull'icona a forma di matita ✏️ accanto alla versione attiva per iniziare la modifica. Il file attivo non può essere modificato direttamente.
* **Eliminare le bozze**: utilizzare l'icona del cestino 🗑️ per rimuovere le bozze non utilizzate.
* **Attivare le modifiche**: fare clic sull'icona a forma di segno di spunta ✅ su una bozza per approvare e pubblicare le modifiche.
  * <mark style="color:red;">**Note**</mark>: l'attivazione di una nuova versione **disattiva automaticamente** quella precedente.

<!-- dbdc-139-edi-sd-detail-en.png --><figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/dbdc-139-edi-sd-detail-en.png" alt="Editor JSON dello Structure Descriptor nell'ambiente Sandbox in inglese, con l'elenco delle versioni a sinistra che mostra la versione 1 contrassegnata come Active e un'icona a forma di matita per creare una bozza"><figcaption>Il file Structure Descriptor con l'elenco delle versioni; la matita crea una bozza modificabile.</figcaption></figure>

## 3. Preview Function (Preview Parsed Output)

La **Preview Function** consente di verificare come viene analizzato un file EDI caricato con lo Structure Descriptor attualmente visualizzato, prima di attivare qualsiasi modifica.

#### Utilizzo

* Caricare un file EDI tramite il normale processo di caricamento.
* Copiare il **Document ID** del file caricato.
* Aprire il file **Structure Descriptor** come descritto sopra.
* Fare clic su **Preview** in alto a destra per aprire il pannello di test.

    <div align="left"><!-- dbdc-139-edi-sd-preview-en.png --><figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/dbdc-139-edi-sd-preview-en.png" alt="Pagina Structure Descriptor dell'ambiente Sandbox in inglese con il pannello di test Preview aperto, che mostra il campo di input Document Id e il pulsante Test" width="560"><figcaption>Il pannello di test: inserire un Document ID e premere Test.</figcaption></figure></div>

* Inserire il **Document ID** nel campo e premere **Test**.
* L'**output strutturato** risultante viene visualizzato accanto all'editor.

Questa funzione è particolarmente utile per il debug dei mapping e per la validazione in tempo reale dei raggruppamenti strutturali. È necessario disporre di un documento EDI rappresentativo del proprio formato; il risultato mostrato dipende dal file caricato.

## 4. Video Walkthrough

Una guida video per questo tipo di file è disponibile nella [pagina Videos.](../edi-videos.md)\
Utilizzarla per seguire la configurazione, la modifica e l'anteprima.

Le schermate mostrano una configurazione e una versione esistenti. Le impostazioni variano in base al tipo di documento e al formato. Validare le modifiche in una bozza prima dell'attivazione.
