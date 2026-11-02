# FatturaPA: wyświetlanie atrybutu w liniach faktury

FatturaPA to włoski format faktur elektronicznych. Ta strona wyjaśnia, gdzie sprawdzić atrybut linii, np. numer zamówienia zakupu, przed zmianą mapowania lub podglądu faktury. **Nie dodawaj drugiej kolumny `PURCHASE_ORDER` bez wcześniejszego sprawdzenia aktywnego mapowania:** bieżące mapowanie w Sandboksie już je zawiera.

## Odnajdź trzy pliki FatturaPA

Otwórz **Ustawienia → Typy Dokumentów → E-Doc**, wybierz **INVOICE**, a następnie rozwiń **FATTURAPA**. Bieżąca lista zawiera trzy różne pliki:

* **TRANSFORMATION (XSLT)** odczytuje źródłowy plik XML FatturaPA i tworzy znormalizowane dane faktury.
* **PREVIEW (XSLT)** buduje wizualny podgląd faktury w stylu HTML/PDF na podstawie tych danych.
* **EXTRACTION PATHS (JSON)** mapuje znormalizowane wartości na pola i kolumny tabel DocBits.

<figure><img src="../../../../../.gitbook/assets/dbdc-630-fatturapa-list-pl-20261010.png" alt="Ustawienia E-Doc w polskiej wersji Sandboksa z rozwiniętym FATTURAPA oraz plikami Transformation, Preview i Extraction Paths"><figcaption><p>Aktualna lista plików FATTURAPA w polskiej wersji Sandboksa.</p></figcaption></figure>

## Sprawdź wyekstrahowaną wartość linii

Otwórz **EXTRACTION PATHS (JSON)**. W aktywnej wersji znajdź tablicę `tables` i jej `columns`. Widoczna wersja w Sandboksie zawiera już `{"name": "PURCHASE_ORDER", "path": "PURCHASE_ORDER"}`. Sprawdź wartość na rzeczywistej fakturze testowej przed jej edycją. Jeśli potrzebujesz innego atrybutu, ustal jego wartość w znormalizowanych danych, a następnie dodaj odrębną nazwę kolumny i odpowiadającą jej ścieżkę w wersji roboczej.

<figure><img src="../../../../../.gitbook/assets/dbdc-630-fatturapa-json-pl-20261010.png" alt="FATTURAPA Extraction Paths JSON z aktywną wersją i istniejącą kolumną tabeli PURCHASE_ORDER"><figcaption><p>Aktywne mapowanie ekstrakcji JSON zawiera już kolumnę numeru zamówienia zakupu.</p></figcaption></figure>

## Zmieniaj transformację lub podgląd tylko wtedy, gdy to konieczne

Jeśli znormalizowana wartość jest nieobecna, obejrzyj **TRANSFORMATION (XSLT)** oraz ścieżkę XML źródła, która ma ją wygenerować. Zmiana w tym miejscu wpływa na dane używane przez kolejne kroki mapowania i podglądu. Jeśli wartość jest wyekstrahowana poprawnie, ale nie pojawia się na wizualnej fakturze, obejrzyj **PREVIEW (XSLT)** oraz odpowiedni wiersz tabeli w tym szablonie. Oba pliki XSLT mają różne przeznaczenie.

<figure><img src="../../../../../.gitbook/assets/dbdc-630-fatturapa-transformation-pl-20261010.png" alt="Aktywna transformacja XSLT FATTURAPA tworząca znormalizowane dane INVOICE"><figcaption><p>Transformacja odczytuje źródłowy XML i buduje znormalizowane pola faktury.</p></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/dbdc-630-fatturapa-preview-pl-20261010.png" alt="Aktywny podgląd XSLT FATTURAPA z wyjściem HTML i stylami tabeli faktury"><figcaption><p>Podgląd steruje wizualnym wynikiem faktury.</p></figcaption></figure>

Użyj ikony ołówka na karcie wersji, aby przygotować zmianę. Przejrzyj wersję roboczą i użyj **Zapowiedzi** z reprezentatywną fakturą FatturaPA przed jej aktywacją. Zrzuty ekranu pokazują aktualne wersje aktywne; w tej sesji Sandboksa nie zapisano wersji roboczej ani nie uruchomiono testu podglądu.

Dawna instrukcja, że wszystkie dokumenty elektroniczne mają jako pochodzenie Wielką Brytanię, nie jest bezpieczną regułą ogólną. Sprawdź kraj, walutę i format liczbowy faktury w odniesieniu do dokumentu źródłowego oraz konfiguracji Twojej organizacji.
