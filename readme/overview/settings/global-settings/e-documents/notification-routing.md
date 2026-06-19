# Rutiranje obaveštenja

<figure><img src="../../../../.gitbook/assets/edoc_notification_routing.png" alt="Rute obaveštenja"><figcaption><p>Povezivanje nalaza validacije sa agentima</p></figcaption></figure>

Stranica **Rutiranje obaveštenja** (**Elektronski dokumenti → Akcije**) povezuje nalaze validacije sa **AI Workforce agentima**. Svaki blokirajući nalaz pokreće tačno jednog agenta — onog čiji se prefiks koda najduže poklapa. Sve što se ne poklapa vraća se na podrazumevanog agenta za obaveštavanje dobavljača.

## Rute obaveštenja

Izaberite ko obrađuje koju vrstu problema sa fakturom. Sve što nije navedeno ide podrazumevanom agentu:

| Ruta | Nalazi koje pokriva |
|------|---------------------|
| **Kolumbijska poslovna pravila** | Nalazi poslovnih pravila specifičnih za Kolumbiju. |
| **Nemačka poslovna pravila** | Nalazi poslovnih pravila specifičnih za Nemačku. |
| **Provere IBAN / bankovnog računa** | Nalazi o podacima za plaćanje (kontrolni zbir IBAN, dužina, zemlja). |
| **Provere PIB-a** | Nalazi o formatu PIB-a. |
| **Sve ostalo** | Podrazumevana rezerva za sve što se gore ne poklapa. |

Za svaku rutu izaberite agenta koji je obrađuje iz padajuće liste. **Napredno (prilagođena pravila koda)** omogućava rutiranje prema tačnom kodu nalaza kada vam je potrebna finija kontrola.

## Dostupni agenti

<figure><img src="../../../../.gitbook/assets/edoc_notification_agents.png" alt="Registar dostupnih agenata"><figcaption><p>Registar AI Workforce agenata samo za čitanje</p></figcaption></figure>

Odeljak **Dostupni agenti** je registar samo za čitanje AI Workforce agenata isporučenih sa vašom instalacijom, na primer:

| Agent | Svrha |
|-------|-------|
| **Podrazumevano obaveštenje dobavljaču** | Generička e-pošta za obaveštavanje dobavljača; univerzalni agent kada nijedan specifičniji agent ne odgovara. |
| **Banking Bot** | Specijalizovani šablon za nalaze o podacima za plaćanje (IBAN/BIC ispravke). |
| **Tax Bot** | Obaveštenje dobavljaču specifično za PIB. |
| **Compliance Bot** | Obrađuje nalaze o usklađenosti. |

Svaki agent prikazuje svoj Celery zadatak i prefikse kodova nalaza koje podrazumevano obrađuje.
