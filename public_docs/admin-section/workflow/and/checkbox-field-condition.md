# Warunek pola wyboru

<figure><img src="../../../.gitbook/assets/userlmn_b689c7ce31284b4635be85f674a90917.png" alt=""><figcaption></figcaption></figure>

**Cel**

Ta karta przepływu pracy została zaprojektowana w celu automatyzacji działań w oparciu o stan (zaznaczony lub odznaczony) pola wyboru w systemie ERP. Poprzez ocenę warunku pola wyboru ułatwia uruchamianie określonych procesów lub egzekwowanie określonych reguł w aplikacji.

**Składniki karty**

1. **Nazwa pola**
* **Opis**: Określa nazwę pola wyboru, które będzie oceniane.
* **Szczegóły**: Powinno to odpowiadać dokładnej etykiecie pola lub identyfikatorowi używanemu w systemie. Określa, które pole wyboru jest monitorowane.
2. **Boolean**
* **Opis**: Określa warunek, który uruchamia przepływ pracy.
* **Opcje**:
* **Prawda**: Przepływ pracy uruchamia się, jeśli pole wyboru jest zaznaczone.
* **Fałsz**: Przepływ pracy uruchamia się, jeśli pole wyboru jest odznaczone.

**Funkcjonalność**

* **Wykrywanie stanu**: Karta ciągle monitoruje stan określonego pola wyboru.
* **Ocena warunku**:
* System sprawdza, czy pole wyboru znajduje się w stanie (zaznaczony lub odznaczony), określonym przez warunek Boolean.
* **Wykonywanie działań**:
* **Warunek Prawdziwy**: Jeśli stan pola wyboru odpowiada określonemu warunkowi Boolean (zarówno prawda dla zaznaczonego, jak i fałsz dla odznaczonego), system inicjuje powiązane działania. Mogą one obejmować włączanie lub wyłączanie pól formularza, uruchamianie powiadomień, rozpoczynanie przepływów pracy lub aktualizowanie rekordów.
* **Warunek Fałszywy**: Jeśli stan pola wyboru nie zgadza się z warunkiem, mogą zostać podjęte alternatywne lub brak działań, w zależności od konfiguracji przepływu pracy.

**Interakcje użytkownika**

* **Konfiguracja i ustawienia**: Użytkownicy konfigurują kartę, wybierając pole wyboru z listy dostępnych pól i ustawiając warunek Boolean. Proces konfiguracji powinien być intuicyjny, zazwyczaj obejmujący prosty rozwijany menu do wyboru pola i przełącznik do warunku Boolean.
* **Monitorowanie i raportowanie**: Zapewnia funkcje monitorowania statusu tego warunku, być może poprzez panel, który pokazuje aktualizacje na żywo dotyczące aktywnych lub uruchomionych warunków.
* **Obsługa błędów i powiadomienia**: Zapewnia, że użytkownicy zostaną poinformowani o wszelkich niezgodnościach lub błędach w procesie sprawdzania warunków, takich jak awarie systemu w odczycie stanu pola wyboru.

#### Podsumowanie

Karta przepływu pracy "Warunek pola wyboru" jest podstawowym narzędziem do zarządzania dynamicznymi formularzami i dokumentami w systemie ERP, gdzie dane wprowadzone przez użytkownika mogą dyktować kolejne procesy danych. Poprzez automatyzację działań w oparciu o stan pola wyboru, ta karta zwiększa efektywność przepływu pracy i zapewnia, że zachowania systemu są zgodne z danymi wprowadzanymi przez użytkownika. Jasna dokumentacja tej karty pomoże użytkownikom skutecznie ją wdrożyć w swoich operacjach, umożliwiając lepszą kontrolę nad zachowaniami formularzy i automatyzacją procesów.
