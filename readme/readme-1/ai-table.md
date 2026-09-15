# Tabela veštačke inteligencije

AI ekstrahovana tabela je tabela stavki koju DocBits čita pomoću veštačke inteligencije kada dobavljač nema obučena pravila za tabelu. Pojavljuje se na ekranu za validaciju ispod polja zaglavlja. Ova stranica objašnjava kada je dobijate, kako da je ponovo pokrenete i kako da oblikujete ono što ona ekstrahuje.

## Kada dobijate AI tabelu

* Administrator je uključio **AI ekstrakciju tabela** (Podešavanja → Obrada dokumenata → Klasifikacija i ekstrakcija). Ako je isključena, oblast tabele prikazuje *AI Table will display here. Enable in …*.
* Dobavljač **nema sačuvana pravila**. Čim neko obuči tabelu dobavljača i klikne na *Save Rules*, sačuvana pravila zamenjuju AI tabelu za tog dobavljača; redovi se tada pojavljuju na kartici *Ekstrahovana tabela* umesto na kartici *AI ekstrahovana tabela*.
* Izuzetak: kolone označene sa **Koristi AI** u podešavanjima kolona tabele popunjava AI čak i kod dobavljača sa sačuvanim pravilima, pogledajte [Koristi AI po koloni](#koristi-ai-po-koloni).

Koji AI nivo čita tabelu (Fast, Full, Nexus) podešava se po organizaciji i može se zameniti po dobavljaču pod *Više postavki* na ekranu za validaciju (AI model specifičan za dobavljača).

## Ponovna ekstrakcija AI tabele

Koristite ovo kada nedostaju redovi ili je kolona pomerena, a želite da AI pokuša ponovo, na primer nakon dodavanja oznake (tag):

1. Dodajte ili izmenite oznake u polju ispod tabele i kliknite na **Primeni**. AI ponovo gradi tabelu za ovaj dokument sa vašim oznakama i izmenama kolona; za dobavljača se još ništa ne čuva. Ako dokument ima stavke uparene sa narudžbenicom, DocBits upozorava da ponovna izgradnja uklanja uparivanja.
2. Zadovoljni ste rezultatom? Kliknite na **Sačuvaj** (*Save Rules*) da bi sledeći dokument ovog dobavljača bio ekstrahovan na isti način.
3. Da biste počeli iznova, kliknite na **Obriši** (*Delete Rules*): DocBits potvrđuje sa *Rules has been deleted successfully* i ponovo pokreće AI ekstrakciju bez ikakvih sačuvanih oznaka ili formatiranja.

*Delete Rules* uklanja oznake i pravila formatiranja sačuvana za ovog dobavljača, a ne konfiguraciju kolona tabele. Da biste ponovo ekstrahovali ceo dokument (zaglavlje i tabelu) nakon što je administrator promenio podešavanja ili kolone, umesto toga koristite *Ponovo pokreni* u meniju dokumenta na kontrolnoj tabli.

## Koristi AI po koloni

Svaka kolona tabele ima oznaku **Koristi AI** (Podešavanja → Globalna podešavanja → Tipovi dokumenata → [Kolone tabele](../admin-section/settings/global-settings/document-types/table-columns.md)). Kada je oznaka uključena, AI popunjava tu kolonu čak i kada dobavljač ima sačuvana pravila; ostale kolone i dalje dolaze iz pravila. Tipična upotreba: kolona sa opisom u slobodnom tekstu koju obučena pravila loše prepoznaju, ili vrednost koja menja mesto na stranici.

Imajte u vidu da AI tada pogađa tu kolonu iz celog reda. Ako u nju dosledno stavlja pogrešnu vrednost (na primer ukupan iznos stavke u *Troškove*), provera ukupnog iznosa stavke ne prolazi ni u jednom redu. U tom slučaju isključite *Koristi AI* za tu kolonu ili dodajte oznaku koja AI-ju govori šta je ta kolona.

## Strukturirana ekstrakcija

Kada je u podešavanjima organizacije uključeno **Koristi strukturiranu ekstrakciju (AI)**, AI vraća tabelu u fiksnoj strukturi koja se direktno mapira na konfigurisane kolone tabele, umesto da kopira zaglavlja kolona dobavljača. Nazivi kolona tada uvek odgovaraju vašoj konfiguraciji; kolona koju dobavljač štampa, a vi je niste konfigurisali, ne ekstrahuje se. Zamolite administratora da je uključi kada zaglavlja dobavljača znatno variraju i trošite vreme na ponovno mapiranje.

## Rad sa ekstrahovanom tabelom

Evo ključnih mogućnosti i uputstava za korišćenje:

* **Brisanje Kolona**: Ako određene kolone u izvučenoj tabeli nisu potrebne, korisnici ih mogu lako ukloniti klikom na ikonu "Obriši kolonu" (predstavljenu sa tri vertikalne tačke) pored zaglavlja kolone. Ovo pomaže da se tabela sredi i fokusira samo na relevantne informacije.

<figure><img src="../.gitbook/assets/Bildschirmfoto 2024-05-08 um 20.48.56 (1).png" alt=""><figcaption></figcaption></figure>

* **Promena Formata Valute**: Format valute može biti promenjen izborom željenog formata iz padajućeg menija pored polja "Valuta". Ovo osigurava da vrednosti valute budu prikazane u željenom formatu, olakšavajući tumačenje i analizu finansijskih podataka.

<figure><img src="../.gitbook/assets/Bildschirmfoto 2024-05-08 um 20.49.15 (2).png" alt=""><figcaption></figcaption></figure>

* **Prikazivanje/Skrivanje Nemapiranih Kolona**: Podrazumevano, samo mapirane kolone (kolone sa izvučenim podacima) su vidljive u tabeli. Međutim, korisnici mogu odabrati da prikažu ili sakriju nemapirane kolone klikom na dugme "Sakrij nemapirane kolone" ili "Prikaži nemapirane kolone" na dnu tabele. Ova funkcija je korisna kada korisnici žele da pregledaju sve dostupne kolone, čak i ako trenutno ne sadrže podatke.

<figure><img src="../.gitbook/assets/Bildschirmfoto 2024-05-08 um 20.49.26 (2).png" alt=""><figcaption></figcaption></figure>

* **Menjanje Zaglavlja Tabele**: Zaglavlja tabele (nazivi kolona) mogu biti izmenjeni klikom na zaglavlje i unošenjem željenog imena. Ova funkcija omogućava korisnicima da prilagode nazive kolona kako bi se bolje uskladili sa njihovom terminologijom ili preferencijama, čineći podatke čitljivijim i razumljivijim.

<figure><img src="../.gitbook/assets/Bildschirmfoto 2024-05-08 um 20.48.43.png" alt=""><figcaption></figcaption></figure>

* **Čuvanje izmena**: **Sačuvaj** pored oznaka (opis alatke *Save Rules*) čuva trenutno mapiranje kolona, skrivene kolone i oznake za ovog dobavljača. Sledeći dokument tog dobavljača ekstrahuje se sa njima.

Ove funkcije vam daju kontrolu nad ekstrahovanim podacima. Kada isti dobavljač svaki put zahteva iste ispravke, umesto toga jednom obučite tabelu, pogledajte [Obuka polja stavki / obuka tabele](../setup/document-training/training-line-fields-table-training/README.md), i AI tabela se više ne koristi za tog dobavljača.
