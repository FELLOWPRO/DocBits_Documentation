# Estrazione dei codici a barre

## Panoramica

Questa funzionalità consente il rilevamento automatico dei codici a barre nei documenti. Quando è attiva, durante l'elaborazione vengono scansionati ed estratti tutti i tipi di codice a barre supportati.

## Come attivare l'estrazione dei codici a barre

Per attivare la funzionalità Bar-Code Extraction, procedi come segue:

1. **Vai su Settings**:
   * Dal Dashboard, vai su **Settings**.
   * Seleziona **Document Processing** e poi **Module**.
2. **Attiva la funzionalità**:
   * Scorri verso il basso fino all'opzione **Bar-Code Extraction**.
   * Sposta il cursore per attivare Bar-Code Extraction.\\

## **Impostazioni aggiuntive**

### **Assegnazione dei codici a barre**

#### **Scopo:** consente ai validatori di assegnare manualmente il valore di un codice a barre estratto a un campo specifico del documento durante la validazione dei campi.

#### Come attivare **Barcode Assignment**

Per attivare la funzionalità **Barcode Assignment**, procedi come segue:

1. **Vai su Settings**:
   * Dal Dashboard, vai su **Settings**.
   * Seleziona **Document Processing** e poi **Module**.
2. **Attiva la funzionalità**:
   * Scorri verso il basso fino all'opzione **Barcode Assignment**.
   * Sposta il cursore per attivare **Barcode Assignment**.\\

#### **Come funziona:**

* Abilita l'opzione "Assign Barcode" nella schermata di validazione dei campi.\\
* Gli utenti possono selezionare un valore di codice a barre rilevato e associarlo a un campo del documento, come PO Number o Invoice Number.\\

### Suddivisione del documento tramite codice a barre / QR code

**Scopo:** suddivide automaticamente i documenti multipagina in documenti separati in base alla presenza di specifici codici a barre o QR code.

#### Come attivare la suddivisione del documento tramite codice a barre / QR code

Per attivare la funzionalità di **suddivisione del documento tramite codice a barre / QR code**, procedi come segue:

1. **Vai su Settings**:
   * Dal Dashboard, vai su **Settings**.
   * Seleziona **Elaborazione documenti** e poi **Classificazione ed estrazione**.
2. **Attiva la funzionalità**:
   * Individua l'opzione **Document Splitting**.
   * Per **Split**, seleziona **Split by Barcode / QR Code**.
   * Per **Barcode Type**, scegli dall'elenco uno o più tipi di codice a barre supportati.
   * Per **Barcode Pattern**, definisci il pattern che deve attivare la suddivisione. Puoi usare un'**espressione regolare** (regex) per riconoscere valori di codici a barre dinamici.

**Come funziona:**

* Selezioni i tipi di codice a barre che devono attivare una suddivisione.
* Definisci un pattern che il codice a barre deve soddisfare: può essere una stringa fissa o una regex (ad es. `^INV\d{6}$` per riconoscere codici a barre come `INV123456`).
* Durante l'elaborazione del documento, ogni volta che una pagina contiene un codice a barre corrispondente, viene **creato un nuovo documento** a partire da quella pagina.

### Tipi di codice supportati

Consulta la [pagina di panoramica](./) per l'elenco completo dei formati di codici a barre e QR code supportati.
