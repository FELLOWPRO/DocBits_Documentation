# Analitika prijava

**Analitika prijava** administratorima pruža uvid u to *kada* i *koliko često* se korisnici prijavljuju u DocBits, na nivou cele organizacije i samo za čitanje. Ona odgovara na pitanja poput „da li broj prijava raste?“, „koliko je različitih korisnika bilo aktivno ovog meseca?“ i „kada se dešavaju vršna opterećenja?“ — a da pritom ne otkriva pristupne podatke niti lične podatke pojedinačnih korisnika.

> **Pristup:** Otvorite **Podešavanja → Organizacija i pristup → Korisnici** i kliknite na dugme **Analitika prijava** u gornjem desnom uglu (`/settings/login-analytics`).

<figure><img src="../../../../../.gitbook/assets/login_analytics_overview.png" alt="Stranica Analitika prijava sa grafikonom aktivnosti i karticama sa rezimeom"><figcaption><p>Aktivnost prijavljivanja u organizaciji tokom izabranog perioda</p></figcaption></figure>

## Vremenski opseg

Period koji želite da analizirate izaberite pomoću selektora u gornjem desnom uglu: **7D**, **30D**, **90D**, **180D**, **Year** ili **Custom** za slobodno definisan opseg datuma. Sve na stranici — grafikon i kartice sa rezimeom — ponovo se izračunava za period koji izaberete.

Baner **Data Information** ponovo prikazuje tačan opseg koji je u prikazu (npr. *Showing data from 19.05.2026 to 18.06.2026*), tako da je uvek jasno koje datume brojevi obuhvataju.

## Grafikon aktivnosti prijavljivanja

Grafikon prikazuje dve serije podataka tokom izabranog perioda:

| Serija | Značenje |
|--------|----------|
| **Total Logins** | Broj prijava po danu, uključujući ponovljene prijave iste osobe. |
| **Unique Users** | Koliko se *različitih* korisnika prijavilo tog dana. |

Pređite mišem preko bilo koje tačke da biste videli tačnu vrednost za taj dan. Vršne vrednosti pokazuju vaše najaktivnije dane; ravna linija **Unique Users** ispod nazubljene linije **Total Logins** znači da se nekoliko osoba prijavilo mnogo puta.

## Kartice sa rezimeom

Ispod grafikona, tri kartice sumiraju ceo izabrani period:

| Kartica | Značenje |
|---------|----------|
| **Total Logins** | Sve prijave tokom perioda. |
| **Unique Users** | Različiti korisnici koji su se prijavili bar jednom. |
| **Avg/Day** | Prosečan broj prijava po danu tokom perioda. |

## Privatnost

Analitika prijava prikazuje isključivo **zbirne** brojeve — broj prijava i trendove za organizaciju u celini. Ona ne navodi pojedinačne korisnike, adrese e-pošte niti IP adrese. Da biste videli ili izmenili nalog određene osobe, koristite stranicu [Korisnici](README.md).
