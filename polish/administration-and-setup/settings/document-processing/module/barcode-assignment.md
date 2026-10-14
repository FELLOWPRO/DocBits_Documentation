# Przypisanie na podstawie kodu kreskowego

### Przegląd

Ustawienie **Przypisanie na podstawie kodu kreskowego** (Barcode Assignment) dodaje narzędzie kodów kreskowych do **ekranu walidacji dokumentów**. Odczytuje kody kreskowe i kody QR znalezione w dokumencie i pozwala **przypisać ich wartości do pól dokumentu** — na przykład wypełnić numer zamówienia, referencyjny lub dowodu dostawy z kodu kreskowego zamiast go wpisywać.

To ustawienie jest **domyślnie wyłączone**.

### Co otrzymujesz po włączeniu

Po włączeniu ustawienia na pasku narzędzi po prawej stronie **ekranu walidacji** (`/field_validation_v1/…`) pojawia się nowy **przycisk kodu kreskowego** (ikona kodu QR). Ten przycisk jest punktem wejścia do całej funkcji — bez tego ustawienia ikona pozostaje ukryta.

<figure><img src="../../../../.gitbook/assets/barcode_assignment_validation_icon.png" alt="Ikona kodu kreskowego (kod QR) na pasku narzędzi walidacji"><figcaption><p>Gdy ustawienie jest włączone, ikona kodu kreskowego pojawia się na pasku narzędzi walidacji.</p></figcaption></figure>

Oto ikona w kontekście ekranu walidacji, obok przeglądanego dokumentu:

<figure><img src="../../../../.gitbook/assets/barcode_assignment_validation_screen.png" alt="Ekran walidacji z dostępną ikoną kodu kreskowego"><figcaption><p>Ekran walidacji — ikona kodu kreskowego (wyróżniona, pasek narzędzi po prawej) jest wyświetlana tylko wtedy, gdy Przypisanie na podstawie kodu kreskowego jest włączone.</p></figcaption></figure>

### Jak odczytywane są kody kreskowe

DocBits wykrywa kody kreskowe podczas przetwarzania dokumentu i udostępnia ich zdekodowane wartości do przypisania. Jeden dokument może zawierać kilka typów kodów kreskowych — na przykład **kod QR**, **Code 128** i **EAN-13** — z których każdy koduje inną wartość, taką jak numer zamówienia, numer faktury lub GLN dostawcy.

<figure><img src="../../../../.gitbook/assets/barcode_assignment_demo_invoice.png" alt="Przykładowa faktura zawierająca kilka typów kodów kreskowych"><figcaption><p>Przykładowa faktura demonstracyjna DocBits zawierająca trzy typy kodów kreskowych (kod QR → numer zamówienia, Code 128 → numer faktury, EAN-13 → GLN dostawcy), z których każdy koduje wartość możliwą do przypisania do pola.</p></figcaption></figure>

{% hint style="info" %}
To, które typy kodów kreskowych są wykrywane, określa ustawienie **Bar-Code / QR Code Extraction** (`Barcode Extraction Types`). Jeśli okno dialogowe pokazuje *„no barcodes extracted found”*, upewnij się, że wyodrębnianie kodów kreskowych jest włączone i że wybrano oczekiwane typy (np. `QRCODE`, `CODE128`, `EAN13`). Zobacz [Bar-Code / QR Code Extraction](bar-code-qr-code-extraction/README.md).
{% endhint %}

### Korzystanie z okna dialogowego Przypisanie na podstawie kodu kreskowego

1. Otwórz dokument na **ekranie walidacji**.
2. Kliknij **ikonę kodu kreskowego** na pasku narzędzi po prawej stronie.
3. Okno dialogowe **Przypisanie na podstawie kodu kreskowego** wyświetla każdy kod kreskowy wykryty przez DocBits w dokumencie, pokazany jako `Barcode <n> : <wartość>`.

<figure><img src="../../../../.gitbook/assets/barcode_assignment_dialog.png" alt="Okno dialogowe Przypisanie na podstawie kodu kreskowego z wykrytymi kodami"><figcaption><p>Okno dialogowe Przypisanie na podstawie kodu kreskowego wyświetla każdy wykryty kod z listą rozwijaną do wyboru pola docelowego.</p></figcaption></figure>

4. Dla każdego kodu kreskowego otwórz jego listę rozwijaną i wybierz pole, do którego ma trafić wartość.

<figure><img src="../../../../.gitbook/assets/barcode_assignment_field_options.png" alt="Wybór pola docelowego dla kodu kreskowego"><figcaption><p>Każdy kod kreskowy można przypisać do dowolnego pola dokumentu — np. Numer zamówienia, Numer faktury, ID dostawcy.</p></figcaption></figure>

5. Gdy tylko wybierzesz pole, zostaje ono wypełnione wartością kodu kreskowego.

<figure><img src="../../../../.gitbook/assets/barcode_assignment_field_mapped.png" alt="Kod kreskowy przypisany do pola Numer zamówienia"><figcaption><p>Po wybraniu pola (tutaj Numer zamówienia) pole zostaje wypełnione wartością kodu kreskowego.</p></figcaption></figure>

### Jak włączyć

1. Przejdź do **Ustawienia**.
2. Wybierz **Przetwarzanie dokumentów**.
3. Wybierz **Moduł**.
4. Otwórz sekcję **Typ dokumentu**.
5. Znajdź **Przypisanie na podstawie kodu kreskowego** i włącz suwak.

<figure><img src="../../../../.gitbook/assets/barcode_assignment_toggle.png" alt="Suwak Przypisanie na podstawie kodu kreskowego"><figcaption><p>Suwak Przypisanie na podstawie kodu kreskowego w Ustawienia → Przetwarzanie dokumentów → Moduł.</p></figcaption></figure>

### Korzyści

* **Szybsze, bezbłędne wprowadzanie**: Pobieraj wartości bezpośrednio z kodu kreskowego, zamiast je odczytywać i wpisywać ręcznie.
* **Mniej literówek**: Zeskanowana wartość to dokładnie to, co jest zakodowane w kodzie kreskowym.
* **Zachowujesz kontrolę**: To Ty decydujesz, który kod kreskowy trafia do którego pola podczas walidacji.

### Kiedy używać tej funkcji

* **Dokumenty z kodami kreskowymi**: Gdy Twoje dokumenty zawierają kody kreskowe/QR, których wartości należą do określonych pól (np. numery zamówień lub referencyjne).
* **Ręczne procesy walidacji**: Gdy osoba przegląda dokumenty i chce szybko wypełnić pola z kodów kreskowych.
* **Pozostaw wyłączone**, jeśli Twoje dokumenty nie mają użytecznych kodów kreskowych lub jeśli potrzebujesz tylko automatycznego **wyodrębniania** kodów kreskowych/QR — zobacz [Bar-Code / QR Code Extraction](bar-code-qr-code-extraction/README.md).

{% hint style="info" %}
**To służy do odczytania wartości kodu kreskowego/QR i przypisania jej do pola podczas walidacji.** Automatyczne wyodrębnianie ustrukturyzowanych danych z kodów płatności (takich jak Swiss QR Bill lub GiroCode) — oraz dzielenie wielostronicowego pliku w miejscach stron rozdzielających z kodem kreskowym — obsługuje **inne** ustawienie: [Bar-Code / QR Code Extraction](bar-code-qr-code-extraction/README.md).
{% endhint %}
