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
  čipa je pretraga podniza kroz sva polja, uključujući brojeve narudžbenica,
  barkodove i brojeve trebovanja. Broj rezultata, pločice statusa i paginacija
  opisuju isti skup dokumenata, a pretraga koja je dostigla prozor rezultata
  ili je izvršena bez indeksa celog teksta to i saopštava umesto da prijavi
  „kompletno". Sopstvena veza kontrolne table za pretragu (WebSocket) ranije
  nikada nije dosezala indeks celog teksta; sada doseže.
- **Dobavljači se češće prepoznaju.** Kada jedno polje za pretragu (PIB, IBAN,
  broj dobavljača) odgovara tačno jednom dobavljaču, taj dobavljač se koristi
  čak i ako široko polje kao što je naziv odgovara većem broju dobavljača.
  XRechnung CII i Facturae dokumenti ponovo nose svoja polja dobavljača. Tamo
  gde su matični podaci zamenili ekstrahovanu vrednost, ekran validacije to
  saopštava i omogućava vam da vratite original.
- **Usklađivanje narudžbenica objašnjava samo sebe.** Ekran saopštava zašto
  nema usklađivanja, opis neslaganja (tooltip) imenuje kolonu koja nije
  prošla, istorija usklađivanja navodi pravila transformacije koja su
  pokrenuta, a cene po jedinici narudžbenice izvode se iz neto iznosa. Ručna
  usklađivanja ponovo rade za organizacije bez rezervnog pravila, uklonjene
  narudžbenice ostaju uklonjene, a nasilno prekinut zadatak usklađivanja
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
  pregledom, primenom i poništavanjem, stranicu dobavljača sa trendom i
  primerima, dijagram toka obrade po dokumentu i dijagram skupa pravila
  narudžbenica koji saopštava zašto dokument nije prošao.
- **Brže tamo gde su podaci veliki.** Hladne prijave preskaču sabiranje knjige
  kredita koje je trajalo do 33 s, padajuća lista konta radi za organizacije
  sa više od 2.000 konta, stranica pravila E-dokumenata lista svojih 1.600
  pravila po stranicama na serveru umesto da zamrzava pregledač, a „Refresh"
  na kontrolnoj tabli narudžbenica vraća sveže podatke umesto keširane liste.
- **Bezbednost.** Source map datoteke frontenda više se ne isporučuju sa
  svakom verzijom, filteri pretrage matičnih podataka vezuju se kao SQL
  parametri umesto da se umeću u upit, istekli token se odbija čak i pri
  pogotku keša, a provera organizacije na tokenu za obradu sprovodi se
  nezavisno od sloja ispred nje.

---

## Web App — `10.66.3`

### Prijava i nalozi

- Prijava je brža. Provera pretplate pri prijavi tražila je puno stanje
  kredita, što je sabiralo milione redova knjige i često prelazilo klijentovo
  vremensko ograničenje od 10 s. Prijava sada samo pita da li pretplata
  postoji; stanja se i dalje izračunavaju na Settings → Subscription.
- Prelazak između regiona (EU ↔ US) zadržava vas prijavljene. Ciljni region
  nekoliko sekundi odgovara sa „invalid token" dok se sesija ne replicira, a
  dve putanje u kodu tumačile su to kao mrtvu sesiju.
- Prekrivajući prozor „Updating DocBits v10.59.3.1 → v10.59.3.1" koji se na
  sandbox-u beskonačno ponovo učitavao je ispravljen. Ponovno učitavanje iste
  verzije više ne prikazuje prozor, petlja je ograničena po kartici, a baner
  nudi ručni oporavak ako se to ponovo dogodi.
- Administratori mogu da dodele karticu Analytics Dashboard određenim
  ulogama, a izmene uloga se pouzdano čuvaju.
- Polje za potvrdu System Admin može da se označi na postojećem korisniku.
  Kreiranje sistemskog administratora iz frontenda sada ima efekta; posao
  sinhronizacije je ranije resetovao oznaku pri svakom pokretanju.
- Settings → Roles: lista članova se iscrtava umesto da visi iza indikatora
  učitavanja kada server odgovori greškom.
- Prijava na DocBits MCP server sprovodi dvofaktorsku autentifikaciju i
  jednokratnu saglasnost.

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
- Pretraga sa nula rezultata resetuje paginaciju i svaki broj na stranici.
  Ranije je paginacija zadržavala broj rezultata prethodne pretrage.
- Brojevi narudžbenica, brojevi porudžbina, barkodovi, tipovi faktura i
  brojevi trebovanja mogu da se pronađu bez čipa.

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
- Strukturirana ekstrakcija može da se uključi po dobavljaču, u tfidf
  iskačućem prozoru ekrana validacije i kao kolona samo za čitanje u
  Settings → Classification & Extraction.
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

- Opis neslaganja (tooltip) imenuje kolonu koja se nije poklopila. Ranije je
  bio prazan jer su se beležile samo poklopljene kolone, pa je ekran mogao da
  kaže samo „Mismatched".
- Dugme Auto Match takođe izvozi dokument kada je uključena opcija „PO Auto
  Match and Export". Ranije se izvoz dešavao samo kada je dokument otvoren sa
  kontrolne table preko „PO Match".
- Iskačući prozor tolerancije količine/cene po jedinici ostaje otvoren kada
  server odbije čuvanje, pa se unete vrednosti ne gube.
- Dugme Refresh na kontrolnoj tabli narudžbenica briše keš na strani servera
  pre ponovnog učitavanja. Narudžbenica uvezena iz ERP-a pojavljivala se tek
  nakon sedam do osam minuta.
- Stranica pravila usklađivanja narudžbenica iscrtava skup pravila kao
  dijagram toka, a istorija usklađivanja premeštena je u traku sa akcijama.

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
- List of Values: bočna traka prikazuje novu listu i uklanja obrisanu bez
  ponovnog učitavanja; zakasneli odgovori prethodne liste više ne prepisuju
  trenutnu.
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
  delujete: kartica objašnjava predloženu izmenu kroz četiri pitanja,
  omogućava vam da je prilagodite, pregleda šta bi uradila (ništa se ne čuva),
  primenjuje je, meri efekat i može da je poništi. Koraci za popravku vode
  direktno na stranicu podešavanja koju imenuju, unapred filtriranu po tipu
  dokumenta, polju ili pravilu.
- **Stranica dobavljača.** Izaberite dobavljača sa kartice ili pretražite red
  prilika po nazivu ili broju. Stranica prikazuje touchless stopu dobavljača
  tokom vremena (od 30 dana do 1 godine), njegove problematične dokumente i
  dokumente koji su prošli dobro, i nudi AI dijagnozu po dobavljaču. Do pet
  dobavljača može da se uporedi jedan pored drugog. Prikazuje se broj
  dobavljača umesto internog heša.
- **Tok obrade.** Dijagram po dokumentu i po klasteru prikazuje put kroz
  prijem, klasifikaciju, proveru e-dokumenta, dobavljača, OCR, ekstrakciju,
  validaciju, usklađivanje narudžbenica, odobrenje i izvoz, sa fazom koja ga
  je zaustavila.
- **Usklađivanje narudžbenica, objašnjeno.** Skup pravila narudžbenica
  iscrtava se kao dijagram toka na stranici podešavanja i u Touchless-u, sa
  putem koji je jedan dokument prošao i razlogom, jednostavnim jezikom, zašto
  nije prošao. Kodovi razloga razlikuju „narudžbenica nije pronađena" od
  „neslaganje stavki" i „nedostaje obavezno polje".
- **Segmentacija.** KPI pokazatelji, klasteri i predlozi mogu da se podele po
  polju dokumenta, na primer Order Type = Direct / Indirect.
- **Tačni brojevi.** KPI pločice poštuju filter pod-organizacije i broje samo
  dokumente koje detaljni prikaz može da navede. Sesija pregledača sistemskog
  korisnika organizacije računa se kao ljudska, pa se dokumenti ispravljeni
  ručno više ne svrstavaju kao touchless.
- Traka sa alatkama izveštaja smešta svoje kontrole na širokim ekranima, a
  boje tamnog režima dolaze iz teme.

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
- IDM izvoz: polje sa više vrednosti mapirano na numeričko polje (na primer
  količinu) rušilo je sadržaj izvoza. Vrednost se prvo pretvara u tekst.

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
  identifikatore. Narudžbenica, broj porudžbine, barkod, tip fakture, podtip
  fakture i broj trebovanja uopšte nisu imali granu za običnu tekstualnu
  pretragu.
- Čip broja fakture je tačan na Postgres-u, kao što je već bio na indeksu.
  Vodeće nule, decimalni oblici i velika/mala slova tretiraju se isto u
  slobodnom tekstu i u čipovima.
- WebSocket pretraga kontrolne table prenosi kredencijal pozivaoca servisu za
  pretragu celog teksta. Ranije je svako delegiranje odbijano, pa je kontrolna
  tabla tiho pretraživala samo Postgres i predstavljala odgovor kao kompletan.
- Pločice statusa, broj rezultata i lista rezultata izvršavaju se nad jednim
  skupom predikata. Pločice su ranije opisivale celu organizaciju tokom bilo
  koje pretrage.
- Dozvole pod-organizacije i tipa dokumenta primenjuju se pre prozora
  rezultata, pa dozvoljeni dokumenti više ne ispadaju iz ograničenja od
  500 / 10.000.
- Vektorska pretraga ograničava se na stvarni prozor rezultata i prijavljuje
  ograničenje umesto da prikazuje „(50)" kao tačan ukupan broj.
- Pretraga koja je izvršena bez indeksa celog teksta (indeks nedostaje, indeks
  kasni minutima, provera mogućnosti nije uspela, degradirano razrešavanje
  polja) prijavljuje status svog prozora umesto „kompletno".
- Izvozi kontrolne table skraćene pretrage nose red sa napomenom u CSV/XLSX
  datoteci i u e-poruci obaveštenja.
- Skripte dokumenata koje pozivaju pretragu celog teksta ispravno se
  autentifikuju i prijavljuju greške umesto da vraćaju prazan rezultat.

### Usklađivanje narudžbenica (usklađivanje unutar API-ja)

Za organizacije koje usklađuju u API-ju umesto u PO Match Service-u:

- Svako poređenje kolona se beleži, uključujući cenu po jedinici i količinu,
  pa opis neslaganja (tooltip) može da imenuje kolonu koja nije prošla.
- Narudžbenice koje je korisnik uklonio ostaju uklonjene u automatskom
  usklađivanju.
- Ispravljeni broj narudžbenice usklađuje se u istom čuvanju koje ga
  ispravlja.

### Analitika

- Touchless: sve backend izmene iza odeljka Web App iznad, uključujući dokaze
  koje beleži svaka faza obrade, trag usklađivanja narudžbenica, predloge
  izmena sa pregledom, primenom i vraćanjem, segmentaciju, masovni status u
  jednom pozivu po otkucaju i krajnju tačku trenda koja prihvata bilo koji
  prozor i dobavljača.
- Tri pozadinska zadatka analitike koja su padala pri svakom zakazanom
  pokretanju su ispravljena.

---

## PO Match Service — `1.59.34`

- Cena po jedinici stavke narudžbenice izvodi se iz njenog neto iznosa, a ne
  iz ukupnog iznosa sa porezom, a snimak narudžbenice dokumenta ponovo izvodi
  svoje cene po jedinici u trenutku usklađivanja.
- Servis beleži odakle je došao svaki kandidat za broj narudžbenice i koje je
  brojeve pokretanje tražilo. Sopstveni broj fakture dokumenta nikada nije
  kandidat za narudžbenicu. Odbačeno usklađivanje ostavlja svoj razlog na
  dokumentu za ekran.
- Kolona koja se nije poklopila se beleži, a kolone koje je rezervno pravilo
  uklonilo se mere.
- Narudžbenice koje je korisnik uklonio se poštuju, a zastarela pozadinska
  usklađivanja brišu se nakon konačnog isključenja.
- Ručno usklađivanje radi za organizacije čija pravila nemaju oznaku
  `is_fallback`. Korisnici su birali stavke, pritiskali usklađivanje i ništa
  se nije vraćalo.
- Nema više dokumenata ostavljenih u statusu „Queue": vremenska ograničenja
  naredbi baze podataka, keepalive signali i eksplicitni rukovalac mekog
  vremenskog ograničenja označavaju zadatak kao neuspeo umesto da se
  oslanjaju na nasilni prekid koji nije ostavljao trag.
- Dve produkcijske greške (cena po jedinici `NaN`, grupa bez količina) više ne
  obaraju celo usklađivanje.
- Izmene tolerancija čitaju se po zahtevu za usklađivanje, pa se tolerancija
  sačuvana malopre koristi pri sledećem usklađivanju.
- Trag odlučivanja u pet faza trajno se čuva po dokumentu za Touchless.

---

## Auth Service — `1.78.27`

- `/organisation/subscriptions` može da preskoči stanje kredita, a obračun
  kredita izvršava sve prozore ugovorne godine u jednoj naredbi umesto jednog
  upita po prozoru (32 upita od oko 700 ms svaki za najveću organizaciju).
  Dnevni zbirni pregled potrošnje pripremljen je za dalju upotrebu.
- Brojke preostalih tokena u čitačima organizacije izračunavaju se po
  ugovornoj godini.
- Istek tokena sprovodi se i pri pogocima keša. Keširani unos mogao je da
  autentifikuje do devet sati nakon što je token istekao.
- Provera tokena više ne upisuje nepromenjeni `org_id` nazad u red korisnika
  pri svakom zahtevu, što je proizvodilo po jedan UPDATE po pozivu.
- Provere zdravlja preskaču Redis U/I, a Redis klijent koristi zajednički
  bazen veza. Curenje memorije koje je teralo autoskaler na maksimalan broj
  replika je ispravljeno, a servis je vraćen na dva radna procesa.
- Ponovljena registracija dobavljača (magični link otvoren dvaput) ponovo
  koristi postojeće članstvo umesto da padne sa greškom dupliranog ključa.
- Nit za slanje e-poruke za resetovanje lozinke koristi jedinu registrovanu
  Flask aplikaciju; resetovanje je padalo sa „current Flask app is not
  registered" od 25. avgusta.
- Oznaka sistemskog korisnika može da se promeni na postojećem korisniku kada
  je nijedan drugi član ne drži.
- MCP prijava: MFA vezan za transakciju, jednokratna saglasnost i obavezan
  izbor naloga kada pregledač drži dva identiteta sesije.

---

## Auth Bridge Service — `0.5.7`

Replikacija autentifikacije EU ↔ US:

- Periodično usaglašavanje održava tok replikacije živim. Trajalo je oko 95 s
  dok je vremensko ograničenje pošiljaoca bilo 60 s, pa je svako
  šestočasovno usaglašavanje po rasporedu prekidalo tok.
- Kada tok prekine, slot replikacije ponovo se prikači na licu mesta umesto
  da se most ponovo gradi i ponovo izvršava puno usaglašavanje pri pokretanju.
- Usaglašavanje poredi primarne ključeve po stranicama umesto da učitava obe
  strane u memoriju, što više ne staje otkad se tabela tokena pridružila
  replikaciji.
- Postojeći izvor replikacije tretira se kao uspeh, a ne kao degradacija.

---

## Extraction Service — `1.55.33`

- Strukturirana ekstrakcija razrešava se po dobavljaču: podešavanje
  treniranog izgleda nadjačava podešavanje organizacije, isto kao što to čini
  AI model.
- Naučeno mapiranje kolona ne može da zabrani kolone koje faktura ima.
- AI ekstrakcija tabela: kolone iznosa tipizirane su kao brojevi sa opisom, a
  izmišljene nenumeričke vrednosti u kolonama iznosa („St." prepisano iz
  susedne ćelije u unit price per) odbacuju se umesto da se čuvaju.
- Američke fakture: kada je neto iznos već jednak ukupnom, porez se razrešava
  na 0 umesto da se zadrži lažno ekstrahovan porez. Šum pokretnog zareza
  ispod centa više ne odlučuje između kandidatskih parova neto/porez
  (268.28 + 22.13 gubilo je od neto = ukupno, porez = 0).
- Tabela čiji red zaglavlja nikada nije mapiran na stvarne nazive ekstrahuje
  se umesto da u potpunosti padne.

---

## Fulltext Service — `1.42.35`

- Keš rezultata pretrage uključen je u svakom okruženju; produkcija, sandbox i
  stage radili su bez njega otkad su kreirane aktivne env datoteke. Otpremanje
  i brisanje ga poništavaju, pa pretraga nakon otpremanja vidi novi dokument.
- Tačno `=` na dinamičkom tekstualnom polju poredi samo celu vrednost. Džoker
  znak na analiziranoj putanji činio je da `note_field=53173` odgovara „PO
  53173 / 2024".
- Goli identifikator sa crticom kao što je `2026-003` je jedan literal, a ne
  skup tokena.
- Brojevi narudžbenica pronalaze se u svakom obliku skladištenja, uključujući
  identifikatore koji se sastoje samo od cifara, čija je klauzula tačnog
  podudaranja tiho odbacivana.
- Putanje čitanja više ne kreiraju indeks koji čitaju. Indeks koji nedostaje
  ili je prazan prijavljivao je „kompletno, 0 rezultata"; svaki odgovor bez
  pogodaka sada nosi status prozora i razlog.
- Vrednosti valuta napisane rečima, nasleđena boolean mapiranja, datumi i
  poreske oznake preživljavaju ponovnu izgradnju tankog indeksa, a unosi
  indeksa bez polja otkrivaju se i oporavljaju iz ekstrakcije.

---

## Docflow Service — `2.10.11`

- Uvozi naprednih radnih tokova uslovljeni su pravom organizacije, a serija se
  proverava pre nego što se bilo šta upiše. Organizacija bez naprednog modula
  mogla je da uveze napredni radni tok koji potom nije imala kako da otvori.
- Preimenovanje radnog toka ide uz čuvanje, a preimenovanja šablona se trajno
  čuvaju.
- Ažuriranje „pending workflow execution" ponavlja se pri prekinutim vezama.
  Jedan neuspeo zahtev ostavljao je oznaku nepromenjenom i držao dokument van
  izvoza dok ga neko ne bi ponovo pokrenuo.

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

<!-- Release R1.0.13. Everything in the prod->sandbox code delta is announced.
     Held back because Jira "Release No." names the later release R1.1:
     DRFS-778 (discount due dates on import), DRFS-712, MEF-165, MEF-166,
     DOCB-14389. Announce them with R1.1. -->
