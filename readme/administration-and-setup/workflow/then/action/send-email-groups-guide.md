# Pošalji e-poštu grupama

---

Dodajte ovu karticu u grupu **Then** u Workflow Builder-u — akcije koje se pokreću kada se When/And uslovi poklope:

<figure><img src="../../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow Builder platno sa grupama kartica When, And i Then"><figcaption><p>Kartica <strong>Send Email to Groups</strong> se dodaje u grupu <strong>Then</strong> preko <strong>Add Card</strong>.</p></figcaption></figure>

---

## 📌 Version Information

**Status:** ✅ Jedna verzija (Bez prekidajućih promena)
**Najnovija verzija:** v1 (Aktivna)
**Napomena:** Ova kartica koristi model sa jednom verzijom sa podrškom za više jezika preko ključeva za prevod.

📖 [Kompletna baza podataka kartica](../../../../DocFlow/docs/card_version.md)

---

## Svrha
Ova kartica automatski šalje obaveštenja e-poštom grupama korisnika. Umesto dodeljivanja posla pojedinačnim osobama, šaljete poruku grupi, i svi članovi te grupe je primaju.

**Primer iz stvarnog sveta:** Kada stigne faktura velike vrednosti, automatski pošaljite obaveštenje e-poštom svima u grupi „Finance Team" tako da znaju da zahteva pregled.

---

## Kada koristiti ovu karticu

Koristite ovu karticu kada treba da:
- Obavestite više ljudi odjednom
- Pošaljete upozorenja timskim grupama
- Emitujete ažuriranja odeljenjima
- Obavestite grupe o promenama statusa dokumenta
- Pošaljete podsetnike članovima grupe

**Uobičajeni scenariji:**
- Obaveštavanje tima za nabavku o novim dobavljačima
- Upozoravanje finansijskog tima o fakturama velike vrednosti
- Obaveštavanje tima skladišta o pošiljkama
- Emitovanje promena statusa dokumenta

---

## Kako funkcioniše

1. **Provera uslova**: Tok rada proverava „Where" i „And" uslove
2. **Priprema e-pošte**: Sistem priprema e-poštu koristeći šablon
3. **Dobijanje članova grupe**: Sistem pronalazi sve članove navedene grupe
4. **Slanje**: E-pošta se šalje svakom članu grupe
5. **Zapisivanje**: Slanje e-pošte se beleži

---

## Objašnjenje parametara

### Šablon e-pošte
Poruka e-pošte koja se šalje

**Opcije:**
- Izaberite iz postojećih šablona
- Svaki šablon ima unapred definisan predmet, telo i formatiranje
- Šabloni mogu uključivati čuvare mesta kao što su {document_number}, {supplier_name}

**Primer šablona:**
```
Subject: Document {document_number} requires review

Body:
Dear Team,

A new invoice has arrived and requires review:
- Document: {document_number}
- Supplier: {supplier_name}
- Amount: {amount} {currency}
- Date: {date}

Please login to DocBits to review.

Best regards,
DocBits Automation
```

### Grupa
Grupa korisnika kojoj se šalje e-pošta

**Primeri grupa:**
- Finance Team
- Procurement Team
- Warehouse Team
- Approval Committee
- Management Group

---

## Koraci konfiguracije

### Korak 1: Izaberite šablon e-pošte
1. Kliknite na „Select Email Template"
2. Izaberite šablon sa liste
3. Verifikujte predmet i sadržaj

### Korak 2: Izaberite grupu
1. Kliknite na „Select Group"
2. Izaberite grupu koju želite da obavestite
3. Verifikujte članove grupe (obično prikazuje broj)

### Korak 3: Postavite uslove
1. Dodajte uslov: „When [condition] is true"
2. Primer: „When invoice amount is greater than €5000"

### Korak 4: Testirajte
1. Testirajte sa uzorkom dokumenta
2. Verifikujte da se e-pošta šalje grupi
3. Proverite renderovanje šablona

---

## Primeri šablona e-pošte

### Šablon 1: Upozorenje o fakturi velike vrednosti
```
Subject: High-Value Invoice Alert - {document_number}

Body:
Team,

An invoice exceeding €10,000 has been received:

Document Number: {document_number}
Supplier: {supplier_name}
Amount: {amount} EUR
Received Date: {date}
Status: {status}

This requires immediate review and approval.

---
Sent automatically by DocBits
```

### Šablon 2: Promena statusa dobavljača
```
Subject: Supplier Status Update - {supplier_name}

Body:
Procurement Team,

The following supplier's status has been updated:

Supplier: {supplier_name}
Supplier Code: {supplier_code}
New Status: {status}
Effective Date: {date}

Please update your systems accordingly.

---
Sent automatically by DocBits
```

### Šablon 3: Dokument spreman za izvoz
```
Subject: Document Approved for Export - {document_number}

Body:
Export Team,

The following document has been approved and is ready for export:

Document Number: {document_number}
Invoice Number: {invoice_number}
Supplier: {supplier_name}

Please proceed with export to {destination_system}.

---
Sent automatically by DocBits
```

---

## Uobičajeni slučajevi upotrebe

### Slučaj upotrebe 1: Upozorenja kontrole kvaliteta
**Okidač:** Kada se pronađe neslaganje između fakture i PO

**Grupa e-pošte:** Quality Team

**Sadržaj:**
```
Invoice {number} has quality issues:
- Unit Price variance: 12% (exceeds 5% tolerance)
- Please review and take action
```

### Slučaj upotrebe 2: Obaveštenja o odobravanju
**Okidač:** Kada dokument dostigne određeni status

**Grupa e-pošte:** Approval Committee

**Sadržaj:**
```
Document {number} is awaiting approval:
- Amount: {amount}
- Supplier: {supplier_name}
- Please login to approve/reject
```

### Slučaj upotrebe 3: Obaveštenja o izuzecima
**Okidač:** Kada uslovi nisu ispunjeni

**Grupa e-pošte:** Managers

**Sadržaj:**
```
Exception alert for document {number}:
- Supplier code missing
- Delivery date invalid
- Manual review required
```

### Slučaj upotrebe 4: Ažuriranja statusa
**Okidač:** Kada se status dokumenta promeni

**Grupa e-pošte:** Tim odgovoran za sledeći korak

**Sadržaj:**
```
Document {number} status changed to: {status}
Assigned to: {assigned_user}
Next steps: {next_steps}
```

---

## Rešavanje problema

### „Email not received"

**Mogući uzroci:**
- [ ] Korisnici u grupi nemaju adrese e-pošte
- [ ] E-pošta blokirana filterom za neželjenu poštu
- [ ] Adresa e-pošte je netačna u grupi
- [ ] Grupa nema članove

**Rešenja:**
1. Verifikujte da svi članovi grupe imaju adrese e-pošte
2. Proverite folder neželjene/đubrišne pošte
3. Verifikujte da je članstvo u grupi ispravno
4. Dodajte korisnike u grupu ako nedostaju
5. Proverite sa IT-jem da li servis e-pošte radi

### „Template not rendering correctly"

**Uzrok:** Promenljive čuvara mesta nisu pronađene

**Rešenje:**
- [ ] Verifikujte da se nazivi polja tačno poklapaju
- [ ] Proverite da li polje ima vrednost u dokumentu
- [ ] Koristite ispravan format čuvara mesta: {field_name}
- [ ] Testirajte sa uzorkom dokumenta koji ima sva polja

### „Some people getting email, others not"

**Uzrok:** Nepotpuno članstvo u grupi ili nevažeće e-pošte

**Rešenja:**
- [ ] Verifikujte da svi članovi imaju važeću e-poštu
- [ ] Proverite da li su se neki korisnici isključili
- [ ] Verifikujte da je članstvo u grupi ažurno
- [ ] Kontaktirajte IT da validira adrese e-pošte

### „Want to add/remove people from group"

**Rešenje:**
- Kontaktirajte svog administratora
- Grupe se upravljaju u podešavanjima sistema
- Ne mogu se menjati sa ove kartice
- Zatražite promene članstva u grupi u IT-ju

---

## Prilagođavanje šablona e-pošte

### Dostupni čuvari mesta
```
{document_number} - Document ID
{invoice_number} - Invoice ID
{supplier_name} - Supplier name
{supplier_code} - Supplier code
{amount} - Invoice amount
{currency} - Currency (EUR, USD, etc.)
{date} - Document date
{status} - Current status
{assigned_user} - Assigned person
{assigned_group} - Assigned group
{next_steps} - What needs to happen next
{reason} - Reason for exception/alert
{comment} - Comments or notes
```

### Kreiranje prilagođenih čuvara mesta
Ako vam je potrebno više podataka u e-pošti:
1. Kontaktirajte svog administratora
2. Zatražite novi čuvar mesta
3. Dodajte potrebno polje u dokument
4. Ažurirajte šablon e-pošte

---

## Najbolje prakse

✅ **Radite:**
- Održavajte sadržaj e-pošte kratkim i jasnim
- Uključite stavke akcije (šta primaoci treba da urade?)
- Uključite vezu ili uputstva za pristup dokumentu
- Testirajte šablon sa uzorcima podataka
- Šaljite pravoj grupi (ne prekomerno obaveštavajte)
- Koristite šablone radi doslednosti

❌ **Ne radite:**
- Ne šaljite previše e-poruka (umor od obaveštenja)
- Ne uključujte osetljive podatke u e-poštu
- Ne šaljite grupama kojima informacija nije potrebna
- Ne koristite nejasne predmete
- Ne zaboravljajte da uključite kako preduzeti akciju
- Ne šaljite e-poštu pojedincima (umesto toga koristite grupu)

---

## Napomene o performansama

- Svaka e-pošta zahteva ~1 sekundu za slanje
- Velike grupe mogu da potraju (100 ljudi = ~100 sekundi)
- Ne kreirajte petlje koje šalju hiljade e-poruka
- Pratite kapacitet servisa e-pošte
- Razmotrite paketnu obradu ako ima mnogo dokumenata

---

## Povezane kartice

- **ACTION_SEND_EMAIL** - Slanje pojedinačnoj osobi
- **ACTION_ASSIGN_TASK_TO_PROCUREMENT_GROUP** - Dodelite zadatak umesto samo obaveštavanja
- **ACTION_CREATE_TASK_FOR_GROUP_SEQUENTIAL** - Kreirajte zadatak i obavestite
- **STAUS_CHANGE** - Promenite status i obavestite

---

## Tipičan primer toka rada

```
Document Arrives
    ↓
Check Condition: "Is amount > €10,000?"
    ↓
YES: Send Email to Finance Team
     "High value invoice alert"
    ↓
Send Email to Procurement Team
     "New invoice from supplier"
    ↓
Workflow Continues
```

---

## Često postavljana pitanja

**P: Mogu li da pošaljem na više grupa?**
O: Kreirajte odvojene kartice za svaku grupu

**P: Šta ako se nečija e-pošta odbije?**
O: E-pošta se beleži kao neuspela, IT može da rešava problem

**P: Mogu li da promenim šablon e-pošte?**
O: Kontaktirajte svog administratora da izmeni šablone

**P: Mogu li da šaljem na osnovu uslova?**
O: Da! Koristite „Where" i „And" uslove da kontrolišete kada se e-pošte šalju

**P: Kako da znam da li je e-pošta primljena?**
O: Proverite zapise e-pošte u DocBits-u za status slanja
