# Item Id on Purchase Order

<figure><img src="../../../../.gitbook/assets/image (275).png" alt="" width="563"><figcaption></figcaption></figure>

## **Svrha:**

Ova kartica radnog toka je dizajnirana da uporedi ID-ove stavki između naloga za nabavku i povezanog dokumenta kako bi se obezbedilo da su uključene ispravne stavke. Kartica procenjuje da li se ID stavke u nalogu za nabavku poklapa sa ID-om stavke u dokumentu. Ovo poređenje može pokrenuti akcije ako se pronađu nepodudaranja, obezbeđujući da stavke u dokumentu budu usklađene sa nalogom za nabavku.

## **Komponente kartice:**

1. **Any / All:**
   * **Opis**: Definiše da li se uslov primenjuje na bilo koju ili na sve instance poređenja ID-a stavke.
   * **Opcije**:
     * **Any**: Uslov je ispunjen ako se bilo koji ID stavke u nalogu za nabavku poklapa sa ID-om stavke u dokumentu.
     * **All**: Uslov je ispunjen samo ako se svi ID-ovi stavki u nalogu za nabavku poklapaju sa ID-ovima stavki u dokumentu.
2. **Operator:**
   * **Opis**: Definiše uslov za poređenje ID-a stavke u nalogu za nabavku sa ID-om stavke u dokumentu.
   * **Opcije**:
     * **Equals (=)**: Proverava da li se ID stavke u nalogu za nabavku tačno poklapa sa ID-om stavke u dokumentu.
     * **Not Equals (≠)**: Obezbeđuje da se ID stavke u nalogu za nabavku ne poklapa sa ID-om stavke u dokumentu.

## **Funkcionalnost:**

* **Procena uslova:** Sistem upoređuje ID stavke u nalogu za nabavku sa ID-om stavke u dokumentu na osnovu izabranog operatora. Ako je uslov poređenja tačan (npr. ID-ovi stavki se poklapaju ili ne poklapaju), radni tok će se nastaviti u skladu sa tim.
* **Izvršavanje akcije:**
  * **Tačan uslov**: Ako se uslov proceni kao tačan (npr. ID stavke u nalogu za nabavku jednak je ID-u stavke u dokumentu), radni tok će se nastaviti sa tačnom akcijom (npr. odobrenje ili dalja obrada).
  * **Netačan uslov**: Ako se uslov proceni kao netačan (npr. ID stavke u nalogu za nabavku se ne poklapa sa ID-om stavke u dokumentu), radni tok se neće nastaviti.

## **Podešavanje i konfiguracija:**

* Korisnici konfigurišu karticu izborom ID-a stavke i u nalogu za nabavku i u dokumentu. Zatim biraju odgovarajući operator (Equals ili Not Equals) da definišu kako će se ID-ovi stavki upoređivati. Na kraju, korisnici biraju da li se uslov primenjuje na bilo koji ili na sve ID-ove stavki u poređenju.

## **Primer scenarija:**

* Faktura navodi stavku sa ID-om "ABC123", a povezani nalog za nabavku takođe uključuje stavku sa ID-om "ABC123". Koristeći operator "Equals", kartica upoređuje ID stavke u dokumentu sa ID-om stavke u nalogu za nabavku. Pošto se ID-ovi stavki poklapaju, radni tok se nastavlja bez problema

## **Zaključak:**

Kartica radnog toka "Item ID Comparison" obezbeđuje da ID-ovi stavki u dokumentima budu usklađeni sa onima u nalozima za nabavku. Ovo pomaže u sprečavanju nepodudaranja u listama stavki i obezbeđuje da se ispravne stavke obrađuju u skladu sa nalogom za nabavku. Mogućnost poređenja na osnovu bilo koje ili svih instanci pruža fleksibilnost u različitim slučajevima upotrebe, poboljšavajući tačnost i efikasnost radnih tokova nabavke.
