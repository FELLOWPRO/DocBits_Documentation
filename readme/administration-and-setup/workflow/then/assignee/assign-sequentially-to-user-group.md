# Assign Sequentially to User/Group

<figure><img src="../../../../.gitbook/assets/image (11) (1) (2).png" alt="" width="563"><figcaption></figcaption></figure>

## **Svrha**

Kartica radnog toka "**Assign the Document Sequentially to User/Group Based on Decision Table**" dinamično dodeljuje dokumente bilo korisniku bilo grupi, u zavisnosti od procene tabele odlučivanja. Ovo obezbeđuje da se dokumenti usmeravaju na odgovarajući način na osnovu unapred definisanih pravila.

## **Komponente kartice**

1. **Priority (Value)**
   * **Opis**: Navodi nivo prioriteta za dodele, pri čemu niži brojevi predstavljaju viši prioritet.
   * **Detalj**: Numeričko polje za unos u kojem se može postaviti vrednost prioriteta za kontrolu redosleda dodele.

## **Funkcionalnost**

* **Procena tabele odlučivanja**:\
  Tabela odlučivanja procenjuje unapred definisane uslove da odluči da li se dokument dodeljuje korisniku ili grupi.
* **Dodela dokumenta**:
  * Ako tabela odlučivanja vrati korisnika, dokument se dodeljuje direktno tom korisniku.
  * Ako tabela odlučivanja vrati grupu, dokument se dodeljuje grupi sekvencijalno, poštujući navedenu vrednost prioriteta.

## **Podešavanje i konfiguracija**

1. Dodajte karticu **Assign the Document Sequentially** u svoj radni tok.
2. Konfigurišite polje **Priority (Value)**:
   * Unesite numeričku vrednost da postavite prioritet dodele.
3. Sačuvajte i aktivirajte radni tok da biste primenili konfiguraciju.

## **Zaključak**

Kartica radnog toka "**Assign the Document Sequentially to User/Group Based on Decision Table**" obezbeđuje efikasno i dinamičko usmeravanje dokumenata. Korišćenjem logike tabele odlučivanja i vrednosti prioriteta, kartica olakšava tačnu dodelu bilo korisniku bilo grupi, pojednostavljujući radne tokove dokumenata.
