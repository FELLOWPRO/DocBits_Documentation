# Classification And Extraction

## Przegląd

W ustawieniach **Klasyfikacja i ekstrakcja** możesz:

* Włącz **Podział dokumentu** w oparciu o kody QR
* Skonfiguruj **formatowanie kwoty**
* Skonfiguruj **ekstrakcję tabeli**
* Przełącz przetwarzanie nieobsługiwanych plików **ZUGFeRD**
* Zdefiniuj specjalne zasady klasyfikacji
* Monitoruj specjalnie przeszkolone **AI modele** wykorzystywane w procesie klasyfikacji

Na tej stronie znajduje się szczegółowy opis wszystkich dostępnych ustawień.

## **Dostęp do ustawień klasyfikacji i wyodrębniania**

Aby uzyskać dostęp do ustawień **Klasyfikacja i wyodrębnianie**, przejdź do:\
**Ustawienia → Przetwarzanie dokumentu → Klasyfikacja i wyodrębnianie**

<figure><img src="../../../../.gitbook/assets/dbdc864-settings-nav-pl-20261012.png" alt="Nawigacja Ustawień z wyróżnionymi pozycjami Przetwarzanie dokumentów oraz Klasyfikacja i ekstrakcja"><figcaption><p>Otwórz <strong>Ustawienia → Przetwarzanie dokumentów → Klasyfikacja i ekstrakcja</strong>.</p></figcaption></figure>

## Document Splitting

W sekcji **Podział dokumentu** możesz skonfigurować, czy przesłany dokument powinien być dzielony na wiele dokumentów, gdy na jednej z jego stron pojawi się **kod kreskowy**.

Aby aktywować tę funkcję:

1. Przejdź do sekcji **Podział dokumentu**.
2.  Otwórz menu rozwijane.

    <figure><img src="../../../../.gitbook/assets/classification_and_extraction_14.png" alt="Strona ustawień Classification And Extraction z zakładkami Allgemein, Klassifizierungsregeln i AI-Modelle, na pustym panelu AI-Modelle widnieje napis Kein Datensatz gefunden"><figcaption></figcaption></figure>
3.  Wybierz **Podziel według kodu kreskowego/QR kodu**.

    <figure><img src="../../../../.gitbook/assets/classification_and_extraction_15.png" alt="Strona ustawień Classification And Extraction z zakładkami Allgemein, Klassifizierungsregeln i AI-Modelle oraz lewą nawigacją niemieckich ustawień DocBits"><figcaption></figcaption></figure>

Będziesz wtedy mieć możliwość:

* Wybierz jeden lub więcej typów kodów kreskowych, które mają zostać wykryte.
*   Określ wzór wyrażenia regularnego, do którego musi pasować kod kreskowy, aby uruchomić podział dokumentu.

    <figure><img src="../../../../.gitbook/assets/classification_and_extraction_16.png" alt="Panel wyników ekstrakcji pokazujący rozpoznane pola z ocenami pewności obok okna podglądu dokumentu"><figcaption></figcaption></figure>

## Formatowanie kwot

W sekcji **Formatowanie kwoty** masz dwie opcje:

* **Zezwalaj na zaokrąglanie podczas porównywania kwot:**\
  Jeśli ta opcja jest włączona, podczas porównywania ilości dozwolona jest tolerancja ±0.5.\
  Jeżeli opcja jest wyłączona, obowiązuje domyślna tolerancja ±0.05.
* **Wymagaj dokładnego dopasowania do porównania kwot:**\
  Jeśli ta opcja jest włączona, kwoty muszą dokładnie odpowiadać zerowej tolerancji.\
  Jeśli opcja jest wyłączona, dozwolona jest tolerancja ±0.05.

<mark style="color:red;">**Uwaga**</mark>: Tylko jedno z tych ustawień może być aktywne w danym momencie.

## Ekstrakcja tabeli

{% hint style="info" %}
**Warunki wstępne działającej ekstrakcji tabeli**

* Typ dokumentu ma **kolumny tabeli** (Ustawienia → Ustawienia globalne → Typy dokumentów → [Kolumny tabeli](../../global-settings/document-types/table-columns/README.md)). Bez kolumn nie ma do czego wyodrębniać.
* Poniżej włączona jest opcja **Ekstrakcja tabeli** lub **Ekstrakcja tabeli AI**, dla całej organizacji.
* Dokument ma czytelny tekst: wykonano OCR albo dla plików PDF utworzonych cyfrowo używany jest E-Text ([Ustawienia OCR](../ocr-settings.md)).
* Szkolenie i modele AI działają **dla każdego dostawcy osobno**. Wytrenowana tabela dotyczy tylko dokumentów dostawcy, na którym została wytrenowana.
{% endhint %}

Tabele z dokumentów można wyodrębniać, włączając opcję **Ekstrakcja tabeli** lub **Ekstrakcja tabeli AI**. Wytrenowana tabela (oparta na AI lub ręczna) jest zawsze powiązana z konkretnym dostawcą.

**Ekstrakcja tabeli (Table Extraction):** Włącza ekstrakcję tabeli opartą na regułach. Tabele trenuje się dla każdego dostawcy na ekranie walidacji (*Go to table extraction view*).\
Więcej o szkoleniu [tutaj](../../../setup/document-training/training-line-fields-table-training/defining-tables-and-columns.md).

**Ekstrakcja tabeli AI (AI Table Extraction):** Wykorzystuje AI do wyodrębniania tabeli dowolnego dostawcy bez szkolenia. Jeśli wyniki dla jednego dostawcy nie są wystarczająco dokładne, wytrenuj tabelę tego dostawcy; zapisane reguły mają wtedy pierwszeństwo przed AI dla tego dostawcy.

**Użyj wizji ekstrakcji tabeli (AI):** AI odczytuje obraz strony zamiast warstwy tekstowej. Pomaga przy dokumentach skanowanych i tabelach bez wyraźnej struktury tekstowej; działa wolniej. Rozwijana lista obok przełącznika określa, jak intensywnie używany jest obraz strony:

* **Wyłączone (tylko tekst)** – Używana jest tylko warstwa tekstowa. To ustawienie domyślne.
* **Tylko obrazy** – Odczytywany jest wyłącznie obraz strony.
* **Hybrydowy (tekst i obrazy)** – Warstwa tekstowa i obraz strony są łączone w tym samym żądaniu.
* **Auto (decydowane dla każdego dokumentu)** – DocBits decyduje dla każdego dokumentu osobno, czy warstwa tekstowa wystarcza.

Tryb jest zapisywany pod kluczem preferencji `TABLE_EXTRACTION_VISION_MODE`; starszy przełącznik `TABLE_EXTRACTION_USE_VISION` pozostaje i oznacza w praktyce *Tylko obrazy*.

**Użyj ekstrakcji strukturalnej (AI):** AI zwraca tabelę w stałej strukturze, która mapuje się bezpośrednio na skonfigurowane kolumny tabeli. Zalecane, gdy nagłówki kolumn na dokumentach mocno się różnią. Kliknięcie tego ustawienia otwiera podgląd tego, o jakie pola i kolumny AI zostanie dokładnie poproszona: pola nagłówka oraz kolumny wierszy są wymienione wraz z ich źródłem (żądane albo wyłączone pola standardowe) wraz z oczekiwanym trybem wyjścia (na przykład *strict* – bez dodatkowych kolumn). Pola skonfigurowane dla typu dokumentu, ale wyłączone, nie są żądane od AI.

**Ekstrakcja tabeli dla elementu kosztowego (Table Extraction for Costing Element):** Po włączeniu DocBits może wyodrębniać elementy kosztowe z tabel na poziomie pozycji i odpowiednio je klasyfikować.\
Szczegółowe wyjaśnienie [tutaj](table-extraction-for-costing-element.md).

**Automatyczne wyodrębnianie kodu podatkowego (Auto Extract Tax Code):** Po włączeniu system automatycznie wypełnia pole **Kod podatkowy** na ekranie walidacji, pod warunkiem że pole kodu podatkowego jest skonfigurowane.\
Więcej informacji o tym ustawieniu [tutaj](auto-extract-tax-code.md).

**Zapisywanie reguł ekstrakcji (tylko administrator) (Save extraction rules (Admin only)):** Tylko administratorzy mogą kliknąć *Save Rules* w szkoleniu tabeli. Włącz tę opcję, gdy użytkownicy zapisują reguły, które psują ekstrakcję dostawcy.

**Model sztucznej inteligencji:** Wybiera poziom AI używany do ekstrakcji tabeli. Dostępnych jest sześć opcji: **Full** (najwyższa dokładność, najwolniejsza, 2 tokeny na dokument), **Fast** (domyślna; 1 token na dokument), **Nexus** i **Nexus Flash** (alternatywna rodzina modeli, opcjonalnie) oraz **Auto** i **Auto Nexus**, w których DocBits decyduje dla każdego dokumentu, jak silny model jest potrzebny. Tabela pod selektorem pokazuje:

* Którzy **dostawcy** używają którego modelu AI
* Czy używają ekstrakcji strukturalnej (AI) i E-Textu
* Opcje usunięcia wpisu i zresetowania w ten sposób dostawcy do wartości domyślnej

To ustawienie jest szczegółowo opisane [tutaj](ai-model.md).

### Dlaczego tabela wygląda inaczej u każdego dostawcy?

Wszystko, czego DocBits uczy się o tabeli, jest zapisywane **dla każdego dostawcy osobno**:

* **Zapisane reguły** (szkolenie tabeli): położenie tabeli i mapowanie jej kolumn w układzie tego dostawcy.
* **Tagi tabeli AI i reguły formatowania**: wskazówki zapisane przez użytkownika dla tabeli AI tego dostawcy.
* **Model AI specyficzny dla dostawcy**: poziom wybrany dla tego dostawcy w *Więcej ustawień* na ekranie walidacji.

Dlatego dostawca A z zapisanymi regułami pokazuje deterministyczną tabelę w zakładce *Extracted table* na ekranie walidacji, a dostawca B bez reguł otrzymuje zakładkę *AI Extracted table*. Aby dostawca B zachowywał się jak A, wytrenuj raz tabelę dostawcy B. Aby zresetować dostawcę, usuń jego reguły na ekranie walidacji albo zresetuj jego dane szkoleniowe w tabeli Model AI.

### Klucze preferencji

Każdy przełącznik w tej sekcji jest zapisywany jako preferencja organizacji. Użyj klucza, gdy ustawiasz wartość przez API (`/preferences/set_preference`), skrypt lub DocBits MCP (`get_preference` / `set_preference`).

| Ustawienie (etykieta w interfejsie) | Klucz preferencji | Wartości |
|---|---|---|
| Table Extraction | `TABLE_EXTRACTION_SETTING` | `true` / `false` |
| AI Table extraction | `USE_AI_TABLE_EXTRACTION` | `true` / `false` |
| Use Table Extraction Vision (AI) | `TABLE_EXTRACTION_VISION_MODE` | `off` (domyślnie), `vision`, `hybrid`, `auto` |
| Use Table Extraction Vision (AI) – starszy przełącznik | `TABLE_EXTRACTION_USE_VISION` | `true` / `false`; oznacza w praktyce `vision` |
| Użyj wyodrębnienia strukturalnego (AI) | `USE_STRUCTURED_EXTRACTION` | `true` / `false` |
| Ekstrakcja tabeli dla elementu kosztorysowego | `CHARGES_TABLE_EXTRACTION` | `true` / `false` |
| Automatyczne wyodrębnianie kodu podatkowego | `AUTO_EXTRACT_TAX_CODE` | `true` / `false` |
| Zapisz reguły wyodrębniania (tylko administrator) | `ONLY_ADMIN_CAN_SAVE_RULES` | `true` / `false` |
| Model sztucznej inteligencji | `AI_MODEL` | `gpt-6-sol` (Full), `gpt-6-luna` (Fast), `qwen3.8-max` (Nexus), `glm-5.3-flash` (Nexus Flash), `auto` (Auto), `auto-nexus` (Auto Nexus) |
| Wersja ekstrakcji tabeli (okno potwierdzenia) | `TBL_EXT_VERSION` | ciąg wersji |
| Ustawienia OCR → Use AI data for tables if available | `USE_AI_DATA_FOR_TABLE` | `true` / `false` |
| Ustawienia OCR → Use E-Text if available | `USE_ETEXT_IF_AVAILABLE` | `true` / `false` |

Uwagi:

* Preferencje logiczne są zapisywane jako ciągi `true` / `false`; klucz, który nigdy nie został ustawiony, liczy się jako `false`. Jeśli wyślesz `1` lub `0`, DocBits zapisze `true` / `false`.
* Nieustawiony `AI_MODEL` oznacza **Fast**.
* Nieustawiony `TABLE_EXTRACTION_VISION_MODE` jest wyznaczany ze starszego przełącznika `TABLE_EXTRACTION_USE_VISION`: `true` daje `vision`, każda inna wartość daje `off`.
* Zmiana klucza obowiązuje dla dokumentów przetwarzanych później. Uruchom dokument ponownie, aby wyodrębnić go ponownie z nowym ustawieniem.
* Wybory dla poszczególnych dostawców (E-Text, model AI, zapisane reguły) nie są preferencjami organizacji; ustawia się je na ekranie walidacji w *Więcej ustawień* dla dokumentu tego dostawcy.

## Dokument elektroniczny

**Przetwarzaj nieobsługiwane pliki PDF ZUGFeRD:** Jeśli ta opcja jest włączona, nieobsługiwane wersje **ZUGFeRD** będą przetwarzane jako standardowe pliki PDF, a osadzone XML będą ignorowane.

Listę obsługiwanych wersji **ZUGFeRD** można znaleźć [tutaj](../../global-settings/document-types/edi/zugferd/README.md).

## **Reguły klasyfikacji**

W sekcji **Zasady klasyfikacji** możesz zdefiniować konkretne wzorce i kryteria **regex**, które pomogą systemowi automatycznie klasyfikować dokumenty podczas przetwarzania.

Aby uzyskać dostęp do tej sekcji, kliknij zakładkę **Zasady klasyfikacji** u góry strony.

<figure><img src="../../../../.gitbook/assets/classification_and_extraction_1.png" alt="Strona ustawień Classification And Extraction z zakładkami Allgemein, Klassifizierungsregeln i AI-Modelle oraz lewą nawigacją niemieckich ustawień DocBits"><figcaption></figcaption></figure>

### **Dodaj nową regułę klasyfikacji**

Aby utworzyć nową regułę:

1.  Kliknij **Dodaj** w prawym górnym rogu.

    <figure><img src="../../../../.gitbook/assets/classification_and_extraction_2.png" alt="Strona ustawień ekstrakcji pokazująca listę mapowania pól z nazwami kolumn, polami wejściowymi i przyciskiem Speichern"><figcaption></figcaption></figure>
2. Wypełnij następujące pola:
   * **Wzorzec**: Wzorzec wyrażenia regularnego, którego system powinien szukać, aby wywołać klasyfikację.
   * **Type**: Gdzie należy szukać wzorca (np. **Kod kreskowy**).
   * **Podorganizacja** _(opcjonalnie)_: Określ, której organizacji podrzędnej dotyczy reguła.
   * **Typ dokumentu**: Określ typ dokumentu, który ma zostać przypisany po dopasowaniu wzorca.
   *   **Podtyp dokumentu** _(opcjonalnie)_: Określ podtyp w celu uzyskania bardziej szczegółowej klasyfikacji.

       <figure><img src="../../../../.gitbook/assets/classification_and_extraction_3.png" alt="Strona Zuordnung von Dokumententypen z listą rozwijaną Bereich oraz przełącznikami No Classification, No Splitting i Database Sharing-Klassifikation"><figcaption></figcaption></figure>
3.  Kliknij **Zapisz**, aby zapisać regułę klasyfikacji.

    <figure><img src="../../../../.gitbook/assets/classification_and_extraction_4.png" alt="Strona ustawień Classification And Extraction z zakładkami Allgemein, Klassifizierungsregeln i AI-Modelle, na pustym panelu AI-Modelle widnieje napis Kein Datensatz gefunden"><figcaption></figcaption></figure>

### **Edytuj regułę klasyfikacji**

Aby edytować istniejącą regułę:

1.  Kliknij trzy kropki w kolumnie **Akcje**.

    <figure><img src="../../../../.gitbook/assets/classification_and_extraction_5.png" alt="Strona ustawień Classification And Extraction z zakładkami Allgemein, Klassifizierungsregeln i AI-Modelle oraz lewą nawigacją niemieckich ustawień DocBits"><figcaption></figcaption></figure>
2.  Select **Edit**.

    <figure><img src="../../../../.gitbook/assets/classification_and_extraction_6.png" alt="Strona konfiguracji klasyfikacji z listą typów dokumentów, sekcją próbek treningowych i elementem do przesyłania"><figcaption></figcaption></figure>
3. Wprowadź żądane zmiany.
4.  Kliknij **Zapisz**, aby zastosować aktualizacje.

    <figure><img src="../../../../.gitbook/assets/classification_and_extraction_4.png" alt="Strona ustawień Classification And Extraction z zakładkami Allgemein, Klassifizierungsregeln i AI-Modelle, na pustym panelu AI-Modelle widnieje napis Kein Datensatz gefunden"><figcaption></figcaption></figure>

### **Usuń regułę klasyfikacji**

Aby usunąć regułę:

1.  Kliknij trzy kropki w kolumnie **Akcje**.

    <figure><img src="../../../../.gitbook/assets/classification_and_extraction_5.png" alt="Strona ustawień Classification And Extraction z zakładkami Allgemein, Klassifizierungsregeln i AI-Modelle oraz lewą nawigacją niemieckich ustawień DocBits"><figcaption></figcaption></figure>
2.  Select **Delete**.

    <figure><img src="../../../../.gitbook/assets/classification_and_extraction_7.png" alt="Ekran ustawień klasyfikacji z panelem sugestii typów dokumentów, wartościami pewności i listą pól po prawej stronie"><figcaption></figcaption></figure>

## Modele AI

Sekcja **Modele AI** wyświetla wszystkie specjalnie wytrenowane modele, które zostały specjalnie dostosowane do Twoich potrzeb.

### Dostęp do sekcji modeli AI

Aby otworzyć tę sekcję, kliknij zakładkę **Modele AI** znajdującą się na górze strony.

<figure><img src="../../../../.gitbook/assets/classification_and_extraction_8.png" alt="Strona Trainingsdaten z otwartą kartą Table Extraction pokazująca tabelę mapowania kolumn CSV z kolumnami Spalte, Typ i Werte"><figcaption></figcaption></figure>

### Kategorie modeli

Modele są podzielone na kategorie. Pod każdą nazwą kategorii pokazana jest liczba modeli, które zawiera.\
Kliknij kategorię, aby wyświetlić jej szczegóły.

<figure><img src="../../../../.gitbook/assets/classification_and_extraction_9.png" alt="Strona ustawień Classification And Extraction z zakładkami Allgemein, Klassifizierungsregeln i AI-Modelle, na pustym panelu AI-Modelle widnieje napis Kein Datensatz gefunden"><figcaption></figcaption></figure>

U góry strony wybranej kategorii zobaczysz najważniejsze informacje o każdym modelu:

* **Type**: Typ modelu.
* **Tylko pierwsza strona**: Wskazuje, czy model przetwarza tylko pierwszą stronę dokumentu.
* **Version**: Numer wersji modelu.

### Tabela modeli

Wszystkie modele w danej kategorii są wymienione w tabeli zawierającej następujące informacje:

* **Nazwa**: Nazwa modelu.
* **Następny model**: Model, który będzie dalej przetwarzał dane wyjściowe bieżącego modelu.
* **Typ dokumentu**: Podstawowy typ dokumentu przypisany przez model podczas klasyfikacji.
* **Podtypy dokumentów**: Podtypy, na które dokument jest dalej klasyfikowany.
* **Priority**: Poziom priorytetu określający pozycję modelu w kolejce klasyfikacyjnej.

<figure><img src="../../../../.gitbook/assets/classification_and_extraction_11.png" alt="Ekran walidacji z panelem sugestii klasyfikacji po lewej stronie i wyekstrahowaną tabelą z kolumnami Position, Menge i Preis"><figcaption></figcaption></figure>

### Edycja modelu

Aby edytować model:

1.  Kliknij ikonę pióra w kolumnie **Akcje** obok modelu, który chcesz edytować.

    <figure><img src="../../../../.gitbook/assets/classification_and_extraction_10.png" alt="Ekran ustawień klasyfikacji dokumentów z polami reguł ekstrakcji, listą rozwijaną wyboru modelu i przyciskiem zapisu"><figcaption></figcaption></figure>
2. Zaktualizuj dostępne pola:
   * **Następny model**: Wybierz model, który powinien przetwarzać dane wyjściowe z bieżącego modelu.
   * **Typ dokumentu**: Wybierz typ dokumentu, jako który model powinien klasyfikować dane wejściowe.
3.  Kliknij **Zapisz**, aby zastosować zmiany.

    <figure><img src="../../../../.gitbook/assets/classification_and_extraction_12.png" alt="Strona Trainingsdaten z zakładkami Language Models i Table Extraction oraz tabelą wytrenowanych modeli z kolumnami Name, Zugewiesene Dokumente, Datum i Bearbeiten"><figcaption></figcaption></figure>
