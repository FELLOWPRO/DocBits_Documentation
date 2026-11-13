---
description: "P1: Een beslissingstabel tot de toewijzing volgen"
---

# P1: Een beslissingstabel tot de toewijzing volgen

Een beslissingstabel koppelt invoervelden aan getypeerde resultaten. Het voorbeeld gebruikt `cost_center=4711` en `total_amount`: beoordelaar A tot en met 1000, B daarboven. Maak twee niet-overlappende regels met geldige gebruikers van uw testorganisatie. Het pakketbestand beschrijft de configuratie en garandeert geen import in de editor.

Schakel bij **Decision Table has Returns** v3 `store_data=wf_store_data` in. Versie 2 leest de booleaanse opslagoptie. De volgende toewijzingskaart vereist resultaten die in dezelfde uitvoering zijn opgeslagen. Een geslaagde tabeluitvoering bevestigt nog geen geldige gebruiker.

Een gebruikersresultaat kan `output_type=user` en `value=101` bevatten; 101 is synthetisch en moet door een bestaande testgebruiker worden vervangen. Kies daarna **Assign document based on decision table** met `assignee_type=user`. De onderzochte versie 2 van deze actie kiest het laatste passende resultaat. Meerdere treffers vereisen niet automatisch goedkeuring van alle gebruikers.

Test één, geen en meerdere treffers, verkeerd resultaattype, ongeldig gebruikers-ID en uitgeschakelde opslag. Verbind geen treffer en toewijzingsfouten met een expliciet alternatief. Bepaal volgorde en trefferbeleid in plaats van toevallige tabelvolgorde tot bedrijfsregel te maken. Accepteer de werkelijke toewijzing op het document.

De beslissingstabelvoorwaarde roept de tabeldienst werkelijk aan om de tabel te beoordelen. Testmodus garandeert niet dat alle bijwerkingen ontbreken; gebruik uitsluitend eigen testgegevens en controleer de gebruikte acties.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/decision-tables/v1/nl.mp4" %}

**Video:** Beslissingstabellen in toewijzingskaarten · 2:01 · [Ondertitels (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/decision-tables/v1/nl.vtt)

<details>

<summary>Transcriptie</summary>

**Beslissingstabellen in twee stappen** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/decision-tables/v1/nl.mp4#t=0.25)

Beslissingstabellen bepalen wie een document behandelt. In een Workflow werken ze in twee stappen. Een En-kaart voert de tabel uit en bewaart wat die teruggeeft. Dan-kaarten gebruiken dat om het document toe te wijzen of taken te maken.

**Succes, mislukte conditie of fout** · [0:16](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/decision-tables/v1/nl.mp4#t=16.85)

De En-kaart slaagt als de tabel minstens één treffer voor het document teruggeeft. Zonder treffer eindigt ze als mislukte conditie en volgt ze het oranje pad. Zonder geselecteerde tabel, of als de tabel niet kan lopen, eindigt ze als fout.

**Tabel uitvoeren en resultaten opslaan** · [0:33](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/decision-tables/v1/nl.mp4#t=33.95)

Voeg de En-kaart Beslissingstabel bevat resultaten toe en kies de beslissingstabel. Stel haar dan in om de teruggegeven gegevens op te slaan. Zonder dat hebben de kaarten erna niets om mee te werken.

**Eerste gebruiker krijgt het document, iedereen een taak** · [0:49](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/decision-tables/v1/nl.mp4#t=49.05)

Op het succespad geeft de Dan-kaart die toewijst aan de eerste teruggegeven gebruiker, het document aan de eerste gebruiker uit de tabel. Elke teruggegeven gebruiker, ook de eerste, krijgt een taak of melding. Geef de taak een titel, beschrijving en prioriteit, en kies of er ook een e-mail gaat. Groepen in de resultaten worden genegeerd.

**Geen velden: alles uit de tabel** · [1:16](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/decision-tables/v1/nl.mp4#t=76.416)

De kaart die het document sequentieel toewijst aan Gebruiker/Groep op basis van de beslissingstabel, heeft daarentegen geen velden. Ze neemt gebruikers en groepen uit de tabel, elk met de prioriteit die de tabel geeft, of een standaardwaarde. Aan het eind van de uitvoering krijgt de regel met het laagste prioriteitsnummer het document, tenzij een andere kaart het al direct heeft toegewezen.

**Welke kaart voor welke taak** · [1:40](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/decision-tables/v1/nl.mp4#t=100.383)

Kortom: om het document aan één persoon te geven en de rest te informeren, gebruikt u de kaart voor de eerste gebruiker. Laat de tabel alles beslissen, ook prioriteiten? Neem dan de sequentiële kaart zonder velden. Wilt u alleen taken, gebruik dan de taakkaart voor resultaten van de beslissingstabel.

</details>

## Kaarten en voorbeeldparameters

Deze waarden beschrijven kaartparameters, geen volledig importeerbare workflow. Vervang YOUR_* door eigen testkeuzes. De ontwerper beheert het verborgen aanroeper-ID. Catalogus: Dev, DocFlow 2.10.38, 21 oktober 2026; controleer versies en rechten van uw organisatie afzonderlijk.

### `condition_decision_tree_data` · v3

Identiteit: `c40160ce-805f-4312-8726-51b0fd7af8ec`

| Parameter | Type / keuzes | Voorbeeld |
| --- | --- | --- |
| `decision_table` | `decision_table:str` | `"YOUR_TEST_DECISION_TABLE_ID"` |
| `boolean` | `boolean:bool` | `true` |
| `store_data` | `wf_store_data / wf_do_not_store_data` | `"wf_store_data"` |

### `action_assign_doc_based_on_decision_table` · v2

Identiteit: `699912a7-2369-47e0-9092-8d027e13752a`

| Parameter | Type / keuzes | Voorbeeld |
| --- | --- | --- |
| `assignee_type` | `user / group` | `"user"` |

## Zakelijke testgevallen

| Geval | Invoer / configuratie | Verwacht resultaat |
| --- | --- | --- |
| DT-01 | 4711; 1000; store_data=wf_store_data | USER_A |
| DT-02 | 4711; 1000.01; store_data=wf_store_data | USER_B |
| DT-03 | geen resultaat / ongeldige gebruiker / verkeerd type | Terugvalroute |
| DT-04 | returns=[USER_A, USER_B]; assign v2 | USER_B |
| DT-05 | store_data=wf_do_not_store_data | geen opgeslagen resultaat voor toewijzing |

## Bewijs en grenzen

Parameters en gedrag zijn vergeleken met de Dev-catalogus en onderzochte broncode. Zakelijke testgevallen vormen een acceptatieprocedure. Voor dit hoofdstuk zijn geen persoonlijke goedkeuringen, echte wijzigingen of afleveringen uitgevoerd.

[Verder leren](../workflow-learning-path.md) · [Oefenpakket](../workflow-training-kit.md)
