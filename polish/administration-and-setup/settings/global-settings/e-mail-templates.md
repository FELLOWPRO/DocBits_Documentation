# Szablony e-maili

{% embed url="https://youtu.be/R5IrCpiP__4" %}

## **Przegląd**

Szablony e-maili pozwalają na dostosowanie automatycznych powiadomień e-mail wysyłanych z DocBits. Szablony mogą zawierać dynamiczne pola (np. `{{FieldID}}`), obrazy i formatowanie HTML.

## **Dostęp do szablonów e-maili**

1.  Przejdź do: **Ustawienia → Ustawienia globalne → Szablony e-maili**

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FWzjaI1Jinpw0PQHCuwM0%252Fimage.png%3Falt%3Dmedia%26token%3D21f7af41-6ebe-4e25-952f-9ae0b11cade2\&width=768\&dpr=4\&quality=100\&sign=ae789081\&sv=2)
2. Panel wyświetla wszystkie szablony z:
   * **Nazwą**
   * **Tematem**
   * Datą **Ostatniej modyfikacji**
   * **Działaniami** (Edytuj lub Usuń).

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FENN4zipGg75mpi2OooPP%252Fimage.png%3Falt%3Dmedia%26token%3Ddff6d8a8-e5b3-4e52-bee1-e311daba7b64\&width=768\&dpr=4\&quality=100\&sign=4202a84f\&sv=2)

## **Tworzenie nowego szablonu**

### **1 Podstawowa konfiguracja**

* Kliknij **Nowy**.
* Wypełnij pola po prawej stronie:
  * **Nazwa**: Identyfikator szablonu (np. "Błąd dokumentu").
  * **Temat**: Linia tematu e-maila (np. "Wymagane działanie: Błąd dokumentu").
  *   **Typ dokumentu**: Wybierz z listy rozwijanej (np. "Faktura").

      ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FXzmfZBIoyoDS7tTz1qo4%252Fimage.png%3Falt%3Dmedia%26token%3D24547984-2406-41b5-95d6-0f7f45e06258\&width=768\&dpr=4\&quality=100\&sign=f7aa9b89\&sv=2)

### **2 Edytor szablonu**

* **Menu**: Formatuj tekst, dodawaj linki lub wstawiaj tabele.
* **Edytor HTML**: Kliknij ikonę `<>` aby edytować surowy HTML.
* **Dodaj obrazy**: Użyj funkcji **Prześlij**.
*   **Pola dynamiczne:** Wstaw wartości pól dokumentu przez

    * **Opcję pola zmiennego**: Wybierz z listy rozwijanej.
    * **Ręczne wprowadzenie**: Wpisz `{{FieldID}}` (np. `{{NumerFaktury}}`).

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/email_templates_4.png)

### **3 Zapisywanie**

* Kliknij **Zapisz**, aby zapisać szablon.

## **Wysyłanie testowego e-maila**

1.  Otwórz szablon i kliknij **Wyślij test**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FZTskZNsVfWj6IwBmwoR5%252Fimage.png%3Falt%3Dmedia%26token%3D62229942-2ee7-4d58-833c-eb863b18f2d3\&width=768\&dpr=4\&quality=100\&sign=b804f787\&sv=2)
2. Wprowadź:
   * **E-mail odbiorcy** (wymagane).
   * **Wartości pól** (opcjonalne; dane testowe dla zmiennych). ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FO2yw8EgefTPSCIhxUFH6%252Fimage.png%3Falt%3Dmedia%26token%3D2acc0067-3698-4565-92d8-6c4ddabe497c\&width=300\&dpr=4\&quality=100\&sign=461ae8e7\&sv=2)
3. Przejrzyj testowy e-mail i dostosuj szablon w razie potrzeby.

## **Używanie szablonów w powiadomieniach e-mailowych**

Zapisane szablony mogą być powiązane z [**Powiadomieniami e-mailowymi**](email-notification/) (np. przypomnienia o zatwierdzeniu, aktualizacje statusu).
