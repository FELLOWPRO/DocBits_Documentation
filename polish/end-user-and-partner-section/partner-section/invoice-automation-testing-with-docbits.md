# Automatyzacja Testów Faktur z DocBits

## Przegląd

Dokument ten przedstawia plan testów automatyzacji faktur przy użyciu DocBits z Infor LN lub M3. Zawiera szczegóły dotyczące przypadków testowych, przygotowania do testów, kroków wykonawczych oraz procesów wsparcia.

## Przypadki Testowe

| ID | Przypadek Testowy                                                                  | Opis                                                                                                                                                                                        | Status            |
| -- | ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| 1  | Faktury kosztowe                                                                   | Faktury bez zamówienia zakupu są pomyślnie przetwarzane w DocBits i eksportowane do LN jako „faktura kosztowa”.                                                                             | DO PRZETESTOWANIA |
| 2  | Faktura związana z zamówieniem zakupu z idealnym dopasowaniem                      | Faktury związane z zamówieniem zakupu są pomyślnie przetwarzane w DocBits z idealnym dopasowaniem od faktury do zamówienia, ponieważ numer artykułu, ilość i cena jednostkowa się zgadzają. | DO PRZETESTOWANIA |
| 3  | Faktury związane z zamówieniem zakupu z różną ilością                              | Faktury związane z zamówieniem zakupu są przetwarzane w DocBits, ale w module dopasowywania zamówień mamy niezgodność co do ilości.                                                         | DO PRZETESTOWANIA |
| 4  | Faktury związane z zamówieniem zakupu z różną ceną jednostkową                     | Faktury związane z zamówieniem zakupu są przetwarzane w DocBits, ale w module dopasowywania zamówień mamy niezgodność co do ceny jednostkowej.                                              | DO PRZETESTOWANIA |
| 5  | Faktury związane z zamówieniem zakupu z różnym lub nieistniejącym numerem artykułu | Faktury związane z zamówieniem zakupu są przetwarzane w DocBits, ale w module dopasowywania zamówień mamy niezgodność lub nieistniejący numer artykułu.                                     | DO PRZETESTOWANIA |
| 6  | Faktury związane z zamówieniem zakupu z niezgodnością w tolerancji                 | Faktury związane z zamówieniem zakupu są przetwarzane w DocBits, ale w module dopasowywania zamówień mamy niezgodność co do ilości lub ceny jednostkowej, ale jest to w tolerancji.         | DO PRZETESTOWANIA |
| 7  | Noty kredytowe                                                                     | Noty kredytowe są pomyślnie przetwarzane w DocBits i eksportowane do LN. Wyjaśnij, czy kwoty powinny być eksportowane z dodatnim czy ujemnym znakiem.                                       | DO PRZETESTOWANIA |

## Plan Testów z Klientem

### 1. Ustawienia

* **Spotkanie Wstępne**: Zaplanuj spotkanie inauguracyjne z klientem, aby wyjaśnić proces testowania i cele.
* **Dostęp i Uprawnienia**: Upewnij się, że klient ma wszelkie niezbędne uprawnienia do DocBits i Infor LN lub M3 w celach testowych.

### 2. Przygotowanie do Testów

* **Szkolenie**: Zapewnij kompleksowe szkolenie dla zespołu klienta na temat korzystania z DocBits do przetwarzania faktur.
* **Dokumentacja**: Udostępnij szczegółową dokumentację na temat procedur testowych, w tym oczekiwanych wyników dla każdego przypadku testowego.

### 3. Wykonanie Przypadków Testowych

* **Środowisko Testowe**: Ustaw środowisko testowe, które jak najbliżej odwzorowuje system produkcyjny klienta.
* **Testowanie Krok po Kroku**: Współpracuj z klientem, aby wykonać każdy przypadek testowy, upewniając się, że rozumieją każdy krok:
  * Przetwarzaj faktury przez DocBits.
  * Weryfikuj wyniki w module dopasowywania zamówień.
  * Sprawdź wyniki eksportu w LN lub M3.

### 4. Rozwiązywanie Problemów

* **Śledzenie**: Użyj systemu śledzenia (takiego jak Jira lub prosty arkusz kalkulacyjny), aby rejestrować wszelkie problemy lub niezgodności, które wystąpią podczas testowania.
* **Wsparcie**: Zapewnij natychmiastowe wsparcie w celu rozwiązania problemów i wyjaśnienia wszelkich wątpliwości.

### 5. Weryfikacja i Informacja Zwrotna

* **Weryfikacja**: Po każdym przypadku testowym zweryfikuj wyniki z klientem, aby zapewnić dokładność.
* **Pętla Informacji Zwrotnej**: Zbieraj opinie od klienta na temat procesu i wszelkich potrzebnych ulepszeń.

### 6. Finalizacja

* **Dokumentacja Wyników**: Udokumentuj wyniki każdego przypadku testowego i przygotuj raport podsumowujący dla klienta.
* **Spotkanie Przeglądowe**: Przeprowadź spotkanie przeglądowe, aby omówić wyniki testów i wszelkie dalsze kroki wymagane przed uruchomieniem.

### 7. Przygotowanie do Uruchomienia

* **Odświeżenie Szkolenia**: Oferuj sesję odświeżającą szkolenie, jeśli to konieczne.
* **Plan Wsparcia**: Opracuj plan wsparcia na początkowy etap uruchomienia, aby zapewnić płynne przejście.
