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

## Obsługiwane załączniki dokumentów

Obie metody importu e-mail przyjmują następujące załączniki dokumentów:

| Format | Rozszerzenia plików | Typowe zastosowanie |
| --- | --- | --- |
| PDF | `.pdf` | Faktury i inne dokumenty PDF |
| TIFF | `.tif`, `.tiff` | Dokumenty skanowane |
| XML | `.xml` | Ustrukturyzowane dokumenty elektroniczne |
| EDI / dane zamówienia | `.edi`, `.purchaseorder` | Elektroniczna wymiana danych i zamówienia |

Jeśli usługa przekazywania oznacza plik PDF, TIFF lub XML jako ogólny załącznik, DocBits może go rozpoznać na podstawie zawartości pliku lub znanego rozszerzenia. Przekazane wiadomości `.eml` również mogą zawierać obsługiwane dokumenty; DocBits wydobywa te wewnętrzne załączniki przed importem.

Obrazy, takie jak PNG, JPG, GIF i BMP, nie są importowane jako dokumenty. Obrazy podpisów i logo w przekazanych wiadomościach e-mail są pomijane. Pliki pakietu Office, takie jak Word, Excel i PowerPoint, nie są obsługiwane przez te metody importu e-mail.

W przypadku przekazanych wiadomości sprawdź **Dzienniki** w sekcji **Wiadomości przychodzące**, jeśli brakuje dokumentu. Gdy opcja **Powiadom nadawcę, gdy import się nie powiedzie** jest włączona, nadawca otrzymuje wyjaśnienie i link do tej strony. Dla podłączonej skrzynki skorzystaj z przewodnika konfiguracji [IMAP](imap.md) lub [OAuth (Office 365)](oauth-office365.md).
