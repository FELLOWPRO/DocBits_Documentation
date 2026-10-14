# Hotfixes 8 september 2026

> Purchase order matching: wat is er veranderd met de hotfixes die op 8 september 2026 zijn uitgerold. Het onderstaande gedrag is live op de ontwikkelomgeving en bereikt stage, sandbox en productie met de volgende upgrades.

## Purchase order matching

- **De match blijft behouden na opslaan.** Een purchase order match die een transformatieregel vroeger stilzwijgend liet vallen bij elke opslag (regels die de regelitems herbouwen) wordt nu behouden zolang de regel dezelfde regels produceert. Wanneer een regel daadwerkelijk de gematchte regels vervangt, registreert het document de regel en noemt het scherm deze.
- **Matching wordt opnieuw uitgevoerd bij opslaan.** Wanneer het purchase order nummer op het document verandert — of wanneer masterdata het invulde na verwerking en er nog geen matching run heeft gezocht — matcht de opslag het document direct. Een bestaande match wordt nooit overschreven door een opslag.
- **Het scherm geeft aan waarom er geen match is.** Het Purchase Order Matching scherm toont één zin boven het purchase order gebied: geen purchase order nummer, purchase order niet gevonden in het ERP, nog niet opgezocht, geladen maar niet verbonden, geen regel komt overeen, geen tabel, tabelkolommen niet gemapt, geen openstaande regels meer. Kandidaten die opzij zijn gezet worden vermeld met de reden (bijvoorbeeld een factuurnummer dat was ingelezen in de purchase order kolom).
- **Een gevallen match wordt nooit als opgeslagen gerapporteerd.** Als de server een match niet behoudt, herstelt het scherm deze, markeert het document als niet opgeslagen en rapporteert de afwijzing met de reden in plaats van "opgeslagen".
- **Matching geschiedenis toont de transformatieregels.** De matching geschiedenis van een document heeft nu een _Transformatierules_ stap vóór de eerste matchingfase, met een lijst van de regels die zijn uitgevoerd en of één van hen de match heeft laten vallen. Beheerders krijgen een link naar de regel.
- **PO eenheidsprijs uit het nettobedrag.** Met _Calculate PO unit price_ ingeschakeld, wordt de prijs nu eerst afgeleid van het **netto** bedrag van de purchase order regel en alleen van het totaal wanneer er geen netto bedrag is. Purchase orders van Infor bevatten belasting in het regel totaal; facturen met netto prijzen werden vroeger getoond als "unit price under-matched" met precies het belastingtarief. De berekende prijs wordt bij elke match vernieuwd, zodat bestaande documenten profiteren zonder de purchase order opnieuw te laden.
- **Factuurnummers worden niet langer verward met purchase order nummers.** Een kandidaat uit een regelitemkolom of een eerdere lookup die gelijk is aan het eigen factuurnummer van het document wordt opzij gezet.

## Documentatie

- Nieuwe pagina [Transformatierules](../../administration-and-setup/settings/global-settings/document-types/transformation-rules.md).
- [Purchase Order Matching Rules](../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-matching-rules.md) behandelt nu regeltypes, activatievoorwaarden, fallback regels, de standaard regelsset, tolerantie types en de effectieve kolommen.
- [Calculate PO unit price](../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/calculate-po-unit-price.md) beschrijft de netto-bedrag berekening.
- [Purchase Order Matching Screen](../../end-user-and-partner-section/end-user-section/purchase-order-matching/README.md) legt de "waarom is er geen match" berichten en de matching geschiedenis uit.