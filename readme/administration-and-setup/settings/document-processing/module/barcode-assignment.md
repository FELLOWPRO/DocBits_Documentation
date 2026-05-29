# Przypisanie na podstawie kodu kreskowego

### Przegląd

Ustawienie **Przypisanie na podstawie kodu kreskowego** (Barcode Assignment) pozwala DocBits używać **kodów kreskowych wewnątrz pliku do rozdzielenia go na pojedyncze dokumenty**. Jest to przydatne, gdy kilka dokumentów jest skanowanych razem do jednego dużego pliku PDF, a kod kreskowy oznacza, gdzie kończy się jeden dokument, a zaczyna następny.

To ustawienie jest **domyślnie wyłączone**.

### Co robi to ustawienie?

Gdy to ustawienie jest włączone, DocBits wyszukuje kody kreskowe w przychodzącym wielostronicowym pliku i dzieli go na osobne dokumenty w oznaczonych miejscach. Każdy powstały dokument jest następnie przetwarzany osobno.

* **Włączone** — DocBits wykrywa kody kreskowe i automatycznie rozdziela połączony plik na pojedyncze dokumenty na ich podstawie.
* **Wyłączone** — Plik jest przetwarzany jako jeden dokument; kody kreskowe nie są używane do jego podziału.

{% hint style="info" %}
Chodzi tu o **podział i przypisanie** stron na podstawie kodów kreskowych. Odczyt danych zakodowanych w kodzie kreskowym (np. dla płatniczych kodów QR) jest obsługiwany osobno w sekcji **Bar-Code / QR Code Extraction**.
{% endhint %}

### Korzyści

* **Szybsze skanowanie wsadowe**: Zeskanuj cały stos dokumentów za jednym razem, oddzielonych arkuszami z kodem kreskowym, zamiast skanować każdy dokument osobno.
* **Mniej ręcznego sortowania**: DocBits tworzy pojedyncze dokumenty za Ciebie, więc nikt nie musi ręcznie dzielić pliku PDF.
* **Mniej błędów**: Dokumenty są za każdym razem rozdzielane dokładnie w oznaczonych miejscach.

### Jak używać

1. Przejdź do **Ustawienia**.
2. Wybierz **Przetwarzanie dokumentów**.
3. Wybierz **Moduł**.
4. Otwórz sekcję **Typ dokumentu**.
5. Znajdź **Przypisanie na podstawie kodu kreskowego** i włącz suwak.

### Kiedy używać tej funkcji

* **Skanowanie o dużej objętości**: Gdy skanujesz wiele dokumentów razem i używasz między nimi arkuszy rozdzielających z kodem kreskowym.
* **Mieszane partie**: Gdy jeden przychodzący plik zawiera kilka różnych dokumentów, które trzeba przetworzyć osobno.
* **Pozostaw wyłączone**, jeśli dokumenty zawsze przychodzą jako osobne pliki — podział nie jest wtedy potrzebny.
