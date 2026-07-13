# DocBits beleške o izdanju — 4–14. jul 2026.

_Pregled onoga što se za vas menja u ovom DocBits izdanju. Svaki servis ispod
prikazuje verziju koja se sada uvodi u produkciju, praćenu novinama ili
ispravkama objašnjenim jednostavnim jezikom — bez brojeva tiketa i tehničkog
žargona. Servisi koji nisu navedeni nisu imali izmene vidljive korisnicima u
ovom periodu._

---

## Najvažnije

- **Prijava sa više organizacija.** Korisnici koji pripadaju većem broju
  organizacija sada pri prijavi dobijaju pravi izbor organizacije, prekidač
  za promenu organizacije u zaglavlju i podešavanje podrazumevane
  organizacije. Sesije su bezbedno vezane za jednu organizaciju u datom
  trenutku, a aplikacija automatski prati region aktivne organizacije.
  Prijava na pogrešan region sada automatski ponovo pokušava ispravan umesto
  da ne uspe.
- **Kanali izdanja (frozen / latest).** Organizacije sada mogu biti zakačene
  na stabilno („frozen") izdanje dok druge primaju najnovija ažuriranja — što
  omogućava kontrolisano uvođenje. Dijalog Service Versions prikazuje novu
  kolonu *Release*, a administratori upravljaju kanalom iz odeljka Company
  Information. Više servisa u ovom periodu pokazuje veće skokove verzija
  isključivo zbog nove numeracije verzija po kanalima — ti skokovi ne nose
  nikakvu funkcionalnu izmenu.
- **Konfigurabilni sistemi pravila.** Tri nova sistema pravila stižu u API
  (svaki podrazumevano isključen, uključuje se po organizaciji): **pravila
  validacije** koja proveravaju izvučene vrednosti i označavaju neuspehe
  direktno na dokumentu, **pravila transformacije** koja automatski čiste ili
  prepravljaju izvučene vrednosti polja i tabela, i **izbor rasporeda
  zasnovan na pravilima** koji bira odgovarajući raspored dokumenta po
  pravilima umesto po tome odakle je dokument stigao.
- **Transparentnost uvoza e-pošte.** Dnevnik uvoza e-pošte sada prikazuje
  jedan proširiv red po prilogu, govori vam koji su dokumenti kreirani (sa
  dugmadima koja vode pravo do njih na kontrolnoj tabli), označava
  preskočene i podeljene stavke i omogućava preuzimanje originalne e-poruke
  kao `.eml` datoteke.
- **AI ekstrakcija tabela.** Novi strukturirani AI režim ekstrakcije za
  tabele, sa poljem za potvrdu „Use AI" po tabeli i po koloni u podešavanjima
  tipa dokumenta.
- **Stabilnost Web App-a.** Ispravljena beskonačna petlja ponovnog
  učitavanja nakon istekle sesije, ispravljen pokvareni Layout Builder, a
  tabele ekstrakcije sada imaju prevlačivi regulator visine.
- **Novo: Auth Bridge Service.** Novi servis kontinuirano sinhronizuje
  podatke za prijavu između EU i US regiona, sa ugrađenim samooporavkom i
  nadzorom.

---

## API Service — u produkciji: `12.57.8`

- **Pravila validacije (novo, po organizaciji):** sistem pravila koji
  konfiguriše administrator proverava izvučene vrednosti (ukupne iznose,
  obavezna polja i drugo) i označava neuspehe direktno na dokumentu,
  uključujući i to koje se pravilo aktiviralo. Pravila mogu da se testiraju
  probnim pokretanjem pre uključivanja, mogu da se uključe po tipu dokumenta
  i dolaze sa početnim katalogom podrazumevanih pravila (sva su isključena
  dok se sami ne opredelite).
- **Pravila transformacije (novo, po organizaciji):** automatski čiste ili
  prepravljaju izvučene vrednosti polja i tabela tokom obrade — podesivo po
  tipu dokumenta ili za celu organizaciju.
- **Izbor rasporeda zasnovan na pravilima (novo):** rasporedi dokumenata
  sada mogu da se biraju konfigurabilnim pravilima umesto da budu vezani za
  poreklo dokumenta. Postojeće ponašanje zasnovano na poreklu migrira se
  automatski, šabloni rasporeda mogu da se preimenuju, a duplirani naslovi
  rasporeda su sprečeni.
- **Brži izvozi sa kontrolne table:** izvozi pokrenuti sa kontrolne table
  sada se prosleđuju posebnom radnom procesu umesto da čekaju ciklus
  provere, pa počinju bez odlaganja.
- **Ispravljen blok izvoza za detekciju duplikata:** blok izvoza za
  sumnjive duplikate ponovo radi.
- **Podešavanja koja se nisu čuvala:** ispravljeno povremeno nečuvanje
  sačuvanih podešavanja kada je postojala starija obrisana kopija istog
  podešavanja.
- **Dokumenti sa neobičnim znakovima:** ispravljene greške pri čuvanju
  izazvane nevidljivim NUL znakovima u izvučenim podacima.
- **Ispravno „Updated by":** dokumenti automatski otpremljeni kao
  e-dokumenti više ne prikazuju sistemskog korisnika kao poslednjeg
  urednika — polje ostaje prazno dok neko zaista ne izmeni dokument.
- **Skenirani PDF-ovi sa dobrim tekstualnim slojem:** nova opcija omogućava
  DocBits-u da veruje tekstu koji je već ugrađen u skeniranu stranicu umesto
  ponovnog pokretanja OCR-a — brže i često tačnije.
- **E-fakture:** robusnije otkrivanje ugrađenog XML-a kada originalna
  datoteka mora ponovo da se proveri.
- **Zadaci:** novi prekidač na nivou organizacije koji korisnicima koji nisu
  administratori omogućava korišćenje filtera „Sve" u listi zadataka.
- **Uparivanje stavki:** ponašanje približnog (fuzzy) uparivanja sada je
  podesivo po stavci.
- **Stabilnost:** WebSocket veze se pri greškama zatvaraju čisto umesto da
  izazivaju izuzetke na serveru; sinhronizacija keša dozvola sama sebe
  proverava i popravlja; verzija servisa je sada vidljiva na krajnjoj tački
  za proveru zdravlja.

## Auth Service — u produkciji: `1.71.1`

- **Prijava sa više organizacija:** prijava sada pita u koju organizaciju
  ulazite kada korisnik pripada većem broju njih, sesije se vezuju za tu
  organizaciju, a nove krajnje tačke podržavaju izbor, promenu i podešavanje
  podrazumevane organizacije. Duplirana ili konfliktna članstva u
  organizacijama su očišćena i sada su sprečena na nivou baze podataka, uz
  brže pretrage članstva.
- **Ispravke podrazumevane organizacije:** prijava automatski bira vašu
  podrazumevanu organizaciju (a ne proizvoljnu), a promena podrazumevane
  organizacije stupa na snagu odmah umesto prikazivanja zastarelih podataka
  profila.
- **Ispravljena odjava:** rešena greška servera (HTTP 500) pri odjavi i
  vraćena krajnja tačka za opoziv tokena.
- **Bezbednost tokena:** provera i keširanje tokena sada poštuju
  organizaciju za koju je token izdat, a opoziv tokena je centralizovan.
- **Kanali izdanja:** kanal izdanja organizacije čuva se ovde, njime
  upravljaju administratori organizacije i izložen je aplikaciji i sloju
  rutiranja.

## Auth Bridge Service — u produkciji: `0.2.4.2` _(novi servis)_

- **Šta je to:** novi servis koji kontinuirano replikuje podatke o
  autentifikaciji između EU i US regiona, tako da nalozi i prijave ostaju
  usklađeni između regiona.
- **Samooporavak:** otkriva i popravlja odstupanja podataka između regiona —
  uključujući i to da se brisanja propagiraju — i automatski se oporavlja od
  gubitka veze umesto da gubi podatke.
- **Bezbednost i nadzor:** ranija petlja dvosmerne replikacije je
  zaustavljena i sada se aktivno otkriva i blokira; praćenje grešaka i
  upozoravanje su povezani; a servis prijavljuje svoju verziju u dijalogu
  Service Versions.

## Docflow Service — u produkciji: `2.6.1`

- **Kartice toka rada prihvataju prazne vrednosti:** kartice sa poljem za
  potvrdu i partner-kartice više ne otkazuju kada je polje legitimno prazno;
  provere tipa kartice su strože i predvidljivije.
- **Tokovi rada se ponovo pokreću pri stvarnim izmenama:** zaključavanje
  toka rada ponovo poštuje status dokumenta iz okidača, a sada prati i
  verziju dokumenta — tako da dokument čiji su se podaci zaista promenili
  može ponovo da prođe kroz tok rada čak i sa istim statusom, dok pravi
  duplikati ostaju blokirani.
- **Veći napredni tokovi rada:** ograničenje broja čvorova toka rada je
  povećano i sada je podesivo po okruženju.
- **Alternativni izvoz:** alternativni izvozi pokrenuti tokom rada sada su
  tako i označeni, pa sistemi u nastavku lanca mogu da ih razlikuju.
- **Otpornost:** servis se automatski ponovo povezuje kada se veza sa bazom
  podataka prekine tokom korišćenja, toleriše sporiji sistem za razmenu
  poruka umesto da otkazuje, a neuspeli API zahtevi sada se beleže sa punim
  kontekstom i sledljivim ID-jevima izvršavanja.

## Email Service — u produkciji: `1.38.4`

- **Dnevnik uvoza, obnovljen radi sledljivosti:** svaka uvezena e-poruka
  sada beleži koji su dokumenti iz nje kreirani, sa detaljnim redovima po
  prilogu.
- **Preuzimanje originalne e-poruke:** originalna poruka može da se preuzme
  kao `.eml` datoteka direktno iz dnevnika uvoza.
- **Oporavak priloga:** putanja oporavka od oštećenja sada obrađuje i poruke
  u čistom tekstu, pa se više oštećenih dolaznih e-poruka oporavlja umesto
  da se preskače.

## Extraction Service — u produkciji: `1.51.6`

- **Porez/neto se više ne zamenjuju:** ispravljen slučaj na američkim
  dokumentima gde je iznos poreza mogao biti dodeljen kao veći od neto
  iznosa kada je pronađeno više parova kandidata.
- **Više poreskih stopa po dobavljaču:** ekstrakcija sada obrađuje
  dobavljače čije fakture nose različite poreske stope na jednom dokumentu.
- **AI ekstrakcija tabela (novo, opciono):** strukturirane AI krajnje tačke
  za ekstrakciju tabela, aktiviraju se po organizaciji putem funkcionalnog
  prekidača.
- **Brži AI pozivi:** podešena je konfiguracija AI modela koji se koristi
  tokom ekstrakcije kako bi se izbeglo nepotrebno vreme obrade.
- **Ispravka pada:** rešena greška na dokumentima koji su tokom ekstrakcije
  proizvodili praznu listu kandidata.

## Fulltext Service — u produkciji: `1.37.2`

- **Popravljene migracije indeksa pretrage:** vraćene definicije migracija
  koje su odstupile, čime nadogradnje indeksa pretrage ostaju pouzdane.
- Interni radovi na rutiranju za novu infrastrukturu kanala izdanja.

## PO Match Service — u produkciji: `1.58.2`

- **Tolerantnije uparivanje:** PO uparivanje više ne otkazuje na neobičnim
  podacima — netekstualni brojevi artikala, nedostajuće količine i
  netekstualne vrednosti iznosa sada se obrađuju uredno umesto da izazivaju
  grešku.

## Web App — u produkciji: `10.41.8`

- **Iskustvo sa više organizacija:** nova stranica za izbor organizacije pri
  prijavi, posebna ikona za promenu organizacije u zaglavlju, podešavanja
  podrazumevane organizacije, a aplikacija prati region vaše aktivne
  organizacije. Prijava na pogrešan region tiho ponovo pokušava ispravan
  region i po potrebi vas vodi na izbor organizacije.
- **Nema više beskonačnih ponovnih učitavanja:** ispravljena beskonačna
  petlja ponovnog učitavanja koja je mogla da nastane kada server odbije
  sačuvani token sesije — aplikacija sada nameće pravo osvežavanje tokena
  umesto beskonačnog ponovnog učitavanja.
- **Ispravljen Layout Builder:** Layout Builder ponovo radi, a izbor
  rasporeda je odvojen od porekla dokumenta (u skladu sa novim izborom
  zasnovanim na pravilima u API-ju).
- **Tabele ekstrakcije:** tabele stavki sada imaju prevlačivu ručku za
  promenu veličine, pa tokom validacije tabeli možete dati više prostora.
- **Dnevnik uvoza e-pošte:** novi status „preskočeno" i oznake podele,
  proširivi redovi po prilogu, preuzimanje originalne e-poruke i dugmad sa
  ID-jem dokumenta koja vode pravo na kontrolnu tablu filtriranu na taj
  dokument.
- **Pretraga na kontrolnoj tabli:** padajuća lista vrednosti upita sada
  prikazuje lokalizovanu oznaku za polja sa listom vrednosti, a primeri u
  pomoći za pretragu su prerađeni.
- **Pouzdanost podešavanja:** korisnička podešavanja sada se pouzdano
  učitavaju pri prijavi preko SSO-a, a potvrda čuvanja prikazuje se samo
  kada je čuvanje zaista uspelo.
- **Zadaci:** filter „Sve" može da se vrati korisnicima koji nisu
  administratori putem novog prekidača na nivou organizacije.
- **Watchdog dnevnici:** više nisu ograničeni na 10.000 zapisa, uz opšta
  poboljšanja upotrebljivosti.
- **Tiketi podrške:** obrazac za podršku unapred popunjava vašu adresu
  e-pošte iz profila.
- **Podešavanja tipa dokumenta:** novo polje za potvrdu „Use AI" na tabelama
  i kolonama za upravljanje AI ekstrakcijom tabela.
- **Dijalog Service Versions:** nova kolona *Release* koja prikazuje kanal
  svakog servisa (frozen/latest), rutirana tako da ostane brza za zakačene
  organizacije.
- **Field Validation:** ispravljena greška pri povratku na Field Validation
  sa drugog ekrana, a dugme „Scripts" više ne vodi na stranicu 404.

---

## Samo nova numeracija verzija (bez funkcionalnih izmena)

**Auto Accounting** (`1.20.1`), **Barcode Service** (`1.17.1`), **OCR
Service** (`1.9.1`), **FTP Service** (`1.31.1`), **Operator Service**
(`1.40.2`) i **Ideas Service** (`0.3.1`) dobili su nove brojeve verzija u
okviru nove infrastrukture kanala izdanja. Njihovi naizgled veći skokovi
verzija ne nose izmene funkcionalnosti ili ponašanja u ovom periodu.
**Docnet Service** (`1.54.6`) je nepromenjen od 19. juna.

<!-- Generated by the docbits-changelog skill (version-boundary mode: exact
     git ranges between the ALT (2026-07-03/04) and NEU (2026-07-09..14)
     version-bump commits supplied by the user, per service). -->
