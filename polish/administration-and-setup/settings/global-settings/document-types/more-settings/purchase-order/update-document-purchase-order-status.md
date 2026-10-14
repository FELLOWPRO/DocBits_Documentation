# Aktualizuj status zamówienia zakupu



## Przegląd

Gdy jest włączone, kolumna **Status PO** na tablicy rozdzielczej jest automatycznie aktualizowana za każdym razem, gdy zmienia się status zamówienia zakupu.

## Gdzie aktywować

1. Przejdź do: **Ustawienia** → **Ustawienia globalne** → **Typ dokumentu**
2.  Wybierz pożądany typ dokumentu i kliknij **Więcej ustawień**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fsd3ebb3IETh7wNSA5flh%252Fimage.png%3Falt%3Dmedia%26token%3D6f1d286b-e006-4b23-9866-9ed37bf2bdaa\&width=768\&dpr=4\&quality=100\&sign=b0f0b121\&sv=2)
3.  W sekcji **Zamówienie zakupu**, przejdź do opcji **Aktualizuj status zamówienia zakupu**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FSsFkQ46Jd4tn0WGqNSjk%252Fimage.png%3Falt%3Dmedia%26token%3D51ee4f2d-76ae-42b4-a748-f0e9d340b329\&width=768\&dpr=4\&quality=100\&sign=e0f4b1af\&sv=2)

## Jak to działa

Gdy ta opcja jest włączona, kolumna **Status PO** na tablicy rozdzielczej automatycznie odzwierciedla bieżący status zamówienia zakupu. Na przykład, jeśli status PO zostanie zaktualizowany na _Odebrany_ lub _Zafakturowany_, kolumna na tablicy rozdzielczej zostanie odpowiednio zaktualizowana, aby pokazać ten nowy status.

<div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FmWZIOi5pqWyeagCfiXgy%252FStatus%2520on%2520Dashboard.jpg%3Falt%3Dmedia%26token%3D3aad59e7-d249-4f07-afa3-c68429128cec&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=6cde440e&#x26;sv=2" alt="" width="375"></div>

## Konfiguracja

1. **Włącz ustawienie** Przejdź do wyżej wymienionego miejsca i przełącz ustawienie.
2. **Dodaj kolumnę Status PO (jeśli nie jest widoczna)** Jeśli kolumna **Status PO** nie jest jeszcze widoczna na tablicy rozdzielczej:
   *   Przejdź do: **Ustawienia zaawansowane** → **Ustaw kolumny tabeli dla organizacji**

       ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fn6GyECCtvUeKLYd6FkEH%252Fimage.png%3Falt%3Dmedia%26token%3Da023deba-748f-4140-bb33-17483c91f2cf\&width=768\&dpr=4\&quality=100\&sign=164eb544\&sv=2)
   * Dodaj pole z typu dokumentu, szukając **Status PO**
3. **Skonfiguruj konfigurację wyszukiwania**
   *   Skonfiguruj pole Status w nagłówku zamówienia zakupu w ten sposób:

       ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Folrh285NuJO787Udc80C%252Fimage.png%3Falt%3Dmedia%26token%3Def5abe46-fe94-4946-a893-66f7ca21322b\&width=768\&dpr=4\&quality=100\&sign=415e657e\&sv=2)
   * **Uwaga:** **Zamówienie zakupu musi być w trybie Auto Trigger, w przeciwnym razie aktualizacje statusu mogą nie działać poprawnie**
   * Nie wiesz jak **Skonfigurować konfigurację wyszukiwania? Oto** [**przewodnik konfiguracji wyszukiwania**](../../../../../setup/document-types/fuzzy-data-configuration-with-master-data.md)
4. **Zweryfikuj** Odbierz lub zafakturować zamówienie zakupu, a następnie sprawdź tablicę rozdzielczą, aby potwierdzić, że status został poprawnie zaktualizowany.
