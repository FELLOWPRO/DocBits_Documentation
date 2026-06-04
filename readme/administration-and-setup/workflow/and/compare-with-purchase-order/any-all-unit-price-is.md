# Any / All Unit Price is

<figure><img src="../../../../.gitbook/assets/image (274).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (273).png" alt="" width="563"><figcaption></figcaption></figure>

## **Svrha:**

Ova kartica radnog toka se koristi za poređenje jedinične cene u dokumentu sa jediničnom cenom u nalogu za nabavku, obezbeđujući da cene budu usklađene unutar definisanih nivoa tolerancije. Poređenje može pokrenuti akcije ako jedinična cena ne ispunjava očekivanja. **Verzija 4** dodaje veću fleksibilnost omogućavajući korisnicima da izaberu različite entitete za poređenje, pružajući dublji nivo kontrole nad procesima određivanja cena i nabavke.

## **Komponente kartice:**

1. **Any / All:**
   * **Opis**: Definiše da li se uslov primenjuje na bilo koju ili na sve instance u kojima se upoređuje jedinična cena.
   * **Opcije**:
     * **Any**: Uslov je ispunjen ako bilo koja jedinična cena ispunjava navedeni uslov poređenja.
     * **All**: Uslov je ispunjen samo ako sve jedinične cene ispunjavaju navedeni uslov poređenja.
2. **Operator:**
   * **Opis**: Definiše uslov za poređenje jedinične cene sa navedenom vrednošću.
   * **Opcije**:
     * **Equals (=)**: Proverava da li se jedinična cena poklapa sa navedenom vrednošću.
     * **Not Equals (≠)**: Obezbeđuje da se jedinična cena razlikuje od navedene vrednosti.
     * **Greater Than (>)**: Proverava da li je jedinična cena veća od navedene vrednosti.
     * **Greater or Equals (≥)**: Proverava da li je jedinična cena veća ili jednaka navedenoj vrednosti.
     * **Lesser Than (<)**: Proverava da li je jedinična cena manja od navedene vrednosti.
     * **Lesser or Equals (≤)**: Proverava da li je jedinična cena manja ili jednaka navedenoj vrednosti.

## **Dodatne komponente u Verziji 4:**

**Comparison Type:**

* **Opis**: Omogućava korisnicima da izaberu koji će se entiteti upoređivati pored jedinične cene.
* **Opcije**:
  * **Purchase Order to Document**: Upoređuje jediničnu cenu u nalogu za nabavku sa jediničnom cenom u dokumentu.
  * **Received to Document**: Upoređuje primljenu količinu sa jediničnom cenom u dokumentu.
  * **Purchase Order to Received**: Upoređuje jediničnu cenu u nalogu za nabavku sa primljenom količinom.

## **Funkcionalnost:**

* **Procena uslova:** Sistem upoređuje jediničnu cenu u dokumentu sa jediničnom cenom u nalogu za nabavku (ili drugim izabranim entitetom, u Verziji 4) na osnovu izabranog operatora. Ako je poređenje tačno, radni tok se nastavlja prema sledećim koracima, bilo pokretanjem odobrenja ili zaustavljanjem procesa.
* **Izvršavanje akcije:**
  * **Tačan uslov**: Ako se uslov proceni kao tačan (npr. jedinična cena u dokumentu je veća od navedene vrednosti), radni tok će se nastaviti sa tačnom akcijom (npr. odobrenje, obrada dokumenta).
  * **Netačan uslov**: Ako se uslov proceni kao netačan (npr. jedinična cena u dokumentu ne ispunjava poređenje), radni tok se neće nastaviti.

## **Podešavanje i konfiguracija:**

* **Podešavanje u Verziji 3:** Korisnici konfigurišu karticu izborom jedinične cene u dokumentu, izborom odgovarajućeg operatora za definisanje načina na koji će se jedinična cena upoređivati sa navedenom vrednošću i postavljanjem vrednosti za poređenje. Pored toga, korisnici biraju da li se uslov primenjuje na bilo koju ili sve instance poređenja jedinične cene.
* **Podešavanje u Verziji 4:** U Verziji 4, korisnici imaju dodatnu opciju da izaberu Comparison Type. Ovo im omogućava da definišu entitete za poređenje, kao što su Purchase Order to Document, Received to Document ili Purchase Order to Received. Ovo poboljšava fleksibilnost kartice za poređenje jediničnih cena u složenijim scenarijima.

## **Primer scenarija:**

*   **Primer u Verziji 3:**&#x20;

    Faktura pokazuje jediničnu cenu od $50. Povezani nalog za nabavku ima jediničnu cenu od $45. Kartica upoređuje dve jedinične cene koristeći operator "Greater Than". Pošto je jedinična cena u dokumentu ($50) veća od jedinične cene u nalogu za nabavku ($45), radni tok će pokrenuti tačan uslov (npr. slanje dokumenta na pregled).
* **Primer u Verziji 4:**\
  Faktura pokazuje jediničnu cenu od $50, a povezani nalog za nabavku je odobrio jediničnu cenu od $45. Pored toga, primljena količina je 60 jedinica. Kartica upoređuje primljenu količinu sa jediničnom cenom u dokumentu koristeći operator "Greater Than". Pošto je primljena količina (60) veća od jedinične cene ($50), radni tok pokreće tačan uslov, i dokument se označava za dalji pregled.

## **Zaključak:**

Verzija 3 kartice radnog toka "Unit Price Comparison" je dizajnirana da obezbedi da jedinične cene u dokumentima budu usklađene sa onima u nalozima za nabavku, pokrećući akcije na osnovu definisanih uslova. Verzija 4 proširuje ovu funkcionalnost uvođenjem složenijih opcija poređenja, kao što su poređenje naloga za nabavku sa dokumentima, primljenih količina sa dokumentima i naloga za nabavku sa primljenim količinama. Ova dodatna fleksibilnost omogućava organizacijama da rukuju sofisticiranijim scenarijima određivanja cena i nabavke, poboljšavajući kontrolu i tačnost u svojim radnim tokovima.
