# Infor OS met DocBits API-integratie



{% embed url="https://youtu.be/0aeSDWi9cV8" %}



## De DocBits API importeren in Infor OS: gebruik de Swagger 2.0-specificatie

Wanneer u Infor OS koppelt aan de DocBits API (bijvoorbeeld bij het maken van een eigen applicatie of een API-flow in Infor OS), importeert Infor de API-specificatie van DocBits. **Gebruik voor Infor OS de Swagger 2.0-specificatie, niet de OpenAPI 3.0-specificatie.**

DocBits publiceert zijn API-specificatie in twee dialecten:

| Specificatie | Pad | Te gebruiken voor |
| --- | --- | --- |
| OpenAPI 3.0 / 3.1 | `/openapi.json` | Standaard API-clients, SDK-generatie, de gewone API-documentatie |
| **Swagger 2.0** | `/openapi-swagger2.json` | **Infor OS** (en elke andere tool die een oudere swagger-ui gebruikt) |

{% hint style="warning" %}
**Waarom Swagger 2.0 voor Infor?** Infor OS gebruikt een oudere versie van swagger-ui die uit de moderne OpenAPI 3.0-weergave (een `requestBody` met `format: binary`) geen bestandsuploadverzoek kan opbouwen. De upload wordt verstuurd **zonder multipart-boundary**, en de API weigert deze met:

`400 — Missing boundary in multipart`

De Swagger 2.0-specificatie declareert bestandsuploads als `in: formData, type: file`, wat de swagger-ui van Infor correct opbouwt (met een boundary). Dezelfde endpoints, dezelfde gegevens: alleen het specificatiedialect verschilt.
{% endhint %}

### Zo haalt u de Swagger 2.0-URL op

1. Open de DocBits API-documentatie in uw browser (bijv. `https://api.docbits.com/docs`).
2. Open bovenaan de pagina de **specificatie-keuzelijst** en selecteer **Swagger 2.0 (Infor OS)**.
3. Kopieer de URL die voor die specificatie wordt getoond. Dit is uw DocBits API-basis-URL gevolgd door `/openapi-swagger2.json`.

Gebruik die URL overal waar Infor OS om de API-/Swagger-specificatie vraagt. Door de URL uit de keuzelijst te kopiëren, weet u zeker dat de host klopt voor uw regio en omgeving.

{% hint style="info" %}
Al het andere aan de integratie (authenticatie met API key/token, endpoints en payloads) blijft ongewijzigd. Alleen het specificatiedialect dat u in Infor importeert, verschilt.
{% endhint %}
