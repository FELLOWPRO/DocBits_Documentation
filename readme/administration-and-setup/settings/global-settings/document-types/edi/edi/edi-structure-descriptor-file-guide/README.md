# Przewodnik pliku opisującego strukturę EDI

## **1. Przegląd**

Plik **Opisujący Strukturę** definiuje, w jaki sposób powtarzające się segmenty EDI (np. `N1`–`N4`) są grupowane w strukturalny JSON. Zapewnia:

* **Dokładny parsowanie** powiązanych elementów jako jednostek pojedynczych.
* **Spójne wyniki** dla systemów docelowych.

_Dla pełnego przykładu z szczegółami segmentów, zobacz_ [_Przykład opisu struktury_](edi-structure-descriptor.md)_._

## **2. Dostęp i podstawowa edycja**

#### **Dostęp do pliku**

1.  **Ustawienia** → **Typ Dokumentu** → \[Twój Dokument (np. _Zamówienie Zakupu_)] → **E-Dok.**

    ![Edytor typu dokumentu Purchase Order z kartami Edit layout, Document Sub Types, Table columns, Fields, Model Training, Regex, Scripts i E-Doc](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Ff6zyL0AvmqSvrogZdnox%252Fimage.png%3Falt%3Dmedia%26token%3D6bc9ab55-6ee9-43d1-b576-4c5833c208cf\&width=768\&dpr=4\&quality=100\&sign=a23de442\&sv=2)
2. W sekcji **E-Dok**, wybierz swój format (np. _EDI_ ).
3.  Kliknij **Opis Struktury**.

    ![Sekcja EDI E-Doc z listą plików Structure Descriptor, Transformation, Preview i Extraction Paths wraz ze znacznikami czasu](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FOuNVhIuYBPJTu4PdMecy%252Fimage.png%3Falt%3Dmedia%26token%3Dd111b34e-0dd9-4436-9df4-f59490ac0d87\&width=768\&dpr=4\&quality=100\&sign=6e8e9f0e\&sv=2)

#### **Zarządzanie wersjami roboczymi**

* **Utwórz wersję roboczą**: Kliknij ikonę ✏️ ołówka, aby rozpocząć edycję.
* **Usuń wersje robocze**: Użyj ikony 🗑️ kosza, aby usunąć nieużywane wersje robocze.
* **Aktywuj zmiany**: Kliknij ikonę ✅ znaczka zatwierdzenia, aby zatwierdzić i opublikować zmiany.
  * **Uwaga**: Aktywowanie nowej wersji **automatycznie dezaktywuje** poprzednią.

## 3. Funkcja podglądu (Podgląd sparsowanego XML)

Funkcja **Podglądu** pozwala na testowanie i podgląd, jak przesłany plik EDI jest parsowany przy użyciu bieżącego pliku opisującego strukturę.

#### Użycie

* Prześlij plik EDI za pomocą standardowego przepływu przesyłania.
* Skopiuj **ID Dokumentu** przesłanego pliku.
* Przejdź do interfejsu **Pliku Opisującego Strukturę**.
*   Otwórz **Funkcję Podglądu**.\


    <div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F9lddYJl2G4tzpdr9RD5F%252Fimage.png%3Falt%3Dmedia%26token%3Df7663f70-ef10-4e64-bbdc-41048ed8352a&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=36ce2b93&#x26;sv=2" alt="Panel podglądu Extraction paths z selektorem dokumentów pokazującym 29 dokumentów i przyciskiem Preview" width="375"></div>
* Wprowadź **ID Dokumentu** do pola i naciśnij **Test**.
* Wynikowy **sparsowany wynik XML** zostanie wyświetlony.

Jest to szczególnie przydatne do debugowania mapowań i walidacji grup strukturalnych w czasie rzeczywistym.

![Widok testowy JSON dla Structure Descriptor z polem identyfikatora dokumentu, listą pól JSON i ustrukturyzowanym wyjściem XML z elementami VALUE](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FBXU6zeFapt7ZIVFl37Iz%252Fimage.png%3Falt%3Dmedia%26token%3D9d51e329-b781-4781-a527-3258f6f933c6\&width=768\&dpr=4\&quality=100\&sign=4ca17281\&sv=2)

## 6. Przewodnik wideo

Przewodnik wideo dla tego typu pliku jest dostępny na [stronie z filmami.](https://docs.docbits.com/administration-and-setup/settings/global-settings/document-types/edi/edi/edi-videos) Użyj go, aby śledzić konfigurację, edycję i podgląd.


<figure><img src="../../../../../../../.gitbook/assets/site-all-edi-list-pl.png" alt="Istniejący format EDI z czterema skonfigurowanymi atrybutami."><figcaption><p>Istniejący format EDI z czterema skonfigurowanymi atrybutami.</p></figcaption></figure>

<figure><img src="../../../../../../../.gitbook/assets/site-all-edi-detail-pl.png" alt="Aktywny atrybut STRUCTUREDESCRIPTOR: deskryptor struktury JSON w edytorze tylko do odczytu."><figcaption><p>Aktywny atrybut STRUCTUREDESCRIPTOR: deskryptor struktury JSON w edytorze tylko do odczytu.</p></figcaption></figure>


Widoki przedstawiają istniejącą konfigurację i wersję. Ustawienia różnią się w zależności od typu dokumentu i formatu. Sprawdź zmiany w wersji roboczej przed aktywacją.

Ilustracje przedstawiają polskie karty etapów oraz aktywną wersję konfiguracji w trybie tylko do odczytu. W pokazanej wersji interfejsu przycisk podglądu ma błędny podpis „Zapowiedź”; odpowiada on funkcji podglądu, oznaczonej w karcie jako „Podgląd”. Techniczne nagłówki edytora, identyfikatory atrybutów i kod konfiguracji pozostają w oryginalnej postaci.
