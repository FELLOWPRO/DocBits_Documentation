# Document Type

<figure><img src="../../../../.gitbook/assets/image (16) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## Svrha:

Ova kartica radnog toka je dizajnirana da proceni da li se dokument poklapa sa određenim tipom. Proverom da li dokument odgovara datom tipu, radni tokovi se mogu nastaviti ili preduzeti alternativne akcije na osnovu ovog uslova. Ovo pomaže u automatizaciji procesa gde tip dokumenta diktira sledeće korake u radnom toku.

## Komponente kartice:

1. **Operator**
   * **Opis**: Definiše da li dokument treba da bude navedenog tipa ili ne.
   * **Opcije**:
     * **Is**: Dokument mora da se poklapa sa navedenim tipom da bi uslov bio tačan.
     * **Is Not**: Dokument ne sme da se poklapa sa navedenim tipom da bi uslov bio tačan.
2. **Type**
   * **Opis**: Navodi tip dokumenta sa kojim treba uporediti.
   * **Detalj**: Ovo uključuje različite tipove dokumenata kao što su "Invoice", "Purchase Order", itd., na osnovu kojih će se uslov (is/is not) proceniti.

## Funkcionalnost:

* **Procena uslova**: Sistem procenjuje da li se tip dokumenta u navedenom polju poklapa sa uslovom definisanim operatorom. Upoređuje vrednost polja sa datim tipom dokumenta.
* **Izvršavanje akcije**:
  * **Tačan uslov**: Ako se tip dokumenta poklapa sa navedenim tipom (ili ne, na osnovu operatora), radni tok se nastavlja sa tačnim uslovom. Ovo može pokrenuti akcije kao što su dalja obrada dokumenta, slanje na odobrenje ili primena određenih pravila na osnovu tipa dokumenta.
  * **Netačan uslov**: Ako se tip dokumenta ne poklapa sa navedenim tipom, radni tok se nastavlja sa netačnim uslovom. Ovo može pokrenuti alternativne akcije, kao što su usmeravanje dokumenta u drugi proces ili zaustavljanje daljih akcija.

## Podešavanje i konfiguracija:

* Korisnici konfigurišu karticu izborom polja dokumenta koje sadrži tip dokumenta iz liste dostupnih polja. Zatim se bira operator da definiše da li dokument mora biti navedenog tipa ili ne. Na kraju, korisnici postavljaju uslov za nastavak (tačan ili netačan), koji određuje sledeću akciju na osnovu tipa dokumenta.

## Zaključak:

Kartica radnog toka "Document Type Comparison" je od suštinskog značaja za obezbeđivanje da se radni tokovi nastave na osnovu tipa dokumenta koji se obrađuje. Poređenjem tipa dokumenta, ona pomaže organizacijama da automatizuju zadatke usmeravanja i obrade dokumenata, obezbeđujući da se dokumentima rukuje na odgovarajući način na osnovu njihovog tipa.
