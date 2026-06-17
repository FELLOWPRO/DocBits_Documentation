# Korisnici

<figure><img src="../../../../../.gitbook/assets/users_settings.png" alt="Upravljanje korisnicima"><figcaption><p>Stranica za upravljanje korisnicima</p></figcaption></figure>

Stranica „Korisnici“ omogućava administratorima da upravljaju svim korisničkim nalozima u vašoj DocBits organizaciji. Ovde možete dodavati nove korisnike, dodeljivati uloge i kontrolisati pristup.

## Lista korisnika

Tabela korisnika prikazuje sledeće kolone:

| Kolona | Opis |
|--------|-------------|
| **Ime** | Puno ime korisnika. |
| **E-pošta** | Adresa e-pošte korisnika, koja se koristi kao njegova identifikacija pri prijavi. |
| **Poslednja prijava** | Datum i vreme poslednje prijave korisnika. |
| **Admin** | Polje za potvrdu koje pokazuje da li korisnik ima administratorska ovlašćenja. Admini mogu da pristupe svim podešavanjima i da upravljaju ostalim korisnicima. |
| **System Admin** | Polje za potvrdu koje označava jedini System Admin nalog organizacije — nalog koji DocBits koristi za automatske radnje koje se odvijaju u pozadini (kao što su automatizovani uvozi i izvozi). System Admin uvek ima i Admin ovlašćenja. Pogledajte [Administratorska ovlašćenja](admin-privileges.md#admin-vs-system-admin) za razliku između Admin i System Admin uloge. |
| **Aktivan** | Polje za potvrdu koje pokazuje da li je korisnički nalog trenutno aktivan. Neaktivni korisnici ne mogu da se prijave. |
| **Radnje** | Meni sa opcijama kao što su izmena podataka o korisniku, resetovanje lozinki ili deaktiviranje naloga. |

Koristite traku za **pretragu** na vrhu da biste brzo pronašli korisnike po imenu ili identifikacionom broju.

## Analitika prijava

Kliknite na **Analitika prijava** da biste videli podatke o aktivnostima prijavljivanja u vašoj organizaciji, uključujući učestalost i obrasce prijava.

## Dodavanje novog korisnika

1. Kliknite na dugme **Dodaj korisnika** u gornjem desnom uglu.
2. Popunite obavezne podatke:
   * **Korisničko ime**: Jedinstveno ime za korisnika.
   * **Ime** i **Prezime**: Puno ime korisnika.
   * **Adresa e-pošte**: Koristi se za prijavu i obaveštenja.
   * **Lozinka**: Mora biti usklađena sa bezbednosnim pravilima vaše organizacije.
   * **Uloga korisnika**: Dodelite odgovarajuću ulogu (Standard User, Admin ili System Admin).
3. Kliknite na **Sačuvaj** da biste kreirali korisnički nalog. Novi korisnik će dobiti obaveštenje e-poštom sa podacima za prijavu.

> **Napomena:** Uloga **System Admin** može se izabrati samo prilikom kreiranja korisnika — ne može se dodati ili ukloniti naknadno. Svaka organizacija može imati samo jednog System Admin korisnika, a njegovim izborom automatski se dodeljuju i Admin ovlašćenja. Pogledajte [Administratorska ovlašćenja](admin-privileges.md#admin-vs-system-admin) da biste saznali kada ga koristiti.
