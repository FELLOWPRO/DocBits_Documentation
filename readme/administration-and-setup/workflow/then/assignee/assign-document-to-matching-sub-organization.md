# Assign document to matching sub organization

<figure><img src="../../../../.gitbook/assets/image (303).png" alt="" width="563"><figcaption></figcaption></figure>

## **Svrha:**

Kartica radnog toka **"Assign Document to Matching Sub-Organization Based on Field"** dinamično dodeljuje dokument pod-organizaciji, na osnovu navedenog polja u dokumentu. Ako se ne pronađe odgovarajuća pod-organizacija, kartica koristi unapred definisanu rezervnu pod-organizaciju.

## **Komponente kartice:**

1. **Field Name**
   * **Opis:** Navodi polje dokumenta koje se koristi za određivanje odgovarajuće pod-organizacije.
   * **Detalj:** Kartica traži vrednost u navedenom polju da bi je uparila sa dostupnom pod-organizacijom.
2. **Sub-Organization (Fallback)**
   * **Opis:** Definiše rezervnu pod-organizaciju koja se koristi ako se ne pronađe poklapanje u navedenom polju.
   * **Detalj:** Ako se vrednost polja ne poklapa ni sa jednom pod-organizacijom, dokument će biti dodeljen izabranoj rezervnoj pod-organizaciji.

## **Funkcionalnost:**

* **Procena uslova:**\
  Kartica izvršava svoju akciju samo ako se oba odeljka, **"Where"** i **"And"**, procene kao tačna.
* **Dinamička dodela:**\
  Kartica proverava vrednost navedenog polja i dodeljuje dokument pod-organizaciji koja se poklapa sa ovom vrednošću.
* **Mehanizam rezerve:**\
  Ako se ne pronađe odgovarajuća pod-organizacija, dokument se dodeljuje rezervnoj pod-organizaciji.

## **Podešavanje i konfiguracija:**

* **Izbor imena polja:**\
  Izaberite polje iz dokumenta koje sadrži vrednost za uparivanje sa pod-organizacijom.
* **Izbor rezervne pod-organizacije:**\
  Izaberite pod-organizaciju koja će se koristiti ako se ne pronađe poklapanje u polju dokumenta.

## **Zaključak:**

Kartica radnog toka **"Assign Document to Matching Sub-Organization Based on Field"** nudi fleksibilnost dinamičkim usmeravanjem dokumenata odgovarajućoj pod-organizaciji, sa dodatnom rezervnom opcijom kako bi se obezbedilo da nijedan dokument ne ostane nedodeljen.
