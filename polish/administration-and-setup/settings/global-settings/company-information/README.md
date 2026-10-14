# Informacje o firmie

<figure><img src="../../../../.gitbook/assets/company_information.png" alt="Formularz Company Information w angielskiej testowej organizacji DocBits Sandbox"><figcaption><p>Company Information: edytuj nazwę organizacji, adres, identyfikatory prawne i dane kontaktowe, a następnie wybierz Save.</p></figcaption></figure>

Strona Company Information pozwala zarządzać profilem firmy, preferencjami i szczegółami subskrypcji. Jest podzielona na następujące sekcje:

## Company Information

Ta sekcja zawiera podstawowe dane firmy, pogrupowane w cztery obszary:

### Company Identity

* **Name** *(wymagane)*: Prawna nazwa Twojej firmy.

### Address

* **Street + Number**: Adres ulicy Twojej firmy.
* **Postal Code**: Kod pocztowy.
* **City**: Nazwa miasta.
* **Country**: Wybierz swój kraj z listy rozwijanej.

### Legal Information

* **Company ID**: Unikalny identyfikator Twojej firmy, używany w integracjach i do wewnętrznych odniesień.
* **Tax ID**: Twój numer identyfikacji podatkowej na potrzeby sprawozdawczości finansowej.
* **Commercial Register ID**: Twój numer w rejestrze handlowym na potrzeby dokumentacji prawnej.

### Contact

* **Official Company Phone Number**: Główny numer telefonu Twojej firmy.
* **E-Mail**: Główny adres e-mail używany do oficjalnej komunikacji.

Po wprowadzeniu lub zaktualizowaniu dowolnych pól kliknij **Save**, aby zastosować zmiany. Ikony **?** obok identyfikatorów prawnych pokazują dodatkowe wskazówki dotyczące pól. Wybierz nagłówek sekcji, aby rozwinąć lub zwinąć formularz.

## E-mail domains

Administratorzy organizacji mogą otworzyć **Settings → Company Information → E-mail domains**, aby zarządzać domenami używanymi do automatycznego przypisywania do organizacji. Gdy ktoś loguje się przez Microsoft lub Google i nie jest jeszcze członkiem żadnej organizacji, DocBits może przypisać go do tej organizacji, jeśli jego adres e-mail używa jednej z wymienionych domen. Domena może należeć tylko do jednej organizacji.

<figure><img src="../../../../.gitbook/assets/company_email_domains_en.png" alt="Rozwinięta sekcja E-mail domains z pustą listą domen, polem wprowadzania i przyciskiem Add domain"><figcaption><p>Sekcja E-mail domains przed dodaniem domeny. Wprowadź domenę firmy, a następnie wybierz Add domain.</p></figcaption></figure>

Wprowadź w polu samą domenę, na przykład `example.com`, i wybierz **Add domain** lub naciśnij Enter. Pierwsza domena staje się domeną główną. Jeśli na liście jest więcej domen, użyj **Make primary** w innym wierszu, aby zmienić domenę główną, lub ikony kosza, aby usunąć domenę. Błędy, takie jak nieprawidłowa domena, prywatny dostawca poczty e-mail lub domena już przypisana gdzie indziej, pojawiają się pod polem wprowadzania. **No domains assigned yet** oznacza, że ta organizacja nie ma reguły domeny.

Przed dodaniem domeny sprawdź, która organizacja powinna przyjmować nowe logowania. Aby zarządzać istniejącymi członkostwami, przejdź do [Users](../groups-users-and-permissions/users/README.md).

## Company Preferences

Skonfiguruj domyślne ustawienia dla całej firmy:

* **Date Pattern**: Wybierz, w jaki sposób daty są wyświetlane w całym DocBits (np. `%m/%d/%Y`, `%d.%m.%Y`).
* **Amount Formatting**: Wybierz format liczbowy kwot (np. Deutsch dla `1.000,00`, English dla `1,000.00`).
* **New Version Info Dialog**: Określ, czy użytkownicy widzą powiadomienie o wydaniu nowej wersji DocBits.

Po wprowadzeniu zmian kliknij **Save**.

## App-Color

Dostosuj kolor podstawowy interfejsu DocBits. Jest to przydatne do wizualnego odróżniania różnych środowisk (np. dev od produkcyjnego).

* **Color**: Wprowadź kod koloru szesnastkowego (np. `#2388AE`) lub użyj próbnika kolorów.
* Kliknij **Save**, aby zastosować, lub **Reset**, aby przywrócić kolor domyślny.

## Subscription Plan

Wyświetl aktywne plany subskrypcji i ich szczegóły:

* **Plan Name**: Nazwa każdego aktywnego planu (np. DocBits, DocFlow Users, DocSearch).
* **Days Left**: Liczba dni pozostałych do wygaśnięcia planu.
* **Start Date / End Date**: Okres subskrypcji.
* **Users Count**: Łączna liczba użytkowników w Twojej organizacji.
* **Sub Organizations Count**: Liczba skonfigurowanych podorganizacji.
* **Suppliers Count**: Liczba zarejestrowanych dostawców.

## Subscription Usage

Monitoruj miesięczne zużycie tokenów i workflowów:

| Kolumna | Opis |
|--------|-------------|
| **Type** | Typ zużycia (Document lub Workflow). |
| **From / To** | Daty okresu rozliczeniowego. |
| **Tokens Used** | Liczba tokenów zużytych w bieżącym okresie. |
| **Remaining Tokens** | Tokeny nadal dostępne w bieżącym okresie. |

Użyj przycisku **Select**, aby filtrować według określonych zakresów dat.
