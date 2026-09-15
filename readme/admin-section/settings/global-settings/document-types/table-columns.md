# Kolone tabele

Kolone tabele određuju koje kolone ima tabela stavki jednog tipa dokumenta: šta DocBits ekstrahuje u svaku kolonu, šta korisnik vidi na ekranu za validaciju i šta se prilikom izvoza šalje u ERP.

**Gde:** Podešavanja → Globalna podešavanja → Tipovi dokumenata → Kolone tabele

<figure><img src="../../../../.gitbook/assets/table-columns_list.png" alt="Lista Kolone tabele sa oznakama Obavezno, Samo za čitanje, Skriveno i Koristi AI za svaku kolonu"><figcaption><p>Kolone tabele: jedan red po koloni, oznake se uključuju direktno u listi</p></figcaption></figure>

## Šta vidite

Svaki red je jedna kolona jedne tabele. Lista prikazuje:

| Kolona | Značenje |
|---|---|
| **Naziv kolone** (Column name) | Tehnički naziv, generisan iz naslova (velika slova, donje crte). Koristi se u skriptama, mapiranjima izvoza i API-ju. Kasnije se ne može menjati. |
| **Naslov** | Oznaka koja se prikazuje na ekranu za validaciju. Menjate je ikonom za prevod u koloni *Radnje* (*Update translation key*). |
| **Tip kolone** | `AMOUNT`, `STRING`, `DATE`, `NUMBER`, `BOOLEAN` ili `CURRENCY`. Određuje validaciju i formatiranje. |
| **Naziv tabele** | Tabela kojoj kolona pripada, na primer `INVOICE_TABLE`. |
| **Obavezno** (Is Required) | Dokument ne može da se odobri dok je ova kolona prazna u bilo kom redu. |
| **Samo za čitanje** (Read Only) | Korisnici vide vrednost, ali ne mogu da je menjaju. |
| **Skriveno** (Hidden) | Kolona se ne prikazuje i ne izvozi. Koristi se za isključivanje podrazumevanih kolona koje vam nisu potrebne. |
| **Koristi AI** (Use AI) | AI ekstrakcija tabele popunjava ovu kolonu, čak i kada dobavljač ima obučena pravila. |
| **Radnje** | Ikona za prevod: preimenovanje naslova. Ikona sa informacijama: odakle potiče prikazana oznaka (vaš prevod, podrazumevana vrednost, ključ). Meni sa tri tačke: *Obriši*, samo za kolone koje je kreirala vaša organizacija; podrazumevane kolone mogu samo da se sakriju. |

Iznad liste nalaze se dva dugmeta:

* **Kreiraj novu tabelu**: druga tabela stavki za tip dokumenta (na primer tabela troškova pored tabele artikala).
* **Dodaj novu kolonu tabele**: otvara dijalog opisan u odeljku [Dodavanje nove kolone](#dodavanje-nove-kolone).

## Podrazumevane kolone i vaše kolone

Svaki tip dokumenta dolazi sa skupom podrazumevanih kolona (za fakture: broj artikla, opis, količina, jedinična cena, ukupan iznos, porez, ...). One pripadaju DocBits-u, a ne vašoj organizaciji, pa ne mogu da se obrišu; umesto toga ih sakrijte. Kolone koje sami dodate pripadaju vašoj organizaciji i mogu da se obrišu.

{% hint style="info" %}
**Izmene važe samo za nove dokumente.** Kolona koju dodate, sakrijete ili obrišete pojavljuje se na dokumentima koji su otpremljeni ili ponovo pokrenuti nakon izmene. Dokumenti koji su već na kontrolnoj tabli zadržavaju tabelu onako kako je ekstrahovana. Ponovo pokrenite dokument da bi preuzeo novu konfiguraciju.
{% endhint %}

## Povezane stranice

* [Svrha i upotreba](#svrha-i-upotreba): gde se kolone tabele pojavljuju
* [Dodavanje nove kolone](#dodavanje-nove-kolone)
* [Izmena i brisanje kolona](#izmena-i-brisanje-kolona)
* [Najbolje prakse](#najbolje-prakse)
* [Otklanjanje problema](#otklanjanje-problema)
* [Obuka polja stavki / obuka tabele](../../../../setup/document-training/training-line-fields-table-training/README.md): naučite DocBits gde se nalazi tabela dobavljača
* [AI tabela](../../../../readme-1/ai-table.md): šta korisnik vidi na ekranu za validaciju

## Svrha i upotreba

Kolona tabele je jedno polje tabele stavki. Sve što DocBits radi sa tabelom (ekstrakcija, validacija, PO uparivanje, izvoz) radi na kolonama koje su ovde konfigurisane.

### Gde se kolona pojavljuje

| Mesto | Šta kolona tamo radi |
|---|---|
| **Ekran za validaciju** | Jedna kolona u tabeli stavki. *Naslov* je zaglavlje, *Tip kolone* određuje editor (iznos, datum, tekst, da/ne). Skrivene kolone se ne prikazuju. |
| **Obuka tabele** | Kada obučavate tabelu dobavljača, svaku prepoznatu kolonu tabele mapirate na jednu od ovde konfigurisanih kolona. Mogu se mapirati samo konfigurisane kolone. |
| **AI ekstrakcija tabele** | AI popunjava konfigurisane kolone. Kolonu označenu sa *Koristi AI* popunjava AI čak i kod dobavljača sa obučenim pravilima. |
| **Pravila validacije** | Provere stavki kao što je *količina × jedinična cena = ukupan iznos stavke* izvršavaju se na podrazumevanim kolonama `QUANTITY`, `UNIT_PRICE`, `TOTAL_AMOUNT`, `CHARGES`, `DISCOUNT`. |
| **PO uparivanje** | Zahteva podrazumevane kolone broj artikla, jedinična cena, količina i ukupan iznos. Bez njih dokument prikazuje poruku *Line Item Table is missing Mandatory column for PO*. |
| **Izvoz** | Svaka kolona koja nije skrivena deo je podataka o stavkama koji se šalju u ERP. Mapiranje izvoza referencira *Naziv kolone*. |
| **Skripte** | Skripte čitaju i upisuju kolone preko *Naziva kolone*, na primer `row["TOTAL_AMOUNT"]`. |

### Opseg

* Kolone tabele se konfigurišu **po tabeli**, a tabela pripada **tipu dokumenta**. Kolone faktura ne utiču na otpremnice.
* Konfiguracija važi **po organizaciji**. Podorganizacije je nasleđuju.
* Koje kolone se *popunjavaju* za određenog dobavljača odlučuje obuka tog dobavljača ili AI; konfiguracija kolona samo određuje koje kolone postoje.

### Tipični razlozi za izmenu konfiguracije

* Vrednost specifična za kupca mora da se beleži po stavci (mesto troška, broj projekta, interni broj artikla): dodajte kolonu.
* Podrazumevana kolona se nikada ne koristi i zatrpava ekran za validaciju: sakrijte je.
* Kolona mora uvek da bude popunjena pre izvoza: označite je kao *Obavezno*.
* Vrednost dolazi iz ERP pretrage i korisnici ne smeju da je menjaju: označite je kao *Samo za čitanje*.
* AI prepoznaje kolonu bolje od obučenih pravila (na primer opise u slobodnom tekstu): označite je sa *Koristi AI*.

## Dodavanje nove kolone

Dodajte kolonu kada po stavci treba beležiti vrednost koju podrazumevane kolone ne pokrivaju: mesto troška, broj projekta, interni broj artikla.

### Pre nego što počnete

* Odlučite kojoj **tabeli** kolona pripada. Većina tipova dokumenata ima jednu tabelu (na primer `INVOICE_TABLE`). Ako je lista prazna, prvo kliknite na **Kreiraj novu tabelu**; dijalog traži samo naziv tabele.
* Odlučite o **tipu**: `AMOUNT` za novčane iznose, `NUMBER` za količine, `DATE`, `BOOLEAN` za da/ne, `CURRENCY` za ISO kod valute, `STRING` za sve ostalo. Tip ne može da se promeni nakon čuvanja.
* Proverite da li **podrazumevana kolona** sa istim značenjem već postoji, ali je skrivena. Skrivene kolone su navedene sa uključenom oznakom *Skriveno*; otkrijte je umesto da kreirate duplikat.

### Koraci

1. Otvorite **Podešavanja → Globalna podešavanja → Tipovi dokumenata → Kolone tabele**.
2. Kliknite na **Dodaj novu kolonu tabele**.

<figure><img src="../../../../.gitbook/assets/table-columns_add-dialog.png" alt="Dijalog Dodaj novu kolonu tabele sa poljima Naslov, Da li je kolona obavezna, Izaberite tip kolone i Izaberite tabelu"><figcaption><p>Dodaj novu kolonu tabele</p></figcaption></figure>

3. Popunite dijalog:

| Polje | Šta uneti |
|---|---|
| **Naslov** | Oznaka koju korisnik vidi na ekranu za validaciju, na primer `Cost Centre`. Samo slova i brojevi. DocBits iz njega izvodi tehnički *Naziv kolone* (`COST_CENTRE`). |
| **Da li je kolona obavezna?** | Označite kada dokument ne sme da se odobri dok je kolona prazna u bilo kom redu. |
| **Izaberite tip kolone** | Pogledajte listu tipova iznad. |
| **Izaberite tabelu** | Tabela koja dobija kolonu. |

4. Kliknite na **Nastavi**. Kolona se pojavljuje u listi sa isključenim oznakama *Samo za čitanje*, *Skriveno* i *Koristi AI*. Po potrebi uključite te oznake u listi, pogledajte [Izmena i brisanje kolona](#izmena-i-brisanje-kolona).

### Nakon dodavanja

* Kolona je **prazna na postojećim dokumentima**. Popunjava se na dokumentima koji su otpremljeni ili ponovo pokrenuti nakon izmene.
* Za dobavljače sa **obučenim pravilima** otvorite jedan od njihovih dokumenata u obuci tabele i mapirajte novu kolonu; u suprotnom kolona ostaje prazna za tog dobavljača. Pogledajte [Definisanje tabela i kolona](../../../../setup/document-training/training-line-fields-table-training/defining-tables-and-columns.md).
* Uz **AI ekstrakciju tabele** AI popunjava kolonu ako je vrednost prepoznatljiva na dokumentu. Označite kolonu sa *Koristi AI* ako dobavljač ima obučena pravila, ali ova kolona ipak treba da dolazi od AI-ja.
* Dodajte kolonu u **mapiranje izvoza** ako ERP treba da je primi, pogledajte [Izvoz](../../document-processing/export.md).

### Poruke

| Poruka | Značenje |
|---|---|
| *Column name already exists* | Kolona sa ovim tehničkim nazivom već postoji u tabeli. Izaberite drugi naslov. |
| *Column name already exists – Please activate it in Table Column settings* | Skrivena podrazumevana kolona ima ovaj naziv. Isključite njenu oznaku *Skriveno* umesto da kreirate novu. |
| *No table exists. Please create table before creating columns.* | Tip dokumenta još nema tabelu: prvo kliknite na **Kreiraj novu tabelu**. |

## Izmena i brisanje kolona

Sve osim naslova menja se direktno u listi; ne postoji dijalog za izmenu.

**Gde:** Podešavanja → Globalna podešavanja → Tipovi dokumenata → Kolone tabele

### Uključivanje oznake

Označite ili poništite polje za potvrdu u redu. Izmena se odmah čuva (*Successfully saved*).

| Oznaka | Uključeno | Isključeno |
|---|---|---|
| **Obavezno** | Odobravanje je blokirano dok je kolona prazna u bilo kom redu; ekran za validaciju označava ćeliju. | Prazne ćelije su dozvoljene. |
| **Samo za čitanje** | Vrednost se prikazuje, ali ne može da se prekuca. Koristite je za vrednosti koje dolaze iz pretrage ili skripte. | Korisnici mogu da menjaju ćeliju. |
| **Skriveno** | Kolona nestaje sa ekrana za validaciju i iz izvoza. Njeni podaci se čuvaju. | Kolona se prikazuje i izvozi. |
| **Koristi AI** | AI ekstrakcija tabele popunjava ovu kolonu, i kod dobavljača koji imaju obučena pravila. | Kolonu popunjavaju obučena pravila, ili AI kada pravila ne postoje. |

{% hint style="info" %}
Oznake važe za dokumente otpremljene ili ponovo pokrenute **nakon** izmene. Otvoreni dokumenti zadržavaju svoju trenutnu tabelu dok se ponovo ne pokrenu.
{% endhint %}

### Preimenovanje naslova

Kliknite na ikonu za prevod u koloni *Radnje* (*Update translation key*), unesite novu oznaku i potvrdite. Ikona sa informacijama pored nje prikazuje koja oznaka trenutno važi i odakle potiče. Menja se samo oznaka; tehnički *Naziv kolone* ostaje isti, tako da skripte, mapiranja izvoza i obučena pravila nastavljaju da rade.

### Promena tipa ili tabele

Nije moguća. Sakrijte kolonu (ili je obrišite ako je vaša) i dodajte novu sa odgovarajućim tipom.

### Brisanje kolone

Radnja brisanja se nudi samo za kolone koje je kreirala vaša organizacija. Podrazumevane kolone ne mogu da se obrišu; sakrijte ih.

1. Otvorite meni sa tri tačke u koloni *Radnje* i izaberite **Obriši**. Kod podrazumevanih kolona ova stavka ne postoji.
2. Potvrdite.

Šta se dešava:

* Kolona se uklanja iz konfiguracije. Dokumenti koji se obrađuju **od tog trenutka** više je nemaju.
* Već ekstrahovani dokumenti zadržavaju kolonu i njene vrednosti dok se ponovo ne pokrenu.
* Obučena pravila koja su mapirala ovu kolonu nastavljaju da rade za ostale kolone; mapiranje obrisane kolone se ignoriše.
* Ako se kolona referencira u mapiranju izvoza ili skripti, uklonite tu referencu; u suprotnom izvoz ili skripta ne uspeva sa greškom o nedostajućoj koloni.

### Poništavanje brisanja

Obrisana kolona ne može da se vrati iz liste. Dodajte je ponovo sa istim naslovom: tehnički naziv se izvodi iz naslova, pa kolona kreirana sa istim naslovom dobija isti *Naziv kolone* i postojeća mapiranja ponovo odgovaraju.

## Najbolje prakse

### Zadržite podrazumevane kolone za iznose i količine

Provere stavki (*količina × jedinična cena = ukupan iznos stavke*) i PO uparivanje traže podrazumevane kolone `QUANTITY`, `UNIT_PRICE`, `TOTAL_AMOUNT`, `ITEM_NUMBER`. Ako umesto njih kreirate sopstvene kolone za ove vrednosti, provere se ne izvršavaju, a PO uparivanje prijavljuje nedostajuće obavezne kolone. Preimenujte *naslov* ako vam formulacija ne odgovara; kolonu zadržite.

### Sakrijte, nemojte brisati

Podrazumevane kolone koje vam nisu potrebne se sakrivaju, ne brišu; one ionako ne mogu da se obrišu. I za vaše kolone sakrivanje je bezbedniji izbor dok niste sigurni da li skripta ili mapiranje izvoza još uvek referencira kolonu.

### Označite kao obavezno samo ono što blokira izvoz

Svaka obavezna kolona mora da bude popunjena u svakom redu pre nego što korisnik može da odobri dokument. Koristite to za vrednosti koje ERP odbija kada nedostaju (na primer mesto troška u računovodstvenom izvozu), a ne za vrednosti koje su samo korisne.

### Koristite *Samo za čitanje* za vrednosti iz pretrage

Vrednosti koje skripta ili pretraga matičnih podataka upisuje u tabelu (opis artikla iz matičnih podataka artikala, poreski kod od dobavljača) treba da budu samo za čitanje, kako bi korisnici ispravljali izvor, a ne kopiju.

### Koristite AI po koloni, a ne po dobavljaču

Kod dobavljača sa obučenim pravilima većina kolona izlazi ispravno iz pravila. Ako je jedna kolona nepouzdana (dugi opisi koji se prelamaju, popust koji ponekad stoji na drugom mestu), uključite *Koristi AI* samo za tu kolonu. Pravila zadržavaju ostatak.

### Imenujte kolone prema ERP-u, a ne prema dokumentu

*Naziv kolone* završava u mapiranjima izvoza i skriptama. `COST_CENTRE` je lakše mapirati nego `KST` i ne menja se kada ga dobavljač drugačije odštampa.

### Testirajte na ponovo pokrenutom dokumentu

Nakon izmene ponovo pokrenite jedan postojeći dokument tog tipa i otvorite ga: nova kolona se pojavljuje, skrivena je nestala, obavezne ćelije su označene. Tek onda to pustite korisnicima.

### Jedna tabela po strukturi stavki

Kreirajte drugu tabelu samo kada tip dokumenta zaista ima dve nezavisne tabele (na primer stavke artikala i zasebnu tabelu troškova). Dodatne prazne tabele se pojavljuju na svakom dokumentu tog tipa.

## Otklanjanje problema

### Nova kolona se ne pojavljuje na ekranu za validaciju

* Dokument je obrađen pre nego što je kolona dodata. Izmene važe za dokumente otpremljene ili ponovo pokrenute nakon toga, **ponovo pokrenite dokument** (Kontrolna tabla → meni dokumenta → Ponovo pokreni).
* Kolona je **skrivena**. Proverite oznaku u listi Kolone tabele.
* Kolona je dodata u **drugu tabelu**, a ne u prikazanu. Ekran za validaciju prikazuje tabele tipa dokumenta; uporedite kolonu *Naziv tabele*.
* Dokument nije tipa dokumenta koji ste konfigurisali.

### Kolona postoji, ali je uvek prazna

* Dobavljač ima **obučena pravila** i nova kolona u njima nije mapirana. Otvorite jedan od dokumenata dobavljača u obuci tabele i mapirajte kolonu, ili uključite *Koristi AI* za kolonu.
* Kod AI ekstrakcije vrednost nije prepoznatljiva na dokumentu (nema zaglavlja, skraćena je, na drugom jeziku). Dodajte oznaku (tag) za AI tabelu koja imenuje kolonu, ili je mapirajte u obuci.

### "Column name already exists"

Kolona sa istim tehničkim nazivom već postoji u tabeli. Ako nije u listi, radi se o skrivenoj podrazumevanoj koloni: poruka glasi *Please activate it in Table Column settings*. Isključite *Skriveno* za tu kolonu umesto da kreirate novu.

### Odobravanje je blokirano obaveznom kolonom

Poruka na tabeli imenuje kolonu. Ili popunite ćeliju u svakom redu, ili (ako vrednost ne postoji na ovom dokumentu) isključite *Obavezno* za kolonu, ponovo pokrenite dokument i pokušajte ponovo. Razmislite da li kolona uopšte treba da bude obavezna (pogledajte [Najbolje prakse](#najbolje-prakse)).

### AI popunjava kolonu pogrešnom vrednošću

Tipičan slučaj: `CHARGES` dobija ukupan iznos stavke, pa svaki red potom ne prolazi proveru ukupnog iznosa stavke sa porukom *Line total does not match quantity x unit price (expected …, got …)*, jer su troškovi deo formule `količina × jedinična cena + troškovi`.

* Isključite *Koristi AI* za kolonu ako je obučena pravila ispravno prepoznaju.
* Ako dobavljač nema pravila, jednom obučite tabelu (obuka tabele) da bi kolona bila vezana za pravu poziciju, ili sakrijte kolonu ako dobavljač nikada ne štampa tu vrednost.
* Kao poslednje rešenje, *Preskoči validaciju tabele* u Dodatnim postavkama tipa dokumenta isključuje sve provere tabele za ceo tip dokumenta; neslaganje se tada više ne otkriva, kao ni prazne obavezne kolone.

### PO uparivanje: "Line Item Table is missing Mandatory column"

PO uparivanje zahteva podrazumevane kolone broj artikla, jedinična cena, količina i ukupan iznos. Jedna od njih je skrivena ili je zamenjena prilagođenom kolonom. Otkrijte podrazumevanu kolonu ili mapirajte vrednost na nju u obuci tabele.

### Skripta ili izvoz ne uspeva nakon brisanja kolone

Skripta ili mapiranje izvoza i dalje referencira obrisani *Naziv kolone*. Uklonite referencu ili ponovo dodajte kolonu sa istim naslovom; tehnički naziv se izvodi iz naslova i ponovo se poklapa.

### Gde dalje potražiti

* [Obuka polja stavki / obuka tabele](../../../../setup/document-training/training-line-fields-table-training/README.md)
