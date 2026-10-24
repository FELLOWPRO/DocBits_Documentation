# Tabela decyzyjna zwraca wyniki

<figure><img src="../../../../.gitbook/assets/workflow_card_condition_decision_tree_data_v2-pl-pl.png" alt="Tabela decyzyjna zwraca wyniki, Wersja 2" width="634"><figcaption><p>Wersja 2</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/workflow_card_condition_decision_tree_data_v3-pl-pl.png" alt="Tabela decyzyjna zwraca wyniki, Wersja 3" width="634"><figcaption><p>Wersja 3</p></figcaption></figure>

## **Cel:**

Ta karta DocBits sprawdza, czy określona tabela decyzyjna ma wartości zwracane dla danego dokumentu, i określa, czy zwrócone dane powinny zostać użyte w kolejnych krokach przepływu pracy. Zapewnia, że przepływy pracy mogą dynamicznie dostosowywać się na podstawie wyników tabeli decyzyjnej.

## **Funkcjonalność:**

* **Walidacja tabeli decyzyjnej:** Ta karta weryfikuje, czy wybrana tabela decyzyjna dostarcza wartości zwracane dla przetwarzanego dokumentu.
* **Wybór tabeli decyzyjnej:** Użytkownicy określają nazwę tabeli decyzyjnej do sprawdzenia.
* **Użyj danych zwrotnych:** Użytkownicy mogą określić, czy użyć danych zwracanych w późniejszych kartach, za pomocą ustawienia **Wartość logiczna**:
  * **True:** Dane zwracane są dostępne i zostaną użyte w kolejnych krokach przepływu pracy.
  * **False:** Dane zwracane nie zostaną użyte, a przepływ pracy jest kontynuowany bez nich.

## **Zastosowanie:**

Ta karta jest idealna dla przepływów pracy obejmujących logikę warunkową lub podejmowanie decyzji na podstawie predefiniowanych reguł w tabeli decyzyjnej. Zapewnia bezproblemową integrację wyników tabeli decyzyjnej z procesami przepływu pracy.

## **Przykładowy scenariusz:**

* Użytkownik konfiguruje kartę, aby sprawdzić tabelę decyzyjną **„Zasady przetwarzania faktur”** pod kątem wartości zwracanych. Ustawienie **Wartość logiczna** ustawiono na **True**, co wskazuje, że dane zwracane (np. wymagania dotyczące zatwierdzania) zostaną wykorzystane w późniejszych kartach do kierowania decyzjami przepływu pracy.

Korzystając z karty "Decision Table Check", organizacje mogą zwiększyć elastyczność przepływu pracy, usprawnić przetwarzanie oparte na regułach i zapewnić spójność w podejmowaniu decyzji w zautomatyzowanych przepływach pracy.
