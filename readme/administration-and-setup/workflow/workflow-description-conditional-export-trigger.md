# Workflow Primer: Uslovni okidač za izvoz

<figure><img src="../../.gitbook/assets/image (3) (2) (2).png" alt=""><figcaption></figcaption></figure>

Ovaj radni tok opisuje uslove pod kojima treba pokrenuti proces izvoza. On obezbeđuje da se za izvoz obrađuju samo dokumenti koji ispunjavaju sve navedene kriterijume, čime se poboljšava integritet podataka i usklađenost sa poslovnim pravilima.

### When:

* Dokument u sistemu se procenjuje radi podobnosti za izvoz.

### Logika:

1. **Provera tipa dokumenta**
   * Dokument mora biti određenog tipa (npr. „Invoice“ ili „Receipt“). Navedite tip dokumenta koji je podoban za proces izvoza.
2. **Verifikacija statusa**
   * Trenutni status dokumenta mora ispunjavati unapred definisane kriterijume (npr. „Approved“ ili „Ready for Export“) što ukazuje na to da je spreman za dalju obradu.
3. **Kontekstualni uslovi**
   * Vrše se dodatne provere kako bi se obezbedilo da se detalji dokumenta usklađuju sa određenim zahtevima. Ove provere mogu uključivati verifikaciju informacija unutar potvrda porudžbina ili narudžbenica. Navedite određene uslove koji moraju biti ispunjeni. Na primer:
     * Sve stavke navedene u potvrdi porudžbine odgovaraju onima u narudžbenici.
     * Ukupan iznos u potvrdi porudžbine odgovara ukupnom iznosu u narudžbenici.
     * Datumi isporuke navedeni u potvrdi porudžbine usklađeni su sa onima u narudžbenici.

### Then:

#### Akcija:

* **Pokretanje izvoza**
  * Ako su svi gore navedeni uslovi ispunjeni, sistem automatski pokreće proces izvoza za dokument.
  * Ovo može uključivati generisanje izvozne datoteke, slanje podataka u eksterni sistem ili pokretanje radnog toka u drugoj aplikaciji.

#### Primer implementacije:

```yaml
rules:
  - description: "Conditional Export Trigger"
    conditions:
      - type: "DocumentType"
        criteria: "<SpecifyDocumentType>"
      - type: "Status"
        criteria: "<SpecifyStatus>"
      - type: "DetailMatch"
        criteria:
          - "ItemMatch"
          - "AmountMatch"
          - "DateMatch"
    actions:
      - operation: "StartExport"
```
