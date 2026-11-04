# Walidacja e-faktury

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/einvoice-validation/v1/pl.mp4" %}

Strona **Walidacja e-faktury** (**Ustawienia → Dokumenty elektroniczne → Walidacja e-faktury**, ścieżka `/settings/einvoice-validation`; wcześniej nazywana *Reguły walidacji*) kontroluje sposób, w jaki DocBits weryfikuje przychodzące e-faktury. Opiera się na oficjalnym zestawie reguł **KoSIT XRechnung + ZUGFeRD** oraz wewnętrznych kodach wyników walidatora i pozwala nadpisać poziom ważności każdej reguły dla Twojej organizacji.

> Ta strona dotyczy **e-faktur** (XRechnung, ZUGFeRD, Factur-X). To coś innego niż **Reguły walidacji danych**, które sprawdzają wyodrębnione pola dokumentu.

## Co znajdziesz na tej stronie

<figure><img src="../../../../.gitbook/assets/einvoice-validation-settings-pl-20261104.png" alt="Walidacja i blokowanie według typu dokumentu. Skonfigurowane nazwy są ukryte. Przykład z Dev. W tej wersji niektóre teksty interfejsu mogą nadal być po angielsku lub mieć błędne tłumaczenie. Instrukcja wyjaśnia ich znaczenie; zrzuty pokazują niezmieniony interfejs."><figcaption><p>Walidacja i blokowanie według typu dokumentu. Skonfigurowane nazwy są ukryte. Przykład z Dev. W tej wersji niektóre teksty interfejsu mogą nadal być po angielsku lub mieć błędne tłumaczenie. Instrukcja wyjaśnia ich znaczenie; zrzuty pokazują niezmieniony interfejs.</p></figcaption></figure>

| Temat | Co robi | Kto |
| --- | --- | --- |
| [Konfiguracja walidacji i akceptowane wersje](validation-setup.md) | Kreator konfiguracji, akceptowane wersje XRechnung, akceptowane profile i znaczenie każdego poziomu ważności. | Administratorzy organizacji |
| [Poziomy ważności reguł](validation-rule-severities.md) | Tabela reguł: zmień poziom ważności każdej reguły dla swojej organizacji. | Administratorzy organizacji |
| [Walidacja dla każdego typu dokumentu](validation-per-document-type.md) | Włącz walidację (**Włączony**) i zdecyduj, czy nieudana kontrola zatrzymuje dokument (**Blokowanie**). Każda zmiana wymaga potwierdzenia. | Administratorzy organizacji |
| [Dziennik zmian](validation-change-log.md) | Każda zmiana ustawień: kiedy, kto, jaka reguła, od → do. | Administratorzy organizacji |
| [Ekran błędu odrzuconej e-faktury](validation-error-screen.md) | Co widzisz po wgraniu błędnego pliku XML: wyjaśnienie, błędna linia i następny krok. | Wszyscy, którzy przetwarzają faktury |
| [Raport walidacyjny](validation-report.md) | Co widzi użytkownik, gdy faktura nie przejdzie kontroli: wyniki prostym językiem. Raport otwiera się z dokumentu, a nie z tej strony. | Wszyscy, którzy przetwarzają faktury |
| [Następny krok i odrzucenie dokumentu](validation-next-step-and-reject.md) | Co zrobić po przeczytaniu raportu, pobieranie raportu i **Odrzuć dokument**. | Wszyscy, którzy przetwarzają faktury |
