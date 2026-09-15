# Ekran za validaciju

## Pregled

<div data-full-width="false">

<figure><img src="../.gitbook/assets/Bildschirmfoto 2024-05-10 um 07.58.15.png" alt=""><figcaption></figcaption></figure>

</div>

## **Dugme Sačuvaj:**

<figure><img src="../.gitbook/assets/Bildschirmfoto 2024-05-10 um 08.40.49 (2).png" alt=""><figcaption></figcaption></figure>

* **Dugme Sačuvaj:**
* **Svrha:** Čuva trenutno stanje dokumenta ili skripte na kojoj se radi.
* **Upotreba:** Nakon izmene ili dodavanja napomena u dokument, koristite ovo dugme da biste osigurali da su sve izmene sačuvane.

### **Dodaj specijalna pravila:**

<figure><img src="../.gitbook/assets/Bildschirmfoto 2024-05-10 um 08.41.01.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/Bildschirmfoto 2024-05-10 um 08.42.13.png" alt=""><figcaption></figcaption></figure>

* **Dodaj Specijalna Pravila / Dodaj Skriptu u DocBits:**
* **Svrha:** Omogućava korisnicima da implementiraju specifična pravila ili skripte koje prilagođavaju način obrade dokumenata.
* **Upotreba:** Koristite ovu funkciju za automatizaciju zadataka poput ekstrakcije podataka ili validacije formata, poboljšavajući efikasnost radnog toka.

{% hint style="info" %}
Pogledajte ovde dodaj [Skriptu u DocBits](../admin-section/setup/scripting-in-docbits/)
{% endhint %}

### **Mutna polja:**

<figure><img src="../.gitbook/assets/Bildschirmfoto 2024-05-10 um 08.46.38 (1).png" alt=""><figcaption></figcaption></figure>

*   **Mutna Polja:**

* **Svrha:** Pomaže u identifikaciji i ispravljanju polja gde podaci možda nisu savršeno podudarni, ali su dovoljno blizu.
* **Upotreba:** Korisno u procesima validacije podataka gde tačna podudaranja nisu uvek moguća, kao što su imena ili adrese sa blagim greškama u kucanju.

## Ekstrahovana tabela (stavke)

<figure><img src="../.gitbook/assets/validation_screen_line_items_table.png" alt="Tabela stavki na ekranu za validaciju sa trakom sa alatkama tabele"><figcaption><p>Ekstrahovana tabela ispod polja zaglavlja</p></figcaption></figure>

Ispod polja zaglavlja DocBits prikazuje tabelu stavki dokumenta: jedan red po stavci fakture, jedna kolona po [koloni tabele](../admin-section/settings/global-settings/document-types/table-columns.md) konfigurisanoj za tip dokumenta. Kada tip dokumenta ima više tabela (na primer artikle i troškove), svaka tabela ima svoju karticu iznad mreže.

### Odakle tabela potiče

Iznad mreže postoji po jedna kartica za svaki put ekstrakcije koji je organizacija uključila:

| Kartica | Značenje |
|---|---|
| **Ekstrahovana tabela** | Ekstrakcija zasnovana na pravilima (podešavanje *Ekstrakcija tabela*). Kod dobavljača sa obučenom tabelom ovi redovi dolaze iz sačuvanih pravila i ekstrahuju se na isti način na svakom dokumentu tog dobavljača; kod neobučenog dobavljača kartica može biti prazna. |
| **AI ekstrahovana tabela** | AI ekstrakcija tabele (podešavanje *AI ekstrakcija tabela*). Popunjava se kada dobavljač nema sačuvana pravila, a za kolone označene sa *Koristi AI* čak i kada pravila postoje. Opis *AI table not found* na kartici znači da AI nije vratio ništa za ovaj dokument. |
| **PO tabele** | Samo u graditelju rasporeda: stavke narudžbenice koje se koriste za uparivanje. |

Ako se ne pojavljuje nijedna kartica, oba podešavanja tabele su isključena za organizaciju (Podešavanja → Obrada dokumenata → Klasifikacija i ekstrakcija). Koji AI nivo čita tabelu podešava se po organizaciji i može se zameniti po dobavljaču (AI model specifičan za dobavljača pod *Više postavki*).

### Rad u tabeli

* **Izmena ćelije**: kliknite u nju i kucajte. Kolone sa iznosima, brojevima i datumima validiraju se tokom kucanja.
* **Dodaj novi red tabele**: dodaje prazan red na kraj. Koristite ga kada stavka nije prepoznata.
* **Brisanje reda**: ikona kante na kraju reda.
* **Dodaj prazne mapirane kolone**: prikazuje konfigurisane kolone koje je AI ostavio prazne, tako da možete ručno da ih popunite.
* **Obnovi kolonu tabele**: vraća kolonu koju ste uklonili iz prikaza za ovaj dokument.
* **Obriši tabelu**: briše sve redove ove tabele na ovom dokumentu. Konfiguracija se ne dira.
* **Dodaj novu kolonu tabele** (administratori): isti dijalog kao u podešavanjima kolona tabele, bez napuštanja dokumenta.
* **Oznake (tags)** (samo AI tabela): kratke tekstualne napomene za AI, na primer *"poslednja kolona je neto iznos"*.
* **Primeni** / **Sačuvaj** / **Obriši** pored oznaka: *Primeni* ponovo pokreće AI tabelu za ovaj dokument sa oznakama i izmenama kolona koje ste napravili, bez čuvanja (ako dokument ima stavke uparene sa narudžbenicom, DocBits upozorava da se uparivanja uklanjaju); *Save Rules* čuva trenutno mapiranje kolona i oznake za ovog dobavljača; *Delete Rules* ih uklanja i ponovo pokreće AI ekstrakciju za ovaj dokument.
* **Izvoz**: preuzima tabelu kao CSV datoteku.
* **Idi na prikaz ekstrakcije tabele**: otvara obuku tabele za ovaj dokument. Koristite ga kada isti dobavljač stalno daje pogrešan rezultat: jednom nacrtajte tabelu, mapirajte kolone i kliknite na *Save Rules*; od tada se redovi pojavljuju na kartici *Ekstrahovana tabela*. Pogledajte [Obuka polja stavki / obuka tabele](../setup/document-training/training-line-fields-table-training/README.md).

{% hint style="info" %}
Ako je tabelu ekstrahovao AI, a vi otvorite obuku tabele, DocBits pita *Table is already extracted by AI. Do you want to train manually?* Nakon što sačuvate pravila, AI tabela se više ne koristi za ovog dobavljača.
{% endhint %}

### Ponovna ekstrakcija tabele

* **Isti dokument, AI tabela:** dodajte ili izmenite oznake i kliknite na **Primeni**; AI tabela se ponovo gradi samo za ovaj dokument. Da biste odbacili i sačuvane oznake i formatiranje dobavljača, kliknite na **Obriši** (*Delete Rules*): DocBits potvrđuje sa *Rules has been deleted successfully* i ponovo pokreće AI ekstrakciju.
* **Isti dokument, obučena pravila:** otvorite *Idi na prikaz ekstrakcije tabele*, ispravite tabelu i kliknite na *Save & re-extract*.
* **Ceo dokument ponovo (zaglavlje i tabela):** Kontrolna tabla → meni dokumenta → *Ponovo pokreni*. Potrebno je nakon što administrator promeni kolone tabele ili podešavanja ekstrakcije.

### Šta blokira odobravanje

Tabela se proverava kada sačuvate ili odobrite dokument. Crvena ćelija ili poruka ispod tabele znači jedno od sledećeg:

| Poruka | Uzrok | Šta uraditi |
|---|---|---|
| Obavezna kolona je prazna | Kolona označena sa *Obavezno* nema vrednost u ovom redu. | Popunite ćeliju ili pitajte administratora da li kolona mora da bude obavezna. |
| *Line total does not match quantity x unit price (expected …, got …)* | `količina × jedinična cena + troškovi − popust` razlikuje se od ukupnog iznosa stavke za više od 0,02. Često je jedna od četiri vrednosti pročitana u pogrešnu kolonu. | Ispravite vrednost koja je pogrešna na dokumentu; ako je kolona kao što je *Troškovi* dosledno popunjena pogrešnom vrednošću, obavestite administratora (pogledajte [Otklanjanje problema](../admin-section/settings/global-settings/document-types/table-columns.md#otklanjanje-problema)). |
| *Line items add up to … but the net total is …* | Zbir ukupnih iznosa stavki razlikuje se od neto iznosa u zaglavlju. | Proverite da li nedostaje red ili je dupliran, ili je iznos u zaglavlju pogrešno pročitan. |
| *Line Item Table is missing Mandatory column for PO* | PO uparivanje zahteva broj artikla, jediničnu cenu, količinu i ukupan iznos; jedna od tih kolona je skrivena. | Administrator: otkrijte kolonu pod Kolone tabele. |

Administrator može da isključi sve provere tabele za tip dokumenta pomoću *Preskoči validaciju tabele* (Tipovi dokumenata → Dodatne postavke); neslaganja stavki i prazne obavezne kolone se tada ne prijavljuju.

### **Lupa:**

<figure><img src="../.gitbook/assets/Bildschirmfoto 2024-05-10 um 09.00.49.png" alt="" width="118"><figcaption></figcaption></figure>

* **Lupa (Povećaj Lupa):**
* **Svrha:** Pruža uvećani prikaz odabranog dela dokumenta.
* **Upotreba:** Pomaže u pregledu sitnih detalja ili malog teksta u dokumentima, osiguravajući tačnost unosa podataka ili pregleda.

<figure><img src="../.gitbook/assets/Bildschirmfoto 2024-05-10 um 14.03.46.png" alt=""><figcaption></figcaption></figure>

### **Otvori novi prozor:**

<figure><img src="../.gitbook/assets/Bildschirmfoto 2024-05-10 um 09.01.26.png" alt="" width="130"><figcaption></figcaption></figure>

* **Otvori Novi Prozor:**
* **Svrha:** Otvara novi prozor za poređenje dokumenata jedan pored drugog ili multitasking.
* **Upotreba:** Korisno prilikom poređenja dva dokumenta ili kada se referiše na dodatne informacije bez napuštanja trenutnog dokumenta.

### **Prečice na tastaturi:**

<figure><img src="../.gitbook/assets/Bildschirmfoto 2024-05-10 um 09.01.42.png" alt="" width="145"><figcaption></figcaption></figure>

1. **Prečice na tastaturi:**
* **Svrha:** Omogućava korisnicima brzo izvršavanje radnji korišćenjem kombinacija na tastaturi.
* **Upotreba:** Poboljšava brzinu i efikasnost u navigaciji i obradi dokumenata smanjujući oslanjanje na navigaciju mišem.

<figure><img src="../.gitbook/assets/Bildschirmfoto 2024-05-10 um 14.05.39.png" alt=""><figcaption><p>Tastatura</p></figcaption></figure>

### **Zadaci:**

<figure><img src="../.gitbook/assets/Bildschirmfoto 2024-05-10 um 09.02.00.png" alt="" width="55"><figcaption></figcaption></figure>

Da biste podelili internu informaciju, možete kreirati zadatke i dodeliti ih određenom zaposlenom ili grupi unutar kompanije.

* **Zadaci:**
* **Svrha:** Omogućava korisnicima da kreiraju zadatke vezane za dokumenta i dodele ih članovima tima.
* **Upotreba:** Olakšava saradnju i upravljanje zadacima unutar timova, osiguravajući da svi znaju svoje odgovornosti.

<figure><img src="../.gitbook/assets/Bildschirmfoto 2024-05-10 um 11.21.27.png" alt="" width="218"><figcaption></figcaption></figure>

### **Režim anotacija:**

<figure><img src="../.gitbook/assets/Bildschirmfoto 2024-05-10 um 09.02.21.png" alt="" width="187"><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (35).png" alt=""><figcaption></figcaption></figure>

Možete ostaviti anotacije na dokumentu. Ovo može biti korisno kako biste ostavili informacije za druge korisnike koji će dalje uređivati ovaj dokument.

* **Režim Anotacija:**
* **Svrha:** Omogućava korisnicima da ostave beleške ili anotacije direktno na dokumentu.
* **Upotreba:** Korisno za pružanje povratnih informacija, uputstava ili važnih napomena drugim članovima tima koji će kasnije raditi na dokumentu.

### **Spajanje:**

<figure><img src="../.gitbook/assets/Bildschirmfoto 2024-05-10 um 09.02.33.png" alt="" width="60"><figcaption></figcaption></figure>

Dokumenti se mogu spojiti ovde, na primer ako je stranica fakture nedostajala, ove stranice se mogu kasnije spojiti na ovaj način bez potrebe da se ceo dokument obriše ili ponovo otpremi.

* **Spajanje Dokumenata:**
* **Svrha:** Spaja više dokumenata u jedan fajl.
* **Upotreba:** Korisno u scenarijima gde delovi dokumenta se skeniraju odvojeno i treba ih konsolidovati.

### **Prikaz OCR-a:**

<figure><img src="../.gitbook/assets/Bildschirmfoto 2024-05-10 um 09.03.00.png" alt="" width="77"><figcaption></figcaption></figure>

U prikazu OCR-a, tekst se automatski filtrira iz dokumenta. Ovo se koristi za prepoznavanje relevantnih karakteristika, kao što su poštanski broj, broj ugovora, broj fakture i sortiranje dokumenta.

* **Prikaz OCR-a:**
* **Svrha:** Automatski prepoznaje tekst unutar dokumenata koristeći tehnologiju optičkog prepoznavanja karaktera.
* **Upotreba:** Optimizuje proces digitalizacije štampanih ili ručno pisanih tekstova, čineći ih pretraživim i izmenjivim.

<figure><img src="../.gitbook/assets/Bildschirmfoto 2024-05-10 um 14.07.25.png" alt=""><figcaption><p>OCR</p></figcaption></figure>

### **Kreiraj tiket:**

<figure><img src="../.gitbook/assets/Bildschirmfoto 2024-05-10 um 09.03.24.png" alt="" width="97"><figcaption></figcaption></figure>

Za razliku od zadataka koji se prenose interno unutar kompanije, ovaj podršni tiket je važan kako bi nas obavestio i odmah kreirao tiket u slučaju grešaka i/ili neslaganja. Ovo olakšava proces jer možete odmah poslati bag sa odgovarajućim dokumentom. Takođe postoji opcija za postavljanje prioriteta, pravljenje snimka ekrana dokumenta ili njegovo otpremanje.

* **Kreiraj Tiket:**
* **Svrha:** Omogućava korisnicima da prijave probleme ili neslaganja kreiranjem podršnog tiketa.
* **Upotreba:** Ključno za brzo rešavanje problema i bagova, pomažući održavanju integriteta i glatkog funkcionisanja sistema.

<figure><img src="../.gitbook/assets/Bildschirmfoto 2024-05-10 um 10.45.07.png" alt="" width="237"><figcaption></figcaption></figure>
### **Dnevnički skriptova dokumenta:**

<figure><img src="../.gitbook/assets/Bildschirmfoto 2024-05-10 um 09.03.34.png" alt="" width="160"><figcaption></figcaption></figure>

Skripte se mogu kreirati u postavkama pod Tipovima dokumenata; ove informacije će biti prikazane ovde.

* **Dnevnički skriptova dokumenata:**
* **Svrha:** Prikazuje dnevnike povezane sa skriptovima koji su implementirani za različite tipove dokumenata.
* **Upotreba:** Korisno za praćenje i otklanjanje grešaka u radu skriptova na dokumentima, pomažući korisnicima da razumeju automatizovane procese i isprave eventualne probleme.

<figure><img src="../.gitbook/assets/image (34).png" alt=""><figcaption></figcaption></figure>



### **Više postavki:**

<figure><img src="../.gitbook/assets/Bildschirmfoto 2024-05-10 um 09.04.13.png" alt="" width="239"><figcaption></figcaption></figure>

### **Podeli dokument:**

* Ovde možete podeliti dokument i iseći ili obrisati stranice koje nisu potrebne
* **Podeli dokument:**
* **Svrha:** Omogućava korisnicima da podele dokument na odvojene delove, uklanjajući ili izolujući stranice koje nisu potrebne.
* **Upotreba:** Idealno kada se radi sa više-straničnim dokumentima gde su potrebni samo određeni delovi za obradu ili pregled.

### **Unapredi dokument:**

* Dokument će biti restartovan
* **Unapredi dokument:**
* **Svrha:** Resetuje dokument na početno stanje radi ponovne evaluacije ili daljih modifikacija.
* **Upotreba:** Korisno kada je potrebno poništiti početne modifikacije ili osvežiti dokument za još jedan krug izmena. Ovde nam je potrebna dodatna ML vizija da unapredimo kvalitet dokumenta.&#x20;

### **Tok dokumenata:**

Ovde ćete pronaći tok dokumenta

* **Svrha:** Prikazuje sekvencu i napredovanje obrade dokumenata unutar sistema.
* **Upotreba:** Pomaže u praćenju statusa dokumenata kroz različite faze, osiguravajući da su svi neophodni koraci obrade ispoštovani.

### **Idi na šablon rasporeda:**

* Sa ovom opcijom bićete preusmereni i moći ćete da uređujete svoj raspored ili koristite podrazumevani šablon
* **Idi na Šablon Rasporeda:**
* **Svrha:** Preusmerava korisnike na uređivač rasporeda gde mogu modifikovati postojeće šablone ili primeniti podrazumevani.
* **Upotreba:** Omogućava prilagođavanje rasporeda dokumenata kako bi se ispunile specifične poslovne potrebe ili preferencije, poboljšavajući vizuelni i funkcionalni sklad dokumenata sa standardima kompanije.

### **Obavezna polja:**

<figure><img src="../.gitbook/assets/Bildschirmfoto 2024-05-10 um 09.41.08.png" alt=""><figcaption></figcaption></figure>

Postoje polja koja su obavezna za dalje uređivanje, ova polja se mogu urediti u postavkama.

Koristite tooltip da saznate da li:&#x20;

* Da li je polje obavezno (required)
* Potrebna validacija&#x20;
* Niska sigurnost
* Neusklađenost sa punim iznosom poreza
* **Obavezna polja:**
* **Svrha:** Identifikuje obavezna polja unutar dokumenata koja moraju biti popunjena ili ispravljena pre dalje obrade.
* **Upotreba:** Osigurava da se bitni podaci tačno unose, održavajući integritet podataka i usklađenost sa poslovnim pravilima.

### **Idi na prikaz ekstrakcije tabele:**

<figure><img src="../.gitbook/assets/Bildschirmfoto 2024-05-10 um 11.35.37.png" alt=""><figcaption></figcaption></figure>

Ovde dolazite do prikaza ekstrakcije tabele i imate dalje opcije za nastavak. Na primer, u režimu obuke, učenje tabele.

* **Idi na Prikaz Ekstrakcije Tabele:**
* **Svrha:** Navigira korisnike ka interfejsu gde mogu ekstrahovati i manipulisati podacima tabele iz dokumenata.
* **Upotreba:** Korisno za kompleksne dokumente koji sadrže tabele, omogućavajući preciznu ekstrakciju podataka i učenje za poboljšanje prepoznavanja tokom vremena.

### **Dodaj nepridružene kolone:**

<figure><img src="../.gitbook/assets/Bildschirmfoto 2024-05-10 um 11.35.49.png" alt=""><figcaption></figcaption></figure>

Za dodavanje nepridruženih kolona kliknite ovde i izaberite kolone koje želite u tabeli ili uklonite one koje vam nisu potrebne.

<figure><img src="../.gitbook/assets/image (37).png" alt="" width="375"><figcaption></figcaption></figure>

### **Prikaži/ne prikazuj nepridružene kolone:**

<figure><img src="../.gitbook/assets/Bildschirmfoto 2024-05-10 um 11.35.58.png" alt=""><figcaption></figcaption></figure>

* **Prikaži/Ne prikazuj Nepridružene Kolone:**
* **Svrha:** Menja vidljivost kolona u tabeli koje nisu automatski povezane sa poznatim poljima.
* **Upotreba:** Omogućava korisnicima da se fokusiraju na relevantne podatke sakrivanjem nepotrebnih kolona ili pregledom radi potencijalnog uključivanja.

<figure><img src="../.gitbook/assets/image (38).png" alt=""><figcaption></figcaption></figure>

### **Blokiraj ekstrakciju tabele za ovog dobavljača:**

<figure><img src="../.gitbook/assets/Bildschirmfoto 2024-05-10 um 11.36.06.png" alt=""><figcaption></figcaption></figure>

* **Blokiraj Ekstrakciju Tabele za Ovog Dobavljača:**
* **Svrha:** Onemogućava procese ekstrakcije tabele za dokumente određenih dobavljača.
* **Upotreba:** Korisno u scenarijima gde dokumenti dobavljača konstantno ne uspevaju da se ispravno ekstraktuju ili ne zahtevaju ekstrakciju.

### **Obriši tabelu:**

<figure><img src="../.gitbook/assets/Bildschirmfoto 2024-05-10 um 11.36.14.png" alt=""><figcaption></figcaption></figure>

* **Obriši Tabelu:**
* **Svrha:** Uklanja celu tabelu iz dokumenta.
* **Upotreba:** Korisno kada je tabela pogrešno uključena ili više nije potrebna za svrhu dokumenta.

### **Dodaj novu kolonu tabele:**

<figure><img src="../.gitbook/assets/Bildschirmfoto 2024-05-10 um 11.36.21.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (36).png" alt="" width="375"><figcaption></figcaption></figure>

Ako nedostaje kolona, možete kreirati novu kolonu ovde. Navedite naslov, odlučite da li treba da bude obavezno polje i tip kolone (ovo je važno za ispravan format)

* **Dodaj Novu Kolonu Tabele:**
* **Svrha:** Kreira novu kolonu u postojećoj tabeli, sa specifikacijama za naslov, obaveznoću i tip.
* **Upotreba:** Poboljšava fleksibilnost i tačnost prikupljanja podataka omogućavajući kreiranje prilagođenih kolona prilagođenih specifičnim zahtevima podataka.



### **Ignoriši validaciju tabele:**

<figure><img src="../.gitbook/assets/Bildschirmfoto 2024-05-10 um 11.36.29.png" alt=""><figcaption></figcaption></figure>

* **Ignoriši Validaciju Tabele:**
* **Svrha:** Omogućava korisnicima da zaobiđu pravila validacije za određene tabele.
* **Upotreba:** Korisno kada poznate anomalije u podacima ne utiču na celokupnu obradu i insistiranje na validaciji bi ometalo radni tok.

### **Obnovi kolonu tabele:**

<figure><img src="../.gitbook/assets/Bildschirmfoto 2024-05-10 um 11.36.37.png" alt=""><figcaption></figcaption></figure>

* **Obnovi Kolonu Tabele:**
* **Svrha:** Vraća prethodno obrisane ili izmenjene kolone u tabeli.
* **Upotreba:** Korisno za vraćanje podataka koji su greškom uklonjeni ili izmenjeni, osiguravajući potpunost podataka.
