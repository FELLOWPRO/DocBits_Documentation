# Assign document to User

<figure><img src="../../../../.gitbook/assets/image (300).png" alt="" width="563"><figcaption></figcaption></figure>

## **Svrha:**

Kartica radnog toka **"Assign Document to User"** omogućava korisnicima da dodele dokument određenom korisniku, obezbeđujući neometano upravljanje radnim tokom usmeravanjem dokumenata odgovarajućoj osobi. Verzija 3 dodaje mogućnost korišćenja stabla odlučivanja za dinamičko određivanje dodele korisnika na osnovu dostupnih uslova.

## **Komponente kartice:**

1. **User**
   * **Opis:** Navodi korisnika kome će dokument biti dodeljen.
   * **Detalj:** Za izbor je dostupna padajuća lista svih dostupnih korisnika. Izabranom korisniku će biti dodeljen dokument za dalju akciju.

## **Dodatne komponente u Verziji 3:**

1. **Use Decision Tree**
   * **Opis:** Ako je omogućeno, kartica koristi stablo odlučivanja za dinamičko određivanje dodele korisnika.
   * **Opcije:**
     * **True:** Koristi stablo odlučivanja za dinamičku dodelu korisnika.
     * **False:** Dodeljuje dokument izabranom korisniku bez korišćenja stabla odlučivanja.

## **Funkcionalnost:**

* **Procena uslova:**\
  Kartica izvršava svoju akciju samo ako se oba odeljka, **"Where"** i **"And"**, procene kao tačna.
* **Dodela dokumenta:**\
  Kartica dodeljuje dokument izabranom korisniku, obezbeđujući da zadatak bude usmeren odgovarajućoj osobi za akciju. Ovo pomaže sa odgovornošću i efikasnim upravljanjem dokumentima.
* **Stablo odlučivanja (Verzija 3):**\
  Ako je stablo odlučivanja omogućeno, kartica procenjuje uslove definisane unutar stabla da bi dinamično izabrala korisnika za dodelu dokumenta.

## **Podešavanje i konfiguracija:**

* **Izbor korisnika:**\
  Izaberite **korisnika** iz padajuće liste kome će dokument biti dodeljen.
* **Korišćenje stabla odlučivanja (Verzija 3):**\
  Omogućite ili onemogućite korišćenje stabla odlučivanja za dinamički izbor korisnika.

## **Zaključak:**

Kartica radnog toka **"Assign Document to User"** olakšava efikasno usmeravanje dokumenata dodeljivanjem izabranom korisniku, sa dodatnom fleksibilnošću u Verziji 3 da se dinamično odredi korisnik pomoću stabla odlučivanja. Ovo obezbeđuje prilagodljiviji i efikasniji proces radnog toka.
