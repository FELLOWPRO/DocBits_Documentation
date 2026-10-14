# Wykrywanie duplikatów

## Przegląd

W **DocBits** możesz filtrować duplikaty dokumentów, określając, które pola muszą się zgadzać oraz definiując interwał czasowy, w którym duplikaty powinny być wykrywane.

Ta strona zawiera szczegółowy przewodnik, jak skutecznie włączyć i korzystać z funkcji **Wykrywanie duplikatów**.

## Włączanie wykrywania duplikatów

Aby włączyć wykrywanie duplikatów dokumentów w **DocBits**, wykonaj następujące kroki:

1.  Przejdź do **Ustawienia** → **Ustawienia globalne** → **Typy dokumentów**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/Calculate_PO_unit_price_1.png)
2.  Wybierz żądany **Typ dokumentu** i kliknij **Więcej ustawień**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/Calculate_PO_unit_price_2.png)
3.  Przejdź do sekcji **Wykrywanie duplikatów**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/DuplicateDocument_3.png)

DocBits oferuje dwie opcje identyfikacji duplikatów dokumentów:

1. **Wykrywanie duplikatów dokumentów**:\
   Ta funkcja sprawdza duplikaty dokumentów przesłanych do **DocBits** na podstawie wybranych kryteriów. Jeśli jakikolwiek dokument pasuje do wybranych kryteriów w innych dokumentach, zostanie oznaczony jako duplikat.
2.  **Wykrywanie duplikatów faktur** (Dostępne tylko dla typu dokumentu **Faktura**):\
    Ta funkcja wymaga synchronizacji faktur dostawców z Infor do DocBits. Porównuje numery faktur w panelu DocBits z tymi w Infor. Jeśli ten sam numer faktury pojawi się więcej niż raz, zostanie oznaczony jako duplikat.

    <mark style="color:red;">**Uwaga**</mark>: Korzystanie z funkcji **Wykrywanie duplikatów faktur** spowoduje dodatkową opłatę kredytową.

## Filtruj, które dokumenty powinny być wykrywane jako duplikaty

Gdy **Wykrywanie duplikatów** jest włączone, dostępne będą dwa menu rozwijane do konfiguracji:

*   **Pola wykrywania duplikatów**\
    Wybierz pola, które powinny być używane do identyfikacji duplikatów (np. Identyfikator dostawcy, Data, Numer faktury itp.). Dokumenty pasujące do tych pól będą oznaczane jako duplikaty.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/DuplicateDocument_4.png)
*   **Interwał wykrywania duplikatów**

    Użyj tego ustawienia, aby zdefiniować zakres czasowy, w którym wykrywane są duplikaty. Dokumenty przesłane w wybranym interwale będą porównywane ze sobą na podstawie wybranych pól.

    **Dostępne opcje:**

    * 1 miesiąc
    * 3 miesiące (Zalecane)
    * 6 miesięcy
    * 1 rok

    <mark style="color:red;">**Uwaga**</mark>: Zaleca się interwał 3 miesięcy, aby zapewnić optymalną wydajność. Wybór dłuższego interwału może prowadzić do wolniejszego ładowania panelu.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/DuplicateDocument_6.png)

## Wyświetlanie duplikatów dokumentów na panelu

Gdy **Wykrywanie duplikatów** jest włączone, wszelkie dokumenty zidentyfikowane jako duplikaty będą wyświetlać ikonę wskaźnika duplikatu na panelu.

*   Kliknij tę ikonę, aby otworzyć pasujące rekordy w widoku podzielonego ekranu obok siebie dla łatwego porównania.\
    <mark style="color:red;">**Uwaga**</mark>: Ikona pojawi się tylko wtedy, gdy dla dokumentu wykryto przynajmniej jeden duplikat.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/DuplicateDocument_7.png)
*   Podczas przeglądania oznaczonego dokumentu, na górze pojawi się pasek ostrzegawczy, wskazujący, że dokument jest duplikatem.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/DuplicateDocument_5.png)
