# Porównanie Pola Dokumentu

<figure><img src="../../../.gitbook/assets/userlmn_7d5c06ce63181faee30b7bc6903e4d7b.png" alt=""><figcaption></figcaption></figure>

**Cel**

Ta karta przepływu pracy została zaprojektowana do automatycznego porównywania wartości dwóch określonych pól w dokumencie na podstawie zdefiniowanego operatora. Służy do egzekwowania integralności danych i zapewnienia, że dane dokumentu są zgodne z regułami biznesowymi lub warunkami.

**Składniki Karty**

1. **Nazwy Pól**
* **Opis**: Określa nazwy dwóch pól w dokumencie, które zostaną porównane.
* **Szczegóły**: Użytkownicy muszą wprowadzić dokładne nazwy pól tak, jak się one pojawiają w systemie. Pola te mogą być dowolnego typu danych, które obsługują porównanie, takie jak liczbowe, daty lub pola tekstowe.
2. **Operator**
* **Opis**: Operator porównania używany do oceny relacji między wartościami dwóch pól.
* **Opcje**:
* **Równy (==)**: Sprawdza, czy wartość pierwszego pola jest równa wartości drugiego pola.
* **Nierówny (!=)**: Sprawdza, czy wartość pierwszego pola jest różna od wartości drugiego pola.
* **Większy niż (>)**: Sprawdza, czy wartość pierwszego pola jest większa niż wartość drugiego pola.
* **Większy niż lub równy (>=)**: Sprawdza, czy wartość pierwszego pola jest większa lub równa wartości drugiego pola.
* **Mniejszy niż (<)**: Sprawdza, czy wartość pierwszego pola jest mniejsza niż wartość drugiego pola.
* **Mniejszy niż lub równy (<=)**: Sprawdza, czy wartość pierwszego pola jest mniejsza lub równa wartości drugiego pola.

**Funkcjonalność**

* **Wybór Pola**: Użytkownicy wprowadzają lub wybierają nazwy dwóch pól do porównania. Zazwyczaj odbywa się to za pomocą formularza lub menu rozwijanego w konfiguracji karty.
* **Wybór Operatora**: Użytkownicy wybierają operatora z listy dostępnych opcji, które określają sposób porównywania pól.
* **Wykonanie Porównania**:
* System odczytuje wartości z określonych pól i stosuje wybrany operator do oceny relacji między nimi.
* Na podstawie wyniku porównania (prawda lub fałsz) mogą zostać uruchomione kolejne działania. Na przykład, jeśli porównanie nie powiedzie się, system może oznaczyć dokument do przeglądu, zablokować dalsze przetwarzanie lub powiadomić odpowiednie strony.

**Interakcje Użytkownika**

* **Konfiguracja i Ustawienia**: Użytkownicy konfigurują porównanie, wprowadzając nazwy pól i wybierając operatora. Konfiguracja ta powinna być prosta i prowadzona, być może z tekstem pomocy lub przykładami.
* **Monitorowanie i Raportowanie**: System może dostarczać informacje zwrotne na temat wyników porównań, takie jak logowanie wszystkich wykonanych porównań, ich wyniki i wszelkie działania podjęte w odpowiedzi na wyniki porównań.
* **Obsługa Błędów i Powiadomienia**: Użytkownicy otrzymują alert, jeśli porównanie nie może zostać wykonane (np. jeśli jedno z pól nie zostanie znalezione w dokumencie lub nie będzie w porównywalnym formacie).

#### Podsumowanie

Karta przepływu pracy "Porównanie Pola Dokumentu" jest kluczowa dla utrzymania dokładności i spójności danych w dokumentach w systemie ERP. Pomaga automatyzować kontrole, które w przeciwnym razie byłyby manualne, podatne na błędy i czasochłonne, zwiększając efektywność i niezawodność przetwarzania dokumentów. Dokumentowanie tej karty w sposób jasny w podręczniku systemu ERP pomoże użytkownikom skutecznie korzystać z tej funkcji, zapewniając, że dane w dokumentach pozostają spójne i zgodne z regułami biznesowymi.
