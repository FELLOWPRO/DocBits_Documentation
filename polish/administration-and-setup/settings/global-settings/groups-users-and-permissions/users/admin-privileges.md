# Uprawnienia administratora

Rola administratora jest kluczowa w zarządzaniu systemami IT, sieciami i platformami cyfrowymi w organizacji. Administrator ma zaawansowane uprawnienia i odpowiedzialności, które pozwalają mu kontrolować różne aspekty infrastruktury technicznej oraz zapewnić jej efektywne i bezpieczne działanie. Oto niektóre z głównych zadań administratora:

* **Zarządzanie użytkownikami:** Administratorzy zarządzają kontami użytkowników, prawami dostępu i uprawnieniami. Tworzą nowe konta użytkowników, przydzielają im niezbędne uprawnienia i zarządzają kontrolą dostępu, aby zapewnić, że tylko uprawnieni użytkownicy mogą uzyskać dostęp do określonych zasobów.
* **Bezpieczeństwo:** Administratorzy są odpowiedzialni za bezpieczeństwo systemów IT, aby chronić je przed utratą danych i nieautoryzowanym dostępem.
* **Rozwiązywanie problemów i wsparcie:** Administrator jest często pierwszym punktem kontaktu w przypadku problemów technicznych. Pomaga użytkownikom rozwiązywać problemy i dba o to, aby system działał sprawnie.

Oprócz tych zadań administratorzy zajmują się również zarządzaniem wrażliwymi ustawieniami oraz zapewnieniem, że systemy spełniają wymagania zgodności i najlepsze praktyki w zakresie bezpieczeństwa informacji. Obejmuje to zarządzanie danymi wrażliwymi, konfigurowanie kontroli dostępu i uprawnień oraz monitorowanie i analizowanie dzienników systemowych w celu identyfikacji i usunięcia potencjalnych zagrożeń bezpieczeństwa.

## Admin vs System Admin

DocBits ma dwie role administratora: **Admin** i **System Admin**. Brzmią podobnie, ale pełnią różne zadania. Oto prosta wersja.

### Admin — osoba, która zarządza Twoją organizacją

**Admin** to prawdziwa osoba z Twojego zespołu, która ma prawo zarządzać DocBits. Administratorzy mogą:

* Otwierać wszystkie obszary **Ustawień** i zmieniać sposób działania Twojej organizacji.
* Dodawać nowych użytkowników, edytować ich, włączać lub wyłączać, a także decydować, kto jeszcze zostanie Adminem.
* Konfigurować grupy, uprawnienia, integracje i przepływy pracy.

Możesz mieć **tylu Adminów, ilu potrzebujesz**, i w dowolnym momencie nadać lub odebrać rolę Admina dowolnemu użytkownikowi. Większość administratorów w Twoim zespole należy właśnie do tego typu.

### System Admin — konto, którego DocBits używa do samodzielnej pracy

**System Admin** to **jedno specjalne konto w organizacji**, którego DocBits używa do działań wykonywanych **automatycznie, bez klikania czegokolwiek przez kogoś** — na przykład gdy dokumenty są importowane z poczty e-mail, eksportowane do innego systemu lub przekazywane w tle przez połączoną usługę.

Możesz traktować je jako „robocze” konto organizacji. Gdy system robi coś samodzielnie, robi to **jako System Admin**, dzięki czemu taka automatyczna aktywność jest łatwa do rozpoznania i nie miesza się z pracą Twoich rzeczywistych członków zespołu.

System Admin jest wyjątkowy pod trzema względami:

* **Zawsze jest też Adminem.** Wybranie System Admin automatycznie nadaje temu kontu również pełne uprawnienia Admin.
* **Może być tylko jeden w organizacji.** Gdy System Admin już istnieje, nie możesz oznaczyć kolejnego użytkownika jako System Admin.
* **Ustawia się go wyłącznie przy tworzeniu użytkownika.** Decydujesz o tym w momencie dodawania użytkownika. **Nie da się tego włączyć ani wyłączyć później.**

> **Zalecenie:** Utwórz w tym celu dedykowane konto — na przykład `system@your-company.com` — i oznacz je jako System Admin. Dzięki temu wszystko, co DocBits robi automatycznie, będzie wyraźnie widoczne w dziennikach i historii dokumentów jako działanie **System Admin**, oddzielnie od Twoich rzeczywistych użytkowników.

### W skrócie

| | Admin | System Admin |
|---|---|---|
| Pełny dostęp do zarządzania organizacją | Tak | Tak |
| Ilu można mieć | Tylu, ilu potrzeba | Tylko jeden |
| Można zmienić po utworzeniu użytkownika | Tak, w dowolnej chwili | Nie, ustawiane tylko przy tworzeniu |
| Używany do automatycznych działań w tle | Nie | Tak |
| Zawsze posiada uprawnienia Admin | — | Tak |

## Najlepsze praktyki w zakresie bezpieczeństwa

Bezpieczeństwo jest istotnym aspektem każdej organizacji, szczególnie w kontekście zarządzania kontami użytkowników i prawami dostępu. Oto kilka najlepszych praktyk, aby utrzymać bezpieczny protokół zarządzania użytkownikami:

* **Regularne aktualizacje haseł:** Zachęcaj użytkowników do regularnej aktualizacji haseł, aby utrzymać bezpieczeństwo ich kont. Ustal polityki złożoności haseł i wymagaj używania silnych haseł, które zawierają kombinację liter, cyfr i znaków specjalnych.
* **Monitorowanie działań administratorów:** Wprowadź mechanizmy monitorowania działań administratorów, aby wykrywać podejrzaną lub nietypową aktywność. Rejestruj wszystkie działania administratorów, w tym dostęp do wrażliwych danych lub ustawień, aby zapewnić rozliczalność i zidentyfikować potencjalne naruszenia bezpieczeństwa.
* **Ograniczenie liczby administratorów:** Zmniejsz liczbę administratorów do minimum i przyznawaj uprawnienia administracyjne tylko tym, którzy naprawdę ich potrzebują. Ograniczając liczbę administratorów, minimalizujesz ryzyko naruszeń bezpieczeństwa i ułatwiasz zarządzanie oraz monitorowanie kont użytkowników.
* **Uwierzytelnianie dwuskładnikowe (2FA):** Wdróż uwierzytelnianie dwuskładnikowe dla kont administratorów, aby dodatkowo zwiększyć bezpieczeństwo. Wprowadza ono dodatkowy krok zabezpieczający, który gwarantuje, że nawet w przypadku przejęcia hasła osoba atakująca nie uzyska nieautoryzowanego dostępu do konta.
* **Regularne przeglądy bezpieczeństwa:** Przeprowadzaj regularne przeglądy bezpieczeństwa i audyty, aby zidentyfikować i usunąć potencjalne luki w zabezpieczeniach lub słabe punkty. Sprawdzaj prawa dostępu i uprawnienia kont użytkowników, aby upewnić się, że odpowiadają one aktualnym wymaganiom i najlepszym praktykom.
* **Szkolenie i świadomość:** Regularnie szkol pracowników i administratorów w zakresie najlepszych praktyk bezpieczeństwa oraz świadomości ataków phishingowych i innych zagrożeń cybernetycznych. Uświadamiaj im znaczenie bezpieczeństwa i zachęcaj do zgłaszania podejrzanej aktywności.

Wdrażając te najlepsze praktyki, organizacje mogą poprawić bezpieczeństwo swojego protokołu zarządzania użytkownikami i zminimalizować ryzyko naruszeń bezpieczeństwa oraz utraty danych. Ważne jest, aby postrzegać bezpieczeństwo jako proces ciągły i regularnie wprowadzać aktualizacje oraz dostosowania, by nadążać za nieustannie zmieniającymi się zagrożeniami i wymaganiami bezpieczeństwa.
