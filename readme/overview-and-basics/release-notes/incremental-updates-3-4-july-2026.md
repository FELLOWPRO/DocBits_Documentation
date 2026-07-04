# DocBits beleške o izdanju — 3–4. jul 2026.

_Šta je donela ova produkcijska nadogradnja, jednostavnim jezikom. Uz svaki servis
prikazana je verzija koja je sada aktivna u produkciji. Servisi koji nisu navedeni
nisu imali izmene vidljive korisnicima u ovom periodu._

---

## Najvažnije

- **Čistije primene u celoj floti.** Nekoliko ključnih servisa (API, Auto
  Accounting, Docflow, Extraction, OCR, PO Match) sada se ispravno gase tokom
  primene, tako da postepena primena (rolling deploy) više ne rizikuje da
  prekine zahtev koji je već bio u obradi.
- **Poboljšanja izvoza e-faktura.** Izvoz dokumenta u više izvoznih
  konfiguracija odjednom sada je pouzdaniji — provere duplog izvoza sada se
  izvršavaju jednom po grupi (batch) umesto po svakoj stavci, a nova izvozna
  krajnja tačka sprečava treperenje statusa izvoza kada se pokrene više
  izvoza istovremeno. XRechnung/ZUGFeRD dokumenti takođe dobijaju doslednije
  mapiranje polja.
- **Stabilnija obrada dokumenata.** Ispravljen pad koji je mogao da obori ceo
  OCR dokument kada bi jedna stranica imala grešku, ispravljena sinhronizacija
  isporuka za porudžbenice (Purchase Order) koja je preuzimala samo prvih 100
  zapisa, i ojačano je nekoliko servisa protiv kratkotrajnih prekida veze sa
  bazom podataka.
- **Ispravljeni prilozi e-pošte.** Ispravljen slučaj u kojem su prilozi
  e-pošte mogli da stignu oštećeni ili sa nedostajućim bajtovima tokom uvoza
  dolazne pošte.
- **Pouzdanost radnih tokova.** Ispravljeno zaglavljivanje radnih tokova
  usled brave (lock) koja se nije ispravno oslobađala, i ispravljena logika
  ponovnog zakazivanja tako da preskočeni koraci radnog toka budu ispravno
  obrađeni i zabeleženi.
- **Novo: Ideas Service.** Novi pozadinski servis (Ideas, v0.3.0) pridružio se
  produkcijskoj floti.

---

## API Service — u produkciji: `12.52.4`

- **Pouzdanost OCR-a:** pad na jednoj stranici više ne obara ceo dokument.
- **Izvoz:** provere duplog izvoza sada se izvršavaju jednom po grupi (batch)
  umesto jednom po stavci; nova izvozna krajnja tačka sprečava treperenje
  statusa izvoza kada se više izvoza izvršava istovremeno; XRechnung/ZUGFeRD
  dokumenti dobijaju doslednije kanoničko mapiranje polja.
- **Porudžbenice (Purchase Orders):** ispravljena sinhronizacija isporuka
  koja je preuzimala samo prvih 100 zapisa po porudžbini.
- **Dnevnici aktivnosti (Activity Logs):** ispravljeno dugme „Sledeća"
  stranica koje je skakalo na nepovezani vremenski period.
- **Pretraga matičnih podataka (Master Data Lookup):** ispravljena
  serverska greška (HTTP 500).
- **Indeksiranje pretrage:** dodata potvrda isporuke i ponovni pokušaj tako
  da dokumenti pouzdano budu postavljeni u red za pretragu celog teksta.
- Opšte ispravke stabilnosti kojima je rešeno nekoliko učestalih pozadinskih
  grešaka.

## Auth Service — u produkciji: `1.68.7`

- Samo interna pouzdanost i održavanje u ovom periodu.

## Auto Accounting — u produkciji: `1.18.8`

- **Čistije gašenje** tokom primena, čime se izbegava prekid zahteva koji su
  već u obradi.

## Barcode Service — u produkciji: `1.15.8`

- Samo interna ispravka konfiguracije primene u ovom periodu.

## Docflow Service — u produkciji: `2.5.3`

- **Nova opcija izvoza** za slanje dokumenta u više izvoznih konfiguracija
  odjednom.
- **Ispravljeno zaglavljivanje radnih tokova** usled brave (lock) koja se
  nije ispravno oslobađala bez obzira na status.
- **Ispravljeno ponovno zakazivanje radnog toka** tako da preskočeni koraci
  budu ispravno obrađeni i zabeleženi umesto da tiho budu odbačeni.
- **Brže pokretanje:** baze podataka se sada unapred „zagrevaju" u pozadini.
- Veća otpornost na kratkotrajne prekide veze sa bazom podataka.
- Poboljšano parsiranje polja datuma za kartice radnog toka.

## Email Service — u produkciji: `1.37.9`

- **Ispravljeni dolazni prilozi** koji su mogli da stignu oštećeni ili sa
  nedostajućim bajtovima.
- **Jasnije greške** kada fascikla poštanskog sandučeta ne može da se
  preuzme, umesto opšteg neuspeha.

## Extraction Service — u produkciji: `1.49.6`

- **Ispravljeni padovi** na dokumentima sa neprepoznatim tipom dokumenta i
  na tabelama neuobičajenog/neispravnog oblika.
- Veća otpornost na kratkotrajne prekide veze sa bazom podataka usred upita.

## FTP Service — u produkciji: `1.30.3`

- Samo interna nadogradnja radnog okvira (framework) u ovom periodu.

## Fulltext Service — u produkciji: `1.36.3`

- **Indeksiranje pretrage:** periodično čišćenje sada popravlja sve
  dokumente koji nisu uspeli da dospeju u indeks pretrage za bilo koju
  organizaciju.
- **ERP sinhronizacija:** ispravljena zaglavljena brava (lock) koja je
  mogla da blokira ERP sinhronizaciju nakon neuspelog ponovnog pokušaja.

## OCR Service — u produkciji: `1.7.8`

- **Ispravljena OCR autentifikacija** tako da API ključevi organizacije
  ponovo ispravno rade.
- Čistije gašenje tokom primena.

## Operator Service — u produkciji: `1.39.7`

- Samo interne ispravke pouzdanosti primene u ovom periodu.

## PO Match Service — u produkciji: `1.56.0`

- **Ispravljen pad** prilikom sortiranja PO Match količina koje su
  uključivale prazne vrednosti.
- Čistije gašenje tokom primena.

## Web App — u produkciji: `10.36.9`

- **Ispravljena greška** prilikom povratka na Field Validation sa drugog
  ekrana.
- **Ispravljeno dugme „Scripts"** koje je usmeravalo na 404 stranicu.
- **Dnevnici aktivnosti (Activity Logs):** ispravljen netačan prikaz
  „Stranica 2 od 1" i ispravljen filter za nivo ozbiljnosti WARN koji nije
  prikazivao nijedan rezultat.

---

## Nema izmena vidljivih korisnicima u ovom periodu

Auth Service, Barcode Service, FTP Service, Operator Service i Docnet
Service (`1.54.6`, nepromenjeno) dobili su samo interno održavanje ili
održavanje konfiguracije primene.

<!-- Generated by the docbits-changelog skill (version-boundary mode: exact
     git ranges between the ALT and NEU version-bump commits supplied by the
     user, per service). Window ~2026-07-01 → 2026-07-04. -->
