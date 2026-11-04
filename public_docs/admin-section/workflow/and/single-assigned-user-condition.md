# Warunek pojedynczego przypisanego użytkownika

<figure><img src="../../../.gitbook/assets/userlmn_77e991cee96598023f9a3ac7ad230e50.png" alt=""><figcaption></figcaption></figure>

**Cel**

Ta karta workflow ułatwia operacje oparte na przypisaniu zadania lub dokumentu do jednego określonego użytkownika. Korzystając z bezpośredniego podejścia logicznego warunkowego, zarządza workflow, które wymagają zaangażowania konkretnego użytkownika, zapewniając precyzję w obsłudze zadań opartych na użytkowniku.

**Składniki karty**

1. **Operator**
* **Opis**: Określa logikę do zastosowania w przypisaniu użytkownika.
* **Opcje**:
* **IS**: Wywołuje operację, jeśli przypisany użytkownik dokumentu lub zadania odpowiada określonemu użytkownikowi.
* **IS NOT**: Wywołuje operację, jeśli przypisany użytkownik nie odpowiada określonemu użytkownikowi.
2. **Użytkownik**
* **Opis**: Umożliwia wybór jednego użytkownika, z którym zostanie porównany przypisany użytkownik.
* **Szczegóły**: Obejmuje prosty rozwijany lub pole autouzupełniania, w którym można wybrać jednego użytkownika na raz.

**Funkcjonalność**

* **Identyfikacja przypisania użytkownika**: Identyfikuje użytkownika obecnie przypisanego do określonego zadania lub dokumentu.
* **Ocena warunku**:
* Dla operatora **IS**, karta sprawdza, czy przypisany użytkownik jest taki sam jak wybrany użytkownik.
* Dla operatora **IS NOT**, weryfikuje, czy przypisany użytkownik różni się od wybranego użytkownika.
* **Wykonanie działania**:
* **Warunek prawdziwy**: Jeśli przypisanie spełnia określony warunek (IS lub IS NOT), wywołuje zdefiniowane wcześniej działania, które mogą obejmować kontynuację zatwierdzeń, inicjowanie dalszych zadań, wysyłanie powiadomień lub inne powiązane workflowy.
* **Warunek fałszywy**: Jeśli warunek nie jest spełniony, system może przekierować zadanie, zatrzymać je do przeglądu lub wywołać alternatywne zdefiniowane działania.

**Interakcje użytkownika**

* **Konfiguracja i ustawienia**: Użytkownicy konfigurują kartę, wybierając operatora i wybierając użytkownika z pola użytkownika. Konfiguracja ta powinna być prosta, zapewniając łatwe wybieranie użytkownika i konfigurację.
* **Monitorowanie i raportowanie**: Oferuje narzędzia do monitorowania wydajności karty, takie jak śledzenie zadań wywołanych przez konkretne przypisania użytkowników i wyniki tych wyzwalaczy.
* **Obsługa błędów i powiadomienia**: Zapewnia mechanizmy do powiadamiania użytkowników, jeśli zadania są nieprawidłowo przypisane lub jeśli występują błędy operacyjne z powodu problemów z przypisaniem.

#### Podsumowanie

Karta workflow "Warunek pojedynczego przypisanego użytkownika" jest niezbędna do precyzyjnego zarządzania dokumentami i zadaniami związanymi z użytkownikiem w systemie ERP. Uprości workflowy, skupiając się na indywidualnych przypisaniach użytkowników, zapewniając tym samym, że działania są wykonywane tylko w odpowiednich przypadkach, na podstawie roli i obowiązków użytkownika. Dokumentacja tej karty w sposób jasny pomoże użytkownikom zrozumieć jej zastosowanie, umożliwiając im skuteczne wdrożenie i zarządzanie nią w codziennej pracy. Ta dokumentacja zapewnia, że wszyscy potencjalni użytkownicy mogą łatwo zrozumieć cel karty i bezproblemowo ją zintegrować z ich workflowami.
