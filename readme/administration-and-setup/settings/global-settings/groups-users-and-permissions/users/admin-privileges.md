# Administratorska ovlašćenja

Uloga administratora je ključna za upravljanje IT sistemima, mrežama i digitalnim platformama u organizaciji. Administrator ima napredna ovlašćenja i odgovornosti koje mu omogućavaju da kontroliše različite aspekte tehničke infrastrukture i da obezbedi njeno efikasno i bezbedno funkcionisanje. Evo nekih od glavnih odgovornosti administratora:

* **Upravljanje korisnicima:** Administratori upravljaju korisničkim nalozima, pravima pristupa i ovlašćenjima. Oni kreiraju nove korisničke naloge, dodeljuju im potrebna ovlašćenja i upravljaju kontrolom pristupa kako bi obezbedili da samo ovlašćeni korisnici mogu da pristupe određenim resursima.
* **Bezbednost:** Administratori su odgovorni za bezbednost IT sistema radi zaštite od gubitka podataka i neovlašćenog pristupa.
* **Rešavanje problema i podrška:** Administrator je često prva osoba kojoj se obraćate za tehničke probleme. Oni pomažu korisnicima da otkriju i reše probleme i obezbeđuju da sistem nesmetano radi.

Pored ovih odgovornosti, administratori imaju i zadatak da upravljaju osetljivim podešavanjima i da obezbede da sistemi ispunjavaju zahteve usklađenosti i najbolje prakse u oblasti bezbednosti informacija. Ovo uključuje upravljanje osetljivim podacima, konfigurisanje kontrola pristupa i ovlašćenja, kao i praćenje i analizu sistemskih zapisa radi identifikovanja i otklanjanja potencijalnih bezbednosnih rizika.

## Admin vs System Admin

DocBits ima dve administratorske uloge: **Admin** i **System Admin**. Zvuče slično, ali obavljaju različite poslove. Evo jednostavnog objašnjenja.

### Admin — osoba koja upravlja vašom organizacijom

**Admin** je stvarna osoba u vašem timu kojoj je dozvoljeno da upravlja DocBits-om. Admini mogu da:

* Otvore sve oblasti u **Podešavanjima** i menjaju način na koji vaša organizacija funkcioniše.
* Dodaju nove korisnike, menjaju ih, uključuju ih ili isključuju i odlučuju ko još postaje Admin.
* Podese grupe, ovlašćenja, integracije i radne tokove.

Možete imati **onoliko Admina koliko vam je potrebno**, i možete dodeliti ili oduzeti Admin ulogu bilo kom korisniku u bilo kom trenutku. Većina administratora u vašem timu pripada ovom tipu.

### System Admin — nalog koji DocBits koristi za samostalan rad

**System Admin** je **jedan poseban nalog po organizaciji** koji DocBits koristi za radnje koje se dešavaju **automatski, bez ičijeg klika na dugme** — na primer kada se dokumenti uvoze iz e-pošte, izvoze u drugi sistem ili prosleđuju putem povezane usluge u pozadini.

Zamislite ga kao „robotski“ nalog organizacije. Kada sistem nešto uradi samostalno, to radi **kao System Admin**, tako da je takvu automatsku aktivnost lako prepoznati i ne meša se sa radom stvarnih članova vašeg tima.

System Admin je poseban na tri načina:

* **Uvek je takođe i Admin.** Izborom System Admin uloge tom nalogu se automatski dodeljuju i puna Admin ovlašćenja.
* **Postoji samo jedan po organizaciji.** Kada System Admin već postoji, ne možete drugog korisnika označiti kao System Admin.
* **Postavlja se samo prilikom kreiranja korisnika.** O tome odlučujete u trenutku dodavanja korisnika. To se **ne može uključiti ili isključiti naknadno**.

> **Preporuka:** Kreirajte namenski nalog za ovu svrhu — na primer `system@your-company.com` — i označite ga kao System Admin. Na taj način se sve što DocBits radi automatski jasno prikazuje kao **System Admin** u vašim zapisima i istoriji dokumenata, odvojeno od vaših stvarnih korisnika.

### Ukratko

| | Admin | System Admin |
|---|---|---|
| Pun pristup upravljanju organizacijom | Da | Da |
| Koliko ih možete imati | Onoliko koliko vam je potrebno | Samo jedan |
| Može se menjati nakon kreiranja korisnika | Da, bilo kada | Ne, postavlja se samo pri kreiranju |
| Koristi se za automatske radnje u pozadini | Ne | Da |
| Uvek ima Admin ovlašćenja | — | Da |

## Najbolja bezbednosna praksa

Bezbednost je suštinski aspekt svake organizacije, posebno kada je reč o upravljanju korisničkim nalozima i pravima pristupa. Evo nekoliko najboljih praksi za održavanje bezbednog protokola upravljanja korisnicima:

* **Redovno ažuriranje lozinki:** Podstaknite korisnike da redovno ažuriraju svoje lozinke kako bi njihovi nalozi ostali bezbedni. Uspostavite pravila o složenosti lozinki i zahtevajte korišćenje jakih lozinki koje sadrže kombinaciju slova, brojeva i specijalnih znakova.
* **Pratite radnje administratora:** Uvedite mehanizme za praćenje aktivnosti administratora kako biste otkrili sumnjive ili neuobičajene radnje. Beležite sve radnje administratora, uključujući pristup osetljivim podacima ili podešavanjima, kako biste obezbedili odgovornost i identifikovali potencijalne bezbednosne propuste.
* **Ograničite broj administratora:** Smanjite broj administratora na minimum i dodeljujte administratorska ovlašćenja samo onima kojima su zaista potrebna. Ograničavanjem broja administratora smanjujete rizik od bezbednosnih propusta i olakšavate upravljanje korisničkim nalozima i njihovo praćenje.
* **Dvofaktorska autentifikacija (2FA):** Uvedite dvofaktorsku autentifikaciju za administratorske naloge radi dodatnog povećanja bezbednosti. Time se uvodi dodatni bezbednosni korak koji obezbeđuje da, čak i ako je lozinka kompromitovana, napadač ne dobije neovlašćeni pristup nalogu.
* **Redovne bezbednosne provere:** Sprovodite redovne bezbednosne provere i revizije kako biste identifikovali i otklonili potencijalne bezbednosne propuste ili slabosti. Proverite prava pristupa i ovlašćenja korisničkih naloga kako biste se uverili da odgovaraju trenutnim zahtevima i najboljim praksama.
* **Obuka i podizanje svesti:** Redovno obučavajte zaposlene i administratore o najboljim bezbednosnim praksama i podižite svest o phishing napadima i drugim sajber pretnjama. Upoznajte ih sa značajem bezbednosti i podstaknite ih da prijavljuju sumnjive aktivnosti.

Primenom ovih najboljih praksi, organizacije mogu poboljšati bezbednost svog protokola za upravljanje korisnicima i smanjiti rizik od bezbednosnih propusta i gubitka podataka. Važno je posmatrati bezbednost kao kontinuiran proces i sprovoditi redovna ažuriranja i prilagođavanja kako biste išli u korak sa pretnjama i bezbednosnim zahtevima koji se stalno menjaju.
