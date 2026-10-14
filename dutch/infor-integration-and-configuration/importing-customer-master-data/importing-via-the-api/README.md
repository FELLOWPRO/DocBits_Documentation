---
description: Stamgegevens handmatig naar DocBits sturen via de API
---

# Importeren via de API

Stamgegevens bereiken DocBits normaal gesproken automatisch via uw ION-datastroom. De pagina's in deze sectie beschrijven hoe u dezelfde gegevens handmatig verstuurt via de testinterface van de API — handig wanneer u een record opnieuw wilt importeren, iets wilt laden dat nooit is aangekomen, of een nieuwe veldtoewijzing wilt uitproberen voordat u de automatische stroom inschakelt.

Elke pagina volgt dezelfde vijf stappen: de API-link voor uw omgeving openen, autoriseren met uw Org ID en API key, het formulier invullen, uitvoeren en controleren of de gegevens zijn aangekomen.

* [Leveranciers importeren (Supplier BOD)](supplier-bod.md)
* [Inkooporders importeren (Purchase Order BOD)](purchase-order-bod.md)
* [Goederenontvangsten importeren (Receive Delivery BOD)](receive-delivery-bod.md)
* [Stamgegevens importeren uit XML](master-data-xml.md)

## Wat u nodig hebt

* **Een API key** — zie [API Key Management](../../../administration-and-setup/settings/global-settings/integration/api-key-management.md).
* **Uw Org ID** — onder **Settings → Integration & SSO**, in de sectie **ID**.
* **De gegevens zelf**, als XML-bestand of als XML-inhoud die u kunt plakken.

{% hint style="warning" %}
Een import schrijft rechtstreeks in de stamgegevens van uw organisatie. Controleer naar welke omgeving, welke regio en welke organisatie u wijst voordat u uitvoert.
{% endhint %}
