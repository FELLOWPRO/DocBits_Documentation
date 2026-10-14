# Rilevamento dei duplicati

## Panoramica

In **DocBits**, puoi filtrare i documenti duplicati specificando quali campi devono corrispondere e definendo un intervallo di tempo durante il quale i duplicati devono essere rilevati.

Questa pagina fornisce una guida dettagliata su come abilitare e utilizzare efficacemente la funzionalità di **Rilevamento dei duplicati**.

## Abilitare il Rilevamento dei duplicati

Per abilitare il rilevamento di documenti doppi in **DocBits**, segui questi passaggi:

1.  Naviga su **Impostazioni** → **Impostazioni globali** → **Tipi di documenti**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/Calculate_PO_unit_price_1.png)
2.  Seleziona il **Tipo di documento** desiderato e fai clic su **Altre impostazioni**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/Calculate_PO_unit_price_2.png)
3.  Vai alla sezione **Rilevamento dei duplicati**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/DuplicateDocument_3.png)

DocBits fornisce due opzioni per identificare documenti duplicati:

1. **Rilevamento di documenti doppi**:\
   Questa funzionalità controlla i documenti duplicati caricati su **DocBits** in base ai criteri selezionati. Se un documento corrisponde ai criteri selezionati in altri documenti, verrà contrassegnato come duplicato.
2.  **Rilevamento di fatture doppie** (Disponibile solo per il tipo di documento **Fattura**):\
    Questa funzionalità richiede la sincronizzazione delle fatture dei fornitori da Infor a DocBits. Confronta i numeri di fattura nel cruscotto di DocBits con quelli in Infor. Se lo stesso numero di fattura appare più di una volta, verrà contrassegnato come duplicato.

    <mark style="color:red;">**Nota**</mark>: L'utilizzo della funzionalità di **Rilevamento di fatture doppie** comporterà un addebito di credito aggiuntivo.

## Filtrare quali documenti devono essere rilevati come duplicati

Una volta abilitato il **Rilevamento dei duplicati**, saranno disponibili due menu a discesa per la configurazione:

*   **Campi di rilevamento dei duplicati**\
    Seleziona i campi che devono essere utilizzati per identificare i duplicati (ad es., Id del fornitore, Data, Numero di fattura, ecc.). I documenti che corrispondono a questi campi verranno contrassegnati come duplicati.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/DuplicateDocument_4.png)
*   **Intervallo di rilevamento duplicati**

    Utilizza questa impostazione per definire l'intervallo di tempo entro il quale vengono rilevati i duplicati. I documenti caricati all'interno dell'intervallo selezionato verranno confrontati tra loro in base ai campi selezionati.

    **Opzioni disponibili:**

    * 1 mese
    * 3 mesi (Consigliato)
    * 6 mesi
    * 1 anno

    <mark style="color:red;">**Nota**</mark>: Si consiglia un intervallo di 3 mesi per garantire prestazioni ottimali. Selezionare un intervallo più lungo potrebbe portare a tempi di caricamento più lenti del cruscotto.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/DuplicateDocument_6.png)

## Visualizzare documenti duplicati nel Cruscotto

Una volta abilitato il **Rilevamento dei duplicati**, qualsiasi documento identificato come duplicato mostrerà un'icona indicativa di duplicato nel cruscotto.

*   Fai clic su questa icona per aprire i record corrispondenti in una vista affiancata per un facile confronto.\
    <mark style="color:red;">**Nota**</mark>: L'icona apparirà solo se è stato rilevato almeno un duplicato per il documento.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/DuplicateDocument_7.png)
*   Quando visualizzi un documento contrassegnato, apparirà una barra di avviso nella parte superiore, indicando che il documento è un duplicato.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/DuplicateDocument_5.png)
