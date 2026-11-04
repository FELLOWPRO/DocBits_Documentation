# Pomiń ekstrakcję XML z hybrydowych plików PDF

### Przegląd

Ustawienie **Pomiń ekstrakcję XML z hybrydowych plików PDF** (Skip Hybrid PDF XML Extraction) określa, w jaki sposób DocBits przetwarza **hybrydowe pliki PDF** — faktury PDF zawierające osadzoną ustrukturyzowaną e-fakturę (ZUGFeRD / Factur-X). Decyduje, czy **ustrukturyzowany XML wewnątrz PDF** jest dokumentem wiodącym dla automatycznego przetwarzania, czy też **sam plik PDF** jest przetwarzany za pomocą OCR jako dokument główny.

To ustawienie jest szczególnie istotne dla **klientów w USA**. W przeciwieństwie do UE/Niemiec, Stany Zjednoczone nie mają ogólnego obowiązku fakturowania elektronicznego B2B, dlatego organizacje z USA zwykle chcą, aby PDF był traktowany jako główna, czytelna dla człowieka faktura — nawet gdy kontrahent wysyła plik ZUGFeRD/Factur-X z osadzonym XML.

### Co robi to ustawienie?

Plik ZUGFeRD/Factur-X to pojedynczy PDF, który zawiera również fakturę XML czytelną dla maszyn. Domyślnie DocBits wykrywa ten osadzony XML i wykorzystuje go jako wiodące źródło do ekstrakcji (ustrukturyzowana ścieżka elektroniczna).

* **Wyłączone (domyślnie)** — DocBits wykrywa osadzony XML e-faktury i przetwarza dokument na **ustrukturyzowanej ścieżce elektronicznej**. XML jest fakturą wiodącą. Jest to prawnie poprawne zachowanie dla UE/Niemiec, gdzie ustrukturyzowana e-faktura jest fakturą właściwą, a PDF stanowi jedynie wizualizację / kopię do odczytu.
* **Włączone** — DocBits **ignoruje osadzony XML** i kieruje dokument do **procesora PDF (OCR)**. PDF staje się głównym dokumentem przetwarzania. Jest to typowy wybór dla **organizacji z USA**, które chcą przetwarzania zorientowanego na PDF.

{% hint style="info" %}
To ustawienie dotyczy wyłącznie **hybrydowych plików PDF** (ZUGFeRD / Factur-X = `.pdf` z osadzonym XML). Czysty plik XRechnung/EDI przesłany jako `.xml` jest zawsze przetwarzany na ustrukturyzowanej ścieżce elektronicznej — nie ma pliku PDF, który mógłby stać się dokumentem głównym.
{% endhint %}

### Audyt i zgodność — oryginał jest zawsze zachowywany

Włączenie tego ustawienia **nie odrzuca** e-faktury. Oryginalny artefakt jest zawsze zachowywany:

* Oryginalny **plik PDF** ZUGFeRD/Factur-X — **wraz z osadzonym XML — pozostaje przechowywany** i możliwy do pobrania. Z przechowywanej kopii dokumentu nic nie jest usuwane.
* Przetwarzanie zmienia tylko **to, która treść napędza ekstrakcję** (PDF/OCR a osadzony XML), a nie to, co jest archiwizowane.

Dzięki temu organizacja z USA może przetwarzać PDF jako dokument główny, podczas gdy ustrukturyzowana e-faktura pozostaje dostępna do audytu.

{% hint style="warning" %}
W przypadku organizacji z UE/Niemiec pozostaw to ustawienie **wyłączone**. Zgodnie z przepisami o e-fakturowaniu z 2025 r. ustrukturyzowana e-faktura (ZUGFeRD/Factur-X, XRechnung) jest fakturą prawnie właściwą; zwykły PDF to jedynie kopia do odczytu. Przetwarzanie PDF jako głównego zamiast danych ustrukturyzowanych nie jest właściwe, gdy istnieje ważna e-faktura.
{% endhint %}

### Jak używać

1. **Otwórz ustawienie**:
   * Przejdź do **Ustawienia**.
   * Wybierz **Przetwarzanie dokumentów**.
   * Wybierz **Moduł**.
   * Otwórz sekcję **Typ dokumentu**.
   * Znajdź **Pomiń ekstrakcję XML z hybrydowych plików PDF** i przełącz suwak.
2. **Wybierz tryb**:
   * **Organizacje z USA / zorientowane na PDF** → włącz suwak, aby pliki PDF ZUGFeRD/Factur-X były przetwarzane za pomocą OCR jako dokument główny.
   * **Organizacje z UE/Niemiec** → pozostaw suwak wyłączony, aby ustrukturyzowana e-faktura pozostała dokumentem wiodącym.
3. **Zweryfikuj**:
   * Prześlij plik PDF ZUGFeRD/Factur-X i sprawdź wynik przetwarzania — przy włączonym suwaku jest on traktowany jako zwykły PDF (OCR); przy wyłączonym wyodrębniane są osadzone dane e-faktury.

### Kiedy używać tej funkcji

* **Klienci z USA / brak obowiązku e-faktury**: włącz, aby znajomy PDF był głównym dokumentem przetwarzania, a osadzona e-faktura pozostawała zarchiwizowana.
* **Mieszane / zorientowane na PDF przepływy pracy**: włącz, gdy procesy następcze, walidacja lub przegląd opierają się na układzie PDF, a nie na XML.
* **Zgodność UE/Niemcy**: pozostaw wyłączone, aby ustrukturyzowane dane e-faktury napędzały przetwarzanie, zgodnie z wymogami.
