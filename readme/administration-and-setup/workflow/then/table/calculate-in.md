# Calculate in



<figure><img src="../../../../.gitbook/assets/image (295).png" alt="" width="563"><figcaption></figcaption></figure>

## **Scopo:**

La scheda di workflow **"Calculate with Regex Dependency"** consente agli utenti di eseguire calcoli tra colonne in una tabella selezionata, con una condizione aggiuntiva basata su un pattern di espressione regolare (regex) applicato a una colonna di dipendenza. Se il pattern corrisponde, il calcolo viene eseguito e il risultato viene memorizzato nella colonna dei risultati specificata.

## **Componenti della scheda:**

1. **Table Name**
   * **Descrizione:** Specifica la **tabella** in cui verranno calcolate le colonne.
   * **Dettaglio:** Viene fornito un menu a discesa di tutte le **tabelle** disponibili per la selezione.
2. **Column Name (1st Column)**
   * **Descrizione:** Specifica la **prima colonna** coinvolta nel calcolo.
   * **Dettaglio:** Viene fornito un elenco di tutte le **colonne** disponibili per la selezione.
3. **Operation**
   * **Descrizione:** Definisce l'operazione matematica da applicare tra le colonne selezionate.
   * **Opzioni:**
     * **Add (+):** Somma il valore della seconda colonna al valore della prima colonna.
     * **Subtract (-):** Sottrae il valore della seconda colonna dalla prima colonna.
     * **Multiply (\*):** Moltiplica il valore della prima colonna per il valore della seconda colonna.
     * **Divide (/):** Divide il valore della prima colonna per la seconda colonna.
4. **Column Name (2nd Column)**
   * **Descrizione:** Specifica la **seconda colonna** coinvolta nel calcolo.
   * **Dettaglio:** Viene fornito un elenco di tutte le **colonne** disponibili per la selezione.
5. **Column Name (Dependency)**
   * **Descrizione:** Specifica la **colonna di dipendenza** a cui verrà applicato il pattern regex.
   * **Dettaglio:** Viene fornito un elenco di tutte le **colonne** disponibili per la corrispondenza del pattern.
6. **Regex Pattern**
   * **Descrizione:** Definisce il **pattern regex** che verrà utilizzato per la corrispondenza con la colonna di dipendenza.
   * **Dettaglio:** Se il valore nella colonna di dipendenza corrisponde al pattern regex, il calcolo verrà eseguito.
7. **Result Column**
   * **Descrizione:** Specifica la **colonna dei risultati** in cui verrà memorizzato il risultato del calcolo.
   * **Dettaglio:** Può essere una colonna nuova o esistente in cui verrà memorizzato il valore calcolato.

## **Funzionalità:**

* **Valutazione della condizione:**
  * La scheda esegue la sua azione solo se sia la sezione **"Where"** che la sezione **"And"** risultano vere.
  * La scheda esegue la sua azione solo se il valore nella colonna di dipendenza corrisponde al **pattern regex** fornito.
* **Calcolo delle colonne:**\
  Se il pattern regex corrisponde, la scheda esegue l'operazione matematica selezionata tra le due colonne scelte.
* **Memorizzazione del risultato:**\
  Il risultato del calcolo viene memorizzato nella **colonna dei risultati** selezionata.

## **Configurazione e impostazione:**

* **Seleziona la tabella:**\
  Scegli la **tabella** in cui verranno calcolate le colonne.
* **Scegli le colonne:**\
  Seleziona la **prima colonna** e la **seconda colonna** che verranno utilizzate nel calcolo.
* **Seleziona l'operazione:**\
  Scegli l'operazione matematica (**Add (+)**, **Subtract (-)**, **Multiply (\*)**, **Divide (/)**) da applicare tra le colonne.
* **Seleziona la colonna di dipendenza:**\
  Scegli la **colonna di dipendenza** a cui verrà applicato il pattern regex.
* **Definisci il pattern regex:**\
  Inserisci il **pattern regex** a cui la colonna di dipendenza dovrebbe corrispondere.
* **Seleziona la colonna dei risultati:**\
  Scegli la **colonna dei risultati** in cui verrà memorizzato il valore calcolato.

## **Conclusione:**

La scheda di workflow **"Calculate with Regex Dependency"** offre un modo potente per eseguire calcoli con logica condizionale basata su un pattern regex. Ciò garantisce che solo le righe in cui la colonna di dipendenza corrisponde al pattern specificato vengano sottoposte al calcolo specificato, e il risultato viene memorizzato nella colonna dei risultati scelta.
