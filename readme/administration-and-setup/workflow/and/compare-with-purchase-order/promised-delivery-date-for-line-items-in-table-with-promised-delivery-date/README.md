# Promised delivery date for line items in table with promised delivery date

<figure><img src="../../../../../.gitbook/assets/image (3).png" alt="" width="375"><figcaption></figcaption></figure>

## Svrha:

Ova kartica radnog toka je dizajnirana da proveri **obećani datum isporuke stavki** u odnosu na **obećani datum isporuke na nalogu za nabavku**, koristeći operatore poređenja i podesiva pravila tolerancije. Omogućava radnim tokovima da automatski otkriju usklađene, rane ili kasne datume isporuke i da u skladu sa tim reaguju.

## Komponente kartice:

1. **Operator**
   * **Opis:**\
     Definiše kako se obećani datum isporuke stavke upoređuje sa obećanim datumom isporuke iz naloga za nabavku.
   * **Opcije:**
     * **Equals (=):** Datum stavke mora pasti unutar prozora tolerancije.
     * **Not Equals (≠):** Datum stavke mora pasti izvan prozora tolerancije.
     * **Greater Than (>):** Datum stavke mora biti posle prozora tolerancije.
     * **Greater or Equals (≥):** Datum stavke mora biti na ili posle početka prozora tolerancije.
     * **Lesser Than (<):** Datum stavke mora biti pre prozora tolerancije.
     * **Lesser or Equals (≤):** Datum stavke mora biti na ili pre kraja prozora tolerancije.<br>
2. **Tolerance Days**
   * **Opis:**\
     Navodi broj dana koji se koristi za izračunavanje prihvatljivog prozora tolerancije oko obećanog datuma isporuke iz naloga za nabavku.
   * **Detalj:**\
     Ova vrednost je ceo broj i definiše koliko se dana pre i posle datuma naloga za nabavku uzima u obzir tokom validacije.<br>
3. **Allowed Tolerance Days**
   * **Opis:**\
     Definiše koji se radni dani računaju pri izračunavanju dana tolerancije.
   * **Detalj:**\
     Korisnici mogu izabrati određene radne dane (na primer, od ponedeljka do petka). Samo izabrani dani se uključuju pri izračunavanju prozora tolerancije.

### Funkcionalnost:

* **Procena uslova:** Sistem izračunava prozor tolerancije oko obećanog datuma isporuke iz naloga za nabavku na osnovu konfigurisanih **Tolerance Days** i **Allowed Tolerance Days**.\
  Obećani datum isporuke svake stavke se zatim upoređuje sa ovim prozorom koristeći izabrani operator.
* Izvršavanje akcije:
  * **Tačan uslov:** Ako je razlika u datumu isporuke unutar opsega tolerancije i poklapa se sa uslovom postavljenim operatorom, radni tok se nastavlja.
  * **Netačan uslov:** Ako uslov nije ispunjen, radni tok se neće nastaviti.

### Podešavanje i konfiguracija:

* Izaberite odgovarajući operator poređenja.
* Unesite broj dana tolerancije.
* Izaberite koji radni dani treba da se računaju kao dani tolerancije.

### Zaključak:

Kartica radnog toka **Compare with Purchase Order – Promised Delivery Date for Line Items** pruža fleksibilan način za sprovođenje pravila o datumima isporuke. Kombinovanjem operatora sa rukovanjem tolerancijom koje uzima u obzir radne dane, ona omogućava preciznu validaciju obaveza isporuke uz smanjenje ručnih provera i izuzetaka.
