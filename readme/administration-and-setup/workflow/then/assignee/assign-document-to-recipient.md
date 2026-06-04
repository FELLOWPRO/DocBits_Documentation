# Assign document to recipient

<figure><img src="../../../../.gitbook/assets/image (301).png" alt="" width="563"><figcaption></figcaption></figure>

## **Svrha:**

Kartica radnog toka **"Assign Document to Disponent / Purchaser"** dodeljuje dokument bilo **disponentu** bilo **nabavljaču**. Ako se ne pronađe validan korisnik, bira se rezervni korisnik kako bi se obezbedilo da dokument uvek bude dodeljen nekome.

## **Komponente kartice:**

1. **Disponent / Purchaser**
   * **Opis:** Navodi da li će dokument biti dodeljen disponentu ili nabavljaču.
   * **Opcije:**
     * **Disponent:** Dodeljuje dokument disponentu.
     * **Purchaser:** Dodeljuje dokument nabavljaču.
2. **Fallback User**
   * **Opis:** Navodi rezervnog korisnika u slučaju da se dokument ne može dodeliti izabranom disponentu ili nabavljaču.
   * **Detalj:** Padajuća lista dostupnih korisnika vam omogućava da izaberete rezervnog korisnika kako biste obezbedili da se dokument dodeli čak i ako se primarni korisnik ne može odrediti.

## **Funkcionalnost:**

* **Procena uslova:**\
  Kartica izvršava svoju akciju samo ako se oba odeljka, **"Where"** i **"And"**, procene kao tačna.
* **Dodela dokumenta:**\
  Kartica dodeljuje dokument bilo **disponentu** bilo **nabavljaču** kako je izabrano. Ako izabrana osoba nije dostupna ili nije validna, dokument se dodeljuje rezervnom korisniku.

## **Podešavanje i konfiguracija:**

* **Izbor Disponent / Purchaser:**\
  Izaberite da li ćete dokument dodeliti **disponentu** ili **nabavljaču**.
* **Izbor rezervnog korisnika:**\
  Izaberite rezervnog korisnika iz padajuće liste koji će primiti dokument ako primarna dodela nije moguća.

## **Zaključak:**

Kartica radnog toka **"Assign Document to Disponent / Purchaser"** obezbeđuje da dokument uvek bude dodeljen, bilo izabranom disponentu/nabavljaču ili, ako je potrebno, rezervnom korisniku. Ovo smanjuje prekide u radnom toku i obezbeđuje da se obrada dokumenata neometano nastavlja.
