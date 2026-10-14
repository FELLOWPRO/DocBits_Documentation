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

* [Unico](decision-trees/unique-policy.md)
* [Primo](decision-trees/first-policy.md)
* [Priorità](decision-trees/priority-policy.md)
* [Raccogliere (somma)](decision-trees/collect-sum-policy.md)
* [Raccogliere (Min/max/conteggio)](decision-trees/collect-min-max-count-policy.md)
* [Ordine della regola](decision-trees/rule-order-policy.md)
* [Qualsiasi](decision-trees/any-policy.md)
* [Primo e adiacente](decision-trees/first-and-adjacent-policy.md)

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
