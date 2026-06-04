# Pošalji HTTPS zahtev

---

Dodajte ovu karticu u grupu **Then** u Workflow Builder-u — akcije koje se pokreću kada se When/And uslovi poklope:

<figure><img src="../../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow Builder platno sa grupama kartica When, And i Then"><figcaption><p>Kartica <strong>Send HTTPS Request</strong> se dodaje u grupu <strong>Then</strong> preko <strong>Add Card</strong>.</p></figcaption></figure>

---

## 📌 Version Information

**Trenutna verzija:** v2 (Najnovija i preporučena)
**Status:** ✅ Aktivna

**Istorija verzija:**
- v1 → Jednostavan HTTP zahtev (više se ne preporučuje)
- **v2 → TRENUTNA** (dodata podrška za više jezika)

**Šta se promenilo:** v2 je dodala podršku za internacionalizaciju (i18n). Osnovna funkcionalnost webhook-a/zahteva ostaje nepromenjena.

📖 [Istorija verzija i promene](../../../changelog/release.md#2-https-request-https_request) | [Kompletna baza podataka kartica](../../../../DocFlow/docs/card_version.md)

---

## Svrha
Ova kartica šalje bezbednu poruku veb-sajtu ili servisu i može da primi odgovor nazad. Jednostavnija je od kartice „Call API" i korisna je za brze integracije.

**Primer iz stvarnog sveta:** Pošaljite podatke fakture svom računovodstvenom sistemu, ili pitajte eksterni sistem da li je zaposleni odobren da obradi ovu kupovinu.

---

## Kada koristiti ovu karticu

Koristite ovu karticu kada treba da:
- Pošaljete webhook obaveštenja eksternim servisima
- Pokrenete akcije u drugim sistemima
- Upitate jednostavan veb-servis
- Pošaljete ažuriranja statusa drugim aplikacijama
- Izvedete jednostavne integracije bez složenih API zahteva

---

## Kako funkcioniše

1. **Provera okidača**: Sistem proverava da li su „Where" i „And" uslovi ispunjeni
2. **Izgradnja zahteva**: Sistem priprema HTTPS zahtev sa vašim parametrima
3. **Bezbedno slanje**: Podaci se šalju koristeći bezbednu HTTPS vezu
4. **Prijem odgovora**: Eksterni servis odgovara
5. **Nastavak**: Tok rada se nastavlja sa podacima odgovora

---

## Parametri

### URL
Adresa veb-sajta na koju se šalje zahtev

**Primer:** `https://webhook.company.com/process`

### Zaglavlja
Posebna uputstva za primaoca

**Primer:**
```
Content-Type: application/json
Authorization: Bearer token123
```

### Metoda
- **GET**: Zahteva informacije
- **POST**: Šalje podatke
- **PUT**: Ažurira podatke

### Parametri (Niska upita)
Podaci dodati u URL

**Primer:** `?action=approve&user_id=123`

### Podaci zahteva
Stvarne informacije koje se šalju (u JSON formatu)

**Primer:**
```json
{
  "invoice_number": "INV-2025-001",
  "amount": 5000,
  "currency": "EUR"
}
```

---

## Primer korak po korak

### Scenario: Slanje fakture računovodstvenom sistemu

**Konfiguracija kartice:**
- **URL:** `https://accounting.company.com/invoices/create`
- **Metoda:** POST
- **Zaglavlja:** `Authorization: Bearer YOUR-TOKEN`
- **Podaci zahteva:**
```json
{
  "supplier_id": "SUPP001",
  "invoice_number": "12345",
  "amount": 1500.00,
  "currency": "EUR",
  "date": "2025-10-23"
}
```

**Očekivani odgovor:**
```json
{
  "status": "success",
  "accounting_id": "ACC-98765",
  "message": "Invoice recorded in accounting system"
}
```

---

## Uobičajeni slučajevi upotrebe

### 1. Webhook obaveštenja
Šaljite obaveštenja u realnom vremenu drugim sistemima kad god se nešto dogodi u DocFlow-u

**Primer:**
- Dokument odobren → Pošalji obaveštenje sistemu za realizaciju
- Dobavljač promenjen → Obavesti tim za kupovinu preko Slack/Teams webhook-a

### 2. Integracija eksternih sistema
Povežite DocFlow sa drugim poslovnim sistemima za automatsku razmenu podataka

**Primer:**
- Nakon obrade dokumenta → Sinhronizuj sa ERP sistemom
- Dodat novi dobavljač → Kreiraj zapis dobavljača u sistemu glavnih podataka

### 3. Tokovi rada za odobravanje
Pošaljite dokument eksternom sistemu za odobravanje i primite odluku

**Primer:**
- Faktura velike vrednosti → Pošalji finansijama na odobravanje
- Vrati dokument eksternom sistemu sa odlukom

---

## Vodič za konfiguraciju

### Korak 1: Dobijte informacije o endpoint-u
Pitajte sistem primalac za:
- [ ] HTTPS URL
- [ ] Potrebna zaglavlja
- [ ] Metodu autentifikacije
- [ ] Očekivani format zahteva
- [ ] Očekivani format odgovora

### Korak 2: Konfigurišite karticu
1. Unesite HTTPS URL
2. Postavite HTTP metodu (obično POST)
3. Dodajte autentifikaciju ako je potrebno
4. Formatirajte podatke zahteva kao JSON
5. Dodajte sva prilagođena zaglavlja

### Korak 3: Testirajte
Pošaljite test zahtev i verifikujte odgovor

---

## Rukovanje odgovorom

Vaš HTTPS zahtev će dobiti odgovor. Uobičajeni odgovori:

### Uspeh (200, 201)
```json
{
  "success": true,
  "id": "REC-12345",
  "status": "processed"
}
```

### Bad Request (400)
```json
{
  "error": "Missing required field: invoice_number"
}
```

### Unauthorized (401)
```json
{
  "error": "Invalid authentication token"
}
```

### Server Error (500)
Sistem primalac ima interni problem

---

## Rešavanje problema

### „Certificate Error"
**Uzrok:** Problem sa HTTPS bezbednosnim sertifikatom

**Rešenje:**
- Verifikujte da je URL ispravan
- Proverite da li je sertifikat veb-sajta važeći
- Obezbedite da koristite HTTPS (ne HTTP)

### „Connection Refused"
**Uzrok:** Nije moguće povezati se sa serverom

**Rešenje:**
- Verifikujte da je URL/IP adresa ispravna
- Proverite da li servis radi
- Proverite pravila zaštitnog zida
- Verifikujte internet povezanost

### „No Response / Timeout"
**Uzrok:** Server ne odgovara u okviru vremenskog ograničenja

**Rešenje:**
- Proverite da li je servis dostupan
- Verifikujte endpoint URL
- Proverite da li postoje ograničenja brzine
- Kontaktirajte administratora sistema

### „Invalid JSON"
**Uzrok:** Podaci zahteva su nepravilno formirani

**Rešenje:**
- Proverite nedostajuće zareze u JSON-u
- Verifikujte da su svi navodnici ispravni
- Validirajte JSON format (koristite onlajn JSON validator)
- Proverite specijalne znakove

---

## Primeri

### Primer 1: Slanje webhook servisu
```
URL: https://webhook.site/your-unique-id
Method: POST
Data:
{
  "document_id": "DOC-123",
  "status": "approved",
  "amount": 5000
}
```

### Primer 2: Ažuriranje eksternog sistema
```
URL: https://api.company.com/update
Method: PUT
Data:
{
  "record_id": "REC-456",
  "status": "completed",
  "timestamp": "2025-10-23T10:30:00"
}
```

### Primer 3: Upit eksternog servisa
```
URL: https://lookup.company.com/validate?id=SUP-789
Method: GET
Headers: Authorization: Bearer token
```

---

## Razlika u odnosu na karticu „Call API"

| Karakteristika | HTTPS Request | Call API |
|---------|---------------|----------|
| Jednostavnost | Jednostavna | Složenija |
| Parametri | Osnovni | Napredni |
| Rukovanje greškama | Osnovno | Detaljno |
| Koristi za | Brze integracije | Složene API-je |
| Najbolje za | Webhook-ove | Profesionalne API-je |

---

## Razmatranja bezbednosti

✅ **Uvek koristite HTTPS** (bezbedna veza)

⚠️ **Nikada:**
- Ne stavljajte lozinke u URL
- Ne izlažite API ključeve u zapisima
- Ne uključujte lične podatke u parametre
- Ne koristite HTTP za osetljive podatke

---

## Najbolje prakse

✅ **Radite:**
- Prvo testirajte sa malim količinama podataka
- Uključite rukovanje greškama
- Beležite važne zahteve
- Dokumentujte integraciju
- Pratite neuspehe

❌ **Ne radite:**
- Ne pozivajte isti endpoint više puta ako nije potrebno
- Ne ignorišite greške u odgovoru
- Ne uključujte osetljive podatke u običnom tekstu
- Ne prekoračujte ograničenja brzine servisa

---

## Povezane kartice

- **CALL_API** - Naprednija API integracija
- **CONDITION_HTTPS_REQUEST_STATUS** - Proverite da li je zahtev uspeo
- **ACTION_SEND_EMAIL** - Slanje putem e-pošte umesto toga
- **ACTION_RUN_DOCOPERATOR_SCRIPT** - Automatizovani skripti
