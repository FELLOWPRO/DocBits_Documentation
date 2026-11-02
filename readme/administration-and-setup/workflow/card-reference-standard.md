---
description: "Configureer kaarten op basis van naam, versie, invoer, gegevensbereik, resultaten en gevolgen."
---

# Workflowkaarten begrijpen en configureren

Kies een kaart op basis van haar bewerking en gegevensbereik. **Field is** controleert aanwezigheid of leegte; **Docfield is** vergelijkt een waarde. Documenttoewijzing, een taak en een melding hebben verschillende gevolgen. Een categorie vervangt geen referentie voor een specifieke kaartversie.

## Wat een volledige referentie uitlegt

| Onderdeel | Vereiste vraag |
| --- | --- |
| Identiteit | Zichtbare naam, technisch type, versie en When/And/Then-rol? |
| Voorwaarden | Benodigde licentie, rechten en documentgegevens? |
| Invoer | Type, waarde, standaard en toegestane keuzes per parameter? |
| Bereik | Een veld, rij, alle regels of een organisatievariabele? |
| Resultaten | Succes, onwaar of fout? Wat kan de volgende kaart gebruiken? |
| Gevolgen | Wijzigingen aan documenten, taken of externe systemen? Wat simuleert de test? |
| Voorbeelden | Welke volledige configuratie en invoer geven welk resultaat? |
| Grenzen en versies | Ontbrekende gegevens, exacte grenzen en oudere versies? |

## Ingevuld voorbeeld: Docfield is

**Technisch type:** `condition_docfield_operator_value` · **Versie:** 2 · **Rol:** And. Vereist een document met gedefinieerde layout en het te controleren veld.

| Invoer | Configuratie |
| --- | --- |
| Field Name | `total_amount`, de technische sleutel en niet het vertaalde label |
| Operator | `gt` / Groter dan |
| Field Value | `1000`, zonder valutasymbool |

De kaart vergelijkt het veld van het huidige document met de ingestelde waarde. Zij verandert geen status, maakt geen taak en exporteert niet. In Advanced volgt waar Success, normaal onwaar Failed Condition en een evaluatiefout Error. In Standard stopt een niet-vervulde voorwaarde de lineaire reeks.

Werkelijk gecontroleerde gevallen: **1785** → Success; **999** en **1000** → Failed Condition; **1000,01** → Success; ontbrekend of ongeldig getal → Error. JSON gebruikt decimale punten. Dit geldt voor deze numerieke configuratie, niet voor alle typen en operatoren.

Onderscheid deze kaart van expliciete tolerantiekaarten. Leid gelijkheid of inclusieve operatoren niet alleen uit `gt` af; test de benodigde combinatie met eigen grensgevallen.

## Vervolgstappen

Verbind succes met controle, onwaar met standaardverwerking en fout met gegevenscorrectie. Het [volledige voorbeeld](advanced-workflow-case-study.md) bevat configuratie, vervolgkaarten en echte testresultaten. Het [uitvoeringsmodel](workflow-execution-model.md) beschrijft opslaan en activeren; de [diagnose](workflow-troubleshooting.md) helpt afwijkende resultaten onderzoeken.

## WF-05: Oefening en acceptatie

Beschrijf Run Workflow en een PO-kaart met dezelfde opbouw: parameters, onderzochte standaardwaarden, paden, effecten en versies. Controleer inactief doel, ontbrekende gegevens en procentbasis.

[Leerpad](workflow-learning-path.md)
