# Podešavanja Pretrage Punog Teksta

<figure><img src="../../../.gitbook/assets/fulltext_search_settings.png" alt="Podešavanja Pretrage Punog Teksta"><figcaption><p>Podešavanja Pretrage Punog Teksta — Dijalog „Potreban modul"</p></figcaption></figure>

Podešavanja Pretrage Punog Teksta kontrolišu šta DocBits indeksira i kako taj sadržaj postaje pretraživ kroz dokumente, ERP master podatke i šablone. Stranica podešavanja otvara se samo kada je **modul Pretrage Punog Teksta** uključen — pogledajte [Pretragu Punog Teksta](../document-processing/module/fulltext-search.md) za korisnički jezik upita.

## Preduslovi

Modul Pretrage Punog Teksta mora biti aktiviran u **Podešavanja → Obrada Dokumenata → Modul → Kontrolne table → Pretraga punog teksta**. Ako modul nije uključen, dijalog vam predlaže:

* **Idite u Module** — Otvorite stranicu konfiguracije Modula da pregledate podešavanja.
* **Uključite odmah** — Aktivirajte modul Pretrage Punog Teksta direktno (pokreće DocSearch pretplatu).

Sama stranica podešavanja postaje dostupna kada je modul aktivan.

## Raspored stranice

Stranica podešavanja organizovana je u tri kartice, od kojih svaka pokriva različit tip sadržaja koji Pretraga Punog Teksta može da indeksira.

### Kartica „Dokumenti"

Kartica Dokumenti pokriva sve u vezi sa indeksiranjem obrađenih dokumenata:

* **Statistika indeksiranja** — ukupni brojevi indeksiranih i dokumenata na čekanju, osvežavi po zahtevu.
* **Vektorske preferencije** — tri prekidača na nivou organizacije koji odlučuju da li vektorska indeksacija radi paralelno sa tekstualnim indeksom za dokumente. Vektorska indeksacija pokreće režim upita `vector:` i funkciju „Pronađi slično".
* **Akcije reindeksiranja** — pokrenite kompletnu ili inkrementalnu reindeksaciju. Dok reindeksacija traje, vidite napredak uživo (dokumenti u minuti, procenjeno preostalo vreme), trenutni status toka i poslednju grešku (ako je bilo).
* **Dijagnostika sinhronizacije** — dijagnostika po zahtevu za slučajeve kada indeks deluje desinhronizovano u odnosu na osnovno skladište dokumenata.

<mark>Reindeksacija nije destruktivna — postojeća pretraga nastavlja da radi dok se novi indeks gradi.</mark>

### Kartica „ERP"

Kartica ERP kontroliše indeksiranje ERP master podataka — dobavljača, klijenata, artikala i sličnih entiteta. Svaki entitet ima sopstveni prekidač:

* **Indeksiranje** — tekstualno indeksira entitet tako da je pretraživ sa kontrolne table.
* **Vektor** — vektorski indeksira entitet kako bi mogao biti pronađen semantičkim upitima.

Koristite akciju **Prebaci sve** na vrhu liste da primenite isti uključeno/isključeno stanje na sve entitete odjednom. Indeksiranje se pokreće u pozadini; indikator u svakom redu pokazuje kada je u toku.

### Kartica „Šabloni"

Kartica Šabloni navodi verzije šablona poznate indeksu Punog Teksta. Koristite ovaj prikaz da nakon ponovnog uvođenja potvrdite da su verzije šablona od kojih zavisite prisutne u indeksu.

## Šta se indeksira

Kada se uključi i konfiguriše, Pretraga Punog Teksta omogućava korisnicima:

* Pretraživanje kroz celokupan sadržaj dokumenta (ne samo polja metapodataka).
* Pronalaženje dokumenata po tekstu sadržanom u otpremljenim fajlovima.
* Korišćenje naprednih operatora pretrage za precizne upite.
* Pristup rezultatima pretrage direktno sa kontrolne table.
* Korišćenje semantičke pretrage (prefiks `vector:`) kada je vektorska indeksacija uključena za taj tip sadržaja.

Kompletnu referencu jezika upita — uključujući upite po opsegu, pametne filtere i režim pretrage sa AI — pogledajte na stranici modula [Pretraga Punog Teksta](../document-processing/module/fulltext-search.md).
