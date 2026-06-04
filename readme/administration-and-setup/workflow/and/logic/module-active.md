# Module active

<figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Svrha:**

Ova DocBits kartica proverava da li je određeni modul u sistemu aktivan ili neaktivan. Omogućava radnim tokovima da se nastave na osnovu statusa aktivacije modula, obezbeđujući da se akcije izvršavaju samo ako je neophodni modul dostupan.

## **Funkcionalnost:**

* **Validacija statusa modula:** Ova kartica proverava status aktivacije navedenog modula i procenjuje ga u odnosu na uslov koji je definisao korisnik.
* **Izbor modula:** Korisnici navode ime modula koji treba proveriti, obezbeđujući preciznu validaciju.
* **Operatori:** Mogu se primeniti sledeći uslovi:
  * **Is:** Radni tok se nastavlja ako je izabrani modul aktivan.
  * **Is Not:** Radni tok se nastavlja ako je izabrani modul neaktivan.

## **Upotreba:**

Ova kartica je posebno korisna za administratore ili sistemske menadžere kojima je potrebno da kreiraju radne tokove koji zavise od dostupnosti ili funkcionalnosti određenih modula. Pomaže da se obezbedi da se radni tokovi izvršavaju samo kada su svi potrebni moduli odgovarajuće konfigurisani.

## **Primer scenarija**

* Korisnik konfiguriše karticu da proveri da li je modul **"Document Processing"** **aktivan.** Ako je modul aktivan, radni tok se nastavlja, pokrećući automatizovane zadatke obrade dokumenata. Ako je modul neaktivan, radni tok se zaustavlja, sprečavajući nepotrebne akcije.

Korišćenjem kartice "Module Active Check", organizacije mogu poboljšati pouzdanost radnog toka, izbeći greške usled neaktivnih modula i obezbediti da procesi budu usklađeni sa konfiguracijom sistema.
