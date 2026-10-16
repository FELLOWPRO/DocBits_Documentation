# And

Użyj karty **And**, aby zdecydować, czy przepływ pracy ma być kontynuowany po wyzwalaczu **When**. Dodaj kontrole, których potrzebujesz, przed akcją **Then**. Każda karta pokazuje pola do wypełnienia, takie jak **Operator**, **Field Name** lub **Value**; zrzuty ekranu przedstawiają dostępne szablony kart, a nie gotowe reguły.

W **Workflow Builder** wybierz **Add Card** pod **And...**. Wybierz kategorię po lewej stronie lub wpisz nazwę karty w polu **Search Card**. Wybierz podgląd karty, aby dodać ją do przepływu pracy. Możesz przewijać listę podglądów, aby zobaczyć więcej kart. Użyj **×**, aby zamknąć selektor bez wybierania kolejnej karty. Po skonfigurowaniu kart zapisz przepływ pracy. Zobacz [Workflow](../../), aby poznać otaczające kroki **When**, **And** i **Then**.

## Compare with Purchase Order

Użyj tych kart, aby porównać dane zamówienia lub faktury z zamówieniem zakupu, na przykład cenę jednostkową, obiecaną datę dostawy, opłaty lub ilość. Wybierz pola, operator i ewentualną tolerancję, o którą prosi wybrana karta. Poszczególne karty opisano w [Compare with Purchase Order](compare-with-purchase-order/).

<figure><img src="../../../../.gitbook/assets/and-category-po-comparison-en.png" alt="Selektor kart And w języku angielskim z wybraną kategorią Compare with Purchase Order; widoczne podglądy obejmują porównanie ceny jednostkowej, daty dostawy, opłat i ilości."><figcaption><p>Kategoria Compare with Purchase Order w angielskim środowisku Sandbox.</p></figcaption></figure>

## Document Field

Wybierz tę kategorię, aby sprawdzić pole wyboru lub status pola, porównać pole z wartością albo porównać dwa pola. Wypełnij pola zastępcze **Field Name** i **Operator** na wybranej karcie. Niektóre porównania wymagają także podania tolerancji. Zobacz [Document Field](document-field/).

<figure><img src="../../../../.gitbook/assets/and-category-document-field-en.png" alt="Selektor kart And w języku angielskim z wybraną kategorią Document Field; widoczne podglądy sprawdzają pole wyboru, status pola, wartości pól i porównania dwóch pól."><figcaption><p>Kontrole Document Field korzystają z wartości z bieżącego dokumentu.</p></figcaption></figure>

## Date & Time

Użyj **Date & Time**, aby porównać datę lub godzinę z zakresem albo porównać **Today** z wybraną datą. Wybierz **Operator** i wartości dat na karcie. Zobacz [Date & Time](date-and-time/).

<figure><img src="../../../../.gitbook/assets/and-category-date-time-en.png" alt="Selektor kart And w języku angielskim z wybraną kategorią Date &#x26; Time; dwa podglądy porównują datę lub godzinę z zakresem oraz porównują Today z datą."><figcaption><p>Date &#x26; Time oferuje kontrolę zakresu i kontrolę względem dzisiejszej daty.</p></figcaption></figure>

## Document

Użyj tych kart, gdy przepływ pracy ma zależeć od **typu dokumentu** lub **podorganizacji**. Wybierz typ lub organizację wskazaną na karcie. Zobacz [Document](document/).

<figure><img src="../../../../.gitbook/assets/and-category-document-en.png" alt="Selektor kart And w języku angielskim z wybraną kategorią Document; podglądy sprawdzają typ dokumentu i przynależność do podorganizacji."><figcaption><p>Warunki Document sprawdzają typ lub podorganizację.</p></figcaption></figure>

## Logic

Ta kategoria obejmuje kontrole z użyciem tabeli decyzyjnej, odpowiedzi HTTPS, dostępności modułu, ceny z oferty, wartości szansy lub dwóch wartości. Otwórz konkretną kartę i wypełnij jej nazwane pola zastępcze; na przykład karta HTTPS prosi o adres URL, metodę i akceptowany kod statusu. Zobacz [Logic](logic/).

<figure><img src="../../../../.gitbook/assets/and-category-logic-en.png" alt="Selektor kart And w języku angielskim z wybraną kategorią Logic; podglądy obejmują karty tabeli decyzyjnej, żądania HTTPS, aktywnego modułu, ceny z oferty, szansy i porównania wartości."><figcaption><p>Logic oferuje kilka różnych typów warunków; wybierz ten, który odpowiada Twojej regule.</p></figcaption></figure>

## Status

Użyj **Status**, aby sprawdzić, czy dokument ma wybrany status lub czy jego status należy do wybranego zbioru. Wybierz **Operator** i **Status** na karcie. Zobacz [Status](status/).

<figure><img src="../../../../.gitbook/assets/and-category-status-en.png" alt="Selektor kart And w języku angielskim z wybraną kategorią Status; dwa podglądy porównują Document status ze Status lub zbiorem statusów."><figcaption><p>Warunki Status sprawdzają bieżący stan dokumentu.</p></figcaption></figure>

## Table

Te karty badają wiersze tabeli dokumentu. Widoczne opcje obejmują kontrole dat, wzorce tekstowe, okres trwałości i porównania między kolumnami. Przed wybraniem operatora lub wzorca wybierz **Table name** i **Column Name**. Zobacz [Table](table/).

<figure><img src="../../../../.gitbook/assets/and-category-table-en.png" alt="Selektor kart And w języku angielskim z wybraną kategorią Table; widoczne podglądy obejmują datę, wzorzec regex, okres trwałości i porównania kolumn tabeli."><figcaption><p>Warunki Table korzystają z wierszy i kolumn tabeli dokumentu.</p></figcaption></figure>

## Compare with Quote Price

Użyj tych kart, aby porównać pozycję z danymi o cenie z oferty. Widoczne opcje obejmują identyfikator pozycji, typ dostawcy, identyfikator pozycji dostawcy, cenę jednostkową i jednostkę miary. **Operator** i pola zastępcze danych zależą od wybranej karty.

<figure><img src="../../../../.gitbook/assets/and-category-quote-price-en.png" alt="Selektor kart And w języku angielskim z wybraną kategorią Compare with Quote Price; pięć podglądów obejmuje identyfikator pozycji, typ dostawcy, identyfikator pozycji dostawcy, cenę jednostkową i jednostkę miary."><figcaption><p>Compare with Quote Price jest osobną kategorią w bieżącym selektorze kart.</p></figcaption></figure>

## Assignee

Użyj **Assignee**, gdy warunek zależy od przypisanego użytkownika lub grupy. Wybierz, czy porównywać z jednym użytkownikiem lub jedną grupą, czy z wybranym zbiorem. Zobacz [Assignee](assignee/).

<figure><img src="../../../../.gitbook/assets/and-category-assignee-en.png" alt="Selektor kart And w języku angielskim z wybraną kategorią Assignee; podglądy porównują przypisanego użytkownika lub grupę z jednym lub kilkoma wyborami."><figcaption><p>Warunki Assignee sprawdzają użytkownika lub grupę przypisaną do dokumentu.</p></figcaption></figure>
