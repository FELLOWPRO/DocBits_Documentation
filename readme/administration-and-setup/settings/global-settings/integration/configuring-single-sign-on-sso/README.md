---
description: Konfigurišite Single Sign-On (SSO) u DocBits-u sa SAML provajderom identiteta.
---

# Konfiguracija Single Sign-On (SSO)

Konfiguracija Single Sign-On (SSO) u DocBits-u zahteva nekoliko koraka pripreme i podešavanja. Evo uputstva korak po korak:

**Pristup SSO podešavanjima:**

* Prijavite se na svoj DocBits nalog kao administrator.
* Idite u podešavanja i potražite Single Sign-On ili SSO.

**Konfiguracija SSO parametara:**

![Trenutni ekran Integracija i SSO u DocBits-u u engleskoj Sandbox test organizaciji, sa ID-om entiteta provajdera usluga, SSO URL-om, SLO URL-om i preuzimanjima sertifikata i metapodataka.](../../../../../.gitbook/assets/dbdc-182-infor-v2-sso-settings-en.png)

* Unesite potrebne SSO parametre, kao što su ID entiteta, Single Log-Out (SLO) URL i Single Sign-On (SSO) URL.
* ID entiteta je jedinstveni identifikator vašeg servisa ili aplikacije.
* SLO URL se koristi za Single Log-Out, odnosno za odjavu korisnika sa svih servisa kada je to potrebno.
* SSO URL preusmerava korisnike na provajdera identiteta radi autentifikacije.

**Preuzimanje sertifikata i metapodataka:**

* Provajder identiteta (IdP) obično obezbeđuje sertifikat koji DocBits koristi za proveru SAML autentifikacionog odgovora.
* Preuzmite sertifikat dugmetom **Preuzmi sertifikat** i bezbedno ga sačuvajte.
* Preuzimanje metapodataka (**Preuzmi metapodatke**) sadrži sve informacije potrebne za SSO integraciju, uključujući ID entiteta, SSO URL, podatke o sertifikatu i druge informacije.
* Preuzmite metapodatke i sačuvajte ih lokalno ili ih prosledite provajderu identiteta.

**Konfiguracija provajdera identiteta (IdP):**

* Prijavite se na provajdera identiteta i konfigurišite aplikaciju ili servis za SAML integraciju.
* Iskoristite preuzete metapodatke ili ručno unete SSO parametre da dodate DocBits kao pouzdanu aplikaciju ili servis.
* Proverite da konfiguracija IdP-a odgovara SSO parametrima navedenim u DocBits-u.
* U sekciji **Podešavanja provajdera identiteta** unesite **ID tenanta**, otpremite IdP metapodatkovni fajl putem **Otpremi fajl** i izaberite **Konfiguriš**.

**Testiranje SSO integracije:**

* Nakon završene konfiguracije testirajte SSO integraciju kako biste potvrdili da se korisnici uspešno prijavljuju u DocBits pomoću SSO-a.
* Proverite i da Single Log-Out radi ispravno: odjavite se iz DocBits-a i potvrdite da ste odjavljeni i sa ostalih povezanih servisa.

Detaljna uputstva po provajderu: [Konfiguracija Infor SSO](sso-configuration/README.md) sa stranicom [V2](sso-configuration/v2.md) za Infor OS Portal V2.

Ispravno podešen SSO omogućava korisnicima da se besprekorno prijavljuju u DocBits svojim postojećim kredencijalima, čime se poboljšava korisničko iskustvo i povećava bezbednost.
