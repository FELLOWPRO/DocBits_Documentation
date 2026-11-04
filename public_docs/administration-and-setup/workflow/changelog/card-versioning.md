# Versiesysteem voor Kaarten - Update Oktober 2025

**Document:** Overzicht Workflow Kaartversies
**Laatst Bijgewerkt:** 23 oktober 2025
**Status:** Voltooid

---

## Overzicht

De DocBits Workflow Engine gebruikt **op gehele getallen gebaseerde versiebeheer** om de evolutie van kaarten te beheren en tegelijkertijd achterwaartse compatibiliteit te behouden. Dit document biedt een overzicht van het versiesysteem.

---

## Wat is Kaartversiebeheer?

### Concept
Elke workflowkaart kan meerdere versies hebben, waardoor het systeem het volgende kan doen:
- Nieuwe functies toevoegen zonder bestaande workflows te verbreken
- Verouderde functionaliteit ondersteunen terwijl deze wordt uitgefaseerd
- Kaartmogelijkheden in de loop van de tijd laten evolueren
- Achterwaartse compatibiliteit behouden

### Versiestructuur
- **Formaat:** Gehele getallen (1, 2, 3, 4, 5...)
- **Identificatie:** Samengestelde sleutel van (card_type, card_version)
- **Status:** Elke versie heeft markeringen voor verouderd/ingeschakeld

### Voorbeeld
De `tasks_create` kaart is geëvolueerd door 4 versies:
- **v1:** Originele taakcreatie (verouderd)
- **v2:** Toegevoegde vertaalondersteuning (verouderd)
- **v3:** Experimentele beslissingsboomondersteuning (verouderd)
- **v4:** Ondersteuning voor generieke werkitemtypen (momenteel actief)

---

## Belangrijkste Statistieken

### Overzicht Versiebeheer
| Metriek | Waarde |
|--------|-------|
| **Kaarten met Meerdere Versies** | 30+ |
| **Totaal Aantal Versierecords** | 90+ |
| **Versies per Kaart (gemiddeld)** | 3 |
| **Maximale Versies** | 5 (CONDITION_DOC_TO_PO_UNIT_PRICE) |
| **Verouderde Versies** | 9 |
| **Volledig Uitgeschakelde Kaarten** | 2 |

### Versieverdeling
- **2 Versies:** 14 kaarten (eenvoudigere evolutie)
- **3 Versies:** 11 kaarten (gematigde evolutie)
- **4 Versies:** 4 kaarten (aanzienlijke evolutie)
- **5 Versies:** 1 kaart (meest geëvolueerd: CONDITION_DOC_TO_PO_UNIT_PRICE)

---

## Veelvoorkomende Versiepatronen

### Patroon 1: Adoptie van Vertaalsleutels (v1 → v2)

**Betrokken:** 15+ kaarten

**Wijziging:**
```
v1: Platte tekst: "Call Api: [param] with method: [param]"
v2: Met i18n: "trnsl_%call_api trnsl_be_% Call Api: [param]..."
```

**Doel:** Meertalige ondersteuning inschakelen

**Kaarten:** CALL_API, RUN_WORKFLOW, APPROVE, REJECT, CALC_COLUMNS, en meer

**Migratie:** Veilig - geen functionele wijzigingen

---

### Patroon 2: Integratie van Beslissingsboom (v2 → v3)

**Betrokken:** 5 kaarten

**Wijziging:** Toevoeging van parameter voor beslissingsboom

```
v2: Maak een nieuwe Taak met titel: [param], beschrijving: [param]...
v3: (zelfde als v2) + "Gebruik beslissingsboom, indien beschikbaar: [param]"
```

**Doel:** Resultaten van beslissingstabellen ondersteunen

**Kaarten:**
- tasks_create (v3 verouderd)
- ACTION_TASK_FOR_GROUP (v3 verouderd)
- DOC_USER_ASSIGN (v3 verouderd)
- DOC_GROUP_ASSIGN (v3 verouderd)
- ACTION_DECISION_TREE_CREATE_TASKS

**Status:** Verouderd - beslissingsboomaanpak was experimenteel

---

### Patroon 3: Evolutie van Generiek Type (v3 → v4)

**Betrokken:** 4 kaarten

**Wijziging:** "Taak" wordt flexibel werkitemtype

```
v3: Maak een nieuwe Taak met de titel: [param]
v4: Maak een nieuw [param] met de titel: [param]
```

**Doel:** Taken, Tickets, Problemen en andere werkitemtypen ondersteunen

**Kaarten:**
- tasks_create (v4 huidig)
- ACTION_TASK_FOR_GROUP (v4 huidig)
- ACTION_ASSIGN_TASK_TO_PROCUREMENT_GROUP (v3 huidig)
- ACTION_ASSIGN_TASK_TO_USER_FROM_FIELD_WITH_FALLBACK (v3 huidig)

**Huidige Status:** Actief en aanbevolen

---

### Patroon 4: Tolerantieparameters (PO Kaarten)

**Betrokken:** 6 PO-vergelijkingskaarten

**Wijziging:** Toevoeging van tolerantie/afwijking ondersteuning

```
v2: Documentwaarde [operator] Inkooporderwaarde
v3+: Documentwaarde [operator] PO-waarde met tolerantie [bedrag] [eenheid]
```

**Doel:** Acceptabele afwijking in matching toestaan (bijv. 2% prijsverschil OK)

**Belangrijkste Kaarten:**
- CONDITION_DOC_TO_PO_UNIT_PRICE (geëvolueerd naar v5 met tolerantie)
- CONDITION_DATES_OPERATOR_OC_LINE_ITEMS (v2 → v3)
- CONDITION_LESS_THAN_TOLERANCE_AS_VALUE_OF_ORDERED_QUANTITY

**Voordeel:** Realistischere matchingscriteria

---

### Patroon 5: Vergelijkingsmodusparameters

**Betrokken:** 3 PO-vergelijkingskaarten

**Wijziging:** Ondersteuning voor verschillende vergelijkingsalgoritmen

```
v3: Standaard vergelijkingslogica
v4: Zelfde logica + "Vergelijk als [param]" parameter
```

**Doel:** Flexibele vergelijkingsmethoden

**Kaarten:**
- COMBINED_PRICE_OF_QUANTITY_DIFFERENCE_OPERATOR_VALUE (v2-4)
- CONDITION_OC_TO_PO_ITEMS (v3-4)
- CONDITION_LESS_THAN_TOLERANCE_AS_VALUE_OF_ORDERED_QUANTITY (v3-4)

---

### Patroon 6: Workflow Triggers

**Betrokken:** Alleen STAUS_CHANGE

**Wijziging:** Automatisch workflows triggeren bij statuswijziging

```
v2: Wijzig Status naar [param]
v3: Wijzig Status naar [param], trigger Workflows [param]
```

**Doel:** Statuswijzigingen doorgeven over workflows heen

---

## Meest Geëvolueerde Kaarten

### 1. CONDITION_DOC_TO_PO_UNIT_PRICE (5 versies)

**Evolutiepad:** v2 → v3 → v4 → v5

- **v2:** Basis eenheidsprijsvergelijking
- **v3:** Zelfde vertaalsleutel (v2)
- **v4:** Parameter voor vergelijkingsmodus toegevoegd
- **v5:** Parameter voor tolerantiedrempel toegevoegd

**Huidig:** v5 (met tolerantieondersteuning)

---

### 2. CONDITION_OC_TO_PO_ITEMS (4 versies)

**Evolutiepad:** v1 → v2 → v3 → v4

- **v1:** Basis item matching (verouderd)
- **v2:** Parameter voor vergelijkingsmethode toegevoegd
- **v3:** Verbeterd met vertaalsleutels
- **v4:** Parameter voor vergelijkingsmodus toegevoegd

**Huidig:** v4

**Vermijden:** v1 (verouderd)

---

### 3. tasks_create (4 versies)

**Evolutiepad:** v1 → v2 → v3 → v4

- **v1:** Originele implementatie (verouderd)
- **v2:** Toegevoegde vertaalondersteuning (verouderd)
- **v3:** Toegevoegde beslissingsboom (verouderd)
- **v4:** Generieke werkitemtypen (huidig)

**Huidig:** v4 (aanbevolen)

**Tijdlijn:**
```
v1 → verouderd (oud)
  → v2 → verouderd (vertaling toegevoegd)
    → v3 → verouderd (beslissingsboom experiment)
      → v4 → HUIDIG & ACTIEF
```

---

## Verouderingsstatus

### Volledig Verouderde Versies (Niet Gebruiken)

| Kaart | Versie | Reden | Alternatief |
|------|---------|--------|-------------|
| tasks_create | v1 | Zeer oud | Gebruik v4 |
| tasks_create | v3 | Beslissingsboom verouderd | Gebruik v4 |
| ACTION_TASK_FOR_GROUP | v3 | Beslissingsboom verouderd | Gebruik v4 |
| DOC_USER_ASSIGN | v3 | Beslissingsboom verouderd | Gebruik v2 |
| DOC_GROUP_ASSIGN | v3 | Beslissingsboom verouderd | Gebruik v2 |
| CONDITION_DOC_TYPE_IS_ISNOT | v1 | Zeer oud | Gebruik v2 |
| CONDITION_OC_TO_PO_ITEMS | v1 | Zeer oud | Gebruik v4 |
| ACTION_RUN_DOCOPERATOR_SCRIPT | v4 | Functies teruggedraaid | Gebruik v3 |

### Volledig Uitgeschakelde Kaarten (Niet Te Gebruiken)

| Kaart | Versies | Opmerkingen |
|------|----------|-------|
| DOC_SUBORG_CHANGE | v1, v2 | Niet-ondersteunde functionaliteit |
| RUN_SCRIPT | v2, v3 | Vervangen door ACTION_RUN_DOCOPERATOR_SCRIPT |

---

## Versieaanbevelingen

### Per Gebruiksscenario

**Nieuwe Workflow Creatie:**
- Gebruik altijd het **hoogste ingeschakelde versienummer**
- Biedt de nieuwste functies en verbeteringen
- Ondersteund en gedocumenteerd

**Bestaand Workflow Onderhoud:**
- Blijf de huidige versie gebruiken als deze werkt
- Plan migratie wanneer haalbaar
- Geen dringende noodzaak om te upgraden

**Migratie van Oude Workflows:**
- Identificeer de versie die momenteel in gebruik is
- Plan upgradepad
- Test grondig vóór implementatie

---

## Hoe Versies Werken

### Versieselectie
Bij het maken van een workflow selecteert u welke versie van een kaart u wilt gebruiken. Voorbeeld:
- Gebruik `tasks_create v4` voor nieuwe taakcreatie (aanbevolen)
- Gebruik `tasks_create v2` als oude systemen dit vereisen (ouder maar werkt)
- Gebruik NIET `tasks_create v1` (verouderd)

### Achterwaartse Compatibiliteit
- Nieuwere versies breken oudere workflows niet
- Oude workflows blijven werken met hun originele versie
- Kan workflows geleidelijk upgraden

### Technische Implementatie
Versies worden beheerd op databaseniveau:
```
card_templates tabel (PostgreSQL)
- card_type: Identificeert de kaart (bijv. "tasks_create")
- card_version: Versienummer (bijv. 2, 3, 4)
- deprecated: Booleaanse vlag
- enabled: Booleaanse vlag
- text: Kaartbeschrijving/parameters
```

---

## Voor Documentatiedoeleinden

### Versie-informatie Begrijpen
Wanneer u "Kaart v3" in de documentatie ziet:
- Verwijst dit naar versie 3 van die specifieke kaart
- Controleer [Volledige Versiereferentie](../../docs/card_version.md) voor details
- Verifieer welke versie wordt aanbevolen

### Uw Versie Controleren
Om te weten welke versie u gebruikt:
1. Open de kaart in uw workflow
2. Controleer het weergegeven versienummer
3. Vergelijk met aanbevelingen in gidsen

### Tijdlijn Versie-evolutie
- **2024-2025:** Voortdurende evolutie
- **Oktober 2025:** Volledige versiedocumentatie
- **Toekomst:** Voortdurende verbeteringen

---

## Gerelateerde Documentatie

### Uitgebreide Referentie
→ [Volledige Kaartversie Referentie](../../docs/card_version.md)

Omvat:
- Alle 30+ kaarten met versies
- Gedetailleerde tekstevolutie voor elk
- Specifieke parameterwijzigingen
- SQL-query's voor versie-lookup

### Kaartspecifieke Gidsen
→ [Workflow Gidsen](../)

Documentatie voor elke kaart met versieaanbevelingen

### Details Versiegeschiedenis
Elke gids bevat versie-informatie en migratienotities

---

## Snelle Referentie

### Kaarten met de Meeste Versies
1. CONDITION_DOC_TO_PO_UNIT_PRICE - 5 versies
2. CONDITION_OC_TO_PO_ITEMS - 4 versies
3. tasks_create - 4 versies
4. COMBINED_PRICE_OF_QUANTITY_DIFFERENCE_OPERATOR_VALUE - 3 versies
5. CONDITION_LESS_THAN_TOLERANCE_AS_VALUE_OF_ORDERED_QUANTITY - 4 versies

### Meest Voorkomend Evolutiepatroon
**Adoptie van Vertaalsleutels (v1 → v2)** - 15+ kaarten

### Belangrijkste Wijziging
**Evolutie van Generiek Type (v3 → v4)** - Gewijzigd van "Taak" naar flexibel werkitemtype

### Volledig Uitgeschakeld
- DOC_SUBORG_CHANGE
- RUN_SCRIPT

---

## Veelgestelde Vragen

### V: Welke versie moet ik gebruiken?
A: Gebruik de **hoogste ingeschakelde versie** tenzij u een specifieke reden hebt om een oudere versie te gebruiken.

### V: Kan ik mijn workflow upgraden naar een nieuwere versie?
A: Ja, maar test grondig. Sommige versies hebben andere parametervereisten.

### V: Wat gebeurt er als ik een verouderde versie gebruik?
A: Het blijft werken, maar u krijgt geen nieuwe functies. Migratie aanbevolen.

### V: Kan ik een uitgeschakelde kaart gebruiken?
A: Nee, uitgeschakelde kaarten kunnen niet worden gebruikt. Gebruik in plaats daarvan het aanbevolen alternatief.

### V: Hoe weet ik of mijn kaart een upgrade nodig heeft?
A: Controleer de [Volledige Versiereferentie](../../docs/card_version.md) voor uw kaarttype en volg de aanbevelingen.

---

## Beste Praktijken

1. **Nieuwe Workflows:** Gebruik de laatste stabiele versie
2. **Updates:** Controleer periodiek op nieuwe versies
3. **Testen:** Test versie-upgrades eerst in sandbox
4. **Documentatie:** Raadpleeg kaartspecifieke gidsen voor versiedetails
5. **Migratie:** Plan upgrades incrementeel
6. **Ondersteuning:** Neem contact op met ondersteuning als er vragen zijn over versiecompatibiliteit

---

## Samenvattingstabel

| Kaarttype | Huidige Versie | Totaal Aantal Versies | Status | Opmerkingen |
|-----------|-----------------|----------------|--------|-------|
| tasks_create | 4 | 4 | Actief | Meest geëvolueerd; v3 verouderd |
| CONDITION_DOC_TO_PO_UNIT_PRICE | 5 | 4 | Actief | Hoogste aantal versies |
| CONDITION_OC_TO_PO_ITEMS | 4 | 4 | Actief | v1 verouderd |
| ACTION_TASK_FOR_GROUP | 4 | 3 | Actief | v3 verouderd |
| ACTION_RUN_DOCOPERATOR_SCRIPT | 3 | 3 | Actief | v4 verouderd/uitgeschakeld |
| De meeste kaarten | 2 | 2 | Actief | v1 → v2 patroon |

---

## Zie Ook

- 📖 [Volledige Kaartversie Referentie](../../docs/card_version.md)
- 🔗 [Workflow Gidsen](../)
- 📋 [Release Notes Oktober 2025](./2025-10-october.md)
- 🔄 [Workflow Koppelingsanalyse](../../WORKFLOW_LINKING_MAP.md)

---

**Laatst Bijgewerkt:** 23 oktober 2025
**Bron:** postgres-dev-docflow database
**Status:** Volledige Referentie
