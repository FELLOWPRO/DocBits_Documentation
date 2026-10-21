# Przypisany warunek użytkownika

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-3e450ede5dea-pl.png" alt="Pola karty w pokazanej wersji. Pola nie są jeszcze skonfigurowane. Niektóre etykiety tej wersji interfejsu nie są jeszcze przetłumaczone lub mają nieprawidłowe tłumaczenie. Objaśnienia na tej stronie używają właściwych terminów; obraz przedstawia rzeczywisty interfejs." width="563"><figcaption><p>Pola karty w pokazanej wersji. Pola nie są jeszcze skonfigurowane. Niektóre etykiety tej wersji interfejsu nie są jeszcze przetłumaczone lub mają nieprawidłowe tłumaczenie. Objaśnienia na tej stronie używają właściwych terminów; obraz przedstawia rzeczywisty interfejs.</p></figcaption></figure>

**Cel**

Ta karta przepływu pracy zarządza wykonywaniem operacji w zależności od tego, czy zadanie lub dokument jest przypisane do określonego użytkownika lub zestawu użytkowników. Wykorzystuje logikę warunkową, aby wyzwalać lub blokować określone akcje, co czyni ją idealną dla przepływów pracy wymagających obsługi specyficznej dla użytkownika.

**Komponenty karty**

1. **Operatora**
   * **Opis**: Definiuje warunek logiczny stosowany do przypisania użytkownika.
   * **Opcje**:
     * **IS**: Wyzwala operację, jeśli przypisany użytkownik dokumentu lub zadania odpowiada dowolnemu użytkownikowi z określonej listy.
     * **NIE JEST**: Wyzwala operację, jeśli przypisany użytkownik dokumentu lub zadania nie odpowiada żadnemu użytkownikowi z określonej listy.
2. **Lista użytkowników**
   * **Opis**: Lista lub wybór użytkowników do porównania z przypisanym użytkownikiem.
   * **Szczegóły**: Lista ta może zawierać jednego lub wielu użytkowników, umożliwiając karcie skuteczną obsługę zarówno pojedynczych, jak i wielu warunków użytkownika. Wybór można dokonać za pomocą pól wyboru, rozwijanej listy wielokrotnego wyboru lub podobnych elementów interfejsu.

**Funkcjonalność**

* **Identyfikacja przypisania użytkownika**: Automatycznie identyfikuje użytkownika lub użytkowników przypisanych do określonego zadania lub dokumentu w systemie ERP.
* **Ocena warunku**:
  * Przy operatorze **IS** karta sprawdza, czy przypisany użytkownik znajduje się na liście User List.
  * Przy operatorze **NIE JEST** karta zapewnia, że przypisany użytkownik nie znajduje się na liście.
* **Wykonanie akcji**:
  * **Warunek prawdziwy**: Jeśli przypisanie użytkownika spełnia warunek (IS lub IS NOT), wyzwalane są odpowiednie akcje, takie jak powiadomienia, inicjowanie zadań, zatwierdzenia lub inne kroki przepływu pracy.
  * **Warunek fałszywy**: Jeśli warunek nie jest spełniony, przepływ pracy nie będzie kontynuowany.

**Interakcje użytkownika**

* **Konfiguracja**: Użytkownicy konfigurują kartę, wybierając operator i wskazując odpowiednich użytkowników z listy User List. Konfiguracja powinna być przyjazna i intuicyjna, aby uwzględnić wybory z potencjalnie dużych baz użytkowników.
* **Monitorowanie i raportowanie**: System ERP powinien zapewniać funkcjonalność monitorowania i raportowania operacji wyzwalanych przez tę kartę, dostarczając informacji o dokładności przypisań i efektywności procesu.
* **Obsługa błędów i powiadomienia**: Użytkownicy powinni mieć możliwość otrzymywania alertów lub powiadomień w przypadku problemów z przypisaniami, takich jak nieprzypisane zadania lub błędy w wyborze użytkownika.

#### Podsumowanie

Karta przepływu pracy "Assigned User Condition" jest kluczowym narzędziem do zarządzania przepływami pracy dokumentów i zadań zależnymi od przypisań użytkowników. Pozwalając na warunki oparte na tym, czy zadanie lub dokument jest przypisane do określonych użytkowników, zapewnia, że przepływy pracy są wyzwalane tylko przez odpowiednie interakcje użytkowników, zwiększając zarówno odpowiedzialność, jak i dopasowanie zadań w zespołach. Jasne udokumentowanie tej karty pomoże użytkownikom zrozumieć jej znaczenie i skutecznie zintegrować ją z przepływami pracy, zapewniając płynne i wydajne działanie dostosowane do ról i obowiązków użytkowników.

<!-- workflow-card-practical-example-20261021 -->

## Praktyczny przykład

**Kiedy używać:** Kontynuuj tylko wtedy, gdy dokument jest przypisany zatwierdzonemu recenzentowi.

**Konfiguracja:** Wybierz jest-jednym z i skonfigurowanych użytkowników demonstracyjnych `Demo Reviewer A` i `Demo Reviewer B`.

**Oczekiwany wynik i kontrprzykład:** Dokument przypisany do `Demo Reviewer B` przechodzi; przypisany do innego użytkownika kończy się niepowodzeniem.

To jest ilustracyjna konfiguracja i oczekiwany wynik. Korzystaj z pól, użytkowników i grup skonfigurowanych w Twojej organizacji testowej; nie jest to twierdzenie, że ten przykład został wykonany.
