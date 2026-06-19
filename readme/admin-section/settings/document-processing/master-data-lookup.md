# Pretraga matičnih podataka

{% embed url="https://youtu.be/hn_bkeUMxJg" %}
{% endembed %}

**Pretraga matičnih podataka** (bočna traka: **Lookup Master Data**) omogućava vam da pregledate matične podatke koje DocBits koristi za validaciju podataka izdvojenih iz dokumenata u odnosu na vaš ERP sistem i da njima upravljate. Ovo je ključno za precizan PO matching, validaciju dobavljača i automatsko popunjavanje polja. Otvorite je preko **Podešavanja → Obrada dokumenata → Lookup Master Data**.

<figure><img src="../../../.gitbook/assets/master_data_lookup_overview.png" alt="Pretraga matičnih podataka"><figcaption><p>Stranica Pretraga matičnih podataka – izvori podataka i tabela podataka</p></figcaption></figure>

## Izvori podataka

Levi panel prikazuje četiri kategorije izvora podataka:

| Izvor | Opis |
|-------|------|
| **BOD Input Data** | Podaci primljeni putem Infor BOD (Business Object Document) poruka. |
| **ERP API Data** | Podaci preuzeti direktno iz vašeg ERP sistema putem API-ja. Kliknite na ikonu zupčanika da biste konfigurisali API vezu. |
| **Imported** | Ručno uvezeni podaci (na primer putem otpremanja CSV-a). Kliknite na ikonu **+** da biste dodali nove podatke. |
| **DocBits Master Data** | Interni matični podaci kojima se upravlja unutar DocBits-a. |

## Tabela podataka

Kada izaberete izvor podataka, njegovi podaci se otvaraju desno u pretraživoj tabeli koja se može sortirati:

* **Kartice** – svaka kartica je tip matičnih podataka (na primer Dobavljač, Nalog za nabavku, Stavka).
* **Pretraga** – filtrirajte po koloni (**Search by column**) ili pretražujte po tekstu (**Search String**).
* **Radnje** – ažurirajte oznake kolona, sakrijte prazne kolone, ažurirajte aliase ili preuzmite podatke kao CSV.
* **Paginacija** – krećite se kroz velike skupove podataka pomoću kontrola stranice.

Tabele Dobavljač i Nalog za nabavku sadrže kolone kao što su ID dobavljača, Naziv dobavljača, Adresa, Bank Id, PO broj, ID stavke, Opis, Količina, Jedinična cena, Ukupan iznos, Valuta i Status, kao i sva prilagođena polja.

## Podešavanja

Kliknite na **Settings** (ikona zupčanika) u donjem levom uglu panela izvora podataka da biste otvorili podešavanja matičnih podataka.

<figure><img src="../../../.gitbook/assets/master_data_lookup_settings.png" alt="Podešavanja Pretrage matičnih podataka"><figcaption><p>Podešavanja Supplier BOD i brisanja naloga za nabavku</p></figcaption></figure>

### Supplier BOD

**Allow Multiple Supplier Accounts Sync**

* **Omogućeno**: jedan dobavljač može imati više `<FinancialParty>` elemenata u BOD-u (često zbog više IBAN-ova ili finansijskih računa). Svi `<FinancialParty>` unosi se izdvajaju i čuvaju u tabeli dobavljača, tako da se može sačuvati više finansijskih atributa.
* **Onemogućeno**: izdvaja se samo poslednji pronađeni `<FinancialParty>` element za dobavljača. Prethodni finansijski atributi (na primer dodatni IBAN-ovi) se zanemaruju i čuvaju se samo podaci poslednjeg pojavljivanja.

### Purchase Order Deletion Assistant

**Delete Purchase Order After** – izaberite kada zatvoreni nalozi za nabavku treba da budu uklonjeni. Nakon izabranog perioda, zapisi se automatski brišu.

{% hint style="info" %}
Da biste saznali kako da učitate matične podatke u DocBits, pogledajte [Uvoz matičnih podataka](../../../infor-integration-and-configuration/importing-customer-master-data/).
{% endhint %}
