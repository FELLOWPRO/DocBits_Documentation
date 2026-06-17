# Model sztucznej inteligencji

## Przegląd

Ustawienie **Model sztucznej inteligencji** pozwala zdefiniować, który model AI jest używany domyślnie do **ekstrakcji pól** i **ekstrakcji tabeli** podczas przetwarzania dokumentów.\
W tej sekcji możesz przejrzeć koszt tokenów dla każdego modelu oraz sprawdzić, który model jest obecnie przypisany do każdego dostawcy.

## Jak uzyskać dostęp

1.  Przejdź do **Ustawienia** → **Przetwarzanie dokumentów** → **Klasyfikacja i ekstrakcja**

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_classification_and_extraction.png)
2.  Przewiń w dół do sekcji **Ekstrakcja tabeli**

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ai_model_1.png)

## Opcje Modelu sztucznej inteligencji

DocBits oferuje trzy opcje modelu AI do ekstrakcji pól i tabel. Różnią się równowagą między **dokładnością ekstrakcji**, **szybkością przetwarzania** i **kosztem tokenów na dokument** — dzięki temu możesz dopasować opcję do rodzaju przetwarzanych dokumentów. Najedź kursorem na ikonę informacji obok ustawienia, aby zobaczyć koszt tokenów dla aktualnie wybranej opcji.

* **Full** – Najbardziej dokładna opcja, o najwyższej dokładności ekstrakcji. Najlepsza do złożonych układów, skanów niskiej jakości lub dokumentów, w których precyzja jest najważniejsza. Jako najpotężniejsza opcja jest też najwolniejsza, przy **2 tokenach za dokument**.
* **Fast** – Zrównoważona opcja łącząca wysoką dokładność z szybszym przetwarzaniem przy niższym koszcie. To zalecana opcja domyślna dla większości codziennych dokumentów, przy **1 tokenie za dokument**.
* **Turbo** – Najszybsza i najbardziej ekonomiczna opcja. Najlepiej nadaje się do dużych ilości prostych, czystych, dobrze ustrukturyzowanych dokumentów, gdzie szybkość i niski koszt są ważniejsze niż maksymalna dokładność, przy **1 tokenie za dokument**.

| Opcja | Najlepsza do | Dokładność | Szybkość | Koszt tokenów |
|-------|--------------|------------|----------|---------------|
| **Full** | Złożone układy, słabe skany, wysoka precyzja | Najwyższa | Najwolniejsza | 2 / dokument |
| **Fast** | Codzienne dokumenty (zalecana domyślna) | Wysoka | Szybka | 1 / dokument |
| **Turbo** | Duże ilości prostych, czystych dokumentów | Dobra | Najszybsza | 1 / dokument |

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ai_model_2.png)

## Tabela przypisania Modelu sztucznej inteligencji

Możesz również skonfigurować specyficzne dla dostawcy **modele AI** bezpośrednio na ekranie **Walidacja**, co pozwala dostosować dokładność ekstrakcji dla poszczególnych dostawców.\
\
Więcej informacji znajdziesz w odpowiedniej dokumentacji [tutaj](../../../../end-user-and-partner-section/end-user-section/validation-screen/supplier-specific-ai-model-for-field-and-table-extraction.md).

Tabela przypisania wyświetla ustawienia modelu AI dla każdego dostawcy i zawiera następujące szczegóły:

* **Supplier ID** – Unikalny identyfikator dostawcy
* **AI Model** – Model AI obecnie przypisany do dostawcy
* **E-Text**: Wskazuje, czy funkcja E-Text jest włączona
* **Action** – Zawiera opcję usunięcia wpisu

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ai_model_3.png)

### Usuń wpis – Zresetuj ustawienia specyficzne dla dostawcy

Aby zresetować ustawienie modelu AI dostawcy do domyślnych:

1.  Kliknij ikonę kosza w kolumnie **Action** obok wpisu dostawcy.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ai_model_4.png)
2.  Pojawi się okno potwierdzenia—potwierdź, że chcesz usunąć wpis.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ai_model_5.png)

Po usunięciu dostawca wróci do korzystania z domyślnego **modelu AI** do **ekstrakcji pól** i **ekstrakcji tabeli**.
