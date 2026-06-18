# Wiadomości e-mail przychodzące

### Przegląd

DocBits może pobierać dokumenty bezpośrednio z poczty e-mail — bez ręcznego przesyłania. Istnieją **dwa sposoby** wprowadzania dokumentów z e-maili, oba w **Ustawienia → Przetwarzanie dokumentów → Import**:

| Metoda | Jak działa | Najlepsza do |
|--------|------------|--------------|
| **Konto importu e-mail** | DocBits łączy się ze skrzynką, która należy do Ciebie (**IMAP**, **OAuth Office365** lub **OAuth Office365 – Tenant**) i importuje znalezione dokumenty. | Dedykowana skrzynka, która już odbiera Twoje dokumenty (np. `faktury@twojafirma.com`). |
| **Przekazywane e-maile (Wiadomości przychodzące)** | DocBits udostępnia Ci unikalny adres; każdy autoryzowany nadawca może **przekazać** dokumenty na ten adres. | Doraźne przekazywanie od wielu nadawców bez udostępniania danych logowania skrzynki. |

Możesz używać każdej metody osobno lub obu jednocześnie.

### Metoda 1 — Podłączenie skrzynki (Import e-mail)

Przejdź do **Ustawienia → Przetwarzanie dokumentów → Import** i otwórz sekcję **Import e-mail**. Kliknij **Nowy**, aby dodać połączenie ze skrzynką.

<figure><img src="../../../../.gitbook/assets/inbound_emails_email_import_entry.png" alt="Sekcja Import e-mail z przyciskiem Nowy"><figcaption><p>W sekcji Import e-mail kliknij <strong>Nowy</strong>, aby podłączyć skrzynkę.</p></figcaption></figure>

Otworzy się kreator konfiguracji. Pierwsze pole, **Protokół**, decyduje o sposobie połączenia DocBits — wybierz **IMAP**, **OAuth Office365** lub **OAuth Office365 – Tenant**.

<figure><img src="../../../../.gitbook/assets/inbound_emails_protocol_select.png" alt="Lista rozwijana Protokół z IMAP, OAuth Office365 i OAuth Office365 - Tenant"><figcaption><p>Lista <strong>Protokół</strong> oferuje trzy typy połączeń.</p></figcaption></figure>

#### IMAP

Dla standardowej skrzynki wybierz **IMAP** i wprowadź dane serwera oraz dane logowania konta:

* **Nazwa serwera** i **Port** (domyślnie `993`) Twojego serwera poczty.
* **Szyfrowanie** — `SSL`, `TLS` lub `None`.
* **Nazwa użytkownika**, **e-mail** i **hasło** skrzynki.

<figure><img src="../../../../.gitbook/assets/inbound_emails_imap.png" alt="Formularz połączenia IMAP z serwerem, portem, szyfrowaniem i danymi logowania"><figcaption><p>Formularz IMAP: połączenie z serwerem poczty oraz dane logowania skrzynki.</p></figcaption></figure>

#### OAuth Office365

Dla pojedynczej skrzynki użytkownika Microsoft 365 wybierz **OAuth Office365**. Zamiast hasła autoryzujesz DocBits przez Microsoft: wybierz cel **Routingu dokumentów**, następnie kliknij **Uwierzytelnij** i dokończ logowanie Microsoft.

<figure><img src="../../../../.gitbook/assets/inbound_emails_o365.png" alt="Formularz OAuth Office365 z Routingiem dokumentów i przyciskiem Uwierzytelnij"><figcaption><p>OAuth Office365 łączy się przez logowanie Microsoft — w DocBits nie jest przechowywane żadne hasło.</p></figcaption></figure>

#### OAuth Office365 – Tenant

Aby połączyć się na poziomie dzierżawy (organizacji) przez rejestrację aplikacji Azure, wybierz **OAuth Office365 – Tenant** i wprowadź dane Azure: **Identyfikator dzierżawy** (Tenant ID), **Identyfikator aplikacji klienckiej** (Client App ID) oraz **Wartość aplikacji klienckiej** (klucz tajny klienta). Użyj **Testuj połączenie**, aby zweryfikować, a następnie **Zapisz**.

<figure><img src="../../../../.gitbook/assets/inbound_emails_o365_tenant.png" alt="Konfiguracja dzierżawy Azure z Identyfikatorem dzierżawy, Identyfikatorem aplikacji klienckiej i Wartością aplikacji klienckiej"><figcaption><p>OAuth Office365 – Tenant używa rejestracji aplikacji Azure (Identyfikator dzierżawy, Identyfikator aplikacji klienckiej, klucz tajny klienta).</p></figcaption></figure>

{% hint style="info" %}
**Routing dokumentów** decyduje, dokąd trafiają importowane dokumenty — **DocBits** (standardowy panel) lub **AI Workforce**. Po połączeniu kolejne kroki kreatora pozwalają wybrać, z którego **folderu** importować, opcjonalną **skrzynkę współdzieloną** oraz czy przetworzone e-maile mają być **przenoszone** do innego folderu.
{% endhint %}

### Metoda 2 — Przekazywanie e-maili do DocBits (Wiadomości przychodzące)

Ta metoda wymaga najpierw włączenia modułu **Wiadomości przychodzące**. Przejdź do **Ustawienia → Przetwarzanie dokumentów → Moduł**, otwórz sekcję **Typ dokumentu**, znajdź **Wiadomości przychodzące** i włącz przełącznik.

<figure><img src="../../../../.gitbook/assets/inbound_emails_1.png" alt="Włączanie modułu Wiadomości przychodzące"><figcaption><p>Włącz <strong>Wiadomości przychodzące</strong> w Ustawienia → Przetwarzanie dokumentów → Moduł.</p></figcaption></figure>

Po włączeniu w **Ustawienia → Przetwarzanie dokumentów → Import** pojawia się sekcja **Wiadomości przychodzące**. Zawiera wszystko, co potrzebne do odbierania przekazywanych dokumentów:

<figure><img src="../../../../.gitbook/assets/inbound_emails_forward.png" alt="Sekcja Wiadomości przychodzące: adres importu, predefiniowani nadawcy i adres powiadomień o błędach"><figcaption><p>Sekcja Wiadomości przychodzące: Twój adres importu, lista predefiniowanych nadawców oraz adres powiadomień o błędach.</p></figcaption></figure>

* **Adres importu** — unikalny, wygenerowany przez system adres w formacie `org_id@environment.inbound.docbits.com`. Przekaż lub wyślij dokumenty na ten adres, a DocBits zaimportuje je automatycznie. Użyj ikony kopiowania, aby go skopiować.
* **Importuj dokumenty tylko z predefiniowanych adresów e-mail** — gdy włączone, akceptowane są tylko adresy nadawców wymienione tutaj; e-maile od pozostałych są ignorowane. Dla każdego nadawcy możesz wybrać **Podorganizację** (pozostaw puste, aby przypisać do organizacji głównej). Użyj **Dodaj**, aby dodać kolejnych nadawców, i **Usuń**, aby któregoś usunąć.
* **Odpowiedz na ten e-mail, jeśli import nie jest możliwy** — gdy włączone, wprowadź adres, który ma być powiadamiany przy każdej nieudanej próbie importu, aby problemy nie pozostały niezauważone.

Kliknij **Zapisz**, aby zastosować zmiany.

{% hint style="info" %}
**Które załączniki są importowane?** DocBits importuje obsługiwane załączniki dokumentów — pełną listę typów plików znajdziesz w [Import → Import e-mail](../import/README.md#email-import) — oraz rozpakowuje przekazane wiadomości `.eml`, aby zaimportować zawarte w nich dokumenty. Rozpoznawanie opiera się również na **rzeczywistej zawartości pliku**, dzięki czemu załączniki, którym przekazujący serwer poczty nadał ogólny typ (`application/octet-stream`), są nadal importowane poprawnie. Obrazy osadzone w treści (logo w stopce / wbudowana grafika) są ignorowane.
{% endhint %}

### Kiedy której metody użyć

* **Użyj konta importu e-mail**, gdy dokumenty już trafiają do dedykowanej skrzynki i chcesz, aby DocBits sam je pobierał — IMAP dla ogólnych serwerów poczty, OAuth Office365 dla Microsoft 365.
* **Użyj przekazywanych e-maili**, gdy osoby mają przekazywać dokumenty w razie potrzeby lub gdy nie chcesz udostępniać danych logowania skrzynki DocBits.
* **Połącz obie**, jeśli niektóre dokumenty trafiają do stałej skrzynki, a inne są przekazywane doraźnie.

{% hint style="info" %}
Ograniczanie nadawców (Metoda 2) i wybór właściwego celu **Routingu dokumentów** (Metoda 1) to dwa najczęstsze sposoby utrzymania czystego potoku przychodzącego — tylko oczekiwane dokumenty, kierowane tam, gdzie chcesz.
{% endhint %}
