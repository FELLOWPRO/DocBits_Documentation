# Pulpit

## Przegląd

Ustawienia panelu są zaprojektowane, aby pomóc administratorom kontrolować prezentację danych i interakcję w panelu DocBits. Te ustawienia określają, jakie informacje są natychmiast dostępne po zalogowaniu, zapewniając użytkownikom szybki dostęp do najważniejszych danych dla ich zadań.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/dashboard_settings_1.png)

## Uzyskiwanie dostępu do Ustawień Panelu

Aby uzyskać dostęp do ustawień panelu, przejdź do:\
**Ustawienia → Ustawienia globalne → Panel**

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_dashboard.png)

## **Ogólny**

* **Zresetuj filtry**: Umożliwia skonfigurowanie, kiedy filtry panelu powinny być resetowane, na przykład po przesłaniu dokumentu, ponownym uruchomieniu dokumentu lub eksporcie dokumentu. Pomaga to w utrzymaniu czystego widoku danych zgodnie z określonymi etapami pracy.
* **Dane pulpitu nawigacyjnego**:
  * **Automatyczne ładowanie pulpitu nawigacyjnego**: Kontroluje, czy panel powinien automatycznie ładować dane po uzyskaniu dostępu przez użytkownika, co może pomóc w skróceniu czasów ładowania i poprawie doświadczeń użytkownika poprzez ładowanie danych tylko wtedy, gdy są potrzebne.
  *   **Eksportuj dane pulpitu nawigacyjnego**: Ta funkcja dodaje nowy przycisk **Eksportuj** do paska narzędzi panelu, umożliwiając eksportowanie bieżącego widoku panelu jako pliku **.csv** lub **.xlsx**.

      ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/dashboard_settings_3.png)

## **Historia eksportu**

W **Historii eksportu** zobaczysz tabelę z listą wszystkich wcześniejszych eksportów wraz z kluczowymi informacjami o każdym żądaniu.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/dashboard_settings_4.png)

Zawarte są następujące szczegóły:

* **E-mail**: Adres e-mail, z którego żądano eksportu.
* **Status**: Bieżący status eksportu (Oczekujące, Zakończone).
* **Data żądania**: Data i godzina, kiedy eksport został zainicjowany.
* **Data zakończenia**: Data i godzina, kiedy eksport został zakończony.
* **Format**: Format pliku użyty do eksportu (CSV, XLSX).
* **Użyte filtry**: Jakiekolwiek filtry, które były zastosowane do panelu w momencie eksportu.

<mark style="color:red;">**Uwaga**</mark>: Aby eksportować tabele, opcja Eksportuj dane pulpitu nawigacyjnego w sekcji [Ogólny](./#ogolny) musi być aktywna.

## **Akcja**

* **Przypisz do**: Ta funkcja pozwala użytkownikom definiować uprawnienia do przypisywania dokumentów
  * **Tylko dla administratora**: Tylko użytkownicy z uprawnieniami administratora mogą przypisywać dokumenty, niezależnie od uprawnień przyznanych użytkownikom niebędącym administratorami.
  * **Wszyscy użytkownicy**: Wszyscy użytkownicy, którzy otrzymali niezbędne [uprawnienia](../groups-users-and-permissions/groups-and-permissions/activating-permissions.md), mogą przypisywać dokumenty.
* **Uruchom ponownie**: Ta funkcja pozwala użytkownikom definiować uprawnienia do ponownego uruchamiania dokumentów
  * **Tylko dla administratora**: Tylko użytkownicy z uprawnieniami administratora mogą ponownie uruchamiać dokumenty, niezależnie od uprawnień przyznanych użytkownikom niebędącym administratorami.
  * **Tylko administrator i przypisany**: Tylko użytkownicy z uprawnieniami administratora i przypisany użytkownik mogą ponownie uruchomić dokument.
  * **Wszyscy użytkownicy**: Wszyscy użytkownicy, którzy otrzymali niezbędne [uprawnienia](../groups-users-and-permissions/groups-and-permissions/activating-permissions.md), mogą ponownie uruchamiać dokumenty.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/dashboard_settings_2.png)

## **Filtry**

* **Styl filtra statusu**: Określa styl prezentacji filtrów statusu, który można ustawić na domyślny lub dostosowany zgodnie z operacyjnym skupieniem użytkowników.
* **Niestandardowy filtr statusu**: Umożliwia tworzenie i stosowanie niestandardowych filtrów, które mogą celować w konkretne statusy dokumentów, takie jak "Nowy", "Walidacja" lub "Eksportowanie". Umożliwia to użytkownikom szybki dostęp do dokumentów na określonych etapach przetwarzania.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/dashboard_settings_5.png)

## Panel zaawansowanej wysyłki

* **Widoczność dostarczonych zamówień**: Ta funkcja pozwala użytkownikowi określić czas, przez jaki dostarczone zamówienia będą widoczne.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/dashboard_settings_6.png)

Te ustawienia panelu są kluczowe dla zapewnienia, że platforma DocBits jest jak najbardziej responsywna i użyteczna, zapewniając użytkownikom potężne narzędzie do monitorowania i zarządzania aktywnościami przetwarzania dokumentów bezpośrednio z panelu.
