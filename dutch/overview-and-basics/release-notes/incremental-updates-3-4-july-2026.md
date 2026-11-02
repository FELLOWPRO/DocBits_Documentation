# DocBits Release-opmerkingen — 3–4 juli 2026

_Een overzicht van wat er voor u verandert met deze DocBits-release. Elke service
hieronder toont de versie die nu in productie draait, gevolgd door wat er nieuw of
opgelost is — in gewone taal, zonder ticketnummers of technisch jargon. Services
die niet zijn vermeld, hadden in dit tijdvenster geen wijzigingen die zichtbaar
zijn voor klanten._

---

## Hoogtepunten

- **Zero-downtime deployments, over de hele linie.** API, Auto Accounting,
  Docflow, Extraction, OCR en PO Match sluiten nu netjes af wanneer een
  nieuwe release wordt uitgerold. Voorheen kon een verzoek dat tijdens een
  deployment nog onderweg was, worden afgebroken; nu wordt elk lopend
  verzoek afgerond voordat de oude versie stopt, waardoor releases niet
  langer voor korte haperingen bij gebruikers zorgen.
- **Verbeteringen in e-invoice-export.** Het exporteren van een document naar
  meerdere exportconfiguraties tegelijk is nu betrouwbaarder — controles op dubbele
  exports draaien nu één keer per batch in plaats van per item, en een nieuw
  exporteindpunt voorkomt dat de exportstatus knippert wanneer meerdere exports
  tegelijk worden gestart. XRechnung/ZUGFeRD-documenten krijgen ook consistentere
  veldmapping.
- **Stabielere documentverwerking.** Een crash opgelost die een volledig
  OCR-document kon laten uitvallen wanneer één pagina mislukte, de
  Purchase-Order-leveringssynchronisatie opgelost die alleen de eerste 100 records
  ophaalde, en verschillende services steviger gemaakt tegen korte onderbrekingen
  van de databaseverbinding.
- **E-mailbijlagen hersteld.** Een geval opgelost waarbij e-mailbijlagen beschadigd
  konden aankomen of bytes konden missen tijdens inkomende import.
- **Betrouwbaarheid van workflows.** Workflows die vastliepen door een lock die niet
  correct werd vrijgegeven zijn opgelost, en de herplanningslogica is opgelost zodat
  overgeslagen workflowstappen correct worden afgehandeld en gelogd.
- **Nieuw: Ideas Service.** Een nieuwe backendservice (Ideas, v0.3.0) is toegevoegd
  aan de productieomgeving.

---

## API Service — live: `12.52.4`

- **OCR-betrouwbaarheid:** een crash op één pagina laat het hele document niet
  langer mislukken.
- **Export:** controles op dubbele exports draaien nu één keer per batch in plaats
  van één keer per item; een nieuw exporteindpunt voorkomt dat de exportstatus
  knippert wanneer meerdere exports tegelijk lopen; XRechnung/ZUGFeRD-documenten
  krijgen consistentere canonieke veldmapping.
- **Purchase Orders:** leveringssynchronisatie opgelost die alleen de eerste 100
  records per order ophaalde.
- **Activiteitenlogboeken:** de knop "Volgende" pagina sprong naar een niet
  gerelateerd tijdvenster — opgelost.
- **Master Data Lookup:** een serverfout (HTTP 500) opgelost.
- **Zoekindexering:** een leveringsbewijs-markering en herhaalpoging toegevoegd
  zodat documenten betrouwbaar in de wachtrij voor volledige tekstzoekfunctie worden
  geplaatst.
- **Zero-downtime deployments:** lopende verzoeken worden nu afgerond voordat
  een release de service herstart.
- Algemene stabiliteitsfixes voor verschillende terugkerende achtergrondfouten.

## Auth Service — live: `1.68.7`

- Alleen interne betrouwbaarheid en onderhoud in dit tijdvenster.

## Auto Accounting — live: `1.18.8`

- **Zero-downtime deployments:** lopende verzoeken worden nu afgerond voordat
  een release de service herstart.

## Barcode Service — live: `1.15.8`

- Alleen een interne deploymentconfiguratiefix in dit tijdvenster.

## Docflow Service — live: `2.5.3`

- **Nieuwe exportoptie** om een document naar meerdere exportconfiguraties tegelijk
  te versturen.
- **Workflows die vastliepen opgelost** door een lock die niet correct werd
  vrijgegeven, ongeacht de status.
- **Workflowherplanning opgelost** zodat overgeslagen stappen correct worden
  afgehandeld en gelogd in plaats van stilzwijgend te worden weggelaten.
- **Snellere opstart:** databases worden nu op de achtergrond vooraf opgewarmd.
- Veerkrachtiger tegen korte onderbrekingen van de databaseverbinding.
- Verbeterde parsing van datumvelden voor workflowkaarten.
- **Zero-downtime deployments:** lopende verzoeken worden nu afgerond voordat
  een release de service herstart.

## Email Service — live: `1.37.9`

- **Inkomende bijlagen opgelost** die beschadigd konden aankomen of bytes konden
  missen.
- **Duidelijkere foutmeldingen** wanneer een postbusmap niet kan worden opgehaald,
  in plaats van een generieke fout.

## Extraction Service — live: `1.49.6`

- **Crashes opgelost** bij documenten met een niet-herkend documenttype en bij
  tabellen met een ongebruikelijke/misvormde structuur.
- Veerkrachtiger tegen korte onderbrekingen van de databaseverbinding halverwege
  een query.
- **Zero-downtime deployments:** lopende verzoeken worden nu afgerond voordat
  een release de service herstart.

## FTP Service — live: `1.30.3`

- Alleen een interne framework-upgrade in dit tijdvenster.

## Fulltext Service — live: `1.36.3`

- **Zoekindexering:** een periodieke controle herstelt nu alle documenten die voor
  een organisatie niet in de zoekindex terechtkwamen.
- **ERP-synchronisatie:** een vastgelopen lock opgelost die de ERP-synchronisatie
  kon blokkeren na een mislukte herhaalpoging.

## OCR Service — live: `1.7.8`

- **OCR-authenticatie opgelost** zodat organisatie-API-sleutels weer correct
  werken.
- **Zero-downtime deployments:** lopende verzoeken worden nu afgerond voordat
  een release de service herstart.

## Operator Service — live: `1.39.7`

- Alleen interne fixes voor deploymentbetrouwbaarheid in dit tijdvenster.

## PO Match Service — live: `1.56.0`

- **Een crash opgelost** bij het sorteren van PO Match-hoeveelheden met lege
  waarden.
- **Zero-downtime deployments:** lopende verzoeken worden nu afgerond voordat
  een release de service herstart.

## Web App — live: `10.36.9`

- **Een fout opgelost** bij het terugkeren naar Veldvalidatie vanuit een ander
  scherm.
- **De knop "Scripts" opgelost** die naar een 404-pagina leidde.
- **Activiteitenlogboeken:** een onjuiste weergave "Pagina 2 van 1" opgelost en het
  WARN-ernstfilter dat niets matchte opgelost.

---

## Geen wijzigingen zichtbaar voor klanten in dit tijdvenster

Auth Service, Barcode Service, FTP Service, Operator Service en Docnet Service
(`1.54.6`, ongewijzigd) kregen alleen intern of deploymentconfiguratie-onderhoud.

<!-- Generated by the docbits-changelog skill (version-boundary mode: exact
     git ranges between the ALT and NEU version-bump commits supplied by the
     user, per service). Window ~2026-07-01 → 2026-07-04. -->
