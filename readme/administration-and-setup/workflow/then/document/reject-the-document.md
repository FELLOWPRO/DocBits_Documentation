# Reject the Document

<figure><img src="../../../../.gitbook/assets/image (282).png" alt="" width="563"><figcaption></figcaption></figure>

## **Svrha:**

Kartica radnog toka **"Reject the Document"** se koristi za označavanje dokumenta kao odbijenog unutar radnog toka. Ova akcija zaustavlja napredovanje dokumenta i sprečava ga da pređe u sledeću fazu radnog toka. Obezbeđuje da se dokumenti koji ne ispunjavaju neophodne uslove ili kriterijume označe i spreče u daljoj obradi.

## **Komponente kartice:**

1. **Status odbijanja**
   * **Opis**: Ova komponenta označava dokument kao odbijen, signalizirajući da nije ispunio tražene uslove za odobrenje.
   * **Detalj**: Kada se pokrene, ova kartica ažurira status dokumenta u "rejected". Ova odluka se donosi na osnovu uslova postavljenih u odeljcima **"Where"** i **"And"**.

## **Funkcionalnost:**

* **Procena uslova**: Sistem procenjuje uslove postavljene u odeljcima **"Where"** i **"And"**.
  * Ako su **oba uslova tačna**, dokument će biti odbijen.
  * Ako je **bilo koji uslov netačan**, kartica se neće izvršiti, i status dokumenta će ostati nepromenjen.
* **Izvršavanje akcije**: Kada su uslovi zadovoljeni, dokument se označava kao odbijen. Ova akcija obezbeđuje da samo dokumenti koji ispunjavaju određene kriterijume idu dalje, dok se ostali označavaju i zaustavljaju radi pregleda ili ispravke.

## **Zaključak:**

Kartica radnog toka **"Reject the Document"** je suštinski alat za kontrolu toka dokumenata u automatizovanim procesima. Omogućavanjem odbijanja neusklađenih dokumenata, ona obezbeđuje da samo validni i tačni dokumenti nastave kroz radni tok, poboljšavajući efikasnost i tačnost u upravljanju dokumentima.
