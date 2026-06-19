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

* [Polityka unikalności (Unique)](decision-trees/unique-policy.md)
* [Polityka pierwszego dopasowania (First)](decision-trees/first-policy.md)
* [Polityka priorytetu (Priority)](decision-trees/priority-policy.md)
* [Polityka zbierania – suma (Collect – sum)](decision-trees/collect-sum-policy.md)
* [Polityka zbierania – min/max/zliczanie (Collect – min/max/count)](decision-trees/collect-min-max-count-policy.md)
* [Polityka kolejności reguł (Rule Order)](decision-trees/rule-order-policy.md)
* [Polityka dowolnego dopasowania (Any)](decision-trees/any-policy.md)
* [Polityka pierwszego i sąsiedniego dopasowania (First & Adjacent)](decision-trees/first-and-adjacent-policy.md)

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
