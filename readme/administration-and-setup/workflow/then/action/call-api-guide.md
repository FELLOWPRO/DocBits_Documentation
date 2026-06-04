# Pozovi eksterni API

---

Dodajte ovu karticu u grupu **Then** u Workflow Builder-u — akcije koje se pokreću kada se When/And uslovi poklope:

<figure><img src="../../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow Builder platno sa grupama kartica When, And i Then"><figcaption><p>Kartica <strong>Call External API</strong> se dodaje u grupu <strong>Then</strong> preko <strong>Add Card</strong>.</p></figcaption></figure>

---

## 📌 Version Information

**Trenutna verzija:** v2 (Najnovija i preporučena)
**Status:** ✅ Aktivna

**Istorija verzija:**
- v1 → Osnovni API poziv (više se ne preporučuje)
- **v2 → TRENUTNA** (dodata podrška za više jezika)

**Šta se promenilo:** v2 je dodala podršku za internacionalizaciju (i18n) sa ključevima za prevod. Funkcionalnost ostaje identična.

📖 [Istorija verzija i promene](../../../changelog/release.md#1-call_api) | [Kompletna baza podataka kartica](../../../../DocFlow/docs/card_version.md#call_api)

---

## Svrha
Ova kartica vam omogućava da pošaljete podatke eksternom veb-sajtu ili servisu i primite informacije nazad. Zamislite to kao slanje pitanja eksternom servisu i dobijanje odgovora koji možete koristiti u svom toku rada.

**Primer iz stvarnog sveta:** Vaša kompanija koristi sistem za cene na drugom veb-sajtu. Ova kartica može automatski da pita taj sistem za cene za trenutnu cenu stavke i da tu cenu unese u vaš dokument.

---

## Kada koristiti ovu karticu

Koristite ovu karticu kada treba da:
- Dobijete informacije iz eksternog servisa (kao što su cene, validacija ili podaci pretrage)
- Pošaljete informacije dokumenta drugom sistemu na obradu
- Integrišete se sa servisima trećih strana
- Automatski preuzmete podatke bez ručnih pretraga
- Povežete više poslovnih sistema zajedno

**Uobičajeni scenariji:**
- Pretraga informacija o dobavljaču iz baze podataka
- Dobijanje cena u realnom vremenu iz servisa za cene
- Validacija podataka u odnosu na eksterni sistem
- Preuzimanje informacija o dostavi od logističkog pružaoca

---

## Kako funkcioniše

1. **Provera uslova**: Tok rada prvo proverava da li su uslovi u „Where" i „And" odeljcima ispunjeni
2. **Priprema podataka**: Kartica prikuplja parametre koje ste konfigurisali
3. **Slanje zahteva**: Šalje vaše podatke eksternom API-ju/servisu
4. **Prijem odgovora**: Eksterni servis odgovara podacima
5. **Nastavak**: Tok rada koristi ove podatke u narednim karticama

---

## Objašnjenje parametara

### API Endpoint URL
**Šta je to:** Adresa eksternog servisa sa kojim želite da komunicirate

**Primer:** `https://api.supplier-system.com/product/pricing`

**Kako da je pronađete:** Pitajte svoj IT tim ili pružaoca servisa za njihov API endpoint

---

### HTTP metoda
**Šta je to:** Tip zahteva koji se šalje

**Opcije:**
- **GET**: Zahteva informacije (kao postavljanje pitanja)
- **POST**: Šalje nove podatke
- **PUT**: Ažurira postojeće podatke
- **DELETE**: Uklanja podatke

**Najčešća:** GET (za preuzimanje informacija)

---

### Zaglavlja
**Šta je to:** Dodatna uputstva za servis koji pozivate

**Primer:**
```
Authorization: Bearer your-api-key
Content-Type: application/json
```

**Zašto je potrebno:** Servisi često zahtevaju autentifikaciju ili specifična uputstva o formatu

---

### Parametri (Parametri upita)
**Šta je to:** Dodatne informacije prosleđene u URL-u

**Primer:**
```
?supplier_id=12345&currency=USD
```

**Stvarni primer:** Ako tražite cene, parametri mogu uključivati ID dobavljača i valutu

---

### Podaci zahteva (Telo)
**Šta je to:** Informacije koje šaljete servisu

**Primer:**
```json
{
  "product_id": "ABC123",
  "quantity": 100,
  "currency": "EUR"
}
```

**Kada se koristi:** Kada koristite POST ili PUT metode

---

## Primer korak po korak

### Scenario: Dobijanje cena dobavljača u realnom vremenu

**Podešavanje:**
1. **Tip kartice:** Call API
2. **API Endpoint:** `https://api.suppliers.com/v1/prices`
3. **Metoda:** POST
4. **Zaglavlja:** `Authorization: Bearer YOUR-API-KEY`
5. **Podaci zahteva:**
   ```json
   {
     "product_id": "ABC123",
     "quantity": 100
   }
   ```

**Šta se dešava:**
1. Dokument stiže sa Product ID: ABC123, Quantity: 100
2. Kartica šalje zahtev API-ju dobavljača
3. API dobavljača odgovara sa: `{"unit_price": 25.50, "total_price": 2550}`
4. Tok rada se nastavlja sa ovim informacijama o ceni
5. Sledeća kartica može koristiti ove podatke za validaciju cene fakture

---

## Koraci konfiguracije

### 1. Dobijte informacije o API-ju
Kontaktirajte pružaoca eksternog servisa i zatražite:
- [ ] API endpoint URL
- [ ] Metodu autentifikacije (API ključ, korisničko ime/lozinka, OAuth)
- [ ] Potrebne parametre
- [ ] Očekivani format odgovora
- [ ] Ograničenja brzine ili kvote

### 2. Konfigurišite karticu
1. Unesite API endpoint URL
2. Izaberite HTTP metodu (obično GET ili POST)
3. Dodajte zaglavlja za autentifikaciju ako je potrebno
4. Dodajte sve potrebne parametre
5. Formatirajte podatke zahteva kao JSON ako je potrebno

### 3. Testirajte karticu
1. Koristite test dokument
2. Pokrenite tok rada
3. Proverite da li je odgovor ispravno primljen
4. Verifikujte da format podataka odgovara očekivanjima

---

## Uobičajeni scenariji odgovora

### Uspešan odgovor (Statusni kod 200)
```json
{
  "success": true,
  "data": {
    "price": 150,
    "currency": "EUR",
    "delivery_days": 5
  }
}
```
✅ Podaci su dostupni za korišćenje u sledećim karticama

### Odgovor sa greškom (Statusni kod 404)
```json
{
  "error": "Product not found"
}
```
⚠️ API nije mogao da pronađe ono što tražite

### Isticanje vremena
Eksterni servis nije odgovorio u okviru vremenskog ograničenja
⚠️ Proverite da li je servis dostupan ili da li je endpoint URL ispravan

---

## Primeri tokova rada

### Primer 1: Automatska validacija cena
**Scenario:** Validirajte cene fakture u odnosu na trenutne cene dobavljača

**Tok:**
1. Dokument stiže sa stavkom fakture (Product: A123, Price: €50)
2. **Call API kartica** → Pita API dobavljača: „What's the current price for A123?"
3. Dobavljač odgovara: „€48"
4. **Uslovna kartica** → Proverava da li je cena fakture (€50) unutar 5% trenutne cene (€48)
5. **Kartica odobravanja** → Odobrava ako je unutar tolerancije

### Primer 2: Automatska pretraga dobavljača
**Scenario:** Dobijte glavne podatke o dobavljaču iz centralne baze podataka

**Tok:**
1. Faktura stiže sa Supplier Code: SUPP-789
2. **Call API kartica** → Pita sistem: „Give me details for supplier SUPP-789"
3. Sistem odgovara sa: Naziv, kontakt, uslovi, itd.
4. **Set Field kartice** → Popunjavaju polja dokumenta ovim podacima
5. **Export kartica** → Izvoz sa kompletnim informacijama

### Primer 3: Troškovi dostave u realnom vremenu
**Scenario:** Dobijte automatski trošak dostave na osnovu odredišta

**Tok:**
1. Dokument ima adresu isporuke
2. **Call API kartica** → Pita pružaoca dostave: „What's the cost to [address]?"
3. Pružalac odgovara troškom dostave
4. **Calculate kartica** → Dodaje dostavu ukupnom iznosu fakture
5. **Export kartica** → Slanje sa ažuriranim ukupnim iznosom

---

## Rešavanje problema

### Greška „Connection Timeout"
**Uzrok:** API servis ne odgovara

**Rešenja:**
- [ ] Proverite da li je servis dostupan (posetite veb-sajt)
- [ ] Verifikujte da je endpoint URL ispravan (bez grešaka u kucanju)
- [ ] Proverite internet vezu
- [ ] Kontaktirajte pružaoca servisa
- [ ] Proverite da li servis ima ograničenja brzine (šaljete previše zahteva)

### Greška „Unauthorized" ili „403 Forbidden"
**Uzrok:** Autentifikacija nije uspela

**Rešenja:**
- [ ] Verifikujte da je vaš API ključ ispravan
- [ ] Proverite da li je vaš API ključ istekao
- [ ] Obezbedite da je zaglavlje autentifikacije ispravno formatirano
- [ ] Verifikujte da imate dozvole za ovaj endpoint

### Greška „Bad Request" ili „400 Error"
**Uzrok:** Format podataka zahteva nije ispravan

**Rešenja:**
- [ ] Proverite JSON sintaksu (nedostajući zarezi, navodnici, itd.)
- [ ] Verifikujte da su sva potrebna polja uključena
- [ ] Proverite da se nazivi parametara poklapaju sa onim što servis očekuje
- [ ] Konsultujte API dokumentaciju

### „Response not working as expected"
**Rešenja:**
- [ ] Testirajte API koristeći alat kao što je Postman
- [ ] Uporedite stvarni format odgovora sa očekivanim formatom
- [ ] Proverite da li se promenila dokumentacija API-ja
- [ ] Verifikujte da su podaci koje šaljete ispravni

---

## Upotreba podataka odgovora

Kada dobijete podatke nazad od API-ja, sledeće kartice mogu da ih koriste:

```
API Response:
{
  "unit_price": 45.00,
  "currency": "USD",
  "available": true
}

Next Card (Set Field):
- Set "Unit_Price" field to 45.00
- Set "Currency" field to USD
- Set "In_Stock" checkbox to true
```

---

## Bezbednosne napomene

⚠️ **Važno:** Nikada ne stavljajte osetljive informacije u konfiguraciju kartice koje bi mogle biti vidljive drugim korisnicima

- Ne kodirajte čvrsto lozinke
- Koristite API ključeve bezbedno
- Ne uključujte lične podatke u zapise
- Koristite HTTPS endpoint-ove (ne HTTP)

---

## Saveti i najbolje prakse

✅ **Radite:**
- Prvo testirajte sa malim uzorkom dokumenata
- Održavajte API pozive jednostavnim i fokusiranim
- Dodajte rukovanje greškama sa uslovnim karticama
- Pratite upotrebu/troškove API-ja
- Dokumentujte zahteve API-ja za svoj tim

❌ **Ne radite:**
- Ne pozivajte API-je za svaki zahtev ako možete keširati podatke
- Ne ignorišite kodove grešaka u odgovoru
- Ne koristite test API-je u produkciji
- Ne zaboravljajte da dodate zaglavlja za autentifikaciju
- Ne pretpostavljajte da će API uvek biti dostupan

---

## Povezane kartice

- **ACTION_HTTPS_REQUEST** - Slični ali jednostavniji HTTPS zahtevi
- **CONDITION_HTTPS_REQUEST_STATUS** - Proverite da li je API poziv uspeo
- **ACTION_SEND_EMAIL** - Pošaljite podatke putem e-pošte umesto API-ja
- **CALL_API** (druga verzija) - Alternativna metoda API poziva

---

## Treba vam pomoć?

- Pitajte svoj IT/Integracioni tim za API dokumentaciju
- Koristite Postman alat da prvo testirate API endpoint-ove
- Proverite portal za podršku pružaoca servisa
- Pregledajte API dokumentaciju za potrebne formate
