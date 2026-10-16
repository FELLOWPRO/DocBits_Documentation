# Modifica e salvataggio dei pattern regex

## Guida alla modifica dei pattern esistenti e all'importanza di testare tali modifiche per garantire che funzionino come previsto senza compromettere le funzionalità esistenti.

**Per modificare i pattern regex esistenti e assicurarti che le modifiche funzionino come previsto senza compromettere le funzionalità esistenti, puoi seguire la guida qui sotto:**

<figure><img src="../../../../../.gitbook/assets/Bildschirmfoto 2024-05-22 um 12.46.56.png" alt=""><figcaption><p>Impostazioni: Tipo di documento</p></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/Bildschirmfoto 2024-05-22 um 14.18.25.png" alt=""><figcaption></figcaption></figure>

**Analizza il pattern esistente:**

* Esamina il pattern regex esistente per capire quali dati acquisisce e come funziona.
* Individua le parti del pattern da modificare e l'impatto di tali modifiche sui dati acquisiti.

**Ad esempio: deve essere letto l'importo della fattura:**

*   (?<=Rechnungsbetrag:)\[\s]\*((((\d+)\[,.]{1,10})+\d{0,2})|(\d+(?!,)))

    Rechnungsbetrag: 100.00
*   Leggere l'importo con il punto come separatore delle migliaia, ma NON far passare il punto

    \[\d.]_\[,\d]_

    Caratteri consentiti: 0123456789,
*   Deve essere letto il valore "P32180". La parola di ancoraggio qui è "Invoice Date".

    (?<=InvoiceDate )\[\s]\*P\d{5}

    Customer number Invoice number Invoice date P32180 613976 05/13/2019

<figure><img src="../../../../../.gitbook/assets/image (108).png" alt=""><figcaption></figcaption></figure>

**Documenta le modifiche:**

* Annota le modifiche che intendi apportare al pattern regex.
* Annota quali nuovi pattern intendi aggiungere e quali parti del pattern esistente potrebbero dover essere modificate o rimosse.

**Prepara i dati di prova:**

* Raccogli dati di prova rappresentativi dei diversi tipi di dati che il pattern regex acquisisce di solito.
* Assicurati che i dati di prova coprano sia i casi tipici sia i casi limite, per verificare la robustezza delle modifiche.

**Apporta le modifiche al pattern regex:**

* Apporta le modifiche pianificate al pattern regex.
* Può trattarsi di aggiungere nuovi pattern, rimuovere o adattare parti esistenti oppure ottimizzare il pattern per prestazioni migliori.

**Testa le modifiche:**

* Applica il pattern regex aggiornato ai tuoi dati di prova ed esamina attentamente i risultati.
* Verifica che il pattern acquisisca ancora correttamente i dati desiderati e che non ci siano effetti inattesi su altre parti dei dati o del sistema.

**Debug e adattamento:**

* Se i risultati dei test non sono quelli previsti o si verificano problemi inattesi, rivedi attentamente le modifiche e apporta ulteriori adattamenti, se necessario.
* Può essere necessario annullare alcune modifiche o aggiungere ulteriori adattamenti per risolvere il problema.

**Documenta le modifiche:**

* Aggiorna la documentazione del tuo pattern regex per riflettere le modifiche apportate.
* Descrivi i pattern aggiornati e i motivi delle modifiche effettuate, per aiutare gli altri sviluppatori a comprendere e usare il pattern.

**Salvataggio delle modifiche:**

* Quando sei sicuro che le modifiche abbiano avuto successo e funzionino come previsto, salva il pattern regex aggiornato nel tuo codice o nei file di configurazione, in modo che sia disponibile per usi futuri.

<figure><img src="../../../../../.gitbook/assets/image (109).png" alt=""><figcaption><p>Salva le modifiche</p></figcaption></figure>

Seguendo questi passaggi e testando con attenzione le modifiche ai pattern regex, puoi assicurarti che il tuo pattern regex continui a funzionare correttamente e soddisfi allo stesso tempo i nuovi requisiti.
