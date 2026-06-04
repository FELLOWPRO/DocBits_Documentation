---
hidden: true
---

# Supplier on Invoice

<figure><img src="../../../../.gitbook/assets/image (1) (1) (2).png" alt=""><figcaption></figcaption></figure>

## **Svrha**

Ova DocBits kartica omogućava detaljno poređenje, upoređujući dobavljača sa fakture i dobavljača iz potvrde porudžbine. Treba obezbediti da je dobavljač koji je izdao fakturu isti kao onaj u potvrdi porudžbine.

## **Funkcionalnost:**

* **Supplier on Invoice Supplier on Purchase Order:** Ova kartica proverava da li je dobavljač na fakturi isti kao u potvrdi porudžbine ili ne.
* **Vrednost operatora:** Korisnici mogu postaviti određene uslove kao što su: da li je dobavljač koji je izdao fakturu isti kao u PO ili ne. Dostupni operatori uključuju:
  * **Is (=):** Proverava da li se dobavljač na fakturi poklapa sa dobavljačem u potvrdi porudžbine.
  * **Is not (≠):** Obezbeđuje da je dobavljač koji je izdao fakturu isti kao u potvrdi porudžbine.

## **Upotreba:**

Ova kartica je korisna da bi se obezbedilo da se ceo proces obavlja sa istim dobavljačem i da sve odgovara jedno drugom. Ovo obezbeđuje da se, ako postoje nepodudaranja, skrene pažnja na proveru tih nepodudaranja i da se faktura ne plati pogrešnom dobavljaču koji nema veze sa porudžbinom i potvrdom porudžbine.

## **Primer scenarija:**

* Porudžbina se postavlja, zatim dolazi potvrda porudžbine i potom se izdaje faktura. Ceo proces naručivanja se obavlja sa jednim dobavljačem. Ako to nije slučaj, kartica može odmah utvrditi da postoje nepodudaranja između dobavljača i time obezbeđuje da se ne vrše nepravilna plaćanja i da se faktura izdaje samo sa dobavljačem koji je takođe bio uključen u ceo proces.

Korišćenjem kartice "Supplier on Invoice … Supplier on Purchase Order", kompanije mogu automatizovati proveru dobavljača koji izdaju fakture i povezanih potvrda porudžbina.
