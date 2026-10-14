# eSLOG 1.6 i 2.0

### Obsługiwane wersje faktur eSLOG

Obecnie obsługiwane są **wersje faktur eSLOG 1.6 i 2.0**.

Aby uzyskać oficjalną dokumentację eSLOG, możesz odwołać się do [tego linku](https://epos.si/en/eslog).

Obie wersje eSLOG są włączone domyślnie.

### Kroki do modyfikacji konfiguracji eSLOG

**Skonfiguruj eSLOG:**

* Przejdź do **Ustawienia → Ustawienia globalne → Typy dokumentów → Faktura**.
*   Kliknij na **E-Doc**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FctcfxakxpfAcknvIueSQ%252Fimage.png%3Falt%3Dmedia%26token%3Dca599f1e-323d-4b61-99af-760f5f51a75d\&width=768\&dpr=4\&quality=100\&sign=3eee1abc\&sv=2)
* Pojawi się lista wszystkich dostępnych e-dokumentów.
*   Zlokalizuj wersję eSLOG, którą chcesz zmodyfikować.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FzWM10W6vAigJ44spm4ai%252Fimage.png%3Falt%3Dmedia%26token%3Db61fe4e5-517b-47da-89ca-13a53d370abf\&width=768\&dpr=4\&quality=100\&sign=9d2c40e3\&sv=2)

### **Konfiguracja transformacji i ścieżki XML:**

W **ustawieniach transformacji** możesz zdefiniować ścieżkę do lokalizacji konkretnych informacji w pliku XML i zapisać je w nowej strukturze, co ułatwia dostęp do danych. **Uwaga:** Jeśli korzystasz z tej funkcjonalności, musisz używać nowo utworzonych ścieżek XML, a nie oryginalnych ścieżek XML, w **Podglądzie** i **Ścieżce ekstrakcji**.

#### **Kroki do modyfikacji pliku transformacji:**

1. Otwórz **Transformację**.
2. Utwórz nowy szkic, klikając ikonę **ołówka**.
3. Wybierz nowo utworzony szkic.
4. Utwórz nowe pole lub zmodyfikuj istniejące.
5. Ustaw pożądaną ścieżkę do ekstrakcji danych.
6. Kliknij **Zapisz**.

### Konfiguracja podglądu PDF

**Konfiguracja podglądu PDF** jest używana do generowania wersji dokumentu czytelnej dla użytkownika. Możesz ją dostosować za pomocą HTML, aby odpowiadała Twoim potrzebom.

#### **Kroki do modyfikacji pliku podglądu:**

1. Otwórz **Podgląd**.
2. Utwórz nowy szkic, klikając ikonę **ołówka**.
3. Wybierz nowo utworzony szkic.
4. Utwórz nowe pole lub zmodyfikuj istniejące.
5. Ustaw pożądaną ścieżkę do ekstrakcji danych.
6. Kliknij **Zapisz**.

### Konfiguracja ścieżek ekstrakcji

**Konfiguracja ścieżek ekstrakcji** jest używana do ekstrakcji danych i wypełniania pól w **ekranie walidacji**, takich jak tabela faktur lub pola skonfigurowane w układzie faktury.

#### **Kroki do modyfikacji** **ścieżek ekstrakcji**:

1. Otwórz **Ścieżki ekstrakcji**.
2. Utwórz nowy szkic, klikając ikonę **ołówka**.
3. Wybierz nowo utworzony szkic.
4. Utwórz nowe pole lub zmodyfikuj istniejące.
5.  Lewa strona reprezentuje **ID pola DocBits**, które można znaleźć w **Ustawienia → Ustawienia globalne → Typy dokumentów → Faktura → Pola**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F1UkfNRxu2YiwFEpl4r78%252Fimage.png%3Falt%3Dmedia%26token%3Dc0c75088-5071-422d-89bc-1a65b47c8304\&width=768\&dpr=4\&quality=100\&sign=b671dd86\&sv=2)

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FmmL87niJd0tym9UnOTGg%252Fimage.png%3Falt%3Dmedia%26token%3D52490976-ed01-45b5-a2b1-c8374812ade3\&width=768\&dpr=4\&quality=100\&sign=b9d96dd6\&sv=2)
6. Prawa strona reprezentuje **ścieżkę do pola** utworzonego w Transformacji.
7. Kliknij **Zapisz**.
