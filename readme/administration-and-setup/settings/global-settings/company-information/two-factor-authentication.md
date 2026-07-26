# Dvofaktorska autentifikacija (Admin)

## Pregled

Kao administrator organizacije možete **zahtevati da svaki član koristi dvofaktorsku autentifikaciju (2FA)** kada se prijavljuje lozinkom. Kada je zahtev uključen, član koji još nije podesio drugi faktor biva vođen kroz registraciju pre nego što može da završi prijavljivanje.

Prijave putem jedinstvene prijave (SSO) — Google, Microsoft, SAML — su **izuzete**: njihov provajder identiteta već primenjuje sopstvenu MFA zaštitu, pa zahtev utiče samo na prijave lozinkom.

Ovo podešavanje nalazi se u **Podešavanja → Globalna podešavanja → Informacije o kompaniji → Dvofaktorska autentifikacija** i dostupno je samo administratorima organizacije.

## Zahtevajte MFA za svoju organizaciju

1. Idite na **Podešavanja → Globalna podešavanja → Informacije o kompaniji**.
2. Otvorite odeljak **Dvofaktorska autentifikacija**.
3. Uključite **Zahtevaj dvofaktorsku autentifikaciju za sve članove** i kliknite na **Sačuvaj**.

<figure><img src="../../../../.gitbook/assets/mfa-admin-requirement.png" alt="The organisation MFA requirement toggle and adoption report"><figcaption><p>Uključite zahtev za sve članove i pratite prihvaćenost ispod.</p></figcaption></figure>

Nakon što sačuvate, promena stupa na snagu u roku od jednog minuta. Od tada:

* Član **sa** drugim faktorom biva zatražen za njega nakon lozinke, kao i obično.
* Član **bez** drugog faktora mora da registruje jedan pre nego što dobije sesiju.
* Na SSO / društvene prijave to ne utiče.

{% hint style="warning" %}
Uključivanjem ove opcije blokiraju se prijave lozinkom za članove koji nemaju drugi faktor dok ne završe registraciju. Obavestite svoj tim o promeni i razmislite o njenom uključivanju van perioda najveće aktivnosti.
{% endhint %}

## Izveštaj o prihvaćenosti MFA

Ispod prekidača, panel **Prihvaćenost MFA** prikazuje koliko se široko 2FA koristi u vašoj organizaciji pre nego što je primenite:

* ukupni **procenat prihvaćenosti** i traku napretka,
* koliko vaših članova ima omogućenu 2FA (npr. *0 od 74 člana*),
* raščlanjenje po faktorima — **Aplikacija za autentifikaciju**, **E-pošta** i **Pristupni ključ**.

<figure><img src="../../../../.gitbook/assets/mfa-adoption-report.png" alt="The MFA adoption report"><figcaption><p>Izveštaj o prihvaćenosti MFA: ukupni procenat, registrovani članovi i raščlanjenje po faktorima.</p></figcaption></figure>

Koristite ga da procenite spremnost: prvo podignite prihvaćenost, a zatim uključite zahtev sa manje članova blokiranih u koraku registracije.

## Šta članovi vide

Član od kojeg se zahteva registracija biva preusmeren na podešavanje 2FA pri sledećoj prijavi i bira metodu (aplikacija za autentifikaciju, kôd putem e-pošte ili pristupni ključ). Koraci za krajnjeg korisnika opisani su u [Dvofaktorska autentifikacija (2FA)](../../../../overview-and-basics/two-factor-authentication.md).

## Povezane bezbednosne kontrole

Zahtev za MFA na nivou cele organizacije dopunjuje ugrađene zaštite koje uvek važe kada korisnik ima uključenu 2FA: jednokratni kodovi za prijavu, zaštita od ponovnog korišćenja TOTP-a (replay), ograničenja broja pokušaja po izazovu i po nalogu (nalog se privremeno zaključava nakon previše neuspelih pokušaja) i automatsko opozivanje pouzdanih uređaja kada član promeni lozinku.
