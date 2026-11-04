# Warunek Przypisanego Użytkownika

<figure><img src="../../../.gitbook/assets/userlmn_5e16e9b23626ec1211c753fec5333513.png" alt=""><figcaption></figcaption></figure>

**Cel**

Ta karta workflow zarządza wykonaniem operacji w zależności od tego, czy zadanie lub dokument jest przypisane do określonego użytkownika lub zestawu użytkowników. Wykorzystuje logikę warunkową do wyzwalania lub zapobiegania określonym działaniom, co czyni ją idealną do zastosowań, które wymagają obsługi związanej z użytkownikiem.

**Składniki Karty**

1. **Operator**
* **Opis**: Określa warunek logiczny do zastosowania w przypisaniu użytkownika.
* **Opcje**:
* **IS**: Wywołuje operację, jeśli przypisany użytkownik dokumentu lub zadania pasuje do któregokolwiek użytkownika na określonej liście.
* **IS NOT**: Wywołuje operację, jeśli przypisany użytkownik dokumentu lub zadania nie pasuje do żadnego użytkownika na określonej liście.
2. **Lista Użytkowników**
* **Opis**: Lista lub wybór użytkowników do porównania z przypisanym użytkownikiem.
* **Szczegóły**: Ta lista może zawierać jednego lub wielu użytkowników, umożliwiając karcie skuteczne obsługiwanie warunków pojedynczego lub wielu użytkowników. Wybór można dokonać za pomocą pól wyboru, rozwijanej listy wielokrotnego wyboru lub podobnych elementów interfejsu użytkownika.

**Funkcjonalność**

* **Identyfikacja Przypisania Użytkownika**: Automatycznie identyfikuje użytkownika lub użytkowników przypisanych do określonego zadania lub dokumentu w systemie ERP.
* **Ocena Warunku**:
* Korzystając z operatora **IS**, karta sprawdza, czy przypisany użytkownik znajduje się na liście użytkowników.
* Korzystając z operatora **IS NOT**, karta zapewnia, że przypisany użytkownik nie znajduje się na liście.
* **Wykonanie Działania**:
* **Warunek Prawdziwy**: Jeśli przypisanie użytkownika spełnia warunek (IS lub IS NOT), wyzwalane są odpowiednie działania, takie jak powiadomienia, inicjacje zadań, zatwierdzenia lub inne kroki workflow.
* **Warunek Fałszywy**: Jeśli warunek nie jest spełniony, dokument lub zadanie może przejść przez inne trasy, a mogą być określone alternatywne działania.

**Interakcje Użytkownika**

* **Konfiguracja i Ustawienia**: Użytkownicy konfigurują kartę, wybierając operatora i określając odpowiednich użytkowników z listy użytkowników. Konfiguracja powinna być przyjazna dla użytkownika i intuicyjna, aby umożliwić wybór spośród potencjalnie dużych baz użytkowników.
* **Monitorowanie i Raportowanie**: System ERP powinien zapewniać funkcjonalność monitorowania i raportowania operacji wywołanych przez tę kartę, oferując wgląd w dokładność przypisania i efektywność procesu.
* **Obsługa Błędów i Powiadomienia**: Użytkownicy powinni mieć możliwość otrzymywania alertów lub powiadomień w przypadku problemów z przypisaniem, takich jak zadania bez przypisania lub błędy w wyborze użytkownika.

#### Podsumowanie

Karta workflow "Warunek Przypisanego Użytkownika" jest kluczowym narzędziem do zarządzania workflow dokumentów i zadań, które zależą od przypisania użytkowników. Poprzez umożliwienie warunków opartych na tym, czy zadanie lub dokument jest przypisane do konkretnych użytkowników, zapewnia, że workflow są wyzwalane tylko przez odpowiednie interakcje użytkowników, zwiększając zarówno odpowiedzialność, jak i dopasowanie zadań w zespołach. Dokumentowanie tej karty w sposób jasny pomoże użytkownikom zrozumieć jej znaczenie i skutecznie ją zintegrować z ich workflow, zapewniając płynne i efektywne operacje dostosowane do ról i obowiązków użytkowników.
