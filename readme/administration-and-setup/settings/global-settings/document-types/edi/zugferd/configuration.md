# Configurazione di ZUGFeRD

{% embed url="https://youtu.be/AxrHNEmmXtg" %}
Tutorial DocBits E-Invoice: elaborare XRechnung / ZUGFeRD (Factur-X), convalidare i dati e automatizzare i flussi di lavoro
{% endembed %}

## **Versioni supportate di ZUGFeRD**

DocBits supporta tutte le principali versioni di ZUGFeRD, tra cui:

* **1.0**
* **2.0**
* **2.1** (conforme a FACTUR-X 1.0.05)
* **2.2**
* **2.3** (conforme a FACTUR-X 1.07.2)
* **2.3.2**

#### Attivazione e modifica dello standard

Lo standard ZUGFeRD è sempre attivo per impostazione predefinita, ma se necessario è possibile modificarlo.

### **Passaggi per modificare le impostazioni di ZUGFeRD:**

1. Vai su **Impostazioni → Impostazioni globali → Tipi di documento → Fattura**.
2. Fai clic su **E-Doc**.\\
3. Viene visualizzato l'elenco di tutti gli e-doc disponibili.
4. Individua la versione di **ZUGFeRD** che vuoi modificare.\\

## **Configurazione della trasformazione e dei percorsi XML:**

Nelle **impostazioni di trasformazione** puoi definire il percorso per individuare informazioni specifiche all'interno del file XML e salvarle in una nuova struttura, così da accedere ai dati più facilmente.\
<mark style="color:red;">**Nota**</mark>: se utilizzi questa funzione, nell'**Anteprima** e nel **Percorso di estrazione** devi usare i nuovi percorsi XML creati, non quelli XML originali.

### **Passaggi per modificare il file di trasformazione:**

1. Apri la **Trasformazione**.
2. Crea una nuova bozza facendo clic sull'**icona della matita**.
3. Seleziona la bozza appena creata.
4. Crea un nuovo campo oppure modifica uno esistente.
5. Imposta il percorso desiderato per l'estrazione dei dati.
6. Fai clic su **Salva**.

### Note importanti:

* Il **file di anteprima** viene utilizzato solo per **FACTUR-X** e non per **ZUGFeRD**. ZUGFeRD utilizza il **PDF** originale.

## Configurazione del PDF di anteprima

La **configurazione del PDF di anteprima** serve a generare una versione del documento leggibile dall'utente. Puoi personalizzarla con HTML in base alle tue esigenze.

### **Passaggi per modificare il file di anteprima:**

1. Apri l'**Anteprima**.
2. Crea una nuova bozza facendo clic sull'**icona della matita**.
3. Seleziona la bozza appena creata.
4. Crea un nuovo campo oppure modifica uno esistente.
5. Imposta il percorso desiderato per l'estrazione dei dati.
6. Fai clic su **Salva**.

## Configurazione dei percorsi di estrazione

La **configurazione dei percorsi di estrazione** serve a estrarre i dati e a popolare i campi nella **schermata di convalida**, come la tabella della fattura o i campi configurati nel layout della fattura.

### **Passaggi per modificare i** **percorsi di estrazione**:

1. Apri i **Percorsi di estrazione**.
2. Crea una nuova bozza facendo clic sull'**icona della matita**.
3. Seleziona la bozza appena creata.
4. Crea un nuovo campo oppure modifica uno esistente.
5. Il lato sinistro rappresenta l'**ID del campo DocBits**, che si trova in **Impostazioni → Impostazioni globali → Tipi di documento → Fattura → Campi**.\\
6. Il lato destro rappresenta il **percorso del campo** creato nella Trasformazione.
7. Fai clic su **Salva**.

Seguendo questi passaggi puoi garantire un'estrazione e una convalida accurate dei dati per le fatture ZUGFeRD.

## Regole effettivamente utilizzate e attivazione

Le regole specifiche dell’organizzazione hanno la precedenza su quelle predefinite per il formato eDoc rilevato. Verificate la TRANSFORMATION attiva e verificate quale nodo fornisce invoice_type nell’XML trasformato; il percorso dipende dal formato. Save salva una bozza; usate il segno di spunta per attivarla dopo i test. Il rendering di Preview non dimostra il tipo di documento memorizzato. Consultate la [guida alla diagnosi della classificazione](../credit-note-recognized-as-invoice.md) per i codici 381/261, gli script successivi e le precauzioni prima della rielaborazione.
