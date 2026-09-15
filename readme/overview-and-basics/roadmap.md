# DocBits plan razvoja

_Stanje planiranja na dan 15. septembra 2026. Svako izdanje navodi planirani
datum za sandbox (kada klijenti mogu da ga testiraju) i planirani datum za
produkciju. Teme opisuju šta je planirano za izdanje, a ne šta je već
isporučeno; obim i datumi mogu da se pomere. Hitne popravke između izdanja
dokumentovane su u [Beleškama o izdanju](release-notes/README.md)._

| Izdanje | Sandbox | Produkcija |
|---|---|---|
| R1.1 | 16. septembar 2026. | 23. septembar 2026. |
| R1.2 | 21. oktobar 2026. | 28. oktobar 2026. |
| R1.3 | 25. novembar 2026. | 2. decembar 2026. |
| R1.4 | 27. januar 2027. | 3. februar 2027. |
| R1.5 | 10. mart 2027. | 17. mart 2027. |

---

## R1.1 — Sandbox 16. septembar 2026. · Produkcija 23. septembar 2026.

**Pravila transformacije i izgledi**

- Mehanizam pravila za ekstrahovane vrednosti polja i kolona: postavite,
  zamenite ili izvedite vrednosti pomoću ugnežđenih grupa uslova, sa ekranom
  podešavanja za upravljanje pravilima. Pravila za izbor izgleda dobijaju iste
  ugnežđene uslove.
- Izbor izgleda radi nezavisno od toga odakle je dokument stigao.
- Jasna pravila prvenstva za oznake polja na poljima zaglavlja i kolonama
  tabele.

**Ekrani odobravanja i validacije**

- Tri tabele stavki na ekranu odobravanja (stavke fakture, stavke za
  poređenje, usklađivanje narudžbenica) dele jedan stil, a prikaz poređenja
  prikazuje broj artikla koji pripada stavci.
- Poslednje otvoreni bočni panel (tok aktivnosti ili istorija odobravanja)
  pamti se po korisniku.
- Spajanje dokumenata sa ekrana odobravanja pomoću alata za otpremanje
  dokumenata.
- Prilagođena pravila validacije obrađuju troškove isporuke generički, a
  pravila koja su prijavljivala lažno negativan rezultat su ispravljena.
- Traka učitavanja zamenjuje običnu ikonu učitavanja; prijatnije URL adrese
  stranica.

**Otkrivanje duplikata**

- Prilagođena polja pojavljuju se u rezultatu otkrivanja duplikata, a
  podešavanja duplikata mogu da se pretražuju.

**Radni tokovi i zadaci**

- Dugme „Novi radni tok", zapisi (logovi) za napredne radne tokove, a koraci
  radnog toka koji menjaju polje ili polje za potvrdu primenjuju se pouzdano.
- E-poruke za odobravanje stižu do dodeljenih odobravalaca u radnim tokovima
  ulaznih faktura.
- Svaka promena statusa dokumenta se beleži.

**Uvoz**

- Uvoz e-pošte premešta poruku iz prijemnog sandučeta tek nakon što je
  otpremanje potvrđeno, ponovo isporučeno prosleđivanje tretira kao jednu
  isporuku, beleži ko je poslednji sačuvao i prihvata S/MIME potpisane
  poruke.
- FTP uvoz dobija pravu opciju brisanja nakon uvoza pored premeštanja i
  arhiviranja.
- Otpremanje iz aplikacije za skeniranje ponovo radi.

**Obrada dokumenata i ekstrakcija**

- Kada servis za barkodove zastane, dokument prikazuje grešku umesto da
  beskonačno stoji u statusu „Processing".
- „Restrict to pages" ograničava samo OCR i brojanje stranica; više ne odseca
  stranice iz dokumenta.
- Čuvanje dokumenta ne dira nepovezane podatke.
- Novi, jeftiniji nivo AI modela („Eco") za ekstrakciju, a primena oznaka
  tabele na AI tabeli ponovo radi.
- Spajanje ZUGFeRD PDF-a sa drugim PDF-om zadržava podatke e-fakture; UBL
  šabloni e-dokumenata su prilagođeni; ispravke ekstrakcije za iznose, poreske
  stope i brojeve narudžbenica na određenim izgledima dobavljača.
- Prepoznaju se dodatni formati datuma.

**Usklađivanje narudžbenica**

- Usklađivanje zahteva kolonu količine, koristi cenu po osnovnoj jedinici
  količine, a rezervno pravilo poslednje stavke može da se uključi po
  klijentu.
- Ekran e-dokumenata više se ne zamrzava na fakturama sa više od 250 stavki.
- Dijagnostika meri količinu čak i kada stavka narudžbenice nema cenu.

**Touchless Intelligence**

- Više detalja u Touchless izveštaju, a blokada narudžbenice prijavljuje se
  kao takva umesto kao neuspela validacija polja.

**Kontrolna tabla**

- Kontrolna tabla može da sadrži do 10.000 dokumenata po pretrazi.
- Datum dospeća popusta i datum dospeća fakture dostupni su kao polja izgleda
  i popunjavaju se pri uvozu.
- Korisnici sa kojima je kontrolna tabla podeljena zadržavaju se kada se
  kontrolna tabla sačuva; „Assigned to" i „Updated by" prikazuju pravu osobu.
- Dozvole za dokumente primenjuju se i na indeks celog teksta.

**Izvoz i EDI**

- BOD izvoz zadržava vrednosti kolona tabele duže od 30 znakova.
- Dodatni korak izvoza u Infor M3 za dodatne informacije o fakturi i cene po
  jedinici u izvozima tipa linije 5.
- Ponovni uvoz prijema isporuke više ne pada zbog dupliranog ključa.
- Ažurirana su EDI X12 mapiranja za fakturu (810), narudžbenicu (850),
  potvrdu porudžbine (855), obaveštenje o isporuci (856, uključujući WMS
  izvoz) i izmenu porudžbine (860).

**Bezbednost**

- Mapiranja kontnog plana dobavljača čuvaju se sa vezanim SQL parametrima, a
  provera organizacije za API ključeve sprovodi se u svakom okruženju.

---

## R1.2 — Sandbox 21. oktobar 2026. · Produkcija 28. oktobar 2026.

**Odobravanje i usklađivanje narudžbenica**

- Status „Pending input" pauzira dokument dok neko ne odgovori, bez
  narušavanja radnog toka ili istorije revizije, a odobravaoci mogu da
  postavljaju pitanja bez prekidanja toka odobravanja.
- Fakture za avansno plaćanje mogu da se usklade pre prijema robe dok opcija
  „Match on received quantity" ostaje aktivna.
- Oznaka dostupnosti prijema poredi fakturisane i primljene količine.
- Potvrde porudžbina: elementi troškova prikazani dok se čeka odobrenje,
  pozicije doplata označene bojama u usklađivanju narudžbenica i kolona broja
  artikla u stavkama fakture.
- Kolone koje nisu mapirane više ne ulaze u obračun iznosa tabele.
- Obrađuju se RMA stavke dobavljača.

**Uvoz i klasifikacija**

- Adresa pošiljaoca dostupna je iz uvoza e-pošte.
- Tip dobavljača izvodi se iz stavki.

**Podešavanja i automatizacija**

- Skripta „Set sub-organisation" postaje pravilo transformacije.
- Standardne kolone mogu da se uklone iz tipa dokumenta.
- Tok zahteva za izmenu narudžbenice i vlasnik dokumenta u mapiranju Infor
  izvoza.

**Izvoz**

- Istorija izvoza ponovo navodi izvezene dokumente.
- Fakture za prevoz izvoze se u Infor LN.

---

## R1.3 — Sandbox 25. novembar 2026. · Produkcija 2. decembar 2026.

**Auto Accounting Rule Manager**

- Pravila automatski dodeljuju konta i dimenzije, ograničena po
  pod-organizaciji i tipu dokumenta, sa ekranom revizije koji prikazuje koje
  je pravilo pokrenuto.
- Pravilo može da popuni vrednost iz kolone stavke tabele.
- Polja i dimenzije mogu pojedinačno da se obrišu, stavke bez iznosa mogu da
  se izbrišu, a pravila nastavljaju da rade na poljima koja su promenjena iz
  teksta u padajuću listu.

**Usklađivanje narudžbenica**

- Ikona usklađivanja navigira, pomera prikaz i ističe stavke kroz kartice,
  uključujući usklađivanja jedan-prema-više.
- Konverzija jedinica sa alijasima (na primer KG i TO), podesiva varijansa
  zaokruživanja sa kontom za zaokruživanje i obračuni sa četiri decimale
  prikazane kao tri.

**Izvoz**

- Podesivi nazivi izvoznih datoteka.
- Nepotpun dokument u Infor LN briše se nakon neuspelog izvoza.
- Konektor baze podataka obuhvata sve relevantne tabele.

---

## R1.4 — Sandbox 27. januar 2027. · Produkcija 3. februar 2027.

**Uvoz**

- Mehanizam za ponovne pokušaje za FTP, e-poštu i uvoz dolazne e-pošte sa
  automatskom i ručnom ponovnom obradom.

**DocNet Agents**

- Prijem porudžbina: porudžbina kupca postaje prodajni nalog u Infor M3 ili
  Infor LN (prva verzija, tekstualni dokumenti).

**Odobravanje**

- Poboljšan tok odobravanja, delegiranje drugom korisniku tokom odobravanja i
  dugme „Export & Next".

**Usklađivanje narudžbenica**

- Na ekranu usklađivanja nude se samo upotrebljive stavke narudžbenice.
- Više skladišnih unosa može da se uskladi sa jednom stavkom fakture, a
  jedinice mere se konvertuju tokom usklađivanja fakture.

**Ostalo**

- Krug povratnih informacija o Rule Manager-u.
- Obrazac za tiket podrške prihvata priloge i automatski povezuje
  organizaciju.
- Proširena Vertex integracija za poreze.

---

## R1.5 — Sandbox 10. mart 2027. · Produkcija 17. mart 2027.

**Auto Accounting**

- Rule Manager akcija pretraživanja (lookup): uparite matične podatke i
  dodelite više polja odjednom.
- Predviđanja podržavaju više poreskih šifara i dimenzija, vaučere i
  reference knjiženja.
- Ekrani Auto Accounting na više jezika.

**Odobravanje i usklađivanje narudžbenica**

- Ponovno dodeljivanje dokumenta drugom korisniku.
- Redosled kolona na ekranu usklađivanja narudžbenica čuva se po korisniku.
- Šifre naknada (putarina, transport, energija) se prepoznaju, a njihov
  trošak raspoređuje.

**Zaštita izvoza**

- Izvoz se blokira uz upozorenje kada usklađena količina premašuje primljenu
  količinu ili previše odstupa od nje, ili kada je datum knjiženja pre datuma
  skladišnog unosa.

**Upotrebljivost**

- Redosled izvršavanja skripti dokumenata vidljiv je u frontendu.
- Enter i Tab pomeraju kroz polja pomoću tastature.

<!-- Generated from Jira "Release No." (customfield_10392) on 2026-09-15 by the
     docbits-roadmap skill. Themes only; ticket keys, customer names and
     internal work are deliberately left out. Rerun the skill to refresh. -->
