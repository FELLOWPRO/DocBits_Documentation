---
hidden: true
noIndex: true
---

# E-mail

DocBits może importować dokumenty z poczty e-mail na dwa sposoby. Oba konfiguruje się w **Ustawienia → Import** (Przetwarzanie dokumentów).

## Metoda 1 — Import e-mail (podłączenie skrzynki)

Podłącz konto e-mail, a DocBits automatycznie zaimportuje dokumenty w momencie nadejścia nowych wiadomości. Na stronie Import otwórz sekcję **Import e-mail** i kliknij **+ Nowy**.

<figure><img src="../../../../.gitbook/assets/email_import_section.png" alt="Sekcja Import e-mail"><figcaption>Import e-mail — podłącz skrzynkę do automatycznego importu dokumentów</figcaption></figure>

Następnie wybierz protokół swojej skrzynki:

* **IMAP** — zobacz [IMAP](imap.md)
* **OAuth (Office 365)** — zobacz [OAuth Office365](oauth-office365.md)

## Metoda 2 — Wiadomości przychodzące (przekazywanie do DocBits)

Przekaż — lub wyślij bezpośrednio — wiadomości na unikalny adres przychodzący Twojej organizacji, a DocBits automatycznie zaimportuje załączniki. Podłączenie skrzynki nie jest wymagane. Otwórz sekcję **Wiadomości przychodzące** na stronie Import.

<figure><img src="../../../../.gitbook/assets/inbound_emails_section.png" alt="Sekcja Wiadomości przychodzące"><figcaption>Wiadomości przychodzące — przekazuj dokumenty na swój adres DocBits</figcaption></figure>

* **Info / E-mail** — unikalny adres przychodzący Twojej organizacji (format `<org-id>@inbound.docbits.com`). Przekazuj dokumenty na ten adres; użyj ikony kopiowania, aby go skopiować.
* **Importuj dokumenty tylko z predefiniowanych adresów e-mail** — gdy włączone, importowane są tylko wiadomości od nadawców dodanych do białej listy; wiadomości od innych nadawców są ignorowane.
* **Odpowiedz na tę wiadomość, jeśli import nie jest możliwy** — wysyła nadawcy automatyczną odpowiedź, gdy import się nie powiedzie.
* **Powiadom nadawcę, gdy import się nie powiedzie** — informuje nadawcę, jeśli jego wiadomości nie udało się zaimportować.
* **Dzienniki** — otwiera dziennik przetwarzania wiadomości przychodzących. Kliknij **Zapisz**, aby zastosować zmiany.
