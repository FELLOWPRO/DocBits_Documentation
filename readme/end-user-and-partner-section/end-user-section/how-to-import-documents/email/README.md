---
hidden: true
noIndex: true
---

# E-mail

DocBits kan op twee manieren documenten uit e-mail importeren. Beide worden geconfigureerd onder **Instellingen → Import** (Documentverwerking).

## Methode 1 — E-mailimport (een mailbox koppelen)

Koppel een e-mailaccount en DocBits importeert documenten automatisch zodra er nieuwe e-mails binnenkomen. Open op de Import-pagina de sectie **E-mailimport** en klik op **+ Nieuw**.

<figure><img src="../../../../.gitbook/assets/email_import_section.png" alt="Sectie E-mailimport"><figcaption>E-mailimport — koppel een mailbox voor automatische documentimport</figcaption></figure>

Kies vervolgens het protocol van uw mailbox:

* **IMAP** — zie [IMAP](imap.md)
* **OAuth (Office 365)** — zie [OAuth Office365](oauth-office365.md)

## Methode 2 — Inkomende e-mails (doorsturen naar DocBits)

Stuur — of verzend rechtstreeks — e-mails naar het unieke inkomende adres van uw organisatie en DocBits importeert de bijlagen automatisch. Een mailboxkoppeling is niet nodig. Open de sectie **Inkomende e-mails** op de Import-pagina.

<figure><img src="../../../../.gitbook/assets/inbound_emails_section.png" alt="Sectie Inkomende e-mails"><figcaption>Inkomende e-mails — stuur documenten door naar uw DocBits-adres</figcaption></figure>

* **Info / E-mail** — het unieke inkomende adres van uw organisatie (formaat `<org-id>@inbound.docbits.com`). Stuur uw documenten naar dit adres door; gebruik het kopieerpictogram om het te kopiëren.
* **Documenten alleen importeren vanaf vooraf gedefinieerde e-mail(s)** — indien ingeschakeld worden alleen e-mails geïmporteerd van afzenders die u aan de witte lijst toevoegt; e-mails van andere afzenders worden genegeerd.
* **Beantwoord deze e-mail als import niet mogelijk is** — stuurt de afzender een automatisch antwoord wanneer de import mislukt.
* **Afzender informeren wanneer import mislukt** — informeert de afzender als zijn e-mail niet kon worden geïmporteerd.
* **Logboeken** — opent het verwerkingslogboek van inkomende e-mails. Klik op **Opslaan** om uw wijzigingen toe te passen.
