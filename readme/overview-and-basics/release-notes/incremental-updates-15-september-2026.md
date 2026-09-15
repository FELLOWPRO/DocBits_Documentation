# DocBits beleške o izdanju — 15. septembar 2026.

_Šta se menja u DocBits produkcijskom hitnom popravku 15. septembra 2026.
(izdanje R1.0.13), koji obuhvata sve od izdanja 1. septembra. Svaki servis
navodi verziju koja se isporučuje, a zatim novine i ispravke objašnjene
jednostavnim jezikom. Servisi koji nisu navedeni nisu imali izmene vidljive
korisnicima._

---

## Najvažnije

- **Jedan skup pravila za pretragu kontrolne table.** `field=value` je sada
  tačno ova vrednost na svakom mehanizmu pretrage, `field:value` znači
  „sadrži" (sa `value*` i `*value` za „počinje sa" i „završava se sa"), a
  `field!=value` vraća i dokumente koji uopšte nemaju vrednost. Pretraga bez
  čipa je pretraga podniza kroz sva polja, uključujući poslovne
  identifikatore. Broj rezultata i lista rezultata opisuju isti skup
  dokumenata, a pretraga koja je dostigla prozor rezultata ili je izvršena bez
  indeksa celog teksta to i saopštava umesto da prijavi „kompletno".
  Sopstvena veza kontrolne table za pretragu (WebSocket) ranije nikada nije
  dosezala indeks celog teksta; sada doseže.
- **Dobavljači se češće prepoznaju.** Kada jedno polje za pretragu (PIB, IBAN,
  broj dobavljača) odgovara tačno jednom dobavljaču, taj dobavljač se koristi
  čak i ako široko polje kao što je naziv odgovara većem broju dobavljača.
  XRechnung CII i Facturae dokumenti ponovo nose svoja polja dobavljača. Tamo
  gde su matični podaci zamenili ekstrahovanu vrednost, ekran validacije to
  saopštava i omogućava vam da vratite original.
- **Usklađivanje narudžbenica objašnjava samo sebe.** Ekran saopštava zašto
  nema usklađivanja i zašto usklađivanje nije zadržano, istorija usklađivanja
  navodi pravila transformacije koja su pokrenuta, a cene po jedinici
  narudžbenice izvode se iz neto iznosa. Ručna usklađivanja ponovo rade za
  organizacije bez rezervnog pravila, a nasilno prekinut zadatak usklađivanja
  označava dokument kao neuspeo umesto da ga zauvek ostavi u statusu „Queue".
- **Zaglavljeni dokumenti i lažne greške.** Organizacijama koje neprekidno
  otpremaju dokumenti su spuštani na prioritet reda koji tokom radnog vremena
  nikada nije opsluživan (866 dokumenata zaglavljenih u statusu „new" kod
  jednog klijenta). Mehanizam za ponovne pokušaje mogao je satima kasnije da
  prepiše uspešno izvezen dokument sa „error" i da za njega pošalje e-poruku o
  grešci izvoza. Taj put je zatvoren.
- **Touchless Intelligence.** Kartica Analitike koja meri koliko dokumenata
  prolazi kroz DocBits bez ljudskog dodira dobija svoje potpuno prvo izdanje:
  klastere problema sa AI savetima, masovnu analizu, predloge izmena sa
  pregledom, primenom i poništavanjem, AI dijagnozu po dobavljaču i dijagram
  toka obrade po dokumentu.
- **Brže tamo gde su podaci veliki.** Padajuća lista konta radi za
  organizacije sa više od 2.000 konta, stranica pravila E-dokumenata lista
  svojih 1.600 pravila po stranicama na serveru umesto da zamrzava pregledač,
  a „Refresh" na kontrolnoj tabli narudžbenica vraća sveže podatke umesto
  keširane liste.
- **Bezbednost.** Source map datoteke frontenda više se ne isporučuju sa
  svakom verzijom, filteri pretrage matičnih podataka vezuju se kao SQL
  parametri umesto da se umeću u upit, istekli token se odbija čak i pri
  pogotku keša, a provera organizacije na tokenu za obradu sprovodi se
  nezavisno od sloja ispred nje.

---

## Web App — `10.66.3`

### Prijava i nalozi

- Prekrivajući prozor „Updating DocBits v10.59.3.1 → v10.59.3.1" koji se na
  sandbox-u beskonačno ponovo učitavao je ispravljen. Ponovno učitavanje iste
  verzije više ne prikazuje prozor, petlja je ograničena po kartici, a baner
  nudi ručni oporavak ako se to ponovo dogodi.
- Polje za potvrdu System Admin može da se označi na postojećem korisniku.
  Kreiranje sistemskog administratora iz frontenda sada ima efekta; posao
  sinhronizacije je ranije resetovao oznaku pri svakom pokretanju.

### Kontrolna tabla i pretraga

- Nova pravila operatora, opisana i u iskačućem prozoru pomoći za pretragu:
  `=` je tačno ova vrednost (bez razlikovanja velikih i malih slova), `:` je
  „sadrži", `: value*` „počinje sa", `: *value` „završava se sa", `!=` je sve
  što nije tačno ova vrednost, uključujući dokumente bez vrednosti. Navodnici
  samo grupišu vrednost sa razmacima.
- Fraza pod navodnicima kao što je `"Johnson and Johnson"` pretražuje se kao
  jedna fraza. „and" i „or" unutar navodnika više se ne tumače kao veznici.
- Kada obična pretraga ne pronađe ništa, kontrolna tabla objašnjava pravilo i
  nudi čipove na jedan klik (`Invoice number : <term>`,
  `Purchase order : <term>`, `Supplier ID : <term>`).
- Pretraga sa nula rezultata resetuje paginaciju. Ranije je paginacija
  zadržavala broj rezultata prethodne pretrage.
- Brojevi trebovanja i podnosioci trebovanja pronalaze se običnom pretragom,
  bez čipa.

### Ekran validacije

- Vrednosti koje su matični podaci zamenili su označene. Žuta oznaka prikazuje
  originalnu i trenutnu vrednost, skup podataka i način na koji je podudaranje
  nađeno, a dugme vraća ekstrahovanu vrednost. Vrednosti koje su matični
  podaci potvrdili ili koje su popunjene iz narudžbenice dobijaju sopstvene
  oznake. Ranije su sve nosile oznaku „Extracted using saved rules".
- Pečat odobrenja se čuva čak i kada stranica već nosi drugu anotaciju.
  Preuzeti dokumenti sa anotacijama u tom slučaju nisu imali pečat.
- „Hide non mapped columns" zadržava kolone koje ste ručno trenirali (na
  primer Item Number i Purchase Order).
- Čuvanje pravila ekstrakcije radi nakon što unesete broj stranice, a zatim
  nacrtate okvir za polje. Taj redosled je ranije rušio čuvanje.
- Train Model se izvršava u pozadini. Ekran prikazuje „training started",
  proverava rezultat i prijavljuje uspeh ili neuspeh. Velike organizacije su
  ranije dobijale grešku gateway-a dok se treniranje nastavljalo na strani
  servera.
- Tamni režim: kursor makaza na ekranu za deljenje i prekidač režima na
  ekranu Auto Accounting ponovo su čitljivi.

### Usklađivanje narudžbenica

Izmene najavljene u [Hotfixes 8. septembar 2026.](incremental-updates-8-september-2026.md)
stižu u produkciju sa ovim izdanjem: usklađivanje opstaje nakon čuvanja,
usklađivanje se ponovo pokreće kada se broj narudžbenice ispravi, ekran
saopštava zašto nema usklađivanja i zašto usklađivanje nije zadržano,
istorija usklađivanja prikazuje pravila transformacije, a cena po jedinici
narudžbenice izračunava se iz neto iznosa. Pored toga:

- Dugme Auto Match takođe izvozi dokument kada je uključena opcija „PO Auto
  Match and Export". Ranije se izvoz dešavao samo kada je dokument otvoren sa
  kontrolne table preko „PO Match".
- Iskačući prozor tolerancije količine/cene po jedinici ostaje otvoren kada
  server odbije čuvanje, pa se unete vrednosti ne gube.
- Dugme Refresh na kontrolnoj tabli narudžbenica briše keš na strani servera
  pre ponovnog učitavanja. Narudžbenica uvezena iz ERP-a pojavljivala se tek
  nakon sedam do osam minuta.

### Automatsko računovodstvo

- Organizacije sa više od 2.000 konta pretražuju listu konta na serveru.
  Padajuća lista je za takve organizacije na sandbox-u bila prazna, a
  učitavanje stranice trajalo je pet sekundi.
- Konta na koja se dokument poziva razrešavaju se u serijama: dokumentu od 100
  stavki sa dve podele po stavci potrebna su 4 zahteva umesto 403.
- Naslovi tabela Auto Accounting i PO prate oznaku podešenu u alatu za izradu
  izgleda umesto fiksnog teksta.

### Podešavanja

- Settings → E-Documents → Rules lista po stranicama, pretražuje i sortira
  katalog od 1.600 pravila na serveru. Kartica je ranije iscrtavala sva
  pravila odjednom i zamrzavala pregledač. „Reset all" je jedan poziv umesto
  jednog po pravilu.
- Napredna podešavanja (Advanced Settings) tipa dokumenta prikazuju sačuvano
  stanje svakog prekidača. Sačuvano `false`, tolerancija `0` ili prazna
  padajuća lista bili su zamenjivani podrazumevanom vrednošću, a prelazak na
  drugi tip dokumenta ostavljao je vrednosti prethodnog tipa.
- Pravila transformacije: akcija „Set value" se čuva. Uređivač ju je slao pod
  nazivom koji server odbija.
- Veza ka podtipovima dokumenata prikazuje se na standardnim tipovima
  dokumenata.
- JPL mapiranje SMB izvoza preuzima se kao `.properties`, pa datoteka može
  ponovo da se otpremi. Bila je nazvana `.xml` i odbijana pri ponovnom
  otpremanju.

### Radni tokovi

- Preimenovanje radnog toka zadržava izmene kartica napravljene u istoj
  sesiji. Novi radni tokovi kreiraju se u jednom zahtevu za čuvanje, a
  preimenovanja šablona se trajno čuvaju.
- Izvezena datoteka radnog toka sadrži ceo izvozni omotač (verzija, naziv,
  opis). Napredni radni tokovi mogu ponovo da se uvezu; ranije je datoteka
  gubila verziju, čitala se kao standardni radni tok i bila odbijena.
- Filteri kolona na listi radnih tokova kombinuju se sa AND. Sa aktivnim
  filterom naziva i datuma, redovi koji odgovaraju samo nazivu provlačili su
  se u rezultat.
- Rokovi zadataka koriste format datuma iz vaših korisničkih podešavanja u
  listi, na tabli i u detaljnom prikazu.

### Analitika: Touchless Intelligence

Kartica Touchless (Analytics → Touchless) meri koliko dokumenata prođe kroz
DocBits a da ih nijedna osoba ne dotakne, i zašto ostali nisu. Ovo izdanje je
upotpunjuje:

- **Klasteri problema sa dokazima.** Dokumenti kojima je bila potrebna
  intervencija grupišu se po uzroku. Svaka kartica klastera imenuje polja,
  kodove validacije i poruke o greškama na kojima pada, kao i svog dobavljača,
  ili saopštava da ga nema. Klasteri koje DocBits može da popravi (pravilo,
  podešavanje polja) odvojeni su od onih koje može da popravi samo dobavljač,
  a budžet za AI analizu prvo ide na one koji se mogu popraviti.
- **AI analiza, označena kao takva.** Kartica klastera saopštava da li je
  savet napisao jezički model ili pravilo, šta je analiza brojala i kada je
  prestala da važi, i da li će klik ponovo iskoristiti keširanu analizu. Ako
  AI savetnik ne može da radi u ovom okruženju, kartica saopštava zašto.
- **Masovna analiza.** Analizirajte mnogo klastera u jednom pokretanju,
  pratite klaster po klaster šta pokretanje radi i pronađite rezultate nakon
  toga. Lista rezultata preživljava navigaciju i ponovno učitavanje, a
  pokretanje više ne visi na „Running · 0/6 done" u prikazu pod-organizacije.
- **Predlozi izmena.** Preporuka postaje nešto na osnovu čega možete da
  delujete: predlog koji cilja polje koje blokira dokumente, pregled koji
  prikazuje šta bi uradio (ništa se ne čuva), primena, izmereni efekat i
  poništavanje. Agenti dolaze do istih koraka putem MCP alata. Koraci za
  popravku vode direktno na stranicu podešavanja koju imenuju, unapred
  filtriranu po tipu dokumenta, polju ili pravilu.
- **Dijagnoza dobavljača.** Stranica dobavljača objašnjava prazno stanje umesto
  da prikazuje nule i nudi AI dijagnozu po dobavljaču. Možete da izaberete do
  pet dobavljača i uporedite ih jedan pored drugog.
- **Tok obrade.** Dijagram po dokumentu i po klasteru prikazuje put kroz
  prijem, klasifikaciju, proveru e-dokumenta, dobavljača, OCR, ekstrakciju,
  validaciju, usklađivanje narudžbenica, odobrenje i izvoz, sa fazom koja ga
  je zaustavila.
- **Razlozi usklađivanja narudžbenica.** Odluka o usklađivanju prati se po
  dokumentu (faza, prolaz, pravilo, kolona) i sažima u Touchless rezultat.
  Kodovi razloga razlikuju „narudžbenica nije pronađena" od „neslaganje
  stavki" i „nedostaje obavezno polje", a predlozi tolerancija savetnika
  ciljaju mehanizam pravila koji odlučuje.
- **Tačni brojevi.** KPI pločice poštuju filter pod-organizacije i broje samo
  dokumente koje detaljni prikaz može da navede.

### DocNet

- Lista aktivnosti (Activities), vidžet Recent Activity i vremenska linija
  misije su prevedeni. Sažeci revizije bili su na engleskom na sva 22 jezika.
- Agenti vide polja koja tip dokumenta definiše, a koja je ekstrakcija
  ostavila prazna. Ranije su zaključivali da takva polja ne postoje i
  preskakali obavezna ažuriranja bez pokušaja upisa.

### Bezbednost

- Source map datoteke frontenda uklanjaju se iz svake isporuke. Svako
  okruženje ih je posluživalo, uključujući produkciju.

---

## API Service — `12.83.156`

### Prepoznavanje dobavljača i matični podaci

- Dobavljač se identifikuje kada je jedno polje za pretragu jedinstveno. Sa
  više pretraživih polja rezultati su se kombinovali kao unija, pa je široko
  podudaranje naziva sa četiri dobavljača nadjačavalo PIB koji je odgovarao
  tačno jednom. Polja koja ne odgovaraju ničemu više ne poništavaju polja koja
  jesu odgovarala. Kako polja rade zajedno opisano je u
  [Master Data Settings](../../administration-and-setup/settings/global-settings/document-types/fields/master-data-settings.md).
- Zamene iz matičnih podataka beleže se sa svojim poreklom: skup podataka,
  konfiguracija, izvorno polje, operator i vrsta podudaranja. Ekran validacije
  to prikazuje i može da vrati ekstrahovanu vrednost.
- Cash Discount Term se uvozi iz BOD-a dobavljača; dobavljači sinhronizovani
  iz ERP-a imali su ga praznog. Discount Term Overwrite unet kao pun kod
  („143", „012", „X08") se primenjuje; ranije se gledao samo procentualni
  prefiks.
- Pretrage matičnih podataka ograničene su na 1.000 redova po stranici i
  pivotiraju se u SQL-u. Pretraga od 19.000 zapisa trajala je pet sekundi po
  pozivu i blokirala API.
- Nazivi svojstava filtera i tipovi podataka u pretrazi matičnih podataka
  vezuju se kao SQL parametri. Ranije su se umetali direktno u upit.

### Obrada dokumenata

- Dokumenti organizacije koja neprekidno otprema spuštani su na prioritet 9,
  koji red opslužuje tek kada je svaki viši prioritet prazan. Spuštanje je
  sada ograničeno na 3. Mehanizam za oporavak (reconciler) koji bi trebalo da
  vrati zaglavljene dokumente u red nije imao ispravne kredencijale u
  produkciji; sada ih ima.
- Završen, izvezen dokument nikada se ne prepisuje sa „error". Oznaka radnog
  toka koja nikada nije brisana navodila je mehanizam za ponovne pokušaje da
  jednom u minutu preuzima uspešno izvezen dokument dok ograničenje ponovnih
  pokušaja nije stavilo pečat „error" i poslalo klijentovu e-poruku o grešci
  izvoza, 2 h 17 min nakon izvoza.
- Spajanje i dodavanje prihvata `.PDF` i `.Pdf` datoteke. Izlaz skenera nazvan
  `SCAN0001.PDF` odbijan je sa „Only PDF files are allowed."
- Poništavanje keša skenira prostor ključeva jednom umesto dvaput i briše
  samo tipove podataka za pretragu koje je BOD promenio. Svaki BOD je ranije
  brisao ceo keš pretrage za organizaciju, blokirajući API dok je prolazio
  kroz sve ključeve.
- Ponovno treniranje modela izvršava se kao pozadinski zadatak i odmah vraća
  status koji korisnički interfejs proverava.
- Token za obradu iz druge organizacije odbija se nezavisno od provere
  članstva u pod-organizaciji ispred njega.
- Sinhronizacija korisnika ne dira oznaku sistemskog korisnika umesto da je
  resetuje pri svakom pokretanju.

### Izvoz

- M3 linije prijema uparuju izvezenu cenu po jedinici sa osnovom cene same
  stavke fakture. Cena je putovala sa deliocem stavke narudžbenice, pa je ERP
  ponovo obračunavao stavku na 1.000 puta veći iznos od fakturisanog.
- Izvoz tabele preživljava stavku čija je narudžbenica uklonjena; stavka se
  izvozi bez osnove cene.

### E-dokumenti

- XRechnung CII fakture čiji je dospeli iznos za plaćanje 0,00 jer unapred
  plaćeni iznos pokriva ukupan iznos prikazuju ukupan zbir (BT-112) kao ukupan
  iznos. Klijent je video „total amount 0,00".
- XRechnung CII i Facturae dokumenti ponovo isporučuju svoja polja
  dobavljača. Zastarela prepisivanja na nivou organizacije zaklanjala su
  ispravno podrazumevano mapiranje, pa prepoznavanje dobavljača nikada nije
  moglo da nađe podudaranje.
- Katalog pravila validacije lista se po stranicama, pretražuje i sortira na
  serveru, sa fasetama za traku filtera.

### Klasifikacija

- Švajcarski dokumenti klasifikuju se kao `de_CH`, `fr_CH` ili `it_CH` na
  osnovu sadržaja (CHF iznosi, CHE PDV brojevi, CH IBAN). Lokalitet se uzimao
  iz podrazumevane vrednosti organizacije i švajcarski dokumenti dobijali su
  `de_DE`.

### Pretraga kontrolne table

- Jedna semantika operatora na Postgres-u i ClickHouse-u: `=` tačno, `:`
  sadrži sa džoker znakovima na krajevima, `!=` komplement uključujući prazne
  vrednosti. Na Postgres-u je `=` ranije bilo podudaranje prefiksa, pa je
  `invoice_id=911892112` vraćalo i 911892112333.
- Obična pretraga je pretraga podniza kroz sva polja, uključujući poslovne
  identifikatore. Identifikator sa crticom kao što je `2026-003` je jedan
  literal, a tip klauzule se više ne menja posle petog znaka.
- Čip broja fakture je tačan na Postgres-u, kao što je već bio na indeksu.
  Vodeće nule, decimalni oblici i velika/mala slova tretiraju se isto u
  slobodnom tekstu i u čipovima.
- WebSocket pretraga kontrolne table prenosi kredencijal pozivaoca servisu za
  pretragu celog teksta. Ranije je svako delegiranje odbijano, pa je kontrolna
  tabla tiho pretraživala samo Postgres i predstavljala odgovor kao kompletan.
- Broj rezultata i lista rezultata izvršavaju se nad jednim skupom predikata.
  Broj je ranije bio Postgres aproksimacija dok je lista dolazila iz indeksa.
- Vektorska pretraga ograničava se na stvarni prozor rezultata i prijavljuje
  ograničenje umesto da prikazuje „(50)" kao tačan ukupan broj.
- Pretraga koja je izvršena bez indeksa celog teksta (indeks kasni minutima,
  provera mogućnosti nije uspela, degradirano razrešavanje polja) prijavljuje
  status svog prozora umesto „kompletno".
- Skripte dokumenata koje pozivaju pretragu celog teksta ispravno se
  autentifikuju i prijavljuju greške umesto da vraćaju prazan rezultat.

### Usklađivanje narudžbenica (usklađivanje unutar API-ja)

Za organizacije koje usklađuju u API-ju umesto u PO Match Service-u:
ispravljeni broj narudžbenice usklađuje se u istom čuvanju koje ga ispravlja.

### Analitika

- Touchless: sve backend izmene iza odeljka Web App iznad, uključujući dokaze
  koje beleži svaka faza obrade, trag usklađivanja narudžbenica, predloge
  izmena sa pregledom, primenom i vraćanjem, i masovni status u jednom pozivu
  po otkucaju.

---

## PO Match Service — `1.59.34`

- Cena po jedinici stavke narudžbenice izvodi se iz njenog neto iznosa, a ne
  iz ukupnog iznosa sa porezom, a snimak narudžbenice dokumenta ponovo izvodi
  svoje cene po jedinici u trenutku usklađivanja.
- Servis beleži odakle je došao svaki kandidat za broj narudžbenice i koje je
  brojeve pokretanje tražilo. Sopstveni broj fakture dokumenta nikada nije
  kandidat za narudžbenicu. Odbačeno usklađivanje ostavlja svoj razlog na
  dokumentu za ekran.
- Ručno usklađivanje radi za organizacije čija pravila nemaju oznaku
  `is_fallback`. Korisnici su birali stavke, pritiskali usklađivanje i ništa
  se nije vraćalo.
- Nema više dokumenata ostavljenih u statusu „Queue": vremenska ograničenja
  naredbi baze podataka, keepalive signali i eksplicitni rukovalac mekog
  vremenskog ograničenja označavaju zadatak kao neuspeo umesto da se
  oslanjaju na nasilni prekid koji nije ostavljao trag.
- Izmene tolerancija čitaju se po zahtevu za usklađivanje, pa se tolerancija
  sačuvana malopre koristi pri sledećem usklađivanju.
- Trag odlučivanja u pet faza trajno se čuva po dokumentu za Touchless.

---

## Auth Service — `1.78.27`

- Istek tokena sprovodi se i pri pogocima keša. Keširani unos mogao je da
  autentifikuje do devet sati nakon što je token istekao.
- Provera tokena više ne upisuje nepromenjeni `org_id` nazad u red korisnika
  pri svakom zahtevu, što je proizvodilo po jedan UPDATE po pozivu.
- Curenje memorije koje je teralo autoskaler na maksimalan broj replika je
  ispravljeno, a servis je vraćen na dva radna procesa.
- Oznaka sistemskog korisnika može da se promeni na postojećem korisniku kada
  je nijedan drugi član ne drži.

---

## Auth Bridge Service — `0.5.7`

- Kada tok replikacije EU ↔ US prekine, slot replikacije ponovo se prikači na
  licu mesta umesto da se most ponovo gradi i ponovo izvršava puno usklađivanje
  pri pokretanju, tokom kojeg je slot stajao neaktivan.

---

## Extraction Service — `1.55.33`

- AI ekstrakcija tabela: kolone iznosa tipizirane su kao brojevi sa opisom, a
  izmišljene nenumeričke vrednosti u kolonama iznosa („St." prepisano iz
  susedne ćelije u unit price per) odbacuju se umesto da se čuvaju.
- Američke fakture: šum pokretnog zareza ispod centa više ne odlučuje između
  kandidatskih parova neto/porez (268.28 + 22.13 gubilo je od neto = ukupno,
  porez = 0).

---

## Fulltext Service — `1.42.35`

- Keš rezultata pretrage uključen je u svakom okruženju; produkcija, sandbox i
  stage radili su bez njega otkad su kreirane aktivne env datoteke. Otpremanje
  i brisanje ga poništavaju, pa pretraga nakon otpremanja vidi novi dokument.
- Obična pretraga samog broja fakture vraća fakturu sa tačnim podudaranjem.
  Vrednosti valuta napisane rečima, nasleđena boolean mapiranja, datumi i
  poreske oznake preživljavaju ponovnu izgradnju tankog indeksa, a unosi
  indeksa bez polja otkrivaju se i oporavljaju iz ekstrakcije.
- Tačno `=` na dinamičkom tekstualnom polju poredi samo celu vrednost. Džoker
  znak na analiziranoj putanji činio je da `note_field=53173` odgovara „PO
  53173 / 2024".
- Goli identifikator sa crticom kao što je `2026-003` je jedan literal, a ne
  skup tokena.
- Putanje čitanja više ne kreiraju indeks koji čitaju, a svaki odgovor bez
  pogodaka nosi status prozora i razlog.
- Ograničenje od 50 na strani servisa za vektorsku pretragu je uklonjeno.

---

## Docflow Service — `2.10.11`

- Uvozi naprednih radnih tokova uslovljeni su pravom organizacije, a serija se
  proverava pre nego što se bilo šta upiše. Organizacija bez naprednog modula
  mogla je da uveze napredni radni tok koji potom nije imala kako da otvori.
- Preimenovanje radnog toka ide uz čuvanje, a preimenovanja šablona se trajno
  čuvaju.

---

## Docnet Service — `1.56.12`

- Otkrivanje polja vraća svako polje zaglavlja koje izgled definiše, popunjeno
  ili ne, i poklapa se sa onim što zaštita upisa proverava. Agenti su
  preskakali obavezna ažuriranja polja jer su prazna polja izgledala kao da ne
  postoje.
- Identiteti se keširaju pod istim ključem ograničenim na organizaciju koji
  koristi API, pa granica API ključa organizacije važi u oba servisa.

---

## Email Service — `1.41.6`

- Deljeni Office 365 poštanski sandučići sa više od deset potfoldera
  razrešavaju svaki folder. Microsoft Graph vraća foldere po deset; 11. i
  svaka sledeća konfiguracija nije uspevala pri svakoj proveri sa „unable to
  find the selected Folder".

---

## FTP Service — `1.32.18`

- SFTP planer pokreće se u svakom radnom procesu umesto pre grananja (fork).
  Periodični SFTP uvozi tiho su padali sa oštećenim stanjem planera, dok je
  svež proces radio bez problema.

---

## Auto Accounting `1.21.7`, Barcode `1.18.14`, OCR `1.10.11`, Operator `1.42.12`, Ideas `0.3.6`

Samo izmene u izgradnji i isporuci (ažuriranje osnovne slike, CI
kredencijali). Nema promene u ponašanju.

<!-- Release R1.0.13. Announced: tickets with Jira "Release No." = R1.0.13 and a
     status on sandbox or beyond, plus DOCB-14454, DOCB-14450, DOCB-14415,
     DOCB-14419, DOCB-14431, DOCB-14045/46 (no Release No., on sandbox).
     Held back (Release No. R1.1): DRFS-778, DRFS-712, MEF-165, MEF-166, DOCB-14389.
     Labelled R1.0.12 but code ships now: DRFS-746/748/749/750/751, DOCB-14282. -->
