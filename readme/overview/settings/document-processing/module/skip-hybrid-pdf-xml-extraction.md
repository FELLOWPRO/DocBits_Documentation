# Preskoči hibridnu ekstrakciju XML iz PDF-a

### Pregled

Podešavanje **Preskoči hibridnu ekstrakciju XML iz PDF-a** (Skip Hybrid PDF XML Extraction) kontroliše kako DocBits obrađuje **hibridne PDF-ove** — PDF fakture koje sadrže ugrađenu strukturiranu e-fakturu (ZUGFeRD / Factur-X). Ono odlučuje da li je **strukturirani XML unutar PDF-a** vodeći dokument za automatsku obradu, ili se **sam PDF** obrađuje putem OCR-a kao primarni dokument.

Ovo podešavanje je posebno važno za **klijente iz SAD-a**. Za razliku od EU/Nemačke, Sjedinjene Države nemaju opštu B2B obavezu e-fakturisanja, pa organizacije iz SAD-a obično žele da se PDF tretira kao primarna, ljudima čitljiva faktura — čak i kada druga strana pošalje ZUGFeRD/Factur-X datoteku sa ugrađenim XML-om.

### Šta radi?

ZUGFeRD/Factur-X datoteka je jedan PDF koji takođe sadrži mašinski čitljivu XML fakturu. Podrazumevano DocBits detektuje taj ugrađeni XML i koristi ga kao vodeći izvor za ekstrakciju (strukturirana elektronska putanja).

* **Onemogućeno (podrazumevano)** — DocBits detektuje ugrađeni XML e-fakture i obrađuje dokument na **strukturiranoj elektronskoj putanji**. XML je vodeća faktura. Ovo je pravno ispravno ponašanje za EU/Nemačku, gde je strukturirana e-faktura relevantna faktura, a PDF je samo vizuelizacija / čitljiva kopija.
* **Omogućeno** — DocBits **ignoriše ugrađeni XML** i usmerava dokument na **PDF procesor (OCR)**. PDF postaje primarni dokument za obradu. Ovo je tipičan izbor za **organizacije iz SAD-a** koje žele obradu zasnovanu na PDF-u.

{% hint style="info" %}
Ovo podešavanje utiče samo na **hibridne PDF-ove** (ZUGFeRD / Factur-X = `.pdf` sa ugrađenim XML-om). Čista XRechnung/EDI datoteka otpremljena kao `.xml` uvek se obrađuje na strukturiranoj elektronskoj putanji — ne postoji PDF koji bi mogao da postane primarni dokument.
{% endhint %}

### Revizija i usklađenost — original se uvek čuva

Omogućavanje ovog podešavanja **ne odbacuje** e-fakturu. Originalni artefakt se uvek čuva:

* Originalni ZUGFeRD/Factur-X **PDF — uključujući njegov ugrađeni XML — ostaje sačuvan** i dostupan za preuzimanje. Ništa se ne briše iz sačuvane kopije dokumenta.
* Obrada menja samo **koji sadržaj pokreće ekstrakciju** (PDF/OCR naspram ugrađenog XML-a), a ne ono što se arhivira.

Tako organizacija iz SAD-a može da obrađuje PDF kao primarni, dok strukturirana e-faktura ostaje dostupna za reviziju.

{% hint style="warning" %}
Za organizacije iz EU/Nemačke ostavite ovo podešavanje **onemogućeno**. Prema pravilima o e-fakturisanju iz 2025, strukturirana e-faktura (ZUGFeRD/Factur-X, XRechnung) je pravno relevantna faktura; običan PDF je samo čitljiva kopija. Obrada PDF-a kao primarnog umesto strukturiranih podataka nije prikladna kada postoji važeća e-faktura.
{% endhint %}

### Kako se koristi

1. **Otvorite podešavanje**:
   * Idite na **Podešavanja**.
   * Izaberite **Obrada dokumenata**.
   * Izaberite **Modul**.
   * Otvorite odeljak **Tip dokumenta**.
   * Pronađite **Preskoči hibridnu ekstrakciju XML iz PDF-a** i uključite prekidač.
2. **Izaberite režim**:
   * **Organizacije iz SAD-a / PDF-orijentisane** → uključite prekidač da bi se ZUGFeRD/Factur-X PDF-ovi obrađivali putem OCR-a kao primarni dokument.
   * **Organizacije iz EU/Nemačke** → ostavite prekidač isključen da bi strukturirana e-faktura ostala vodeći dokument.
3. **Proverite**:
   * Otpremite ZUGFeRD/Factur-X PDF i proverite rezultat obrade — sa uključenim prekidačem tretira se kao običan PDF (OCR); sa isključenim, izvlače se ugrađeni podaci e-fakture.

### Kada koristiti ovu funkciju

* **Klijenti iz SAD-a / bez obaveze e-fakture**: uključite je da bi poznati PDF bio primarni dokument za obradu, dok ugrađena e-faktura ostaje arhivirana.
* **Mešoviti / PDF-orijentisani tokovi rada**: uključite je kada se naredni procesi, validacija ili pregled oslanjaju na izgled PDF-a umesto na XML.
* **Usklađenost EU/Nemačka**: ostavite je isključenu da bi strukturirani podaci e-fakture pokretali obradu, kako se zahteva.
