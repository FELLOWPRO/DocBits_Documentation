# Dokumenty elektroniczne

DocBits weryfikuje przychodzące faktury elektroniczne (e-faktury) względem oficjalnych standardów — **XRechnung**, **ZUGFeRD** i **Factur-X** — oraz kieruje wszelkie wykryte problemy do właściwego odbiorcy. Grupa ustawień **Dokumenty elektroniczne** (w sekcji **Przetwarzanie dokumentów**) zawiera dwie strony:

* **[Reguły walidacji](validation-rules.md)** — wybierz, które wersje i profile e-faktur akceptujesz, oraz ustaw wagę każdej reguły walidacji dla swojej organizacji.
* **[Routing powiadomień](notification-routing.md)** — przypisz wyniki walidacji do agenta AI Workforce, który ma je obsłużyć.

Razem pozwalają zdecydować, **co jest uznawane za problem** na przychodzącej e-fakturze i **kto się tym zajmuje**.

## Włączanie lub wyłączanie walidacji e-faktur

Obie strony Dokumenty elektroniczne działają dopiero po **włączeniu walidacji e-faktur dla danego typu dokumentu**. Przełącznik znajduje się przy samym typie dokumentu, a nie w menu Dokumenty elektroniczne.

Przejdź do **Ustawienia → Typy dokumentów → Faktura → Ustawienia zaawansowane** i otwórz sekcję **Walidacja e-faktur**.

<figure><img src="../../../../.gitbook/assets/edoc_enable_validation_toggle.png" alt="Przełączniki walidacji e-faktur przy typie dokumentu Faktura"><figcaption><p>Włącz lub wyłącz walidację e-faktur dla każdego typu dokumentu, z opcjonalnym powiadomieniem dostawcy</p></figcaption></figure>

* **Waliduj przychodzące e-faktury** — przełącznik główny. Gdy jest **włączony**, każda przesłana faktura jest sprawdzana według reguł Schematron KoSIT XRechnung oraz kontroli semantycznych L0 (PDF/A-3) i L4 (IBAN/VAT), z wagami ustawionymi na stronie [Reguły walidacji](validation-rules.md). Nieprawidłowe faktury są blokowane. Gdy jest **wyłączony**, faktury całkowicie pomijają walidację e-faktur, a strony Reguły walidacji i Routing powiadomień nie mają żadnego efektu.
* **Powiadom dostawcę o odrzuceniu** — pojawia się po włączeniu walidacji. Gdy jest **włączony**, odrzucona faktura wyzwala e-mail do dostawcy z listą brakujących lub nieprawidłowych pól, aby mógł wystawić ją ponownie. To, kto otrzymuje i obsługuje każdy wynik, konfiguruje się na stronie [Routing powiadomień](notification-routing.md).

> Walidacja e-faktur jest konfigurowana **dla każdego typu dokumentu**. Obecnie dotyczy typu dokumentu **Faktura**; włącz ją dla każdego typu dokumentu, który ma być walidowany.

Możesz też przejść tutaj bezpośrednio za pomocą **globalnego szybkiego wyszukiwania**: naciśnij <kbd>Cmd</kbd> + <kbd>K</kbd> (<kbd>Ctrl</kbd> + <kbd>K</kbd> w systemach Windows i Linux) w dowolnym miejscu DocBits i wpisz *e-invoice*.

<figure><img src="../../../../.gitbook/assets/edoc_quicksearch_einvoice.png" alt="Globalne szybkie wyszukiwanie przechodzi do Walidacji e-faktur"><figcaption><p>Wpisz „e-invoice" w szybkim wyszukiwaniu, aby przejść bezpośrednio do przełącznika.</p></figcaption></figure>
