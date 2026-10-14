# Strutturazione e Miglioramento dell'Estrazione delle Tabelle in DocBits

Una volta che una tabella è stata estratta e il mapping iniziale delle colonne è completo, è possibile migliorare la qualità e la struttura dei dati utilizzando diversi strumenti integrati. Questa guida ti accompagna attraverso:

* Raggruppamento delle righe
* Selezione manuale delle righe
* Mapping delle colonne
* Perfezionamento dell'intestazione utilizzando regex

Questi strumenti sono particolarmente utili quando si tratta di layout di documenti complessi o non coerenti.

## 1. Raggruppamento delle Righe

Documenti come fatture o conferme d'ordine spesso contengono voci di tabella in cui una colonna (ad esempio, una descrizione) si estende su più righe, mentre altre colonne (ad esempio, quantità o prezzo) utilizzano una sola riga.

Prendi ad esempio questa fattura tedesca — la colonna "Bezeichnung" (descrizione) si estende su più righe:

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FVino2M4Esor3IRHGqBd5Brx7_lKPIwEOlRYBHzMXw4WoacFNW39hbWuwoUNGocubx4Bh9_BvUBqZSWA4U_NmU8FBw4Q1_AiTASgMx-2MLKvsHLJY057oqyks0fQ5b7mI577JTX5rBKdEG90O9F5TcoU\&width=768\&dpr=4\&quality=100\&sign=ae0bd75a\&sv=2)

Inizialmente, DocBits estrae ogni riga separatamente:

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FUX5OdkW59HPVROnNzSeZbDw4NYTPbfayDLIXBQi0pwHzUEJ1B5t7I9uKBNc0dmOB3Cile8Xv6AdgVXuUd0aMbQFGWagBCEetw8P-N4zgG_cGTjWHhpDtGQZg27UZKdCDJ5FeEDJgFAYtTB8kZrMSdho\&width=768\&dpr=4\&quality=100\&sign=b6990876\&sv=2)

Puoi quindi **raggruppare le righe in base a una colonna**, come ad esempio "Posizione." Questo unisce le righe correlate in un'unica voce strutturata:

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FPxA6h2udUuYd1YmHV97t-bzfZzipFpdA5t8gjpGXWx9sA-I4tW3tYwD28icv88UEmitz0EAaWuGkU5ZwqAjcQnoOkmg9u1AcBJW3nITU6eFa0foHB-AQPb0qv0AWaaEwM6WvwaEcAODEUzKtvRZOMN0\&width=768\&dpr=4\&quality=100\&sign=36b99bc7\&sv=2)

## 2. Selezione Manuale delle Righe

In alcuni casi, il testo su un documento è distribuito su più colonne in una singola riga, rendendo difficile l'assegnazione automatica.

Ecco un esempio in cui la riga "PRAEF" si sovrappone a **Bezeichnung**, **Menge**, **ME**, e **Preis in EUR**:

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FLbVbmfdOBpeCWDftPvW0qjEHjbLmWYRrAGTZHVW8VEHQTEvl5GoqH2wkFE5iUOySmF50b1V8CDAZhfMzPTeMQscmc61SDKaqSCW-y0Z7fjlwOjhtjxWD44oCsgHmwrgrBD4cuEGgn9JY_UX3t9jRlPs\&width=768\&dpr=4\&quality=100\&sign=5ff4a2e1\&sv=2)

### Come Assegnare Manualmente i Valori:

1.  **Abilita la Modalità di Addestramento**

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2F4D8iCXk0p_Mur8bX_11ne_2iA-GOxoFi2OQWlSEvrH1auoE0ksnYXpZx3Pw3PUJJRZJN85dnQlSSBB369FfafXAy8adjFZcnepQnODSaaIj69cxtUKFAXPgn5eyPE6jbJuzStJALMgumlt49Z1Pv3FY\&width=768\&dpr=4\&quality=100\&sign=232c58a9\&sv=2)
2.  **Attiva la Modalità Modifica Righe**

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2F8YQmo_WRuKKVjk1a_eoxSBiQr0GncuS4BmCA0aI9aOlrbsIvdj8dZlurxxBHp2lH4ozT4HPWw9qYDW7xLQ7u2DSyU8DrNzSBC7LjzKLTDJ2tudY9a_DENDoK5Aya6L1hcf1WF1RD92S_DzhGVV4Gh6Q\&width=768\&dpr=4\&quality=100\&sign=8fc5c089\&sv=2)
3.  **Seleziona e Mappa il Testo** Clicca sulla parte corretta del testo e assegnalo a un'intestazione di colonna **blu**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2Fi2tlbwl9qFE0clthaoRPe7kcPRiURCvemuLEjBK4uAnfsR4auXbftMfEY1ZW5WXwezTBVSG5hbNRkddwIeLtrgJUvZoeKGdPKN8f75O_dPdIWkm4EFALfAj-evDUI3UKrgNOTNjF37C1bBLtE95OA1w\&width=768\&dpr=4\&quality=100\&sign=842a42\&sv=2)

> Nota: Le colonne di colore viola sono già mappate dal sistema e non possono essere modificate manualmente.

## 3. Mapping delle Colonne

Il mapping delle colonne collega i dati estratti alle intestazioni di colonna previste, garantendo coerenza ed esportabilità.

Per mappare o rimpiazzare una colonna:

1. Clicca sull'intestazione della colonna nella vista di estrazione.
2. Scegli la colonna di destinazione corretta dal menu a discesa.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FX_65pCWrI4HMFr_aiA0eoSDp-yIYy49lULzAZaiIgnr0aIowlLSed21MuehkGLs4UIdQousdfhiZi5pnQtpZ0uUn6dxlzii7WPQvov-kN1_Jimsi6U6zowOLxjBzZzZ47kaRhduAVBd_Ya9QQtXTpJ4\&width=768\&dpr=4\&quality=100\&sign=4e2a3bdc\&sv=2)

Puoi regolare il mapping tutte le volte che è necessario.

## 4. Estrarre da Sopra / Sotto

Alcuni documenti sono strutturati in modo tale che i valori di tabella rilevanti non compaiano sulla stessa riga di altri dati. In questi casi, DocBits ti consente di controllare **da dove i dati dovrebbero essere estratti**:

* **Estrai da Sopra**: Usa questo quando il valore per la riga corrente appare **nella riga sopra**.
* **Estrai da Sotto**: Usa questo quando il valore appare **nella riga sotto** la riga corrente.

**Dove Trovarlo**

1. Entra in **Modalità di Addestramento**.
2. Clicca sui tre puntini (⋯) sull'intestazione di una colonna.
3. Sotto l'opzione **"Estrai Da"**, scegli `Sopra` o `Sotto` a seconda del layout del documento.

## 5. Formato dell'Importo

Alcune colonne, come **Quantità** o **Prezzo Unitario**, contengono valori numerici o di data che possono seguire diverse convenzioni di formattazione a seconda dell'origine o della località del documento. DocBits ti consente di specificare il formato che questi valori dovrebbero seguire per garantire un'estrazione e un'interpretazione accurate.

**Opzioni di Formato dell'Importo:**

* Definisci il formato numerico o di data previsto per la colonna, come US (MM/GG/AAAA, decimale con punto), Polonia (GG.MM.AAAA, decimale con virgola), Germania e altri.
* Questo aiuta DocBits a interpretare correttamente e standardizzare i valori anche se il documento utilizza un formato regionale diverso.

**Dove Trovarlo**

1. Entra in **Modalità di Addestramento**.
2. Clicca sui tre puntini (⋯) sull'intestazione di una colonna supportata (ad esempio, Quantità, Prezzo Unitario).
3. Sotto l'opzione **Formato dell'Importo**, seleziona il formato desiderato che corrisponde alla località del tuo documento.

## 6. Miglioramento dell'Estrazione delle Tabelle con Regex

## **Cosa Fa**

Questa funzionalità ti consente di definire una regex per ciascuna intestazione di tabella, migliorando l'accuratezza dell'estrazione e garantendo risultati corretti.

## **Come Usarlo**

1. Apri un documento dal fornitore per il quale desideri definire una regex.
2.  Passa alla vista **Estrazione della Tabella**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FDdlNrO6hG6jnEeWU9DuZ%252Fimage.png%3Falt%3Dmedia%26token%3Dca11a537-27a4-4b00-b3e7-f77540c28c2b\&width=768\&dpr=4\&quality=100\&sign=fd47355a\&sv=2)
3. Abilita la **Modalità di Addestramento**.
4.  Seleziona l'intestazione della tabella che desideri perfezionare, quindi scegli **Regex**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fes6PsB9sHHXp0CNRj6YF%252Fimage.png%3Falt%3Dmedia%26token%3D6e31e4db-fd2f-487c-ac19-f1d6add81ad1\&width=768\&dpr=4\&quality=100\&sign=32264560\&sv=2)
5.  Comparirà un popup dove puoi inserire e definire la tua regex.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FWB7hjuuyVVAewRqrnhYj%252FiScreen%2520Shoter%2520-%2520Google%2520Chrome%2520-%2520250303135020.jpg%3Falt%3Dmedia%26token%3D6a31253d-18d7-4d8f-a00e-acd89a744127\&width=768\&dpr=4\&quality=100\&sign=d8d2d94a\&sv=2)
6.  Clicca su **Convalida** per controllare la regex, quindi su **Salva Modifiche** per applicarla.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FC4R2o2W10ct1o0oesTLZ%252FiScreen%2520Shoter%2520-%2520Google%2520Chrome%2520-%2520250303135153.jpg%3Falt%3Dmedia%26token%3D43e53a05-53fe-4503-ba51-55c85910bd82\&width=768\&dpr=4\&quality=100\&sign=9ec6eb7b\&sv=2)
7. **Salva la regola e conferma** per applicare le modifiche.

## Quando Utilizzare Ciascuna Funzionalità

Utilizza questi strumenti per aumentare l'accuratezza dell'estrazione e ridurre il lavoro manuale:

* **Raggruppamento**: Quando una descrizione o qualsiasi colonna si estende su più righe e deve essere combinata per chiarezza.
* **Selezione Manuale delle Righe**: Quando le righe non sono strutturate correttamente e parti del contenuto finiscono nelle colonne sbagliate.
* **Mapping delle Colonne**: Quando i nomi delle colonne rilevati automaticamente non corrispondono alla tua struttura o necessitano di perfezionamento.
* **Regole Regex**: Quando le intestazioni delle tabelle variano leggermente tra documenti dello stesso fornitore o l'OCR introduce delle inconsistenze.
