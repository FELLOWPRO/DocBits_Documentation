# Test Manager

**Test Manager** vam omogućava da sačuvate **scenarije testiranja** za višekratnu upotrebu u vašim radnim tokovima i da ih pokrećete zajedno — kako biste potvrdili da se radni tok i dalje ponaša ispravno nakon što ga izmenite. Funkcioniše i za standardne i za napredne radne tokove.

Otvorite ga iz **Workflow Dashboard → Test Manager List**.

<figure><img src="../../.gitbook/assets/workflow_test_manager.png" alt="Lista Test Manager-a sa scenarijima testiranja, statusom i opcijom Run All Tests"><figcaption><p>Lista Test Manager-a — svaki sačuvani scenario prikazuje rezultat prošao/pao.</p></figcaption></figure>

## Šta je scenario testiranja

Scenario testiranja obuhvata radni tok, primer ulaznih podataka i **očekivani ishod**. Kada ga pokrenete, Test Manager ponovo izvršava radni tok nad tim ulaznim podacima i upoređuje rezultat sa onim što ste očekivali — pretvarajući red u **zeleni** (prošao) ili **crveni** (pao).

## Rad sa scenarijima

- **Add Test Scenario** — kreirajte novi scenario iz radnog toka i primera dokumenta.
- **Run All Tests** — pokrenite sve scenarije odjednom i odmah vidite koji radni tokovi i dalje prolaze.
- **View Details** — otvorite scenario da biste pregledali njegov rezultat.

<figure><img src="../../.gitbook/assets/workflow_test_manager_detail.png" alt="Detalji scenarija testiranja radnog toka sa statusom, vremenom izvršavanja i podacima"><figcaption><p>Detalji scenarija — naziv, status, vreme izvršavanja, kao i stvarni i izdvojeni podaci koje je pokretanje proizvelo.</p></figcaption></figure>

Prikaz detalja prikazuje naziv scenarija i **status**, **naziv radnog toka**, **vreme izvršavanja**, kao i **stvarne** i **izdvojene podatke** koje je pokretanje proizvelo — tako da možete tačno videti zašto je scenario prošao ili pao.

## Test Manager naspram testiranja u alatu za izradu

Ovo su dve različite stvari:

- **Test Manager** (ova stranica) — *sačuvani, ponovljivi* scenariji sa očekivanim ishodima, koji se pokreću zajedno pomoću **Run All Tests**. Koristite ga za regresiono testiranje nakon izmena.
- **Testiranje u alatu za izradu** — ugrađene **Validate** i **Test** kontrole unutar alata za izradu naprednog radnog toka, za brze provere dok gradite. Pogledajte [Validacija i testiranje](advanced-workflow/validation-and-testing.md).
