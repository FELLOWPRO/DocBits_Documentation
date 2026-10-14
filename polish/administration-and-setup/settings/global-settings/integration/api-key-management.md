---
description: >-
  Jak znaleźć i utworzyć klucze API, które dają innym systemom dostęp do DocBits
---

# API Key Management

Klucz API pozwala innemu systemowi — Twojemu ERP, skryptowi albo aplikacji partnera — rozmawiać z DocBits bez logowania się użytkownika. Twoja organizacja może mieć tyle kluczy, ile potrzebujesz, a każdy z nich jest zarządzany osobno: nadaj mu własną nazwę, zdecyduj, czy ma wygasać, i unieważnij go pojedynczo, jeśli kiedykolwiek zostanie ujawniony.

Ponieważ każda integracja może mieć własny klucz, możesz wyłączyć jeden bez zakłócania pozostałych.

## Otwieranie zarządzania kluczami API

Przejdź do **Settings** i wybierz **Integration & SSO** w sekcji **System & Administration**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/api-key-settings-overview.png)

Sekcja **API Key** na górze strony wymienia każdy klucz, jaki ma Twoja organizacja.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/api-key-list.png)

## Jak czytać listę

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/api-key-list-row.png)

| Kolumna | Co oznacza |
| --- | --- |
| **Key** | Kilka pierwszych znaków klucza, po których następuje `****`. Reszta nigdy nie jest pokazywana ponownie po utworzeniu — zobacz [Tworzenie klucza API](#tworzenie-klucza-api). |
| **Name** | Nazwa nadana kluczowi, a pod nią jego opis. |
| **Expires** | Data, w której klucz przestaje działać, albo **Never**, jeśli nie ustawiono żadnej. |
| **Last Used** | Kiedy ostatnio nadeszło żądanie z tym kluczem. **Never used** oznacza, że żaden system jeszcze go nie użył — przydatne do wychwytywania kluczy, które można bezpiecznie usunąć. |
| **Status** | **Active** oznacza, że klucz działa. Unieważniony klucz jest wyłączony na stałe. |
| **Actions** | Menu z trzema kropkami, w którym możesz unieważnić klucz. |

Jeśli masz więcej kluczy, niż mieści się na jednej stronie, użyj elementów stronicowania na dole listy.

{% hint style="info" %}
**Last Used** to najszybszy sposób na znalezienie kluczy, których już nikt nie potrzebuje. Klucz, który nigdy nie był używany albo nie był używany od miesięcy, to dobry kandydat do unieważnienia.
{% endhint %}

## Tworzenie klucza API

1. Kliknij **+ Create API Key** w prawym górnym rogu sekcji API Keys.
2. Wypełnij okno dialogowe:

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/api-key-create-dialog.png)

| Pole | Co wpisać |
| --- | --- |
| **Key Name** | Wymagane. Nazwij go od systemu, który będzie go używać — `M3 Production`, `Invoice Import Script` — żebyś później wiedział, do której integracji należy dany klucz. |
| **Description** | Opcjonalne. Miejsce na notatkę o tym, do czego służy klucz albo kto go skonfigurował. |
| **Expiration** | Wybierz datę wygaśnięcia albo zostaw **Never expires**. Data wygaśnięcia to bezpieczniejszy wybór: klucz wycofa się sam, jeśli o integracji kiedyś się zapomni. |

3. Kliknij **Create**. DocBits pokaże Ci nowy klucz:

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/api-key-created.png)

4. Skopiuj klucz ikoną kopiowania i wklej go prosto do systemu, który będzie go używać, albo do swojego menedżera haseł.
5. Zaznacz **I have copied and saved this key** i kliknij **Done**.

{% hint style="danger" %}
**Pełny klucz jest pokazywany tylko raz.** DocBits przechowuje go w zaszyfrowanej postaci, której nie da się odwrócić do oryginału, więc nikt — ani Twoi administratorzy, ani wsparcie DocBits — nie może go później odczytać. Jeśli go zgubisz, unieważnij klucz i utwórz nowy.
{% endhint %}

Traktuj klucz jak hasło. Każdy, kto go ma, może działać na dokumentach i danych Twojej organizacji.
