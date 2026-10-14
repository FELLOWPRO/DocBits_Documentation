# Konfiguracja ZUGFeRD

{% embed url="https://youtu.be/AxrHNEmmXtg" %}
Samouczek DocBits E-Invoice: Przetwarzanie XRechnung / ZUGFeRD (Factur-X), walidacja danych i automatyzacja przepływów pracy
{% endembed %}

## **Obsługiwane wersje ZUGFeRD**

DocBits obsługuje wszystkie główne wersje ZUGFeRD, w tym:

* **1.0**
* **2.0**
* **2.1** (zgodnie z FACTUR-X 1.0.05)
* **2.2**
* **2.3** (zgodnie z FACTUR-X 1.07.2)
* **2.3.2**

#### Standardowa aktywacja i modyfikacja

Standard ZUGFeRD jest zawsze aktywny domyślnie, ale w razie potrzeby można wprowadzić w nim zmiany.

### **Kroki modyfikacji ustawień ZUGFeRD:**

1. Przejdź do **Ustawienia → Ustawienia globalne → Typy dokumentów → Faktura**.
2. Kliknij **E-Doc**.
3. Pojawi się lista wszystkich dostępnych e-dokumentów.
4. Znajdź wersję **ZUGFeRD**, którą chcesz zmodyfikować.

## **Konfiguracja transformacji i ścieżki XML:**

W **ustawieniach transformacji** można zdefiniować ścieżkę do lokalizacji określonych informacji w pliku XML i zapisać je w nowej strukturze, co ułatwia dostęp do danych. <mark style="color:red;">**Uwaga**</mark>: W przypadku korzystania z tej funkcji należy używać nowo utworzonych ścieżek XML, a nie oryginalnych ścieżek XML, w **Podglądzie** i **Ścieżce ekstrakcji**.

### **Kroki modyfikacji pliku transformacji:**

1. Otwórz **Transformację**.
2. Utwórz nowy szkic, klikając **ikonę ołówka**.
3. Wybierz nowo utworzony szkic.
4. Utwórz nowe pole lub zmodyfikuj istniejące.
5. Ustaw żądaną ścieżkę do ekstrakcji danych.
6. Kliknij **Zapisz**.

### Ważne uwagi:

* **Plik podglądu** jest używany tylko dla **FACTUR-X**, a nie dla **ZUGFeRD**. ZUGFeRD będzie korzystał z oryginalnego pliku **PDF**.

## Konfiguracja podglądu PDF

**Konfiguracja podglądu PDF** służy do generowania czytelnej dla użytkownika wersji dokumentu. Można ją dostosować za pomocą HTML do własnych potrzeb.

### **Kroki modyfikacji pliku podglądu:**

1. Otwórz **Podgląd**.
2. Utwórz nowy szkic, klikając **ikonę ołówka**.
3. Wybierz nowo utworzony szkic.
4. Utwórz nowe pole lub zmodyfikuj istniejące.
5. Ustaw żądaną ścieżkę do ekstrakcji danych.
6. Kliknij **Zapisz**.

## Konfiguracja ścieżek ekstrakcji

**Konfiguracja ścieżek ekstrakcji** służy do wyodrębniania danych i wypełniania pól na **ekranie walidacji**, takich jak tabela faktur lub pola skonfigurowane w układzie faktury.

### **Kroki modyfikacji** **ścieżek ekstrakcji**:

1. Otwórz **Ścieżki ekstrakcji**.
2. Utwórz nowy szkic, klikając **ikonę ołówka**.
3. Wybierz nowo utworzony szkic.
4. Utwórz nowe pole lub zmodyfikuj istniejące.
5. Lewa strona reprezentuje **ID pola DocBits**, które można znaleźć w **Ustawienia → Ustawienia globalne → Typy dokumentów → Faktura → Pola**.
6. Prawa strona reprezentuje **ścieżkę do pola** utworzoną w Transformacji.
7. Kliknij **Zapisz**.

Wykonując te kroki, można zapewnić dokładną ekstrakcję danych i walidację faktur ZUGFeRD.
