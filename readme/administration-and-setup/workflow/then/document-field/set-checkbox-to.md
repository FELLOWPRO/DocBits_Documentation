# Set Checkbox to

<figure><img src="../../../../.gitbook/assets/image (279).png" alt="" width="563"><figcaption></figcaption></figure>

## **Svrha:**

Ova kartica radnog toka je dizajnirana da postavi polje za potvrdu na navedenu vrednost (true ili false) na osnovu uslova definisanih u odeljcima **"Where"** i **"And"**. Pruža jednostavan ali efikasan način za automatizaciju ažuriranja polja za potvrdu kada su određeni kriterijumi ispunjeni, obezbeđujući pojednostavljenu obradu dokumenata.

## **Komponente kartice:**

1. **Field Name:**
   * **Opis**: Navodi polje u kojem će se postaviti polje za potvrdu.
   * **Detalj**: Polje za potvrdu koje treba ažurirati identifikuje se imenom polja.
2. **Boolean**
   * **Opis**: Definiše vrednost na koju će polje za potvrdu biti postavljeno kada su uslovi u odeljcima **"Where"** i **"And"** oba tačna.
   * **Opcije**:
     * **True**: Polje za potvrdu će biti postavljeno na **true** ako su uslovi ispunjeni.
     * **False**: Polje za potvrdu će biti postavljeno na **false** ako su uslovi ispunjeni.

## **Funkcionalnost:**

* **Procena uslova**: Sistem procenjuje uslove u oba odeljka, **"Where"** i **"And"**&#x20;
* **Izvršavanje akcije**: Ako se oba odeljka, **"Where"** i **"And"**, procene kao tačna, polje za potvrdu će biti ažurirano na navedenu vrednost (true ili false). Ako je bilo koji uslov netačan, ne preduzimaju se nikakve akcije, i polje za potvrdu ostaje kakvo je bilo.

## **Podešavanje i konfiguracija:**

Da bi konfigurisali ovu karticu, korisnici treba da:

1. **Navedu ciljno polje za potvrdu** koje će biti postavljeno na true ili false kada su uslovi ispunjeni.
2. **Izaberu vrednost (true ili false)** na koju će polje za potvrdu biti postavljeno nakon procene uslova.
3. Kartica izvršava svoju akciju samo ako su oba uslova u odeljcima **"Where"** i **"And"** procenjena kao tačna.

## **Zaključak:**

Kartica radnog toka **"Set Checkbox"** je jednostavan i efikasan alat za automatizaciju za ažuriranje polja za potvrdu na osnovu određenih uslova. Obezbeđivanjem da su oba odeljka, **"Where"** i **"And"**, ispunjena, ona omogućava korisnicima da automatizuju procese i smanje ručnu intervenciju, obezbeđujući neometaniju i efikasniju obradu dokumenata.
