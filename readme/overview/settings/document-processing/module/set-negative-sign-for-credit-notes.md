# Postavi negativan predznak za knjižna odobrenja

### Pregled

Podešavanje **Postavi negativan predznak za knjižna odobrenja** (Set Negative Sign for Credit Notes) obezbeđuje da se **knjižna odobrenja** (kreditne note) čuvaju sa **negativnim iznosima**. Knjižno odobrenje storna ili refundira deo fakture, pa bi u računovodstvu njegove vrednosti trebalo da umanjuju ukupne iznose — odnosno da budu negativne. Kada je ovo podešavanje uključeno, DocBits automatski primenjuje taj negativan predznak.

Ovo podešavanje je **podrazumevano uključeno**.

### Šta radi?

Kada se dokument prepozna kao **knjižno odobrenje**, DocBits tokom obrade automatski pretvara njegove iznose u negativne vrednosti. Ovo se odnosi na novčana polja, uključujući neto iznose, iznose poreza i ukupne iznose (na primer neto iznos, iznos poreza, ukupan iznos poreza, ukupan neto iznos i ukupan iznos).

* **Uključeno (podrazumevano)** — Iznosi knjižnih odobrenja se čuvaju kao negativne vrednosti (na primer, `150,00` postaje `-150,00`). Obične fakture nisu zahvaćene.
* **Isključeno** — Iznosi ostaju tačno onakvi kakvi su pročitani iz dokumenta, bez promene predznaka.

{% hint style="info" %}
Ovo važi samo za dokumente identifikovane kao **knjižna odobrenja**. Obične fakture uvek ostaju nepromenjene.
{% endhint %}

### Prednosti

* **Ispravno knjigovodstvo**: Knjižna odobrenja umanjuju salda, pa su negativne vrednosti ono što vaši računovodstveni i ERP sistemi očekuju.
* **Bez ručnog uređivanja**: Vaš tim ne mora ručno da menja predznak za svako knjižno odobrenje.
* **Doslednost**: Svako knjižno odobrenje se obrađuje na isti način u celoj organizaciji.

### Kako se koristi

1. Idite na **Podešavanja**.
2. Izaberite **Obrada dokumenata**.
3. Izaberite **Modul**.
4. Otvorite odeljak **Tip dokumenta**.
5. Pronađite **Postavi negativan predznak za knjižna odobrenja** i uključite ili isključite prekidač.

### Kada koristiti ovu funkciju

* **Ostavite uključeno** ako vaš računovodstveni ili ERP sistem očekuje da knjižna odobrenja stignu sa negativnim iznosima (ovo je najčešća konfiguracija).
* **Isključite** je samo ako vaš sistem nizvodno već sam obrađuje predznak ili očekuje da iznosi knjižnih odobrenja ostanu pozitivni.
