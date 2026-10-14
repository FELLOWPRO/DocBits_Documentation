# Reguły walidacji

<figure><img src="../../../../.gitbook/assets/edoc_validation_rules_setup.png" alt="Konfiguracja walidacji i akceptowane wersje"><figcaption><p>Konfiguracja walidacji i akceptowane wersje XRechnung</p></figcaption></figure>

Strona **Reguły walidacji** (**Dokumenty elektroniczne → Reguły**) kontroluje sposób, w jaki DocBits weryfikuje przychodzące e-faktury. Opiera się na oficjalnym zestawie reguł **KoSIT XRechnung + ZUGFeRD** oraz wewnętrznych kodach wyników walidatora i pozwala nadpisać wagę każdej reguły dla Twojej organizacji.

## Konfiguracja walidacji

Karta **Konfiguracja walidacji** pokazuje Twój bieżący profil walidacji (na przykład *B2G — Public Sector Receiver*). Kliknij **Edytuj odpowiedzi**, aby ponownie uruchomić kreatora konfiguracji i zmienić standard, względem którego prowadzona jest walidacja.

## Akceptowane wersje XRechnung

Bramka **Akceptowane wersje XRechnung** wymienia każdą wersję XRechnung. Zaznacz wersje, które akceptujesz — dokumenty, których CustomizationID znajduje się poza tą listą, są odrzucane z kodem `VAL-VERSION-NOT-ALLOWED` przed jakąkolwiek inną kontrolą. Pusta lista oznacza „akceptuj wszystko". Każda wersja jest oznaczona jako **current**, **deprecated** lub **EOL** wraz z datą wydania.

## Akceptowane profile i model wagi

<figure><img src="../../../../.gitbook/assets/edoc_validation_rules_severity.png" alt="Akceptowane profile i legenda wag"><figcaption><p>Akceptowane profile i znaczenie poszczególnych wag</p></figcaption></figure>

Wybierz, które **profile** akceptujesz (BASIC WL, BASIC, EN 16931 / COMFORT, EXTENDED, XRECHNUNG (CIUS)), używając przycisków **Akceptuj wszystko** / **Wyczyść**, a następnie **Zapisz**.

Każda reguła walidacji ma **wagę**, która decyduje, co się dzieje po jej uruchomieniu:

| Waga | Skutek |
|------|--------|
| **FATAL** | Natychmiast zatrzymuje przetwarzanie. Żadna kolejna warstwa nie jest sprawdzana; dokument przechodzi w stan Błąd. |
| **ERROR** | Dokument jest odrzucany. Pozostałe wyniki dla tego samego dokumentu są nadal pokazywane; powiadomienie dostawcy (jeśli włączone) jest wyzwalane. |
| **WARNING** | Pojawia się w raporcie walidacji, ale dokument przechodzi przez potok normalnie. |
| **INFO** | Tylko dziennik audytu. Brak widocznego efektu dla użytkownika i brak odrzucenia. |

## Nadpisywanie wag reguł

<figure><img src="../../../../.gitbook/assets/edoc_validation_rules_table.png" alt="Tabela reguł walidacji"><figcaption><p>Pełna tabela reguł z nadpisaniem wagi dla każdej reguły</p></figcaption></figure>

Tabela reguł wymienia każdą regułę walidacji (łącznie ponad 1600). Filtruj według **Warstwy (Layer)**, **Profilu** lub **Wersji** albo wyszukuj według kodu lub pola. Dla każdej reguły możesz nadpisać **Wagę** z listy rozwijanej, aby dopasować ją do polityki swojej organizacji — na przykład obniżyć regułę z `ERROR` do `WARNING`, aby nie odrzucała już dokumentu.
