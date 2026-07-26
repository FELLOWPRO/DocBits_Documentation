# Dvofaktorska autentifikacija (2FA)

## Pregled

Dvofaktorska autentifikacija (2FA) dodaje drugi korak prilikom prijavljivanja. Nakon lozinke, DocBits traži drugi faktor koji samo vi posedujete — kôd iz aplikacije za autentifikaciju, kôd poslat na vašu e-poštu ili pristupni ključ (Touch ID, Windows Hello, YubiKey, 1Password). Čak i ako neko sazna vašu lozinku, ne može da se prijavi bez tog drugog faktora.

2FA je **opciona za svakog korisnika** i može biti **obavezna po zahtevu administratora vaše organizacije**. Prijave putem jedinstvene prijave (SSO) (Google, Microsoft, SAML) su izuzete — vaš provajder identiteta već primenjuje sopstvenu MFA zaštitu.

Možete registrovati više od jedne metode. Metode koje DocBits podržava su:

* **Aplikacija za autentifikaciju (TOTP)** — Google Authenticator, Microsoft Authenticator, 1Password, Authy itd.
* **Kôd putem e-pošte** — šestocifreni kôd poslat na e-adresu vašeg naloga.
* **Pristupni ključ (WebAuthn/FIDO2)** — Touch ID, Windows Hello, hardverski ključ (YubiKey) ili menadžer lozinki.

Kada uključite svoj prvi faktor, DocBits vam takođe daje **deset rezervnih kodova** koje možete koristiti ako ikada izgubite pristup svojoj metodi.

## Gde se nalazi

Otvorite **profil / podešavanja naloga** (meni naloga u gornjem desnom uglu → **Izmeni profil**) i izaberite **Dvofaktorska autentifikacija**. Dijalog za 2FA prikazuje vaš trenutni status i metode koje možete dodati.

<figure><img src="../.gitbook/assets/mfa-2fa-dialog.png" alt="The Two-factor authentication dialog"><figcaption><p>Dijalog za dvofaktorsku autentifikaciju. Odavde možete omogućiti aplikaciju za autentifikaciju, verifikaciju putem e-pošte, dodati pristupni ključ ili otvoriti <strong>Upravljanje</strong>.</p></figcaption></figure>

## Podešavanje aplikacije za autentifikaciju (TOTP)

1. U dijalogu za 2FA kliknite na **Omogući 2FA**.
2. Skenirajte QR kôd svojom aplikacijom za autentifikaciju (Google Authenticator, 1Password, Authy, …). Ako ne možete da skenirate, upotrebite **ručni ključ** prikazan ispod QR koda.
3. Unesite šestocifreni kôd koji vaša aplikacija prikazuje i potvrdite.
4. DocBits omogućava 2FA i prikazuje vaše **rezervne kodove** (vidi ispod).

<figure><img src="../.gitbook/assets/mfa-totp-setup.png" alt="The authenticator-app setup screen with QR code"><figcaption><p>Skenirajte QR kôd svojom aplikacijom za autentifikaciju ili unesite ručni ključ. Zatim potvrdite šestocifrenim kodom koji aplikacija prikazuje.</p></figcaption></figure>

## Podešavanje verifikacije putem e-pošte

1. U dijalogu za 2FA kliknite na **Omogući verifikaciju putem e-pošte**.
2. DocBits šalje šestocifreni kôd na adresu vašeg naloga.
3. Unesite kôd da biste potvrdili. Verifikacija putem e-pošte je sada uključena.

## Dodavanje pristupnog ključa

1. U dijalogu za 2FA kliknite na **Dodaj pristupni ključ**.
2. Vaš pregledač ili uređaj tražiće da potvrdite pomoću Touch ID-a, Windows Hello-a, hardverskog ključa ili vašeg menadžera lozinki.
3. Pristupni ključ je sačuvan. Možete dodati više pristupnih ključeva i kasnije ih preimenovati ili ukloniti.

## Rezervni kodovi

Kada omogućite svoj **prvi** faktor, DocBits prikazuje **deset rezervnih kodova** — **jednom**. Svaki kôd radi samo jednom i omogućava vam da se prijavite ako izgubite svoju aplikaciju za autentifikaciju ili telefon.

* Sačuvajte ih na bezbednom mestu (menadžer lozinki je idealan).
* U svakom trenutku možete generisati novi skup pomoću opcije **Ponovo generiši rezervne kodove** (time se stari skup poništava).

<figure><img src="../.gitbook/assets/mfa-backup-codes.png" alt="The backup codes screen"><figcaption><p>Vaših deset rezervnih kodova, prikazanih jednom. Svaki radi samo jednom — čuvajte ih na bezbednom mestu.</p></figcaption></figure>

{% hint style="warning" %}
Rezervni kodovi se prikazuju samo u trenutku kada se generišu. DocBits ne može ponovo da ih prikaže — sačuvajte ih odmah.
{% endhint %}

## Prijavljivanje uz 2FA

1. Unesite svoju e-adresu i lozinku kao i obično.

    <figure><img src="../.gitbook/assets/mfa-login.png" alt="The DocBits login screen"><figcaption><p>Ekran za prijavu. Takođe se možete prijaviti bez lozinke pomoću opcije <strong>Prijavi se pristupnim ključem</strong>.</p></figcaption></figure>
2. DocBits traži vaš drugi faktor. Izaberite svoju metodu:
   * **Aplikacija za autentifikaciju** — ukucajte trenutni šestocifreni kôd iz svoje aplikacije.
   * **E-pošta** — kliknite na **Pošalji mi kôd e-poštom** da biste primili kôd e-poštom, a zatim ga ukucajte.
   * **Pristupni ključ** — kliknite na **Upotrebi pristupni ključ** i potvrdite pomoću Touch ID-a / Windows Hello-a / svog ključa.
   * **Rezervni kôd** — ako ne možete da upotrebite svoju uobičajenu metodu.

    <figure><img src="../.gitbook/assets/mfa-challenge.png" alt="The second-factor challenge screen"><figcaption><p>Nakon lozinke, DocBits traži vaš drugi faktor. Promenite metodu pomoću <strong>Upotrebi pristupni ključ</strong> ili <strong>Pošalji mi kôd e-poštom</strong> i opciono označite uređaj kao pouzdan na 30 dana.</p></figcaption></figure>
3. Nakon uspeha bićete prijavljeni.

### Kako izgleda kôd u e-pošti

Ako izaberete **E-pošta**, DocBits šalje poruku sa šestocifrenim kodom koji ističe za 10 minuta:

<figure><img src="../.gitbook/assets/mfa-email-otp.png" alt="The DocBits verification-code email"><figcaption><p>E-pošta sa verifikacionim kodom. Kôd ističe nakon 10 minuta i može se upotrebiti jednom.</p></figcaption></figure>

## Označite ovaj uređaj kao pouzdan

Na ekranu drugog faktora možete označiti **Zapamti ovaj uređaj**. DocBits tada preskače korak 2FA na tom uređaju narednih **30 dana**. Pouzdanost se automatski poništava kada promenite lozinku, a možete je i sami opozvati u svakom trenutku (vidi ispod).

## Upravljanje pristupnim ključevima i pouzdanim uređajima

Otvorite dijalog za 2FA i kliknite na **Upravljanje** da biste pregledali šta je registrovano.

* **Pristupni ključevi** — preimenujte pristupni ključ (kliknite na njegov naziv) ili ga izbrišite. Brisanjem poslednjeg preostalog faktora isključuje se 2FA.
* **Pouzdani uređaji** — opozovite pojedinačni uređaj ili **Opozovi sve uređaje** da biste svuda ponovo zahtevali 2FA.

<figure><img src="../.gitbook/assets/mfa-passkeys-list.png" alt="Managing enrolled passkeys and trusted devices"><figcaption><p>Prikaz za upravljanje navodi vaše registrovane pristupne ključeve i pouzdane uređaje, gde ih možete preimenovati ili ukloniti.</p></figcaption></figure>

## Isključivanje 2FA

U dijalogu za 2FA kliknite na **Onemogući 2FA** i potvrdite trenutnim kodom iz aplikacije za autentifikaciju ili rezervnim kodom. Isključivanjem 2FA takođe se brišu vaši rezervni kodovi i opozivaju pouzdani uređaji.

{% hint style="info" %}
Ako vaša organizacija **zahteva** MFA, ne možete se prijaviti lozinkom dok ne podesite barem jedan faktor. Pitajte administratora ako niste sigurni da li je MFA obavezna za vašu organizaciju.
{% endhint %}

## Prijavljivanje bez lozinke (opciono)

Kada imate pristupni ključ, možete se prijaviti **bez unosa lozinke** pomoću opcije **Prijavi se pristupnim ključem** na ekranu za prijavu. Vaša lozinka i dalje funkcioniše kao rezervna opcija. Prijava bez lozinke zahteva da vas pristupni ključ verifikuje (Touch ID / Windows Hello / PIN), pa je istovremeno brža i otporna na phishing.
