# Checkbox Field Condition

<figure><img src="../../../../.gitbook/assets/userlmn_b689c7ce31284b4635be85f674a90917.png" alt=""><figcaption></figcaption></figure>

**Cel**

Ta karta przepływu pracy służy do automatyzacji akcji na podstawie stanu (zaznaczone lub niezaznaczone) pola wyboru w systemie ERP. Oceniając stan pola wyboru, ułatwia wyzwalanie określonych procesów lub egzekwowanie określonych reguł w aplikacji.

**Komponenty karty**

1. **Field Name**
   * **Opis**: Określa nazwę pola wyboru, które będzie oceniane.
   * **Szczegóły**: Powinna ona odpowiadać dokładnej etykiecie lub identyfikatorowi pola używanemu w systemie. Określa, którego pola wyboru stan jest monitorowany.
2. **Boolean**
   * **Opis**: Definiuje warunek wyzwalający przepływ pracy.
   * **Opcje**:
     * **True**: Przepływ pracy jest wyzwalany, jeśli pole wyboru jest zaznaczone.
     * **False**: Przepływ pracy jest wyzwalany, jeśli pole wyboru jest niezaznaczone.

**Funkcjonalność**

* **Wykrywanie stanu**: Karta na bieżąco monitoruje stan określonego pola wyboru.
* **Ocena warunku**:
  * System sprawdza, czy pole wyboru znajduje się w stanie (zaznaczone lub niezaznaczone) określonym przez warunek Boolean.
* **Wykonanie akcji**:
  * **Warunek prawdziwy**: Jeśli stan pola wyboru odpowiada określonemu warunkowi Boolean (true dla zaznaczonego lub false dla niezaznaczonego), system inicjuje powiązane akcje. Mogą one obejmować włączanie lub wyłączanie pól formularza, wyzwalanie powiadomień, uruchamianie przepływów pracy lub aktualizację rekordów.
  * **Warunek fałszywy**: Jeśli stan pola wyboru nie odpowiada warunkowi, mogą zostać podjęte alternatywne akcje lub żadne, w zależności od konfiguracji przepływu pracy.

**Interakcje użytkownika**

* **Konfiguracja**: Użytkownicy konfigurują kartę, wybierając pole wyboru z listy dostępnych pól i ustawiając warunek Boolean. Proces konfiguracji powinien być intuicyjny, zazwyczaj obejmując proste menu rozwijane do wyboru pola i przełącznik dla warunku Boolean.
* **Monitorowanie i raportowanie**: Zapewnia użytkownikom funkcjonalność monitorowania stanu tego warunku, możliwie za pośrednictwem pulpitu pokazującego aktualizacje w czasie rzeczywistym dotyczące tego, które warunki są aktywne lub wyzwolone.
* **Obsługa błędów i powiadomienia**: Zapewnia, że użytkownicy są powiadamiani o wszelkich rozbieżnościach lub błędach w procesie sprawdzania warunku, takich jak awarie systemu w odczycie stanu pola wyboru.

#### Podsumowanie

Karta przepływu pracy "Checkbox Field Condition" jest podstawowym narzędziem do zarządzania dynamicznymi formularzami i dokumentami w systemie ERP, gdzie dane wprowadzane przez użytkownika mogą dyktować kolejne procesy danych. Automatyzując akcje na podstawie stanu pola wyboru, karta ta zwiększa efektywność przepływu pracy i zapewnia, że zachowania systemu są zgodne z danymi wprowadzanymi przez użytkownika. Jasna dokumentacja tej karty pomoże użytkownikom skutecznie wdrożyć ją w swoich operacjach, umożliwiając lepszą kontrolę nad zachowaniami formularzy i automatyzacją procesów.
