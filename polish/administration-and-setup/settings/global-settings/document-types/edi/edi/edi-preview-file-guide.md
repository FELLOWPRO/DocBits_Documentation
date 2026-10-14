# Przewodnik pliku podglądu EDI

## 1. Przegląd

Plik **Podglądu** definiuje, w jaki sposób strukturalne dane XML są renderowane w czytelny dla człowieka format przypominający PDF. Łączy **HTML i CSS** dla prezentacji wizualnej i używa **XSLT** `**select**` **statements** do dynamicznego wstawiania danych z niestandardowego XML. Ten podgląd jest wyświetlany podczas **walidacji pola** i jest również dołączany podczas eksportowania dokumentów do **IDM**.

## 2. Cel i Funkcja

* Konwertuje czytelne dla maszyny niestandardowe XML na wizualnie sformatowany podgląd (PDF).
* Umożliwia przeglądanie i walidację wydobytych danych w sposób przyjazny dla człowieka.
* Zapewnia spójne renderowanie kluczowych pól dokumentu, takich jak nagłówki, tabele, sumy, itp.
* Zbudowany przy użyciu **HTML + CSS** do układu i projektowania oraz **XSLT** do wiązania danych z układem.

## 3. Dostęp i Podstawowa Edycja

#### **Dostęp do Pliku:**

1.  Przejdź do **Ustawienia** → **Typ Dokumentu** → _\[Twój Dokument (np. Zamówienie Zakupu)]_ → **E-Dok**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Ff6zyL0AvmqSvrogZdnox%252Fimage.png%3Falt%3Dmedia%26token%3D6bc9ab55-6ee9-43d1-b576-4c5833c208cf\&width=768\&dpr=4\&quality=100\&sign=a23de442\&sv=2)
2. W zakładce **E-Dok** wybierz swój format (np. **EDI**).
3.  Kliknij **Podgląd**, aby wyświetlić lub edytować plik.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fdo1R389GeSqFuZKLD0OP%252Fimage.png%3Falt%3Dmedia%26token%3D930903d4-44af-4188-b015-c60c2dd9d9ab\&width=768\&dpr=4\&quality=100\&sign=77bbb2ce\&sv=2)

#### **Zarządzanie Wersjami Roboczymi:**

* **Utwórz Wersję Roboczą:** Kliknij ikonę ✏️ ołówka.
* **Usuń Wersje Robocze:** Użyj ikony 🗑️ kosza, aby usunąć nieużywane wersje robocze.
* **Aktywuj Zmiany:** Kliknij ikonę ✅ zaznaczenia, aby opublikować wersję.
  * **Uwaga**: Aktywowanie nowej wersji spowoduje **automatyczne dezaktywowanie** poprzedniej.

## 4. Edytor HTML/XSLT/CSS

Plik **Podglądu** jest edytowany w dedykowanym edytorze obsługującym HTML, XSLT i CSS.

* **HTML** definiuje strukturę dokumentu wyjściowego (np. tabele, divy, układ).
* **CSS** kontroluje stylowanie (np. czcionki, odstępy, kolory, wyrównanie).
*   **XSLT** `**select**` **statements** są używane do dynamicznego wypełniania pól z niestandardowego XML, takich jak:

    Copy

    ```
    <xsl:value-of select="/PURCHASE_ORDER/PURCHASE_ORDER_NUMBER/text()" />
    ```
* Możesz również używać **logiki XSLT** (`<xsl:if>`, `<xsl:for-each>`, itp.) do obsługi warunkowego wyświetlania lub iterowania po pozycjach linii.

## 5. Funkcja Podglądu (Renderowanie Wyjścia)

Funkcja Podglądu pozwala testować i weryfikować, w jaki sposób dokument EDI jest renderowany z bieżącym plikiem podglądu.

#### **Użycie:**

* Prześlij plik EDI za pomocą standardowego procesu przesyłania.
* Skopiuj **ID Dokumentu** przesłanego pliku.
* Przejdź do interfejsu **Podglądu**.
* Otwórz **Funkcję Podglądu**.\
  \
  &#x20;![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F9lddYJl2G4tzpdr9RD5F%252Fimage.png%3Falt%3Dmedia%26token%3Df7663f70-ef10-4e64-bbdc-41048ed8352a\&width=300\&dpr=4\&quality=100\&sign=36ce2b93\&sv=2)
* Wprowadź ID Dokumentu i kliknij **Test**.
* Renderowany podgląd w stylu PDF zostanie wyświetlony przy użyciu konfiguracji HTML/CSS/XSLT.

Ta funkcja jest kluczowa do debugowania wiązań danych, doskonalenia układu i zapewnienia, że dokument jest zarówno dokładny, jak i wizualnie czytelny dla użytkowników i systemów potokowych, takich jak **IDM**.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FJH103tnbqZjuimpOniVg%252Fimage.png%3Falt%3Dmedia%26token%3D4e63cc09-b0de-488f-bdd0-ee5a9246a371\&width=768\&dpr=4\&quality=100\&sign=bfff5bba\&sv=2)

## 6. Przewodnik Wideo

Przewodnik wideo dla tego typu pliku jest dostępny na [stronie z Filmami.](https://docs.docbits.com/administration-and-setup/settings/global-settings/document-types/edi/edi/edi-videos) Użyj go, aby śledzić konfigurację, edycję i podgląd.
