# Dodela putem barkoda

### Pregled

Podešavanje **Dodela putem barkoda** (Barcode Assignment) dodaje alatku za barkodove na **ekran za validaciju dokumenata**. Ona čita barkodove i QR kodove pronađene u dokumentu i omogućava vam da **njihove vrednosti dodelite poljima dokumenta** — na primer, da popunite referentni broj, broj narudžbine ili otpremnice iz barkoda umesto da ga kucate.

Ovo podešavanje je **podrazumevano isključeno**.

### Šta radi?

Kada je ovo podešavanje uključeno, tokom validacije dokumenta na traci sa alatkama se pojavljuje malo **dugme za barkod** (ikona QR koda). Klik na njega prikazuje barkodove koje je DocBits pronašao u dokumentu, a vi možete da svaki od njih povežete sa poljem. Polje se zatim popunjava vrednošću pročitanom iz barkoda.

* **Uključeno** — Dugme za barkod se prikazuje na ekranu za validaciju. Možete da čitate barkodove u dokumentu i da njihove vrednosti dodeljujete poljima.
* **Isključeno** — Dugme je skriveno i vrednosti barkodova se ne nude za dodelu tokom validacije.

{% hint style="info" %}
**Ovo služi za čitanje vrednosti barkoda/QR koda i njeno dodeljivanje polju tokom validacije.** Automatsko izvlačenje strukturiranih podataka iz platnih kodova (kao što su Swiss QR Bill ili GiroCode) — kao i deljenje višestranične datoteke na stranicama razdvajačima sa barkodom — obrađuje **drugo** podešavanje: **Bar-Code / QR Code Extraction**.
{% endhint %}

### Prednosti

* **Brži unos bez grešaka**: Uzmite vrednosti direktno iz barkoda umesto da ih čitate i kucate ručno.
* **Manje grešaka u kucanju**: Skenirana vrednost je tačno ono što je kodirano u barkodu.
* **Vi zadržavate kontrolu**: Vi odlučujete koji barkod ide u koje polje tokom validacije.

### Kako se koristi

1. Idite na **Podešavanja**.
2. Izaberite **Obrada dokumenata**.
3. Izaberite **Modul**.
4. Otvorite odeljak **Tip dokumenta**.
5. Pronađite **Dodela putem barkoda** i uključite prekidač.
6. Zatim, tokom validacije dokumenta, kliknite na **dugme za barkod** na traci sa alatkama i dodelite otkrivene vrednosti barkodova odgovarajućim poljima.

### Kada koristiti ovu funkciju

* **Dokumenti sa barkodovima**: Kada vaši dokumenti sadrže barkodove/QR kodove čije vrednosti pripadaju određenim poljima (npr. brojevi narudžbine ili referentni brojevi).
* **Tokovi ručne validacije**: Kada osoba pregleda dokumente i želi brzo da popuni polja iz barkodova.
* **Ostavite isključeno** ako vaši dokumenti nemaju upotrebljive barkodove ili ako vam je potrebno samo automatsko **izvlačenje** barkodova/QR kodova.
