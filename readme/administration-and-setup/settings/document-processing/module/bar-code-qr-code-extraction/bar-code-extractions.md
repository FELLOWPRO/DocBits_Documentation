# Ekstrakcja kodów kreskowych

## Przegląd

Ta funkcja umożliwia automatyczne wykrywanie kodów kreskowych w dokumentach. Po jej aktywacji wszystkie obsługiwane typy kodów kreskowych są skanowane i wyodrębniane podczas przetwarzania.

## Jak włączyć ekstrakcję kodów kreskowych

Aby włączyć funkcję ekstrakcji kodów kreskowych, wykonaj następujące kroki:

1. **Przejdź do ustawień**:
   * Na dashboardzie przejdź do **Settings**.
   * Wybierz **Document Processing**, a następnie **Module**.
2. **Włącz funkcję**:
   * Przewiń w dół, aby znaleźć opcję **Bar-Code Extraction**.
   * Przesuń suwak, aby włączyć Bar-Code Extraction.\\

## **Dodatkowe ustawienia**

### **Przypisywanie kodów kreskowych**

#### **Cel:** Pozwala walidatorom ręcznie przypisać wyodrębnioną wartość kodu kreskowego do wybranego pola dokumentu podczas walidacji pól.

#### Jak włączyć **Barcode Assignment**

Aby włączyć funkcję **Barcode Assignment**, wykonaj następujące kroki:

1. **Przejdź do ustawień**:
   * Na dashboardzie przejdź do **Settings**.
   * Wybierz **Document Processing**, a następnie **Module**.
2. **Włącz funkcję**:
   * Przewiń w dół, aby znaleźć opcję **Barcode Assignment**.
   * Przesuń suwak, aby włączyć **Barcode Assignment**.\\

#### **Jak to działa:**

* Włącza opcję „Assign Barcode” na ekranie walidacji pól.\\
* Użytkownicy mogą wybrać wykrytą wartość kodu kreskowego i przypisać ją do pola dokumentu, takiego jak PO Number lub Invoice Number.\\

### Podział dokumentu według kodu kreskowego / kodu QR

**Cel:** Automatycznie dzieli wielostronicowe dokumenty na osobne dokumenty na podstawie obecności określonych kodów kreskowych lub kodów QR.

#### Jak włączyć podział dokumentu według kodu kreskowego / kodu QR

Aby włączyć funkcję **podziału dokumentu według kodu kreskowego / kodu QR**, wykonaj następujące kroki:

1. **Przejdź do ustawień**:
   * Na dashboardzie przejdź do **Settings**.
   * Wybierz **Document Processing**, a następnie **Classification and Extraction**.
2. **Włącz funkcję**:
   * Znajdź opcję **Document Splitting**.
   * Dla **Split** wybierz **Split by Barcode / QR Code**.
   * Dla **Barcode Type** wybierz z listy jeden lub więcej obsługiwanych typów kodów kreskowych.
   * Dla **Barcode Pattern** zdefiniuj wzorzec, który ma wywołać podział. Aby dopasować dynamiczne wartości kodów kreskowych, możesz użyć **wyrażenia regularnego** (regex).

**Jak to działa:**

* Wybierasz typy kodów kreskowych, które mają wywołać podział.
* Definiujesz wzorzec, do którego musi pasować kod kreskowy — może to być stały ciąg znaków lub wyrażenie regularne (np. `^INV\d{6}$` dopasowuje kody kreskowe takie jak `INV123456`).
* Podczas przetwarzania dokumentu za każdym razem, gdy strona zawiera pasujący kod kreskowy, **tworzony jest nowy dokument** zaczynający się od tej strony.

### Obsługiwane typy kodów

Pełną listę obsługiwanych formatów kodów kreskowych i kodów QR znajdziesz na [stronie przeglądu](./).
