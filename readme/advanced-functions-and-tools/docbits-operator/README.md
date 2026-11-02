# Operator DocBits

DocBits Operator wykonuje zadania na podstawie poleceń użytkownika. Polecenie opisuje kolejne kroki, a zmienne pozwalają uzupełnić dane potrzebne do danego uruchomienia.

## Włączenie i dostęp

1. Otwórz **Ustawienia**, a następnie **Moduł → Integracja dokumentów**.
2. Przewiń do ustawienia **DocBits Operator** i włącz tę funkcję, jeśli masz odpowiednie uprawnienia.
3. Otwórz **Operator DocBits** z głównej nawigacji aplikacji.

<figure><img src="../../.gitbook/assets/site-extra-modules-document-integration-pl.png" alt="Moduły integracji dokumentów: skrypty, skanowanie, kody kreskowe i niestandardowe dane podstawowe. W przedstawionej wersji etykieta wyboru kodów kreskowych „Select” pozostaje angielska."><figcaption><p>Moduły integracji dokumentów: skrypty, skanowanie, kody kreskowe i niestandardowe dane podstawowe. W przedstawionej wersji etykieta wyboru kodów kreskowych „Select” pozostaje angielska.</p></figcaption></figure>

## Wpisywanie polecenia

Wpisz instrukcję w polu na dole ekranu. Opisz oczekiwany wynik i kolejne czynności. Zmienne w treści zapisuje się w nawiasach klamrowych, na przykład `{invoice_number}` lub `{url}`. Ich nazwy i wartości uzupełnia się w oknie zmiennych, otwieranym przyciskiem z kołem zębatym.

<figure><img src="../../.gitbook/assets/site-extra-docbits-operator-pl.png" alt="Polski interfejs Operatora DocBits z pustym polem polecenia. Nie uruchomiono zadania."><figcaption><p>Polski interfejs Operatora DocBits z pustym polem polecenia. Nie uruchomiono zadania.</p></figcaption></figure>

Przycisk ze strzałką rozpoczyna wykonanie polecenia. Ikona pobierania otwiera okno zapisywania polecenia, a kosz służy do czyszczenia rozmowy. Samo otwarcie okna zapisu nie zapisuje szablonu.

Więcej przykładów znajdziesz w [przewodniku pisania poleceń](prompt-writing-guide.md).

## Zapisywanie polecenia

W oknie zapisu podaj **nazwę polecenia**. Opcja **Zapisz Monit publicznie** określa udostępnienie szablonu. Przygotowując szablon do udostępnienia, używaj nazw zmiennych w treści; wartości potrzebne do konkretnego zadania uzupełniaj przed jego uruchomieniem.

<figure><img src="../../.gitbook/assets/site-extra-operator-prompt-dialog-pl.png" alt="Polskie okno zapisu polecenia. Nie wpisano danych i nie kliknięto przycisku Zapisz; przycisk Wyczyść w przedstawionej wersji zamyka okno."><figcaption><p>Polskie okno zapisu polecenia. Nie wpisano danych i nie kliknięto przycisku Zapisz; przycisk Wyczyść w przedstawionej wersji zamyka okno.</p></figcaption></figure>

Przycisk **Edytuj zmienne** otwiera definicje zmiennych. Przycisk **Zapisz** zapisuje szablon. Aby zamknąć okno bez zapisywania, użyj krzyżyka w jego prawym górnym rogu. W przedstawionej wersji również przycisk **Wyczyść** zamyka to okno; jego podpis nie opisuje poprawnie tej czynności.

## Lista zapisanych poleceń

Menu w prawym górnym rogu otwiera panel zapisanych poleceń. Lista zawiera oddzielne sekcje poleceń organizacji i poleceń publicznych oraz wyszukiwanie po nazwie.

Przy poleceniach organizacji znajdują się ikony uruchamiania, edycji i usuwania. W sekcji publicznej przycisk ze strzałką uruchamia wybrany szablon. Przed uruchomieniem uzupełnij wartości jego zmiennych.

## Sterowanie wykonaniem

Podczas wykonywania polecenia dostępne są funkcje wstrzymania, wznowienia, anulowania oraz przejęcia kontroli. Wstrzymanie pozwala zatrzymać dalsze kroki i sprawdzić bieżący stan. Wznowienie kontynuuje pracę, a anulowanie kończy uruchomienie. Przejęcie kontroli umożliwia ręczną interakcję z widokiem przeglądarki.

<figure><img src="../../.gitbook/assets/image (3) (1).png" alt="Przykład ikon wznowienia i zatrzymania wykonania."><figcaption><p>Przykład ikon wznowienia i zatrzymania wykonania.</p></figcaption></figure>

## Widok szczegółowy

Przycisk rozwijania otwiera szczegółowy widok wykonania. Można w nim śledzić kolejne działania, bieżący krok i komunikaty operatora oraz korzystać z funkcji sterowania wykonaniem.

<figure><img src="../../.gitbook/assets/Detailed view .jpg" alt="Ikona rozwijania widoku szczegółowego."><figcaption><p>Ikona rozwijania widoku szczegółowego.</p></figcaption></figure>
