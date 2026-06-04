---
hidden: true
---

# In Order Confirmation Purchase Order

### Compare with Purchase Order:

**In Order Confirmation Purchase Order**

<figure><img src="https://lh7-us.googleusercontent.com/glQHETatKah-1YugeLqBb7Jim6lNJxuarRv-KEMv4NPzFfcjSm6mVhTMdI30nxdJ0SHXZ55Oup6KH7K-J6IxjUOiG0wxUX8toAaCopgBJwPyr94CPjoKuauNTmoHGGhg6f3gwHD39W7gpvijg4LQVJ4" alt="" width="563"><figcaption></figcaption></figure>

#### Logic kartica: Poklapanje količine ili jedinične cene ili popusta

Ova logic kartica je dizajnirana da automatski proveri da li se količina, jedinična cena ili popust detaljno navedeni u potvrdi porudžbine poklapaju sa odgovarajućim vrednostima u nalogu za nabavku. Ova provera obezbeđuje doslednost i tačnost između onoga što je naručeno i onoga što dobavljač potvrđuje da će isporučiti.

#### Uslov okidača

Logika se aktivira kada je bilo koji od sledećih uslova ispunjen u potvrdi porudžbine u odnosu na originalni nalog za nabavku:

* **Quantity**: Količina naručenih stavki poklapa se sa količinom koju je dobavljač potvrdio.
* **Unit Price**: Dogovorena cena po stavki poklapa se sa dobavljačevom potvrdom.
* **Discount**: Svi primenjeni popusti su dosledni između naloga za nabavku i potvrde porudžbine.

#### Ishodi

* **Equals**: Ako se količina, jedinična cena ili popust iz potvrde porudžbine tačno poklapaju sa nalogom za nabavku, sistem smatra potvrdu validnom i nastavlja sa sledećim koracima u procesu nabavke.
* **Not Equal**: Ako postoji nepodudaranje u količini, jediničnoj ceni ili popustu, sistem označava potvrdu porudžbine za ručni pregled. Ovo obezbeđuje da se sva neslaganja reše pre nastavka.

#### Prednosti

* **Tačnost i doslednost**: Održava tačnost u procesu nabavke, obezbeđujući da se plaćanja i isporuke vrše na osnovu ispravnih vrednosti.
* **Efikasnost**: Automatizuje proces provere, smanjujući potrebu za ručnim proverama i ubrzavajući obradu porudžbina.
* **Kontrola troškova**: Pomaže u sprečavanju preplaćivanja ili pogrešnih isporuka otkrivanjem nepodudaranja rano u procesu.

<figure><img src="https://lh7-us.googleusercontent.com/DRTMJxJ9XLeC5zWSU8QuZwPLkqHzmCUm9RwiUZIkcc8pVxMZsxLv56dX9spzqr7KeDkTigbeBX2DvAZRe-6MdqOgAnrO-QPnCbi4e6hP4--P_O0A0DSoQJxjGeefOS1p6GuXHs1YXv-A73DXYaE8qlI" alt="" width="563"><figcaption></figcaption></figure>

1. **Definisanje parametara poređenja**: Podesite određena polja (količina, jedinična cena, popust) koja će logic kartica proveravati radi poklapanja.
2. **Automatizacija provere**: Konfigurišite sistem da automatski upoređuje ove detalje po prijemu potvrde porudžbine.
3. **Prilagođavanje upozorenja**: Odlučite o radnom toku za rukovanje nepodudaranjima, uključujući prilagođavanje upozorenja za ručni pregled.

Ova logic kartica je od vitalnog značaja za obezbeđivanje da se detalji potvrde porudžbine poklapaju sa originalnim nalogom za nabavku, štiteći integritet ciklusa nabavke. \`\`
