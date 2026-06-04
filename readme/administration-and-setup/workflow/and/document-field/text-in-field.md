# Text in Field

<figure><img src="../../../../.gitbook/assets/image (10) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Svrha:**

Ova kartica radnog toka je dizajnirana da automatizuje akcije na osnovu prisustva ili odsustva određenog teksta unutar navedenog polja dokumenta. Obezbeđuje da se radni tokovi mogu dinamično prilagoditi sadržaju dokumenata, podržavajući efikasnu obradu i tačno donošenje odluka.

## **Komponente kartice:**

1. **Text**
   * **Opis:** Navodi tekstualni niz koji treba proveriti unutar polja.
   * **Detalj:** Ovo može biti reč, fraza ili niz znakova relevantan za radni tok.
2. **Operator**
   * **Opis:** Definiše uslov za prisustvo teksta u polju.
   * **Opcije:**
     * **Is:** Pokreće radni tok ako je navedeni tekst prisutan u polju.
     * **Is Not:** Pokreće radni tok ako navedeni tekst nije prisutan u polju.
3. **Field Name**
   * **Opis:** Navodi ime polja dokumenta koje treba proceniti.
   * **Detalj:** Ovo mora da se poklapa sa tačnim identifikatorom polja unutar dokumenta.

## **Funkcionalnost:**

1. **Procena uslova:** Sistem proverava da li navedeni tekst postoji u polju, na osnovu izabranog operatora (Is ili Is Not).
2. **Izvršavanje akcije:**
   * **Tačan uslov:**\
     Ako se prisustvo teksta u polju poklapa sa navedenim uslovom, sistem pokreće povezane akcije. One mogu uključivati pokretanje upozorenja, napredovanje radnih tokova ili ažuriranje zapisa.
   * **Netačan uslov:**\
     Ako se prisustvo teksta u polju ne poklapa sa uslovom, mogu se preduzeti alternativne akcije ili nikakve akcije, u zavisnosti od konfiguracije radnog toka.

## **Podešavanje i konfiguracija:**&#x20;

* Korisnik unosi tekst koji treba proveriti. Zatim bira ime polja relevantnog dokumenta.

## **Zaključak:**

Kartica radnog toka "Text Presence in Field" je jednostavan ali moćan alat za analizu sadržaja dokumenta. Automatizacijom akcija na osnovu detekcije teksta, ova kartica podržava inteligentnije radne tokove, poboljšava tačnost rukovanja dokumentima i smanjuje ručni rad.
