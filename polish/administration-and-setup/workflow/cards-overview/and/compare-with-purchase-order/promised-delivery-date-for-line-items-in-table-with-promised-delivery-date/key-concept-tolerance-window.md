# Key Concept: Tolerance Window

Przed przyjrzeniem się operatorom ważne jest zrozumienie, w jaki sposób obliczane jest okno tolerancji.

## Czym jest okno tolerancji?

Okno tolerancji definiuje zakres akceptowalnych dat wokół przyrzeczonej daty dostawy w zamówieniu zakupu.

**Przykład:**

* Data zamówienia zakupu: **9 stycznia**
* Tolerance Days: **3**
* Okno tolerancji: **6 stycznia → 12 stycznia**

> <mark style="color:red;">Tylko wybrane</mark> <mark style="color:red;"></mark><mark style="color:red;">**Allowed Tolerance Days**</mark> <mark style="color:red;"></mark><mark style="color:red;">(dni tygodnia) są liczone przy obliczaniu tego okna.</mark>

### Przykład wizualnej osi czasu

```
← Past                           Future →
|-----|-----|-----|-----|-----|-----|-----|
     6 Jan      9 Jan      12 Jan
   (Start)    (PO Date)     (End)
```

### Zachowanie operatorów wyjaśnione na przykładach

* **Equals (=)**
  * **Znaczenie:**\
    Data dostawy pozycji musi przypadać _wewnątrz_ okna tolerancji.
  * **Daty prawidłowe:**
    * Dowolna data między **6 stycznia a 12 stycznia** (włącznie)
  * **Daty nieprawidłowe:**
    * Dowolna data **przed 6 stycznia**
    * Dowolna data **po 12 stycznia**
* **Not Equals (≠)**
  * **Znaczenie:**\
    Data dostawy pozycji musi przypadać _poza_ oknem tolerancji.
  * **Daty prawidłowe:**
    * Dowolna data **przed 6 stycznia**
    * Dowolna data **po 12 stycznia**
  * **Daty nieprawidłowe:**
    * Daty między **6 stycznia a 12 stycznia**
* **Greater or Equals (≥)**
  * **Znaczenie:**\
    Data dostawy pozycji musi przypadać w dniu lub po **rozpoczęciu okna tolerancji**.
  * **Daty prawidłowe:**
    * **6 stycznia → dowolna przyszła data**
  * **Daty nieprawidłowe:**
    * Dowolna data **przed 6 stycznia**
  * <mark style="color:red;">**Ważne:**</mark>\
    Ten operator dopuszcza daty _wewnątrz_ okna tolerancji **oraz poza nim**.
* **Lesser or Equals (≤)**
  * **Znaczenie:**\
    Data dostawy pozycji musi przypadać w dniu lub przed **końcem okna tolerancji**.
  * **Daty prawidłowe:**
    * Dowolna przeszła data aż do **12 stycznia**
  * **Daty nieprawidłowe:**
    * Dowolna data **po 12 stycznia**
* **Greater Than (>)**
  * **Znaczenie:**\
    Data dostawy pozycji musi przypadać _ściśle po_ oknie tolerancji.
  * **Daty prawidłowe:**
    * **13 stycznia → dowolna przyszła data**
  * **Daty nieprawidłowe:**
    * Dowolna data **w dniu 12 stycznia lub wcześniej**
* **Lesser Than (<)**
  * **Znaczenie:**\
    Data dostawy pozycji musi przypadać _ściśle przed_ oknem tolerancji.
  * **Daty prawidłowe:**
    * Dowolna data **przed 6 stycznia**
  * **Daty nieprawidłowe:**
    * Dowolna data **w dniu 6 stycznia lub później**

## Jak „Allowed Tolerance Days” wpływają na okno tolerancji

Przy obliczaniu okna tolerancji **liczone są tylko wybrane dni tygodnia**.\
Dni, które nie są wybrane (takie jak weekendy lub wykluczone dni tygodnia), są **całkowicie pomijane**.

#### Przykład: Obliczanie tolerancji na podstawie dni tygodnia

**Konfiguracja:**

* Data zamówienia zakupu: **środa, 9 stycznia**
* Tolerance Days: **3**
* Allowed Tolerance Days: **poniedziałek, wtorek, środa, czwartek, piątek**
* Weekendy (sobota, niedziela): **Niewybrane**

#### Obliczanie krok po kroku

Zaczynając od daty zamówienia zakupu (**9 stycznia**):

**Liczenie wstecz (3 dni tolerancji):**

* wtorek, 8 stycznia → **Dzień 1**
* poniedziałek, 7 stycznia → **Dzień 2**
* niedziela, 6 stycznia → _Pominięte (niedozwolone)_
* sobota, 5 stycznia → _Pominięte (niedozwolone)_
* piątek, 4 stycznia → **Dzień 3**

➡ **Data początkowa tolerancji: piątek, 4 stycznia**

**Liczenie do przodu (3 dni tolerancji):**

* czwartek, 10 stycznia → **Dzień 1**
* piątek, 11 stycznia → **Dzień 2**
* sobota, 12 stycznia → _Pominięte_
* niedziela, 13 stycznia → _Pominięte_
* poniedziałek, 14 stycznia → **Dzień 3**

➡ **Data końcowa tolerancji: poniedziałek, 14 stycznia**

#### Wynikowe okno tolerancji

```
4 January  →  14 January
```

#### Dlaczego to ma znaczenie

Jeśli Allowed Tolerance Days są skonfigurowane nieprawidłowo:

* Daty dostawy mogą wydawać się **nieoczekiwanie prawidłowe lub nieprawidłowe**
* Wczesne lub opóźnione dostawy mogą nie być prawidłowo wykrywane
