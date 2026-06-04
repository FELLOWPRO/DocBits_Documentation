# Out of Tolerance Unit Price

<figure><img src="../../../../.gitbook/assets/image (272).png" alt="" width="563"><figcaption></figcaption></figure>

## **Svrha:**

Ova kartica radnog toka je dizajnirana da proceni da li kombinovana vrednost jediničnih cena i navedenog polja prekoračuje ili je ispod definisanog praga. Pomaže u identifikaciji svih nepodudaranja gde su jedinične cene, kada se kombinuju sa drugim poljima, izvan tolerancije, obezbeđujući da uslovi određivanja cena ispunjavaju očekivanja i označavajući sve probleme za pregled ili dalju akciju.

## **Komponente kartice:**

1. **Field Name:**
   * **Opis**: Navodi polje dokumenta koje sadrži vrednost koja se kombinuje sa jediničnom cenom.
   * **Detalj**: Vrednost u ovom polju biće kombinovana sa jediničnom cenom da bi se stvorila ukupna kombinovana vrednost za poređenje.
2. **Operator:**
   * **Opis**: Definiše uslov za poređenje kombinovane vrednosti jedinične cene i vrednosti polja sa navedenom vrednošću.
   * **Opcije**:
     * **Equals (=)**: Proverava da li se kombinovana vrednost jedinične cene i polja poklapa sa navedenom vrednošću.
     * **Not Equals (≠)**: Obezbeđuje da se kombinovana vrednost jedinične cene i polja razlikuje od navedene vrednosti.
     * **Greater Than (>)**: Proverava da li kombinovana vrednost jedinične cene i polja prekoračuje navedenu vrednost.
     * **Greater or Equals (≥)**: Proverava da li je kombinovana vrednost jedinične cene i polja veća ili jednaka navedenoj vrednosti.
     * **Lesser Than (<)**: Proverava da li je kombinovana vrednost jedinične cene i polja manja od navedene vrednosti.
     * **Lesser or Equals (≤)**: Proverava da li je kombinovana vrednost jedinične cene i polja manja ili jednaka navedenoj vrednosti.
3. **Value:**
   * **Opis**: Navodi vrednost sa kojom će se uporediti kombinovana jedinična cena i vrednost polja.
   * **Detalj**: Ova numerička vrednost predstavlja prag za poređenje. Ako kombinovana vrednost jedinične cene i polja prekorači ili je ispod ove vrednosti (na osnovu izabranog operatora), uslov će pokrenuti navedene akcije.

## **Funkcionalnost:**

* &#x20;**Procena uslova:** Sistem izračunava kombinovanu vrednost množenjem ili sabiranjem jedinične cene sa vrednošću polja, u zavisnosti od konfiguracije. Rezultat se zatim upoređuje sa navedenom vrednošću koristeći izabrani operator. Ako je uslov ispunjen (tj. kombinovana vrednost je izvan tolerancije), radni tok se nastavlja sa sledećim korakom, bilo da je to odobrenje, odbijanje ili dalji pregled.
* **Izvršavanje akcije:**
  * **Tačan uslov**: Ako poređenje rezultira tačnim (tj. kombinovana vrednost ispunjava uslov), radni tok pokreće akciju povezanu sa tačnim uslovom (npr. odobrenje ili obaveštenje).
  * **Netačan uslov**: Ako poređenje rezultira netačnim (tj. kombinovana vrednost ne ispunjava uslov), radni tok se neće nastaviti.

## **Podešavanje i konfiguracija:**

* Korisnici biraju polje koje sadrži vrednost koja se kombinuje sa jediničnom cenom. Zatim biraju odgovarajući operator da odrede kako će se kombinovana vrednost upoređivati sa navedenom vrednošću. Na kraju, korisnik postavlja vrednost sa kojom će se kombinovana cena upoređivati.

## **Primer scenarija:**

* Faktura navodi 50 jedinica proizvoda po $30 svaka, što ukupno iznosi $1500. Povezani dokument ima polje količine sa vrednošću 10. Kombinovana cena se izračunava množenjem jedinične cene ($30) i količine (10), što daje $300. Kartica zatim upoređuje ovu kombinovanu vrednost sa pragom od $250. Koristeći operator "Greater Than", kartica utvrđuje da je $300 veće od $250, pokrećući proces odobrenja za dokument.

## **Zaključak:**

Kartica radnog toka "Out of Tolerance Unit Prices Combined with Fields" pomaže da se obezbedi da vrednosti cena i polja budu usklađene sa poslovnim pravilima. Automatizacijom ove provere, organizacije mogu rano identifikovati nepodudaranja u procesu, obezbeđujući da se sve jedinične cene izvan tolerancije označe za pregled ili neophodnu akciju.
