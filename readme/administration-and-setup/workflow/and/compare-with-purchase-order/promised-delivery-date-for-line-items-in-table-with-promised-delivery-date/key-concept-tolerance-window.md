# Key Concept: Tolerance Window

Pre nego što pogledamo operatore, važno je razumeti kako se izračunava prozor tolerancije.

## Šta je prozor tolerancije?

Prozor tolerancije definiše opseg prihvatljivih datuma oko obećanog datuma isporuke iz naloga za nabavku.

**Primer:**

* Datum naloga za nabavku: **9. januar**
* Dani tolerancije: **3**
* Prozor tolerancije: **6. januar → 12. januar**

> <mark style="color:red;">Samo izabrani</mark> <mark style="color:red;"></mark><mark style="color:red;">**Allowed Tolerance Days**</mark> <mark style="color:red;"></mark><mark style="color:red;">(radni dani) se računaju pri izračunavanju ovog prozora.</mark>

### Primer vizuelne vremenske ose

```
← Past                           Future →
|-----|-----|-----|-----|-----|-----|-----|
     6 Jan      9 Jan      12 Jan
   (Start)    (PO Date)     (End)
```

### Ponašanje operatora objašnjeno primerima

* **Equals (=)**
  * **Značenje:**\
    Datum isporuke stavke mora pasti _unutar_ prozora tolerancije.
  * **Validni datumi:**
    * Bilo koji datum između **6. jan i 12. jan** (uključujući)
  * **Nevalidni datumi:**
    * Bilo koji datum **pre 6. jan**
    * Bilo koji datum **posle 12. jan**
* **Not Equals (≠)**
  * **Značenje:**\
    Datum isporuke stavke mora pasti _izvan_ prozora tolerancije.
  * **Validni datumi:**
    * Bilo koji datum **pre 6. jan**
    * Bilo koji datum **posle 12. jan**
  * **Nevalidni datumi:**
    * Datumi između **6. jan i 12. jan**
* **Greater or Equals (≥)**
  * **Značenje:**\
    Datum isporuke stavke mora biti na ili posle **početka prozora tolerancije**.
  * **Validni datumi:**
    * **6. jan → bilo koji budući datum**
  * **Nevalidni datumi:**
    * Bilo koji datum **pre 6. jan**
  * <mark style="color:red;">**Važno:**</mark>\
    Ovaj operator dozvoljava datume _unutar_ prozora tolerancije **i izvan njega**.
* **Lesser or Equals (≤)**
  * **Značenje:**\
    Datum isporuke stavke mora biti na ili pre **kraja prozora tolerancije**.
  * **Validni datumi:**
    * Bilo koji prošli datum do **12. jan**
  * **Nevalidni datumi:**
    * Bilo koji datum **posle 12. jan**
* **Greater Than (>)**
  * **Značenje:**\
    Datum isporuke stavke mora biti _strogo posle_ prozora tolerancije.
  * **Validni datumi:**
    * **13. jan → bilo koji budući datum**
  * **Nevalidni datumi:**
    * Bilo koji datum **na ili pre 12. jan**
* **Lesser Than (<)**
  * **Značenje:**\
    Datum isporuke stavke mora biti _strogo pre_ prozora tolerancije.
  * **Validni datumi:**
    * Bilo koji datum **pre 6. jan**
  * **Nevalidni datumi:**
    * Bilo koji datum **na ili posle 6. jan**

## Kako "Allowed Tolerance Days" utiču na prozor tolerancije

Pri izračunavanju prozora tolerancije, **računaju se samo izabrani radni dani**.\
Dani koji nisu izabrani (kao što su vikendi ili isključeni radni dani) se **u potpunosti preskaču**

#### Primer: Izračunavanje tolerancije zasnovano na radnim danima

**Konfiguracija:**

* Datum naloga za nabavku: **sreda, 9. januar**
* Dani tolerancije: **3**
* Dozvoljeni dani tolerancije: **ponedeljak, utorak, sreda, četvrtak, petak**
* Vikendi (subota, nedelja): **nisu izabrani**

#### Izračunavanje korak po korak

Počevši od datuma naloga za nabavku (**9. jan**):

**Brojanje unazad (3 dana tolerancije):**

* Utorak, 8. jan → **Dan 1**
* Ponedeljak, 7. jan → **Dan 2**
* Nedelja, 6. jan → _Preskočeno (nije dozvoljeno)_
* Subota, 5. jan → _Preskočeno (nije dozvoljeno)_
* Petak, 4. jan → **Dan 3**

➡ **Datum početka tolerancije: petak, 4. januar**

**Brojanje unapred (3 dana tolerancije):**

* Četvrtak, 10. jan → **Dan 1**
* Petak, 11. jan → **Dan 2**
* Subota, 12. jan → _Preskočeno_
* Nedelja, 13. jan → _Preskočeno_
* Ponedeljak, 14. jan → **Dan 3**

➡ **Datum kraja tolerancije: ponedeljak, 14. januar**

#### Rezultujući prozor tolerancije

```
4 January  →  14 January
```

#### Zašto je ovo važno

Ako su Allowed Tolerance Days pogrešno konfigurisani:

* Datumi isporuke mogu izgledati **neočekivano validni ili nevalidni**
* Rane ili kasne isporuke možda neće biti ispravno otkrivene
