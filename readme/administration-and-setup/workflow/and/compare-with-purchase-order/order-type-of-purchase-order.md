# Order Type of Purchase Order

<figure><img src="../../../../.gitbook/assets/image (277).png" alt="" width="563"><figcaption></figcaption></figure>

## **Svrha:**

Ova kartica radnog toka je dizajnirana da uporedi tip porudžbine naloga za nabavku sa navedenom vrednošću. Kartica proverava da li tip porudžbine naloga za nabavku ispunjava navedeni uslov (npr. da li je jednak, nije jednak, veći je ili ispunjava drugi uslov) kako bi se obezbedilo da nalog za nabavku bude ispravno klasifikovan. Ovo poređenje može pokrenuti akcije na osnovu određenih uslova, kao što je usmeravanje porudžbine na dalji pregled ili odobrenje ako se pronađu nepodudaranja.

## **Komponente kartice:**

1. **Any/All:**
   * **Opis**: Definiše da li se uslov primenjuje na bilo koji ili na sve naloge za nabavku koji se procenjuju u radnom toku.
   * **Opcije**:
     * **Any**: Uslov je ispunjen ako bilo koji od naloga za nabavku ispunjava navedeni uslov.
     * **All**: Uslov je ispunjen samo ako svi nalozi za nabavku ispunjavaju navedeni uslov.
2. **Operator:**
   * **Opis**: Definiše uslov koji će se primeniti za poređenje tipa porudžbine sa navedenom vrednošću.
   * **Opcije**:
     * **Equals (=)**: Proverava da li se tip porudžbine poklapa sa navedenom vrednošću.
     * **Not Equals (≠)**: Obezbeđuje da se tip porudžbine razlikuje od navedene vrednosti.
3. **Order Type:**
   * **Opis**: Navodi vrednost sa kojom će se uporediti tip porudžbine naloga za nabavku.
   * **Detalj**: Vrednost mora da se poklapa sa tipom porudžbine ili klasifikacijom u sistemu.

## **Funkcionalnost:**

* **Procena uslova:** Sistem procenjuje tip porudžbine naloga za nabavku u odnosu na navedeni uslov koristeći izabrani operator. Ako se tip porudžbine poklapa (ili ne poklapa) sa navedenom vrednošću, radni tok se nastavlja u skladu sa tim.
* **Izvršavanje akcije:**
  * **Tačan uslov**: Ako se uslov proceni kao tačan (npr. tip porudžbine se poklapa sa navedenom vrednošću), radni tok će se nastaviti, moguće pokretanjem dodatnih akcija ili koraka obrade.
  * **Netačan uslov**: Ako se uslov proceni kao netačan (npr. tip porudžbine se ne poklapa sa navedenom vrednošću), radni tok se neće nastaviti.

## **Podešavanje i konfiguracija:**

* Korisnici konfigurišu karticu izborom polja tipa porudžbine naloga za nabavku i izborom operatora koji definiše kako će se tip porudžbine upoređivati. Zatim postavljaju navedenu vrednost i odlučuju da li će primeniti uslov na bilo koju ili sve linije naloga za nabavku.

## **Primer scenarija:**

* Nalog za nabavku ima tip porudžbine "Standard". Radni tok je konfigurisan da proveri da li je tip porudžbine "Urgent". Koristeći operator "Equals", kartica upoređuje tip porudžbine i utvrđuje da se ne poklapa sa navedenom vrednošću, pokrećući radni tok da pošalje porudžbinu na pregled zbog nepodudaranja.

## **Zaključak:**

Kartica radnog toka "Order Type of Purchase Order" obezbeđuje da nalozi za nabavku budu ispravno klasifikovani u skladu sa svojim navedenim tipom porudžbine. Automatizacijom poređenja tipova porudžbina, organizacije mogu obezbediti da se nalozi za nabavku obrađuju u skladu sa svojim očekivanim klasifikacijama, pomažući u sprovođenju usklađenosti i pojednostavljenju radnih tokova nabavke.
