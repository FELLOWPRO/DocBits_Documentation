# Then

## Pregled "Then..." kartica akcija

### **1. Akcije nad poljima dokumenta:**

* **Invert Checkbox:** Ova akcija prebacuje stanje polja za potvrdu u dokumentu.
* **Set Checkbox:** Postavlja stanje polja za potvrdu na tačno (označeno) ili netačno (neoznačeno).
* **Set Field to Text:** Ova akcija postavlja navedeno polje dokumenta na zadatu tekstualnu vrednost.

<figure><img src="../../../.gitbook/assets/then1 (1).png" alt=""><figcaption></figcaption></figure>

### **2. Akcije nad dokumentom:**

* **Approve the Document:** Označava dokument kao odobren u sistemu.
* **Reject the Document:** Označava dokument kao odbijen.

<figure><img src="../../../.gitbook/assets/image (259).png" alt=""><figcaption></figcaption></figure>

### **3. Akcije izvoza:**

* **Export document with export configuration:** Pokreće proces izvoza sa određenom konfiguracijom izvoza.
* **Start Export:** Pokreće proces izvoza.

<figure><img src="../../../.gitbook/assets/image (260).png" alt=""><figcaption></figcaption></figure>

### **4. Akcije statusa:**

* **Change Status:** Menja status dokumenta ili zadatka u navedeni novi status.

<figure><img src="../../../.gitbook/assets/then3 (1).png" alt=""><figcaption></figcaption></figure>

### **5. Akcije zadataka:**

* Dodele i obaveštenja:
  * **Assign Task:** Kreira i dodeljuje zadatak sa određenim detaljima pojedincu ili grupi, uključujući opcije za obaveštavanje putem e-pošte.
  * **Create a New Task:** Slično dodeljivanju, ali fokusirano na postavljanje potpuno novog zadatka u sistemu.

<figure><img src="../../../.gitbook/assets/then4 (1).png" alt=""><figcaption></figcaption></figure>

### **6. Akcije nad tabelama:**

* **Calculate in Table:** Vrši proračune nad podacima tabele na osnovu navedenih uslova i čuva rezultate u određenoj koloni.
* **Change Entries:** Ažurira unose u tabeli na osnovu navedenih uslova.

<figure><img src="../../../.gitbook/assets/then5 (1).png" alt=""><figcaption></figcaption></figure>

### **7. Akcije osobe kojoj je dodeljeno (Assignee):**

* **Assign User from Field:** Dodeljuje korisnika zadatku ili dokumentu na osnovu korisničkih podataka sačuvanih u određenom polju, uz opciju rezervnog korisnika ako primarni nije dostupan.
* **Assign Document to User or Group:** Direktno dodeljuje dokument korisniku ili grupi, obezbeđujući da odgovornost bude odgovarajuće dodeljena.

<figure><img src="../../../.gitbook/assets/then6 (1).png" alt=""><figcaption></figcaption></figure>

### **8. Akcije eksterne interakcije:**

* **Call API:** Šalje zahtev eksternom API-ju, koji se može prilagoditi određenim metodama, parametrima i podacima.
* **Send HTTPS Request:** Slično pozivima API-ja, ali posebno formatirano za HTTPS protokole.

<figure><img src="../../../.gitbook/assets/then7 (1).png" alt=""><figcaption></figcaption></figure>

### **9. Napredna obrada:**

* **Run Workflow:** Pokreće drugi radni tok unutar sistema, omogućavajući složeno ulančavanje procesa.

#### Praktična primena

Ove kartice akcija se koriste za automatizaciju odgovora na osnovu određenih okidača identifikovanih u ranijim delovima podešavanja radnog toka. Na primer:

* Ako se utvrdi da dokument zahteva pregled, akcija "Approve the Document" se može automatski pokrenuti kada prođe sve navedene uslove.
* Za zadatke upravljanja podacima, akcije "Set Checkbox" ili "Set Field to Text" obezbeđuju da se polja dokumenta automatski ažuriraju, smanjujući ručni unos podataka i mogućnost grešaka.
* Složeni zadaci kao što su interakcije sa API-jem ili promene statusa pojednostavljuju interakcije ne samo unutar ERP sistema već i sa eksternim servisima i alatima, čime se poboljšavaju integracija i funkcionalnost.

### Zaključak

"Then..." odeljak u vašem sistemu radnih tokova pruža robustne alate za definisanje preciznih akcija koje treba da se dogode kao rezultat ispunjenosti uslova u radnom toku. Efikasnim korišćenjem ovih akcija, preduzeća mogu automatizovati rutinske procese, obezbediti tačnost podataka i dinamično reagovati na promenljive informacije i stanja sistema. Razumevanje kako konfigurisati i koristiti ove akcije ključno je za maksimalno iskorišćavanje efikasnosti i delotvornosti mogućnosti radnih tokova vašeg ERP sistema.
