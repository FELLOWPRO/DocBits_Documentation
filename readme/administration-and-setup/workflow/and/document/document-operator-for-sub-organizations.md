# Document Operator for Sub-Organizations

<figure><img src="../../../../.gitbook/assets/image (42).png" alt="" width="563"><figcaption></figcaption></figure>

## Svrha:

Ova kartica radnog toka procenjuje da li je dokument deo određene pod-organizacije. Na osnovu ove procene, radni tok se može nastaviti ili pokrenuti različite akcije u zavisnosti od toga da li je dokument povezan sa navedenom pod-organizacijom ili ne.

## Komponente kartice:

1. **Operator**
   * **Opis:** Definiše da li dokument mora biti deo navedene pod-organizacije ili ne.
   * **Opcije:**
     * **Is:** Dokument mora biti deo navedene pod-organizacije da bi uslov bio tačan.
     * **Is Not:** Dokument ne sme biti deo navedene pod-organizacije da bi uslov bio tačan.
2. **Sub-org**
   * **Opis:** Navodi pod-organizaciju sa kojom dokument treba uporediti.
   * **Detalj:** Ovo treba da se poklapa sa identifikatorom pod-organizacije. Poređenje proverava da li dokument pripada navedenoj pod-organizaciji.

## Funkcionalnost:

* **Procena uslova:** Sistem procenjuje da li je dokument deo navedene pod-organizacije. Ova procena proverava pod-organizaciju dokumenta u odnosu na onu koju je naveo korisnik.
* **Izvršavanje akcije:**
  * **Tačan uslov:**\
    Ako je dokument deo navedene pod-organizacije, radni tok se nastavlja sa tačnim uslovom. Ovo može pokrenuti dalje akcije, kao što su usmeravanje dokumenta određenom odeljenju, primena pravila specifičnih za pod-organizaciju ili omogućavanje funkcija prilagođenih toj pod-organizaciji.
  * **Netačan uslov:**\
    Ako dokument nije deo navedene pod-organizacije, radni tok se nastavlja sa netačnim uslovom. Ovo omogućava izvršavanje alternativnih akcija, kao što su slanje obaveštenja, zaustavljanje radnog toka ili primena opštih pravila izvan opsega pod-organizacije.

## Podešavanje i konfiguracija:

* Korisnici konfigurišu karticu izborom polja dokumenta koje sadrži dokument i navođenjem pod-organizacije za proveru. Operator se zatim bira iz padajuće liste da definiše da li dokument mora biti deo ili ne deo navedene pod-organizacije. Na kraju, korisnici postavljaju uslov za nastavak (tačan ili netačan), koji određuje sledeći korak u radnom toku.

## Zaključak:

Kartica radnog toka "Document in Sub-organization" je koristan alat za automatizaciju akcija na osnovu toga da li dokument pripada određenoj pod-organizaciji. Obezbeđivanjem da se dokumenti obrađuju u skladu sa pravilima specifičnim za pod-organizaciju, ova kartica poboljšava efikasnost radnog toka i obezbeđuje da se akcije izvršavaju u ispravnom organizacionom kontekstu.
