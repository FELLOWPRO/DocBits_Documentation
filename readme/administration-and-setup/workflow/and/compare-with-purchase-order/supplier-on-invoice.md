# Supplier on Invoice

<figure><img src="../../../../.gitbook/assets/image (276).png" alt="" width="563"><figcaption></figcaption></figure>

## **Svrha:**

Ova kartica radnog toka je dizajnirana da uporedi dobavljača na fakturi sa dobavljačem na nalogu za nabavku. Kartica obezbeđuje da dobavljač koji izdaje fakturu bude isti kao onaj naveden u nalogu za nabavku, pomažući u sprečavanju nepodudaranja i grešaka u procesu nabavke.

## **Komponente kartice:**

1. **Operator:**
   * **Opis**: Definiše uslov za poređenje dobavljača na fakturi sa dobavljačem na nalogu za nabavku.
   * **Opcije**:
     * **Is**: Proverava da li se dobavljač na fakturi poklapa sa dobavljačem na nalogu za nabavku.
     * **Is Not**: Obezbeđuje da se dobavljač na fakturi ne poklapa sa dobavljačem na nalogu za nabavku.

## **Funkcionalnost:**

* **Procena uslova:** Sistem upoređuje dobavljača na fakturi sa dobavljačem na nalogu za nabavku na osnovu izabranog operatora. Ako je uslov poređenja tačan (npr. dobavljač je isti ili različit kao što je potrebno), radni tok će se nastaviti u skladu sa tim.
* **Izvršavanje akcije:**
  * **Tačan uslov**: Ako se uslov proceni kao tačan (npr. dobavljač na fakturi se poklapa sa dobavljačem na nalogu za nabavku), radni tok se nastavlja bez pokretanja bilo kakvih grešaka.
  * **Netačan uslov**: Ako se uslov proceni kao netačan (npr. dobavljač na fakturi se ne poklapa sa dobavljačem na nalogu za nabavku), radni tok se neće nastaviti.

## **Podešavanje i konfiguracija:**

* Korisnici biraju odgovarajući operator ("Is" ili "Is Not") da definišu kako će se dobavljači upoređivati.

## **Primer scenarija:**

* Faktura navodi dobavljača sa ID-om "SUP123", a povezani nalog za nabavku takođe navodi "SUP123" kao dobavljača. Koristeći operator "Is", kartica upoređuje dobavljače i utvrđuje da su isti, pa se radni tok nastavlja bez ikakvih problema.

## **Zaključak:**

Kartica radnog toka "Supplier Comparison" obezbeđuje da ispravan dobavljač izdaje fakturu za nalog za nabavku, pomažući u sprečavanju nepodudaranja i grešaka u procesu nabavke. Automatskom proverom informacija o dobavljaču, organizacije mogu pojednostaviti svoj proces odobravanja faktura i smanjiti rizik od prevare ili grešaka u fakturisanju dobavljača.
