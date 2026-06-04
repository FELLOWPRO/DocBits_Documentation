# Compare Total Charges

<figure><img src="../../../../.gitbook/assets/image (271).png" alt="" width="563"><figcaption></figcaption></figure>

## **Svrha:**

Ova kartica radnog toka upoređuje ukupne naknade u polju dokumenta sa odgovarajućim naknadama u nalogu za nabavku. Kartica pomaže da se obezbedi da naknade u dokumentu budu usklađene sa onima u nalogu za nabavku, uzimajući u obzir navedene nivoe tolerancije. Poređenje može pokrenuti akcije ako se pronađu nepodudaranja, kao što je označavanje nepodudaranja za pregled ili odgovarajuće prilagođavanje naknada.

## **Komponente kartice:**

1. **Field Name:**
   * **Opis**: Navodi polje dokumenta koje sadrži vrednosti ukupne naknade za poređenje sa naknadama u nalogu za nabavku.
   * **Detalj**: Vrednost u ovom polju predstavlja ukupne naknade primenjene u dokumentu (npr. faktura) i biće upoređena sa naknadom iz naloga za nabavku.
2. **Operator:**
   * **Opis**: Definiše uslov koji će se primeniti na poređenje između ukupne naknade u dokumentu i naknade u nalogu za nabavku.
   * **Opcije**:
     * **Equals (=)**: Proverava da li se ukupna naknada u dokumentu poklapa sa naknadom u nalogu za nabavku.
     * **Not Equals (≠)**: Obezbeđuje da se ukupna naknada u dokumentu razlikuje od naknade u nalogu za nabavku.
     * **Greater Than (>)**: Proverava da li je ukupna naknada u dokumentu veća od naknade u nalogu za nabavku.
     * **Greater or Equals (≥)**: Proverava da li je ukupna naknada u dokumentu veća ili jednaka naknadi u nalogu za nabavku.
     * **Lesser Than (<)**: Proverava da li je ukupna naknada u dokumentu manja od naknade u nalogu za nabavku.
     * **Lesser or Equals (≤)**: Proverava da li je ukupna naknada u dokumentu manja ili jednaka naknadi u nalogu za nabavku.
3. **Iznos tolerancije**
   * **Opis**: Navodi prag tolerancije za poređenje ukupnih naknada.
   * **Detalj**: Ova numerička vrednost predstavlja dozvoljeno odstupanje u naknadama između dokumenta i naloga za nabavku.
4. **Tip tolerancije:**
   * **Opis**: Navodi tip tolerancije koji će se primeniti.
   * **Opcije**:
     * **Percentage**: Tolerancija se primenjuje kao procenat naknade iz naloga za nabavku.
     * **Value**: Tolerancija se primenjuje kao fiksni numerički iznos.
5. **Separator:**
   * **Opis**: Navodi separator koji se koristi za razlikovanje Charge ID-a na kraju imena polja.
   * **Detalj**: Separator odvaja polje naknade od jedinstvenog Charge ID-a koji će se koristiti za povezivanje naknade iz dokumenta sa odgovarajućom naknadom u nalogu za nabavku.

## **Funkcionalnost:**

* **Procena uslova:** Sistem upoređuje ukupnu naknadu u polju dokumenta sa odgovarajućom naknadom u nalogu za nabavku na osnovu operatora i tolerancije. Tolerancija se primenjuje da bi se utvrdilo da li je razlika između dve naknade unutar prihvatljivog opsega.
* **Izvršavanje akcije:**
  * **Tačan uslov**: Ako se naknade poklapaju (uzimajući u obzir toleranciju) i uslov je tačan, radni tok će se nastaviti sa definisanom akcijom, kao što su odobrenje dokumenta ili dalja obrada.
  * **Netačan uslov**: Ako je uslov netačan (tj. naknade se ne poklapaju unutar tolerancije), radni tok se neće nastaviti.

## **Podešavanje i konfiguracija:**

* Korisnici počinju izborom polja dokumenta koje sadrži vrednost ukupne naknade. Zatim biraju operator da definišu kako će se naknada upoređivati sa naknadom iz naloga za nabavku. Potom korisnici postavljaju iznos i tip tolerancije (procenat ili apsolutni). Na kraju, navode separator i Charge ID koji će se koristiti za poređenje.

## **Primer scenarija:**

Faktura navodi naknadu od $500 u polju "total charges". Odgovarajuća naknada iz naloga za nabavku je $480, a tolerancija je postavljena na $20 (apsolutna tolerancija). Kartica upoređuje naknadu iz dokumenta sa naknadom iz naloga za nabavku:

* Ukupna naknada u dokumentu je unutar tolerancije od $20 u odnosu na nalog za nabavku, i radni tok se nastavlja bez problema.
* Ako naknada prekorači toleranciju, radni tok označava nepodudaranje za pregled.

## **Zaključak:**

Kartica radnog toka "Compare Total Charges" obezbeđuje da naknade u dokumentima budu usklađene sa onima u nalozima za nabavku, uzimajući u obzir navedene nivoe tolerancije. Ovo pomaže organizacijama da automatizuju proces provere, rano identifikuju nepodudaranja i održe bolju kontrolu nad procesima vezanim za naknade.
