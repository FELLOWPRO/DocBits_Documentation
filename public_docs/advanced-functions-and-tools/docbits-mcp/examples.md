# Voorbeelden

Zodra DocBits MCP is verbonden (zie [Installatie en configuratie](setup-and-configuration.md)), praat u met uw assistent in gewone taal — die kiest zelf de juiste DocBits-tools. Hieronder staan realistische dingen die klanten doen, met het soort prompt dat u zou typen en de tools die de assistent op de achtergrond gebruikt.

{% hint style="info" %}
Deze werken hetzelfde in Claude Code, Gemini CLI en Codex — de prompts zijn natuurlijke taal, geen commando's.
{% endhint %}

## De werkwachtrij beoordelen

> *"Hoeveel documenten wachten op validatie, en van welke typen zijn ze?"*

Gebruikt `get_pending_documents_count`, `get_pending_tasks_detail`, `get_top_document_types`. De assistent vat de achterstand samen en kan op elk document inzoomen.

> *"Toon me de facturen die vandaag fouten gaven en leg uit waarom."*

Gebruikt `search_documents` / `query_document_dashboard` + `get_document_logs` om documenten met fouten te vinden en de storing uit de logs toe te lichten.

## Een document zoeken en inspecteren

> *"Open factuur INV-2026-00231 en toon de geëxtraheerde velden en de factuurregels."*

Gebruikt `get_document_by_name`, `get_extracted_fields`, `get_extracted_tables`. De assistent geeft de headergegevens en de tabel terug en kan met `get_page_image` het paginabeeld ophalen als u de bron wilt zien.

> *"Zoek alle documenten van leverancier 'ACME GmbH' van vorige maand boven € 10.000."*

Gebruikt `search_documents` / `query_document_dashboard` met filters per veld.

## Corrigeren en goedkeuren

> *"Zet bij document 84213 het inkoopordernummer op 4500098123 en de vervaldatum op 2026-07-15, en valideer het daarna."*

Gebruikt `update_document_fields` en daarna `validate_document`. De assistent meldt eventuele validatiefouten zodat u ze kunt oplossen.

> *"Valideer en exporteer document 84213 naar het ERP, maar toon me eerst de exportvoorvertoning."*

Gebruikt `get_export_preview`, en daarna `validate_and_export` zodra u bevestigt.

## Een tabelextractie herstellen

> *"In de tabel met artikelregels van deze pakbon ontbreken twee rijen. Extraheer hem opnieuw met AI, verberg de kolom *Charges* en onthoud dat voor deze leverancier."*

Gebruikt `extract_table_ai` om de AI-tabel op het document opnieuw uit te voeren, `apply_ai_table_formatting` om de kolom te verbergen en `save_table_training_rules` om het resultaat voor de leverancier op te slaan; de volgende pakbon van die leverancier wordt op dezelfde manier geëxtraheerd. `get_extracted_tables` toont de uiteindelijke tabel. Nuttig voor documenten waarbij de regelgebaseerde extractie rijen miste.

## Analyses en rapportage

> *"Geef me een managementsamenvatting voor deze maand: volumetrend, touchless-percentage en de top 5 documenttypen."*

Gebruikt `get_executive_summary`, `get_volume_trends`, `get_success_rates`, `get_top_document_types`. Ideaal voor een snelle update aan het management zonder het dashboard te openen.

## E-facturatie (eDocs)

> *"Welke formaten voor elektronische facturen zijn voor ons ingeschakeld, en wordt dit ZUGFeRD-bestand correct geëxtraheerd?"*

Gebruikt `list_electronic_document_types` + `test_electronic_document`, daarna `verify_electronic_documents` om de geëxtraheerde velden te bevestigen.

## Stamgegevens en verrijking van leveranciers

> *"Voeg een nieuwe leverancier (naam, btw-nummer, IBAN) toe aan de stamgegevens en voer daarna de leveranciersopzoeking opnieuw uit op document 84500."*

Gebruikt `upsert_vendor_master_data` + `trigger_supplier_lookup`.

## Configuratiewijzigingen

> *"Schakel QR-code-extractie in voor onze organisatie en bevestig dat de voorkeur is ingesteld."*

Gebruikt `set_preference` (dat de cache automatisch wist) + `get_preference` ter bevestiging.

> *"Toon onze documenttypen en de veldinstellingen voor 'Invoice'."*

Gebruikt `list_document_types` + `get_field_settings`.

## Status en diagnose

> *"Zijn de DocBits API en de verwerkingsworker op dit moment gezond? Als wie ben ik verbonden?"*

Gebruikt `check_api_health`, `check_celery_health`, `get_current_user`.

---

## Tips

- **Wees specifiek over het document** — een ID of exacte bestandsnaam is het snelst; anders zoekt de assistent eerst.
- **Vraag om een voorvertoning vóór het exporteren** — met `get_export_preview` bevestigt u de ERP-payload voordat `validate_and_export` die verzendt.
- **Rechten zijn van toepassing** — de assistent kan alleen doen wat uw DocBits-gebruiker of API-sleutel mag. Goedkeuringen en exports respecteren uw rol en ACL's.
- **Voorzichtigheid in productie** — de MCP werkt op echte gegevens. Geef in klant-/productieomgevingen de voorkeur aan lees- en voorvertoningsacties en bevestig voordat u goedkeurt, exporteert of verwijdert.
