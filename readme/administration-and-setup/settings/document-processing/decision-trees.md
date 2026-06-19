# Alberi decisionali

{% embed url="https://youtu.be/omFWSkSjlL0" %}
Come creare un albero decisionale in DocBits (condizioni, criteri, test ed esportazione)
{% endembed %}

## Panoramica

Gli alberi decisionali sono una funzionalità potente che consente di automatizzare l'instradamento e il processo decisionale in base a regole predefinite. Questa funzionalità è particolarmente utile in ambienti complessi in cui è necessario valutare diverse condizioni per determinare il corretto corso d'azione, come l'assegnazione dei prezzi, la determinazione delle quantità o l'instradamento dei documenti.

#### Componenti chiave

* **Elenco degli alberi decisionali**: è l'interfaccia principale in cui sono elencati tutti gli alberi decisionali esistenti. Ogni albero decisionale può essere associato a un tipo di documento specifico, come `INVOICE` o `QUOTE`.
* **Designer dell'albero decisionale**: questa interfaccia consente di creare e modificare gli alberi decisionali, dove è possibile definire regole, operatori e azioni da intraprendere quando determinate condizioni sono soddisfatte.

## Interfaccia dell'albero decisionale

#### Elenco degli alberi decisionali

L'elenco degli alberi decisionali mostra tutti gli alberi decisionali configurati. Aprilo da **Settings → Document Processing → Decision Trees**.

<figure><img src="../../../.gitbook/assets/decision_trees.png" alt="Elenco degli alberi decisionali"><figcaption><p>L'elenco degli alberi decisionali</p></figcaption></figure>

Ogni voce mostra:

| Colonna | Descrizione |
|--------|-------------|
| **Name** | Il nome dell'albero decisionale. Fai clic su di esso per aprire il Designer. |
| **Document Type** | Il tipo di documento a cui si applica l'albero (ad es. `INVOICE`, `QUOTE`). |
| **Last Modified By** | L'utente che ha modificato per ultimo l'albero. |
| **Last Modified At** | Timestamp dell'ultima modifica. |
| **Actions** | Menu a tre puntini per modificare, copiare, esportare o eliminare l'albero. |

#### Creazione di un albero decisionale

1. Fai clic su **+ Add Decision Tree** nell'angolo in alto a destra.
2. Inserisci un **Name** e seleziona il **Document Type**.
3. Usa il Designer dell'albero decisionale (di seguito) per definire condizioni, criteri e risultati.

#### Importazione di un albero decisionale

Fai clic su **Import Decision Tree** per caricare un file di albero decisionale esportato in precedenza (formato JSON). Questo è utile per copiare un albero tra organizzazioni o ambienti.

## Designer dell'albero decisionale

Il Designer dell'albero decisionale consente di configurare le regole che governano il modo in cui vengono prese le decisioni.

### **Componenti del Designer dell'albero decisionale**

* **Regole**: ogni regola è composta da condizioni e azioni.
* **Select Source**: questo menu a discesa consente di specificare il campo di origine da valutare.
* **Select Operator**: definisce l'operatore logico (ad es. `<=`, `>=`, `=`, `!=`) da applicare al campo di origine.
* **Result**: definisce l'esito o l'azione da intraprendere quando le condizioni sono soddisfatte.
* **Add New Row**: consente di aggiungere ulteriori regole all'albero decisionale.

### Esempio di configurazione di un albero decisionale

Questo albero decisionale valuta il campo **Total Amount** e lo assegna a gruppi diversi in base a condizioni predefinite. Ogni regola confronta l'importo totale con un valore specifico e, in base a quale condizione è vera, viene restituito il corrispondente **Group**.

<figure><img src="../../../.gitbook/assets/decision_tree_example_total_amount.png" alt="Esempio di albero decisionale Total Amount"><figcaption></figcaption></figure>

Questo albero decisionale valuta due condizioni chiave per determinare quale gruppo deve essere assegnato: **Total Amount** e **Warehouse Status**. L'albero utilizza soglie basate sull'importo totale per definire quale gruppo viene restituito, con l'ulteriore distinzione del fatto che il magazzino sia designato come "Warehouse Main", "Warehouse Sub" o "Not Warehouse Main".

<figure><img src="../../../.gitbook/assets/decision_tree_example_warehouse_status.png" alt="Esempio di albero decisionale Warehouse Status"><figcaption></figcaption></figure>

Ogni regola viene valutata in sequenza.

## Criterio dell'albero decisionale

Il criterio dell'albero decisionale definisce come vengono elaborate più regole all'interno di un albero decisionale. È possibile scegliere tra diversi criteri:

### **1. Criterio Unique (univoco)**

Garantisce che venga soddisfatta una sola regola. Se vengono soddisfatte più regole, l'albero decisionale restituirà false.

**Esempio:**

| Regola | Condizione           | Gruppo restituito |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 5000 | GROUP_5     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 3000 | GROUP_3     |

Se l'importo totale è **1500**, le regole valutate saranno:

* **Regola 1**: Total Amount <= 1000 (non corrisponde)
* **Regola 2**: Total Amount <= 2000 (corrisponde)
* **Regola 3**: Total Amount <= 5000 (corrisponde)
* **Regola 4**: Total Amount <= 4000 (corrisponde)
* **Regola 5**: Total Amount <= 3000 (corrisponde)

Poiché vengono soddisfatte più regole (**Regola 2**, **Regola 3**, **Regola 4**, **Regola 5**), l'albero decisionale restituirà **false** perché il criterio **Unique** garantisce che possa corrispondere una sola regola.

### **2. Criterio First (prima)**

Viene applicata la prima regola corrispondente e nessuna regola successiva viene valutata.

**Esempio:**

| Regola | Condizione           | Gruppo restituito |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 5000 | GROUP_5     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 3000 | GROUP_3     |

Se l'importo totale è **1500**, le regole valutate saranno:

* **Regola 1**: Total Amount <= 1000 (non corrisponde)
* **Regola 2**: Total Amount <= 2000 (corrisponde) → L'albero decisionale interrompe la valutazione delle ulteriori regole e applica **GROUP_2**.

### **3. Criterio Priority (priorità)**

La scelta di questa opzione consente di impostare le priorità per ciascuna regola. Più basso è il numero selezionato, più alta è la priorità (ad es. la priorità 1 ha la priorità più elevata). Le regole vengono valutate in base al loro ordine di priorità. Verrà applicata la regola corrispondente con la priorità più alta.

**Esempio:**

<table><thead><tr><th width="137">Regola</th><th width="110">Priorità</th><th width="268">Condizione</th><th>Gruppo restituito</th></tr></thead><tbody><tr><td>1</td><td>5</td><td>Total Amount &#x3C;= 1000</td><td>GROUP_1</td></tr><tr><td>2</td><td>4</td><td>Total Amount &#x3C;= 2000</td><td>GROUP_2</td></tr><tr><td>3</td><td>3</td><td>Total Amount &#x3C;= 3000</td><td>GROUP_3</td></tr><tr><td>4</td><td>2</td><td>Total Amount &#x3C;= 4000</td><td>GROUP_4</td></tr><tr><td>5</td><td>1</td><td>Total Amount &#x3C;= 5000</td><td>GROUP_5</td></tr></tbody></table>

Se l'importo totale è **1500**, le regole valutate saranno:

* **Regola 1**: Total Amount <= 1000 (non corrisponde)
* **Regola 2**: Total Amount <= 2000 (corrisponde)
* **Regola 3**: Total Amount <= 3000 (corrisponde)
* **Regola 4**: Total Amount <= 4000 (corrisponde)
* **Regola 5**: Total Amount <= 5000 (corrisponde)

Poiché la priorità viene applicata nell'ordine **5, 4, 3, 2, 1**, la regola corrispondente con priorità più alta sarà la **Regola 5** (**GROUP_5**). L'albero decisionale restituirà **GROUP_5** perché la **Regola 5** ha la priorità più alta (priorità 1).

### **4. Criterio Collect (sum) (raccogli somma)**

Questo criterio raccoglie tutte le regole corrispondenti e somma i risultati. Funziona solo per **Return Type Value**.

**Esempio:**

| Regola | Condizione           | Valore restituito |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | 1            |
| 2    | Total Amount <= 2000 | 2            |
| 3    | Total Amount <= 3000 | 3            |
| 4    | Total Amount <= 4000 | 4            |
| 5    | Total Amount <= 5000 | 5            |

Per il valore di input di **Total Amount = 3500**, la valutazione delle regole sarebbe:

* **Regola 1**: Total Amount <= 1000 (non corrisponde)
* **Regola 2**: Total Amount <= 2000 (non corrisponde)
* **Regola 3**: Total Amount <= 3000 (corrisponde, Return Value = 3)
* **Regola 4**: Total Amount <= 4000 (corrisponde, Return Value = 4)
* **Regola 5**: Total Amount <= 5000 (corrisponde, Return Value = 5)

Poiché viene applicato il criterio **Collect (sum)**, sommiamo i **Return Values** delle regole corrispondenti, che sono **3, 4, 5**.

**La somma di questi valori** dà:

* 5 + 4 + 3 = **12**

Pertanto, il risultato restituito dall'albero decisionale sarebbe **12**, ovvero la somma di tutti i valori restituiti corrispondenti.

### **5. Criterio Collect (min/max/count) (raccogli min/max/conteggio)**

Questo criterio raccoglie tutte le regole corrispondenti e seleziona il **minimo**, il **massimo** o **conta** le occorrenze. Funziona solo per **Return Type Value**.

**Esempio:**

| Regola | Condizione           | Valore restituito |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | 1            |
| 2    | Total Amount <= 2000 | 2            |
| 3    | Total Amount <= 3000 | 3            |
| 4    | Total Amount <= 4000 | 4            |
| 5    | Total Amount <= 5000 | 5            |

1. Se è selezionata l'opzione **Collect (min)**, il risultato restituirà il **minimo** dei **Return Values** per le regole corrispondenti.
   * Per il valore di input di **Total Amount = 3500**, la valutazione delle regole sarebbe:
     * **Regola 1**: Total Amount <= 1000 (non corrisponde)
     * **Regola 2**: Total Amount <= 2000 (non corrisponde)
     * **Regola 3**: Total Amount <= 3000 (corrisponde, Return Value = 3)
     * **Regola 4**: Total Amount <= 4000 (corrisponde, Return Value = 4)
     * **Regola 5**: Total Amount <= 5000 (corrisponde, Return Value = 5)
   * Le **regole corrispondenti** sono la Regola 3, la Regola 4 e la Regola 5, con **Return Values** di **3, 4 e 5**.
   * Poiché viene applicato il criterio **Collect (min)**, il risultato sarà il **valore minimo**, ovvero **3**.
   * **Risultato**: **3**
2. Se è selezionata l'opzione **Collect (max)**, il risultato restituirà il **massimo** dei **Return Values** per le regole corrispondenti.
   * Per la stessa valutazione di cui sopra, il risultato sarà:
   * **Risultato**: **5**
3. Se è selezionata l'opzione **Collect (count)**, il risultato conterà il **numero di regole corrispondenti**.
   * Per la stessa valutazione di cui sopra, il risultato sarà:
   * **Risultato**: **3** (poiché hanno corrisposto 3 regole).

### **6. Criterio Rule Order (ordine delle regole)**

Questo criterio applica le regole nell'ordine in cui appaiono nell'albero decisionale e restituisce il risultato della prima regola che corrisponde.

**Esempio:**

| Regola | Condizione           | Gruppo restituito |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 3000 | GROUP_3     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 5000 | GROUP_5     |

Dato che il valore di input è **Total Amount = 3500**, la valutazione delle regole sarebbe:

* **Regola 1**: Total Amount <= 1000 (non corrisponde)
* **Regola 2**: Total Amount <= 2000 (non corrisponde)
* **Regola 3**: Total Amount <= 3000 (corrisponde)
* **Regola 4**: Total Amount <= 4000 (corrisponde)
* **Regola 5**: Total Amount <= 5000 (corrisponde)

Con **Rule Order**, l'albero elaborerà le regole nell'ordine in cui sono elencate. Quindi, le regole corrispondenti saranno:

* **Regola 3**: GROUP_3
* **Regola 4**: GROUP_4
* **Regola 5**: GROUP_5

**Risultato**: **GROUP_3**, **GROUP_4**, **GROUP_5**

### **7. Criterio Any (qualsiasi)**

Più regole possono essere vere, ma il risultato di tali regole deve essere lo stesso.

**Esempio:**

| Regola | Condizione           | Gruppo restituito |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 3000 | GROUP_3     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 5000 | GROUP_5     |

Se l'importo totale è **2500**, le regole valutate saranno:

* **Regola 1**: Total Amount <= 1000 (non corrisponde)
* **Regola 2**: Total Amount <= 2000 (non corrisponde)
* **Regola 3**: Total Amount <= 3000 (corrisponde)
* **Regola 4**: Total Amount <= 4000 (corrisponde)
* **Regola 5**: Total Amount <= 5000 (corrisponde)

Affinché **Any** si applichi, tutte le regole corrispondenti devono restituire lo stesso **Return Group**. Poiché i gruppi non corrispondono tra le diverse regole, il risultato sarebbe **false**.

### **8. Criterio First & Adjacent (prima e adiacente)**

Sceglie il risultato della regola adiacente alla prima regola che è vera.

**Esempio:**

| Regola | Condizione           | Gruppo restituito |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 3000 | GROUP_3     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 5000 | GROUP_5     |

Se l'importo totale è **1500**, le regole valutate saranno:

* **Regola 1**: Total Amount <= 1000 (non corrisponde)
* **Regola 2**: Total Amount <= 2000 (corrisponde)

Poiché la **Regola 2** è la prima regola che corrisponde, **First & Adjacent** applicherebbe il risultato della **Regola 3**: **GROUP_3**.

## **Test dell'albero decisionale**

**Panoramica:**
Il designer dell'albero decisionale include una funzionalità di test per convalidare la logica delle regole configurate. Questa funzionalità consente agli utenti di testare l'albero decisionale fornendo valori di input specifici per i campi selezionati.

**Passaggi per utilizzare la funzionalità di test:**

1.  **Individuare il pulsante Test:**

    * Nel designer dell'albero decisionale, trova il pulsante **Test**.

    <figure><img src="../../../.gitbook/assets/decision_tree_test_button.png" alt="Pulsante Test dell'albero decisionale" width="563"><figcaption></figcaption></figure>
2.  **Aprire la finestra popup di test:**

    * Fai clic sul pulsante **Test**.
    * Apparirà una finestra popup che fornisce campi di input corrispondenti ai criteri utilizzati nell'albero decisionale.

    <figure><img src="../../../.gitbook/assets/decision_tree_test_popup.png" alt="Popup di test dell'albero decisionale" width="421"><figcaption></figcaption></figure>
3. **Fornire i valori di input:**
   *   Inserisci i valori nei campi di input per simulare uno scenario reale.

       <figure><img src="../../../.gitbook/assets/decision_tree_test_input.png" alt="Input di test dell'albero decisionale" width="428"><figcaption></figcaption></figure>
4.  **Valutare i risultati:**

    * Dopo aver inserito gli input, l'albero li elabora in base al criterio scelto.
    * Il sistema evidenzia la regola o le regole che corrispondono agli input forniti.

    <figure><img src="../../../.gitbook/assets/decision_tree_test_result.png" alt="Risultato di test dell'albero decisionale" width="563"><figcaption></figcaption></figure>
5. **Esaminare il feedback in caso di nessuna corrispondenza:**
   * Se nessuna regola viene evidenziata, il sistema mostrerà un feedback che spiega perché nessuna regola ha corrisposto.
   * Usa questo feedback per modificare gli input o rivedere la configurazione dell'albero per individuare potenziali problemi.

## Esportazione e salvataggio

* **Save**: salva la configurazione corrente dell'albero decisionale.
* **Export**: consente di esportare la configurazione dell'albero decisionale, che può poi essere importata in un altro ambiente o utilizzata a scopo di backup.

## Casi d'uso

* **Flussi di lavoro di approvazione** — instrada le fatture a diversi approvatori in base a soglie di importo (ad esempio, gli importi superiori a 10.000 richiedono l'approvazione del responsabile).
* **Regole di convalida** — convalida automaticamente i valori dei campi e contrassegna i documenti che non soddisfano i criteri configurati.
* **Assegnazione sequenziale** — assegna i documenti agli utenti in un ordine specifico in base alle condizioni.
