# Cachebeheer

<figure><img src="../../.gitbook/assets/cache_management.png" alt="Cachebeheer"><figcaption><p>Pagina Cachebeheer</p></figcaption></figure>

Cachebeheer regelt het automatisch wissen van de cache voor vaak opgevraagde gegevens. Het inschakelen van caching verbetert de prestaties doordat herhaalde API-aanroepen worden verminderd.

## Cache wissen

Klik op de knop **Clear Cache** (rechtsboven) om alle gecachete gegevens direct handmatig ongeldig te maken.

## Cachetabel

| Kolom | Beschrijving |
|--------|-------------|
| **Object** | Het type gecachete gegevens (bijv. Receive Delivery Cache, Purchase Order Cache). |
| **Status** | Schakelaar om caching voor dit object in of uit te schakelen. |
| **TTL** | Time to Live in minuten: hoe lang gecachete gegevens geldig blijven voordat ze automatisch worden vernieuwd. Stel in op `0` om het automatisch verlopen uit te schakelen. |

## Beschikbare caches

| Cache | Beschrijving |
|-------|-------------|
| **Receive Delivery Cache** | Cachet ontvangstgegevens van leveringen die worden gebruikt tijdens PO-matching. |
| **Purchase Order Cache** | Cachet inkoopordergegevens voor sneller opzoeken tijdens de documentverwerking. |
| **Task and Notification Cache** | Cachet taakaantallen en notificatiegegevens die in het dashboard worden getoond. |
