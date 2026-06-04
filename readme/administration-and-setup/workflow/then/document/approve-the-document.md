# Approve the Document



<figure><img src="../../../../.gitbook/assets/image (281).png" alt="" width="563"><figcaption></figcaption></figure>

## **Svrha:**

Kartica radnog toka **"Approve the Document"** se koristi za označavanje dokumenta kao odobrenog. Omogućava dokumentu da napreduje u sledeću fazu radnog toka, omogućavajući izvršavanje automatizovane obrade ili radnih tokova odobravanja. Ova kartica pomaže u pojednostavljenju procesa upravljanja dokumentima, obezbeđujući da samo odobreni dokumenti idu napred za dalje akcije.

## **Komponente kartice:**

1. **Status odobrenja**
   * **Opis**: Ova komponenta označava dokument kao odobren.
   * **Detalj**: Kada se ova kartica pokrene, status odobrenja dokumenta se ažurira da označi odobrenje. Ova akcija se može postaviti na osnovu uslova definisanih u odeljcima **"Where"** i **"And"**.

## **Funkcionalnost:**

* **Procena uslova**: Sistem procenjuje uslove postavljene u odeljcima **"Where"** i **"And"**.
  * Ako su **oba uslova tačna**, dokument će biti označen kao odobren.
  * Ako je **bilo koji uslov netačan**, kartica se neće izvršiti, i status odobrenja dokumenta će ostati nepromenjen.
* **Izvršavanje akcije**: Kada su uslovi ispunjeni, dokument se odobrava. Ova promena se odražava u statusu dokumenta, omogućavajući mu da nastavi dalje u radnom toku.

## **Zaključak:**

Kartica radnog toka **"Approve the Document"** je ključna komponenta za automatizaciju odobravanja dokumenata u poslovnim radnim tokovima. Obezbeđivanjem da se odobravaju samo dokumenti koji ispunjavaju određene kriterijume, ona pomaže u održavanju doslednosti, smanjuje ručni nadzor i omogućava neometaniju obradu dokumenata.
