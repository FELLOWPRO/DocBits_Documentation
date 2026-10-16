# Creazione e modifica degli script

{% embed url="https://youtu.be/n8NpWWIjmlA" %}
DocBits Document Scripts Explained: Automate Custom Logic in Your Document Workflow
{% endembed %}


## Per creare un nuovo script in DocBits, segui queste istruzioni dettagliate:

**Scegli il linguaggio di scripting:**

Per prima cosa, devi scegliere il linguaggio di scripting che vuoi utilizzare. DocBits supporta in genere i linguaggi di scripting più comuni come Python, JavaScript o SQL. La scelta del linguaggio dipende dalle esigenze del tuo progetto e dalle tue competenze.

**Apri l'ambiente di sviluppo degli script:**

Accedi a DocBits e vai all'ambiente di sviluppo degli script. Si trova nell'area di amministrazione.

<figure><img src="../../../../../.gitbook/assets/Bildschirmfoto 2024-05-23 um 15.19.50.png" alt=""><figcaption></figcaption></figure>

**Crea un nuovo script:**

Fai clic sul pulsante "+ Nuovo" per aprire un nuovo editor di script.

<figure><img src="../../../../../.gitbook/assets/Bildschirmfoto 2024-05-23 um 15.21.58.png" alt=""><figcaption></figcaption></figure>

**Scrivi il codice:**

Usa l'editor per scrivere il codice del tuo script. Inizia con la sintassi di base del linguaggio di scripting scelto.

Ad esempio, se utilizzi Python, il tuo script potrebbe avere il seguente aspetto:

## 1. Esempio di script in Python

<figure><img src="../../../../../.gitbook/assets/image (131).png" alt=""><figcaption></figcaption></figure>

## Funzione per ripulire i nomi dei pazienti

def clean\_patient\_name(name): cleaned\_name = name.strip().title() # Rimuove gli spazi e applica le maiuscole

return cleaned\_name

## Programma principale

if **name** == "**main**": patient\_name = " john doe " cleaned\_name = clean\_patient\_name(patient\_name) print("Cleaned patient name:", cleaned\_name)

## 2. Esempio di script

<figure><img src="../../../../../.gitbook/assets/image (132).png" alt=""><figcaption></figcaption></figure>

**Testa lo script:**

Controlla il codice per individuare eventuali errori e testalo in un ambiente di prova. Assicurati che lo script produca i risultati attesi e funzioni correttamente.

<figure><img src="../../../../../.gitbook/assets/image (133).png" alt=""><figcaption></figcaption></figure>

**Salva lo script:**

Salva lo script in DocBits e assegnagli un nome significativo che ne descriva lo scopo.

<figure><img src="../../../../../.gitbook/assets/image (134).png" alt="" width="84"><figcaption></figcaption></figure>

**Associazione dello script ai tipi di documento:**

Un passaggio importante è l'associazione dello script ai tipi di documento appropriati. Questo determina quando e come lo script viene applicato. Di solito è possibile farlo tramite un'interfaccia di configurazione in DocBits, dove puoi assegnare lo script a un tipo di documento specifico e indicare in quali condizioni deve essere applicato.

<figure><img src="../../../../../.gitbook/assets/image (135).png" alt=""><figcaption></figcaption></figure>

**Revisione e pubblicazione:**

Dopo aver creato, testato e associato lo script, controllalo di nuovo per individuare errori e incoerenze. Se è tutto in ordine, puoi pubblicare lo script nell'ambiente di produzione di DocBits.

<figure><img src="../../../../../.gitbook/assets/Bildschirmfoto 2024-05-23 um 15.29.18.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (136).png" alt=""><figcaption></figcaption></figure>

Attraverso questi passaggi, puoi creare, testare e implementare con successo un nuovo script in DocBits per automatizzare i processi e migliorare l'efficienza della documentazione medica.
