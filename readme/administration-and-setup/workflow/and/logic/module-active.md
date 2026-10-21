# Moduł aktywny

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-405c9bb87c62-pl.png" alt="Pola karty w pokazanej wersji. Pola nie są jeszcze skonfigurowane." width="563"><figcaption><p>Pola karty w pokazanej wersji. Pola nie są jeszcze skonfigurowane.</p></figcaption></figure>

## **Cel:**

Ta karta DocBits sprawdza, czy określony moduł w systemie jest aktywny, czy nieaktywny. Umożliwia przepływom pracy kontynuowanie na podstawie statusu aktywacji modułu, zapewniając, że akcje są wykonywane tylko wtedy, gdy niezbędny moduł jest dostępny.

## **Funkcjonalność:**

* **Walidacja statusu modułu:** Ta karta weryfikuje status aktywacji określonego modułu i ocenia go względem warunku zdefiniowanego przez użytkownika.
* **Wybór modułu:** Użytkownicy określają nazwę modułu do sprawdzenia, zapewniając precyzyjną walidację.
* **Operatorzy:** Można zastosować następujące warunki:
  * **Is:** Przepływ pracy jest kontynuowany, jeśli wybrany moduł jest aktywny.
  * **Nie jest:** Przepływ pracy jest kontynuowany, jeśli wybrany moduł jest nieaktywny.

## **Zastosowanie:**

Ta karta jest szczególnie przydatna dla administratorów lub menedżerów systemu, którzy muszą tworzyć przepływy pracy zależne od dostępności lub funkcjonalności określonych modułów. Pomaga zapewnić, że przepływy pracy są wykonywane tylko wtedy, gdy wszystkie wymagane moduły są odpowiednio skonfigurowane.

## **Przykładowy scenariusz**

* Użytkownik konfiguruje kartę, aby sprawdzić, czy moduł **„Przetwarzanie dokumentów”** **jest aktywny.** Jeśli moduł jest aktywny, przepływ pracy jest kontynuowany, wyzwalając zautomatyzowane zadania przetwarzania dokumentów. Jeśli moduł jest nieaktywny, przepływ pracy zostaje zatrzymany, zapobiegając niepotrzebnym akcjom.

Korzystając z karty "Module Active Check", organizacje mogą poprawić niezawodność przepływu pracy, uniknąć błędów spowodowanych nieaktywnymi modułami i zapewnić zgodność procesów z konfiguracją systemu.
