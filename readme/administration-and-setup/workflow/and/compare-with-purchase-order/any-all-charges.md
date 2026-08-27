# Any / All Charges

<figure><img src="../../../../.gitbook/assets/workflow_cards_and_po_compare_any_all_charges.png" alt="Kartica u biblioteci kartica, verzija 2 i verzija 3"><figcaption><p>Kartica u biblioteci kartica. Verzija 2 gore, verzija 3 dole.</p></figcaption></figure>

## **Svrha:**

Ova kartica toka rada upoređuje dodatne naknade na dokumentu sa dodatnim naknadama na povezanom nalogu za nabavku, u okviru definisane tolerancije. Odgovara na jedno pitanje: da li se dokument i nalog za nabavku slažu o dodatnim naknadama? Upoređuje se svaka naknada koju je povezivanje naloga za nabavku uparilo, pa na kartici nije potrebno navesti nijedno ime polja.

Ova kartica se razlikuje od **Compare Total Charges**, koja upoređuje jedno navedeno polje dokumenta sa jednom naknadom određenom preko Charge ID. Koristite ovu karticu kada sve uparene naknade dokumenta treba proveriti odjednom.

Povezivanje naloga za nabavku mora da se izvrši pre ove kartice. Ako dokument nema povezan nalog za nabavku, kartica zaustavlja tok rada i prijavljuje da podaci nedostaju.

## **Komponente kartice:**

1. **Any / All:**
   * **Opis**: Kako se pojedinačna upoređivanja naknada spajaju u jedan rezultat kartice.
   * **Opcije**:
     * **Any**: najmanje jedna naknada mora da zadovolji upoređivanje.
     * **All**: svaka naknada mora da zadovolji upoređivanje.
2. **Operator:**
   * **Opis**: Kako se iznos naknade na dokumentu upoređuje sa iznosom naloga za nabavku za istu naknadu.
   * **Opcije**:
     * **Within**: dva iznosa moraju da se slažu, uz dopuštenu toleranciju.
     * **Outside**: dva iznosa moraju da se razlikuju za više od tolerancije.
3. **Tolerance Amount:**
   * **Opis**: Dopušteno odstupanje između naknade na dokumentu i naknade na nalogu za nabavku.
4. **Tolerance Type:**
   * **Opis**: Kako se iznos tolerancije tumači.
   * **Opcije**:
     * **Percentage**: procenat naknade iz naloga za nabavku.
     * **Value**: fiksan iznos.
5. **Missing Data Behaviour (samo verzija 3):**
   * **Opis**: Šta učiniti kada naknada postoji samo na jednoj strani, na dokumentu ili na nalogu za nabavku, tako da nema odgovarajuće naknade sa kojom bi se uporedila. Opcija se nalazi na kraju rečenice verzije 3.
   * **Opcije**:
     * **treat as a mismatch**: tok rada se zaustavlja. To je podrazumevana vrednost.
     * **ignore it and treat as a match**: tok rada se nastavlja kao da se naknada slagala.

## **Funkcionalnost:**

Kartica prolazi kroz sledeće korake.

1. **Zahteva povezan nalog za nabavku.** Bez povezanog naloga za nabavku kartica se odmah zaustavlja i prijavljuje da podaci nedostaju.
2. **Čita toleranciju** iz polja **Tolerance Amount** i **Tolerance Type** na kartici.
3. **Verzija 3 raspoređuje svaku uparenu stavku naloga za nabavku** u jednu od četiri situacije, pitajući samo da li svaka strana nosi bilo kakvu naknadu: naknade na obe strane, nema naknada ni na jednoj strani, naknade samo na dokumentu, ili naknade samo na nalogu za nabavku. Stavka koja ne može da se poveže sa podacima naloga za nabavku na dokumentu predstavlja grešku u podacima i kartica se zaustavlja.
4. **Naknada prisutna samo na jednoj strani odlučuje o celoj kartici.** Čim jedna uparena stavka nosi naknade na jednoj strani a nijednu na drugoj, **Missing Data Behaviour** odlučuje o rezultatu i nijedna naknada se ne upoređuje, uključujući i naknade ispravno uparenih stavki. Operator i tolerancija se ne uzimaju u obzir.
5. **Ako nijedna stavka ne nosi naknade ni na jednoj od dve strane**, obe strane se slažu da nema dodatnih naknada. Operator **Outside** time nije zadovoljen, jer ništa ne odstupa iznad tolerancije, i tok rada se zaustavlja. Svaki drugi operator smatra slaganje zadovoljenim i tok rada se nastavlja. **Missing Data Behaviour** ovde nema efekta.
6. **U suprotnom se svaka naknada upoređuje**, iznos dokumenta prema iznosu naloga za nabavku, uz operator i toleranciju. Iznos naknade koji nije broj zaustavlja karticu sa nedostajućim podacima.
7. **Upoređivanja se sakupljaju i spajaju jednom.** Svaka naknada svake uparene stavke doprinosi jednom skupu rezultata, koji podešavanje **Any / All** svodi na jedan rezultat kartice. Sakupljanje je na nivou dokumenta, ne po stavci, pa **Any** znači bilo koju naknadu na bilo kom mestu u dokumentu. Ako je spojeni rezultat istinit, tok rada se nastavlja, u suprotnom se zaustavlja sa nezadovoljenim uslovom.

Tri posledice je korisno znati pre konfigurisanja kartice.

* **Within sa tolerancijom 0 zahteva tačnu jednakost.** Dva iznosa moraju da se slažu do pare.
* **Naknada prisutna samo na jednoj strani nadjačava sve ostalo.** Pošto se korak 4 izvršava pre svakog upoređivanja, **ignore it and treat as a match** preskače i proveru iznosa svake ispravno uparene naknade u dokumentu. Zadržite **treat as a mismatch** ako iznosi moraju da se provere.
* **treat as a mismatch zaustavlja tok rada kao grešku, a ne kao nezadovoljen uslov.** Uprkos formulaciji, kartica prijavljuje da podaci nedostaju, što dnevnik toka rada i test kartice prikazuju crvenom bojom, a ne narandžastom kao nezadovoljen uslov. Tok rada se zaustavlja u oba slučaja.

## **Podešavanje i konfiguracija:**

Dodajte karticu kao And uslov posle povezivanja naloga za nabavku. Izaberite da li svaka naknada ili bilo koja naknada mora da zadovolji upoređivanje, izaberite operator **Within** ili **Outside** i unesite iznos i tip tolerancije. U verziji 3 izaberite šta treba da se dogodi kada se naknade pojave samo na jednoj strani.

Da biste isprobali konfiguraciju bez čekanja na dokument, otvorite meni kartice u Workflow Builder, izaberite **Test Card**, izaberite dokument i zatim **Test on Document**. Dnevnik kartice navodi svaku upoređenu naknadu sa oba iznosa, operatorom i upotrebljenom tolerancijom, a beleži i koja je vrednost **Missing Data Behaviour** odlučila o rezultatu kada je naknada bila prisutna samo na jednoj strani.

## **Primer scenarija:**

Potvrda narudžbine nosi naknadu za prevoz od 100,00, a povezana stavka naloga za nabavku nosi istu naknadu za prevoz od 100,00. Sa **All**, operatorom **Within** i tolerancijom 0 kao vrednošću, iznosi su jednaki, kartica je zadovoljena i tok rada se nastavlja.

Sa 120,00 na potvrdi narudžbine prema 100,00 na nalogu za nabavku, ista konfiguracija nije zadovoljena i tok rada se zaustavlja sa nezadovoljenim uslovom.

Ako ni potvrda narudžbine ni nalog za nabavku ne nose nikakvu naknadu, operator **Within** to smatra slaganjem i tok rada se nastavlja, dok ga **Outside** zaustavlja.

Ako potvrda narudžbine nosi naknadu za prevoz a nalog za nabavku nijednu, operator više ne važi. Sa **treat as a mismatch** tok rada se zaustavlja, kako bi neko mogao da proveri zašto naknada stoji samo na jednoj strani.

## **Razlike između verzija:**

Verziju 3 koriste nove kartice. Verzija 2 ostaje podržana u postojećim tokovima rada. Obe verzije upoređuju po naknadi i spajaju rezultate na nivou dokumenta pomoću podešavanja **Any / All**, ali verzija 2 nema razvrstavanje po slučajevima, što menja šta se dešava čim naknade nisu prisutne na obe strane:

* Verzija 2 nema opciju **Missing Data Behaviour**. Njena rečenica se završava posle tipa tolerancije.
* Verzija 2 ne razvrstava uparene stavke i zato ne prepoznaje naknadu koja postoji samo na jednoj strani. Upoređuje prisutan iznos sa 0,00 koji se drži za stranu koja nedostaje, a operator odlučuje: **Within** nije zadovoljen i tok rada se zaustavlja, **Outside** je zadovoljen i tok rada se nastavlja. Dnevnik kartice prikazuje upoređivanje sa 0,00.
* Ako nijedna od dve strane ne nosi naknade, verzija 2 nema šta da upoređuje i prijavljuje da podaci nedostaju, umesto da odsustvo na obe strane smatra slaganjem.

## **Zaključak:**

Kartica "Any / All Charges" automatizuje proveru da fakturisane ili potvrđene dodatne naknade odgovaraju naručenim dodatnim naknadama. Pošto odsustvo naknada na obe strane u verziji 3 važi kao slaganje, dokumenti bez dodatnih naknada prolaze bez ručne intervencije, dok se naknade koje se pojavljuju samo na jednoj strani zadržavaju za proveru, osim ako to nije namerno dopušteno.
