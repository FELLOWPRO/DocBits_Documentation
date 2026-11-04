---
description: "P1: Exportvarianten, open taken en eindstatus kiezen"
---

# P1: Exportvarianten, open taken en eindstatus kiezen

**Start Export** gebruikt de ingestelde exportroute. **Export with Export Configuration** voert een gekozen configuratie uit. De uitgestelde variant zet die klaar voor de laatste export aan het einde van de huidige uitvoering. Klaarzetten betekent geen automatische verzending na alle latere menselijke goedkeuringen.

De onderzochte nieuwere versies bieden `status=finished` of `status=exported`: finished sluit het document, exported laat verder bewerken toe. Start Export biedt dit vanaf v4; geconfigureerde en uitgestelde export vanaf v3. Oudere versies gebruiken finished. Ontbreekt de keuze in nieuwere versies, dan gebruikt de code ook finished; een ongeldige waarde is een configuratiefout.

Met `ignore_pending_tasks=false` worden open taken gecontroleerd. Daardoor kan de documentdienst onmiddellijke geconfigureerde export weigeren. Die kaart bewijst geen automatische hervatting na latere taakafronding. Bepaal een nieuw uitvoeringsevenement en controleer een bestaande doelregistratie voordat u opnieuw verzendt. Taken negeren vervangt geen goedkeuring.

Verbind export pas na een expliciet gecontroleerde goedkeuringsvoorwaarde. Acceptatie omvat open taak, afgeronde taak, ontbrekende goedkeuring, ontvangst door het testdoel en een herhaalde uitvoering. Onderscheid exportaanvraag, ontvangst en ERP-verwerking. Het pakket bevat geen echte exportbestemmingen en zijn tests bewijzen geen aflevering.

## Kaarten en voorbeeldparameters

Deze waarden beschrijven kaartparameters, geen volledig importeerbare workflow. Vervang YOUR_* door eigen testkeuzes. De ontwerper beheert het verborgen aanroeper-ID. Catalogus: Dev, DocFlow 2.10.38, 21 oktober 2026; controleer versies en rechten van uw organisatie afzonderlijk.

### `export` · v4

Identiteit: `757f30ca-ed60-4e04-8131-2779df17f019`

| Parameter | Type / keuzes | Voorbeeld |
| --- | --- | --- |
| `boolean` | `boolean:bool` | `true` |
| `status` | `finished / exported` | `"finished"` |

### `action_export_with` · v3

Identiteit: `ebcd854d-68b3-4b5f-8d45-1bcf8c675b21`

| Parameter | Type / keuzes | Voorbeeld |
| --- | --- | --- |
| `export_configuration` | `export_configuration:int` | `"YOUR_TEST_EXPORT_CONFIGURATION_ID"` |
| `ignore_pending_tasks` | `ignore_pending_tasks:bool` | `false` |
| `status` | `finished / exported` | `"exported"` |

### `action_export_with_config_deferred` · v3

Identiteit: `060ef4c8-625f-447c-83c9-2ca3f680d88d`

| Parameter | Type / keuzes | Voorbeeld |
| --- | --- | --- |
| `export_configuration` | `export_configuration:int` | `"YOUR_TEST_EXPORT_CONFIGURATION_ID"` |
| `ignore_pending_tasks` | `ignore_pending_tasks:bool` | `false` |
| `status` | `finished / exported` | `"finished"` |

## Zakelijke testgevallen

| Geval | Invoer / configuratie | Verwacht resultaat |
| --- | --- | --- |
| EXPORT-01 | status=finished | gesloten |
| EXPORT-02 | status=exported | bewerkbaar |
| EXPORT-03 | ignore_pending_tasks=false; pending_tasks>0 | weigering mogelijk; automatische hervatting niet bewezen |
| EXPORT-04 | action_export_with_config_deferred | klaargezet ≠ ontvangen |
| EXPORT-05 | RUN-1 → RUN-2 | destination_records=1 |

## Bewijs en grenzen

Parameters en gedrag zijn vergeleken met de Dev-catalogus en onderzochte broncode. Zakelijke testgevallen vormen een acceptatieprocedure. Voor dit hoofdstuk zijn geen persoonlijke goedkeuringen, echte wijzigingen of afleveringen uitgevoerd.

[Verder leren](../workflow-learning-path.md) · [Oefenpakket](../workflow-training-kit.md)
