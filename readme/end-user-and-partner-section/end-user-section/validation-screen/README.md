# Ekran Walidacji

{% embed url="https://youtu.be/CmmQIxOaF6E?si=gYE-U-Jv4dLPi2xT" %}

## Przegląd

<figure><img src="../../../.gitbook/assets/validation_screen1.png" alt=""><figcaption></figcaption></figure>

### **Przycisk Zapisz:**

<figure><img src="../../../.gitbook/assets/validation_screen2.png" alt=""><figcaption></figcaption></figure>

* **Przycisk Zapisz:**
  * **Cel:** Zapisuje bieżący stan dokumentu lub skryptu, nad którym pracujesz.
  * **Przypadek użycia:** Po wprowadzeniu zmian lub adnotacji do dokumentu, użyj tego przycisku, aby upewnić się, że wszystkie modyfikacje zostały zapisane.

### **Dodaj specjalne zasady:**

<figure><img src="../../../.gitbook/assets/validation_screen3.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/validation_screen4.png" alt=""><figcaption></figcaption></figure>

* **Dodaj specjalne zasady / Dodaj skrypt w DocBits:**
  * **Cel:** Umożliwia użytkownikom wdrażanie specyficznych zasad lub skryptów, które dostosowują sposób przetwarzania dokumentów.
  * **Przypadek użycia:** Użyj tej funkcji, aby zautomatyzować zadania takie jak ekstrakcja danych lub walidacja formatu, zwiększając efektywność pracy.

{% hint style="info" %}
Zobacz tutaj dodaj [Skrypt w DocBits](../../../administration-and-setup/settings/global-settings/document-types/script/scripting-in-docbits/)
{% endhint %}

### **Pola rozmyte:**

<figure><img src="../../../.gitbook/assets/validation_screen5.png" alt=""><figcaption></figcaption></figure>

* **Pola rozmyte:**
  * **Cel:** Pomaga w identyfikacji i korekcie pól, gdzie dane mogą nie być idealnie dopasowane, ale są wystarczająco bliskie.
  * **Przypadek użycia:** Przydatne w procesach walidacji danych, gdzie dokładne dopasowanie nie zawsze jest możliwe, na przykład w przypadku lekko błędnie napisanych nazwisk lub adresów.

### **Pola wymagane:**

<figure><img src="../../../.gitbook/assets/validation_screen6.png" alt=""><figcaption></figcaption></figure>

Istnieją pola, które są wymagane do dalszej edycji, można je edytować w ustawieniach.

Użyj podpowiedzi, aby dowiedzieć się, czy:

* Jest to pole obowiązkowe (wymagane)
* Wymagana walidacja
* Niska pewność
* Niezgodność pełnej kwoty podatku

**Pola wymagane:**

* **Cel:** Identyfikuje obowiązkowe pola w dokumentach, które muszą być wypełnione lub poprawione przed dalszym przetwarzaniem.
* **Przypadek użycia:** Zapewnia, że niezbędne dane są dokładnie uchwycone, utrzymując integralność danych i zgodność z zasadami biznesowymi.

## Wyodrębniona tabela (pozycje)

<figure><img src="../../../.gitbook/assets/validation_screen_line_items_table.png" alt="Tabela pozycji na ekranie walidacji z paskiem narzędzi tabeli"><figcaption><p>Wyodrębniona tabela pod polami nagłówka</p></figcaption></figure>

Pod polami nagłówka DocBits wyświetla tabelę pozycji dokumentu: jeden wiersz na pozycję faktury, jedna kolumna na każdą [kolumnę tabeli](../../../administration-and-setup/settings/global-settings/document-types/table-columns.md) skonfigurowaną dla typu dokumentu. Jeśli typ dokumentu ma kilka tabel (na przykład pozycje i opłaty), każda tabela ma własną zakładkę nad siatką.

### Skąd pochodzi tabela

Nad siatką znajduje się jedna zakładka dla każdej ścieżki ekstrakcji włączonej w organizacji:

| Zakładka | Znaczenie |
|---|---|
| **Extracted table** (Wyodrębniona tabela) | Ekstrakcja oparta na regułach (ustawienie *Table Extraction*). U dostawcy z wytrenowaną tabelą wiersze pochodzą z zapisanych reguł i są wyodrębniane tak samo na każdym dokumencie tego dostawcy; u niewytrenowanego dostawcy zakładka może być pusta. |
| **AI Extracted table** (Tabela wyodrębniona przez AI) | Ekstrakcja tabeli AI (ustawienie *AI Table Extraction*). Wypełniana, gdy dostawca nie ma zapisanych reguł, oraz dla kolumn oznaczonych *Use AI* nawet wtedy, gdy reguły istnieją. Podpowiedź *AI table not found* na zakładce oznacza, że AI nie zwróciło niczego dla tego dokumentu. |
| **PO Tables** (Tabele PO) | Tylko w kreatorze układu: pozycje zamówienia zakupu użyte do dopasowania. |

Jeśli nie widać żadnej z zakładek, oba ustawienia tabeli są wyłączone dla organizacji (Ustawienia → Przetwarzanie dokumentów → Klasyfikacja i ekstrakcja). Poziom AI odczytujący tabelę jest ustawiany dla organizacji i można go nadpisać dla dostawcy, patrz [Model AI specyficzny dla dostawcy](supplier-specific-ai-model-for-field-and-table-extraction.md).

### Praca w tabeli

* **Edycja komórki**: kliknij komórkę i wpisz wartość. Kolumny kwot, liczb i dat są sprawdzane podczas wpisywania.
* **Add new table row** (Dodaj nowy wiersz tabeli): dodaje pusty wiersz na końcu. Użyj, gdy pozycja nie została rozpoznana.
* **Usuwanie wiersza**: ikona kosza na końcu wiersza.
* **Add empty mapped columns** (Dodaj puste zmapowane kolumny): pokazuje skonfigurowane kolumny, które AI pozostawiło puste, aby można je było wypełnić ręcznie.
* **Restore Table Column** (Przywróć kolumnę tabeli): przywraca kolumnę usuniętą z widoku dla tego dokumentu.
* **Delete table** (Usuń tabelę): czyści wszystkie wiersze tej tabeli na tym dokumencie. Konfiguracja pozostaje nietknięta.
* **Add new table column** (Dodaj nową kolumnę tabeli, administratorzy): to samo okno dialogowe co w ustawieniach kolumn tabeli, bez opuszczania dokumentu.
* **Tags** (Tagi, tylko tabela AI): krótkie wskazówki tekstowe dla AI, na przykład *"ostatnia kolumna to kwota netto"*. Patrz [Tagowanie tabeli AI](../ai-table/ai-table-tags.md).
* **Apply** / **Save** / **Delete** obok tagów: *Apply* ponownie uruchamia tabelę AI dla tego dokumentu z wprowadzonymi tagami i zmianami kolumn, bez zapisywania czegokolwiek (jeśli dokument ma pozycje dopasowane do PO, DocBits ostrzega, że dopasowania zostaną usunięte); *Save Rules* zapisuje bieżące mapowanie kolumn i tagi dla tego dostawcy; *Delete Rules* usuwa je i ponownie uruchamia ekstrakcję AI dla tego dokumentu.
* **Export** (Eksport): pobiera tabelę jako plik CSV.
* **Go to table extraction view** (Przejdź do widoku ekstrakcji tabeli): otwiera szkolenie tabeli dla tego dokumentu. Użyj, gdy ten sam dostawca wciąż wychodzi źle: zaznacz tabelę raz, zmapuj kolumny i kliknij *Save Rules*; od tej pory wiersze pojawiają się w zakładce *Extracted table*. Patrz [Szkolenie pól linii / Szkolenie tabeli](../../../administration-and-setup/setup/document-training/training-line-fields-table-training/README.md).

{% hint style="info" %}
Jeśli tabela została wyodrębniona przez AI i otworzysz szkolenie tabeli, DocBits zapyta *Table is already extracted by AI. Do you want to train manually?* Po zapisaniu reguł tabela AI nie jest już używana dla tego dostawcy.
{% endhint %}

### Ponowna ekstrakcja tabeli

* **Ten sam dokument, tabela AI:** dodaj lub zmień tagi i kliknij **Apply**; tabela AI jest odbudowywana tylko dla tego dokumentu. Aby usunąć także zapisane tagi i formatowanie dostawcy, kliknij **Delete** (*Delete Rules*): DocBits potwierdza *Rules has been deleted successfully* i ponownie uruchamia ekstrakcję AI.
* **Ten sam dokument, wytrenowane reguły:** otwórz *Go to table extraction view*, popraw tabelę i kliknij *Save & re-extract*.
* **Cały dokument ponownie (nagłówek i tabela):** Pulpit → menu dokumentu → *Restart* (Uruchom ponownie). Potrzebne po zmianie kolumn tabeli lub ustawień ekstrakcji przez administratora.

### Co blokuje zatwierdzenie

Tabela jest sprawdzana przy zapisie lub zatwierdzaniu. Czerwona komórka lub komunikat pod tabelą oznacza jedną z poniższych sytuacji:

| Komunikat | Przyczyna | Co zrobić |
|---|---|---|
| Pusta wymagana kolumna | Kolumna oznaczona *Is Required* nie ma wartości w tym wierszu. | Wypełnij komórkę albo zapytaj administratora, czy kolumna musi być wymagana. |
| *Line total does not match quantity x unit price (expected …, got …)* | `ilość × cena jednostkowa + opłaty − rabat` różni się od sumy pozycji o więcej niż 0,02. Często jedna z czterech wartości została odczytana do niewłaściwej kolumny. | Popraw wartość, która nie zgadza się z dokumentem; jeśli kolumna taka jak *Charges* jest konsekwentnie wypełniana niewłaściwą wartością, zgłoś to administratorowi (patrz [Rozwiązywanie problemów](../../../administration-and-setup/settings/global-settings/document-types/table-columns.md#troubleshooting)). |
| *Line items add up to … but the net total is …* | Suma pozycji różni się od kwoty netto w nagłówku. | Sprawdź, czy nie brakuje wiersza, czy wiersz nie jest zdublowany albo czy kwota w nagłówku nie została źle odczytana. |
| *Line Item Table is missing Mandatory column for PO* | Dopasowanie PO wymaga numeru pozycji, ceny jednostkowej, ilości i kwoty całkowitej; jedna z tych kolumn jest ukryta. | Administrator: odkryj kolumnę w Kolumnach tabeli. |

Administrator może wyłączyć wszystkie kontrole tabeli dla typu dokumentu opcją *Pomiń walidację tabeli* (Typy dokumentów → Więcej ustawień); niezgodności pozycji i puste wymagane kolumny nie są wtedy zgłaszane.

Więcej o kontrolach: [Automatyczne kontrole na ekranie walidacji](automatic-checks-on-the-validation-screen.md) oraz [Rozwiązywanie problemów z ekstrakcją tabeli](../../../overview-and-basics/faq/document-processing/table-extraction-troubleshoot.md).

### **Szkło powiększające:**

<figure><img src="../../../.gitbook/assets/validation_screen7.png" alt=""><figcaption></figcaption></figure>

* **Szkło powiększające:**
  * **Cel:** Zapewnia powiększony widok wybranego obszaru dokumentu.
  * **Przypadek użycia:** Pomaga w badaniu drobnych szczegółów lub małego tekstu w dokumentach, zapewniając dokładność wprowadzania danych lub przeglądu.

<figure><img src="../../../.gitbook/assets/validation_screen8.png" alt="" width="329"><figcaption></figcaption></figure>

### **Otwórz nowe okno:**

<figure><img src="../../../.gitbook/assets/validation_screen9.png" alt="" width="130"><figcaption></figcaption></figure>

* **Otwórz nowe okno:**
  * **Cel:** Otwiera nowe okno do porównania dokumentów obok siebie lub do wielozadaniowości.
  * **Przypadek użycia:** Przydatne przy porównywaniu dwóch dokumentów lub przy odwoływaniu się do dodatkowych informacji bez opuszczania bieżącego dokumentu.

### **Skróty klawiszowe:**

<figure><img src="../../../.gitbook/assets/validation_screen10.png" alt="" width="145"><figcaption></figcaption></figure>

* **Skróty klawiszowe:**
  * **Cel:** Umożliwia użytkownikom szybkie wykonywanie działań za pomocą kombinacji klawiszy.
  * **Przypadek użycia:** Zwiększa szybkość i efektywność nawigacji i przetwarzania dokumentów, minimalizując zależność od nawigacji myszą.

<figure><img src="../../../.gitbook/assets/validation_screen11.png" alt="" width="239"><figcaption></figcaption></figure>

### **Zadania:**

<figure><img src="../../../.gitbook/assets/validation_screen12.png" alt="" width="55"><figcaption></figcaption></figure>

Aby udostępnić informacje wewnętrzne, możesz tworzyć zadania i przypisywać je do konkretnego pracownika lub grupy w firmie.

* **Zadania:**
  * **Cel:** Umożliwia użytkownikom tworzenie zadań związanych z dokumentami i przypisywanie ich członkom zespołu.
  * **Przypadek użycia:** Ułatwia współpracę i zarządzanie zadaniami w zespołach, zapewniając, że każdy zna swoje obowiązki.

<figure><img src="../../../.gitbook/assets/validation_screen13.png" alt="" width="218"><figcaption></figcaption></figure>

### **Tryb adnotacji:**

<figure><img src="../../../.gitbook/assets/validation_screen14.png" alt="" width="187"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/validation_screen15.png" alt=""><figcaption></figcaption></figure>

{% embed url="https://youtu.be/ay0gGtwlqRE" %}
DocBits Annotation Mode Tutorial: Add Notes in Validation & Download With/Without Annotations
{% endembed %}

Możesz zostawić adnotacje na dokumencie. Może to być pomocne, aby zostawić informacje dla innych użytkowników, którzy będą dalej edytować ten dokument.

* **Tryb adnotacji:**
  * **Cel:** Pozwala użytkownikom zostawiać notatki lub adnotacje bezpośrednio na dokumencie.
  * **Przypadek użycia:** Przydatne do udzielania informacji zwrotnych, instrukcji lub ważnych notatek dla innych członków zespołu, którzy będą pracować nad dokumentem później.

### **Scal:**

<figure><img src="../../../.gitbook/assets/validation_screen16.png" alt="" width="60"><figcaption></figcaption></figure>

Dokumenty można tutaj scalać, na przykład jeśli brakowało strony faktury, te strony można później scalić w ten sposób bez konieczności usuwania lub ponownego przesyłania całego dokumentu.

* **Scal dokumenty:**
  * **Cel:** Łączy wiele dokumentów w jeden plik.
  * **Przypadek użycia:** Przydatne w sytuacjach, gdy części dokumentu są skanowane osobno i muszą być skonsolidowane.

### **Widok OCR:**

<figure><img src="../../../.gitbook/assets/validation_screen17.png" alt="" width="77"><figcaption></figcaption></figure>

W widoku OCR tekst jest automatycznie filtrowany z dokumentu. Służy to do rozpoznawania istotnych cech, takich jak kod pocztowy, numer umowy, numer faktury i sortowanie dokumentu.

* **Widok OCR:**
  * **Cel:** Automatycznie rozpoznaje tekst w dokumentach za pomocą technologii rozpoznawania znaków optycznych.
  * **Przypadek użycia:** Usprawnia proces digitalizacji tekstów drukowanych lub pisanych ręcznie, czyniąc je przeszukiwalnymi i edytowalnymi.

<figure><img src="../../../.gitbook/assets/validation_screen18.png" alt=""><figcaption></figcaption></figure>

### **Utwórz zgłoszenie:**

<figure><img src="../../../.gitbook/assets/validation_screen19.png" alt="" width="97"><figcaption></figcaption></figure>

W przeciwieństwie do zadań, które są przekazywane wewnętrznie w firmie, to zgłoszenie wsparcia jest ważne, aby nas powiadomić i natychmiast utworzyć zgłoszenie w przypadku błędów i/lub rozbieżności. To znacznie ułatwia proces, ponieważ można od razu wysłać błąd z odpowiednim dokumentem. Istnieje również opcja ustawienia priorytetu, zrobienia zrzutu ekranu dokumentu lub przesłania go.

* **Utwórz zgłoszenie:**
  * **Cel:** Umożliwia użytkownikom zgłaszanie problemów lub rozbieżności poprzez tworzenie zgłoszenia wsparcia.
  * **Przypadek użycia:** Niezbędne do szybkiego rozwiązywania problemów i błędów, pomagając utrzymać integralność i płynne funkcjonowanie systemu.

<figure><img src="../../../.gitbook/assets/validation_screen20.png" alt="" width="237"><figcaption></figcaption></figure>

### **Logi skryptów dokumentów:**

<figure><img src="../../../.gitbook/assets/validation_screen21.png" alt="" width="160"><figcaption></figcaption></figure>

Skrypty można tworzyć w ustawieniach w sekcji Typy dokumentów; te informacje będą następnie wyświetlane tutaj.

* **Logi skryptów dokumentów:**
  * **Cel:** Wyświetla logi związane ze skryptami, które zostały wdrożone dla różnych typów dokumentów.
  * **Przypadek użycia:** Przydatne do śledzenia i debugowania działań skryptów na dokumentach, pomagając użytkownikom zrozumieć procesy automatyczne i poprawić wszelkie problemy.

<figure><img src="../../../.gitbook/assets/validation_screen22.png" alt=""><figcaption></figcaption></figure>

### **Więcej ustawień:**

<figure><img src="../../../.gitbook/assets/docbits_validation_screen_more_settings_menu.jpg" alt="Docbits Validation Screen More Settings Menu"><figcaption></figcaption></figure>

### **Przepływ dokumentu:**

Tam znajdziesz przepływ dokumentu

* **Cel:** Pokazuje sekwencję i postęp przetwarzania dokumentu w systemie.
* **Przypadek użycia:** Pomaga w śledzeniu statusu dokumentu przez różne etapy, zapewniając, że wszystkie niezbędne kroki przetwarzania są przestrzegane.

### **Przejdź do szablonu układu:**

* Dzięki tej opcji zostaniesz przekierowany i możesz edytować swój układ lub użyć domyślnego szablonu
* **Przejdź do szablonu układu:**
  * **Cel:** Przekierowuje użytkowników do edytora układu, gdzie mogą modyfikować istniejące szablony lub zastosować domyślny.
  * **Przypadek użycia:** Umożliwia dostosowanie układów dokumentów do spełnienia specyficznych potrzeb biznesowych lub preferencji, poprawiając wizualne i funkcjonalne dopasowanie dokumentu do standardów firmy.

### Użyj E-Text, jeśli dostępne

* **Cel:** Umożliwia DocBits korzystanie z e-text dla wszystkich dokumentów od konkretnego dostawcy, jeśli jest dostępny, poprawiając dokładność ekstrakcji.
* **Przykład użycia:** Zwiększa ekstrakcję tekstu, wykorzystując osadzone teksty zamiast OCR, co może prowadzić do dokładniejszych wyników dla tego dostawcy.

### [Model AI oparty na dostawcy](supplier-specific-ai-model-for-field-and-table-extraction.md)

* **Cel:** Umożliwia wybór pomiędzy trzema różnymi modelami AI w celu optymalizacji wyników ekstrakcji dla konkretnego dostawcy.
* **Przykład użycia:** Zapewnia lepszą dokładność ekstrakcji, wybierając najbardziej odpowiedni model AI dla struktury dokumentu i treści każdego dostawcy.
