# Użytkownicy

<figure><img src="../../../../../.gitbook/assets/users_settings.png" alt="Zarządzanie użytkownikami"><figcaption><p>Strona zarządzania użytkownikami</p></figcaption></figure>

Strona Użytkownicy pozwala administratorom zarządzać wszystkimi kontami użytkowników w Twojej organizacji DocBits. Tutaj możesz dodawać nowych użytkowników, przypisywać role i kontrolować dostęp.

## Lista użytkowników

Tabela użytkowników zawiera następujące kolumny:

| Kolumna | Opis |
|--------|-------------|
| **Imię i nazwisko** | Pełne imię i nazwisko użytkownika. |
| **E-mail** | Adres e-mail użytkownika, używany jako identyfikator logowania. |
| **Ostatnie logowanie** | Data i godzina ostatniego logowania użytkownika. |
| **Admin** | Pole wyboru wskazujące, czy użytkownik ma uprawnienia administratora. Administratorzy mają dostęp do wszystkich ustawień i mogą zarządzać innymi użytkownikami. |
| **System Admin** | Pole wyboru oznaczające jedynego w organizacji użytkownika System Admin — konto, którego DocBits używa do automatycznych działań wykonywanych w tle (takich jak automatyczne importy i eksporty). System Admin zawsze posiada również uprawnienia Admin. Zobacz [Uprawnienia administratora](admin-privileges.md#admin-vs-system-admin), aby poznać różnicę między rolami Admin i System Admin. |
| **Aktywny** | Pole wyboru pokazujące, czy konto użytkownika jest obecnie aktywne. Nieaktywni użytkownicy nie mogą się zalogować. |
| **Działania** | Menu z opcjami takimi jak edycja danych użytkownika, resetowanie haseł lub dezaktywacja konta. |

Użyj paska **Szukaj** u góry, aby szybko znaleźć użytkowników po imieniu, nazwisku lub identyfikatorze.

## Analiza logowań

Kliknij **Analiza logowań**, aby wyświetlić dane o aktywności logowania w całej organizacji, w tym częstotliwość i wzorce logowania.

Zobacz [Analiza logowań](login-analytics.md), aby poznać pełne szczegóły.

## Dodawanie nowego użytkownika

1. Kliknij przycisk **Dodaj użytkownika** w prawym górnym rogu.
2. Wypełnij wymagane informacje:
   * **Nazwa użytkownika**: Unikalna nazwa dla użytkownika.
   * **Imię** i **Nazwisko**: Pełne imię i nazwisko użytkownika.
   * **Adres e-mail**: Używany do logowania i powiadomień.
   * **Hasło**: Musi być zgodne z zasadami bezpieczeństwa Twojej organizacji.
   * **Rola użytkownika**: Przypisz odpowiednią rolę (Standard User, Admin lub System Admin).
3. Kliknij **Zapisz**, aby utworzyć konto użytkownika. Nowy użytkownik otrzyma powiadomienie e-mail z danymi do logowania.

> **Uwaga:** Rolę **System Admin** można wybrać wyłącznie podczas tworzenia użytkownika — nie da się jej dodać ani usunąć później. Każda organizacja może mieć tylko jednego System Admina, a jego wybór automatycznie nadaje również uprawnienia Admin. Zobacz [Uprawnienia administratora](admin-privileges.md#admin-vs-system-admin), aby dowiedzieć się, kiedy z niej korzystać.
