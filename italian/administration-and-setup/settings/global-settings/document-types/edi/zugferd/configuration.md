# Configurazione ZUGFeRD

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

#### Attivazione e modifica standard

Lo standard ZUGFeRD è sempre attivo per impostazione predefinita, ma è possibile apportare modifiche se necessario.

### **Passaggi per modificare le impostazioni ZUGFeRD:**

1. Navigare in **Impostazioni → Impostazioni globali → Tipi di documento → Fattura**.
2. Fare clic su **E-Doc**.
3. Apparirà un elenco di tutti gli e-doc disponibili.
4. Individuare la versione **ZUGFeRD** che si desidera modificare.

## **Configurazione della trasformazione e del percorso XML:**

Nelle **impostazioni di trasformazione**, è possibile definire il percorso per individuare informazioni specifiche all'interno del file XML e salvarle in una nuova struttura, semplificando l'accesso ai dati. <mark style="color:red;">**Nota**</mark>: Se si utilizza questa funzionalità, è necessario utilizzare i nuovi percorsi XML creati, non quelli originali, nell'**Anteprima** e nel **Percorso di estrazione**.

### **Passaggi per modificare il file di trasformazione:**

1. Aprire la **Trasformazione**.
2. Creare una nuova bozza facendo clic sull'**icona della matita**.
3. Selezionare la bozza appena creata.
4. Creare un nuovo campo o modificarne uno esistente.
5. Impostare il percorso desiderato per l'estrazione dei dati.
6. Fare clic su **Salva**.

### Note importanti:

* Il **file di anteprima** viene utilizzato solo per **FACTUR-X** e non per **ZUGFeRD**. ZUGFeRD utilizzerà il **PDF** originale.

## Configurazione anteprima PDF

La **Configurazione anteprima PDF** viene utilizzata per generare una versione del documento leggibile dall'utente. È possibile personalizzarla con l'HTML in base alle proprie esigenze.

### **Passaggi per modificare il file di anteprima:**

1. Aprire l'**Anteprima**.
2. Creare una nuova bozza facendo clic sull'**icona della matita**.
3. Selezionare la bozza appena creata.
4. Creare un nuovo campo o modificarne uno esistente.
5. Impostare il percorso desiderato per l'estrazione dei dati.
6. Fare clic su **Salva**.

## Configurazione dei percorsi di estrazione

La **Configurazione dei percorsi di estrazione** viene utilizzata per estrarre i dati e popolare i campi nella **schermata di convalida**, come la tabella delle fatture o i campi configurati nel layout della fattura.

### **Passaggi per modificare i** **percorsi di estrazione**:

1. Aprire i **Percorsi di estrazione**.
2. Creare una nuova bozza facendo clic sull'**icona della matita**.
3. Selezionare la bozza appena creata.
4. Creare un nuovo campo o modificarne uno esistente.
5. Il lato sinistro rappresenta l'**ID del campo DocBits**, che si trova in **Impostazioni → Impostazioni globali → Tipi di documento → Fattura → Campi**.
6. Il lato destro rappresenta il **percorso del campo** creato nella Trasformazione.
7. Fare clic su **Salva**.

Seguendo questi passaggi, è possibile garantire un'estrazione e una convalida accurate dei dati per le fatture ZUGFeRD.
