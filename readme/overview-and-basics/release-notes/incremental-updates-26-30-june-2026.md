# DocBits beleške o izdanju — 26–30. jun 2026.

_Šta je donela ova produkcijska nadogradnja, jednostavnim jezikom. Uz svaki servis
prikazana je verzija koja je sada aktivna u produkciji. Servisi koji nisu navedeni
nisu imali izmene vidljive korisnicima u ovom periodu._

---

## Najvažnije

- **Jedna veza za AI asistente ([DocBits MCP](https://docs.docbits.com/advanced-functions-and-tools/docbits-mcp)).** Jedinstveni, objedinjeni gateway
  sada opslužuje sve DocBits alate — uključujući DocFlow — kroz glavni API, tako da
  se AI asistenti (Claude, Gemini CLI, Codex) povezuju kroz jednu pouzdanu krajnju
  tačku umesto kroz više njih.
- **Pametnija višejezična pretraga kontrolne table.** Veznici pretrage
  (**AND / OR**) sada se prikazuju na vašem jeziku uz isticanje bojom, podtipovi
  faktura nude padajući meni vrednosti, a poruke o sintaksi pretrage su lokalizovane
  — uz sveukupno glađe rukovanje tastaturom.
- **Jednostavnije odobravanje i dozvole.** Odobravanje se više ne pokreće kada je
  jedinica pakovanja iz potvrde porudžbine prazna, obični korisnici ponovo mogu da
  odobravaju elemente troškova nakon migracije kontrole pristupa, a dozvole na nivou
  dokumenta primenjuju se ispravno čak i kada kolona tabele već postoji.
- **Aplikacija se sama ažurira.** Kada izađe nova verzija, DocBits se sada automatski
  osvežava umesto da vas prekida iskačućim prozorom „Osveži odmah".
- **Otpornije podudaranje porudžbina.** Transformacije vrednosti kolona, zaštita od
  pada za stavke bez cene ili količine i automatski ponovni pokušaj pri prekinutim
  vezama sa bazom podataka čine podudaranje stabilnijim.
- **Manje grešaka u celini.** Mnoge retke serverske greške na kontrolnim tablama,
  fakturama dobavljača, PO zapisima i OCR poslovima pronađene su i otklonjene.

---

## Web App — u produkciji: `10.34.4`

- **Brza pretraga kontrolne table:** lokalizovani veznici **AND / OR** (de/fr) uz
  isticanje sintakse bojom; padajući meni vrednosti za podtip fakture; lokalizovane
  poruke o greškama u sintaksi pretrage; glađe iskustvo sa tastaturom; upozorenje
  „potrebna pretraga celog teksta" sada se prikazuje u redu (inline) tako da raspored
  više ne poskakuje.
- **Odobravanje i dozvole:** ispravljeno pogrešno pokretanje odobravanja kada je
  jedinica pakovanja iz potvrde porudžbine prazna; obični korisnici ponovo mogu da
  odobravaju elemente troškova nakon migracije kontrole pristupa; dozvole na nivou
  dokumenta sada se primenjuju kada kolona tabele već postoji.
- **Automatsko ažuriranje:** aplikacija se automatski osvežava pri novoj verziji
  umesto da prikazuje iskačući prozor „Osveži odmah"; uklonjen je stari dijalog sa
  informacijama o verziji.
- **Podešavanja dolazne e-pošte:** novi prekidač i polje za primaoce obaveštenja o
  greškama; dnevnik uvoza sada prikazuje odlaznu aktivnost i razlog greške; dolazna
  adresa se pouzdano kopira.
- **Deljenje dokumenata:** ekran za deljenje dokumenata (Document Split) sada se
  skroluje.
- **Tamni režim:** ispravke za ekstrakciju tabela, brojač zadataka i oznake
  zatvorenih dokumenata na kontrolnoj tabli.
- **Upotrebljivost i stabilnost:** ispravke korisničkog interfejsa za izvoz sa
  kontrolne table; lepljiva zaglavlja tabela više ne probijaju kroz dijaloge; DocNet
  kontrolna tabla više ne pada pri neuspešnom zahtevu za statistiku; skripte polja
  više ne vraćaju ispražnjena polja na stare vrednosti; ispravke checkbox-ova i
  rasporeda u PO podešavanjima; ispravke prikaza liste za klasifikaciju.
- **Dobavljači:** organizacije dobavljača sada mogu da se registruju putem magic
  link-a.

## API Service — u produkciji: `12.46.8`

- **DocBits MCP gateway:** objedinjeni gateway sada proksira DocFlow alate kroz
  glavni API, tako da AI asistenti dosežu svaki DocBits alat kroz jednu krajnju
  tačku; MCP krajnja tačka opslužuje se bez preusmeravanja koje bi moglo da prekine
  veze.
- **Računovodstvo:** dodata je validacija mesta troška za računovodstveni ID.
- **OCR usmeravanje:** dokumenti se šalju na potpuni ponovni OCR kada je e-tekst
  dobavljača isključen, tako da tekst ostaje pouzdan.
- **Infor ERP / SAP:** dodatni troškovi usmeravaju se ispravno kada ERP već sadrži
  trošak sa nultim iznosom.
- **Pouzdanost (manje serverskih grešaka):** ojačani su upiti za kontrolnu tablu,
  fakture dobavljača, PO zapise i upravljač zadacima tako da više ne vraćaju retke
  greške 500; otpornija sinhronizacija keša organizacije i čišćenje sačuvanih
  datoteka.
- **Čistiji filteri kontrolne table:** uklonjeno suvišno polje filtera za broj
  fakture; ispravljena PO-usklađena količina.
- **API dokumentacija za programere:** Swagger UI sada nudi padajući meni
  specifikacija (OpenAPI 3.0 uz Infor Swagger 2.0 prikaz) sa DocBits brendiranjem.

## Auth Service — u produkciji: `1.68.0`

- **Brža odjava / opoziv tokena:** grupni opoziv tokena više ne traje minutima i ne
  prekida vezu.
- **Ispravljene e-poruke za postavljanje lozinke** tako da se prikazuju ispravno.
- **Dobavljači:** organizacije dobavljača mogu da se registruju putem magic link-a.
- **Stabilnost prijave:** član više ne biva zaključan zbog privremenog promašaja pri
  traženju organizacije, a nevažeći id organizacije sada vraća jasnu poruku umesto
  greške.

## Docflow Service — u produkciji: `2.4.1`

- **Pouzdan AI gateway:** otklonjena zamrzavanja i istek vremena na DocFlow MCP
  krajnjoj tački (rukovanje vezom, prekidi veze klijenta, duplirani odgovori) —
  DocFlow strana objedinjenog DocBits MCP gateway-a.

## OCR Service — u produkciji: `1.7.1`

- **Stabilnija OCR obrada:** pozadinski redovi odgovora automatski ističu, a
  privremeni prekidi veze se ponovo pokušavaju, tako da se manje OCR poslova
  zaglavljuje.

## PO Match Service — u produkciji: `1.55.7`

- **Transformacije vrednosti** sada se primenjuju na kolone item-id, unit-code i
  static-value tokom podudaranja po pravilima.
- **Zaštita od pada:** stavka bez cene ili količine, neuobičajena kombinacija
  ponderisanih ključeva ili nemoguće deljenje više ne obaraju podudaranje.
- **Pouzdanost:** upisi u bazu podataka automatski se ponavljaju pri prekinutim ili
  SSL-zatvorenim vezama.
- **Infor ERP / SAP:** dodatni troškovi usmeravaju se ispravno kada ERP sadrži
  trošak sa nultim iznosom.

## Fulltext Service — u produkciji: `1.35.6`

- **Brže ponovno indeksiranje:** sve faze sinhronizacije sada se granaju tako da se
  aktivira automatsko skaliranje, čime se otklanja sporo serijsko ponovno
  indeksiranje i zaglavljeni vidžet napretka na 0%.
- **Stabilnija statistika:** zahtevi za statistiku dokumenata između regiona su
  ograničeni tako da im više ne ističe vreme.

---

## Nema izmena vidljivih korisnicima u ovom periodu

Stabilno, bez značajnih izmena proizvoda između 26. i 30. juna: Auto Accounting
(`1.18.6`), Barcode (`1.15.6`), Docnet (`1.54.6`), Email (`1.36.4`), Extraction
(`1.48.7`), FTP (`1.30.1`), Operator (`1.39.5`). Auto Accounting i FTP dobili su
samo interno održavanje.

<!-- Generated by the docbits-changelog skill (prod-delta mode). Versions read live
     from prod (do-fra1-polydocs/prod); window 2026-06-26 → 2026-06-30. -->
