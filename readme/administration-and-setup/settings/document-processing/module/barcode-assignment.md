# Przypisanie na podstawie kodu kreskowego

### Przegląd

Ustawienie **Przypisanie na podstawie kodu kreskowego** (Barcode Assignment) dodaje narzędzie kodów kreskowych do **ekranu walidacji dokumentów**. Odczytuje kody kreskowe i kody QR znalezione w dokumencie i pozwala **przypisać ich wartości do pól dokumentu** — na przykład wypełnić numer referencyjny, zamówienia lub dowodu dostawy z kodu kreskowego zamiast go wpisywać.

To ustawienie jest **domyślnie wyłączone**.

### Co robi to ustawienie?

Gdy to ustawienie jest włączone, podczas walidacji dokumentu na pasku narzędzi pojawia się mały **przycisk kodu kreskowego** (ikona kodu QR). Kliknięcie go pokazuje kody kreskowe, które DocBits znalazł w dokumencie, i możesz przypisać każdy z nich do pola. Pole zostaje następnie wypełnione wartością odczytaną z kodu kreskowego.

* **Włączone** — Przycisk kodu kreskowego jest wyświetlany na ekranie walidacji. Możesz odczytywać kody kreskowe w dokumencie i przypisywać ich wartości do pól.
* **Wyłączone** — Przycisk jest ukryty, a wartości kodów kreskowych nie są oferowane do przypisania podczas walidacji.

{% hint style="info" %}
**To służy do odczytania wartości kodu kreskowego/QR i przypisania jej do pola podczas walidacji.** Automatyczne wyodrębnianie ustrukturyzowanych danych z kodów płatności (takich jak Swiss QR Bill lub GiroCode) — oraz dzielenie wielostronicowego pliku w miejscach stron rozdzielających z kodem kreskowym — obsługuje **inne** ustawienie: [Bar-Code / QR Code Extraction](bar-code-qr-code-extraction/README.md).
{% endhint %}

### Korzyści

* **Szybsze, bezbłędne wprowadzanie**: Pobieraj wartości bezpośrednio z kodu kreskowego, zamiast je odczytywać i wpisywać ręcznie.
* **Mniej literówek**: Zeskanowana wartość to dokładnie to, co jest zakodowane w kodzie kreskowym.
* **Zachowujesz kontrolę**: To Ty decydujesz, który kod kreskowy trafia do którego pola podczas walidacji.

### Jak używać

1. Przejdź do **Ustawienia**.
2. Wybierz **Przetwarzanie dokumentów**.
3. Wybierz **Moduł**.
4. Otwórz sekcję **Typ dokumentu**.
5. Znajdź **Przypisanie na podstawie kodu kreskowego** i włącz suwak.
6. Następnie podczas walidacji dokumentu kliknij **przycisk kodu kreskowego** na pasku narzędzi i przypisz wykryte wartości kodów kreskowych do odpowiednich pól.

### Kiedy używać tej funkcji

* **Dokumenty z kodami kreskowymi**: Gdy Twoje dokumenty zawierają kody kreskowe/QR, których wartości należą do określonych pól (np. numery zamówień lub referencyjne).
* **Ręczne procesy walidacji**: Gdy osoba przegląda dokumenty i chce szybko wypełnić pola z kodów kreskowych.
* **Pozostaw wyłączone**, jeśli Twoje dokumenty nie mają użytecznych kodów kreskowych lub jeśli potrzebujesz tylko automatycznego **wyodrębniania** kodów kreskowych/QR — zobacz [Bar-Code / QR Code Extraction](bar-code-qr-code-extraction/README.md).
