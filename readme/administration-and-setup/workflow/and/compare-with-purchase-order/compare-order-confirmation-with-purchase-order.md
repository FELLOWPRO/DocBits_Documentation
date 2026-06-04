# Compare Order Confirmation with Purchase order

<figure><img src="../../../../.gitbook/assets/image (8) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (267).png" alt="" width="563"><figcaption></figcaption></figure>

## Svrha:

Ova DocBits kartica je dizajnirana da uporedi određeno polje podataka porudžbine — kao što su količina, popust ili jedinična cena — između potvrde porudžbine i naloga za nabavku. Omogućavanjem fokusiranog poređenja jednog po jednog polja, ona obezbeđuje preciznost u validaciji ključnih tačaka podataka, održavajući tačnost porudžbine. **Verzija 4** proširuje ovu funkcionalnost omogućavajući poređenja između različitih entiteta kao što su nalog za nabavku, primljene količine i sam dokument, dodajući veću fleksibilnost i kontrolu radnom toku.

## Komponente kartice:

1. **Any/All**&#x20;
   * **Opis:** Određuje da li se uslov primenjuje na bilo koju ili sve linije u potvrdi porudžbine.\
     **Opcije:**
     * **Any**: Poređenje će se pokrenuti ako se vrednost izabranog polja u bilo kojoj liniji potvrde porudžbine poklapa sa odgovarajućom vrednošću u nalogu za nabavku.
     * **All**: Poređenje će se pokrenuti samo ako se vrednost izabranog polja u svim linijama potvrde porudžbine poklapa sa odgovarajućom vrednošću u nalogu za nabavku.
2. **Order Data Field**
   * **Opis**: Navodi polje podataka koje treba uporediti između potvrde porudžbine i naloga za nabavku.
   * **Detalj**: Korisnici mogu izabrati jedno od sledećih polja za poređenje:
     * **Quantity**: Upoređuje naručenu količinu sa potvrđenom količinom.
     * **Discount**: Proverava da li se popust u potvrdi poklapa sa nalogom za nabavku.
     * **Unit Price**: Obezbeđuje da je jedinična cena u potvrdi usklađena sa nalogom za nabavku.
3. **Operator**
   * **Opis**: Definiše uslov koji se primenjuje na poređenje izabranog polja podataka.
   * **Opcije**:
     * **Equals (=)**: Potvrđuje da se vrednost poklapa sa nalogom za nabavku.
     * **Not Equals (≠)**: Obezbeđuje da se vrednost razlikuje od naloga za nabavku.
     * **Greater Than (>)**: Proverava da li vrednost prekoračuje vrednost naloga za nabavku.
     * **Greater or Equals (≥)**: Potvrđuje da je vrednost jednaka ili veća od vrednosti naloga za nabavku.
     * **Less Than (<)**: Proverava da li je vrednost ispod vrednosti naloga za nabavku.
     * **Less or Equals (≤)**: Potvrđuje da je vrednost ispod ili jednaka vrednosti naloga za nabavku.

## **Dodatne komponente u Verziji 4**:

* **Comparison Type**: Bira entitete za poređenje. Opcije uključuju:
  * **Purchase Order to Document**: Upoređuje podatke naloga za nabavku sa povezanim dokumentom.
  * **Received to Document**: Upoređuje primljene podatke (npr. primljene količine) sa dokumentom.
  * **Purchase Order to Received**: Upoređuje podatke naloga za nabavku sa primljenim količinama.

## Funkcionalnost:

* **Poređenje polja**: Sistem upoređuje izabrano polje podataka porudžbine (Unit Price, Discount ili Quantity) iz potvrde porudžbine sa odgovarajućom vrednošću u nalogu za nabavku.
* **Izvršavanje akcije**: Na osnovu rezultata poređenja i uslova operatora, kartica može pokrenuti naredne akcije, kao što su obaveštenja ili upozorenja.

## Primer scenarija:

* Potvrda porudžbine navodi **jediničnu cenu** od $50, dok nalog za nabavku navodi $45. Koristeći operator "Greater Than", kartica označava nepodudaranje, omogućavajući timu za nabavku da ga reši pre obrade.

## Zaključak:

Ova kartica pojednostavljuje validaciju pojedinačnih polja podataka porudžbine, obezbeđujući usklađenost sa uslovima naloga za nabavku. Izdvajanjem jednog po jednog polja za poređenje, ona podržava ciljane preglede i sprečavanje grešaka u obradi porudžbina.
