# Confirmed Delivery Date

<figure><img src="../../../../.gitbook/assets/image (266).png" alt="" width="563"><figcaption></figcaption></figure>

## **Svrha**

Ova kartica radnog toka je dizajnirana da proveri da li su potvrđeni datumi isporuke na fakturama ili otpremnim dokumentima usklađeni sa prihvaćenim datumima isporuke definisanim u tabeli za pretragu matičnih podataka. Poređenjem ovih datuma, ona pomaže da se obezbedi usklađenost sa dogovorenim rasporedima isporuke i poboljša pouzdanost lanca snabdevanja.

## **Komponente kartice**

1. **Operator**
   * **Opis:** Definiše uslov za poređenje potvrđenog datuma isporuke sa prihvaćenim datumom isporuke.
   * **Opcije:**
     * **Is:** Potvrđuje da se datum isporuke poklapa sa prihvaćenim datumom isporuke u matičnim podacima.
     * **Is Not:** Obezbeđuje da se datum isporuke ne poklapa sa prihvaćenim datumom isporuke u matičnim podacima.
2. **Pretraga tabele matičnih podataka**
   * **Opis:** Navodi referentnu tabelu koja sadrži prihvaćene datume isporuke za poređenje.
   * **Detalj:** Tabela je definisana parametrom **Master Data Table** i može uključivati dodatne metapodatke kao što su brojevi porudžbina ili regioni isporuke.



## **Funkcionalnost**

* **Poređenje datuma:** Sistem upoređuje potvrđeni datum isporuke iz fakture ili otpremnog dokumenta sa prihvaćenim datumom isporuke u navedenoj tabeli za pretragu matičnih podataka.
* **Izvršavanje akcije:** Na osnovu rezultata poređenja, kartica može pokrenuti naredne akcije kao što su obaveštenja.

## **Podešavanje i konfiguracija**

* Da bi konfigurisali ovu karticu, korisnici biraju polje koje predstavlja potvrđeni datum isporuke u dokumentu i navode tabelu za pretragu matičnih podataka koja sadrži prihvaćene datume isporuke. Operator se zatim bira da definiše kako treba upoređivati dva datuma (npr. **Is** ili **Is Not**).

## **Primer scenarija**

* Faktura navodi potvrđeni datum isporuke 10. juna, dok tabela za pretragu matičnih podataka navodi prihvaćeni datum isporuke 15. juna. Koristeći operator **Is Not**, kartica označava nepodudaranje za pregled, omogućavajući logističkom timu da istraži uzrok i u skladu sa tim prilagodi rasporede.

## **Zaključak**

Kartica radnog toka **"Confirmed Delivery Date vs. Accepted Delivery Date"** pomaže organizacijama da održe pridržavanje dogovorenih rasporeda isporuke automatizacijom poređenja potvrđenih i prihvaćenih datuma isporuke. Ovaj proaktivan pristup upravljanju isporukom poboljšava operativnu efikasnost, smanjuje kašnjenja i podstiče bolju saradnju u celom lancu snabdevanja.
