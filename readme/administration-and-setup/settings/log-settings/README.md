# Activiteitenlogboek

<figure><img src="../../../.gitbook/assets/activity_logging.png" alt="Activiteitenlogboek"><figcaption><p>Pagina Activity Logging</p></figcaption></figure>

Activity Logging biedt een realtime overzicht van systeemgebeurtenissen in alle DocBits-services. Gebruik het om verwerkingsactiviteit te bewaken, fouten op te sporen en systeemgedrag te auditen.

## Analytics-banner

Bovenaan de pagina verwijst een banner naar het **Analytics Dashboard** voor grafieken, metrics en realtime monitoring.

## Filters

| Filter | Beschrijving |
|--------|-------------|
| **Time Range** | Selecteer een tijdvenster (bijv. Today, Last 7 Days, Last 30 Days). |
| **Severity** | Schakel ernstniveaus in of uit om ze op te nemen of uit te sluiten: **Debug**, **Info**, **Warning**, **Error**. Elke chip toont het huidige aantal. |
| **Service** | Filter logboeken op service (bijv. api, auth, api-service). |
| **Search logs** | Vrije tekst zoeken in logberichten. |

## Logtabel

| Kolom | Beschrijving |
|--------|-------------|
| **Timestamp** | Datum en tijdstip waarop de gebeurtenis plaatsvond. Sorteerbaar. |
| **Severity** | Kleurgecodeerde badge: Info (blauw), Warning (geel), Error (rood), Debug (grijs). |
| **Component** | De service of module die het logbericht heeft gegenereerd (bijv. api, auth, api-service). |
| **Message** | Het volledige logbericht met details van de gebeurtenis. |

De resultaten zijn gepagineerd — gebruik de bedieningselementen onderaan om door de pagina's te navigeren.

## Acties in de voettekst

| Actie | Beschrijving |
|--------|-------------|
| **Auto-refresh** | Schakelaar om de logweergave met regelmatige tussenpozen automatisch te vernieuwen. |
| **Refresh Now** | Ververs de loggegevens handmatig. |
| **Export JSON** | Exporteer de huidige gefilterde logboeken als JSON-bestand. |
| **Download Logs** | Download de volledige loggegevens. |
