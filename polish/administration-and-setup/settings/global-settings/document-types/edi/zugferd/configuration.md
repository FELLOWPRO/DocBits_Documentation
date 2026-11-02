# Konfiguracja ZUGFeRD

{% embed url="https://youtu.be/AxrHNEmmXtg" %}
Samouczek DocBits E-Invoice: przetwarzanie XRechnung / ZUGFeRD (Factur-X), walidacja danych i automatyzacja workflowów
{% endembed %}

## **Obsługiwane wersje ZUGFeRD**

DocBits obsługuje wszystkie główne wersje ZUGFeRD, w tym:

* **1.0**
* **2.0**
* **2.1** (zgodna z FACTUR-X 1.0.05)
* **2.2**
* **2.3** (zgodna z FACTUR-X 1.07.2)
* **2.3.2**

#### Standardowa aktywacja i modyfikacja

Standard ZUGFeRD jest domyślnie zawsze aktywny, ale w razie potrzeby możesz go modyfikować.

### **Kroki modyfikacji ustawień ZUGFeRD:**

1. Przejdź do **Settings → Global Settings → Document Types → Invoice**.
2. Kliknij **E-Doc**.\\
3. Pojawi się lista wszystkich dostępnych e-dokumentów.
4. Znajdź wersję **ZUGFeRD**, którą chcesz zmodyfikować.\\

## **Konfiguracja transformacji i ścieżek XML:**

W **ustawieniach transformacji** możesz zdefiniować ścieżkę do konkretnych informacji w pliku XML i zapisać je w nowej strukturze, co ułatwia dostęp do danych.\
<mark style="color:red;">**Uwaga**</mark>: Jeśli korzystasz z tej funkcji, w **Preview** i **Extraction Path** musisz używać nowo utworzonych ścieżek XML, a nie oryginalnych.

### **Kroki modyfikacji pliku transformacji:**

1. Otwórz **Transformation**.
2. Utwórz nowy szkic, klikając **ikonę ołówka**.
3. Wybierz nowo utworzony szkic.
4. Utwórz nowe pole lub zmodyfikuj istniejące.
5. Ustaw żądaną ścieżkę ekstrakcji danych.
6. Kliknij **Save**.

### Ważne uwagi:

* **Plik podglądu** jest używany tylko dla **FACTUR-X**, a nie dla **ZUGFeRD**. ZUGFeRD używa oryginalnego **PDF**.

## Konfiguracja podglądu PDF

**Konfiguracja podglądu PDF** służy do generowania wersji dokumentu czytelnej dla użytkownika. Możesz ją dostosować za pomocą HTML do swoich potrzeb.

### **Kroki modyfikacji pliku podglądu:**

1. Otwórz **Preview**.
2. Utwórz nowy szkic, klikając **ikonę ołówka**.
3. Wybierz nowo utworzony szkic.
4. Utwórz nowe pole lub zmodyfikuj istniejące.
5. Ustaw żądaną ścieżkę ekstrakcji danych.
6. Kliknij **Save**.

## Konfiguracja ścieżek ekstrakcji

**Konfiguracja ścieżek ekstrakcji** służy do wyodrębniania danych i wypełniania pól na **ekranie walidacji**, takich jak tabela faktury lub pola skonfigurowane w układzie faktury.

### **Kroki modyfikacji** **ścieżek ekstrakcji**:

1. Otwórz **Extraction Paths**.
2. Utwórz nowy szkic, klikając **ikonę ołówka**.
3. Wybierz nowo utworzony szkic.
4. Utwórz nowe pole lub zmodyfikuj istniejące.
5. Lewa strona reprezentuje **ID pola DocBits**, które znajdziesz w **Settings → Global Settings → Document Types → Invoice → Fields**.\\
6. Prawa strona reprezentuje **ścieżkę do pola** utworzonego w Transformation.
7. Kliknij **Save**.

Wykonując te kroki, zapewnisz dokładną ekstrakcję danych i walidację faktur ZUGFeRD.

## Faktycznie używane reguły i aktywacja

Reguły specyficzne dla organizacji mają pierwszeństwo przed regułami domyślnymi dla wykrytego formatu eDoc. Sprawdź aktywną TRANSFORMATION i sprawdź, który węzeł dostarcza invoice_type w przekształconym pliku XML; ścieżka zależy od formatu. Save zapisuje wersję roboczą; po testach użyj znacznika wyboru, aby ją aktywować. Wygenerowany Preview nie potwierdza zapisanego typu dokumentu. [Przewodnik rozwiązywania problemów z klasyfikacją](../credit-note-recognized-as-invoice.md) opisuje kody 381/261, późniejsze skrypty i środki ostrożności przy ponownym przetwarzaniu.
