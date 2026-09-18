# DocBits plan razvoja

_Stanje planiranja na dan 18. septembra 2026. Svako izdanje navodi planirani
datum za sandbox (kada klijenti mogu da ga testiraju) i planirani datum za
produkciju. Teme opisuju šta je planirano za izdanje, a ne šta je već
isporučeno; obim i datumi mogu da se pomere. Hitne popravke između izdanja
dokumentovane su u [Beleškama o izdanju](release-notes/README.md)._

| Izdanje | Sandbox | Produkcija |
|---|---|---|
| R1.1 | 5. oktobar 2026. | 14. oktobar 2026. |
| R1.2 | 23. novembar 2026. | 2. decembar 2026. |
| R1.3 | 8. februar 2027. | 17. februar 2027. |
| R1.4 | 7. april 2027. | 15. april 2027. |
| R1.5 | 18. maj 2027. | 27. maj 2027. |
| R1.6 | 6. jul 2027. | 15. jul 2027. |
| R1.7 | 21. septembar 2027. | 30. septembar 2027. |
| R2.0 | biće naknadno objavljeno | biće naknadno objavljeno |

---

## R1.1 — Sandbox 5. oktobar 2026. · Produkcija 14. oktobar 2026.

**Pravila transformacije i izgledi**

- Mehanizam pravila za ekstrahovane vrednosti polja i kolona: postavite,
  zamenite ili izvedite vrednosti pomoću ugnežđenih grupa uslova, sa ekranom
  podešavanja za upravljanje pravilima. Pravila za izbor izgleda dobijaju iste
  ugnežđene uslove.
- Izbor izgleda radi nezavisno od toga odakle je dokument stigao.
- Jasna pravila prvenstva za oznake polja na poljima zaglavlja i kolonama
  tabele.
- Kolona tabele može ponovo da se dodeli nakon što je obrisana, a tabela cena
  artikala dobavljača prikazuje sve svoje kolone.

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

- Dugme "Novi radni tok", zapisi (logovi) za napredne radne tokove, pregledniji
  ekran watchdog zapisa, a koraci radnog toka koji menjaju polje ili polje za
  potvrdu primenjuju se pouzdano.
- Dodavanje stavke u stablo odlučivanja zadržava imena korisnika umesto
  prikazivanja ID-jeva.
- Svaka promena statusa dokumenta se beleži.
- Kreiranje novog šablona e-pošte ponovo radi.

**Uvoz**

- Uvoz e-pošte premešta poruku iz prijemnog sandučeta tek nakon što je
  otpremanje potvrđeno, ponovo isporučeno prosleđivanje tretira kao jednu
  isporuku, beleži ko je poslednji sačuvao i prihvata S/MIME potpisane
  poruke.
- FTP uvoz dobija pravu opciju brisanja nakon uvoza pored premeštanja i
  arhiviranja.
- Otpremanje iz aplikacije za skeniranje ponovo radi.
- BOD datoteke narudžbenica otpremljene u regionu SAD ostaju u regionu SAD.

**Obrada dokumenata i ekstrakcija**

- Kada servis za barkodove zastane, dokument prikazuje grešku umesto da
  beskonačno stoji u statusu "Processing".
- Novi, jeftiniji nivo AI modela ("Eco") za ekstrakciju.
- Kod strukturirane AI ekstrakcije obučeni brojevi artikala dobavljača ostaju
  obučeni, a broj artikla i broj artikla dobavljača više se ne zamenjuju.
- UBL šabloni e-dokumenata su prilagođeni; ispravke ekstrakcije za iznose,
  poreske stope, jedinične cene i brojeve narudžbenica na određenim izgledima
  dobavljača.
- Prepoznaju se dodatni formati datuma.

**Usklađivanje narudžbenica**

- Usklađivanje zahteva kolonu količine, koristi cenu po osnovnoj jedinici
  količine, a rezervno pravilo poslednje stavke može da se uključi po
  klijentu.
- Stavke otpremnice mogu pojedinačno da se izaberu.
- Ekran e-dokumenata više se ne zamrzava na fakturama sa više od 250 stavki.

**Touchless Intelligence**

- Više detalja u Touchless izveštaju, a Touchless polje za potvrdu odražava
  sačuvano podešavanje.

**Kontrolna tabla**

- Kontrolna tabla može da sadrži do 10.000 dokumenata po pretrazi.
- Datum dospeća popusta i datum dospeća fakture dostupni su kao polja izgleda
  i popunjavaju se pri uvozu.
- Korisnici sa kojima je kontrolna tabla podeljena zadržavaju se kada se
  kontrolna tabla sačuva, a "Updated by" prikazuje pravu osobu.
- Arhivirani dokumenti mogu da se vrate iz statusa "Archived".

**Izvoz i EDI**

- Dodatni korak izvoza u Infor M3 za dodatne informacije o fakturi.
- Lista pakovanja sa više brojeva kontejnera izvozi se kao jedan zapis po
  kontejneru.
- Ponovni uvoz prijema isporuke više ne pada zbog dupliranog ključa, a BOD-ovi
  prijema isporuke primenjuju se u pravom redosledu.
- Ažurirana su EDI mapiranja za fakturu, narudžbenicu i potvrdu porudžbine.

**Bezbednost**

- Provera organizacije za API ključeve sprovodi se u svakom okruženju.

---

## R1.2 — Sandbox 23. novembar 2026. · Produkcija 2. decembar 2026.

**Odobravanje i usklađivanje narudžbenica**

- Status "Pending input" pauzira dokument dok neko ne odgovori, bez
  narušavanja radnog toka ili istorije revizije, a odobravaoci mogu da
  postavljaju pitanja bez prekidanja toka odobravanja.
- Fakture za avansno plaćanje mogu da se usklade pre prijema robe dok opcija
  "Match on received quantity" ostaje aktivna.
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

- Skripta "Set sub-organisation" postaje pravilo transformacije.
- Standardne kolone mogu da se uklone iz tipa dokumenta.

**Izvoz**

- Istorija izvoza ponovo navodi izvezene dokumente.
- Fakture za prevoz izvoze se u Infor LN.

---

## R1.3 — Sandbox 8. februar 2027. · Produkcija 17. februar 2027.

**Auto Accounting Rule Manager**

- Pravila automatski dodeljuju konta i dimenzije, ograničena po
  pod-organizaciji i tipu dokumenta, sa ekranom revizije koji prikazuje koje
  je pravilo pokrenuto.
- Pravilo može da popuni vrednost iz kolone stavke tabele.
- Polja i dimenzije mogu pojedinačno da se obrišu, stavke mogu da se izbrišu
  (uključujući stavke bez iznosa), a pravila nastavljaju da rade na poljima
  koja su promenjena iz teksta u padajuću listu.

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

## R1.4 — Sandbox 7. april 2027. · Produkcija 15. april 2027.

**Uvoz**

- Mehanizam za ponovne pokušaje za FTP, e-poštu i uvoz dolazne e-pošte sa
  automatskom i ručnom ponovnom obradom.

**DocNet Agents**

- Prijem porudžbina: porudžbina kupca postaje prodajni nalog u Infor M3 ili
  Infor LN (prva verzija, tekstualni dokumenti).

**Odobravanje**

- Poboljšan tok odobravanja, delegiranje drugom korisniku tokom odobravanja i
  dugme "Export & Next".

**Usklađivanje narudžbenica**

- Na ekranu usklađivanja nude se samo upotrebljive stavke narudžbenice.
- Prekomerno usklađene fakture, kod kojih fakturisana količina premašuje
  primljenu količinu, prepoznaju se na ekranu usklađivanja, a jedinice mere se
  konvertuju tokom usklađivanja fakture.

**Ostalo**

- Krug povratnih informacija o Rule Manager-u.
- Obrazac za tiket podrške prihvata priloge i automatski povezuje
  organizaciju.
- Proširena Vertex integracija za poreze.

---

## R1.5 — Sandbox 18. maj 2027. · Produkcija 27. maj 2027.

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

---

## R1.6 — Sandbox 6. jul 2027. · Produkcija 15. jul 2027.

**Podešavanja**

- Podešavanja mogu da se pretražuju kroz sve prekidače i podstranice.
- Podešavanje servera e-pošte omogućava da zamenite istekli OAuth ili
  klijentski tajni ključ (client secret) bez ponovnog podešavanja poštanskog
  sandučeta.
- Mapa brojeva artikala dobavljača (tabela konverzije brojeva artikala) može
  da se popuni iz CSV uvoza.

**Auto Accounting**

- Dimenzije se čuvaju u novoj strukturi kako bi se veliki skupovi dimenzija
  brže učitavali.

---

## R1.7 — Sandbox 21. septembar 2027. · Produkcija 30. septembar 2027.

**Auto Accounting na ekranu odobravanja**

- Odobravaoci mogu da koriste Auto Accounting direktno na ekranu odobravanja.
- Odobravanje može da se uslovi računovodstvenim poljima kao što su šifra
  konta ili zemlja, uz ispravku obaveza prema dobavljačima (AP) kada se
  dokument vrati.
- Padajuća lista poreskih šifara u Auto Accounting-u bez podešavanja više
  poreskih stavki.

---

## R2.0 — Sandbox biće naknadno objavljeno · Produkcija biće naknadno objavljeno

**Auto Accounting**

- Polja zasnovana na listi prihvataju i slobodan tekst.
- Obavezna polja se validiraju.
- Predviđanja modela automatski popunjavaju računovodstvena polja (hibridni
  režim sa obučenim modelom predviđanja), uz revizijski trag onoga što je
  model popunio.

<!-- Generated from Jira "Release No." (customfield_10392) on 2026-09-18 by the
     docbits-roadmap skill. Themes only; ticket keys, customer names and
     internal work are deliberately left out. Rerun the skill to refresh. -->
