# Any / All Quantity

<figure><img src="../../../../.gitbook/assets/image (269).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (270).png" alt="" width="563"><figcaption></figcaption></figure>

## **Svrha:**

Ova kartica radnog toka je dizajnirana da uporedi količinu u dokumentu sa tolerancijom definisanom u nalogu za nabavku. Omogućava korisnicima da procene da li količina ispunjava određene uslove, kao što su jednakost ili prekoračenje navedene tolerancije. U Verziji 4, kartica proširuje funkcionalnost dodavanjem mogućnosti poređenja više entiteta, uključujući nalog za nabavku, primljene količine i količine u dokumentu, nudeći veću fleksibilnost u rukovanju različitim scenarijima.

## **Komponente kartice:**

1. **Any / All:**
   * **Opis**: Navodi kako poređenje treba primeniti na više stavki ili uslova.
   * **Opcije**:
     * **Any**: Najmanje jedan od uslova mora biti tačan da bi se akcija pokrenula.
     * **All**: Svi uslovi moraju biti tačni da bi se akcija nastavila.
2. **Operator:**
   * **Opis**: Definiše uslov koji će se primeniti za poređenje količine u dokumentu sa navedenom tolerancijom.
   * **Opcije**:
     * **Equals (=)**: Proverava da li se količina poklapa sa navedenom vrednošću tolerancije.
     * **Not Equals (≠)**: Obezbeđuje da se količina razlikuje od navedene vrednosti tolerancije.
     * **Greater Than (>)**: Proverava da li je količina veća od navedene tolerancije.
     * **Greater or Equals (≥)**: Proverava da li je količina veća ili jednaka navedenoj toleranciji.
     * **Lesser Than (<)**: Proverava da li je količina manja od navedene tolerancije.
     * **Lesser or Equals (≤)**: Proverava da li je količina manja ili jednaka navedenoj toleranciji.
3. **Iznos tolerancije:**
   * **Opis**: Navodi vrednost tolerancije sa kojom će se uporediti količina u dokumentu.
   * **Detalj**: Ova vrednost je numerička i predstavlja prag dozvoljenog odstupanja u količini
4. **Tip tolerancije:**
   * **Opis**: Definiše tip tolerancije koji će se primeniti.
   * **Opcije**:
     * **Percentage**: Tolerancija se izračunava kao procenat količine u nalogu za nabavku.
     * **Value**: Tolerancija se navodi kao fiksna numerička vrednost.

## **Dodatne komponente u Verziji 4:**

* **Comparison Type**: Bira entitete za poređenje, pružajući veću fleksibilnost u načinu na koji se količine procenjuju u Verziji 4.
  * **Purchase Order to Document**: Upoređuje količinu u nalogu za nabavku sa količinom u povezanom dokumentu.
  * **Received to Document**: Upoređuje primljenu količinu sa količinom u dokumentu.
  * **Purchase Order to Received**: Upoređuje količinu iz naloga za nabavku sa primljenom količinom.

## **Funkcionalnost:**

* **Procena uslova:** Sistem upoređuje količinu u dokumentu sa tolerancijom u nalogu za nabavku na osnovu izabranog operatora i iznosa/tipa tolerancije. U Verziji 4, **Comparison Type** omogućava poređenje različitih količina, kao što su nalog za nabavku prema primljenom, ili nalog za nabavku prema dokumentu, pružajući dinamičnije poređenje.
* **Izvršavanje akcije:**
  * **Tačan uslov**: Ako poređenje rezultira tačnim (npr. količina u dokumentu je unutar prihvatljivog opsega tolerancije), radni tok će se nastaviti.
  * **Netačan uslov**: Ako poređenje rezultira netačnim (npr. količina ne ispunjava toleranciju), radni tok se neće nastaviti.

## **Podešavanje i konfiguracija:**

**Verzija 3:**

* Korisnici konfigurišu karticu izborom količine iz dokumenta, definisanjem iznosa i tipa tolerancije i izborom odgovarajućeg operatora za poređenje količine sa tolerancijom. Kartica procenjuje da li je količina unutar praga tolerancije i nastavlja sa "Tačnom" ili "Netačnom" akcijom na osnovu rezultata.

**Verzija 4:**

* Pored konfiguracije iz Verzije 3, korisnici mogu izabrati **Comparison Type**, omogućavajući poređenja između različitih entiteta, kao što su:
  * **Purchase Order to Document**
  * **Received to Document**
  * **Purchase Order to Received**

## **Primer scenarija:**

Faktura pokazuje da je isporučeno 100 jedinica, ali je nalog za nabavku odobrio samo 90 jedinica. Iznos tolerancije je postavljen na 10 jedinica, a tip tolerancije je apsolutni.

* **Verzija 3**: Kartica upoređuje 100 jedinica iz dokumenta sa tolerancijom naloga za nabavku od 90 jedinica. Ako količina prekorači toleranciju, kartica označava nepodudaranje za dalji pregled.
* **Verzija 4**: Kartica bi mogla uporediti **količinu iz naloga za nabavku** (90 jedinica) sa **primljenom količinom** (100 jedinica) ili **količinom iz dokumenta** (100 jedinica). U zavisnosti od izabranog **Comparison Type**, ona proverava da li razlika između dva entiteta prekoračuje toleranciju i pokreće odgovarajuću akciju.

## **Zaključak:**

* **Verzija 3**: Ova kartica radnog toka upoređuje količinu iz dokumenta sa tolerancijom naloga za nabavku, pomažući da se nepodudaranja u količini označe i obrade na odgovarajući način.
* **Verzija 4**: Proširuje ovu funkcionalnost omogućavajući korisnicima da uporede različite entitete, kao što su nalog za nabavku prema primljenom ili nalog za nabavku prema dokumentu, pružajući veću fleksibilnost u rukovanju složenijim scenarijima. Verzija 4 obezbeđuje strožiju kontrolu nad radnim tokovima nabavke i prijema, nudeći dinamičnija poređenja i akcije na osnovu izabranog tipa poređenja.
