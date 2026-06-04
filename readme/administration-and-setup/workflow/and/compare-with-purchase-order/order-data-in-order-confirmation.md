# Order Data in Order Confirmation

<figure><img src="../../../../.gitbook/assets/image (265).png" alt="" width="563"><figcaption></figcaption></figure>

## **Svrha**

Ova kartica radnog toka je dizajnirana da uporedi određena polja — **Unit Price**, **Discount** ili **Quantity** — između potvrde porudžbine i naloga za nabavku. Ona obezbeđuje doslednost i usklađenost sa dogovorenim uslovima. Na osnovu rezultata poređenja, kartica omogućava korisnicima da upišu navedeni tekst u izabrano polje kada se uslov proceni kao **tačan** ili **netačan**, pojednostavljujući obradu dokumenata i smanjujući ručnu intervenciju.

## **Komponente kartice**

1. **Order Data**
   * **Opis:** Navodi polje koje treba uporediti između potvrde porudžbine i naloga za nabavku.
   * **Opcije:**
     * **Unit Price**: Upoređuje jediničnu cenu u oba dokumenta.
     * **Discount**: Upoređuje procenat ili vrednost popusta.
     * **Quantity**: Upoređuje naručenu količinu.
2. **Operator**
   * **Opis:** Definiše uslov koji se primenjuje tokom poređenja.
   * **Opcije:**
     * **Equals (=):** Proverava da li se vrednost u izabranom polju poklapa između potvrde porudžbine i naloga za nabavku.
     * **Not Equals (≠):** Obezbeđuje da se vrednost u izabranom polju razlikuje između dva dokumenta.
3. **Text**
   * **Opis:** Navodi tekst koji treba upisati u ciljno polje nakon procene uslova.
   * **Detalj:** Ovaj tekst može uključivati prilagođene napomene, ažuriranja statusa ili unapred definisane vrednosti.
4. **Field Name**
   * **Opis:** Navodi polje u koje će tekst biti upisan.
   * **Detalj:** Ciljno polje se bira iz dostupnih polja koja se mogu uređivati u sistemu.
5. **Condition Result**
   * **Opis:** Određuje kada tekst treba upisati, na osnovu rezultata poređenja.
   * **Opcije:**
     * **True:** Upisuje tekst ako je uslov poređenja ispunjen.
     * **False:** Upisuje tekst ako uslov poređenja nije ispunjen.

## **Funkcionalnost**

* **Procena poređenja:** Sistem upoređuje izabrano polje između potvrde porudžbine i naloga za nabavku koristeći navedeni operator.
* **Izvršavanje akcije:** Ako se uslov proceni kao **tačan** ili **netačan**, navedeni tekst se upisuje u određeno polje.

## **Podešavanje i konfiguracija**

* Da bi podesili ovu karticu, korisnici prvo biraju polje koje treba uporediti — **Unit Price**, **Discount** ili **Quantity**. Zatim biraju operator da definišu uslov poređenja, kao što su **equals** ili **not equals**. Korisnici navode tekst koji treba upisati u ciljno polje i biraju kada ova akcija treba da se dogodi, na osnovu rezultata uslova (**true** ili **false**).

## **Primer scenarija**

* Potvrda porudžbine navodi jediničnu cenu od $50 za proizvod, dok nalog za nabavku navodi cenu od $45. Koristeći operator **Not Equals (≠)**, kartica identifikuje nepodudaranje i upisuje tekst "Price Mismatch" u određeno polje kada se uslov proceni kao **tačan**.

## **Zaključak**

Kartica radnog toka "\[Unit Price/Discount/Quantity] in Order Confirmation" pruža praktično rešenje za obezbeđivanje doslednosti dokumenata. Automatskim označavanjem nepodudaranja i upisivanjem relevantnog teksta u navedena polja, ona poboljšava efikasnost i smanjuje greške u procesima upravljanja porudžbinama.
