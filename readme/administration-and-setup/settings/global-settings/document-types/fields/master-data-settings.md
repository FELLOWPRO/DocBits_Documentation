# Ustawienia danych głównych

## Przegląd

W sekcji **Ustawienia danych głównych** w ustawieniach **Pola** dla konkretnego Typ dokumentu możesz przeglądać i konfigurować mapowania danych głównych do pól używanych podczas walidacji pól, korzystając z danych z [**Wyszukiwanie danych głównych**](../../../document-processing/master-data-lookup.md).

Te mapowania definiują, w jaki sposób dane główne są stosowane do poszczególnych pól podczas walidacji. Ta strona zawiera szczegółowy przewodnik po konfigurowaniu i zarządzaniu tymi mapowaniami.

## **Dostęp do** Ustawienia danych głównych **Ustawienia**

Aby uzyskać dostęp do ustawień **Ustawienia danych głównych**:

1.  Przejdź do **Ustawienia → Ustawienia globalne → Typy dokumentów**

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_document_types.png)
2.  Wybierz żądany **Typ dokumentu** i kliknij **Pola**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_document_types_fields.png)
3.  Kliknij **Ustawienia danych głównych**

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_1.png)

## Wyszukaj dane główne

W sekcji **Wyszukaj dane główne** możesz tworzyć konfiguracje wyszukiwania z danych głównych, aby używać ich jako mapowań pól podczas walidacji pól.

### Wpisy domyślne

W sekcji **Wyszukaj dane główne** niektóre domyślne wpisy są dostarczane przez **DocBits**. Te wpisy:

* Nie mogą być edytowane ani usuwane
* Mogą zostać dezaktywowane, jeśli nie są potrzebne

Wpisy domyślne są wyraźnie oznaczone **Default** tag dla łatwej identyfikacji.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_2.png)

### **Utwórz konfigurację wyszukiwania**

Aby utworzyć nową konfigurację wyszukiwania dla danych głównych:

1. Przejdź do sekcji **Wyszukaj dane główne**.
2.  Kliknij **Utwórz konfigurację wyszukiwania** w prawym górnym rogu.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_3.png)
3. Skonfiguruj następujące opcje:
   * **Wyszukaj nazwę**\
     Nazwa konfiguracji wyszukiwania.
   * **Wyszukaj nazwę zestawu danych**\
     Wybierz zestaw danych, który ma być użyty dla tej konfiguracji wyszukiwania.
   * **Osoba rozwiązująca konflikty**\
     Konflikt oznacza, że wyszukiwanie znalazło więcej niż jeden rekord. To ustawienie decyduje, co się wtedy dzieje:
     * **Best Score** – Używa wpisu pasującego do największej liczby pól. Nigdy nie zostawia pustego pola, więc może wybrać niewłaściwy rekord.
     * **Return None** – Pozostawia pole puste, aby użytkownik wybrał właściwy rekord.
     * **Return First** – Używa pierwszej dopasowanej wartości.
   *   **Typ kontekstu**

       Określa, gdzie w dokumencie zostanie zastosowana konfiguracja wyszukiwania. Wybierz między:

       **HEADER**

       Wyszukiwanie jest używane w walidacji pól. Skonfiguruj następujące:

       * **Dopasuj wszystko**\
         Po włączeniu rekord musi pasować do **wszystkich** użytych pól. Po wyłączeniu (domyślnie) wystarczy **jedno** pasujące pole, co daje dłuższą listę.

       ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_4.png)

       \
       **LINE**

       Wyszukiwanie jest używane w tabeli dokumentu. Skonfiguruj następujące:

       * **Szczegóły kontekstu**\
         Wybierz konkretną tabelę, do której ma być zastosowane wyszukiwanie.
       * **Dopasuj wszystko**\
         Po włączeniu rekord musi pasować do **wszystkich** użytych pól. Po wyłączeniu (domyślnie) wystarczy **jedno** pasujące pole, co daje dłuższą listę.

       ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_5.png)
{% hint style="info" %}
**Dopasuj wszystko** i **Osoba rozwiązująca konflikty** działają razem i decydują, czy dostawca zostanie rozpoznany automatycznie. Strona konfiguracji wyjaśnia oba ustawienia na przykładach:

{% content-ref url="../../../../setup/document-types/fuzzy-data-configuration-with-master-data.md" %}
[fuzzy-data-configuration-with-master-data](../../../../setup/document-types/fuzzy-data-configuration-with-master-data.md)
{% endcontent-ref %}
{% endhint %}

4.  Kliknij **Ratować**, aby utworzyć konfigurację wyszukiwania.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_6.png)

### Akcje na istniejącej konfiguracji wyszukiwania

Aby zarządzać istniejącą konfiguracją wyszukiwania, kliknij trzy kropki w prawym górnym rogu wybranej konfiguracji.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_7.png)

Dostępne są następujące akcje:

* **Aktywować / Dezaktywować**\
  Przełącz status konfiguracji wyszukiwania.
  * Aktywne konfiguracje są oznaczone etykietą **Aktywny**.
  * Nieaktywne konfiguracje są oznaczone etykietą **Nieaktywny**.
*   **Duplikat**\
    Po wprowadzeniu nazwy i kliknięciu **Zrobione** tworzona jest kopia wybranej konfiguracji wyszukiwania.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_8.png)
* **Redagować/Pogląd**\
  Umożliwia modyfikację wybranej konfiguracji wyszukiwania.\
  Po wprowadzeniu zmian kliknij **Ratować**, aby je zastosować.\
  <mark style="color:red;">**Uwaga**</mark>: Domyślne konfiguracje wyszukiwania można tylko przeglądać, nie można ich edytować. Opcja **Redagować** zostanie zastąpiona przez **Pogląd**.
*   **Usuwać**\
    Trwale usuwa wybraną konfigurację wyszukiwania po potwierdzeniu.\
    <mark style="color:red;">**Uwaga**</mark>: Usuwać można tylko konfiguracje bez **Default** tag.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_9.png)

### Utwórz nowe pole

Aby dodać nowe pole do konfiguracji wyszukiwania:

1. Otwórz wybraną konfigurację wyszukiwania.
2.  Kliknij **Tworzyć** w prawym górnym rogu.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_10.png)
3. Skonfiguruj wymagane opcje.
   * **Pole wyszukiwania**\
     Pole, które będzie przeszukiwane w wybranym zestawie danych wyszukiwania.
   * **Pole walidacji**\
     Pole, które będzie wyświetlane podczas walidacji pól.
   * **Pole nadrzędne** (opcjonalne)\
     To pole służy do weryfikacji poprawności wartości w **Pole walidacji**, zapewniając zgodność z odpowiadającym wpisem nadrzędnym w zestawie danych wyszukiwania.
   * **Operator wyszukiwania** (opcjonalne)\
     Wybierz, jak **DocBits** wyszukuje dopasowania w zestawie danych wyszukiwania:
     * **Smart** – _(Domyślne)_ Pomija spacje i znaki interpunkcyjne i szuka terminu **w dowolnym miejscu** pola. Dlatego „Meier" znajduje też „Meier Bau GmbH".
     * **Zawiera** – Wyszukuje wpisy, które zawierają dokładny termin w dowolnym miejscu pola.
     * **Kończy się na** – Wyszukuje wpisy, które kończą się określonym terminem.
     * **dokładny** – Wyszukuje dokładne dopasowanie całej wartości.
     * **Zaczyna się od** – Wyszukuje wpisy, które zaczynają się od określonego terminu.
   * **Automatyczne wyzwalanie** (opcjonalne)\
     Po włączeniu DocBits automatycznie wypełni wszystkie pola w konfiguracji wyszukiwania, gdy tylko to pole zostanie uzupełnione.
   *   **Przeszukiwalny** (opcjonalne)\
       Po włączeniu użytkownicy mogą ręcznie wyszukiwać dane główne podczas walidacji pól **oraz** pole bierze udział w wyszukiwaniu automatycznym. Pozostaw niezaznaczone, jeśli pole nie ma wpływać na wynik automatyczny.

       ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_12.png)

       ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_13.png)
4.  Kliknij **Ratować**, aby utworzyć nowe pole.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_11.png)

### Akcje na istniejącym polu

Aby zarządzać istniejącym polem, kliknij trzy kropki w kolumnie **Akcje** obok pola, które chcesz zmodyfikować.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_14.png)

Dostępne są następujące akcje:

* **Redagować/Pogląd**\
  Umożliwia modyfikację wybranego pola.\
  Po wprowadzeniu zmian kliknij **Ratować**, aby je zastosować.\
  <mark style="color:red;">**Uwaga**</mark>: Domyślne pola można tylko przeglądać, nie edytować. W takich przypadkach opcja **Redagować** pojawi się jako **Pogląd**.
*   **Usuwać**\
    Trwale usuwa wybrane pole po potwierdzeniu.\
    <mark style="color:red;">**Uwaga**</mark>: Usuwać można tylko pola bez **Default** tag.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_9.png)

## Dane główne LOV

Sekcja **Dane główne LOV** pozwala tworzyć konfiguracje list rozwijanych, korzystając z wartości z danych głównych. Te listy mogą być samodzielne lub zależne od innych list, umożliwiając dynamiczne filtrowanie i kaskadowe wybory podczas walidacji pól.

### Utwórz konfigurację wyszukiwania Lov

Konfiguracja wyszukiwania lov definiuje, w jaki sposób opcje listy rozwijanej są pobierane z tabeli danych głównych oraz jak te wartości są wyświetlane i wprowadzane do pól dokumentu.

**Aby utworzyć nową konfigurację wyszukiwania LOV:**

1. Przejdź do sekcji **Dane główne LOV**.
2.  Kliknij **Utwórz konfigurację wyszukiwania Lov** w prawym górnym rogu.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_15.png)
3. Skonfiguruj następujące opcje:
   * **Wyszukaj nazwę Love**\
     Nazwa konfiguracji wyszukiwania lov.
   * **Lookup Lov Dataset Name**\
     Wybierz tabelę danych głównych, która ma być użyta dla tej konfiguracji wyszukiwania lov.
   *   **Typ kontekstu**\
       Określa, gdzie w dokumencie zostanie zastosowana konfiguracja wyszukiwania lov:

       **HEADER**

       Konfiguracja wyszukiwania lov jest używana w walidacji pól. Skonfiguruj następujące:

       * **Pole etykiety wyszukiwania**\
         Wybierz kolumnę, której wartość będzie wyświetlana na liście rozwijanej.
       * **Pole wartości wyszukiwania**\
         Wybierz kolumnę, której wartość będzie przechowywana wewnętrznie i używana do filtrowania po dokonaniu wyboru. Ta wartość nie jest wyświetlana użytkownikowi.
       * **Poza polem**\
         Określa pole w walidacji pól, które otrzyma wybraną etykietę z listy rozwijanej.

       ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_16.png)

       \
       **LINE**

       Konfiguracja wyszukiwania lov jest używana w tabeli dokumentu. Skonfiguruj następujące:

       * **Szczegóły kontekstu**\
         Wybierz konkretną tabelę, w której ta konfiguracja wyszukiwania lov ma być aktywna.
       * **Pole etykiety wyszukiwania**\
         Kolumna, której wartość będzie wyświetlana na liście rozwijanej.
       * **Pole wartości wyszukiwania**\
         Wybierz kolumnę, której wartość będzie przechowywana wewnętrznie i używana do filtrowania po dokonaniu wyboru. Ta wartość nie jest wyświetlana użytkownikowi.
       * **Poza polem**\
         Określa docelowe pole w tabeli, do którego zostanie wstawiona wybrana etykieta.

       ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_17.png)
4.  Kliknij **Ratować**, aby utworzyć konfigurację wyszukiwania lov.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_18.png)

### Akcje na istniejącej konfiguracji wyszukiwania

Aby zarządzać istniejącą konfiguracją wyszukiwania lov, kliknij trzy kropki w prawym górnym rogu konfiguracji.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_19.png)

**Dostępne akcje:**

* **Aktywować / Dezaktywować**\
  Przełącz status konfiguracji wyszukiwania lov.
  * **Aktywny** konfiguracje są oznaczone etykietą **Aktywny**.
  * **Nieaktywny** konfiguracje są oznaczone etykietą **Nieaktywny**.
*   **Duplikat**\
    Po wprowadzeniu nazwy i kliknięciu **Zrobione** tworzona jest kopia wybranej konfiguracji wyszukiwania lov.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_21.png)
* **Redagować / Pogląd**\
  Zmodyfikuj wybraną konfigurację. Po wprowadzeniu zmian kliknij **Ratować**.
*   **Usuwać**\
    Trwale usuwa konfigurację po potwierdzeniu.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_20.png)

### Utwórz nowe pole

W każdej konfiguracji wyszukiwania lov możesz zdefiniować dodatkowe pola jako listy rozwijane, które działają jako wstępne filtry dla głównej logiki lov.

Pola te są oceniane przed załadowaniem głównej listy rozwijanej lov. Na podstawie wartości wybranych w tych polach wyniki głównego pola lov są dynamicznie filtrowane — umożliwiając zależne listy rozwijane.\
Na przykład wybór kraju w polu wstępnego filtra może zawęzić opcje miasta w głównej liście rozwijanej lov.

Oprócz tworzenia nowych pól możesz również używać istniejących pól jako wstępnych filtrów. Przy takiej konfiguracji wybrana wartość w istniejącym polu automatycznie przefiltruje główną listę rozwijaną lov.

**Aby dodać nowe pole:**

1. Otwórz wybraną konfigurację wyszukiwania lov.
2.  Kliknij **Tworzyć** w prawym górnym rogu.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_22.png)
3.  Skonfiguruj wymagane opcje.

    **Opcje konfiguracji pola (dotyczy zarówno kontekstu HEADER, jak i LINE):**

    * **Pole wyszukiwania**\
      Kolumna, która ma być przeszukiwana w wybranym zestawie danych w celu uzyskania wartości listy rozwijanej.
      * **Pole filtra**\
        Określa pole, którego wartość jest używana do wstępnego filtrowania wyników konfiguracji wyszukiwania lov przed załadowaniem głównej listy rozwijanej.
      * **Wartość filtra** (opcjonalne)\
        Dodaj statyczne filtry, aby dodatkowo zawęzić wyniki wyszukiwania.
      * **Wymagany**\
        Po włączeniu to pole musi być wypełnione, zanim jakiekolwiek zależne listy rozwijane będą mogły zostać uzupełnione.
4.  Kliknij **Ratować**, aby utworzyć nowe pole.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_23.png)

### Akcje na istniejącym polu

Aby zarządzać istniejącym polem w konfiguracji wyszukiwania lov, kliknij trzy kropki w kolumnie **Akcje** obok pola.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_24.png)

**Dostępne akcje:**

* **Redagować**\
  Zmodyfikuj wybrane pole. Po zmianach kliknij **Ratować**, aby zastosować.
*   **Usuwać**\
    Trwale usuwa pole po potwierdzeniu.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_20.png)
