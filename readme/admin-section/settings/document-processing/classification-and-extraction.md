# Klasifikacija i Ekstrakcija

<figure><img src="../../../.gitbook/assets/Bildschirmfoto 2024-05-08 um 11.10.49.png" alt=""><figcaption></figcaption></figure>

"Postavke Klasifikacije i Ekstrakcije" u vašem sistemu obrade dokumenata pružaju opcije za konfigurisanje načina automatske obrade dokumenata pri unosu:

1. **Deljenje Dokumenata**: Ova postavka vam omogućava da odaberete da li da delite dokumenta na osnovu određenih kriterijuma ili da ih zadržite kao jedan dokument. Ovo može biti korisno prilikom obrade dokumenata koji imaju više različitih sekcija, ali su otpremljeni kao jedan fajl.
2. **Formatiranje Iznosa**: Ovde možete omogućiti opcije poput zaokruživanja ukupnih iznosa u narudžbinama. Ovo osigurava da ekstrahovani podaci odgovaraju očekivanim finansijskim formatima i pravilima, smanjujući greške u finansijskoj obradi.
3. **Ekstrakcija Tabela**: Ovde uključujete ekstrakciju tabela zasnovanu na pravilima ili AI ekstrakciju tabela i birate AI model. Sva podešavanja, preduslovi i ključevi preferenci opisani su u odeljku [Ekstrakcija tabela](#ekstrakcija-tabela) ispod.
4. **Konfigurisanje Pravila Klasifikacije**: Ova opcija vam omogućava da definišete specifične obrasce i kriterijume koji pomažu sistemu da automatski klasifikuje i kategorizuje dokumenta dok se obrađuju. Ovo može biti zasnovano na tekstualnim obrascima, tipovima dokumenata ili drugim metapodacima povezanim sa dokumentima.

<figure><img src="../../../.gitbook/assets/Bildschirmfoto 2024-05-08 um 11.11.10.png" alt=""><figcaption></figcaption></figure>

## Ekstrakcija tabela

{% hint style="info" %}
**Preduslovi za ispravnu ekstrakciju tabela**

* Tip dokumenta ima **kolone tabele** (Podešavanja → Globalna podešavanja → Tipovi dokumenata → [Kolone tabele](../global-settings/document-types/table-columns.md)). Bez kolona nema u šta da se ekstrahuje.
* **Ekstrakcija tabela** ili **AI ekstrakcija tabela** je uključena ispod, za celu organizaciju.
* Dokument ima čitljiv tekst: OCR je izvršen, ili se za digitalno kreirane PDF-ove koristi E-Text ([OCR podešavanja](ocr-settings.md)).
* Obuka i AI modeli važe **po dobavljaču**. Obučena tabela se primenjuje samo na dokumente dobavljača na kojem je obučena.
{% endhint %}

Tabele iz dokumenata možete ekstrahovati tako što uključite **Ekstrakciju tabela** ili **AI ekstrakciju tabela**. Obučena tabela (bilo AI ili ručna) uvek je vezana za određenog dobavljača.

**Ekstrakcija tabela:** Aktivira ekstrakciju tabela zasnovanu na pravilima. Tabele se obučavaju po dobavljaču na ekranu za validaciju (*Idi na prikaz ekstrakcije tabele*).\
Više o obuci saznajte [ovde](../../../setup/document-training/training-line-fields-table-training/defining-tables-and-columns.md).

**AI ekstrakcija tabela:** Koristi AI za ekstrakciju tabele bilo kog dobavljača bez obuke. Ako rezultati za jednog dobavljača nisu dovoljno tačni, obučite tabelu tog dobavljača; sačuvana pravila tada imaju prednost nad AI-jem za tog dobavljača.

**Koristi Vision ekstrakciju tabela (AI):** AI čita sliku stranice umesto tekstualnog sloja. Pomaže kod skeniranih dokumenata i tabela bez jasne tekstualne strukture; sporije je.

**Koristi strukturiranu ekstrakciju (AI):** AI vraća tabelu u fiksnoj strukturi koja se direktno mapira na konfigurisane kolone tabele. Preporučuje se kada zaglavlja kolona na dokumentima znatno variraju.

**Ekstrakcija tabela za elemente troškova:** Kada je uključeno, DocBits može da ekstrahuje elemente troškova iz tabela na nivou stavke i da ih odgovarajuće klasifikuje.

**Automatski ekstrahuj poreski kod:** Kada je uključeno, sistem automatski popunjava polje **Poreski kod** na ekranu za validaciju, pod uslovom da je polje za poreski kod konfigurisano.

**Čuvanje pravila ekstrakcije (samo administratori):** Samo administratori mogu da kliknu na *Save Rules* u obuci tabele. Uključite ga kada korisnici stalno čuvaju pravila koja kvare ekstrakciju nekog dobavljača.

**AI model:** Bira AI nivo koji se koristi za ekstrakciju tabela: **Fast** (podrazumevano), **Full** (najveća tačnost, sporije) ili **Nexus** (treći nivo, uključuje se na zahtev). Tabela ispod birača prikazuje:

* Koji **dobavljači** koriste koji AI model
* Da li koriste E-Text
* Opcije za brisanje unosa ili resetovanje podataka obuke

### Zašto tabela izgleda drugačije kod svakog dobavljača?

Sve što DocBits nauči o tabeli čuva se **po dobavljaču**:

* **Sačuvana pravila** (obuka tabele): položaj tabele i mapiranje njenih kolona na rasporedu tog dobavljača.
* **Oznake (tags) i pravila formatiranja AI tabele**: napomene koje je korisnik sačuvao za AI tabelu tog dobavljača.
* **AI model specifičan za dobavljača**: nivo izabran za tog dobavljača pod *Više postavki* na ekranu za validaciju.

Zato dobavljač A sa sačuvanim pravilima prikazuje determinističku tabelu na kartici *Ekstrahovana tabela* ekrana za validaciju, dok dobavljač B bez pravila dobija *AI ekstrahovanu tabelu*. Da bi se dobavljač B ponašao kao A, jednom obučite tabelu dobavljača B. Da biste resetovali dobavljača, obrišite njegova pravila na ekranu za validaciju ili resetujte njegove podatke obuke u tabeli AI modela.

### Ključevi preferenci

Svaki prekidač u ovom odeljku čuva se kao preferenca organizacije. Koristite ključ kada vrednost postavljate preko API-ja (`/preferences/set_preference`), skripte ili DocBits MCP-a (`get_preference` / `set_preference`).

| Podešavanje (oznaka u interfejsu) | Ključ preference | Vrednosti |
|---|---|---|
| Ekstrakcija tabela | `TABLE_EXTRACTION_SETTING` | `true` / `false` |
| AI ekstrakcija tabela | `USE_AI_TABLE_EXTRACTION` | `true` / `false` |
| Koristi Vision ekstrakciju tabela (AI) | `TABLE_EXTRACTION_USE_VISION` | `true` / `false` |
| Koristi strukturiranu ekstrakciju (AI) | `USE_STRUCTURED_EXTRACTION` | `true` / `false` |
| Ekstrakcija tabela za elemente troškova | `CHARGES_TABLE_EXTRACTION` | `true` / `false` |
| Automatski ekstrahuj poreski kod | `AUTO_EXTRACT_TAX_CODE` | `true` / `false` |
| Čuvanje pravila ekstrakcije (samo administratori) | `ONLY_ADMIN_CAN_SAVE_RULES` | `true` / `false` |
| AI model | `AI_MODEL` | `gpt-5.4-mini` (Fast), `gpt-5.5` (Full), `qwen3.8-max` (Nexus) |
| Verzija ekstrakcije tabela (dijalog za potvrdu) | `TBL_EXT_VERSION` | string verzije |
| OCR podešavanja → Koristi AI podatke za tabele ako su dostupni | `USE_AI_DATA_FOR_TABLE` | `true` / `false` |
| OCR podešavanja → Koristi E-Text ako je dostupan | `USE_ETEXT_IF_AVAILABLE` | `true` / `false` |

Napomene:

* Logičke (boolean) preference čuvaju se kao stringovi `true` / `false`; ključ koji nikada nije postavljen računa se kao `false`. Ako pošaljete `1` ili `0`, DocBits čuva `true` / `false`.
* Nepostavljen `AI_MODEL` znači **Fast**.
* Izmena ključa važi za dokumente koji se obrađuju nakon toga. Ponovo pokrenite dokument da bi bio ponovo ekstrahovan sa novim podešavanjem.
* Izbori po dobavljaču (E-Text, AI model, sačuvana pravila) nisu preference organizacije; postavljaju se na ekranu za validaciju pod *Više postavki* za dokument tog dobavljača.
