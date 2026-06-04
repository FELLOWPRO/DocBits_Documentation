# Pokreni DocOperator Prompt (Automatizacioni skript)

---

Dodajte ovu karticu u grupu **Then** u Workflow Builder-u — akcije koje se pokreću kada se When/And uslovi poklope:

<figure><img src="../../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow Builder platno sa grupama kartica When, And i Then"><figcaption><p>Kartica <strong>Run DocOperator Prompt</strong> se dodaje u grupu <strong>Then</strong> preko <strong>Add Card</strong>.</p></figcaption></figure>

---

## 📌 Version Information

**Trenutna verzija:** v3 (Najnovija i preporučena)
**Status:** ✅ Aktivna

**Istorija verzija:**
- v2 → Originalna DocOperator implementacija
- **v3 → TRENUTNA** (dodat parametar kontrole izvršavanja)
- v4 → Zastarela (funkcije vraćene unazad)

**Šta se promenilo:** v3 je dodala opcioni parametar „Execute the prompt" za veću kontrolu. v4 je pokušala da ovo vrati unazad ali je zastarela.

📖 [Istorija verzija i promene](../../../changelog/release.md#3-action_run_docoperator_script--) | [Kompletna baza podataka kartica](../../../../DocFlow/docs/card_version.md#action_run_docoperator_script)

---

## Svrha
Ova kartica pokreće automatizovanu akciju pretraživača ili skript koristeći DocOperator. Zamislite to kao robota koji može da interaguje sa veb-sajtovima ili sistemima tačno kao što bi to čovek radio — klikajući dugmad, popunjavajući formulare, izvlačeći podatke, itd.

**Primer iz stvarnog sveta:** Vaša kompanija koristi veb-bazirani sistem nabavke. Ova kartica može automatski da se prijavi, pretraži proizvod, proveri dostupnost i dobije trenutnu cenu — sve bez ikoga da to radi ručno.

---

## Kada koristiti ovu karticu

Koristite ovu karticu kada treba da:
- Automatizujete zadatke na veb-sajtovima koji nemaju API-je
- Izvučete podatke sa veb-stranica
- Automatski popunite formulare
- Prijavite se u sisteme i preuzmete informacije
- Automatizujete ponavljajuće ručne zadatke
- Interagujete sa nasleđenim sistemima koji nisu integrisani

**Uobičajeni scenariji:**
- Prijavljivanje na veb-sajtove dobavljača i dobijanje zaliha u realnom vremenu
- Automatsko popunjavanje formulara na eksternim sistemima
- Izvlačenje podataka sa veb-stranica koje ne nude API-je
- Provera statusa isporuke na veb-sajtovima kurira
- Dobijanje cena iz sistema bez API pristupa

---

## Kako funkcioniše

1. **Kartica okinuta**: Tok rada stiže do ove kartice i uslovi su ispunjeni
2. **Skript počinje**: DocOperator bot počinje da pokreće vaš automatizacioni skript
3. **Akcije bota**: Bot izvodi akcije kao što su klikanje, kucanje, skrolovanje, izvlačenje
4. **Izvlačenje podataka**: Bot prikuplja informacije sa veb-stranica
5. **Vraćanje podataka**: Podaci se vraćaju u DocFlow za upotrebu u sledećim karticama
6. **Rukovanje istekom vremena**: Ako skript predugo traje, zaustavlja se i vraća ono što ima

---

## Objašnjenje parametara

### DocOperator Prompt/Skript
Automatizacioni skript koji govori DocOperator-u tačno šta da radi

**Primer (Običan jezik):**
```
1. Go to https://supplier.com/login
2. Enter username: myuser
3. Enter password: mypass
4. Click Login button
5. Search for product "ABC123"
6. Extract the price
7. Return the price
```

### Promenljive
Podaci koje želite da prosledite U skript

**Primer:**
```
product_id: "ABC123"
supplier_code: "SUPP-001"
```

Ove promenljive mogu se koristiti u skriptu ovako:
```
Search for product "{product_id}"
Find supplier "{supplier_code}"
```

### Maksimalni broj koraka
Koliko akcija je botu dozvoljeno da izvede

**Tipične vrednosti:**
- Jednostavan zadatak (kao dobijanje jedne cene): 10-20 koraka
- Srednja složenost (popunjavanje formulara + izvlačenje): 20-50 koraka
- Složen tok rada (prijava + pretraga + validacija): 50-100 koraka

**Zašto je važno:** Sprečava beskonačne petlje i veoma dugotrajne skripte

### Maksimalni broj ponovnih pokušaja
Ako bot ne uspe akciju, koliko puta treba ponovo da pokuša?

**Primeri:**
- 1: Pokušaj jednom, ako ne uspe nastavi dalje
- 3: Pokušaj 3 puta pre odustajanja
- 5: Veoma uporno - pokušaj 5 puta

---

## Primer korak po korak

### Scenario: Dobijanje cene dobavljača sa veb-sajta

**Definicija skripta:**
```
Step 1: Open website https://prices.supplier-xyz.com
Step 2: Click on "Product Lookup"
Step 3: Enter product code: ABC-123
Step 4: Click "Search"
Step 5: Wait for results to load (3 seconds)
Step 6: Extract price from the page
Step 7: Extract available quantity
Step 8: Return both values
```

**Prosleđene promenljive:**
```
product_code = "ABC-123"
supplier_name = "Supplier XYZ"
```

**Skript koji koristi promenljive:**
```
Open website https://prices.{supplier_name}.com
Enter product code: {product_code}
Extract price and quantity
```

**Očekivani rezultat:**
```
price: 45.50
quantity_available: 500
```

---

## Tipovi akcija koje DocOperator može da izvede

### Navigacija
- Idi na URL
- Klikni na veze
- Pritisni dugmad
- Skroluj stranicu

### Popunjavanje formulara
- Kucaj tekst u polja
- Izaberi opcije padajućeg menija
- Označi/poništi polja za potvrdu
- Klikni dugmad

### Izvlačenje podataka
- Čitaj tekst sa stranice
- Izvuci brojeve
- Dobij podatke tabele
- Kopiraj informacije

### Čekanje
- Čekaj da se stranica učita
- Čekaj da se elementi pojave
- Čekaj dinamički sadržaj

### Uslovna logika
- Ako nešto postoji, uradi ovo
- Ako se tekst poklapa, onda...
- Prebroji rezultate i postupi u skladu sa tim

---

## Uobičajeni slučajevi upotrebe

### 1. Dobijanje cena u realnom vremenu
**Scenario:** Dobavljač nema API ali veb-sajt prikazuje cene

**Skript:**
```
1. Go to supplier website
2. Search for product
3. Extract price from results
4. Return price to DocFlow
5. Use price to validate invoice
```

### 2. Provera dostupnosti zaliha
**Scenario:** Treba da znate da li dobavljač ima zalihe

**Skript:**
```
1. Log into supplier portal
2. Search for product
3. Extract availability status
4. Extract delivery time
5. Return both to DocFlow
```

### 3. Automatsko slanje formulara
**Scenario:** Treba da popunite formular na eksternom sajtu

**Skript:**
```
1. Navigate to form page
2. Fill Company Name field
3. Fill Contact Email field
4. Select Country from dropdown
5. Upload file attachment
6. Click Submit button
7. Capture confirmation message
```

### 4. Verifikacija unosa podataka
**Scenario:** Verifikujte da se podaci poklapaju na dva različita sistema

**Skript:**
```
1. Go to System A
2. Search for Order #123
3. Extract order amount
4. Go to System B
5. Search for Order #123
6. Extract order amount
7. Compare amounts
8. Return true/false if they match
```

---

## Koraci konfiguracije

### Korak 1: Kreirajte skript
1. Definišite šta želite da postignete
2. Razbijte to na male korake
3. Jasno napišite svaki korak
4. Prvo testirajte ručno (otvorite veb-sajt, uradite to sami)
5. Dokumentujte tačno na šta kliknete, gde kucate, šta izvlačite

### Korak 2: Identifikujte promenljive
1. Koji podaci će se menjati između dokumenata?
2. Šta treba proslediti u skript?
3. Definišite nazive promenljivih
4. Navedite gde se promenljive koriste u skriptu

### Korak 3: Postavite parametre
- **Maksimalni broj koraka**: Na osnovu složenosti skripta
- **Maksimalni broj ponovnih pokušaja**: Koliko uporan bot treba da bude?
- **Isticanje vremena**: Koliko dugo treba da čeka stranice?

### Korak 4: Testirajte
1. Testirajte sa uzorcima podataka
2. Verifikujte da bot može da pristupi veb-sajtu
3. Verifikujte da je izvlačenje ispravno
4. Proverite da li promenljive ispravno funkcionišu

---

## Saveti za pisanje skripta

### Jasan jezik
✅ **Radite:**
```
1. Click the "Login" button
2. Type the username in the login field
3. Wait 2 seconds for form to process
```

❌ **Ne radite:**
```
1. Do the login thing
2. Enter stuff
3. Wait for it
```

### Specifični selektori
✅ **Radite:**
```
Click the button labeled "Submit Order"
Type in the field with placeholder "Enter Email"
```

❌ **Ne radite:**
```
Click somewhere
Type in a field
```

### Rukovanje greškama
✅ **Radite:**
```
1. Try to click "Next" button
2. If button not found, extract data from current page
3. Return what we have
```

❌ **Ne radite:**
```
Click "Next" (assumes it's always there)
```

---

## Rešavanje problema

### „Script Timed Out"
**Uzrok:** Skript je predugo trajao da se završi

**Rešenja:**
- [ ] Smanjite broj akcija
- [ ] Povećajte vrednost „Maximum Steps"
- [ ] Optimizujte skript za brže izvršavanje
- [ ] Pojednostavite ono što pokušavate da izvučete

### „Element Not Found"
**Uzrok:** DocOperator nije mogao da pronađe dugme/polje koje ste naveli

**Rešenja:**
- [ ] Verifikujte da je naziv dugmeta/polja tačno ispravan
- [ ] Proverite da li se promenio raspored veb-sajta
- [ ] Dodajte vreme čekanja pre klika
- [ ] Proverite da li se dugme pojavljuje samo pod određenim uslovima

### „Login Failed"
**Uzrok:** Autentifikacija nije uspela

**Rešenja:**
- [ ] Verifikujte da su korisničko ime/lozinka ispravni
- [ ] Proverite da li lozinka ima specijalne znakove
- [ ] Verifikujte da nalog nije zaključan
- [ ] Proverite da li se promenio proces prijave

### „Data Not Extracted Correctly"
**Uzrok:** Skript je radio ali je izvukao pogrešne informacije

**Rešenja:**
- [ ] Verifikujte da je izabrano ispravno polje
- [ ] Proverite da li su podaci na očekivanoj lokaciji
- [ ] Testirajte logiku izvlačenja ručno
- [ ] Dodajte korake za otklanjanje grešaka da verifikujete šta je na stranici

### „Script Runs Slowly"
**Uzrok:** Previše koraka ili spor veb-sajt

**Rešenja:**
- [ ] Uklonite nepotrebne korake
- [ ] Optimizujte vremena čekanja
- [ ] Proverite internet vezu
- [ ] Razmotrite da li postoji API alternativa

---

## Najbolje prakse

✅ **Radite:**
- Temeljno testirajte skripte pre postavljanja
- Održavajte skripte jednostavnim i fokusiranim
- Dodajte komentare koji objašnjavaju svaki korak
- Koristite smislene nazive promenljivih
- Pratite performanse skripta
- Imajte rezervu za slučaj kada skripte ne uspeju

❌ **Ne radite:**
- Ne kreirajte ekstremno duge skripte (>100 koraka)
- Ne stavljajte osetljive lozinke u zapise
- Ne oslanjajte se na tačne koordinate (veb-sajtovi se menjaju)
- Ne kreirajte petlje bez izlaznih uslova
- Ne ignorišite poruke o greškama

---

## Saveti za performanse

- **Uklonite nekorišćene korake** - Svaki korak oduzima vreme
- **Kombinujte slične akcije** - Grupišite povezane klikove
- **Optimizujte čekanja** - Koristite samo neophodna kašnjenja
- **Keširajte podatke** - Ne izvlačite iste podatke dvaput
- **Paralelna obrada** - Pokrenite više skripti ako je moguće

---

## Razmatranja bezbednosti

⚠️ **Važno:**
- Ne čuvajte lozinke u DocFlow-u
- Koristite bezbedne metode za prosleđivanje akreditiva
- Ne beležite osetljive podatke
- Pratite šta se izvlači
- Obezbedite da je aktivnost bota zabeležena i da se može revidirati

---

## Primer promenljivih

### Dostupne promenljive koje možete koristiti:
```
{invoice_number} - From document field
{supplier_code} - From document field
{product_id} - From document field
{quantity} - From document field
{currency} - From document field
```

### Skript koji koristi promenljive:
```
1. Go to https://supplier.com/api/lookup
2. Enter supplier code: {supplier_code}
3. Search for product: {product_id}
4. Enter quantity: {quantity}
5. Extract price in currency: {currency}
6. Return extracted price
```

---

## Poređenje: Kada koristiti DocOperator vs API

| Situacija | Koristi DocOperator | Koristi API |
|-----------|-----------------|---------|
| Veb-sajt ima API | ❌ Ne | ✅ Da |
| Veb-sajt je interaktivan | ✅ Da | ❌ Ne |
| Zahteva prijavu | ✅ Da | Zavisi |
| Potrebno veoma brzo | ❌ Ne | ✅ Da |
| Složen tok rada | ✅ Da | ❌ Možda ne |
| Podaci se menjaju dnevno | ✅ Da | ✅ Da |

---

## Povezane kartice

- **CALL_API** - Koristite kada je API dostupan umesto toga
- **ACTION_HTTPS_REQUEST** - Jednostavniji zahtevi
- **ACTION_SET_FIELD_TO_TEXT** - Koristite izvučene podatke
- **CONDITION_HTTPS_REQUEST_STATUS** - Proverite status zahteva
