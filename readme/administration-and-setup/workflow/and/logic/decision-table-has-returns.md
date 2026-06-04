# Decision Table has Returns

<figure><img src="../../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Cel:**

Ta karta DocBits sprawdza, czy określona tabela decyzyjna ma wartości zwracane dla danego dokumentu, i określa, czy zwrócone dane powinny zostać użyte w kolejnych krokach przepływu pracy. Zapewnia, że przepływy pracy mogą dynamicznie dostosowywać się na podstawie wyników tabeli decyzyjnej.

## **Funkcjonalność:**

* **Walidacja tabeli decyzyjnej:** Ta karta weryfikuje, czy wybrana tabela decyzyjna dostarcza wartości zwracane dla przetwarzanego dokumentu.
* **Wybór tabeli decyzyjnej:** Użytkownicy określają nazwę tabeli decyzyjnej do sprawdzenia.
* **Use Return Data:** Użytkownicy mogą określić, czy użyć danych zwracanych w późniejszych kartach, za pomocą ustawienia **Boolean**:
  * **True:** Dane zwracane są dostępne i zostaną użyte w kolejnych krokach przepływu pracy.
  * **False:** Dane zwracane nie zostaną użyte, a przepływ pracy jest kontynuowany bez nich.

## **Zastosowanie:**

Ta karta jest idealna dla przepływów pracy obejmujących logikę warunkową lub podejmowanie decyzji na podstawie predefiniowanych reguł w tabeli decyzyjnej. Zapewnia bezproblemową integrację wyników tabeli decyzyjnej z procesami przepływu pracy.

## **Przykładowy scenariusz:**

* Użytkownik konfiguruje kartę, aby sprawdzić tabelę decyzyjną **"Invoice Processing Rules"** pod kątem wartości zwracanych. Ustawienie **Boolean** ustawiono na **True**, co wskazuje, że dane zwracane (np. wymagania dotyczące zatwierdzania) zostaną wykorzystane w późniejszych kartach do kierowania decyzjami przepływu pracy.

Korzystając z karty "Decision Table Check", organizacje mogą zwiększyć elastyczność przepływu pracy, usprawnić przetwarzanie oparte na regułach i zapewnić spójność w podejmowaniu decyzji w zautomatyzowanych przepływach pracy.
