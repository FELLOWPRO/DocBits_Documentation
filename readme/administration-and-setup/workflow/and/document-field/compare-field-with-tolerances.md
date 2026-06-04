# Compare Field with tolerances

<figure><img src="../../../../.gitbook/assets/image (15) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Svrha:**

Ova kartica radnog toka je dizajnirana da uporedi vrednost polja sa navedenom referentnom vrednošću uz dozvoljavanje tolerancija. Omogućava preciznu uslovnu obradu u radnim tokovima gde su mala odstupanja prihvatljiva, što je čini idealnom za scenarije kao što su osiguranje kvaliteta, finansijska analiza ili akcije zasnovane na pragu.

## **Komponente kartice:**

1. **Field Name**
   * **Opis:** Polje koje treba proceniti u poređenju.
   * **Detalj:** Ovo mora da se poklapa sa tačnim identifikatorom prvog polja unutar dokumenta.
2. **Operator poređenja**
   * **Opis:** Navodi kako će se vrednost izabranog polja upoređivati sa referentnom vrednošću.
   * **Opcije:**
     * **Equals (=):** Proverava da li se vrednost polja tačno poklapa sa referentnom vrednošću.
     * **Not Equals (≠):** Proverava da li se vrednost polja ne poklapa sa referentnom vrednošću.
     * **Greater Than (>):** Proverava da li je vrednost polja veća od referentne vrednosti.
     * **Greater or Equals (≥):** Proverava da li je vrednost polja veća ili jednaka referentnoj vrednosti.
     * **Lesser Than (<):** Proverava da li je vrednost polja manja od referentne vrednosti.
     * **Lesser or Equals (≤):** Proverava da li je vrednost polja manja ili jednaka referentnoj vrednosti.
3. **Referentna vrednost**
   * **Opis:** Vrednost sa kojom se polje upoređuje.
   * **Detalj:** Ova vrednost može biti numerička, tekstualna ili zasnovana na datumu, u zavisnosti od konteksta poređenja.
4. **Iznos tolerancije**
   * **Opis:** Definiše prihvatljivu marginu greške za poređenje.
   * **Detalj:** Iznos tolerancije je numerička vrednost koja označava maksimalno dozvoljenu razliku između dve vrednosti polja da bi se poređenje smatralo tačnim.
5. **Tip tolerancije**
   * **Opis:** Navodi mernu jedinicu za iznos tolerancije.
   * **Opcije:**
     * **Value:** Tolerancija je apsolutna vrednost, što znači da se dva polja mogu razlikovati za navedeni iznos tolerancije.
     * **Percent:** Tolerancija se izračunava kao procenat vrednosti drugog polja, dozvoljavajući relativnu marginu greške.

## **Funkcionalnost:**

* **Procena uslova:** Sistem procenjuje vrednost polja u odnosu na referentnu vrednost koristeći izabrani operator poređenja. Ako je tolerancija konfigurisana, sistem smatra poređenje uspešnim ako vrednost polja pada unutar definisanog opsega tolerancije.
* **Izvršavanje akcije:**
  * **Unutar tolerancije:** Ako vrednost polja zadovoljava uslov unutar navedene tolerancije, radni tok se nastavlja, pokrećući povezane akcije.
  * **Izvan tolerancije:** Ako vrednost polja ne ispunjava uslov ili pada izvan opsega tolerancije, mogu se izvršiti alternativne akcije, kao što su beleženje, slanje upozorenja ili zaustavljanje radnog toka.

## **Podešavanje i konfiguracija:**

* Korisnici konfigurišu karticu izborom polja koje treba proceniti iz liste dostupnih polja i izborom operatora poređenja (npr. jednako, veće od) iz padajuće liste. Zatim navode referentnu vrednost za poređenje i definišu iznos tolerancije, a potom biraju tip tolerancije (npr. procenat ili vrednost).&#x20;

## **Zaključak:**

Kartica "Field Comparison with Tolerances" je svestran alat za radne tokove koji zahtevaju fleksibilne procene. Omogućavanjem poređenja sa tolerancijama, ona obezbeđuje da radni tokovi ostanu efikasni i prilagodljivi, prilagođavajući se stvarnim varijacijama bez ugrožavanja tačnosti.
