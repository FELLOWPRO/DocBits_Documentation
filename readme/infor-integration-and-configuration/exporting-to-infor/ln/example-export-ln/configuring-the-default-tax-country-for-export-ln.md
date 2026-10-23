# Konfiguracja domyślnego kraju podatkowego dla eksportu LN

### Przegląd

Domyślny kraj podatkowy dla eksportu jest ustawiony na **DE (Niemcy)**, aby zapobiec błędom eksportu. Można to zmienić w pliku mapowania na jeden z dwóch sposobów:

* Zdefiniowanie innej wartości statycznej.
* Dynamiczne zmapowanie na pole w DocBits.

<mark style="color:red;">**Uwaga:**</mark> Jeśli wskazane pole nie istnieje lub jest puste, eksport powróci do wartości domyślnej **DE**.

### Kroki zmiany kraju podatkowego

#### 1. Pobierz plik mapowania

* Przejdź do **DocBits → Ustawienia → Przetwarzanie dokumentów → Eksport**.
* Otwórz konfigurację eksportu, którą chcesz zmodyfikować.
*   Kliknij **Pobierz**, aby pobrać plik mapowania.\\

    <figure><img src="../../../../.gitbook/assets/iScreen Shoter - Google Chrome - 250220120028.jpg" alt="Okno dialogowe Infor LN dla typu dokumentu Invoice z tytułem Invoice LN, polami wyboru ION-Mapping File, IDM Mapping File i LN-Mapping File oraz przyciskiem DOWNLOAD"><figcaption></figcaption></figure>
* Otwórz plik w edytorze tekstu.

#### 2. Zmodyfikuj plik mapowania

Wybierz jedną z dwóch poniższych opcji i wprowadź niezbędne zmiany.

**Opcja 1: Wartość statyczna**

Aby ustawić statyczną wartość kraju podatkowego, wykonaj następujące kroki:

1.  Zdefiniuj nowe pole statyczne, dodając `,TaxCountry` do linii `StaticFields`.

    ```properties
    StaticFields=FinancialCompany...,TaxCountry
    ```
2.  Ustaw kod kraju, dodając następującą linię:

    ```properties
    SF_TaxCountry=CountryCode
    ```

    Zastąp `CountryCode` rzeczywistym kodem kraju, np. `ES` dla Hiszpanii lub `DE` dla Niemiec:

    ```properties
    SF_TaxCountry=ES
    ```

**Przykład:**

```properties
StaticFields=FinancialCompany,TaxCountry
SF_TaxCountry=FR
```

<figure><img src="../../../../.gitbook/assets/image (415).png" alt="Fragment pliku mapowania LN ze StaticFields=FinancialCompany,RateDeterminer,ExternalRateFactor oraz wpisami HeaderFields takimi jak HF_SupplierCode=supplier_id i HF_InvoiceCurrency=currency"><figcaption></figcaption></figure>

**Opcja 2: Dynamiczne mapowanie z pola DocBits**

Aby dynamicznie zmapować kraj podatkowy z pola w DocBits:

1.  Dodaj `,TaxCountry` do linii `HeaderFields`:

    ```properties
    HeaderFields=SupplierCode,...,TaxCountry
    ```
2.  Zdefiniuj odpowiednie mapowanie pola:

    ```properties
    HF_TaxCountry=DocBits_Field_name
    ```

    Zastąp `DocBits_Field_Name` rzeczywistą nazwą pola w DocBits:

    ```properties
    HF_TaxCountry=tax_country_1
    ```

**Przykład:**

```properties
HeaderFields=SupplierCode,TaxCountry
HF_TaxCountry=tax_country_1
```

<figure><img src="../../../../.gitbook/assets/image (411).png" alt="Fragment pliku mapowania LN z dodanym TaxCountry w wierszu StaticFields i pozycją HF_TaxCountry zmapowaną na liście HeaderFields"><figcaption></figcaption></figure>

### Podsumowanie

* Jeśli kraj podatkowy **nie jest zdefiniowany lub pole jest puste**, przyjmowana jest wartość domyślna **DE**.
* **Użyj wartości statycznej**, jeśli kraj podatkowy jest stały dla wszystkich eksportów.
* **Użyj dynamicznego mapowania pola**, jeśli kraj podatkowy różni się w zależności od dokumentu.

Wykonując te kroki, możesz skutecznie zmodyfikować mapowanie kraju podatkowego zgodnie ze swoimi potrzebami.
