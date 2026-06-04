# Document Field Comparison

<figure><img src="../../../../.gitbook/assets/userlmn_7d5c06ce63181faee30b7bc6903e4d7b.png" alt=""><figcaption></figcaption></figure>

**Cel**

Ta karta przepływu pracy służy do automatycznego porównania wartości dwóch określonych pól w dokumencie na podstawie zdefiniowanego operatora. Służy do egzekwowania integralności danych i zapewnienia, że dane dokumentu są zgodne z regułami lub warunkami biznesowymi.

**Komponenty karty**

1. **Field Names**
   * **Opis**: Określa nazwy dwóch pól w dokumencie, które będą porównywane.
   * **Szczegóły**: Użytkownicy muszą wprowadzić dokładne nazwy pól, tak jak pojawiają się w systemie. Pola te mogą być dowolnego typu danych obsługującego porównanie, takiego jak pola liczbowe, daty lub tekstowe.
2. **Operator**
   * **Opis**: Operator porównania używany do oceny relacji między wartościami dwóch pól.
   * **Opcje**:
     * **Equal (==)**: Sprawdza, czy wartość pierwszego pola jest równa wartości drugiego pola.
     * **Not Equal (!=)**: Sprawdza, czy wartość pierwszego pola nie jest równa wartości drugiego pola.
     * **Greater Than (>)**: Sprawdza, czy wartość pierwszego pola jest większa niż wartość drugiego pola.
     * **Greater Than or Equal (>=)**: Sprawdza, czy wartość pierwszego pola jest większa lub równa wartości drugiego pola.
     * **Less Than (<)**: Sprawdza, czy wartość pierwszego pola jest mniejsza niż wartość drugiego pola.
     * **Less Than or Equal (<=)**: Sprawdza, czy wartość pierwszego pola jest mniejsza lub równa wartości drugiego pola.

**Funkcjonalność**

* **Wybór pól**: Użytkownicy wprowadzają lub wybierają nazwy dwóch pól do porównania. Zazwyczaj odbywa się to za pomocą formularza lub menu rozwijanego w konfiguracji karty.
* **Wybór operatora**: Użytkownicy wybierają operator z listy dostępnych opcji, które definiują sposób porównania pól.
* **Wykonanie porównania**:
  * System odczytuje wartości z określonych pól i stosuje wybrany operator do oceny relacji między nimi.
  * Na podstawie wyniku porównania (prawda lub fałsz) mogą zostać wyzwolone kolejne akcje. Na przykład, jeśli porównanie się nie powiedzie, system może oznaczyć dokument do przeglądu, zablokować dalsze przetwarzanie lub powiadomić odpowiedzialne strony.

**Interakcje użytkownika**

* **Konfiguracja**: Użytkownicy konfigurują porównanie, wprowadzając nazwy pól i wybierając operator. Konfiguracja powinna być prosta i prowadzona, możliwie z tekstem pomocy lub przykładami.
* **Monitorowanie i raportowanie**: System może zapewniać informacje zwrotne o wynikach porównań, takie jak rejestrowanie wszystkich wykonanych porównań, ich wyników i wszelkich akcji podjętych w odpowiedzi na wyniki porównań.
* **Obsługa błędów i powiadomienia**: Użytkownicy otrzymują alerty, jeśli porównanie nie może zostać wykonane (np. jeśli jedno z pól nie zostanie znalezione w dokumencie lub nie jest w formacie porównywalnym).

#### Podsumowanie

Karta przepływu pracy "Document Field Comparison" jest kluczowa dla utrzymania dokładności i spójności danych w dokumentach w systemie ERP. Pomaga zautomatyzować kontrole, które w przeciwnym razie byłyby ręczne, podatne na błędy i czasochłonne, zwiększając efektywność i niezawodność przetwarzania dokumentów. Jasne udokumentowanie tej karty w instrukcji systemu ERP pomoże użytkownikom skutecznie wykorzystać tę funkcję, zapewniając, że dane w dokumentach pozostają spójne i zgodne z regułami biznesowymi.
