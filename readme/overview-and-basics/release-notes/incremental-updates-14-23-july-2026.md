# DocBits beleške o izdanju — 14–23. jul 2026.

_Šta se promenilo u DocBits produkcijskoj nadogradnji 23. jula 2026.
(ažuriranje Nova kanala), koja obuhvata sve od izdanja 14. jula. Svaki servis
navodi verziju koja je sada u produkciji, a zatim novine i ispravke objašnjene
jednostavnim jezikom. Servisi koji nisu navedeni nisu imali izmene vidljive
korisnicima._

---

## Najvažnije

- **Tiketi podrške sa ekrana greške.** Kada nešto pođe naopako, tiket podrške
  sada možete otvoriti direktno iz zapisa o grešci. Tiket već sadrži tehnički
  kontekst, pa ne morate da ga opisujete.
- **Dolazna e-pošta u ispravnom regionu.** Američke organizacije dobijaju
  adrese za dolazni uvoz u sopstvenom regionu, a Microsoft 365 poštanski
  sandučići na nacionalnim cloud tenantima (GCC, 21Vianet i slični) sada mogu
  da se konfigurišu izborom Cloud Instance.
- **Jasniji status PO uparivanja.** Fakture čija tabela stavki nije mogla da
  se mapira ranije su dobijale oznaku „porudžbenica nije pronađena", što je
  ljude slalo da traže pogrešan problem. Sada dobijaju sopstveni status
  „tabela nepotpuna" sa detaljima po kolonama o tome šta se nije mapiralo.
- **Mapiranje poreskih kodova za e-dokumente.** Nova stranica podešavanja
  mapira vaše ERP poreske kodove za elektronske dokumente, a izvozi proveravaju
  mapiranje unapred umesto da otkažu tek u ERP-u.
- **Izmene skriptova zaštićene su lozinkom.** Prilagođeni skriptovi mogu da
  promene način obrade dokumenata, pa svaka izmena skripta sada zahteva
  lozinku koja se menja svakog sata. Aktuelnu lozinku zatražite od svog
  administratora.
- **Turbo AI nivo je povučen.** Turbo model je došao do kraja životnog veka.
  Svi koji su ga imali izabranog automatski su prebačeni na Fast; nikakva
  akcija nije potrebna.

---

## Web App — u produkciji: `10.45.1`

### Rad sa dokumentima

- **Obrisani dokumenti:** otvaranje dokumenta koji je u međuvremenu obrisan
  prikazuje razumljivu poruku umesto grešaka skripta.
- **Field Validation:** polje za unos broja stranice je šire i prelazi na
  stranicu pritiskom na Enter. Polje koje je skript učinio dostupnim samo za
  čitanje i dalje prikazuje svoju vezu polja.
- **Ekstrakcija tabela:** brisanje kolone oslobađa njen naziv za ponovnu
  upotrebu, a obrisana zaglavlja se više ne vraćaju u sačuvanu tabelu.
- **Odobrenja:** korisnici više ne mogu da odobre Sales Tax korak za koji
  njihova grupa nema dozvolu, a istorija odobrenja ponovo prikazuje sve
  zapise. Istorija takođe imenuje osobu koja je zaista odobrila, uključujući
  odobrenja koja je administrator dao u ime zaduženog korisnika.
- **Dobavljači:** stranica Accounting više ne prikazuje lažno upozorenje
  „Supplier is missing", a brisanje dobavljača koji postoji samo iz
  ekstrakcije više ne ostavlja dijalog zaglavljen.
- **Zadaci i obaveštenja:** opcija brisanja je sakrivena za korisnike bez
  administratorskih prava.

### Kontrolna tabla i pretraga

- **Izvoz:** izvozi koriste kontrolnu tablu koju imate izabranu, a aplikacija
  vas upozorava pre izvoza kontrolne table sa nesačuvanim izmenama.
- **Pretraga:** Invoice Type je dostupan kao polje pretrage sa svojom listom
  vrednosti.
- **Dnevnik uvoza:** podeljeni dokumenti mogu da se pronađu preko matičnog
  dokumenta, a kolona Failed Filenames navodi samo datoteke koje zaista nisu
  uspele ili su preskočene.

### Prijava

- **Obrisani nalozi:** prijava sa obrisanim nalogom sada to jasno saopštava,
  umesto da ne uspe uz generičku grešku.
- **SSO:** ispravljena greška pri prijavi dok je izabran drugi region.

### Podešavanja i administracija

- **Tiketi podrške:** kreirajte tiket direktno iz zapisa o grešci. Tiketi
  nose okruženje i kanal izdanja, a snimanje ekrana se više ne zaglavljuje.
- **Workflow Builder:** novokreirane ili preimenovane kartice, šabloni
  e-pošte i druge stavke padajućih lista pojavljuju se odmah, bez ponovnog
  učitavanja stranice.
- **Document Types:** novo podešavanje Structured Extraction u odeljku
  ekstrakcije.
- **E-Doc poreski kodovi:** nova stranica podešavanja za mapiranje vaših ERP
  poreskih kodova za elektronske dokumente (vidi Najvažnije).
- **Izbor AI modela:** povučeni Turbo nivo je uklonjen iz padajuće liste;
  postojeći izbori prikazuju Fast.
- **Dijalog Service Versions:** sada može da se skroluje, uključuje Auth
  Bridge servis i prikazuje nazive kanala izdanja Vesta i Nova.
- **Stranica za uvoz:** više se ne ruši za organizacije sa praznim zapisom
  pretplate.

### Manje ispravke

Prazna toast obaveštenja se potiskuju, dijalog za novu ideju ili izmenu ideje
se skroluje, pomereni checkbox-ovi u podešavanjima polja ponovo su poravnati,
blokirana brisanja dokumenata objašnjavaju razlog, a podešavanja E-Document
uredno obrađuju prelazak sa Default na Custom.

## API Service — u produkciji: `12.64.3`

- **Bezbednost skriptova:** izmene skriptova zahtevaju vremenski zasnovanu
  lozinku (vidi Najvažnije).
- **E-Doc poreski kodovi:** mapiranje ERP poreskih kodova za elektronske
  dokumente, uz centralnu proveru pre izvoza tako da nedostajući kodovi
  isplivaju na vreme.
- **Kontrola pristupa:** administratori mogu korisnicima bez administratorskih
  prava da odobre uvid u neklasifikovane dokumente.
- **Lične kontrolne table:** ispravljena podešavanja deljenja koja nisu htela
  da se sačuvaju.
- **Pretraga na kontrolnoj tabli:** Invoice Type se pridružuje proširenim
  poljima pretrage, a dokumenti nastali podelom po barkodu ili QR kodu
  pronalaze se preko matičnog dokumenta.
- **Otpremanja:** ponovljena otpremanja iste datoteke tokom mrežnog ponovnog
  pokušaja više ne kreiraju duple dokumente.
- **Pretraga dobavljača:** rezultati stižu čim su podaci spremni umesto posle
  fiksnog čekanja.
- **Infor izvoz:** jedinične cene zadržavaju četiri decimale. M3 izvozi mogu
  da uključe stavke troškova sa nultim iznosom, a negativne LN stavke
  troškova šalju se kao pozitivna knjižna odobrenja.
- **Odobrenja:** odobrenje se povezuje sa zahtevom za odobrenje samo kada je
  odobravalac njegov zaduženi korisnik.
- **Stabilnost prijave:** privremeni otkaz unutar provere tokena više ne
  odjavljuje korisnike; aplikacija umesto toga ponavlja pokušaj.
- **Klasifikacija:** pravila izvora sada porede sa svakim poljem izvora
  dokumenta, a ne sa fiksnim pozicijama.
- **Stabilnost validacije:** polje bez naziva više ne ruši validaciju
  dokumenta.
- **AI modeli:** Turbo nivo (povučen) svuda je preusmeren na Fast,
  uključujući fino podešene varijante, uz zaštitu koja sprečava da se povučen
  model ikada pokrene.

## Auth Service — u produkciji: `1.72.8`

- **Istorija prijava:** prijave putem SSO/SAML sada se pojavljuju u istoriji
  prijava, a vremenska oznaka poslednje prijave pouzdano se beleži za svaki
  tip prijave. Pregled istorije prijava drugog korisnika zahteva odgovarajući
  administratorski nivo.
- **Nasleđeni nalozi:** brisanje nasleđenog korisničkog naloga ponovo radi
  umesto da tiho ne uradi ništa.
- **Masovna administracija korisnika:** dodajte postojeće korisnike u
  podorganizacije i grupe masovno putem CSV-a, upareno po adresi e-pošte.
  Ispravljeni su i pad na neravnomerno popunjenim CSV redovima i greška
  servera pri dodavanju dva ili više novih korisnika odjednom.
- **Liste članova:** obrisani korisnici se više ne pojavljuju u listama
  članova podorganizacija.
- **Jedinstvena prijava (SSO):** serija ispravki za dodatnu robusnost.
  Istekli tokeni sada vraćaju čist odgovor „isteklo", organizacije bez SAML
  konfiguracije dobijaju ispravan odgovor „nije pronađeno" umesto pogrešnog
  toka prijave, odjava se uvek dovršava čak i kada zahtev za odjavu ne može
  da se verifikuje, a nestalo je i nekoliko padova vezanih za nedostajuću
  konfiguraciju provajdera identiteta.
- **Sesijski tokeni:** ispravljeno odbijanje kratkotrajnih sesijskih tokena
  kao nevažećih iako nisu bili istekli.
- **Alati za upravljanje:** region organizacije je vidljiv u API-ju za
  upravljanje, sistemski korisnik organizacije može ponovo da se dodeli, a
  administracija planova i potrošnje dobila je namenske krajnje tačke. Ove
  izmene se tiču internih alata DocBits osoblja, a ne aplikacije za klijente.

## Email Service — u produkciji: `1.39.9`

- **Uvoz u ispravnom regionu:** domeni dolazne e-pošte postoje po regionu, a
  poruke koje stignu u pogrešan region prosleđuju se u pravi. Američke
  organizacije više ne zavise od EU dolazne putanje.
- **Microsoft 365:** nacionalni cloud tenanti konfigurišu se izborom Cloud
  Instance, čime je ispravljen O365 uvoz za američke klijente. Nevažeći
  tenant sada daje jasnu grešku prijave umesto greške servera, a nepotpuni
  podaci tenanta odmah otkazuju uz poruku umesto da tiho ne uspeju.
- **Higijena sandučeta:** e-poruke bez priloga premeštaju se iz sandučeta
  umesto da se gomilaju.
- **Bez duplikata pri ponovnom pokušaju:** otpremanja ka API-ju za dokumente
  nose ključ idempotentnosti, pa ponovljena isporuka ne može dvaput da
  kreira isti dokument.
- **Imenovanje izvora:** O365 izvori sa konfigurisanom fasciklom uključuju
  adresu naloga u svom nazivu, pa se slični izvori mogu razlikovati.
- **Održavanje dnevnika uvoza:** zapisi dnevnika uvoza čuvaju se 90 dana, a
  nakon toga se automatski čiste.

## PO Match Service — u produkciji: `1.59.1`

- **Status „tabela nepotpuna":** fakture čija tabela stavki nije mogla da se
  mapira dobijaju sopstveni status umesto obmanjujućeg „porudžbenica nije
  pronađena" (vidi Najvažnije). Kontrolna tabla ga prikazuje ikonom
  neuparenog dokumenta.
- **Bolji detalji greške:** neuspesi mapiranja tabele imenuju konkretnu
  kolonu koja se nije mapirala.
- **Urednije ponašanje API-ja:** zahtevi za PO pravila koja ne postoje
  vraćaju ispravan odgovor „nije pronađeno", a oštećeni zapisi keša se
  odbacuju umesto da izazivaju ponovljene greške.
- **Uparivanje po ukupnom iznosu:** ispravljena greška u uparivanju sa
  ukupnim iznosom porudžbenice.

## Fulltext Service — u produkciji: `1.38.3`

- **Evropski formati brojeva:** iznosi zapisani sa decimalnim zarezom
  (`1.234,56`) normalizuju se pre indeksiranja, pa pretrage i filteri po
  iznosu rade nezavisno od formata broja.
- **ERP brojači:** ispravljena greška tokena koja je mogla da prekine tok
  brojanja uživo na kontrolnoj tabli.
- **Otpornost indeksiranja:** indeksiranje sada podnosi privremene zastoje
  baze podataka i auth servisa (automatski ponovni pokušaj, prelazak na
  primarnu bazu) i odbacuje neispravne poruke iz reda umesto da ih ponavlja
  u nedogled.

## OCR Service — u produkciji: `1.9.9`

- **Veliki dokumenti:** vremenski budžet za OCR skalira se sa veličinom
  dokumenta, pa veoma velike datoteke više ne otkazuju zbog isteka vremena.
- **Neobični znakovi:** sanitizer čisti znakove koje OCR mašina ne može da
  predstavi, čime su ispravljeni otkazi na dokumentima sa egzotičnim
  simbolima.
- **Manje prolaznih otkaza:** privremene greške veze ka skladištu automatski
  se ponavljaju.

## Extraction Service — u produkciji: `1.52.0`

- **Američke fakture sa nultim porezom:** ispravljen slučaj u kojem je
  ispravan par neto/porez odbacivan kada je iznos poreza nula.
- **Ekstrakcija tabela:** tabele ostaju izmenjive kada konfigurisano
  mapiranje očekuje više kolona nego što dokument sadrži, a ispravljen je i
  pad na neuobičajenim podacima redova.
- **AI modeli:** povlačenje Turbo nivoa, preneto iz API Service-a.

## Docflow Service — u produkciji: `2.7.2`

- **PO uparivanje u tokovima rada:** nedostajuće vrednosti za poređenje
  tretiraju se kao nedostajući podaci, a ne kao nepodudaranje.
- **Kartice potvrde porudžbine:** kupac i odgovorna osoba pouzdano se
  razrešavaju.
- **Troškovi prevoza:** kada nijedna strana nema troškove, slučaj rešava
  operator kartica umesto da se zaglavi.
- **Bezbednost:** API tokeni tokova rada proveravaju se u odnosu na
  organizaciju kojoj pripadaju.
- **Brže pokretanje:** provera aktivnih tokova rada se kešira, a pozadinski
  radnici se uredno ponovo pokreću umesto da za sobom ostavljaju zaglavljene
  procese.

## Barcode Service — u produkciji: `1.17.4`

- **Dugotrajne podele:** veza sa redom zadataka održava se tokom dugih
  barkod poslova, pa se podela velikih serija više ne zaglavljuje pred kraj.

## FTP Service — u produkciji: `1.31.2`

- **Održavanje dnevnika uvoza:** isto 90-dnevno čuvanje i automatsko
  čišćenje kao kod Email Service-a.

---

## Nepromenjeno u ovom izdanju

**Auth Bridge** (`0.3.6`), **Auto Accounting** (`1.20.1`), **Docnet**
(`1.55.1`), **Operator** (`1.40.2`) i **Ideas** (`0.3.1`) ne nose izmene u
ovom periodu.

<!-- Generated by the docbits-changelog skill (version-boundary mode), then
     reconciled on 23 Jul 2026 against the Nova versions actually deployed
     (Web App 10.45.1, API 12.64.3, Auth 1.72.8, Email 1.39.9, PO Match
     1.59.1, OCR 1.9.9, Docflow 2.7.2, FTP 1.31.2). Manage Layouts and
     Custom Validation Rules were removed from this page: DOCB-13719 gated
     both behind a beta query parameter, so they are not generally available
     in 10.45.1. -->
