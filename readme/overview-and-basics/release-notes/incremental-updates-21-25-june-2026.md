# DocBits beleške o izdanju — 21–25. jun 2026.

_Šta je donela ova produkcijska nadogradnja, jednostavnim jezikom. Uz svaki servis
prikazana je verzija koja je sada aktivna u produkciji. Servisi koji nisu navedeni
nisu imali izmene vidljive korisnicima u ovom periodu._

---

## Najvažnije

- **Pametnija pretraga kontrolne table.** Pouzdano pretražujte dokumente po
  iznosima i brojevima — pronađite fakture iznad određene vrednosti ili pretražujte
  po **broju zahtevnice** — uz opsege iznosa koji porede stvarne brojeve, a ne
  tekst. Podtipovi faktura mogu se pretraživati po svojim prevedenim nazivima.
- **Pouzdana obaveštenja e-poštom.** Obaveštenja o promeni statusa sada se šalju za
  svaki status (nema više tiho odbačenih e-poruka), a potvrde o dolaznom uvozu i
  obaveštenja o greškama sada su ispravno brendirana u DocBits stilu, uz kontrole
  po primaocu.
- **Jednostavnija prijava između regiona (EU/US).** Prebacivanje regiona sada je
  mali baner umesto prekida preko celog ekrana, jedinstvena prijava (SSO) vodi u
  ispravan region, a ostajanje prijavljenim u više kartica pregledača je
  pouzdanije.
- **Ispravke dozvola.** Korisnici dobijaju pristup koji im njihova grupa omogućava
  — otvaranje, uređivanje, odobravanje i ponovno pokretanje dokumenata sada rade
  ispravno čak i kada su grupe i dozvole podešene na ređe načine.
- **Stabilnija obrada dokumenata.** Dokumenti koji su se ranije zaglavljivali nakon
  otpremanja automatski se ponovo preuzimaju, a nagli priliv od jednog klijenta
  više ne usporava ostale.

---

## Web App — u produkciji: `10.32.4`

- **Skok brzom pretragom (Cmd/Ctrl + K)** direktno do podešavanja **Validacija
  e-faktura**.
- **Region i prijava:** prebacivanje regiona prikazano je kao trajni baner umesto
  blokirajućeg ekrana; jedinstvena prijava (SSO) sada preusmerava u ispravan region
  (EU/US); ostajanje prijavljenim u više kartica je pouzdanije.
- **Dozvole:** otklonjeni su slučajevi kada korisnici nisu mogli da **odobre**,
  **urede**, **otvore** ili **ponovo pokrenu** dokumente uprkos ispravnim dozvolama
  grupe.
- **Podešavanja dolazne e-pošte:** novi prekidači „Obavesti pošiljaoca" i „Odgovori
  pošiljaocu po prijemu".
- **Upotrebljivost:** upozorenje o dupliranom dokumentu sada mora biti zatvoreno
  pre nastavka; baner „pozadinski sistem nedostupan" pojavljuje se samo tokom
  stvarnih prekida; brojači zadataka se ažuriraju odmah po završetku zadataka;
  ispravka tamnog režima na ekranu za validaciju AI tabela.
- **Performanse:** otklonjeno je zamrzavanje na ekranu elektronskih dokumenata
  tokom validacije polja i PO podudaranja.
- **Pretraga podtipova faktura po njihovim prevedenim nazivima.**

## API Service — u produkciji: `12.41.9`

- **Preuređena pretraga kontrolne table:** broj zahtevnice i podnosilac zahtevnice
  sada su pretraživi; pretrage po iznosu i broju vraćaju ispravne rezultate (stvarno
  numeričko poređenje); ukupan neto iznos i izračunate kolone prikazuju se ispravno.
- **Pouzdana obaveštenja o statusu e-poštom** za svaki status dokumenta, uz greške
  pri slanju koje više nisu skrivene.
- **Dozvole:** korisnici bez grupe mogu da otvore i odobre sopstvene dokumente;
  vraćena je vidljivost dokumenata za korisnike bez grupe.
- **Pouzdanost obrade dokumenata:** dokumenti zaglavljeni u statusu „novo"
  automatski se ponovo stavljaju u red; obrada sa pravednom raspodelom, tako da
  veliki priliv iz jedne organizacije ne uskraćuje resurse ostalima; samoisceljivanje
  za retke probleme sa sekvencama baze podataka.
- **Skenirani PDF-ovi sa oštećenim tekstualnim slojem usmeravaju se na OCR** umesto
  da proizvode nepouzdan tekst.
- **Tačnost ekstrakcije i PO podudaranja:** naziv dobavljača popunjava se iz
  povezane porudžbine; uklonjene su duplirane kolone sa brojem artikla; bolje
  rukovanje specijalnim (neprelomivim) razmacima.
- **Izvoz u Infor ERP / SAP:** ispravljena je autentifikacija SFTP izvoza.
- **E-fakturisanje:** poboljšanja putanje ekstrakcije za ZUGFeRD / elektronske
  dokumente.

## Auth Service — u produkciji: `1.66.0`

- **Ispravljeno je nedostajuće dodeljivanje organizacije** za neke korisnike
  (prazan org id).

## Docflow Service — u produkciji: `2.3.4`

- **Period mirovanja okidača radnog toka** sada se može podesiti po okruženju.

## Email Service — u produkciji: `1.35.9`

- **Brendirane e-poruke:** potvrde o dolaznom uvozu i obaveštenja o greškama sada
  koriste pravi DocBits logo i boje.
- **Kontrole po organizaciji:** potvrdna e-poruka po prijemu, „obavesti pošiljaoca"
  pri grešci i opcije za odgovor pošiljaocu.
- **Pouzdaniji dolazni uvoz:** rezultati uvoza beleže se ispravno, delimični
  neuspesi prijavljuju se kao greške (a ne kao tihi uspesi), a problematični znakovi
  u telu e-poruke više ne prekidaju uvoz.
- **EU/US usmeravanje:** usmeravanje po organizaciji ka ispravnom regionalnom
  API-ju.

## Fulltext Service — u produkciji: `1.34.5`

- **Pretraga po iznosima i brojevima** sada radi pouzdano, uključujući separatore
  hiljada i opsege iznosa (mehanizam iza preuređene pretrage kontrolne table).
- **Stabilnija infrastruktura pretrage:** napušteni pozadinski redovi se čiste tako
  da više ne zauzimaju deljene resurse.

## PO Match Service — u produkciji: `1.54.7`

- **Otpornije podudaranje porudžbina:** tekstualni kodovi jedinice pakovanja više
  ne blokiraju podudaranje, a ručno podudaranje stavki bezbedno obrađuje prazne
  rezultate.

---

## Nema izmena vidljivih korisnicima u ovom periodu

Stabilno, bez značajnih izmena proizvoda između 21. i 25. juna: Auto Accounting
(`1.18.5`), Barcode (`1.15.6`), Docnet (`1.54.6`), Extraction (`1.48.6`), FTP
(`1.30.0`), OCR (`1.6.8`), Operator (`1.39.5`).

<!-- Generated by the docbits-changelog skill (prod-delta mode). Versions read live
     from prod (do-fra1-polydocs/prod); window 2026-06-21 → 2026-06-25. -->
