# Drzewa decyzyjne

{% embed url="https://youtu.be/omFWSkSjlL0" %}
Jak utworzyć drzewo decyzyjne w DocBits (warunki, polityki, testowanie i eksport)
{% endembed %}

## Przegląd

Drzewa decyzyjne to zaawansowana funkcja umożliwiająca zautomatyzowane kierowanie dokumentów i podejmowanie decyzji na podstawie zdefiniowanych wcześniej reguł. Funkcja ta jest szczególnie przydatna w złożonych środowiskach, w których trzeba ocenić różne warunki, aby ustalić właściwy sposób postępowania, taki jak przypisywanie cen, ustalanie ilości czy kierowanie dokumentów.

#### Kluczowe komponenty

* **Lista drzew decyzyjnych**: jest to główny interfejs, w którym wyświetlane są wszystkie istniejące drzewa decyzyjne. Każde drzewo decyzyjne może być powiązane z określonym typem dokumentu, takim jak `INVOICE` lub `QUOTE`.
* **Projektant drzewa decyzyjnego**: ten interfejs umożliwia tworzenie i edytowanie drzew decyzyjnych, w którym można zdefiniować reguły, operatory i działania, jakie należy podjąć po spełnieniu określonych warunków.

## Interfejs drzewa decyzyjnego

#### Lista drzew decyzyjnych

Lista drzew decyzyjnych wyświetla wszystkie skonfigurowane drzewa decyzyjne. Otwórz ją w **Settings → Document Processing → Decision Trees**.

<figure><img src="../../../.gitbook/assets/decision_trees.png" alt="Lista drzew decyzyjnych"><figcaption><p>Lista drzew decyzyjnych</p></figcaption></figure>

Każdy wpis pokazuje:

| Kolumna | Opis |
|--------|-------------|
| **Name** | Nazwa drzewa decyzyjnego. Kliknij ją, aby otworzyć Projektanta. |
| **Document Type** | Typ dokumentu, którego dotyczy drzewo (np. `INVOICE`, `QUOTE`). |
| **Last Modified By** | Użytkownik, który ostatnio edytował drzewo. |
| **Last Modified At** | Znacznik czasu ostatniej zmiany. |
| **Actions** | Menu z trzema kropkami umożliwiające edycję, kopiowanie, eksport lub usunięcie drzewa. |

#### Tworzenie drzewa decyzyjnego

1. Kliknij **+ Add Decision Tree** w prawym górnym rogu.
2. Wprowadź **Name** i wybierz **Document Type**.
3. Użyj Projektanta drzewa decyzyjnego (poniżej), aby zdefiniować warunki, polityki i wyniki.

#### Importowanie drzewa decyzyjnego

Kliknij **Import Decision Tree**, aby przesłać wcześniej wyeksportowany plik drzewa decyzyjnego (w formacie JSON). Jest to przydatne do kopiowania drzewa między organizacjami lub środowiskami.

## Projektant drzewa decyzyjnego

Projektant drzewa decyzyjnego umożliwia konfigurowanie reguł, które określają sposób podejmowania decyzji.

### **Komponenty Projektanta drzewa decyzyjnego**

* **Reguły**: każda reguła składa się z warunków i działań.
* **Select Source**: ta lista rozwijana umożliwia wskazanie pola źródłowego do oceny.
* **Select Operator**: definiuje operator logiczny (np. `<=`, `>=`, `=`, `!=`), który ma zostać zastosowany do pola źródłowego.
* **Result**: definiuje wynik lub działanie, które należy podjąć po spełnieniu warunków.
* **Add New Row**: umożliwia dodanie kolejnych reguł do drzewa decyzyjnego.

### Przykład konfiguracji drzewa decyzyjnego

To drzewo decyzyjne ocenia pole **Total Amount** i przypisuje je do różnych grup na podstawie zdefiniowanych wcześniej warunków. Każda reguła porównuje kwotę całkowitą z określoną wartością, a w zależności od tego, który warunek jest spełniony, zwracana jest odpowiednia **Group**.

<figure><img src="../../../.gitbook/assets/decision_tree_example_total_amount.png" alt="Przykład drzewa decyzyjnego – Total Amount"><figcaption></figcaption></figure>

To drzewo decyzyjne ocenia dwa kluczowe warunki, aby ustalić, którą grupę należy przypisać: **Total Amount** oraz **Warehouse Status**. Drzewo wykorzystuje progi oparte na kwocie całkowitej, aby określić, która grupa jest zwracana, z dodatkowym rozróżnieniem, czy magazyn jest oznaczony jako „Warehouse Main", „Warehouse Sub", czy „Not Warehouse Main".

<figure><img src="../../../.gitbook/assets/decision_tree_example_warehouse_status.png" alt="Przykład drzewa decyzyjnego – Warehouse Status"><figcaption></figcaption></figure>

Każda reguła jest oceniana sekwencyjnie.

## Polityka drzewa decyzyjnego

Polityka drzewa decyzyjnego określa sposób przetwarzania wielu reguł w obrębie drzewa decyzyjnego. Możesz wybrać spośród kilku polityk:

### **1. Polityka unikalności (Unique)**

Zapewnia dopasowanie tylko jednej reguły. Jeśli dopasowanych zostanie wiele reguł, drzewo decyzyjne zwróci wartość false.

**Przykład:**

| Reguła | Warunek            | Zwracana grupa |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 5000 | GROUP_5     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 3000 | GROUP_3     |

Jeśli kwota całkowita wynosi **1500**, ocenione reguły będą następujące:

* **Reguła 1**: Total Amount <= 1000 (brak dopasowania)
* **Reguła 2**: Total Amount <= 2000 (dopasowanie)
* **Reguła 3**: Total Amount <= 5000 (dopasowanie)
* **Reguła 4**: Total Amount <= 4000 (dopasowanie)
* **Reguła 5**: Total Amount <= 3000 (dopasowanie)

Ponieważ dopasowano wiele reguł (**Reguła 2**, **Reguła 3**, **Reguła 4**, **Reguła 5**), drzewo decyzyjne zwróci wartość **false**, ponieważ polityka **unikalności** zapewnia, że dopasowana może być tylko jedna reguła.

### **2. Polityka pierwszego dopasowania (First)**

Stosowana jest pierwsza dopasowana reguła, a kolejne reguły nie są już oceniane.

**Przykład:**

| Reguła | Warunek            | Zwracana grupa |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 5000 | GROUP_5     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 3000 | GROUP_3     |

Jeśli kwota całkowita wynosi **1500**, ocenione reguły będą następujące:

* **Reguła 1**: Total Amount <= 1000 (brak dopasowania)
* **Reguła 2**: Total Amount <= 2000 (dopasowanie) → Drzewo decyzyjne przerywa ocenę kolejnych reguł i stosuje **GROUP_2**.

### **3. Polityka priorytetu (Priority)**

Wybór tej opcji umożliwia ustawienie priorytetów dla każdej reguły. Im niższa wybrana liczba, tym wyższy priorytet (tzn. priorytet 1 ma najwyższy priorytet). Reguły są oceniane na podstawie kolejności ich priorytetów. Zastosowana zostanie dopasowana reguła o najwyższym priorytecie.

**Przykład:**

<table><thead><tr><th width="137">Reguła</th><th width="110">Priorytet</th><th width="268">Warunek</th><th>Zwracana grupa</th></tr></thead><tbody><tr><td>1</td><td>5</td><td>Total Amount &#x3C;= 1000</td><td>GROUP_1</td></tr><tr><td>2</td><td>4</td><td>Total Amount &#x3C;= 2000</td><td>GROUP_2</td></tr><tr><td>3</td><td>3</td><td>Total Amount &#x3C;= 3000</td><td>GROUP_3</td></tr><tr><td>4</td><td>2</td><td>Total Amount &#x3C;= 4000</td><td>GROUP_4</td></tr><tr><td>5</td><td>1</td><td>Total Amount &#x3C;= 5000</td><td>GROUP_5</td></tr></tbody></table>

Jeśli kwota całkowita wynosi **1500**, ocenione reguły będą następujące:

* **Reguła 1**: Total Amount <= 1000 (brak dopasowania)
* **Reguła 2**: Total Amount <= 2000 (dopasowanie)
* **Reguła 3**: Total Amount <= 3000 (dopasowanie)
* **Reguła 4**: Total Amount <= 4000 (dopasowanie)
* **Reguła 5**: Total Amount <= 5000 (dopasowanie)

Ponieważ priorytet jest stosowany w kolejności **5, 4, 3, 2, 1**, dopasowaną regułą o najwyższym priorytecie będzie **Reguła 5** (**GROUP_5**). Drzewo decyzyjne zwróci **GROUP_5**, ponieważ **Reguła 5** ma najwyższy priorytet (priorytet 1).

### **4. Polityka zbierania – suma (Collect – sum)**

Ta polityka zbiera wszystkie dopasowane reguły i sumuje wyniki. Działa tylko dla **Return Type Value**.

**Przykład:**

| Reguła | Warunek            | Zwracana wartość |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | 1            |
| 2    | Total Amount <= 2000 | 2            |
| 3    | Total Amount <= 3000 | 3            |
| 4    | Total Amount <= 4000 | 4            |
| 5    | Total Amount <= 5000 | 5            |

Dla wartości wejściowej **Total Amount = 3500** ocena reguł wyglądałaby następująco:

* **Reguła 1**: Total Amount <= 1000 (brak dopasowania)
* **Reguła 2**: Total Amount <= 2000 (brak dopasowania)
* **Reguła 3**: Total Amount <= 3000 (dopasowanie, Return Value = 3)
* **Reguła 4**: Total Amount <= 4000 (dopasowanie, Return Value = 4)
* **Reguła 5**: Total Amount <= 5000 (dopasowanie, Return Value = 5)

Ponieważ stosowana jest polityka **zbierania (suma)**, sumujemy **Return Values** dopasowanych reguł, czyli **3, 4, 5**.

**Zsumowanie tych wartości** daje:

* 5 + 4 + 3 = **12**

Zatem wynikiem zwróconym przez drzewo decyzyjne będzie **12**, czyli suma wszystkich dopasowanych wartości zwracanych.

### **5. Polityka zbierania – min/max/zliczanie (Collect – min/max/count)**

Ta polityka zbiera wszystkie dopasowane reguły i wybiera wartość **minimalną**, **maksymalną** lub **zlicza** wystąpienia. Działa tylko dla **Return Type Value**.

**Przykład:**

| Reguła | Warunek            | Zwracana wartość |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | 1            |
| 2    | Total Amount <= 2000 | 2            |
| 3    | Total Amount <= 3000 | 3            |
| 4    | Total Amount <= 4000 | 4            |
| 5    | Total Amount <= 5000 | 5            |

1. Jeśli wybrana zostanie opcja **Collect (min)**, wynikiem będzie wartość **minimalna** spośród **Return Values** dopasowanych reguł.
   * Dla wartości wejściowej **Total Amount = 3500** ocena reguł wyglądałaby następująco:
     * **Reguła 1**: Total Amount <= 1000 (brak dopasowania)
     * **Reguła 2**: Total Amount <= 2000 (brak dopasowania)
     * **Reguła 3**: Total Amount <= 3000 (dopasowanie, Return Value = 3)
     * **Reguła 4**: Total Amount <= 4000 (dopasowanie, Return Value = 4)
     * **Reguła 5**: Total Amount <= 5000 (dopasowanie, Return Value = 5)
   * **Dopasowane reguły** to Reguła 3, Reguła 4 i Reguła 5, z **Return Values** wynoszącymi **3, 4 i 5**.
   * Ponieważ stosowana jest polityka **Collect (min)**, wynikiem będzie **wartość minimalna**, czyli **3**.
   * **Wynik**: **3**
2. Jeśli wybrana zostanie opcja **Collect (max)**, wynikiem będzie wartość **maksymalna** spośród **Return Values** dopasowanych reguł.
   * Dla tej samej oceny co powyżej wynikiem będzie:
   * **Wynik**: **5**
3. Jeśli wybrana zostanie opcja **Collect (count)**, wynik zliczy **liczbę dopasowanych reguł**.
   * Dla tej samej oceny co powyżej wynikiem będzie:
   * **Wynik**: **3** (ponieważ dopasowano 3 reguły).

### **6. Polityka kolejności reguł (Rule Order)**

Ta polityka stosuje reguły w kolejności, w jakiej pojawiają się w drzewie decyzyjnym, i zwraca wynik reguły, która zostanie dopasowana jako pierwsza.

**Przykład:**

| Reguła | Warunek            | Zwracana grupa |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 3000 | GROUP_3     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 5000 | GROUP_5     |

Zakładając, że wartością wejściową jest **Total Amount = 3500**, ocena reguł wyglądałaby następująco:

* **Reguła 1**: Total Amount <= 1000 (brak dopasowania)
* **Reguła 2**: Total Amount <= 2000 (brak dopasowania)
* **Reguła 3**: Total Amount <= 3000 (dopasowanie)
* **Reguła 4**: Total Amount <= 4000 (dopasowanie)
* **Reguła 5**: Total Amount <= 5000 (dopasowanie)

W ramach polityki **Rule Order** drzewo przetwarza reguły w kolejności, w jakiej są wymienione. Dopasowanymi regułami będą zatem:

* **Reguła 3**: GROUP_3
* **Reguła 4**: GROUP_4
* **Reguła 5**: GROUP_5

**Wynik**: **GROUP_3**, **GROUP_4**, **GROUP_5**

### **7. Polityka dowolnego dopasowania (Any)**

Wiele reguł może być prawdziwych, ale wynik tych reguł musi być taki sam.

**Przykład:**

| Reguła | Warunek            | Zwracana grupa |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 3000 | GROUP_3     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 5000 | GROUP_5     |

Jeśli kwota całkowita wynosi **2500**, ocenione reguły będą następujące:

* **Reguła 1**: Total Amount <= 1000 (brak dopasowania)
* **Reguła 2**: Total Amount <= 2000 (brak dopasowania)
* **Reguła 3**: Total Amount <= 3000 (dopasowanie)
* **Reguła 4**: Total Amount <= 4000 (dopasowanie)
* **Reguła 5**: Total Amount <= 5000 (dopasowanie)

Aby polityka **Any** została zastosowana, wszystkie dopasowane reguły muszą zwracać tę samą **Return Group**. Ponieważ grupy nie są zgodne w poszczególnych regułach, wynikiem będzie **false**.

### **8. Polityka pierwszego i sąsiedniego dopasowania (First & Adjacent)**

Wybiera wynik reguły sąsiadującej z pierwszą regułą, która jest prawdziwa.

**Przykład:**

| Reguła | Warunek            | Zwracana grupa |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 3000 | GROUP_3     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 5000 | GROUP_5     |

Jeśli kwota całkowita wynosi **1500**, ocenione reguły będą następujące:

* **Reguła 1**: Total Amount <= 1000 (brak dopasowania)
* **Reguła 2**: Total Amount <= 2000 (dopasowanie)

Ponieważ **Reguła 2** jest pierwszą regułą, która zostaje dopasowana, polityka **First & Adjacent** zastosowałaby wynik **Reguły 3**: **GROUP_3**.

## **Testowanie drzewa decyzyjnego**

**Przegląd:**
Projektant drzewa decyzyjnego zawiera funkcję testowania, która umożliwia walidację logiki skonfigurowanych reguł. Funkcja ta pozwala użytkownikom przetestować drzewo decyzyjne poprzez podanie określonych wartości wejściowych dla wybranych pól.

**Kroki korzystania z funkcji testowania:**

1.  **Znajdź przycisk Test:**

    * W Projektancie drzewa decyzyjnego znajdź przycisk **Test**.

    <figure><img src="../../../.gitbook/assets/decision_tree_test_button.png" alt="Przycisk Test drzewa decyzyjnego" width="563"><figcaption></figcaption></figure>
2.  **Otwórz okno testowe:**

    * Kliknij przycisk **Test**.
    * Pojawi się okno podręczne z polami wejściowymi odpowiadającymi kryteriom używanym w drzewie decyzyjnym.

    <figure><img src="../../../.gitbook/assets/decision_tree_test_popup.png" alt="Okno testowe drzewa decyzyjnego" width="421"><figcaption></figcaption></figure>
3. **Podaj wartości wejściowe:**
   *   Wprowadź wartości w polach wejściowych, aby zasymulować rzeczywisty scenariusz.

       <figure><img src="../../../.gitbook/assets/decision_tree_test_input.png" alt="Dane wejściowe testu drzewa decyzyjnego" width="428"><figcaption></figcaption></figure>
4.  **Oceń wyniki:**

    * Po wprowadzeniu danych wejściowych drzewo przetwarza je na podstawie wybranej polityki.
    * System wyróżnia regułę (lub reguły), które pasują do podanych danych wejściowych.

    <figure><img src="../../../.gitbook/assets/decision_tree_test_result.png" alt="Wynik testu drzewa decyzyjnego" width="563"><figcaption></figcaption></figure>
5. **Przejrzyj informacje zwrotne w przypadku braku dopasowania:**
   * Jeśli żadna reguła nie zostanie wyróżniona, system wyświetli informację zwrotną wyjaśniającą, dlaczego żadna reguła nie została dopasowana.
   * Skorzystaj z tej informacji zwrotnej, aby dostosować dane wejściowe lub przejrzeć konfigurację drzewa pod kątem potencjalnych problemów.

## Eksport i zapis

* **Save**: zapisuje bieżącą konfigurację drzewa decyzyjnego.
* **Export**: umożliwia wyeksportowanie konfiguracji drzewa decyzyjnego, którą można następnie zaimportować do innego środowiska lub wykorzystać do celów tworzenia kopii zapasowej.

## Przypadki użycia

* **Przepływy zatwierdzania** — kierowanie faktur do różnych osób zatwierdzających na podstawie progów kwotowych (na przykład kwoty powyżej 10 000 wymagają zatwierdzenia przez menedżera).
* **Reguły walidacji** — automatyczna walidacja wartości pól i oznaczanie dokumentów, które nie spełniają skonfigurowanych kryteriów.
* **Przypisywanie sekwencyjne** — przypisywanie dokumentów użytkownikom w określonej kolejności na podstawie warunków.
