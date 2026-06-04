# Unit Price Combined with Fields

<figure><img src="../../../../.gitbook/assets/image (26) (2).png" alt="" width="563"><figcaption></figcaption></figure>

## **Svrha:**

Ova kartica radnog toka je dizajnirana da proceni da li jedinična cena, kada se kombinuje sa navedenom vrednošću polja (kao što su količina, popust ili dodatne naknade), ispunjava definisani uslov. Kartica upoređuje jediničnu cenu i vrednost polja sa navedenim pragom kako bi se obezbedilo da je određivanje cena usklađeno sa očekivanjima. Ovo poređenje može pokrenuti akcije na osnovu određenih uslova, kao što je označavanje nepodudaranja ili automatizacija procesa odobrenja u radnim tokovima nabavke ili prijema.

## **Komponente kartice:**

1. **Field Name**
   * **Opis:** Navodi polje dokumenta koje sadrži vrednost koja se kombinuje sa jediničnom cenom.
   * **Detalj:** Ovo mora da se poklapa sa tačnim identifikatorom prvog polja unutar dokumenta.
2. **Operator**
   * **Opis:** Definiše uslov koji će se primeniti na poređenje između kombinovane vrednosti i navedene vrednosti.
   * **Opcije:**
     * **Equals (=):** Proverava da li se kombinovana vrednost jedinične cene i polja poklapa sa navedenom vrednošću.
     * **Not Equals (≠):** Obezbeđuje da se kombinovana vrednost jedinične cene i polja razlikuje od navedene vrednosti.
     * **Greater Than (>):** Proverava da li je kombinovana vrednost veća od navedene vrednosti.
     * **Greater or Equals (≥):** Proverava da li je kombinovana vrednost veća ili jednaka navedenoj vrednosti.
     * **Lesser Than (<):** Proverava da li je kombinovana vrednost manja od navedene vrednosti.
     * **Lesser or Equals (≤):** Proverava da li je kombinovana vrednost manja ili jednaka navedenoj vrednosti.
3. **Value**
   * **Opis:** Navodi vrednost sa kojom će se uporediti kombinovana jedinična cena i vrednost polja.
   * **Detalj:** Vrednost mora biti numerička.

## **Funkcionalnost:**

* **Procena uslova:** Sistem procenjuje kombinovanu jediničnu cenu i vrednost polja na osnovu izabranog operatora i upoređuje je sa navedenom vrednošću. Rezultat ove procene određuje da li je uslov tačan ili netačan.
* **Izvršavanje akcije:**
  * **Tačan uslov:** Ako poređenje rezultira tačnim (npr. kombinovana vrednost prekoračuje navedenu vrednost), radni tok se nastavlja sa tačnim uslovom. Ovo može pokrenuti akcije kao što su odobrenje, usmeravanje dokumenta ili primena pravila obrade.
  * **Netačan uslov:** Ako poređenje rezultira netačnim (npr. kombinovana vrednost ne ispunjava uslov), radni tok se nastavlja sa netačnim uslovom. Ovo bi moglo pokrenuti obaveštenje, poslati dokument na ručni pregled ili zaustaviti radni tok.

## **Podešavanje i konfiguracija:**

* Korisnici počinju izborom polja dokumenta koja sadrže vrednosti koje se kombinuju sa jediničnom cenom. Nakon izbora polja, biraju odgovarajući operator da definišu kako će se kombinovana vrednost upoređivati sa navedenom vrednošću. Zatim mogu postaviti vrednost.

## **Primer scenarija:**

* Faktura navodi 50 jedinica proizvoda po $20 svaka, što ukupno iznosi $1000. Povezani dokument ima polje količine sa vrednošću 10. Koristeći operator "Greater Than", kartica upoređuje kombinovanu vrednost jedinične cene ($20) i količine (10), što je jednako $200. Kartica proverava da li je kombinovana vrednost veća od $150 (navedena vrednost). Pošto je kombinovana vrednost od $200 veća od praga od $150, radni tok se nastavlja da pokrene odobrenje za dokument.

## **Zaključak:**

Kartica radnog toka "Unit Price Combined with Fields" obezbeđuje da uslovi određivanja cena budu ispunjeni procenom kombinovane vrednosti jedinične cene i navedenog polja. Automatizacijom ovog poređenja, organizacije mogu obezbediti doslednost i označiti nepodudaranja u cenama ili količinama pre nego što nastave sa odobrenjem, pomažući u pojednostavljenju procesa nabavke i finansija.
