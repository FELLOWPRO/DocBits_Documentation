# Konfiguracja danych rozmytych z danymi głównymi

## **Przegląd**

Każdy rodzaj dokumentu ma swoje domyślne konfiguracje i musi być ustawiony osobno. Chociaż ten przykład wyjaśnia konfigurację dla **Faktur**, ten sam proces dotyczy wszystkich rodzajów dokumentów.

## Aby skonfigurować Dane Rozmyte, przejdź do:

Ustawienia → Ustawienia globalne → Rodzaje dokumentów → Faktura → Pola → Ustawienia danych głównych → Wyszukaj dane główne

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fhnn2NcPGzVkUO0mLQWTy%252Fimage.png%3Falt%3Dmedia%26token%3De2f87385-fc48-4149-9bef-ca917a7328bd\&width=768\&dpr=4\&quality=100\&sign=116ee1da\&sv=2)

## **Domyślne wyszukiwania**

Istnieją **cztery domyślne grupy wyszukiwań** dla faktur:

1. **Dane firmy**
2. **Nagłówek zamówienia zakupu**
3. **Dostawca**
4. **Kod podatkowy**

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F4VxYFu8M62dXi6qGsPl3%252Fimage.png%3Falt%3Dmedia%26token%3Db2bc4690-805b-4b19-aa89-73f315889d88\&width=768\&dpr=4\&quality=100\&sign=835f513a\&sv=2)

Każda grupa zawiera określone pola. Kliknij na grupę, aby ją **rozszerzyć** i zobaczyć pola. Domyślne grupy wyszukiwań są oznaczone etykietą **"Domyślne"**.

## **Status konfiguracji wyszukiwania**

* **Aktywne konfiguracje** są oznaczone etykietą **"Aktywowane"**.
* **Dezaktywowane konfiguracje** są oznaczone etykietą **"Dezaktywowane"**.

## **Wymaganie wstępne: Importowanie danych głównych**

Aby Dane Rozmyte działały poprawnie, odpowiednie **dane główne** muszą być zaimportowane. Bez tego system nie ma danych referencyjnych do użycia. Oto jak zaimportować dane główne:

{% content-ref url="../../../infor-integration-and-configuration/importing-customer-master-data/" %}
[importing-customer-master-data](../../../infor-integration-and-configuration/importing-customer-master-data/)
{% endcontent-ref %}

## **Zarządzanie grupami wyszukiwań**

Każda grupa wyszukiwań jest **domyślnie aktywowana**, ale można ją zmodyfikować, klikając trzy kropki:

* **Dezaktywuj** → Dezaktywuje grupę. _(Dostępne tylko dla aktywowanych grup)_
* **Aktywuj** → Aktywuje grupę. _(Dostępne tylko dla dezaktywowanych grup)_
* **Duplikuj** → Tworzy kopię, którą można modyfikować bez wpływu na oryginał.
* **Wyświetl** → Wyświetla informacje, takie jak **rodzaj dokumentu**, do którego należy i **tabelę wyszukiwania**, którą używa. _(Dostępne tylko dla domyślnych grup)_
* **Edytuj** → Dostępne dla grup **niestandardowych**. Pozwala na modyfikację szczegółów grupy.
* **Usuń** → Usuwa grupę całkowicie. _(Tylko dla grup niestandardowych)_

## **Tworzenie nowej konfiguracji wyszukiwania**

Istnieją **dwa sposoby** tworzenia konfiguracji wyszukiwania:

1.  **Zduplikuj istniejące wyszukiwanie**

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FZUlPcWGrx1oITQS3tgZP%252Fimage.png%3Falt%3Dmedia%26token%3D59fb300d-836e-40d0-84b7-4a405cf7f321\&width=768\&dpr=4\&quality=100\&sign=3442db8f\&sv=2)

    * Kopiuje wszystkie informacje i pola z istniejącej grupy.
    * Wystarczy podać **nową nazwę**.
2.  **Utwórz wyszukiwanie od zera**

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FNbEpo2p5Q8D1d7DUchBF%252Fimage.png%3Falt%3Dmedia%26token%3D401314b5-44d0-47df-b3e6-69fea83cce82\&width=768\&dpr=4\&quality=100\&sign=1d0ce322\&sv=2)

    * Kliknij **"Utwórz konfigurację wyszukiwania"**.
    * Wypełnij wymagane szczegóły:
      * **Nazwa konfiguracji**
      * **Tabela wyszukiwania** (Tabela danych głównych do użycia)
      * **Obsługa konfliktów** (Wybierz jedno: Najlepszy wynik, Brak zwracania, Zwróć pierwszy)
      * **Typ kontekstu** (Nagłówek lub Linia) wymaga kontekstu
      * **Znajdź wszystkie** (Opcja zaznaczenia) wymaga kontekstu

## **Zarządzanie polami w ramach grupy wyszukiwania**

Każda grupa zawiera pola, które można **dodać, usunąć, edytować lub wyświetlić**, w zależności od tego, czy są to pola domyślne czy niestandardowe.

### **Domyślne pola**

*   Oznaczone etykietą **"Domyślne"**.

    <div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fh37McVpB0tBo5wqiAttR%252Fimage.png%3Falt%3Dmedia%26token%3Dcabce083-83a5-4881-a64f-88a8757df49b&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=b3739019&#x26;sv=2" alt="" width="375"></div>
* **Można tylko je wyświetlić**, nie edytować ani usuwać.

### **Pola niestandardowe**

* **Można edytować lub usunąć**, klikając trzy kropki i wybierając **Edytuj** lub **Usuń**.

### **Dodawanie nowego pola**

**Uwaga:** Możesz tworzyć pola wewnątrz domyślnych konfiguracji wyszukiwania.

Aby dodać nowe pole w ramach grupy:

1.  Kliknij **"Utwórz"** w odpowiedniej grupie.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FvmIXTEQQHKKNbvTJj1b4%252Fimage.png%3Falt%3Dmedia%26token%3D8569867b-9f5b-4865-90bd-f2e41e846979\&width=768\&dpr=4\&quality=100\&sign=603cb7df\&sv=2)
2. Podaj następujące szczegóły:
   * **Pole wyszukiwania** → Nazwa kolumny z tabeli wyszukiwania danych głównych.
   * **Pole walidacji** → Odpowiadające pole DocBits.
   * **Pole nadrzędne** → _(Potrzebne więcej szczegółów)_
   * **Operator wyszukiwania** → Wybierz jedno:
     * Inteligentne
     * Zawiera
     * Dokładne
     * Rozpoczyna się od
     * Kończy się na
   * **Pola wyboru:**
     * **Automatyczne wyzwalanie** → Po włączeniu, jeśli inne pole w innej konfiguracji wyszukiwania dzieli tę samą kolumnę, to pole to zostanie zaktualizowane **automatycznie** za każdym razem, gdy inne pole zostanie zaktualizowane
     * **Możliwe do wyszukania** → Włącza pole jako pole **Danych Rozmytych**, umożliwiając wyszukiwanie w tabeli wyszukiwania danych głównych (niebieska ikona na ekranie walidacji).

## **Ostatni krok: Dodawanie pól do układu**

Po skonfigurowaniu pól Danych Rozmytych, **upewnij się, że dodano je do układu za pomocą Kreatora układu**. Jeśli pola nie są dodane do układu, nie będą dostępne do użycia.

{% content-ref url="../../settings/global-settings/document-types/layout-manager/" %}
[layout-manager](../../settings/global-settings/document-types/layout-manager/)
{% endcontent-ref %}

## **Jak DocBits wybiera jednego dostawcę**

Gdy dokument trafia do systemu, DocBits szuka dostawcy w danych głównych. Wynik zależy od trzech ustawień. Ta sekcja wyjaśnia je krok po kroku, na przykładach.

### **Krok 1 — Które pola są używane do wyszukiwania**

DocBits używa pola do wyszukiwania tylko wtedy, gdy spełnione są oba warunki:

* pole jest zaznaczone jako **Wyszukiwalne (Searchable)** lub **Auto Trigger** w konfiguracji wyszukiwania, oraz
* pole ma wartość na dokumencie.

Nie ma znaczenia, skąd wzięła się wartość. Pole wytrenowane, pole wypełnione przez AI i wartość wpisana przez użytkownika są traktowane tak samo.

{% hint style="warning" %}
**Wyszukiwalne robi dwie rzeczy.** Pokazuje niebieską ikonę wyszukiwania na ekranie walidacji **oraz** dodaje pole do automatycznego wyszukiwania dostawcy. Pole, które ma być przeszukiwane tylko ręcznie, powinno pozostać niezaznaczone.
{% endhint %}

### **Krok 2 — Jedno wyszukiwanie, a nie jedno na pole**

DocBits **nie** przeszukuje każdego pola osobno. Buduje **jedno** wyszukiwanie obejmujące wszystkie użyte pola. **Dopasuj wszystko (Match All)** decyduje, jak są łączone:

* **Dopasuj wszystko wyłączone** (domyślnie) → „znajdź każdego dostawcę pasującego do numeru NIP **LUB** do nazwy dostawcy". Daje to **dłuższą** listę.
* **Dopasuj wszystko włączone** → „znajdź każdego dostawcę pasującego do numeru NIP **ORAZ** do nazwy dostawcy". Daje to **krótszą** listę.

Proszę pamiętać, że operatory **Smart** i **Contains** szukają fragmentu tekstu. Nazwa „Meier" znajdzie także „Meier Bau GmbH" i „Meier & Sons Ltd". Dlatego nazwa dostawcy często znajduje kilku dostawców.

### **Krok 3 — Co się dzieje, gdy lista zawiera więcej niż jednego dostawcę**

Decyduje **Obsługa konfliktów (Conflict Handler)**:

* **Best Score** → wybiera dostawcę pasującego do największej liczby pól. Nigdy nie zostawia pustego dostawcy.
* **Return None** → zostawia dostawcę pustego, aby wybrał go użytkownik.
* **Return First** → wybiera pierwszego dostawcę z listy.

### **Przykłady**

We wszystkich przykładach dokument ma numer NIP i nazwę dostawcy, a oba pola są **Wyszukiwalne**.

<table><thead><tr><th width="150">NIP znajduje</th><th width="150">Nazwa znajduje</th><th width="150">Dopasuj wszystko wył. + Return None</th><th width="150">Dopasuj wszystko wł. + Return None</th><th width="150">Dopasuj wszystko wył. + Best Score</th></tr></thead><tbody>
<tr><td>tylko A</td><td>A i B</td><td>puste</td><td><strong>A</strong></td><td><strong>A</strong></td></tr>
<tr><td>A i B</td><td>tylko B</td><td>puste</td><td><strong>B</strong></td><td><strong>B</strong></td></tr>
<tr><td>A, B i C</td><td>C, D i E</td><td>puste</td><td><strong>C</strong></td><td><strong>C</strong></td></tr>
<tr><td>A, B i C</td><td>B, C i D</td><td>puste</td><td>puste</td><td>B lub C, niepewne</td></tr>
<tr><td>tylko A</td><td>nic</td><td><strong>A</strong></td><td>puste</td><td><strong>A</strong></td></tr>
</tbody></table>

Jak czytać tabelę:

* **Wiersze 1 do 3** to przypadek typowy. Jedno pole jest jednoznaczne, drugie nie. Przy **Dopasuj wszystko wyłączone** lista zawiera kilku dostawców, a **Return None** zostawia pole puste. **Dopasuj wszystko włączone** zostawia tylko dostawcę pasującego do obu pól i go znajduje.
* **Wiersz 4** nie ma żadnego jednoznacznego dostawcy. Pozostawienie pustego pola jest poprawne. **Best Score** i tak wybiera jednego, co może być błędem.
* **Wiersz 5** to ryzyko opcji **Dopasuj wszystko włączone**. Patrz ostrzeżenie poniżej.

{% hint style="warning" %}
**Dopasuj wszystko może zgubić dostawcę.** Przy **Dopasuj wszystko włączone** każde użyte pole musi pasować. Jeśli jedno pole zawiera wartość, której nie ma w danych głównych — literówka, stara nazwa firmy, wartość odczytana ze strony — całe wyszukiwanie nic nie zwróci i żaden dostawca nie zostanie znaleziony, choć sam NIP znalazłby właściwego.
{% endhint %}

### **Dostawca był wcześniej rozpoznawany, a teraz nie jest**

Prawie zawsze kolejne pole zaczęło dostarczać wartość. Proszę sprawdzić w tej kolejności:

1. Otworzyć dokument. Które pole grupy wyszukiwania ma teraz wartość, która wcześniej była pusta?
2. Otworzyć konfigurację wyszukiwania. Czy to pole jest zaznaczone jako **Wyszukiwalne** lub **Auto Trigger**? Jeśli tak, bierze teraz udział w wyszukiwaniu i wydłuża listę wyników.
3. Wybrać jedno z trzech rozwiązań:
   * **Pole nie powinno brać udziału w wyszukiwaniu** → odznaczyć **Wyszukiwalne** i **Auto Trigger** dla tego pola. Pole zachowa swoją wartość na dokumencie i nadal będzie widoczne dla użytkownika. To najmniejsza zmiana.
   * **Pole powinno brać udział** → włączyć **Dopasuj wszystko**, ale najpierw przeczytać ostrzeżenie powyżej.
   * **Dostawca ma być wybrany zawsze** → ustawić **Obsługę konfliktów** na **Best Score**. Trzeba zaakceptować, że zamiast pustego pola może zostać wybrany niewłaściwy dostawca.
