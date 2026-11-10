# Przewodnik po pliku EDI Structure Descriptor

## 1. Przegląd

**Plik Structure Descriptor** to plik **JSON**, który określa, w jaki sposób powtarzające się segmenty EDI (na przykład `N1`–`N4`) są grupowane w ustrukturyzowane dane wyjściowe. To pierwszy etap przetwarzania EDI:

* **Dokładne parsowanie** powiązanych segmentów jako pojedynczych jednostek.
* **Spójne dane wyjściowe** dla [Transformation](../edi-transformation-file-guide.md) i systemów docelowych.

_Pełny przykład ze szczegółami segmentów znajdziesz w_ [_Przykład Structure Descriptor_](edi-structure-descriptor.md)_._

## 2. Dostęp i podstawowa edycja

#### **Otwieranie pliku**

1. Przejdź do **Settings** → **Document Types** i otwórz **E-Doc** dla typu dokumentu, który chcesz skonfigurować (na przykład _Purchase Order_). Do edycji tych plików wymagane są uprawnienia administratora w organizacji.

    <!-- dbdc-139-edi-sd-list-en.png --><figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/dbdc-139-edi-sd-list-en.png" alt="Angielska strona E-Doc w Sandbox z rozwiniętym formatem EDI i wierszem STRUCTURE DESCRIPTOR (JSON) widocznym nad TRANSFORMATION, PREVIEW i EXTRACTION PATHS"><figcaption>Otwórz E-Doc dla swojego typu dokumentu; format EDI zawiera listę plików konfiguracyjnych.</figcaption></figure>

2. Rozwiń format **EDI**. Jego pliki konfiguracyjne są wymienione razem: **STRUCTURE DESCRIPTOR**, **TRANSFORMATION**, **PREVIEW** i **EXTRACTION PATHS**.
3. Kliknij wiersz **STRUCTURE DESCRIPTOR**, oznaczony jako **JSON**, aby go otworzyć.

#### **Zarządzanie wersjami roboczymi**

W lewej kolumnie widoczna jest lista **Version** dla pliku. Wersja oznaczona jako **Active** to ta, której używa DocBits.

* **Utworzenie wersji roboczej**: kliknij ikonę ołówka ✏️ obok aktywnej wersji, aby rozpocząć edycję. Samego aktywnego pliku nie można edytować bezpośrednio.
* **Usuwanie wersji roboczych**: użyj ikony kosza 🗑️, aby usunąć nieużywane wersje robocze.
* **Aktywowanie zmian**: kliknij ikonę znacznika wyboru ✅ na wersji roboczej, aby zatwierdzić i opublikować zmiany.
  * <mark style="color:red;">**Uwaga**</mark>: aktywacja nowej wersji **automatycznie dezaktywuje** poprzednią.

<!-- dbdc-139-edi-sd-detail-en.png --><figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/dbdc-139-edi-sd-detail-en.png" alt="Angielski edytor JSON Structure Descriptor w Sandbox z listą wersji po lewej stronie, wersją 1 oznaczoną jako Active i ikoną ołówka do utworzenia wersji roboczej"><figcaption>Plik Structure Descriptor z listą wersji; ikona ołówka tworzy wersję roboczą, którą można edytować.</figcaption></figure>

## 3. Funkcja Preview (podgląd wyników parsowania)

**Funkcja Preview** pozwala sprawdzić, jak przesłany plik EDI jest parsowany przy użyciu aktualnie wyświetlanego pliku Structure Descriptor, przed aktywacją jakichkolwiek zmian.

#### Jak używać

* Prześlij plik EDI w standardowym procesie przesyłania.
* Skopiuj **Document ID** przesłanego pliku.
* Otwórz plik **Structure Descriptor** w sposób opisany powyżej.
* Kliknij **Preview** w prawym górnym rogu, aby otworzyć panel testowy.

    <div align="left"><!-- dbdc-139-edi-sd-preview-en.png --><figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/dbdc-139-edi-sd-preview-en.png" alt="Angielska strona Structure Descriptor w Sandbox z otwartym panelem testowym Preview, pokazującym pole Document Id i przycisk Test" width="560"><figcaption>Panel testowy: wprowadź Document ID i kliknij Test.</figcaption></figure></div>

* Wprowadź **Document ID** w polu formularza i kliknij **Test**.
* Wynikowe **strukturyzowane dane wyjściowe** są wyświetlane obok edytora.

Jest to szczególnie przydatne do debugowania mapowań i weryfikowania grupowania struktur w czasie rzeczywistym. Wymagany jest reprezentatywny dokument EDI w danym formacie; wyświetlany wynik zależy od przesłanego pliku.

## 4. Omówienie wideo

Przewodnik wideo dla tego typu pliku jest dostępny na [stronie Wideo.](../edi-videos.md)\
Skorzystaj z niego, aby prześledzić konfigurację, edycję i podgląd.

Pokazane widoki przedstawiają istniejącą konfigurację i wersję. Ustawienia różnią się w zależności od typu dokumentu i formatu. Zmiany należy zweryfikować w wersji roboczej przed aktywacją.
