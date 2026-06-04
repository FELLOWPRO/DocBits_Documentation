# Calculate in



<figure><img src="../../../../.gitbook/assets/image (295).png" alt="" width="563"><figcaption></figcaption></figure>

## **Svrha:**

Kartica radnog toka **"Calculate with Regex Dependency"** omogućava korisnicima da vrše proračune između kolona u izabranoj tabeli, sa dodatnim uslovom zasnovanim na obrascu regularnog izraza (regex) koji se primenjuje na kolonu zavisnosti. Ako se obrazac poklopi, proračun se vrši, i rezultat se čuva u navedenoj koloni rezultata.

## **Komponente kartice:**

1. **Table Name**
   * **Opis:** Navodi **tabelu** u kojoj će se kolone proračunati.
   * **Detalj:** Za izbor je dostupna padajuća lista svih dostupnih **tabela**.
2. **Column Name (1st Column)**
   * **Opis:** Navodi **prvu kolonu** koja učestvuje u proračunu.
   * **Detalj:** Za izbor je dostupna lista svih dostupnih **kolona**.
3. **Operation**
   * **Opis:** Definiše matematičku operaciju koja se primenjuje između izabranih kolona.
   * **Opcije:**
     * **Add (+):** Dodaje vrednost druge kolone vrednosti prve kolone.
     * **Subtract (-):** Oduzima vrednost druge kolone od prve kolone.
     * **Multiply (\*):** Množi vrednost prve kolone vrednošću u drugoj koloni.
     * **Divide (/):** Deli vrednost prve kolone drugom kolonom.
4. **Column Name (2nd Column)**
   * **Opis:** Navodi **drugu kolonu** koja učestvuje u proračunu.
   * **Detalj:** Za izbor je dostupna lista svih dostupnih **kolona**.
5. **Column Name (Dependency)**
   * **Opis:** Navodi **kolonu zavisnosti** na koju će se primeniti regex obrazac.
   * **Detalj:** Za poklapanje obrasca dostupna je lista svih dostupnih **kolona**.
6. **Regex Pattern**
   * **Opis:** Definiše **regex obrazac** koji će se koristiti za poklapanje sa kolonom zavisnosti.
   * **Detalj:** Ako se vrednost u koloni zavisnosti poklopi sa regex obrascem, proračun će se izvršiti.
7. **Result Column**
   * **Opis:** Navodi **kolonu rezultata** u kojoj će se sačuvati rezultat proračuna.
   * **Detalj:** Ovo može biti nova ili postojeća kolona u kojoj će se sačuvati izračunata vrednost.

## **Funkcionalnost:**

* **Procena uslova:**
  * Kartica izvršava svoju akciju samo ako se oba odeljka, **"Where"** i **"And"**, procene kao tačna.
  * Kartica izvršava svoju akciju samo ako se vrednost u koloni zavisnosti poklapa sa datim **regex obrascem**.
* **Proračun kolona:**\
  Ako se regex obrazac poklopi, kartica vrši izabranu matematičku operaciju između dve izabrane kolone.
* **Čuvanje rezultata:**\
  Rezultat proračuna se čuva u izabranoj **koloni rezultata**.

## **Podešavanje i konfiguracija:**

* **Izbor tabele:**\
  Izaberite **tabelu** u kojoj će se kolone proračunati.
* **Izbor kolona:**\
  Izaberite **prvu kolonu** i **drugu kolonu** koje će se koristiti u proračunu.
* **Izbor operacije:**\
  Izaberite matematičku operaciju (**Add (+)**, **Subtract (-)**, **Multiply (\*)**, **Divide (/)**) koja se primenjuje između kolona.
* **Izbor kolone zavisnosti:**\
  Izaberite **kolonu zavisnosti** na koju će se primeniti regex obrazac.
* **Definisanje regex obrasca:**\
  Unesite **regex obrazac** sa kojim kolona zavisnosti treba da se poklopi.
* **Izbor kolone rezultata:**\
  Izaberite **kolonu rezultata** u kojoj će se sačuvati izračunata vrednost.

## **Zaključak:**

Kartica radnog toka **"Calculate with Regex Dependency"** pruža moćan način za vršenje proračuna sa uslovnom logikom zasnovanom na regex obrascu. Ovo obezbeđuje da samo redovi u kojima se kolona zavisnosti poklapa sa navedenim obrascem prolaze kroz navedeni proračun, a rezultat se čuva u izabranoj koloni rezultata.
