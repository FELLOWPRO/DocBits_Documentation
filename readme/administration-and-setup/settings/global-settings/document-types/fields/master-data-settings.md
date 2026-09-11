# Impostazioni dei dati master

## Panoramica

Nella sezione **Impostazioni dei dati master** delle **Campi** per un specifico Tipo di documento, puoi visualizzare e configurare le mappature dei dati master ai campi utilizzati nella convalida dei campi, utilizzando i dati dalla [**Ricerca dei dati master**](../../../document-processing/master-data-lookup.md).

Queste mappature definiscono come i dati master vengono applicati ai singoli campi durante la convalida. Questa pagina fornisce una guida dettagliata su come configurare e gestire queste mappature.

## **Accesso alle** Impostazioni dei dati master **Impostazioni**

Per accedere alle **Impostazioni dei dati master** Impostazioni:

1.  Vai a **Impostazioni → Impostazioni globali → Tipi di documenti**

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_document_types.png)
2.  Seleziona il **Tipo di documento** desiderato e clic su **Campi**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_document_types_fields.png)
3.  Clic su **Impostazioni dei dati master**

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_1.png)

## Ricerca di dati anagrafici

Nella sezione **Ricerca di dati anagrafici**, puoi creare configurazioni di ricerca dai tuoi dati master da usare come mappature dei campi durante la convalida dei campi.

### Voci predefinite

Nella sezione **Ricerca di dati anagrafici**, alcune voci predefinite sono fornite da **DocBits**. Queste voci:

* Non possono essere modificate o cancellate
* Possono essere disattivate se non necessarie

Le voci predefinite sono chiaramente contrassegnate con un'etichetta **Default** per una facile identificazione.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_2.png)

### **Creare una configurazione di ricerca**

Per creare una nuova configurazione di ricerca per i dati master:

1. Vai alla sezione **Ricerca di dati anagrafici**.
2.  Clic **Creare una configurazione di ricerca** nell'angolo in alto a destra.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_3.png)
3. Configura le seguenti opzioni:
   * **Cerca nome**\
     Il nome della configurazione di ricerca.
   * **Nome del set di dati di ricerca**\
     Seleziona il set di dati che deve essere utilizzato per questa configurazione di ricerca.
   * **Gestore dei conflitti**\
     Un conflitto significa che la ricerca ha trovato più di un record. Questa impostazione decide cosa succede allora:
     * **Best Score** – Usa la voce che corrisponde al maggior numero di campi. Non lascia mai il campo vuoto e può quindi scegliere il record sbagliato.
     * **Return None** – Lascia il campo vuoto, così un utente sceglie il record giusto.
     * **Return First** – Usa il primo valore trovato.
   *   **Tipo di contesto**

       Specifica dove nel documento verrà applicata la configurazione di ricerca. Scegli tra:

       **HEADER**

       La ricerca è utilizzata nella convalida dei campi. Configura quanto segue:

       * **Abbina tutti**\
         Quando abilitato, un record deve corrispondere a **tutti** i campi usati. Quando disabilitato (predefinito), basta che corrisponda **un** campo, il che restituisce un elenco più lungo.

       ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_4.png)

       \
       **LINE**

       La ricerca viene utilizzata all'interno di una tabella del documento. Configura quanto segue:

       * **Dettaglio del contesto**\
         Seleziona la tabella specifica a cui applicare la ricerca.
       * **Abbina tutti**\
         Quando abilitato, un record deve corrispondere a **tutti** i campi usati. Quando disabilitato (predefinito), basta che corrisponda **un** campo, il che restituisce un elenco più lungo.

       ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_5.png)
{% hint style="info" %}
**Abbina tutti** e il **Gestore dei conflitti** agiscono insieme e decidono se un fornitore viene riconosciuto automaticamente. La pagina di configurazione li spiega con esempi:

{% content-ref url="../../../../setup/document-types/fuzzy-data-configuration-with-master-data.md" %}
[fuzzy-data-configuration-with-master-data](../../../../setup/document-types/fuzzy-data-configuration-with-master-data.md)
{% endcontent-ref %}
{% endhint %}

4.  Clic **Salva** per creare la configurazione di ricerca.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_6.png)

### Azioni sulla configurazione di ricerca esistente

Per gestire una configurazione di ricerca esistente, clic sui tre puntini nell'angolo in alto a destra della configurazione che desideri modificare.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_7.png)

Sono disponibili le seguenti azioni:

* **Attivare / Disattivare**\
  Attiva/Disattiva lo stato della configurazione di ricerca.
  * Le configurazioni attive sono contrassegnate con un tag **Attivo**.
  * Le configurazioni inattive sono contrassegnate con un tag **Inattivo**.
*   **Duplicato**\
    Dopo aver inserito un nome e clic su **Fatto**, viene creata una copia della configurazione di ricerca selezionata.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_8.png)
* **Modifica/Vista**\
  Consente di modificare la configurazione di ricerca selezionata.\
  Dopo aver apportato le modifiche, clic **Salva** per applicarle.\
  <mark style="color:red;">**Nota**</mark>: Le configurazioni di ricerca predefinite possono solo essere visualizzate, non modificate. L'opzione **Modifica** verrà sostituita da **Vista**.
*   **Cancellare**\
    Elimina definitivamente la configurazione di ricerca selezionata dopo la conferma.\
    <mark style="color:red;">**Nota**</mark>: Possono essere cancellate solo le configurazioni senza il tag **Default**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_9.png)

### Creare un nuovo campo

Per aggiungere un nuovo campo alla tua configurazione di ricerca:

1. Apri la configurazione di ricerca desiderata.
2.  Clic **Creare** nell'angolo in alto a destra.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_10.png)
3. Configura le opzioni necessarie.
   * **Campo di ricerca**\
     Il campo che verrà cercato all'interno del set di dati di ricerca selezionato.
   * **Campo di convalida**\
     Il campo che verrà visualizzato durante la convalida dei campi.
   * **Campo genitore** (opzionale)\
     Questo campo viene utilizzato per convalidare la correttezza del valore nel **Campo di convalida** assicurando che corrisponda alla voce genitore corrispondente nel set di dati di ricerca.
   * **Operatore di ricerca** (opzionale)\
     Scegli come **DocBits** cerca le corrispondenze nel set di dati di ricerca:
     * **Smart** – _(Default)_ Ignora spazi e punteggiatura e cerca il termine in **qualsiasi punto** del campo. Per questo "Meier" trova anche "Meier Bau GmbH".
     * **Contiene** – Cerca voci che contengono il termine esatto in qualsiasi punto del campo.
     * **Finisce con** – Cerca voci che terminano con il termine specificato.
     * **esatto** – Cerca una corrispondenza esatta dell'intero valore.
     * **Inizia con** – Cerca voci che iniziano con il termine specificato.
   * **Trigger automatico** (opzionale)\
     Quando abilitato, DocBits compilerà automaticamente tutti i campi nella configurazione di ricerca non appena questo campo viene compilato.
   *   **Ricercabile** (opzionale)\
       Quando abilitato, gli utenti possono cercare manualmente i dati master durante la convalida dei campi **e** il campo partecipa alla ricerca automatica. Lascialo non selezionato se il campo non deve influenzare il risultato automatico.

       ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_12.png)



       ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_13.png)
4.  Clic **Salva** per creare il nuovo campo.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_11.png)

### Azioni sul campo esistente

Per gestire un campo esistente, clic sui tre puntini nella colonna **Azioni** accanto al campo che desideri modificare.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_14.png)

Sono disponibili le seguenti azioni:

* **Modifica/Vista**\
  Consente di modificare il campo selezionato.\
  Dopo aver apportato le modifiche, clic **Salva** per applicarle.\
  <mark style="color:red;">**Nota**</mark>: I campi predefiniti possono solo essere visualizzati, non modificati. In questi casi, l'opzione **Modifica** apparirà come **Vista**.
*   **Cancellare**\
    Elimina definitivamente il campo selezionato dopo la conferma.\
    <mark style="color:red;">**Nota**</mark>: Possono essere cancellati solo i campi senza il tag **Default**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_9.png)

## Dati anagrafici LOV

La sezione **Dati anagrafici LOV** consente di creare configurazioni di dropdown utilizzando valori dai tuoi dati master. Questi dropdown possono essere autonomi o dipendenti da altri dropdown, abilitando filtri dinamici e selezioni a cascata durante la convalida dei campi.

### Creare la configurazione della ricerca Lov

Una configurazione di ricerca lov definisce come le opzioni del dropdown sono ottenute da una tabella di dati master e come quei valori vengono mostrati e inseriti nei campi del documento.

**Per creare una nuova configurazione di ricerca LOV:**

1. Vai alla sezione **Dati anagrafici LOV**.
2.  Clic **Creare la configurazione della ricerca Lov** nell'angolo in alto a destra.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_15.png)
3. Configura le seguenti opzioni:
   * **Cerca il nome Lov**\
     Il nome della configurazione di ricerca lov.
   * **Nome del set di dati di ricerca Lov**\
     Seleziona la tabella di dati master che deve essere utilizzata per questa configurazione di ricerca lov.
   *   **Tipo di contesto**\
       Specifica dove nel documento verrà applicata la configurazione di ricerca lov:

       **HEADER**

       La configurazione di ricerca lov è utilizzata nella convalida dei campi. Configura quanto segue:

       * **Campo etichetta di ricerca**\
         Seleziona la colonna il cui valore verrà visualizzato nel dropdown.
       * **Campo valore di ricerca**\
         Seleziona la colonna il cui valore verrà memorizzato internamente e utilizzato per il filtraggio quando viene effettuata una selezione. Questo valore non è mostrato all'utente.
       * **Fuori campo**\
         Definisce il campo nella convalida dei campi che riceverà l'etichetta selezionata dal dropdown.

       ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_16.png)

       \
       **LINE**

       La configurazione di ricerca lov è utilizzata all'interno di una tabella del documento. Configura quanto segue:

       * **Dettaglio del contesto**\
         Seleziona la tabella specifica in cui questa configurazione di ricerca lov deve essere attiva.
       * **Campo etichetta di ricerca**\
         La colonna il cui valore verrà visualizzato nel dropdown.
       * **Campo valore di ricerca**\
         Seleziona la colonna il cui valore verrà memorizzato internamente e utilizzato per il filtraggio quando viene effettuata una selezione. Questo valore non è mostrato all'utente.
       * **Fuori campo**\
         Specifica il campo di destinazione nella tabella in cui verrà inserita l'etichetta selezionata.

       ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_17.png)
4.  Clic **Salva** per creare la configurazione di ricerca lov.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_18.png)

### Azioni sulla configurazione di ricerca esistente

Per gestire una configurazione di ricerca lov esistente, clic sui tre puntini nell'angolo in alto a destra della configurazione.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_19.png)

**Azioni disponibili:**

* **Attivare / Disattivare**\
  Attiva/Disattiva lo stato della configurazione di ricerca lov.
  * Le configurazioni **Attivo** sono contrassegnate con un tag **Attivo**.
  * Le configurazioni **Inattivo** sono contrassegnate con un tag **Inattivo**.
*   **Duplicato**\
    Dopo aver inserito un nome e clic su **Fatto**, viene creata una copia della configurazione di ricerca lov selezionata.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_21.png)
* **Modifica / Vista**\
  Modifica la configurazione selezionata. Dopo le modifiche, clic **Salva**.
*   **Cancellare**\
    Elimina definitivamente la configurazione dopo la conferma.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_20.png)

### Creare un nuovo campo

All'interno di ciascuna configurazione di ricerca lov, puoi definire campi aggiuntivi come dropdown che fungono da pre-filtri per la logica lov principale.

Questi campi vengono valutati prima che il dropdown lov principale venga caricato. In base ai valori selezionati in questi campi, i risultati del campo lov principale vengono filtrati dinamicamente—abilitando dropdown dipendenti.\
Ad esempio, selezionare un paese in un campo di pre-filtro può restringere le opzioni della città nel dropdown lov principale.

Oltre a creare nuovi campi, puoi anche utilizzare campi esistenti come pre-filtri. Quando configurati in questo modo, il valore selezionato nel campo esistente filtrerà automaticamente il dropdown lov principale.

**Per aggiungere un nuovo campo:**

1. Apri la configurazione di ricerca lov desiderata.
2.  Clic **Creare** nell'angolo in alto a destra.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_22.png)
3.  Configura le opzioni necessarie.

    **Opzioni di configurazione del campo (si applicano ai contesti HEADER e LINE):**

    * **Campo di ricerca**\
      La colonna da cercare nel set di dati selezionato per i valori del dropdown.
      * **Campo filtro**\
        Specifica il campo il cui valore viene utilizzato per pre-filtrare i risultati della configurazione di ricerca lov prima che il dropdown principale venga popolato.
      * **Valore del filtro** (opzionale)\
        Aggiungi filtri statici per restringere ulteriormente i risultati della ricerca.
      * **Necessario**\
        Quando abilitato, questo campo deve essere compilato prima che qualsiasi dropdown dipendente possa essere popolato.
4.  Clic **Salva** per creare il nuovo campo.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_23.png)

### Azioni sul campo esistente

Per gestire un campo esistente all'interno di una configurazione di ricerca lov, clic sui tre puntini nella colonna **Azioni** accanto al campo.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_24.png)

**Azioni disponibili:**

* **Modifica**\
  Modifica il campo selezionato. Dopo le modifiche, clic **Salva** per applicare.
*   **Cancellare**\
    Rimuove definitivamente il campo dopo la conferma.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_20.png)
