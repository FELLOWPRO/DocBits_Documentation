# DocBits beleške o izdanju — 14–23. jul 2026.

_Šta se promenilo u DocBits produkcijskoj nadogradnji 23. jula 2026.
(ažuriranje Nova kanala), koja obuhvata sve od izdanja 14. jula. Svaki servis
navodi verziju koja je sada u produkciji, a zatim novine i ispravke objašnjene
jednostavnim jezikom. Servisi koji nisu navedeni nisu imali izmene vidljive
korisnicima._

---

## Najvažnije

- **Manage Layouts i pravila validacije stižu u aplikaciju.** Sistemi pravila
  uvedeni na serverskoj strani u prošlom izdanju sada imaju kompletan
  korisnički interfejs. Rasporedima dokumenata možete upravljati direktno,
  definisati sopstvena pravila validacije i prepustiti pravilima da izaberu
  pravi raspored umesto porekla dokumenta. Oba su isključena dok ne uključite
  **Custom Validation Rules** na tipu dokumenta, tako da se za vas ništa ne
  menja dok se sami ne opredelite.
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
- **Izmene skriptova zaštićene su lozinkom.** Prilagođeni skriptovi mogu da
  promene način obrade dokumenata, pa svaka izmena skripta sada zahteva
  lozinku koja se menja svakog sata. Aktuelnu lozinku zatražite od svog
  administratora.
- **Turbo AI nivo je povučen.** Turbo model je došao do kraja životnog veka.
  Svi koji su ga imali izabranog automatski su prebačeni na Fast; nikakva
  akcija nije potrebna.

---

## Web App — u produkciji: `10.44.4`

### Manage Layouts i pravila validacije

Sistemi pravila koji su u prošlom izdanju stigli na serversku stranu sada
imaju svoj korisnički interfejs, pod Settings → Document Types → Manage
Layouts.

Rasporedi su višekratno upotrebljivi rasporedi polja, više nevezani za to
odakle je dokument stigao. Pravila izbora odlučuju koji raspored dokument
dobija: procenjuju se po prioritetu, prvi pogodak pobeđuje, a podrazumevani
raspored služi kao rezerva.

<figure><img src="../../.gitbook/assets/manage-layouts-selection-rules-en.png" alt="Ekran Layouts &#x26; Selection Rules sa karticama rasporeda i novim prekidačem Selection rules"><figcaption><p>Layouts &#x26; Selection Rules: višekratno upotrebljivi rasporedi sa izborom zasnovanim na pravilima</p></figcaption></figure>

Pravila validacije omogućavaju vam da definišete sopstvene provere izvučenih
vrednosti i vidite neuspehe označene na dokumentu, uključujući i to koje se
pravilo aktiviralo. Katalog podrazumevanih sistemskih pravila isporučuje se
sa izdanjem; svako pravilo ostaje isključeno dok ga ne aktivirate. Funkciju
uključujete po tipu dokumenta pod Custom Validation Rules.

<figure><img src="../../.gitbook/assets/custom-validation-rules-en.png" alt="Ekran Custom Validation Rules sa listom podrazumevanih sistemskih pravila, ozbiljnošću i prekidačima statusa"><figcaption><p>Custom Validation Rules: podrazumevana sistemska pravila, aktiviraju se po tipu dokumenta</p></figcaption></figure>

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
  zapise.
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

## API Service — u produkciji: `12.61.8`

- **Pravila validacije, sazrela:** novi operatori uslova (contains, starts
  with, ends with), vrednosti iz izvora sa listom vrednosti, aktivacija po
  tipu dokumenta i revizijski trag koji pokazuje ko je kreirao ili izmenio
  svako pravilo. Dokumenti se automatski ponovo validiraju kada se pravila
  promene.
- **Pravila transformacije:** sada mogu da postave ili obrišu vrednosti na
  celom dokumentu, aktiviraju se po tipu dokumenta i nose isti revizijski
  trag.
- **Pravila izbora rasporeda:** aktivacija je premeštena na tip dokumenta, a
  šabloni rasporeda beleže ko ih je i kada izmenio.
- **Bezbednost skriptova:** izmene skriptova zahtevaju vremenski zasnovanu
  lozinku (vidi Najvažnije).
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
  da uključe stavke troškova sa nultim iznosom.
- **Odobrenja:** odobrenje se povezuje sa zahtevom za odobrenje samo kada je
  odobravalac njegov zaduženi korisnik.
- **Stabilnost prijave:** privremeni otkaz unutar provere tokena više ne
  odjavljuje korisnike; aplikacija umesto toga ponavlja pokušaj.
- **Klasifikacija:** pravila izvora sada porede sa svakim poljem izvora
  dokumenta, a ne sa fiksnim pozicijama.
- **AI modeli:** Turbo nivo (povučen) svuda je preusmeren na Fast,
  uključujući fino podešene varijante, uz zaštitu koja sprečava da se povučen
  model ikada pokrene.

## Auth Service — u produkciji: `1.72.5`

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

## Email Service — u produkciji: `1.39.8`

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

## PO Match Service — u produkciji: `1.58.6`

- **Status „tabela nepotpuna":** fakture čija tabela stavki nije mogla da se
  mapira dobijaju sopstveni status umesto obmanjujućeg „porudžbenica nije
  pronađena" (vidi Najvažnije). Kontrolna tabla ga prikazuje ikonom
  neuparenog dokumenta.
- **Bolji detalji greške:** neuspesi mapiranja tabele imenuju konkretnu
  kolonu koja se nije mapirala.
- **Urednije ponašanje API-ja:** zahtevi za PO pravila koja ne postoje
  vraćaju ispravan odgovor „nije pronađeno", a oštećeni zapisi keša se
  odbacuju umesto da izazivaju ponovljene greške.

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

## OCR Service — u produkciji: `1.9.8`

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

## Docflow Service — u produkciji: `2.6.5`

- **PO uparivanje u tokovima rada:** nedostajuće vrednosti za poređenje
  tretiraju se kao nedostajući podaci, a ne kao nepodudaranje.
- **Kartice potvrde porudžbine:** kupac i odgovorna osoba pouzdano se
  razrešavaju.
- **Troškovi prevoza:** kada nijedna strana nema troškove, slučaj rešava
  operator kartica umesto da se zaglavi.
- **Bezbednost:** API tokeni tokova rada proveravaju se u odnosu na
  organizaciju kojoj pripadaju.

## Barcode Service — u produkciji: `1.17.4`

- **Dugotrajne podele:** veza sa redom zadataka održava se tokom dugih
  barkod poslova, pa se podela velikih serija više ne zaglavljuje pred kraj.

---

## Nepromenjeno u ovom izdanju

**Auth Bridge** (`0.3.6`), **Auto Accounting** (`1.20.1`), **Docnet**
(`1.55.1`), **FTP** (`1.31.1`), **Operator** (`1.40.2`) i **Ideas**
(`0.3.1`) ne nose izmene u ovom periodu.

<!-- Generated by the docbits-changelog skill (version-boundary mode: exact git
     ranges between the LATEST (2026-07-09..15) and NOVA (2026-07-15..21)
     version-bump commits supplied by the user, per service). -->
