# Combined Price of Quantity Difference

<figure><img src="../../../../.gitbook/assets/image (17) (1).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (21) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Svrha**:

Ova kartica radnog toka procenjuje kombinovanu cenu razlike u količini, upoređujući je sa navedenom vrednošću. Pomaže u automatizaciji akcija na osnovu nepodudaranja u ceni i količini između povezanih dokumenata, poboljšavajući radne tokove nabavke i prijema. **Verzija 4** proširuje ovu funkcionalnost omogućavajući poređenja između različitih entiteta kao što su nalog za nabavku, primljene količine i sam dokument, dodajući veću fleksibilnost i kontrolu radnom toku.

## **Komponente kartice**:

1. **Operator**:&#x20;
   * **Opis:** Uslov za poređenje kombinovane cene sa navedenom vrednošću.
   * **Opcije:**
     * **Equals (=)**: Proverava da li se kombinovana cena poklapa sa navedenom vrednošću.
     * **Not Equals (≠)**: Obezbeđuje da se kombinovana cena razlikuje od navedene vrednosti.
     * **Greater Than (>)**: Proverava da li je kombinovana cena veća od navedene vrednosti.
     * **Greater or Equals (≥)**: Proverava da li je kombinovana cena veća ili jednaka navedenoj vrednosti.
     * **Lesser Than (<)**: Proverava da li je kombinovana cena manja od navedene vrednosti.
     * **Lesser or Equals (≤)**: Proverava da li je kombinovana cena manja ili jednaka navedenoj vrednosti
2. **Vrednost**:&#x20;
   * **Opis:** Navodi vrednost sa kojom će se uporediti kombinovana cena vrednosti količine.
   * **Detalj:** Vrednost mora biti numerička.

## **Dodatne komponente u Verziji 4**:

* **Comparison Type**: Bira entitete za poređenje. Opcije uključuju:
  * **Purchase Order to Document**: Upoređuje količine i cene između naloga za nabavku i povezanog dokumenta.
  * **Received to Document**: Upoređuje primljene količine sa količinama u dokumentu.
  * **Purchase Order to Received**: Upoređuje količine iz naloga za nabavku sa primljenim količinama.

## **Funkcionalnost**:

* **Procena uslova**: Izračunava kombinovanu cenu množenjem razlike u količini sa cenom po jedinici i upoređuje je sa navedenom vrednošću koristeći izabrani operator.\
  **Verzija 4** dodaje opciju poređenja dodatnih entiteta na osnovu korisnikove konfiguracije, kao što su nalog za nabavku prema primljenom ili nalog za nabavku prema dokumentu.
* **Izvršavanje akcije**: Na osnovu toga da li kombinovana cena ispunjava navedeni uslov, radni tok će se nastaviti sa tačnim ili netačnim uslovima da bi pokrenuo akcije ili zaustavio radni tok. **Verzija 4** takođe omogućava dinamičnije izvršavanje akcija, gde tip uslova (npr. nalog za nabavku prema primljenom) utiče na sledeći korak.

## **Podešavanje i konfiguracija**:

* **Verzija 3**: Korisnici konfigurišu karticu izborom polja dokumenta za razliku u količini i cenu po jedinici. Operator se zatim bira da definiše kako će se kombinovana cena upoređivati sa navedenom vrednošću. Na kraju, korisnici postavljaju uslov za nastavak (tačan ili netačan), koji određuje sledeći korak u radnom toku.
* **Verzija 4**: Pored konfiguracije iz **Verzije 3**, korisnici imaju dodatnu opciju da konfigurišu **Comparison Type**. Ovo definiše koji će se entiteti upoređivati, kao što su **Purchase Order to Document**, **Received to Document** ili **Purchase Order to Received**.

## **Primer scenarija**:

* Faktura pokazuje 50 jedinica proizvoda po $100 svaka, što ukupno iznosi $5000. Povezani nalog za nabavku je odobrio kupovinu od $4500 za 45 jedinica. Razlika u količini je 5 jedinica, a kombinovana cena razlike je $500. Kartica upoređuje količinu iz naloga za nabavku (45 jedinica) sa primljenom količinom (50 jedinica) i proverava da li je kombinovana cena veća od $400 (navedena vrednost). Koristeći operator **Greater Than (>)**, kartica identifikuje nepodudaranje i označava ga za pregled finansijskog tima.

## **Zaključak**:

**Verzija 3** kartice radnog toka "Combined Price of Quantity Difference" nudi jednostavan pristup za poređenje nepodudaranja u količini i pokretanje akcija na osnovu pragova cena.\
**Verzija 4** proširuje ovu funkcionalnost omogućavajući poređenja između različitih entiteta (nalog za nabavku, primljeno, dokument), pružajući veću fleksibilnost i kontrolu nad radnim tokom. Organizacije sada mogu automatizovati složenije scenarije i sprovoditi strožiju kontrolu nad svojim procesima nabavke i prijema.
