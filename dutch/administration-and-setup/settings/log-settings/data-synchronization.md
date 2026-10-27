# Gegevenssynchronisatie controleren

Gebruik dit overzicht wanneer een leverancier, inkooporder of ander stamgegeven ontbreekt. Het toont de geregistreerde synchronisatietijd per gegevenstype in de huidige organisatie, niet de inhoud van elk geïmporteerd record.

## Stappen

1. Controleer organisatie, relevante suborganisatie en ERP-bronbedrijf.
2. Open **Instellingen → Activiteitenlogboek → Gegevenssynchronisatie**. In oudere indelingen staat dit onder loginstellingen.
3. Zoek het type onder **Data Type** en lees **Last Synchronization Time** met uw datumindeling. Nieuwste updates staan bovenaan.
4. Vergelijk de tijd met de verwachte bronwijziging. Een recente leveranciersupdate bewijst geen actuele inkooporders.
5. Zoek de ontbrekende identificatie in stamgegevens of inkooporders. Vergelijk bedrijf, leverancier-/ordernummer en regelidentificaties met de bron.
6. Onderzoek importkanaal en logboeken: bronbericht, doelorganisatie, mapping en antwoord. Herstel de oorzaak in de integratie; dit overzicht heeft geen start- of herhaalknop.
7. Vernieuw na de gecorrigeerde update het overzicht en open de betreffende lookup of het document opnieuw. Controleer tijd én werkelijke waarden.

## Betekenis van het resultaat

| Waarneming | Volgende controle |
| --- | --- |
| Geen regels | Organisatie, importconfiguratie en geregistreerde synchronisaties. Leeg betekent niet geslaagd. |
| Eén oud gegevenstype | Volg die gegevensstroom onafhankelijk van andere regels. |
| Waarschuwing voor oude gegevens | De huidige waarschuwing kan verschijnen zonder regels of wanneer alle updates ouder zijn dan twee weken. Uw proces kan veel actuelere gegevens vereisen. |
| Recente tijd, ontbrekend record | Bronomvang, identificaties, berichtinhoud, mapping en antwoord. De tijd bewijst geen volledigheid. |

Bewaar voor ondersteuning omgeving, organisatie, type, identificatie, verwachte wijzigingstijd en exacte fout of trace-ID met relevante geanonimiseerde bewijzen.

Zie [Stamgegevens importeren](../../../infor-integration-and-configuration/importing-customer-master-data/README.md), [Activiteitenlogboek](README.md) en [Stamgegevens opzoeken](../document-processing/master-data-lookup.md).
