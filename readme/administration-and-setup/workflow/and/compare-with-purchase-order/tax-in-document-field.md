# Tax in document field

<figure><img src="../../../../.gitbook/assets/image (268).png" alt="" width="563"><figcaption></figcaption></figure>

## **Svrha:**

Ova kartica radnog toka je dizajnirana da proceni da li se vrednost poreza u polju dokumenta poklapa sa vrednošću poreza u nalogu za nabavku, uzimajući u obzir tolerancije zasnovane na Charge ID-u. Kartica upoređuje ove dve vrednosti poreza (jednu iz polja dokumenta i jednu iz naloga za nabavku) i proverava da li ispunjavaju navedeni uslov (npr. jednako, veće od, manje od, itd.). Ovo pomaže da se obezbedi doslednost vrednosti poreza i da se nepodudaranja označe za dalji pregled ili odobrenje u radnim tokovima nabavke.

## **Komponente kartice:**

1. **Field Name**
   * **Opis**: Navodi polje dokumenta koje sadrži vrednost poreza za poređenje sa vrednošću poreza u nalogu za nabavku.
   * **Detalj**: Ovo polje mora da se poklapa sa tačnim identifikatorom za vrednost poreza u dokumentu.
2. **Operator**
   * **Opis**: Definiše uslov koji se primenjuje na poređenje između vrednosti poreza u dokumentu i vrednosti poreza u nalogu za nabavku.
   * **Opcije**:
     * **Equals (=)**: Proverava da li se porez u polju dokumenta poklapa sa porezom u nalogu za nabavku.
     * **Not Equals (≠)**: Obezbeđuje da se porez u polju dokumenta ne poklapa sa porezom u nalogu za nabavku.
     * **Greater Than (>)**: Proverava da li je porez u polju dokumenta veći od poreza u nalogu za nabavku.
     * **Greater or Equals (≥)**: Proverava da li je porez u polju dokumenta veći ili jednak porezu u nalogu za nabavku.
     * **Lesser Than (<)**: Proverava da li je porez u polju dokumenta manji od poreza u nalogu za nabavku.
     * **Lesser or Equals (≤)**: Proverava da li je porez u polju dokumenta manji ili jednak porezu u nalogu za nabavku.
3. **Master Data Table**
   * **Opis**: Tabela koja sadrži detalje naloga za nabavku, uključujući Charge ID i vrednosti poreza.
   * **Detalj**: Ova tabela mora da ima referencu na Charge ID povezan sa vrednošću poreza iz naloga za nabavku.
4. **Iznos tolerancije**
   * **Opis**: Iznos praga unutar kojeg vrednosti poreza mogu varirati. Ovo se koristi da bi se uzela u obzir manja nepodudaranja u obračunima poreza.
   * **Detalj**: Iznos tolerancije treba da bude numerička vrednost, koja definiše maksimalno dozvoljenu razliku između vrednosti poreza.
5. **Tip tolerancije**
   * **Opis**: Navodi tip tolerancije koji se primenjuje, bilo apsolutni ili zasnovan na procentu.
   * **Opcije**:
     * **Value**: Tolerancija je fiksna numerička vrednost.
     * **Percentage**: Tolerancija se izračunava kao procenat vrednosti poreza.

## **Funkcionalnost:**

* **Procena uslova:** Sistem procenjuje da li vrednost poreza u polju dokumenta ispunjava navedeni uslov kada se uporedi sa vrednošću poreza u nalogu za nabavku (sa referencom Charge ID-a iz tabele matičnih podataka). Iznos i tip tolerancije se uzimaju u obzir u ovoj proceni kako bi se dozvolile manje razlike u obračunima poreza.
* **Izvršavanje akcije:**
  * **Tačan uslov**: Ako porez u polju dokumenta ispunjava uslov kada se uporedi sa porezom iz naloga za nabavku (unutar iznosa i tipa tolerancije), radni tok se nastavlja.
  * **Netačan uslov**: Ako porez u polju dokumenta ne ispunjava uslov (bilo da nije unutar opsega tolerancije ili poređenje nije uspelo), radni tok će se zaustaviti.

## **Podešavanje i konfiguracija:**

* Korisnici moraju izabrati polje dokumenta koje sadrži vrednost poreza za poređenje. Zatim biraju operator za način na koji treba izvršiti poređenje (npr. jednako, veće od). Nakon toga, korisnici treba da navedu referencu na tabelu matičnih podataka i postave iznos i tip tolerancije kako bi se uzela u obzir manja nepodudaranja u porezu.

## **Primer scenarija:**

* Faktura navodi iznos poreza od $100. Odgovarajući nalog za nabavku, pronađen u tabeli matičnih podataka, navodi vrednost poreza od $95. Koristeći operator "Greater Than", sistem upoređuje vrednost poreza iz dokumenta ($100) sa vrednošću poreza iz naloga za nabavku ($95) sa tolerancijom od $10 (apsolutni tip tolerancije). Pošto je razlika od $5 unutar opsega tolerancije, radni tok se nastavlja bez pokretanja bilo kakvih upozorenja.

## **Zaključak:**

Kartica radnog toka "Tax in Document Field Comparison" obezbeđuje da vrednosti poreza u dokumentima budu usklađene sa detaljima naloga za nabavku, dozvoljavajući manja nepodudaranja na osnovu navedenih tolerancija. Automatizacijom ove provere, organizacije mogu smanjiti greške u obračunima poreza i pojednostaviti procese nabavke, smanjujući potrebu za ručnom intervencijom ili odobrenjima.
