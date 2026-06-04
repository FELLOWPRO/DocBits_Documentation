# Field is

<figure><img src="../../../../.gitbook/assets/image (7) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Svrha:**

Ova kartica radnog toka je dizajnirana da automatizuje akcije na osnovu prisustva ili stanja navedenog polja unutar dokumenta. Procenom da li je polje prazno, nedostaje ili je popunjeno, ona omogućava radnim tokovima da rukuju dokumentima sa preciznošću i tačnošću.

## **Komponente kartice:**

1. **Field Name**
   * **Opis:** Navodi ime polja koje treba proceniti.
   * **Detalj:** Ovo mora da se poklapa sa tačnim identifikatorom koji se koristi u dokumentu kako bi se obezbedila tačna detekcija polja.
2. **Operatori**
   * **Opis**: Definiše uslov koji pokreće radni tok, na osnovu prisustva ili stanja polja.
   * **Opcije**:
     * **Empty/Not in Document:** Radni tok se pokreće ako polje ili nedostaje u dokumentu ili je prisutno ali prazno.
     * **In Document/Not Empty:** Radni tok se pokreće ako polje postoji u dokumentu i sadrži vrednost.

## **Funkcionalnost:**

* **Detekcija stanja:** Kartica prati navedeno polje da bi procenila njegovo prisustvo i stanje.
* **Procena uslova:**
  * Sistem procenjuje da li je navedeno polje u stanju (Empty/Not in Document ili In Document/Not Empty) definisanom izabranim operatorom.
*

    **Izvršavanje akcije:**

    * **Uslov Empty/Not in Document:** Ako se stanje polja poklapa sa ovim uslovom (tj. polje je odsutno iz dokumenta ili je prisutno ali prazno), sistem pokreće povezane akcije. One mogu uključivati generisanje upozorenja, označavanje dokumenta za pregled ili zaustavljanje radnog toka.
    * **Uslov In Document/Not Empty:** Ako se stanje polja poklapa sa ovim uslovom (tj. polje postoji u dokumentu i sadrži vrednost), sistem pokreće povezane akcije. One mogu uključivati omogućavanje narednih koraka radnog toka, ažuriranje zapisa ili pokretanje obaveštenja.

## **Podešavanje i konfiguracija:**&#x20;

* Korisnici biraju polje iz liste dostupnih polja dokumenta. Operator se bira preko padajućeg menija, nudeći jasne opcije za "Empty/Not in Document" ili "In Document/Not Empty".

## **Zaključak:**

Kartica radnog toka "Field Presence and State Validation" je ključni alat za radne tokove obrade dokumenata, obezbeđujući tačno rukovanje poljima koja nedostaju ili su popunjena. Automatizacijom akcija na osnovu stanja polja, ova kartica poboljšava integritet podataka, smanjuje greške i obezbeđuje da radni tokovi funkcionišu neometano i efikasno.
