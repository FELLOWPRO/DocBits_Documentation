# Addestramento dei campi di riga e delle tabelle

## Addestramento delle tabelle: quando e come usarlo

DocBits utilizza per impostazione predefinita l'estrazione di tabelle basata su AI, che funziona con tutti i fornitori. Tuttavia, quando hai bisogno di un maggiore controllo sul modo in cui vengono estratte le voci per un fornitore specifico, puoi utilizzare **addestramento delle tabelle** per definire manualmente la struttura.

#### &#x20;**Importante: addestramento specifico del fornitore**

L’addestramento delle tabelle è **specifica per ciascun fornitore**. Se addestri un layout di tabella per un fornitore, le regole si applicano solo ai documenti di quel fornitore.\
Altri fornitori continueranno a utilizzare l'estrazione di tabelle basata su AI a meno che non vengano formati separatamente.

#### Quando usare l’addestramento delle tabelle?

Utilizza addestramento delle tabelle **solo quando il layout del documento è stabile** e desideri garantire un'estrazione coerente e di alta qualità. È più adatto per i fornitori che:

* Utilizza un formato di fattura fisso  nel tempo.
* Richiedi la **mappatura precisa** delle voci su campi specifici.
* Sono **fornitori ad alto volume**, dove l'automazione coerente è preziosa.

#### Quando non usare l’addestramento delle tabelle

Evita di utilizzare addestramento delle tabelle se:

* Il fornitore **modifica frequentemente il layout della fattura** (ad esempio, ogni due mesi).
* Non ricevi regolarmente documenti da quel fornitore.
* L'estrazione predefinita AI funziona **abbastanza bene** senza addestramento manuale.

In questi casi, riqualificare ripetutamente la tabella sarebbe inefficiente e dispendioso in termini di tempo.



## Come usarlo:

**Training Mode** viene utilizzato per insegnare a DocBits come estrarre correttamente le voci dal layout del documento di un fornitore specifico.

Quando sei in modalità Training, definisci:

* **Dove si trova la tabella** sul documento.
* **Quali aree corrispondono a ciascuna colonna** (ad esempio, Quantità, Descrizione, Prezzo unitario).

Questa modalità crea un **modello di estrazione riutilizzabile** per quel fornitore, quindi i documenti futuri con lo stesso layout verranno elaborati automaticamente, senza dover ripetere l’addestramento.

**Key Characteristics:**

* **Le colonne mappate sono di sola lettura** — non puoi modificare manualmente il testo.
* Non puoi **aggiungere o eliminare righe**.
* Il focus è sulla **mappatura delle posizioni**, non sulla correzione dei valori.
* Una volta terminata la mappatura della tabella e delle sue colonne, fai clic su **“Save Rules”** così DocBits apprende e applica questo addestramento a documenti simili dello stesso fornitore.



**Modalità correzione** ti consente di **correggere gli errori di estrazione** nei dati della tabella per il documento corrente. Si usa quando DocBits ha già tentato di estrarre la tabella, ma i risultati necessitano di piccole correzioni.

Utilizzare la modalità di correzione quando:

* Alcuni valori **mancano o sono disallineati**.
* È stata estratta una **riga vuota o duplicata** che deve essere rimossa.

**Cosa puoi fare in modalità correzione:**

* **Regola manualmente i valori** nelle colonne mappate (ad esempio, correggi gli errori di posizionamento).
* **Elimina le righe** che non dovrebbero far parte della tabella.
* **Aggiungi righe** che sono state completamente perse durante l'estrazione.
