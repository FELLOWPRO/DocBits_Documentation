# DocBits beleške o izdanju — 29. jul – 12. avgust 2026.

_Šta se promenilo u DocBits produkcijskoj nadogradnji uvedenoj 10–12. avgusta
2026, koja obuhvata sve od izdanja 29. jula. Svaki servis navodi verziju koja
je puštena u rad, a zatim novine i ispravke objašnjene jednostavnim jezikom.
Servisi koji nisu navedeni (Auto Accounting `1.21.1`, Ideas `0.3.1`, OCR
`1.10.3`, Operator `1.42.1`, PO Match `1.59.3`, FTP `1.32.4`) nisu imali
izmene vidljive korisnicima._

---

## Najvažnije

- **Podrška za FacturaE.** Španske FacturaE 3.1 e-fakture klasifikuju se i
  ekstrahuju odmah, bez podešavanja, sa potpunim mapiranjima polja. U istom
  talasu, mapiranja za ebInterface (Austrija) postala su verna verzijama,
  podrazumevana podešavanja za Factur-X i ZUGFeRD dobila su putanju za naziv
  kompanije, a ispravljeno je nekoliko pogrešnih podrazumevanih mapiranja za
  popuste, PDV i jedinične cene.
- **Popravljeni pretraga i sortiranje kontrolne table.** Sortiranje više ne
  zavisi od toga koje su kolone trenutno vidljive, OR filter kombinovan sa
  opsegom ili jednakošću više ne briše fraze pretrage, imena dobavljača
  ponovo se prikazuju u brzoj pretrazi, a datumi u ISO formatu čitaju se
  ispravno.
- **AI ekstrakcija se sama ispravlja.** Dokaziva zamena neto i ukupnog iznosa
  koju napravi AI automatski se poništava, polja skenirana AI-jem više se ne
  vraćaju pogrešna nakon restarta dokumenta, a AI ekstrakcija tabela obrađuje
  dokumente u serijama stranica, pa dugačke tabele stižu kompletne.
- **Radni tokovi preživljavaju zastoj autentifikacije.** Kratkotrajno
  nedostupan auth servis ponovo se pokušava umesto da obori pokretanje, a
  okidač radnog toka koji ne može da se autentifikuje prijavljuje grešku
  umesto da ostavi dokument zaglavljen.
- **Teško čitljivi PDF-ovi ponovo se ekstrahuju.** Kada standardni dekoder
  PDF teksta ne može da pročita stranicu (često kod datoteka proizvedenih
  Ghostscript-om), ekstrakcija prelazi na drugi mehanizam umesto da ne vrati
  ništa.
- **MFA radi preko regiona.** Podaci o registraciji dvofaktorske
  autentifikacije repliciraju se između EU i US regiona, pa se drugi faktor
  podešen u jednom regionu poštuje i u drugom.

---

## Web App — `10.49.4`

### Prijava i nalozi

- Odjava u jednoj kartici pregledača odjavljuje i ostale kartice, bez
  iskačućih poruka o grešci koje su se ranije pojavljivale kada se kartice ne
  slože oko sesije.
- Promena sopstvene lozinke u profilu ide kroz namensku samouslužnu krajnju
  tačku, pa radi bez administratorskih dozvola.
- Prijava pristupnim ključem iz regiona koji nije matični prikazuje prevedene
  poruke o grešci, a njeno dugme za potvrdu je vidljivo.

### Ekran validacije

- Kartica „Extracted table" više se ne vrti beskonačno kada AI tabela već
  postoji.
- Dokumenti kojima nedostaju podaci o barkodu više ne obaraju prikaz dodele
  barkodova.
- M3 stavke sa više poreza nude poresku šifru kao padajuću listu punjenu iz
  liste vrednosti umesto polja za slobodan unos.
- Otvaranje velikih faktura dobavljača je primetno brže.

### Zadaci

- Kanban kolone učitavaju se stranicu po stranicu dok skrolujete, pa se table
  sa mnogo zadataka brzo učitavaju.
- Brojač otvorenih zadataka u bočnoj traci broji zadatke u kontekstu vaše
  pod-organizacije, a ne u kontekstu dokumenta koji je slučajno otvoren.

### Workflow Builder

- Lista radnih tokova zadržava vašu pretragu, redosled sortiranja, stranicu i
  veličinu stranice kada otvorite radni tok i vratite se, uključujući i
  povratak preko putanje (breadcrumb), a stranica se podrazumevano otvara na
  kartici List.

### Podešavanja i administracija

- Stranica matičnih podataka više se ne pojavljuje prazna zbog trke pri
  sortiranju, a sortiranje po bedževima više ne ruši stranicu.
- Pretplata u statusu „otkazivanje u toku" može da se nastavi.
- Stranica sa detaljima XSLT-a prijavljuje greške pri učitavanju umesto da ne
  prikaže ništa, a podešavanja obaveštenja e-poštom koriste punu širinu
  stranice sa funkcionalnim panelom dnevnika.
- Birač organizacija za korisnike sa više organizacija ima ispravan raspored
  redova, veličine i boje teme, pravilno se skroluje i nudi filter za naloge
  sa mnogo organizacija.
- Analitika: neuspeo zahtev za metrike prikazuje stanje greške umesto da
  iscrtava nule, a vidžeti korišćenja pošteno prijavljuju kada nema izmerenih
  podataka.
- Zastarele opcije keša uklonjene su sa stranice za upravljanje kešom, a
  stranice Korisnici i Grupe rešene su ugnežđenih duplih traka za skrolovanje.
- „Use Default Template" u upravljaču izgleda više se ne ruši niti stoji bez
  reakcije; takođe više ne tvrdi da podrazumevani izgled ne postoji.
- Pravila izbora zadržavaju svoje operatore podudaranja teksta, prisustva i
  regularnih izraza kada se pravilo ponovo otvori.
- Tipovi dokumenata podržavaju pravila transformacije po tipu, a interfejs
  liste pravila dobio je akciju za fiksnu vrednost.
- Bedževi statusa porudžbenica ispravno se mapiraju za statusne vrednosti u
  ERP zapisu velikih i malih slova.
- Ekrani DocNet-a (AI Workforce), uključujući Agent Wizard, su prevedeni, a
  dijalog za novu ideju odnosno izmenu ideje skroluje horizontalno.
- Ponude na portalu dobavljača: upravljane jedinice mere prikazuju se u tabeli
  stavki, stil odobravanja primenjuje se samo na ponude po ugovoru, a linija
  poređenja više se ne pojavljuje kada su obe vrednosti identične.
- JSON rezervni prikaz stranice o grešci čitljiv je u tamnom režimu, a
  izveštaji koriste ispravnu oznaku „poslednjih 7 dana" umesto zalutalog „7".

## API Service — `12.74.0`

### Kontrolna tabla i pretraga

- Sortiranje radi bez obzira na to koje su kolone vidljive, a ključna reč koju
  pretraga delegira pretrazi celog teksta više ne ostavlja za sobom pokvaren
  SQL fragment.
- Imena dobavljača ponovo se pojavljuju u brzoj pretrazi za organizacije bez
  indeksiranja celog teksta.
- Datumi u ISO formatu (2026-08-12) više se ne čitaju pogrešno u normalizatoru
  datuma koji prvo očekuje dan.
- Izvozi kontrolne table usmeravaju gole tekstualne vrednosti, kao što su
  brojevi faktura, u ispravnu kolonu.

### E-fakture

- FacturaE 3.1 (Španija): pravilo klasifikacije i kompletna mapiranja polja.
- Pravila klasifikacije XRechnung-a usidrena su za svoju sintaksnu porodicu,
  pa UBL dokument više ne odgovara CII pravilima i obrnuto.
- Prihvaćena verzija „3.0" pokriva celu svoju patch porodicu (3.0.1, 3.0.2).
- CII fakture uzimaju pravno ime dobavljača, koristeći trgovačko ime samo kao
  rezervu.
- Mapiranja za ebInterface (Austrija) verna su verzijama, sa ispravljenim
  opštim (catch-all) mapiranjem i iznova izgrađenim test primerima.
- Podrazumevana podešavanja za Factur-X i ZUGFeRD dobila su putanju
  ekstrakcije naziva kompanije, a ispravljene su podrazumevane transformacije
  zaglavlja za poresku stopu, tip fakture i polja trećeg nivoa, zajedno sa
  semantikom popusta, PDV-a i jediničnih cena za celu porodicu formata.
- Šifre poreskih kategorija iz izvora više se ne mapiraju naslepo na vaše ERP
  šifre.
- Dokumenti koji pominju i „fakturu" i „knjižno odobrenje" daju prednost
  klasifikaciji knjižnog odobrenja.

### Dokumenti i ekstrakcija

- Kada standardni PDF dekoder ne može da pročita ugrađeni tekst stranice,
  ekstrakcija prelazi na drugi mehanizam, pa se pogođeni PDF-ovi ekstrahuju
  umesto da se vrate prazni.
- Glavni prekidač za barkodove sada je `BARCODE_EXTRACTION`; staro podešavanje
  za QR kodove nastavlja da radi kao alijas.
- Zapušeno je curenje memorije u pozadinskom planeru; ono je tokom više dana
  rada polako degradiralo obradu.
- Dobavljači uvezeni bez zemlje ostaju prazni umesto da podrazumevano dobiju
  Nemačku.

### Izvoz i matični podaci

- Save Rules prijavljuje neuspeh kada ništa ne upiše, umesto da tvrdi uspeh.
- Stavke sa nultim iznosom više se ne ispuštaju iz izvoza automatskog
  knjiženja, a ispravljen je filter koji je odgovarao svakoj grupi.
- M3 izvozi podržavaju post-hook-ove za dodatne informacije.
- Jedna neuspela proba skupa podataka više ne prazni ceo ekran matičnih
  podataka.
- PO keševi se poništavaju kada ERP ažurira status porudžbenice, pa kontrolna
  tabla prestaje da prikazuje zastarelo stanje.

### Administracija

- Svaka preferenca prikazuje koji ju je korisnik poslednji izmenio.
- Pravila ekstrakcije mogu da se brišu po dobavljaču i kloniraju putem novih
  krajnjih tačaka.
- Primaoci e-poruka statusnih upozorenja porede se bezbedno u odnosu na NULL,
  čime je ispravljen pad u isporuci obaveštenja.

## Auth Service — `1.75.9`

- API ključ organizacije upotrebljen prema nepovezanoj organizaciji se odbija.
- Kreiranje organizacije vraćalo je grešku iako je red zapravo sačuvan; sada
  odgovara ispravno.
- Prijava pristupnim ključem kada nijedan nije registrovan vraća sopstveni kod
  greške, pa ekran za prijavu može da saopšti šta nije u redu.

## Auth Bridge Service — `0.4.2`

- Tabele registracije dvofaktorske autentifikacije repliciraju se između EU i
  US regiona, a redovi se identifikuju svojim stvarnim primarnim ključem.

## Docflow Service — `2.8.7`

- Okidač radnog toka koji ne može da se autentifikuje prijavljuje neuspeh
  umesto da ostavi dokument zaglavljen, a kratkotrajno nedostupan auth servis
  ponovo se pokušava umesto da se tretira kao loš token.
- Kartice za poređenje ponuda: brojevi artikala porede se samo za stavke koje
  matrica cena artikala opisuje, a stavke bez jedinice mere ili bez cene se
  preskaču umesto da obore poređenje.
- Kartica poređenja ugovorenih cena dobila je opciju operatora bilo koji/svi
  (any/all), a keševi kartica ispravno se poništavaju nakon migracija i
  ažuriranja koda.
- Prekinute SSL veze tretiraju se kao prolazne i ponovo se pokušavaju umesto
  da obore pokretanje.

## Docnet Service — `1.56.4`

- Krajnje tačke za zdravlje i verziju više ne blokiraju na živim proverama,
  zbog čega je dijalog Service Versions ranije umeo da visi.

## Email Service — `1.40.6`

- Kada se dolazna e-poruka preskoči, razlog se prikazuje u redu događaja uvoza
  umesto da ostane tih.
- Priložene `.eml` kontejnerske datoteke više se ne uvoze kao dokumenti.
- Neuspela Microsoft Office prijava proizvodi čitljivu poruku o grešci, a
  transportna greška iz AI servisa računa se kao „nejasno", a ne kao
  odbijanje.

## Extraction Service — `1.53.8`

- Dokaziva zamena neto i ukupnog iznosa koju napravi AI poništava se nakon
  ekstrakcije polja, a neuspesi zaštitnih provera beleže se umesto da prođu
  tiho.
- Polja skenirana AI-jem više se ne vraćaju pogrešna nakon restarta dokumenta.
- AI ekstrakcija tabela radi u serijama po stranicama i akumulira sve serije,
  pa dugačke tabele stižu kompletne.
- Dokumenti koji pominju i „fakturu" i „knjižno odobrenje" daju prednost
  klasifikaciji knjižnog odobrenja.
- Ponavljano čišćenje zaglavlja i podnožja se kešira, što ubrzava ekstrakciju
  na višestraničnim dokumentima.

## Fulltext Service — `1.41.7`

- OR filter kombinovan sa uslovom opsega ili jednakosti više ne briše fraze
  pretrage.
- Sortiranje koristi ispravne putanje indeksa i iznosi na videlo stvarni
  razlog kada pozadinski sistem pretrage odbije upit; regresija sortiranja
  koja je potpuno pokvarila pretragu sirovim upitima ispravljena je iste
  nedelje kada se pojavila.
- Pretrage dokumenata rade i na starijim indeksima sa tekstualnim mapiranjem.
- Keš tokena ograničen je na par token–organizacija, pa promena organizacije
  ne može da posluži rezultate pod prethodnim kontekstom.
