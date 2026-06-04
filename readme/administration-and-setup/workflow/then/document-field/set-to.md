# Set to

<figure><img src="../../../../.gitbook/assets/image (278).png" alt="" width="563"><figcaption></figcaption></figure>

## **Svrha:**

Ova kartica radnog toka je dizajnirana da automatski postavi navedeno polje u dokumentu na unapred definisanu tekstualnu vrednost na osnovu uslova definisanih u odeljcima **"Where"** i **"And"**. Omogućava korisnicima da pojednostave unos podataka obezbeđujući da se polja popune doslednim vrednostima kada su određeni kriterijumi ispunjeni.

## **Komponente kartice:**

1. **Field Name**
   * **Opis**: Navodi polje koje će biti ažurirano tekstualnom vrednošću.&#x20;
   * **Detalj**: Izabrano polje će biti ažurirano navedenom tekstualnom vrednošću ako su uslovi u odeljcima **"Where"** i **"And"** ispunjeni.
2. **Text**
   * **Opis**: Definiše tekstualnu vrednost koja će se postaviti u ciljno polje kada se uslovi procene kao tačni.
   * **Detalj**: Ovo može biti prilagođena poruka, status ili unapred definisana vrednost koju korisnik želi da upiše u polje. Tekst treba da bude usklađen sa očekivanim formatom unosa polja (npr. alfanumerički, datum ili drugi tipovi tekstualnih informacija).

## **Funkcionalnost:**

* **Procena uslova**: Sistem procenjuje uslove u odeljcima **"Where"** i **"And"**:
  * Ako su **oba uslova tačna**, izvršiće se akcije definisane u odeljku **"Then"**. Konkretno, ciljno polje (Field Name) će biti popunjeno navedenim tekstom.
  * Ako je **bilo odeljak "Where" ili "And" netačan**, ne preduzima se nikakva akcija, i polje ostaje nepromenjeno. Akcije odeljka **"Then"** se u potpunosti preskaču ako je bilo koji uslov netačan.
* **Izvršavanje akcije**: Ako su oba uslova u odeljcima **"Where"** i **"And"** ispunjena, sistem automatski popunjava navedeno polje izabranom tekstualnom vrednošću. Ako uslovi nisu ispunjeni, ne vrše se nikakve promene polja.

## **Podešavanje i konfiguracija:**

Da bi podesili ovu karticu:

1. **Izaberite polje** (Field Name) koje će biti ažurirano tekstualnom vrednošću. Dostupna polja u dokumentu su navedena za izbor.
2. **Navedite tekstualnu vrednost** koja će se upisati u ciljno polje kada su uslovi tačni.
3. Akcija će se izvršiti samo ako se uslovi oba odeljka, **"Where"** i **"And"**, procene kao tačni.

## **Zaključak:**

Kartica radnog toka **"Set Field to Text"** nudi jednostavan način za automatizaciju popunjavanja tekstualnih vrednosti u određena polja dokumenta na osnovu unapred definisanih uslova. Ovo smanjuje ručni unos podataka i obezbeđuje doslednost u obradi dokumenata, čineći je korisnim alatom za automatizaciju radnih tokova i poboljšanje efikasnosti.
