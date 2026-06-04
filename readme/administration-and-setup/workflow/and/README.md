# And

## Razumevanje "And" kartica

### **Svrha "And" kartica:**

* **And** kartice služe kao kartice uslova koje navode kriterijume koji moraju biti ispunjeni da bi se radni tok nastavio. One zapravo deluju kao logički "AND" operatori, što znači da svi uslovi navedeni u ovim karticama moraju biti zadovoljeni da bi se pokrenula naredna akcija.

#### Kategorije "And" kartica

Iz snimaka ekrana jasno je da ove kartice pokrivaju širok spektar uslova, koji uključuju:

* **Compare with Purchase Order**:
  * Uslovi vezani za validaciju i poređenje sa nalozima za nabavku, kao što su poređenje datuma isporuke, jediničnih cena ili razlika u količinama. Ovo je ključno za obezbeđivanje da transakcije budu usklađene sa dogovorenim uslovima.

<figure><img src="../../../.gitbook/assets/image (14) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

* **Document Field**:
  * Ovo uključuje uslove zasnovane na određenim poljima unutar dokumenata, kao što su označena polja za potvrdu, poređenje vrednosti polja ili obezbeđivanje da polje dokumenta zadovoljava navedenu toleranciju. Ovo je posebno važno za integritet podataka i automatizovane provere unutar formulara ili sistema za upravljanje dokumentima.

<figure><img src="../../../.gitbook/assets/image (15) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

* **Date & Time:**
  * Uslovi zasnovani na datumima i vremenima

<figure><img src="../../../.gitbook/assets/image (16) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

* **Document**:
  * Uslovi zasnovani na karakteristikama dokumenta, kao što su tip ili povezanost sa određenom pod-organizacijom. Ovi uslovi mogu usmeravati radne tokove na osnovu kategorizacije dokumenata ili uključenosti odeljenja.

<figure><img src="../../../.gitbook/assets/image (18) (1) (1).png" alt=""><figcaption></figcaption></figure>

* **Logic**:
  * Logički uslovi koji mogu uključivati procene kao što su "Nastavi sa verovatnoćom od X%" ili izvršavanje HTTPS zahteva, koji su od ključnog značaja za integracije i probabilističko odlučivanje unutar radnih tokova.

<figure><img src="../../../.gitbook/assets/image (19) (1) (1).png" alt=""><figcaption></figcaption></figure>

* **Status**:
  * Fokusirajući se na status dokumenata ili zadataka, ovi uslovi obezbeđuju da samo stavke u određenim stanjima pokreću određene radne tokove, što je ključno za upravljanje procesima vođenim statusom.

<figure><img src="../../../.gitbook/assets/image (20) (1) (1).png" alt=""><figcaption></figcaption></figure>

* **Table**:
  * Ovo uključuje uslove zasnovane na podacima tabele, kao što su poklapanje regex obrazaca ili poređenje vrednosti unutar tabele. Takvi uslovi su od suštinskog značaja za validaciju i manipulaciju velikim skupovima podataka.

<figure><img src="../../../.gitbook/assets/image (22) (1) (1).png" alt=""><figcaption></figcaption></figure>

* **Assignee**:
  * Uslovi zasnovani na osobama kojima su dodeljeni zadaci ili dokumenti. Ovo obezbeđuje da se akcije preduzimaju samo kada su određeni korisnici uključeni, čime se poboljšava odgovornost i specifičnost zadataka.

<figure><img src="../../../.gitbook/assets/image (23) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Praktična primena

Ove "And" kartice se konfigurišu unutar radnog toka da bi vršile provere i validacije koje obezbeđuju da se proces strogo pridržava poslovnih pravila i standarda integriteta podataka. Na primer:

* **Radni tok može koristiti "And" karticu da proveri da li se ukupan iznos fakture poklapa sa nalogom za nabavku pre nego što pokrene plaćanje.**
* **Drugi radni tok bi mogao koristiti "And" karticu da obezbedi da određeni članovi tima pregledaju dokument pre nego što pređe u sledeću fazu.**

### Zaključak

"And" kartice su osnovna komponenta sistema radnih tokova koji zahtevaju preciznu kontrolu nad izvršavanjem procesa na osnovu više uslova. One obezbeđuju da svaki korak radnog toka nastavi samo kada su svi neophodni kriterijumi temeljno ispunjeni, čime se automatizuju složena stabla odlučivanja unutar poslovnih procesa.

Pravilno razumevanje i konfigurisanje ovih kartica je ključno za iskorišćavanje punih mogućnosti vašeg sistema za upravljanje radnim tokovima radi poboljšanja efikasnosti, tačnosti i usklađenosti unutar organizacionih procesa.
