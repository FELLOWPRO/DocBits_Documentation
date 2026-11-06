# Strona Raportu

Strona **Raport** podsumowuje, jak dokumenty przechodziły przez DocBits w wybranym okresie: ile dokumentów napłynęło, jak długo trwało ich przetwarzanie, które pola użytkownicy poprawiali i gdzie dokumenty ostatecznie trafiły. Jest przeznaczona dla administratorów i kierowników zespołów, którzy analizują całość pracy związanej z przyjmowaniem i walidacją dokumentów, a nie pojedynczy dokument.

{% embed url="https://www.youtube.com/watch?v=ar9jXYJo_AM" %}

## Włącz stronę Raportu

Strona jest aktywowana za pomocą przełącznika modułu. Włącz go raz dla organizacji:

1. Przejdź do **Ustawienia → Moduł** i otwórz grupę **Integracja dokumentów**.
2. Na karcie **Typ dokumentu** włącz opcję **Pokaż raport**.
3. Pozycja **Raport** pojawi się wtedy na pasku bocznym użytkowników organizacji.

<figure><img src="../.gitbook/assets/report-show-report-setting-pl.png" alt="Przełącznik Pokaż raport."><figcaption><p>Przełącznik Pokaż raport.</p></figcaption></figure>

## Otwórz stronę Raportu

Wybierz ikonę wykresu na pasku bocznym. Strona otworzy się z filtrem czasu, kluczowymi wskaźnikami wybranego okresu i statystykami pól.

<figure><img src="../.gitbook/assets/report-sidebar-icon-pl.png" alt="Pasek boczny DocBits z wyróżnioną ikoną wykresu i podpowiedzią Raport"><figcaption><p>Pozycja <strong>Raport</strong> na pasku bocznym.</p></figcaption></figure>

## Wybierz zakres czasu

Filtr **Jednostka czasu** u góry strony określa okres dla wszystkich poniższych wskaźników i sekcji. Oferuje opcje **Ostatnie 7 dni**, **Ostatnie 30 dni** oraz **Wybierz zakres czasu**, która otwiera kalendarz umożliwiający wybranie daty początkowej i końcowej.

<figure><img src="../.gitbook/assets/dbdc-19-report-time-options-native-20261103-pl.png" alt="Opcje filtra Jednostka czasu: Ostatnie 7 dni, Ostatnie 30 dni i Wybierz zakres czasu. Nagłówek i nawigacja aplikacji znajdują się poza obrazem."><figcaption><p>Opcje filtra Jednostka czasu: Ostatnie 7 dni, Ostatnie 30 dni i Wybierz zakres czasu. Nagłówek i nawigacja aplikacji znajdują się poza obrazem.</p></figcaption></figure>

## Wskaźniki obok filtra

<figure><img src="../.gitbook/assets/report-time-unit-filter-pl.png" alt="Górny wiersz strony Raportu: filtr Jednostka czasu ustawiony na 30, karta Nowe dokumenty, karta Średni czas systemowy i przycisk pobierania"><figcaption><p><strong>Jednostka czasu</strong>, <strong>Nowe dokumenty</strong>, <strong>Średni czas systemowy</strong> i przycisk pobierania.</p></figcaption></figure>

- **Nowe dokumenty** pokazuje liczbę dokumentów zaimportowanych w wybranym okresie.
- **Średni czas systemowy** pokazuje średni czas w sekundach, jakiego DocBits potrzebował na przetworzenie dokumentu w tym okresie.
- Przycisk pobierania po prawej stronie wiersza eksportuje raport do pliku Excel (XLSX) dla wybranego okresu.

## Zmienione pola

Wykres **Zmienione pola** zlicza, jak często poszczególne pola były ręcznie poprawiane w wybranym okresie. Gdy dane są dostępne, każdy słupek odpowiada jednemu polu, dzięki czemu łatwo zauważyć pola najczęściej edytowane przez zespół. Znak zapytania obok nagłówka wyjaśnia, co zlicza wykres. Komunikat „Nie znaleziono żadnych wpisów danych w odpowiednim przedziale czasowym.” oznacza, że dla wybranego okresu nie ma danych o ręcznych zmianach pól do wyświetlenia.

<figure><img src="../.gitbook/assets/report-changed-fields-pl.png" alt="Sekcja Zmienione pola z komunikatem „Nie znaleziono żadnych wpisów danych w odpowiednim przedziale czasowym.” zamiast słupków oraz menu wykresu w prawym górnym rogu"><figcaption><p>Sekcja <strong>Zmienione pola</strong> z komunikatem o braku danych dla wybranego okresu; słupki nie są wyświetlane.</p></figcaption></figure>

Użyj menu w prawym górnym rogu wykresu, aby pobrać sam wykres w formacie **SVG**, **PNG** lub **CSV**.

## Dodatkowe sekcje raportu

Poniżej wykresu znajdują się cztery karty. Są one domyślnie zwinięte; wybierz nagłówek, aby rozwinąć tabelę, i wybierz go ponownie, aby ją zwinąć.

1. **Łączna liczba dokumentów według typu** wyświetla każdy typ dokumentu w kolumnie **Typ** oraz liczbę dokumentów w kolumnie **Liczyć**. Typ z podtypami dokumentów ma znak **+**, który umożliwia wyświetlenie szczegółowego podziału tej liczby.
2. **Średnia dzienna na typ dokumentu** przedstawia tę samą listę jako średnią dzienną dla każdego typu dokumentu.
3. **Statystyka statusu** przedstawia dokumenty według statusu przetwarzania, w kolumnach **Typ**, **Status** i **Liczyć**.
4. **Statystyki eksportu** najpierw wyświetla organizacje Twojego konta; rozwiń jedną z nich, aby zobaczyć użyte formaty eksportu w kolumnach **Użytkownicy**, **Typ** i **Eksportowano**.

<figure><img src="../.gitbook/assets/report-total-documents-per-type-pl.png" alt="Rozwinięta karta Łączna liczba dokumentów według typu z kolumnami Typ i Liczyć"><figcaption><p><strong>Łączna liczba dokumentów według typu</strong>.</p></figcaption></figure>

<figure><img src="../.gitbook/assets/report-daily-average-per-doctype-pl.png" alt="Rozwinięta karta Średnia dzienna na typ dokumentu z kolumnami Typ i Liczyć"><figcaption><p><strong>Średnia dzienna na typ dokumentu</strong>.</p></figcaption></figure>

<figure><img src="../.gitbook/assets/report-status-statistic-pl.png" alt="Rozwinięta karta Statystyka statusu z kolumnami Typ, Status i Liczyć"><figcaption><p><strong>Statystyka statusu</strong>.</p></figcaption></figure>

<figure><img src="../.gitbook/assets/dbdc-19-report-export-stats-native-20261103-pl.png" alt="Statystyki eksportu z rozwiniętą sekcją istniejącej organizacji. Nazwy organizacji i wartości wierszy są zamaskowane; obraz przedstawia istniejące statystyki."><figcaption><p>Statystyki eksportu z rozwiniętą sekcją istniejącej organizacji. Nazwy organizacji i wartości wierszy są zamaskowane; obraz przedstawia istniejące statystyki.</p></figcaption></figure>
