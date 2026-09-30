---
description: >-
  Odakle potiče vrednost polja zaglavlja i kako nastaje — objašnjenje iza
  Provere polja zaglavlja na ekranu za validaciju.
---

# Provera polja zaglavlja: odakle potiču podaci

Dugme **Provera polja zaglavlja** nalazi se pored dugmeta **Sačuvaj** na ekranu za validaciju. Otvara izveštaj *Odakle potiče svaka vrednost?*: za svako polje zaglavlja prikazuje šta je bilo na dokumentu, šta je promenilo vrednost usput, šta DocBits sada prikazuje i zašto.

Ova stranica objašnjava kako nastaje vrednost i šta znači svaki izvor. Nije potrebno stručno znanje.

{% hint style="info" %}
Provera polja zaglavlja deo je modula **Analytics**. Ako je dugme zasivljeno, administrator ga može dodeliti vašoj ulozi u **Settings › Roles**.
{% endhint %}

## Vrednost uvek nastaje ovim redosledom

| Korak | Šta se dešava |
| --- | --- |
| **1. Čitanje** | Vrednost se čita iz dokumenta — pomoću obučenog pravila, pomoću veštačke inteligencije ili direktno iz e-fakture. |
| **2. Transformacija** | Skripte i pravila transformacije klijenta menjaju pročitanu vrednost: skraćuju je, dopunjuju, prilagođavaju format. |
| **3. Pretraga** | Vrednost se traži u matičnim podacima. Ako se nešto pronađe, zapis iz matičnih podataka zamenjuje pročitanu vrednost. |
| **4. Prikaz** | Korisnik vidi samo rezultat. Šta se desilo usput, prikazuje Provera polja zaglavlja. |

Koraci 2 i 3 ne izvršavaju se uvek — ali kada se izvrše, menjaju vrednost. Upravo odatle potiče većina prijavljenih slučajeva.

## Izvori — šta znači svaki od njih

Ikone su iste kao one koje izveštaj prikazuje u koloni **Akcija** i na traci filtera na vrhu.

### Obučeno pravilo

DocBits pamti gde se polje nalazi na ovom tipu dokumenta, jer ga je neko jednom tamo označio.

* **Primer:** dobavljač „Bornemann“ — uvek na istom mestu gore levo.
* **Ako je pogrešno:** označite ispravno mesto na dokumentu i sačuvajte — pravilo uči iz toga.

### Veštačka inteligencija (AI)

Nema fiksnog obrasca. AI čita dokument kao čovek i sama odlučuje koji tekst pripada kom polju.

* **Primer:** datum fakture, iznosi, uslovi plaćanja.
* **Ako je pogrešno:** ispravite ga. Može se uključiti i isključiti u **Settings › OCR polja zaglavlja**.

### E-faktura

Kod XRechnung ili ZUGFeRD ništa se ne prepoznaje: vrednost je u dokumentu već polje podataka i preuzima se direktno.

* **Primer:** broj fakture iz XML polja pošiljaoca.
* **Ako je pogrešno:** greška je kod pošiljaoca. DocBits tačno prikazuje iz kog XML polja vrednost potiče.

### Skripta / pravilo transformacije

Nakon čitanja, logika klijenta preuzima i preoblikuje vrednost. Dokument ostaje isti — vrednost ne.

* **Primer:** `1001 / LS 206776` postaje `1001`.
* **Ako je pogrešno:** ne tražite na dokumentu. Proverite **Settings › Skripte** ili **Pravila transformacije**.

### Matični podaci

Pročitana vrednost traži se u vašim sopstvenim podacima — narudžbenice, dobavljači. Poklapanje zamenjuje vrednost i povlači sa sobom dodatna polja.

* **Primer:** `1001` pronalazi narudžbenicu `06O051001` — a dobavljač i kupac tada takođe dolaze odatle.
* **Ako je pogrešno:** proverite **Settings › Lookup konfiguracija**. Tamo piše da li je pretraga tačna ili prihvata i delimična poklapanja.

### Izračunato

Nije pročitano, već izračunato iz drugih polja.

* **Primer:** datum dospeća iz datuma fakture plus uslovi plaćanja.
* **Ako je pogrešno:** obično je pogrešno neko od polja iz kojih se računa.

### Barkod

Pročitano iz barkoda ili QR koda na dokumentu.

* **Primer:** broj fakture je kodiran u QR kodu.
* **Ako je pogrešno:** proverite podešavanja barkoda za tip dokumenta.

## Ono što se najčešće pogrešno razume

{% hint style="warning" %}
Kada polje iznenada sadrži vrednost koja se tako ne pojavljuje na dokumentu, to skoro nikada nije bila AI — već korak 2 ili korak 3. Najčešće je to poklapanje u matičnim podacima, koje prihvata i delimična poklapanja: `1001` se poklapa sa `06O051001`, a uz pronađenu narudžbenicu menja se i dobavljač.
{% endhint %}

U izveštaju je takvo polje označeno crveno. Kolona **Akcija** prikazuje zapis iz matičnih podataka zajedno sa crvenim čipom *samo delimično poklapanje*, a deo vrednosti koji se poklapa je istaknut.

## Kako čitati izveštaj

* **Statusni čipovi** na vrhu broje polja koja su došla nepromenjena iz dokumenta, promenjena usput ili se na dokumentu ne nalaze u prikazanom obliku. Kliknite na čip da prikažete samo ta polja; kliknite ponovo da prikažete sva.
* **Filter izvora:** red ikona prikazuje svaki metod ekstrakcije. Kliknite na jednu da prikažete samo polja koja su prošla kroz nju.
* **Akcija:** svaki korak kroz koji je vrednost prošla, sa ikonom njenog izvora. Korak iz kog potiče trenutna vrednost je istaknut. Zadržite pokazivač da vidite šta je svaki korak uradio, iz koje vrednosti u koju.
* **Razlog:** status polja. Ikona (i) objašnjava zašto je vrednost takva kakva jeste. Ako piše *Polje nije postojalo*, polja nije bilo na dokumentu.
* Duge vrednosti se skraćuju sa … — zadržite pokazivač da vidite punu vrednost.
