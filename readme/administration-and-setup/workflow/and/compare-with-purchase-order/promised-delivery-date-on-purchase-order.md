# Promised Delivery Date on Purchase Order

<figure><img src="../../../../.gitbook/assets/image (7) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Svrha**

Ova DocBits kartica je dizajnirana da olakša precizno poređenje obećanih datuma isporuke na nalozima za nabavku sa datumima isporuke navedenim za stavke u tabeli. Integracijom vrednosti tolerancije, kartica obezbeđuje fleksibilnost u praćenju vremenskih rokova isporuke, pomažući u održavanju tačnosti planiranja zaliha i zadovoljstva kupaca.

## **Komponente kartice**

1. **Operator**
   * **Opis:** Definiše uslov koji se primenjuje za poređenje datuma isporuke.
   * **Opcije:**
     * **Equals (=):** Proverava da li se obećani datum isporuke na stavci poklapa sa datumom isporuke iz naloga za nabavku.
     * **Not Equal (≠):** Obezbeđuje da se obećani datum isporuke na stavci ne poklapa sa datumom iz naloga za nabavku.
     * **Greater Than (>):** Proverava da li je obećani datum isporuke stavke kasniji od datuma isporuke iz naloga za nabavku.
     * **Greater or Equals (≥):** Proverava da li je obećani datum isporuke stavke jednak ili kasniji od datuma isporuke iz naloga za nabavku.
     * **Less Than (<):** Potvrđuje da li je obećani datum isporuke stavke raniji od datuma isporuke iz naloga za nabavku.
     * **Less or Equals (≤):** Proverava da li je obećani datum isporuke stavke jednak ili raniji od datuma isporuke iz naloga za nabavku.
2. **Value**
   * **Opis:** Navodi dozvoljenu marginu greške u poređenju datuma isporuke.
   * **Detalj:** Korisnici definišu broj dana za koji se datum isporuke stavke može razlikovati od obećanog datuma isporuke.

## **Funkcionalnost**

* **Procena uslova:**\
  Kartica izračunava razliku između obećanog datuma isporuke iz naloga za nabavku i datuma isporuke za stavke u tabeli. Izabrani operator se zatim primenjuje da bi se utvrdilo da li je uslov ispunjen.
* **Izvršavanje akcije:**
  * **Tačan uslov:** Ako je razlika u datumu isporuke unutar opsega tolerancije i poklapa se sa uslovom postavljenim operatorom, radni tok se nastavlja.
  * **Netačan uslov:** Ako uslov nije ispunjen, radni tok se neće nastaviti.

## **Podešavanje i konfiguracija**

* Operator se bira da definiše željeni uslov poređenja, kao što su jednako, veće od ili manje od. Na kraju, korisnici navode vrednost tolerancije u danima, koja dozvoljava male varijacije u poređenju bez pokretanja upozorenja.

## **Primer scenarija**

* Nalog za nabavku navodi obećani datum isporuke 1. decembra. Stavka u tabeli ima obećani datum isporuke 3. decembra. Sa vrednošću tolerancije postavljenom na 2 dana i izabranim operatorom **Equals (≥)**, kartica smatra datum isporuke unutar prihvatljivog opsega. Nijedno upozorenje se ne pokreće, obezbeđujući da se manja odstupanja tolerišu bez ometanja operacija.

## **Zaključak**

Kartica "Promised Delivery Date Comparison" pomaže u pojednostavljenju operacija lanca snabdevanja omogućavajući precizno praćenje vremenskih rokova isporuke. Svojom sposobnošću da uključi tolerancije i fleksibilne operatore poređenja, ona obezbeđuje pridržavanje očekivanja isporuke uz izbegavanje nepotrebnih upozorenja za manja odstupanja. Ovo poboljšava upravljanje dobavljačima i ukupnu efikasnost radnog toka.
