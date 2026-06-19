# Criterio Collect (min/max/count) (raccogli min/max/conteggio)

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
