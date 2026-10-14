# Przewodnik po pliku transformacji EDI

## 1. Przegląd

**Plik transformacji** definiuje, w jaki sposób strukturalny XML—utworzony za pomocą **Pliku deskryptora struktury**—jest konwertowany na niestandardowy format XML, który odpowiada wymaganiom dotyczącym konkretnego typu dokumentu lub formularza w Twojej organizacji.

Ta transformacja jest wykonywana za pomocą **XSLT (Extensible Stylesheet Language Transformations)**, które można tworzyć i utrzymywać za pomocą **Edytora XSLT** w interfejsie DocBits.

## 2. Cel i Funkcja

* Przekształca **pośredni XML** (wyjście z deskryptora struktury) w **ostateczny XML** zgodny z schematem dokumentu.
* Umożliwia elastyczność w dostosowywaniu się do różnych formatów partnerów EDI i wewnętrznych wymagań systemowych.
* Tworzony za pomocą **reguł XSLT**, które pozwalają zdefiniować odwzorowania, formatowanie wartości, logikę warunkową i strukturę.

## 3. Dostęp i Podstawowe Edycje

#### Dostęp do pliku

1.  Przejdź do **Ustawienia → Typ Dokumentu** → \[Twój Dokument (np. _Zamówienie Zakupu_)] → **E-Dok.**

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F1yCRagLzRFmy2hPRDDc1%252Fimage.png%3Falt%3Dmedia%26token%3D020874a9-1eae-4965-9dd2-c23461fc5884\&width=768\&dpr=4\&quality=100\&sign=5e53a730\&sv=2)
2. W zakładce **E-Dok** wybierz swój format (np. **EDI**).
3.  Kliknij **Transformacja**, aby wyświetlić lub edytować.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FZtaE4dZT9E1exWMZ5FCI%252Fimage.png%3Falt%3Dmedia%26token%3D787868b4-47b4-455e-9a26-112f692b91f3\&width=768\&dpr=4\&quality=100\&sign=460124f1\&sv=2)

#### Zarządzanie Wersjami Roboczymi

* **Utwórz Wersję Roboczą**: Kliknij ikonę ✏️ ołówka.
* **Usuń Wersje Robocze**: Użyj ikony 🗑️ kosza, aby usunąć nieużywane wersje robocze.
* **Aktywuj Zmiany**: Kliknij ikonę ✅ zaznaczenia, aby opublikować wersję.
  * **Uwaga**: Aktywowanie nowej wersji spowoduje **automatyczne dezaktywowanie** poprzedniej.

## 4. Edytor XSLT

Plik transformacji jest edytowany za pomocą wbudowanego **Edytora XSLT**, który obsługuje podświetlanie składni i walidację.

* Dodaj szablony do mapowania określonych ścieżek z wejściowego XML na pożądaną strukturę.
* Użyj logiki warunkowej (np. `<xsl:if>`, `<xsl:choose>`) do obsługi opcjonalnych lub zmiennych formatów danych.
* Stosuj funkcje formatowania według potrzeb (np. manipulacja łańcuchami, formatowanie dat).

## 5. Funkcja Podglądu (Podgląd Przekształconego XML)

**Funkcja Podglądu** pozwala na testowanie i podgląd, w jaki sposób przetwarzany jest przesłany plik EDI za pomocą bieżącego **Pliku transformacji**.

#### Użycie

* Prześlij plik EDI za pomocą standardowego przepływu przesyłania.
* Skopiuj **ID Dokumentu** przesłanego pliku.
* Przejdź do interfejsu **Pliku transformacji**.
*   Otwórz **Funkcję Podglądu**.\


    <div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F9lddYJl2G4tzpdr9RD5F%252Fimage.png%3Falt%3Dmedia%26token%3Df7663f70-ef10-4e64-bbdc-41048ed8352a&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=36ce2b93&#x26;sv=2" alt="" width="375"></div>
* Wprowadź **ID Dokumentu** do pola i naciśnij **Test**.
* Wyświetli się przetworzony **wynikowy XML**.

Jest to szczególnie przydatne do debugowania odwzorowań XSLT i zapewnienia, że ostateczna struktura XML spełnia wymagania formatu.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FWbwwmXgp6nRPIb1zBpgj%252Fimage.png%3Falt%3Dmedia%26token%3Dab5766f1-45bf-484e-9aa4-ab3059705591\&width=768\&dpr=4\&quality=100\&sign=46905864\&sv=2)

## 6. Przewodnik Wideo

Przewodnik wideo dla tego typu pliku jest dostępny na [Stronie z Filmami.](https://docs.docbits.com/administration-and-setup/settings/global-settings/document-types/edi/edi/edi-videos) Użyj go, aby śledzić konfigurację, edycję i podgląd.
