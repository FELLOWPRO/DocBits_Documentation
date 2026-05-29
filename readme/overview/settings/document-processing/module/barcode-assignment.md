# Dodela putem barkoda

### Pregled

Podešavanje **Dodela putem barkoda** (Barcode Assignment) omogućava DocBits-u da koristi **barkodove unutar datoteke kako bi je razdvojio na pojedinačne dokumente**. Ovo je korisno kada se više dokumenata skenira zajedno u jedan veliki PDF, a barkod označava gde se jedan dokument završava, a sledeći počinje.

Ovo podešavanje je **podrazumevano isključeno**.

### Šta radi?

Kada je ovo podešavanje uključeno, DocBits traži barkodove u dolaznoj višestraničnoj datoteci i deli je na zasebne dokumente na označenim pozicijama. Svaki dobijeni dokument se zatim obrađuje pojedinačno.

* **Uključeno** — DocBits detektuje barkodove i automatski razdvaja kombinovanu datoteku na pojedinačne dokumente na osnovu njih.
* **Isključeno** — Datoteka se obrađuje kao jedan dokument; barkodovi se ne koriste za njeno deljenje.

{% hint style="info" %}
Ovde je reč o **deljenju i dodeli** stranica na osnovu barkodova. Čitanje podataka kodiranih u barkodu (na primer za platne QR kodove) obrađuje se zasebno u odeljku **Bar-Code / QR Code Extraction**.
{% endhint %}

### Prednosti

* **Brže grupno skeniranje**: Skenirajte celu gomilu dokumenata u jednom prolazu, razdvojenih listovima sa barkodom, umesto da skenirate svaki dokument pojedinačno.
* **Manje ručnog razvrstavanja**: DocBits kreira pojedinačne dokumente umesto vas, pa niko ne mora ručno da deli PDF.
* **Manje grešaka**: Dokumenti se svaki put razdvajaju tačno na označenim pozicijama.

### Kako se koristi

1. Idite na **Podešavanja**.
2. Izaberite **Obrada dokumenata**.
3. Izaberite **Modul**.
4. Otvorite odeljak **Tip dokumenta**.
5. Pronađite **Dodela putem barkoda** i uključite prekidač.

### Kada koristiti ovu funkciju

* **Skeniranje velikog obima**: Kada skenirate mnogo dokumenata zajedno i između njih koristite listove razdvajače sa barkodom.
* **Mešovite grupe**: Kada jedna dolazna datoteka sadrži više različitih dokumenata koji moraju da se obrade zasebno.
* **Ostavite isključeno** ako vaši dokumenti uvek stižu kao zasebne datoteke — deljenje tada nije potrebno.
