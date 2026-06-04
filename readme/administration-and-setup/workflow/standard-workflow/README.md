# Standard Workflow

<figure><img src="../../../.gitbook/assets/DocBits-APWorkflow-Gronbach.drawio (1) (1).svg" alt=""><figcaption></figcaption></figure>

#### Pregled komponenti radnog toka:

* **AP Invoice Email**: Proces verovatno počinje fakturom primljenom putem e-pošte.
* **DocBits**: Ovaj alat se može koristiti za početne zadatke upravljanja dokumentima, kao što su preuzimanje i digitalizacija faktura.
* **Finance Review**: Fakture prolaze kroz finansijski pregled u kome se donose odluke o njihovoj validnosti i tačnosti.

#### Koraci u radnom toku:

1. **Initial Review**:
   * Fakture se primaju i početno obrađuju pomoću DocBits-a.
   * Zatim ih pregleda finansijski tim kako bi se obezbedilo da budu uklonjene iz radnog toka ako su kompletne, ili prosleđene dalje na dalju obradu.
2. **PO vs Non-PO Invoices**:
   * Radni tok pravi razliku između faktura povezanih sa narudžbenicom (PO) i onih bez narudžbenice (non-PO).
   * Fakture bez narudžbenice usmeravaju se na dalje odobrenje ili odbijanje na osnovu unapred definisanih kriterijuma kao što su ID dobavljača, količina, jedinična cena i broj stavke.
3. **Matching and Mismatching**:
   * Fakture se proveravaju u odnosu na prijemnice robe kako bi se obezbedilo da se detalji podudaraju (kao što su ID dobavljača i količina).
   * Ako dođe do neslaganja, faktura podleže daljem pregledu i eventualnom odbijanju.
4. **Finance and Buyer Review**:
   * Za fakture povezane sa narudžbenicom sprovodi se detaljan proces podudaranja koji uključuje pregled kupca.
   * Mogu biti potrebna prilagođavanja narudžbenica ili prijemnica robe.
5. **Final Decisions**:
   * Fakture koje prođu sve provere se odobravaju i integrišu u finansijske sisteme radi vođenja evidencije.
   * Odbijene fakture pokreću obaveštenja, a kupac može zatražiti novu fakturu.
6. **Integration with Infor IDM & LN+M3**:
   * Odobrene fakture se verovatno šalju u Infor IDM radi upravljanja dokumentima i u LN radi knjiženja u glavnoj knjizi.
   * Ova integracija obezbeđuje da su sve finansijske evidencije ažurne i da se radni tok neometano uklapa u širi ERP sistem.

#### Tačke odlučivanja:

* Tokom celog radnog toka postoje razne tačke odlučivanja gde faktura može biti odobrena, odbijena ili vraćena radi dodatnih informacija. Obaveštenja se šalju nakon kašnjenja, obezbeđujući blagovremenu obradu.

Ovi radni tokovi će biti uključeni u standardni radni tok (Standard Workflow)
