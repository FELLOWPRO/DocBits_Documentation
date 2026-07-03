# DocBits beleške o izdanju — 30. jun – 3. jul 2026.

_Šta je donela ova produkcijska nadogradnja, jednostavnim jezikom. Uz svaki servis
prikazana je verzija koja je sada aktivna u produkciji. Servisi koji nisu navedeni
nisu imali izmene vidljive korisnicima u ovom periodu._

---

## Najvažnije

- **AI chat na dnevnicima aktivnosti.** Nov panel za AI razgovor na stranici
  Activity Logs omogućava vam da postavljate pitanja o aktivnostima direktno, bez
  pretraživanja sirovih unosa.
- **Praćenje odlaznog uvoza e-pošte.** Dnevnik uvoza (Import Log) sada beleži
  odlaznu poštu pored dolazne, sa oznakama za brzo filtriranje Errors / Inbound /
  Outbound — sandučići koji stalno ne uspevaju sada se automatski deaktiviraju
  nakon ponovljenih neuspeha, administratori mogu biti obavešteni e-poštom o
  neuspehu uvoza, a ponovni pokušaji sada traju i do 15 puta tokom otprilike 5
  sati pre nego što se odustane.
- **Jasnije greške pri uvozu e-pošte.** Neuspesi prijave sada prikazuju stvarni
  osnovni uzrok, sa posebnim porukama za nevažeći sertifikat ili pogrešnu Gmail
  lozinku za aplikacije (app-password).
- **Ispravljena petlja pri prijavi.** Neki korisnici su mogli da se zaglave u
  ponovljenoj petlji prijave tokom osvežavanja tokena — rešeno.
- **Stabilnija obrada dokumenata.** Ispravljen pad pri ekstrakciji podataka
  usled nezaokruženih vrednosti koordinata, čitanje barkoda sada ponovo pokušava
  kod grešaka koje se mogu otkloniti umesto da tiho odustane, a redak slučaj gde
  je dokument mogao biti izvezen dvaput istovremeno je ispravljen.
- **Poboljšanja ekrana za validaciju.** Sada možete dalje da uvećate prikaz
  dokumenata, polja se više ne prazne skriptama kada se njihova vrednost zapravo
  nije promenila, a kontrolna tabla pamti vašu poziciju na stranici kada se
  vratite nazad.

---

## Web App — u produkciji: `10.35.7`

- **Panel za AI razgovor** dodat na stranicu Activity Logs (#15512).
- **Dnevnik uvoza:** nove oznake za brzo filtriranje Errors / Inbound / Outbound;
  prekidač za primaoce obaveštenja o neuspehu i polje za podešavanja dolazne
  e-pošte.
- **Ekran za validaciju:** uvećanje dokumenta sada ide dalje od prethodne
  podrazumevane veličine; polja ispražnjena skriptama za validaciju sada
  ispravno zadržavaju svoju vrednost kada skripta vrati istu vrednost.
- **Kontrolna tabla:** pozicija na stranici se čuva prilikom povratka na tabelu;
  ručka za promenu veličine kolone više ne izlazi izvan zaglavlja tabele.
- **Ekran Auto Accounting:** ispravljena greška validacije.
- **DocBits zadaci:** ispravljen problem sa dozvolama.
- **Dnevnici Watchdog-a:** dodat filter vremenskog opsega i podesivi birač broja
  redova po stranici.
- **Ispravke:** greška grafikona („Element not found") na stranici Boards;
  neispravna veza za brisanje izvoza na Activity Logs; ispravke rasporeda na
  ekranu Layout Builder; nedostajući prevod na filteru vremenskog opsega na
  Activity Logs.
- **Automatsko ažuriranje:** dodatno ojačan mehanizam automatskog ažuriranja
  aplikacije (brže čišćenje pri pokretanju, pouzdanije prepoznavanje verzije,
  čišćenje keša pre oporavljajućeg ponovnog učitavanja).

## API Service — u produkciji: `12.48.1`

- **Brže učitavanje skripti dokumenata:** skripte za validaciju sada se
  keširaju na serverskoj strani (keš od 6 sati) umesto da se preuzimaju svaki
  put.
- **Preciznije poverenje u iznos:** obračun poverenja sada uzima u obzir
  dokumente koji koriste različite konvencije decimalnog razdvajača.
- **Pouzdanost:** validacija dokumenta uvek pokreće jedinu aktivnu verziju
  skripte, a koja verzija je pokrenuta sada se beleži; redak slučaj gde je
  dokument mogao biti izvezen dvaput istovremeno je ispravljen; pravila
  ekstrakcije specifična za dobavljača ponovo se ispravno primenjuju nakon
  prinudnog ponovnog OCR-a.
- **Uvoz e-pošte:** dodata je pozadinska podrška za beleženje odlazne pošte i
  e-poruke o obaveštenju o neuspehu (pogledajte Email Service ispod).

## Auth Service — u produkciji: `1.68.5`

- **Ispravljena petlja pri prijavi** u koju su neki korisnici mogli da upadnu
  dok se token njihove sesije osvežavao.
- **Brži ekrani za administratore organizacije:** podaci o korisnicima i
  pretplatama sada se učitavaju u grupama umesto pojedinačno.
- **Ispravljen redak konflikt baze podataka** prilikom povezivanja korisnika sa
  organizacijom.

## Email Service — u produkciji: `1.37.4`

- **Dnevnik uvoza sada prati i odlaznu poštu** pored dolazne, sa filterom za
  prikaz samo dolaznih, odlaznih ili neuspelih uvoza.
- **Sandučići koji stalno ne uspevaju sada se automatski deaktiviraju** nakon
  ponovljenih neuspeha, a administratori mogu biti obavešteni e-poštom kada
  uvoz ne uspe; ponovni pokušaji sada traju i do 15 puta tokom otprilike 5 sati
  pre nego što se odustane.
- **Jasnije poruke o neuspehu prijave:** prikazuje se stvarni osnovni uzrok,
  posebna poruka za nevažeći sertifikat i posebna poruka za pogrešnu Gmail
  lozinku za aplikacije (app-password).
- **Ispravljeno dolazno usmeravanje** koje je pogrešno prepisivalo adrese
  servera za naloge u EU regionu.
- Veća otpornost na kratkotrajne prekide veze sa Redis-om.

## Extraction Service — u produkciji: `1.49.0`

- **Ispravljen pad pri ekstrakciji** izazvan nezaokruženim vrednostima
  koordinata.
- **Preciznije poverenje u iznos** za dokumente sa mešovitim formatima
  decimalnog razdvajača; male razlike u zaokruživanju ukupnog poreza više ne
  blokiraju podudaranje.

## Docflow Service — u produkciji: `2.4.2`

- **Prerađena autentifikacija za napredne (Celery zasnovane) radne tokove**, uz
  zaštitne mehanizme tako da neuspela provera autentifikacije više ne može da
  obori izvršavanje radnog toka.
- **Jasniji odgovor** kada korak radnog toka pokuša da se izvrši nad radnim
  tokom koji više ne postoji.

## Barcode Service — u produkciji: `1.15.7`

- **Čitanje barkoda sada automatski ponovo pokušava** kod grešaka koje se mogu
  otkloniti umesto da tiho odustane.

## OCR Service — u produkciji: `1.7.3`

- **Ispravljen neuspeh OCR-a** izazvan problemom pri pronalaženju Redis
  hostname-a.
- Prekidi veze sa Redis-om tokom provere zdravlja više se ne beleže kao greške,
  čime se smanjuje broj lažnih upozorenja.

## PO Match Service — u produkciji: `1.55.8`

- **Ispravljen problem gde se napomene nisu prikazivale** na PO Match zapisima.

---

## Nema izmena vidljivih korisnicima u ovom periodu

Stabilno, bez značajnih izmena proizvoda između 30. juna i 3. jula: Auto
Accounting (`1.18.7`), Docnet (`1.54.6`), FTP (`1.30.2`), Fulltext (`1.35.7`),
Operator (`1.39.5`). Auto Accounting je dobio samo interno održavanje
konfiguracije primene. Ideas Service nije mogao biti dostupan za proveru
verzije tokom ovog perioda.

<!-- Generated by the docbits-changelog skill (version-boundary mode, resolved
     from the prod version table supplied by the user). Window 2026-06-30 →
     2026-07-03. -->
