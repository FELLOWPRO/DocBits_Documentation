# Assign user from field

<figure><img src="../../../../.gitbook/assets/image (299).png" alt="" width="563"><figcaption></figcaption></figure>

## **Svrha:**

Kartica radnog toka **"Assign User from Field with Fallback"** dinamično dodeljuje korisnika na osnovu vrednosti pronađene u navedenom polju dokumenta. Ako polje ne sadrži validnog korisnika, bira se rezervni korisnik iz unapred definisane liste dostupnih korisnika kako bi se obezbedilo da zadatak ili akcija budu pravilno dodeljeni.

## **Komponente kartice:**

1. **Field Name**
   * **Opis:** Navodi **polje dokumenta** koje sadrži informacije o korisniku koji se dodeljuje.
   * **Detalj:** Ovo polje se procenjuje da bi se odredilo koji korisnik treba da bude dodeljen. Ako polje sadrži validnog korisnika, tom korisniku će biti dodeljen zadatak. Ako je polje prazno ili nevažeće, biće dodeljen rezervni korisnik.
2. **User (Fallback)**
   * **Opis:** Navodi **rezervnog korisnika** koji se dodeljuje ako polje dokumenta ne sadrži validnog korisnika.
   * **Detalj:** Za izbor je dostupna padajuća lista svih dostupnih korisnika. Ovaj korisnik će biti dodeljen ako je polje dokumenta prazno ili ne sadrži validnog korisnika.

## **Funkcionalnost:**

* **Procena uslova:**\
  Kartica izvršava svoju akciju samo ako se oba odeljka, **"Where"** i **"And"**, procene kao tačna.
* **Dodela korisnika zasnovana na polju:**\
  Kartica prvo pokušava da dodeli zadatak ili akciju korisniku identifikovanom u **Field Name**.
* **Dodela rezervnog korisnika:**\
  Ako polje ne sadrži validnog korisnika (ili je prazno), kartica dodeljuje zadatak rezervnom korisniku izabranom iz padajuće liste **User (Fallback)**.

## **Podešavanje i konfiguracija:**

* **Izbor imena polja:**\
  Izaberite **polje dokumenta** koje navodi korisnika za dodelu.
* **Izbor rezervnog korisnika:**\
  Izaberite **rezervnog korisnika** iz padajuće liste. Ovom korisniku će biti dodeljen zadatak ako polje dokumenta ne sadrži validnog korisnika.

## **Zaključak:**

Kartica radnog toka **"Assign User from Field with Fallback"** obezbeđuje da zadatak ili akcija uvek budu dodeljeni validnom korisniku. Ako korisnik u polju dokumenta nije dostupan, automatski se dodeljuje rezervni korisnik, pružajući fleksibilnost i obezbeđujući završetak zadatka.
