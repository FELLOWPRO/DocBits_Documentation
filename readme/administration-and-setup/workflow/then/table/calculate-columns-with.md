# Calcola colonne con

<figure><img src="../../../../.gitbook/assets/workflow_card_calc_columns_v1-it-it.png" alt="Calcola colonne con, Versione 1" width="634"><figcaption><p>Versione 1</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/workflow_card_calc_columns_v2-it-it.png" alt="Calcola colonne con, Versione 2" width="634"><figcaption><p>Versione 2</p></figcaption></figure>

## **Scopo:**

La scheda di workflow **"Calcola colonne nella tabella"** viene utilizzata per eseguire calcoli tra colonne in una tabella selezionata. Consente agli utenti di selezionare le colonne, applicare un'operazione matematica e memorizzare il risultato in una colonna dei risultati specificata.

## **Componenti della scheda:**

1. **Nome tabella**
   * **Descrizione:** Specifica la **tabella** in cui verranno calcolate le colonne.
   * **Dettaglio:** Viene fornito un menu a discesa di tutte le **tabelle** disponibili per la selezione.
2. **Nome colonna (1a colonna)**
   * **Descrizione:** Specifica la **prima colonna** da coinvolgere nel calcolo.
   * **Dettaglio:** Viene fornito un elenco di tutte le **colonne** disponibili per la selezione.
3. **Operazione**
   * **Descrizione:** Definisce l'operazione matematica da applicare tra le colonne selezionate.
   * **Opzioni:**
     * **Add (+):** Somma il valore della seconda colonna al valore della prima colonna.
     * **Sottrarre (-):** Sottrae il valore della seconda colonna dal valore della prima colonna.
     * **Multiply (\*):** Moltiplica il valore della prima colonna per il valore della seconda colonna.
     * **Dividi (/):** Divide il valore della prima colonna per il valore della seconda colonna.
4. **Nome colonna (2a colonna)**
   * **Descrizione:** Specifica la **seconda colonna** da coinvolgere nel calcolo.
   * **Dettaglio:** Viene fornito un elenco delle **colonne** disponibili per la selezione.
5. **Colonna dei risultati**
   * **Descrizione:** Specifica la **colonna** in cui verrà memorizzato il risultato del calcolo.
   * **Dettaglio:** Viene fornito un elenco delle **colonne** disponibili in cui verrà salvato il valore calcolato.

## **Funzionalità:**

* **Valutazione della condizione:**\
  La scheda esegue la sua azione solo se sia la sezione **"Quando"** che la sezione **"E"** risultano vere.
* **Calcolo delle colonne:**\
  La scheda esegue l'operazione matematica selezionata tra le due colonne scelte.
* **Memorizzazione del risultato:**\
  Il risultato del calcolo viene memorizzato nella **colonna dei risultati** selezionata.

## **Configurazione e impostazione:**

* **Seleziona la tabella:**\
  Scegli la **tabella** in cui verranno calcolate le colonne.
* **Scegli le colonne:**\
  Seleziona la **prima colonna** e la **seconda colonna** che verranno utilizzate nel calcolo.
* **Seleziona l'operazione:**\
  Scegli l'operazione matematica (**Add (+)**, **Sottrai (-)**, **Multiply (\*)**, **Divide (/)**) da applicare tra le colonne.
* **Seleziona la colonna dei risultati:**\
  Scegli la **colonna dei risultati** in cui verrà memorizzato il calcolo.

## **Conclusione:**

La scheda di workflow **"Calcola colonne nella tabella"** consente agli utenti di eseguire calcoli dinamici tra colonne in una tabella e di memorizzare i risultati in una colonna designata. La scheda offre la flessibilità di applicare diverse operazioni matematiche e garantisce che il risultato venga memorizzato nella colonna specificata.

<!-- workflow-card-practical-example-20261021 -->

## Esempio pratico

**Quando utilizzarlo:** Calcola i totali delle righe dalla quantità e dal prezzo unitario.

**Configurazione:** Seleziona la tabella `lines`, colonne `quantity` e `unit_price`, moltiplicazione e colonna dei risultati `line_total`.

**Risultato atteso e controesempio:** Una riga contenente `2` e `10` produce `20`. Testare un'altra riga in modo indipendente e diagnosticare l'input mancante o non numerico anziché trattarlo come un totale valido.

Questa è una configurazione illustrativa e il risultato atteso. Utilizza campi, utenti e gruppi configurati nella tua organizzazione di test; non si afferma che questo esempio sia stato eseguito.
