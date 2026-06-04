# Single Assigned User Condition

<figure><img src="../../../../.gitbook/assets/userlmn_77e991cee96598023f9a3ac7ad230e50.png" alt=""><figcaption></figcaption></figure>

**Cel**

Ta karta przepływu pracy umożliwia wykonywanie operacji na podstawie przypisania zadania lub dokumentu do pojedynczego, konkretnego użytkownika. Wykorzystując bezpośrednie podejście oparte na logice warunkowej, zarządza przepływami pracy wymagającymi ukierunkowanego zaangażowania użytkownika, zapewniając precyzję w obsłudze zadań opartych na użytkowniku.

**Komponenty karty**

1. **Operator**
   * **Opis**: Określa logikę stosowaną do przypisania użytkownika.
   * **Opcje**:
     * **IS**: Wyzwala operację, jeśli przypisany użytkownik dokumentu lub zadania odpowiada określonemu użytkownikowi.
     * **IS NOT**: Wyzwala operację, jeśli przypisany użytkownik nie odpowiada określonemu użytkownikowi.
2. **User**
   * **Opis**: Umożliwia wybór pojedynczego użytkownika, z którym porównywany będzie przypisany użytkownik.
   * **Szczegóły**: Obejmuje to proste pole rozwijane lub z autouzupełnianiem, w którym można wybrać jednego użytkownika naraz.

**Funkcjonalność**

* **Identyfikacja przypisania użytkownika**: Identyfikuje użytkownika aktualnie przypisanego do określonego zadania lub dokumentu.
* **Ocena warunku**:
  * Dla operatora **IS** karta sprawdza, czy przypisany użytkownik jest taki sam jak wybrany użytkownik.
  * Dla operatora **IS NOT** weryfikuje, czy przypisany użytkownik jest inny niż wybrany użytkownik.
* **Wykonanie akcji**:
  * **Warunek prawdziwy**: Jeśli przypisanie spełnia ustawiony warunek (IS lub IS NOT), wyzwala predefiniowane akcje, które mogą obejmować dalsze zatwierdzenia, inicjowanie kolejnych zadań, wysyłanie powiadomień lub inne powiązane przepływy pracy.
  * **Warunek fałszywy**: Jeśli warunek nie jest spełniony, system może przekierować zadanie, wstrzymać je do przeglądu lub wyzwolić alternatywne predefiniowane akcje.

**Interakcje użytkownika**

* **Konfiguracja**: Użytkownicy konfigurują kartę, wybierając operator i wskazując użytkownika w polu użytkownika. Konfiguracja powinna być prosta, zapewniając łatwy wybór użytkownika i konfigurację.
* **Monitorowanie i raportowanie**: Oferuje narzędzia do monitorowania działania karty, takie jak śledzenie, które zadania są wyzwalane przez określone przypisania użytkowników, oraz wyników tych wyzwalaczy.
* **Obsługa błędów i powiadomienia**: Zapewnia mechanizmy ostrzegania użytkowników, jeśli zadania zostaną nieprawidłowo przypisane lub jeśli wystąpią błędy operacyjne z powodu problemów z przypisaniem.

#### Podsumowanie

Karta przepływu pracy "Single Assigned User Condition" jest niezbędna do precyzyjnego, specyficznego dla użytkownika zarządzania dokumentami i zadaniami w systemie ERP. Upraszcza przepływy pracy, koncentrując się na przypisaniach indywidualnych użytkowników, zapewniając tym samym, że akcje są wykonywane tylko wtedy, gdy jest to właściwe, na podstawie roli i obowiązków użytkownika. Jasne udokumentowanie tej karty pomoże użytkownikom zrozumieć jej zastosowanie, umożliwiając im skuteczne wdrożenie i zarządzanie nią w codziennych operacjach. Dokumentacja ta zapewnia, że wszyscy potencjalni użytkownicy mogą łatwo zrozumieć cel karty i bezproblemowo zintegrować ją z przepływami pracy.
