# Document Type Operation one of

<figure><img src="../../../../.gitbook/assets/userlmn_14ab8ac5e693d9bbe68d178795d12a9f (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Svrha:**

Ova kartica je dizajnirana da upravlja akcijama nad dokumentima u zavisnosti od njihovog tipa, koristeći jednostavnu uslovnu logiku (is/is not) da pokrene ili spreči određene radne tokove. Ovo omogućava preciznu kontrolu nad time kako se različiti tipovi dokumenata obrađuju unutar ERP sistema.

## **Komponente kartice:**

1. **Operator**
   * **Opis**: Određuje uslovnu logiku koja se primenjuje na tipove dokumenata.
   * **Opcije**:
     * **is**: Operacija će se pokrenuti ako se tip dokumenta poklapa sa jednim od navedenih tipova u listi.
     * **is not**: Operacija će se pokrenuti ako se tip dokumenta ne poklapa ni sa jednim od navedenih tipova.
2. **Lista tipova dokumenata**
   * **Opis**: Navodi listu tipova dokumenata na koje će se uslov primeniti.
   * **Detalj**: Ovo uključuje različite tipove dokumenata kao što su "Invoice", "Purchase Order", itd., na osnovu kojih će se uslov (is/is not) proceniti.

## Funkcionalnost:

* **Procena uslova:** Sistem proverava da li se tip dokumenta poklapa sa uslovom operatora (is ili is not) u odnosu na navedenu listu tipova dokumenata.
* **Izvršavanje akcije:**
  * **Tačan uslov:**\
    Ako tip dokumenta zadovoljava navedeni uslov (bilo is ili is not u listi), radni tok se nastavlja. Ovo može pokrenuti procese kao što su odobrenja dokumenata, određene validacije ili akcije usmeravanja.
  * **Netačan uslov:**\
    Ako tip dokumenta ne ispunjava uslov, izvršavaju se alternativne akcije, kao što su odbijanje dokumenta ili zaustavljanje radnog toka.

## Podešavanje i konfiguracija:

* Korisnici konfigurišu karticu izborom polja tipa dokumenta i definisanjem operatora (is ili is not). Zatim navode listu tipova dokumenata za proveru. Podešavanje je jednostavno, uključuje padajuće menije za izbor polja i operatora i polje za unos liste tipova dokumenata.

## Zaključak:

Kartica radnog toka "Document Type Condition" igra ključnu ulogu u upravljanju operacijama zasnovanim na dokumentima sa preciznošću i fleksibilnošću. Korišćenjem jednostavne uslovne logike, ona pomaže da se obezbedi da se dokumenti obrađuju na odgovarajući način, poboljšavajući efikasnost i usklađenost. Jasno dokumentovanje ove kartice pomoći će korisnicima da razumeju kako da je efikasno implementiraju i koriste, čineći je vrednim delom dokumentacije vašeg ERP sistema.
