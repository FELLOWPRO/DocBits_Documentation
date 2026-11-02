# Infor OS con l'integrazione API di DocBits



{% embed url="https://youtu.be/0aeSDWi9cV8" %}



## Importare l'API di DocBits in Infor OS: utilizza la specifica Swagger 2.0

Quando colleghi Infor OS all'API di DocBits (ad esempio durante la creazione di un'applicazione personalizzata o di un flusso API in Infor OS), Infor importa la specifica API di DocBits. **Per Infor OS, utilizza la specifica Swagger 2.0, non quella OpenAPI 3.0.**

DocBits pubblica la propria specifica API in due dialetti:

| Specifica | Percorso | Da utilizzare per |
| --- | --- | --- |
| OpenAPI 3.0 / 3.1 | `/openapi.json` | Client API standard, generazione di SDK, la normale documentazione API |
| **Swagger 2.0** | `/openapi-swagger2.json` | **Infor OS** (e qualsiasi altro strumento che utilizzi un swagger-ui più datato) |

{% hint style="warning" %}
**Perché Swagger 2.0 per Infor?** Infor OS utilizza una versione più datata di swagger-ui che non è in grado di costruire una richiesta di caricamento file a partire dalla rappresentazione moderna OpenAPI 3.0 (un `requestBody` con `format: binary`). Invia il caricamento **senza un boundary multipart** e l'API lo rifiuta con:

`400 — Missing boundary in multipart`

La specifica Swagger 2.0 dichiara i caricamenti di file come `in: formData, type: file`, che il swagger-ui di Infor costruisce correttamente (con un boundary). Stessi endpoint, stessi dati: cambia solo il dialetto della specifica.
{% endhint %}

### Come ottenere l'URL Swagger 2.0

1. Apri la documentazione API di DocBits nel browser (ad es. `https://api.docbits.com/docs`).
2. In cima alla pagina, apri il **menu a discesa delle specifiche** e seleziona **Swagger 2.0 (Infor OS)**.
3. Copia l'URL mostrato per quella specifica: è l'URL di base dell'API DocBits seguito da `/openapi-swagger2.json`.

Utilizza quell'URL ovunque Infor OS richieda la specifica API / Swagger. Copiarlo dal menu a discesa garantisce l'host corretto per la tua regione e il tuo ambiente.

{% hint style="info" %}
Tutto il resto dell'integrazione (autenticazione con chiave API / token, endpoint e payload) rimane invariato. Cambia solo il dialetto della specifica che importi in Infor.
{% endhint %}
