---
description: "P1: Een beslissingstabel tot de toewijzing volgen"
---

# P1: Een beslissingstabel tot de toewijzing volgen

Een beslissingstabel koppelt invoervelden aan getypeerde resultaten. Het voorbeeld gebruikt `cost_center=4711` en `total_amount`: beoordelaar A tot en met 1000, B daarboven. Maak twee niet-overlappende regels met geldige gebruikers van uw testorganisatie. Het pakketbestand beschrijft de configuratie en garandeert geen import in de editor.

Schakel bij **Decision Table has Returns** v3 `store_data=wf_store_data` in. Versie 2 leest de booleaanse opslagoptie. De volgende toewijzingskaart vereist resultaten die in dezelfde uitvoering zijn opgeslagen. Een geslaagde tabeluitvoering bevestigt nog geen geldige gebruiker.

Een gebruikersresultaat kan `output_type=user` en `value=101` bevatten; 101 is synthetisch en moet door een bestaande testgebruiker worden vervangen. Kies daarna **Assign document based on decision table** met `assignee_type=user`. De onderzochte versie 2 van deze actie kiest het laatste passende resultaat. Meerdere treffers vereisen niet automatisch goedkeuring van alle gebruikers.

Test één, geen en meerdere treffers, verkeerd resultaattype, ongeldig gebruikers-ID en uitgeschakelde opslag. Verbind geen treffer en toewijzingsfouten met een expliciet alternatief. Bepaal volgorde en trefferbeleid in plaats van toevallige tabelvolgorde tot bedrijfsregel te maken. Accepteer de werkelijke toewijzing op het document.

De beslissingstabelvoorwaarde roept de tabeldienst werkelijk aan om de tabel te beoordelen. Testmodus garandeert niet dat alle bijwerkingen ontbreken; gebruik uitsluitend eigen testgegevens en controleer de gebruikte acties.

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
