# DocBits beleške o izdanju — 12–25. avgust 2026.

_Šta se menja u DocBits produkcijskoj nadogradnji 25. avgusta 2026, koja
obuhvata sve od izdanja 12. avgusta. Svaki servis navodi verziju koja se
isporučuje, a zatim novine i ispravke objašnjene jednostavnim jezikom. Servisi
koji nisu navedeni nisu imali izmene vidljive korisnicima._

---

## Najvažnije

- **Stroža izolacija organizacija.** Bezbednosna provera zatvorila je nekoliko
  mesta na kojima su podaci jedne organizacije mogli da se čitaju ili menjaju
  iz druge: skripte dokumenata, liste korisnika pod-organizacija, članstva u
  grupama i token za obradu koji dokument nosi kroz tok obrade sada se svi
  proveravaju u odnosu na organizaciju pozivaoca. Odobrenja takođe ispravno
  sprovode princip četvoro očiju: drugi odobravalac mora biti druga osoba, a
  ne ona koja je odobrila prva.
- **Dokumenti više ne ostaju zaglavljeni.** Ispravljena su četiri odvojena
  uzroka trajnog zaglavljivanja dokumenata: izvozi koji su ostajali u statusu
  „Exporting" nakon odbijanja, restarti koji su se zamrzavali kada korak
  obrade padne, deljenja po barkodu koja se nikada ne jave nazad i ekran
  računovodstva koji visi na „Preparing…". U svakom slučaju dokument sada ili
  završi obradu ili prikaže stvarnu grešku na osnovu koje možete da reagujete.
- **Knjižna odobrenja se prepoznaju kao knjižna odobrenja.** XRechnung 3.0,
  3.0.1 i 3.0.2 knjižna odobrenja u CII sintaksi, čista CII knjižna odobrenja
  i ZUGFeRD 2.4 / Factur-X 1.08 dokumenti sada se ispravno klasifikuju, a
  ukupan iznos se čita iz ispravnog polja. Skenirani dokumenti koji pominju i
  „fakturu" i „knjižno odobrenje" razrešavaju se prema tome koja je ključna
  reč bliža oznaci tipa dokumenta, a iznosi ponovo postaju pozitivni kada
  knjižno odobrenje reklasifikujete nazad u fakturu.
- **PO uparivanje računa onako kako očekujete.** Tolerancije se porede kao
  tačne decimalne vrednosti umesto vrednosti u pokretnom zarezu, zasnovane su
  na vrednosti porudžbenice, a fakture koje se pozivaju na više porudžbenica
  uparuju se sa svima njima. Kolone koje nikada niste mapirali više ne
  iskrivljuju proveru iznosa stavki, a kada obavezne kolone nedostaju, greška
  ih imenuje.
- **Pokretanja radnih tokova čuvaju svoj rad.** Radni tok koji upisuje
  vrednost polja sada je upisuje na dokument tako da je kasniji izvoz ne može
  tiho poništiti. Ponovljeni okidači više ne odbacuju ono što je pokretanje
  već uradilo, a dva okidača nad istim dokumentom staju u red umesto da jedan
  drugom otimaju zaključavanje.
- **E-poruke za resetovanje lozinke ponovo se šalju.** Tiho nikada nisu
  napuštale server. Obrazac za resetovanje sada prikazuje stvarnu povratnu
  informaciju nakon slanja, a odgovor više ne otkriva da li nalog postoji.

---

## Web App — `10.55.0`

### Prijava i nalozi

- Resetovanje lozinke ponovo radi od početka do kraja: e-poruka stiže, obrazac
  potvrđuje slanje, a odgovor je isti bez obzira na to da li adresa ima nalog
  ili ne.
- Odjava u jednoj kartici pregledača odjavljuje i ostale kartice, bez
  iskačućih poruka o grešci koje su se ranije pojavljivale kada se kartice ne
  slože oko sesije.
- Ako vaša organizacija zahteva uključivanje dvofaktorske autentifikacije,
  ekran za prijavu to sada saopštava umesto da ne uspe bez poruke. Prijava
  pristupnim ključem preko regiona prikazuje prevedene poruke o grešci, a
  njeno dugme za potvrdu je vidljivo.
- Administratori više ne mogu da uključe obaveznu MFA za celu organizaciju pre
  nego što registracija pri prijavi postane dostupna, što je ranije moglo da
  zaključa korisnike napolju.

### Ekran validacije

- Klizač zumiranja sada ide do 150% (ranije je stajao na 80%), a zumiranje u
  tabelu radi i preko širine kontejnera umesto da ne radi ništa.
- Prazna polja iznosa računaju se kao 0 umesto da izbace poruku o grešci, a
  dvostruki klik na sliku dokumenta se ignoriše kada nijedno polje nije
  izabrano.
- Baner koji se prikazuje kada druga sesija drži zaključan dokument nije imao
  tekst; sada se sam objašnjava. Označavanje tabele više ne izaziva lažno
  upozorenje „dokument je izmenjen spolja" zbog vaše sopstvene izmene.
- U AI tabeli, ponovno mapiranje kolone koje bi poništilo mapiranje druge
  kolone prvo traži potvrdu, a vrednosti koje nisu brojevi označavaju se u
  kolonama AMOUNT i NUMBER.
- Kartica „Extracted table" ponovo vodi na ručno treniranje tabele kada je
  prazna i više se ne vrti beskonačno kada AI tabela već postoji.
- Brojevi artikala u Compare tabeli stavki prikazuju se kao identifikatori, a
  ne zaokruženi kao iznosi.
- Polja odobravaoca razrešavaju ID-jeve korisnika i grupa u imena, pa nikada
  ne prikazuju sirov ID niti ostaju prazna. Rokovi zadataka konvertuju se kroz
  jedinstvenu putanju svesnu UTC-a, pa svaki korisnik vidi isti datum.
- Dokumenti vraćeni na validaciju prikazuju indikator učitavanja umesto mrtvog
  ekrana dok se pripremaju.
- Otvaranje velikih faktura dobavljača je primetno brže.

### Računovodstvo

- Podeljene stavke zadržavaju znak % nakon pritiska na Enter, a 0 % se
  prihvata kao vrednost.
- U filteru konta, Enter potvrđuje prvi odgovarajući konto umesto da ne radi
  ništa.
- Flexdimension znakovi mapiraju se po ID-ju dimenzije, pa dimenzije dospevaju
  u pravu kolonu čak i kada se redosled razlikuje.
- Neuspela priprema knjiženja oporavlja se uz poruku o grešci umesto da
  zauvek visi na „Preparing…", a ponovno otvaranje dokumenta više ne služi
  zastarele podatke prethodnog dokumenta.

### PO uparivanje

- Otvaranje PO uparivanja bez svih mapiranih obaveznih kolona ponovo je
  moguće; kada nešto potrebno nedostaje, poruka imenuje tačne kolone.
- Kolone koje nisu mapirane ni na šta sakrivaju se pri otvaranju ekrana, nakon
  što vas jednom pita, i više ne ulaze u izračunavanje iznosa stavki.
- Uparena količina se osvežava nakon čuvanja, a iskačući prozor o nedostajućoj
  koloni vodi vas na Validaciju polja gde to možete da ispravite.

### Kontrolna tabla i pretraga

- Kolone zasnovane na padajućim listama (tip fakture, status i slično)
  prikazuju svoju oznaku na jeziku vašeg interfejsa umesto sirove sačuvane
  vrednosti.
- Pretraga slobodnim tekstom prihvata zagrade kao običan tekst; ranije je
  odbijala upit. Operator filtera „nije jednako" ostaje izabran, a ručno
  uređivanje filtera više ne kvari naziv polja.
- Izbor pod-organizacije u brzoj pretrazi ubacuje njen naziv, a ne njen uuid,
  i automatsko dopunjavanje pod-organizacija više ne navodi duplikate.
- Kontrolna tabla sada može da dohvati do 10.000 dokumenata po prozoru
  pretrage, pa se veliki skupovi rezultata ispravno listaju po stranicama.
- Panel duplikata dokumenata prikazuje iste razrešene kolone kao glavna lista,
  a višerečne vrednosti filtera dobavljača preživljavaju pritisak na Enter.
- Brojač otvorenih zadataka u bočnoj traci broji zadatke u kontekstu vaše
  pod-organizacije, a ne u kontekstu dokumenta koji je slučajno otvoren.

### Zadaci

- Kanban kolone učitavaju se stranicu po stranicu dok skrolujete, pa se table
  sa mnogo zadataka brzo učitavaju.
- E-poruka o dodeli šalje se kada se zadatak dodeli — jednom. Uređivanje
  zadatka ili označavanje kao završenog više je ne šalje ponovo, a datum
  „dodeljeno" ostaje datum dodele. E-poruke zadataka takođe se ispravno
  prikazuju u Outlook-u.

### Workflow Builder

- Lista radnih tokova zadržava vašu pretragu, redosled sortiranja, stranicu i
  veličinu stranice kada otvorite radni tok i vratite se, uključujući i
  povratak preko putanje (breadcrumb). Stranica se podrazumevano otvara na
  kartici List.
- Prekidač „pokreni radni tok pri promeni" u alatu za izradu izgleda sada
  zaista kontroliše pokretanje, a njegovo uključivanje zahteva izbor radnog
  toka.

### Podešavanja i administracija

- Veza za preuzimanje WatchDog-a i komanda za podešavanje pokazuju na
  okruženje u kojem se nalazite, a ne uvek na produkciju.
- Stabla odlučivanja: izabrano polje dokumenta ostaje istaknuto kada se birač
  ponovo otvori, skraćene oznake dobijaju tooltip, a pri dodavanju linije
  prikazuju se imena korisnika (a ne sirovi ID-jevi).
- Polje za potvrdu System Admin može da se menja pri uređivanju korisnika.
- Stranica matičnih podataka više se ne pojavljuje prazna zbog trke pri
  sortiranju, a sortiranje po bedževima više ne ruši stranicu.
- Pretplata u statusu „otkazivanje u toku" može da se nastavi.
- Stranica sa detaljima XSLT-a prijavljuje greške pri učitavanju umesto da ne
  prikaže ništa, a podešavanja obaveštenja e-poštom koriste punu širinu
  stranice sa funkcionalnim panelom dnevnika.
- Birač organizacija za korisnike sa više organizacija ima ispravan raspored
  redova, veličine i boje teme.
- Analitika: Core Web Vitals se iscrtavaju iz stvarnih izmerenih podataka,
  prikaz servisa dnevnika radi, a neuspeo zahtev za metrike prikazuje stanje
  greške umesto da iscrtava nule.
- „Use Default Template" u upravljaču izgleda kopira podrazumevani izgled
  kako je i zamišljeno; ranije se rušio ili tvrdio da podrazumevani ne
  postoji.
- Prilagođene oznake polja više ne preklapaju ugrađene prevode standardnih
  polja, a ekrani DocNet-a (AI Workforce), uključujući Agent Wizard, su
  prevedeni.
- Ponude na portalu dobavljača: slanje ponude sa REF1 vrednošću izvan
  dozvoljene liste je blokirano, upravljane jedinice mere prikazuju se u
  tabeli stavki, a stil odobravanja primenjuje se samo na ponude po ugovoru.
- MediOrder dobija otkrivanje duplikata dokumenata na svom ekranu validacije.

## API Service — `12.82.3`

### Bezbednost i izolacija organizacija

- Promena aktivne organizacije proverava se u odnosu na vaše stvarno članstvo
  i u slučaju neuspeha odbija pristup, a interna test krajnja tačka koja je
  mogla da se zloupotrebi za prelazak između organizacija je ugašena.
- Skripte dokumenata više ne mogu da se čitaju niti prepisuju preko granica
  organizacija, ni preko poziva za primenu na dokument ni preko tuđeg ID-ja
  verzije pri čuvanju.
- Liste korisnika pod-organizacija i liste članova grupa vraćaju samo osobe iz
  organizacije pozivaoca, a dodavanje više korisnika u grupu odjednom više ne
  ispušta sve osim prvog.
- Kredencijal iz pogrešne organizacije odbija se pre nego što može da postane
  token za obradu dokumenta, a upiti pretrage celog teksta izvršavaju se kao
  korisnik koji poziva, a ne kao servisni identitet.
- Odobravanje u četiri oka se sprovodi: drugi odobravalac mora da se razlikuje
  od osobe koja je odobrila prva.
- Live lista PO Dashboard-a ograničena je na pod-organizacije korisnika.

### Tok obrade dokumenata

- Dokumenti kojima je izvoz odbijen više ne stoje zauvek u statusu
  „Exporting", a greške izvoza uvek nose poruku umesto prazne.
- Kada korak obrade padne, dokument prelazi u stanje greške umesto da ostane
  zaglavljen u „restart u toku" bez izlaza.
- Deljenje po barkodu koje ne uspe ili istekne označava dokument kao Error
  umesto da tiho prikazuje „Running", a deljenje koje ne proizvede nijedan
  poddokument zadržava roditeljski dokument i označava ga umesto da sve
  obriše.
- Neuspeo ponovni pokušaj više ne može da prepiše dokument koji je u
  međuvremenu završio obradu.
- Dokumenti restartovani bez interakcije korisnika i poddokumenti nastali
  deljenjem sada rade pod trajnim tokenom organizacije, pa dugotrajna obrada
  ne umire sa isteklom sesijom.
- Prazan odgovor šablona izgleda više se ne kešira šest sati, zbog čega su
  izgledi ranije nestajali dok keš ne istekne.

### Ekstrakcija i e-dokumenti

- Iznosi napisani sa minusom na kraju („100,00-") parsiraju se kao negativni
  umesto da budu odbačeni.
- Švajcarski dokumenti se prepoznaju kao švajcarski (CHF, CHE PDV brojevi, CH
  IBAN-i) umesto da podrazumevano dobiju nemačke konvencije, a datumi napisani
  tipografskim crticama ispravno se parsiraju.
- XRechnung 3.0, 3.0.1 i 3.0.2 knjižna odobrenja u CII sintaksi klasifikuju se
  kao knjižna odobrenja sa ukupnim iznosom pročitanim iz polja ukupnog zbira;
  isto važi za čista CII knjižna odobrenja. Deklarisana verzija ZUGFeRD 2.4 /
  Factur-X 1.08 ima prednost nad generičkim identifikatorom profila, a goli
  XRechnung tipovi razrešavaju se u svog UBL ili CII parnjaka umesto da ne
  uspeju.
- Padajuća polja (lista vrednosti) kao što su Tax Country i Tax Code
  zadržavaju svoju vrednost kroz transformaciju polja; ranije su bila
  pražnjena.
- Ekstrakcija tabela: greška u koloni koja sadrži samo brojeve ostaje u toj
  koloni umesto da obori celu tabelu, AI ekstrakcija tabela dobija vremensko
  ograničenje koje preživljava višeserijske obrade, a ispravljena su dva pada
  na neobičnim oblicima tabela (redovi bez pozicija na stranici, nejednaki
  brojevi kolona).
- Šabloni izvornih pravila podudaraju se bez razlikovanja velikih i malih
  slova.

### Izvoz

- Poreska provera koja ne uspe tokom pregleda izvoza vraća čitljivu grešku
  umesto serverske greške, na obe krajnje tačke pregleda.
- SFTP izvoz može da pošalje originalni dokument uz konvertovani.
- Kada konfiguracije izvoza postoje na više nivoa, dosledno pobeđuje
  najspecifičnija.
- BOD izvozi mogu da nose atribute tipa kolone putem mapiranja.

### Uvoz i matični podaci

- Dnevnik uvoza e-pošte je potpun: odbijene i neuspele dolazne e-poruke uvek
  dobijaju red u dnevniku sa tačnim razlogom. Nema više tihih ispuštanja.
- BOD uvozi porudžbenica drže podstavke uz ispravnu stavku; prenesena oznaka
  ih je ranije vezivala za pogrešnu.
- Uvoz CSV datoteke sa više novih dobavljača radi (njihovi generisani ID-jevi
  se više ne sudaraju), aliasi uslova kasa-skonta se uvoze i poštuju
  podešavanje „on conflict", a izbor IGNORE pri konfliktu važi i šire od
  dobavljača.
- Predlog dobavljača (TF-IDF) zadržava svoj ID dobavljača kada se preferenca
  ažurira, pa predlozi više ne pokazuju ni na šta.

### Ostale ispravke

- Redovi kontrolne table razrešavaju oznake padajućih lista na jeziku
  korisnika, bez blokiranja zahteva.
- Nakon uređivanja polja, status PO uparivanja se ažurira umesto da prikazuje
  stanje pre izmene.
- Purchase Order Change dokumenti dobijaju pet polja u paritetu sa Purchase
  Order dokumentima i podrazumevani izgled validacije polja.
- Odgovori o greškama na 152 krajnje tačke vraćaju čitljive poruke umesto
  sirovih objekata izuzetaka, a stranica analitike dnevnika više ne odgovara
  sa 502 za organizacije bez indeksa dnevnika.

## Auth Service — `1.77.9`

- E-poruke za resetovanje lozinke tiho se nikada nisu slale; ispravljeno,
  zajedno sa problemom bezbednosti niti koji je ležao ispod toga.
- Ponovo iskorišćeni refresh token se odbija: autoritativna provera u bazi
  podataka sada se izvršava svaki put umesto da se preskače pri pogotku keša.
- Dvofaktorska autentifikacija: aplikacija za autentifikaciju može da se
  registruje uz kodove putem e-pošte, a uklanjanje poslednjeg pristupnog
  ključa ili ponovno generisanje rezervnih kodova prvo zahteva svež drugi
  faktor.
- Važeći ID pod-organizacije više se ne odbija sa „Organization not found", a
  API ključ kreiran u pod-organizaciji razrešava svog tehničkog korisnika iz
  te pod-organizacije.
- Uređivanje organizacije proverava ID partnera i više ne resetuje tip
  organizacije kao propratni efekat.
- „Preostali tokeni" u prikazu pretplate vezani su za ugovornu godinu, a ne za
  kalendarsku.

## Auth Bridge Service — `0.5.7`

- Replikacija naloga između EU i US regiona oporavlja se sama. Prekinuti tok
  replikacije ponovo se prikači na licu mesta, replikacija nastavlja da teče
  dok se izvršava usklađivanje, a memorija usklađivanja je ograničena, pa
  servis više ne upada u petlju rušenja na velikim tabelama.

## Barcode Service — `1.18.7`

- Čitanje barkodova izvršava se pod vremenskim ograničenjem i prijavljuje
  istek vremena umesto da visi, što je ranije ostavljalo dokument zaglavljen u
  obradi.

## Docflow Service — `2.9.8`

- Vrednosti polja koje upiše kartica radnog toka dospevaju na dokument u obe
  sačuvane reprezentacije, pa ih kasniji izvoz više ne poništava.
- Ponovljeni okidač zadržava rad koji je pokretanje već obavilo, sukobljeni
  okidači nad istim dokumentom staju u red umesto da otimaju zaključavanje, a
  eskalirani ponovni pokušaj rangira se prvi u redu.
- Kartice za poređenje porudžbenica: tolerancije se porede kao tačne decimalne
  vrednosti i zasnovane su na vrednosti porudžbenice, obrnuti smerovi
  poređenja dostupni su kao opcije, dodeljena grupa se prijavljuje kao grupa
  umesto da obori poređenje po ID-ju korisnika, ID-jevi dodele porede se
  ispravno kao UUID-jevi, stavke sa praznim numeričkim vrednostima se
  preskaču, a poređenje „received" bez ikakvih podataka o prijemu prijavljuje
  nedostajuće podatke umesto da se pravi da se podudara.
- Kartica Apply Decision Table je povučena.

## Email Service — `1.41.0`

- Gmail uvozi preuzimaju svaki prilog tačno jednom; duplikati iz preklapajućih
  preuzimanja su nestali.
- Kursor čitanja uvoza pomera se tek nakon što je uvoz potvrđen, pa pad usred
  uvoza više ne može da preskoči e-poruke.
- Kada se konfiguracija uvoza deaktivira jer postoji slična, ta deaktivacija
  je vidljiva i praćena obaveštenjem umesto tiha.

## Extraction Service — `1.54.5`

- Da li je dokument knjižno odobrenje ili faktura razrešava se prema tome koja
  je ključna reč bliža pominjanju tipa dokumenta, umesto da pobedi prvo
  podudaranje.
- Kada je više poreskih interpretacija unutar tolerancije, tačno usklađivanje
  ima prednost nad približnim.
- Nakon prinudnog ponovnog OCR-a vraćaju se tip dokumenta i lokalitet, pa
  ekstrakcija tabela i treniranje ponovo rade na ponovo OCR-ovanim
  dokumentima.
- Dokumenti bez tipa dokumenta više ne obaraju pretragu pravila za tabele.

## FTP Service — `1.32.8`

- Skeniranje foldera obavlja jedan krug listanja po folderu sa ograničenom
  dubinom, pa su uvozi iz velikih FTP direktorijuma znatno brži i prestaju da
  probijaju vremenska ograničenja.

## Fulltext Service — `1.42.3`

- Dokumenti čiji sačuvani sadržaj za pretragu nije imao ekstrahovana polja
  ponovo se indeksiraju iz baze podataka, pa se opet pojavljuju u pretrazi
  kontrolne table.
- Prozor pretrage kontrolne table podržava do 10.000 dokumenata.
- Fasetne pretrage više ne padaju kada je semantička pretraga aktivna.

## OCR Service — `1.10.7`

- Vremenski budžet OCR-a dimenzioniše se prema stvarnom trošku po stranici, pa
  se dugački dokumenti završavaju umesto da udare u ograničenje toka obrade.

## PO Match Service — `1.59.8`

- Stavke tabele sa nultom količinom preskaču se u proverama neusklađenosti
  umesto da proizvode lažne neusklađenosti.
- Kada nedostaju obavezne kolone za PO uparivanje, rezultat ih imenuje.
