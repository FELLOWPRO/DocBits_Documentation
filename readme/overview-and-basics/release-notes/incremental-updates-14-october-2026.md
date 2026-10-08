# DocBits beleške o izdanju — 14. oktobar 2026.

_Šta se menja u DocBits produkcijskom hitnom popravku 14. oktobra 2026.
(izdanje R1.0.15), koji obuhvata sve od [hitnog popravka od 15. septembra](incremental-updates-15-september-2026.md).
Svaki servis navodi verziju koja se isporučuje, a zatim novine i ispravke
objašnjene jednostavnim jezikom. Servisi koji nisu navedeni nisu imali izmene
vidljive korisnicima._

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/release-notes/2026-10-14/rs.mp4" %}

---

## Najvažnije

- **Settings Assistant.** Traka za ćaskanje na svakoj stranici podešavanja
  odgovara na pitanja o podešavanju vaše organizacije, na vašem jeziku i na
  osnovu DocBits dokumentacije. Čita trenutno stanje vaših podešavanja i
  objašnjava ih (dozvole grupa, kanali uvoza, prekidači za narudžbenice,
  računovodstvo). Kada ga zamolite da nešto uključi ili isključi, prvo prikaže
  pregled, sačeka vašu potvrdu i nudi poništavanje. „Open setting" vodi
  direktno do podešavanja, čak i unutar skupljenog odeljka, i ističe ga.
  Administratori organizacije uključuju ili isključuju asistenta na stranici
  Company Information. Odgovara samo na DocBits pitanja i nikada ništa ne menja
  bez potvrde.
- **Novi AI nivoi.** Nivoi Fast i Full rade na novim modelima. Novi nivo Auto
  bira Fast ili Full za svaki dokument, a Nexus Flash se pridružuje nivou
  Nexus. Režim vizije (hybrid ili auto) odlučuje kada se slika stranice šalje
  uz zahtev. Sačuvana podešavanja AI modela sama prelaze na nove nivoe, a
  ekrani prikazuju samo nazive nivoa. „Use AI" je padajuća lista (Standard,
  Yes, No) sa pregledom onoga što će strukturirana ekstrakcija zatražiti.
- **Provera polja zaglavlja.** Ekran validacije ima dugme „Header field check"
  pored dugmeta Save. Njegov izveštaj navodi svako polje zaglavlja i odakle
  vrednost potiče (AI, pravilo, skripta ili matični podaci), u kompaktnoj
  tabeli sa filterom izvora, pretragom i sortiranjem, uz iste oznake polja kao
  na ekranu validacije. Iskačući prozor porekla prikazuje izvor svake vrednosti
  u jednoj traci.
- **Bezbednost prijave i organizacije.** MFA izazov može da se iskoristi samo
  jednom na svakoj putanji prijave, a za upis autentifikatora potreban je kôd iz
  e-pošte. Organizacije poseduju listu verifikovanih domena e-pošte; društvena
  prijava (na primer Microsoft) pridružuje korisnika organizaciji koja navodi
  taj domen i nikada sama ne kreira organizaciju, korisnika ili pretplatu. Samo
  administratori organizacije menjaju preference organizacije i pišu ili
  odobravaju pravila usklađivanja narudžbenica. Keširani odgovori više ne mogu
  da procure između organizacija.
- **Usklađivanje narudžbenica i troškovi.** Troškovi koje narudžbenica očekuje
  kao nulu dobijaju apsolutni prag, tolerancija troškova važi i za troškove
  koje narudžbenica ne budžetira, a jedno polje može da navede više elemenata
  troška čiji se iznosi dele srazmerno narudžbenici. Kolona usklađivanja može
  da nosi oznaku „allow mismatch". Kartice radnog toka porede troškove po
  listi, a ograničenje izvršavanja radnog toka raste sa 30 na 50.
- **Manje pogrešnih brojeva.** Iznosi se prikazuju u ličnom formatu svakog
  korisnika (uključujući Švajcarsku i Sloveniju), vrednosti samo sa datumom
  zadržavaju svoj kalendarski dan u svakoj vremenskoj zoni, američka jednačina
  ukupnog iznosa uzima u obzir dodatne iznose i fakture sa više poreza, a
  dokumenti sa zaglavljem od 0.00 više ne upadaju u pogrešan prolaz kandidata.

---

## Takođe ispravljeno u ovom izdanju

- Kontrolna tabla više ne ostaje prazna kada trka (race condition) postavi
  filter pod-organizacije na ID organizacije i tako isključi svaki dokument.
- Vrednosti dimenzija ponovo mogu da se biraju za svakog korisnika.
- Ispravljena je greška pri otpremanju koju je prijavio klijent.
- „Match on total" radi za dobavljače čija faktura ima samo jednu stavku, kao i
  za podešavanja dobavljača koja su to prijavila.
- SPS e-dokumenti: usklađeni su troškovi 810, ažuriran je raspored troškova
  855, a ispravljen je logotip klijenta u pregledu e-dokumenta.

---

## Web App — `10.78.9.4`

**Settings Assistant**
- Bočna fioka za ćaskanje sa prekidačem nalazi se na svim stranicama
  podešavanja. Razgovor se zadržava pri promeni stranice, ograničen je na 20
  poruka i prikazuje primenjene izmene sa mogućnošću poništavanja.
- Pozdravlja vas pitanjima koja odgovaraju trenutnoj stranici podešavanja i
  prikazuje kartice podešavanja sa prekidačem za uključivanje/isključivanje.
  Esc prvo zatvara menije, Stop prekida odgovor u toku, a snimci ekrana u
  odgovorima otvaraju se u lightbox-u.
- Primena izmene otvara dijalog sa pregledom, potvrdom i poništavanjem.
- Svako podešavanje može da se pretraži iz bočne trake, a pronađeno podešavanje
  ističe se drugom bojom. „Open setting" skroluje do cilja unutar skupljenog
  akordeona.
- Prekidač za asistenta namenjen administratoru organizacije nalazi se na
  stranici Company Information.
- AI saveti se pripisuju Nova-i, a prikazuju se samo nazivi nivoa, nikada ID-jevi
  modela.

**Ekran validacije i obrada dokumenata**
- Novo dugme „Header field check" sa izveštajem, poreklom po polju i stranicom
  pomoći (vidi Najvažnije). Oznake izvora i čipovi statusa ostaju unutar svojih
  ćelija.
- Tekstualne značke „from master data" pored oznaka polja su uklonjene;
  iskačući prozor porekla nosi tu informaciju.
- Jedna zajednička validacija polja radi svuda, čime se uklanja opšta greška
  „One or more fields need validation" nakon Auto Accounting-a.
- Saveti (tooltip) na dugmadima iskačućeg prozora polja (Delete, Clear,
  Confirm) kažu šta svako radi pre nego što kliknete.
- Optimistički red sada prikazuje ono što je sačuvano, a ne ono što je
  otkucano. Ponovno mapiranje kolone traži potvrdu samo kada vidljiva kolona
  izgubi mapiranje.
- Stranice iza ograničenja OCR stranica su samo za čitanje i označene su, i u
  Auto Accounting pregledaču. Stari panel za ograničenje stranica pri uvozu je
  ukinut.
- PO tabela se pojavljuje za svaki broj narudžbenice u polju zaglavlja sa više
  narudžbenica, a Layout Builder označava PO kartice prema ključu PO tabele i
  više ne prijavljuje modul kao isključen kada je PO tabela uključena.
- Kartica predloga ispisuje toleranciju umesto `[object Object]`, a ekran
  poređenja odobravanja prestaje da zaokružuje podešene kolone poređenja (brojevi
  artikala).

**Nalozi, podešavanja i greške**
- Svaki prozorčić sa greškom i greška prijave prikazuju trace id neuspelog
  zahteva, kako bi ga podrška pronašla. Greške WebSocket-a kontrolne table
  odbijaju tačno zahtev koji navode.
- Company Information navodi domene e-pošte organizacije.
- Administratori mogu ponovo da pošalju e-poruku „Set your password" sa stranice
  korisnika.
- Globalni administratori postavljaju početak ugovora u tabeli pretplate.
- Administratori organizacije vide karticu Executive Dashboard i dugmad za
  dodavanje i brisanje XSLT-a. Članovi čuvaju izglede kao sopstvenu preferencu.
- Sesija bez organizacije dobija jasnu grešku i izbor organizacije umesto prazne
  kontrolne table.
- Iznosi prate lični format brojeva korisnika, a vrednosti samo sa datumom
  zadržavaju svoj dan u svakoj vremenskoj zoni.
- Matični podaci šalju ID-jeve pod-organizacija samo kada se razlikuju od ID-ja
  organizacije, a prilagođena zaglavlja matičnih podataka šalju se kao
  zaglavlja.
- Maska Tables više ne seče padajuću listu „Use AI", tekst AI saveta više ne
  prekriva liniju treniranja, a AI tabela zadržava direktno dugme Apply, sa
  proverom zaglavlja samo u vidu ikone i porukom o licenci.
- Ikone ekstrakcije tabela ponovo se iscrtavaju nakon uklanjanja starog fonta
  ikona.

**Tabla zadataka**
- Tabla učitava svoju prvu stranicu sa manje duplih zahteva, Enter odmah
  pokreće pretragu, zakasneli odgovori se pridružuju pravoj pretrazi, podnožje
  prikazuje stvarni broj pogodaka umesto kapaciteta stranice, a brisanje
  započeto u jednoj organizaciji otkazuje se pre slanja ako promenite
  organizaciju.

---

## API Service — `12.83.293`

**Settings Assistant i MCP**
- Endpoint za ćaskanje sa zaštitnim ogradama: samo DocBits pitanja, nijedna
  izmena bez potvrde, nejasna ili meta pitanja dobijaju pomoć umesto odbijanja,
  a odgovori strimuju prvo kartice, pa tekst.
- Gradivni blokovi samo za čitanje za svaku oblast podešavanja (dozvole grupa,
  kanali uvoza, usklađivanje narudžbenica, računovodstvo, domeni e-pošte),
  katalog dubokih linkova sa alatom za pronalaženje podešavanja i pretraga
  dokumentacije sa slikama iz DocBits dokumentacije.
- Tok primene, talas 1: pregled, potvrda i poništavanje za podržana podešavanja,
  jedno pravilo opsega za sva tri, zaštićeno od dvostruke potvrde i isteka.
- MCP alati nikada ne čitaju datoteke sa servera u udaljenom režimu, a alati za
  fixture i lab rade samo na dev okruženju.

**AI**
- Novi modeli iza nivoa Fast i Full, nivo Auto, Nexus Flash i preferenca režima
  vizije. Sačuvane `AI_MODEL` preference prebacuju se na nove nivoe.
- „Use AI" dokumentuje šta strukturirana ekstrakcija zahteva.

**Bezbednost i izolacija**
- Samo administratori organizacije menjaju preference organizacije.
- Poziv `/accounting/rebuild` trenira samo organizaciju pozivaoca, odbija zahtev
  (fail closed) pri neuspelom pronalaženju organizacije i odgovara sa 400 za
  neispravan ID.
- XSLT, XML i PDF renderovanje zabranjuju pristup datotekama i mreži, ne
  razrešavaju spoljne includes, a bajtovi fakture se sanitizuju pre nego što
  stignu do transformatora. Renderovani PDF pregledi dozvoljavaju samo
  pouzdane hostove slika.
- Ključevi keša nose organizaciju i isti identifikator uvek daje isti ključ, pa
  tuđi ID organizacije više ne može da pročita keširane podatke. Brisanja keša
  kontrolne table na nivou cele organizacije pri svakoj izmeni dokumenta su
  uklonjena.
- Lista domena e-pošte organizacije prosleđuje se Auth-u.

**Usklađivanje narudžbenica i izvoz**
- Polje može da navede više elemenata troška čiji se iznosi dele srazmerno
  narudžbenici.
- Zamene odobravanja povezuju se sa aktivnim zahtevom za odobravanje, čuvanja
  izlečenih odobravanja više ne blokiraju, a dokument koji čeka odobrenje
  odbija se za izvoz.
- PDF/A anotacija zadržava katalog i ugrađeni XML, pa e-fakture zadržavaju svoj
  XML nakon anotacije. UBL fakture sa golim EN 16931 CustomizationID se
  klasifikuju (mreža e-faktura).
- GRPR se zaokružuje na 6 decimala koje M3 prihvata. Faktori konverzije osnovne
  jedinice mere dodaju se zamrznutoj stavci.
- Obrisane obuke i pravila formatiranja (soft-delete) se poštuju, a MCP
  `update_document_fields` više ne potvrđuje upis koji je izgubio. `get_table_rules`
  odgovara tipiziranim promašajem, a prazan payload prevoda koristi svoju
  rezervnu vrednost.
- Slovenački iznosi koriste `sl_SI`, a sačuvane preference se migriraju.
  Prilagođene oznake klasifikacije poslate kao UUID ID-jevi se razrešavaju.
  Deljene kontrolne table zadržavaju `created_by` i listu deljenja pri
  ažuriranju.
- Okviri grešaka kontrolne table nose `request_id` zahteva, a svaki neuspeo
  JSON odgovor nosi trace id.
- Sistem restartuje samo nezdrave radne procese umesto celog API parka i
  ispravno proverava registrovanu listu zadataka. Red monitora zaglavljivanja
  ponovo se troši.

---

## Auth Service — `1.78.49`

- Višefaktorski izazov je jednokratan na svakoj putanji prijave, ne samo u MCP
  toku. Upis zahteva kôd iz e-pošte, nakon prijave sa deljenom lozinkom ne
  izdaje se token za upis, a korisnici dobijaju obaveštenje kada se faktor
  upiše.
- Organizacije poseduju listu domena e-pošte, a svaki se može dodeliti samo
  jednom. Društvena prijava pridružuje organizaciji koja navodi verifikovani
  domen, nikada ne izmišlja organizaciju, korisnika ili pretplatu i odbija bez
  imenovanja ikoga, dok se administratori umesto toga obaveštavaju. Domeni koje
  Microsoft vraća su obrađeni.
- Svaka odbijena prijava nosi trace id. Administratori mogu ponovo da pošalju
  e-poruku „Set your password". Saldo ugovora je označen predznakom, a početak
  ugovora se evidentira u reviziji.

## Auth Bridge — `0.5.7`

- Replikacija naloga EU i US održava vezu hranjenom tokom usaglašavanja, sama
  ponovo prikači prekinuti slot replikacije, koristi ograničenu memoriju i
  postojeći izvor replikacije tretira kao uspeh. Prijava između regiona je
  pouzdanija.

## Docflow Service — `2.10.22`

- Zasebna kartica jedinične cene čita podrazumevane definicije polja
  organizacije za troškove i poredi svaki element troška koji polje navodi.
- Ograničenje izvršavanja radnog toka raste sa 30 na 50, a pretrage zapisa
  radnog toka odbijaju ID koji nije UUID.

## Docnet Service — `1.56.15`

- `list_document_fields` prijavljuje svaku konfigurisanu kolonu tabele,
  uključujući prazne.

## Extraction Service — `1.56.0.1`

- Nivoi: novi modeli iza nivoa Fast i Full, Auto, Nexus Flash i režim vizije.
  Zahtevi vizije ka inference hostu ostaju ispod njegovog ograničenja
  veličine.
- Ekstrakcija tabela sa Nexus-om grupiše stranice u serije (po dve), izvršava
  serije paralelno sa izmerenim vremenskim ograničenjem, ponavlja prolazne
  greške i deli seriju kojoj je isteklo vreme. Polja zaglavlja čitaju se iz
  svih serija.
- Američki iznosi: dodatni iznosi su deo jednačine ukupnog iznosa, par 1 se
  računa u zaštiti para 2, kandidati sa niskim skorom se preskaču kada porezi
  nisu nula, a „above" i „below" se poklapaju sa oznakama od više reči.
- Polja identifikatora popravljaju znakove koji se zaista pojavljuju, a
  nevidljivi znakovi tretiraju se prema onome što znače, pa se „O" više ne
  pretvara u neobičan znak.

## Fulltext Service — `1.42.41`

- Novi indeks za DocBits dokumentaciju, sa endpointima za ingest i pretragu,
  slikama u odgovorima i rokom za celu pretragu. Napaja Settings Assistant.

## PO Match Service — `1.59.48`

- Apsolutni prag za troškove koje narudžbenica očekuje kao nulu i tolerancija
  troškova za troškove koje narudžbenica ne budžetira.
- Kolona može da nosi oznaku „allow mismatch". Više elemenata troška po polju
  deli se srazmerno.
- Samo administratori organizacije pišu ili odobravaju pravila usklađivanja, a
  uslovi pravila prihvataju samo gramatiku izraza sa liste dozvoljenih.
- Izmene pravila mogu da se simuliraju prema skupu pravila koji ih nadjačava,
  bez upisa, za Touchless predloge izmena. PO dodatne kolone za usklađivanje
  čitaju se iz atributa tipa dokumenta, uz migraciju stare preference.

---

_Nisu zahvaćeni u ovom izdanju: Auto Accounting, Barcode, E-Mail, FTP, Ideas,
OCR, Operator. FTP i Operator nose samo interno održavanje._

<!-- Release R1.0.15 (sandbox 02-10-26, planned prod 14-10-26, deployed Wednesday 14 Oct 2026).
Versions on prod before this deploy: API 12.83.222, Auth 1.78.38, Auth Bridge 0.4.2,
Docflow 2.10.18, Docnet 1.56.13, Extraction 1.55.50.1, Fulltext 1.42.38, PO Match 1.59.39,
Web App 10.70.6.
Held back (Release No. names a later release; announce with that release):
R1.1: CORE-6145, CORE-6148 (import failure notice and card per channel), CORE-6127 and
CORE-6136 (run transformation rules after master data lookup), CORE-6117, CORE-6072, CORE-6071,
CORE-2452, CORE-2444, DRFS-779, CORE-554 (rule execution logs from the dashboard), CORE-550, CORE-6278,
CORE-6180, CORE-6168, DMB-431, OBO-160, DRFS-806 (date tolerance for PO matching and approval).
R1.0.16: CORE-6103 (assistant drafts transformation rules), DRFS-822 (charge cards use only
matched POs, trigger status filter), DPG-170 (cost invoice export gate), OBO-159 (the "x" on a
field stores "leave empty" on its own; field suppression).
R1.2 / R1.4: DRFS-535 (receipt availability flag), DOP-53 (UOM conversion).
Added from the Ready for Production Release list: DRFS-742, DU-220, MAR-67, DRFS-708, DRFS-820,
DRFS-723, DRFS-724, DRFS-726. Not on the page (no matching code in the delta, check by hand):
MEF-169 (S/MIME invoices from one supplier not arriving, Email Service version unchanged), DMB-391.
Shipped although Release No. is empty or stale: OBO-156, CORE-6102, CORE-6154, CORE-6155,
CORE-6150, CORE-6169, CORE-6181, CORE-6183, CORE-6185, CORE-6187, CORE-2606, CORE-2461,
CORE-2457, CORE-6092 (R1.0.14 labels). -->
