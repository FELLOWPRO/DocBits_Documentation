# Infor OS mit DocBits-API-Integration



{% embed url="https://youtu.be/0aeSDWi9cV8" %}



## Die DocBits-API in Infor OS importieren – verwenden Sie die Swagger-2.0-Spezifikation

Wenn Sie Infor OS mit der DocBits-API verbinden (zum Beispiel beim Erstellen einer benutzerdefinierten Anwendung oder eines API-Flows in Infor OS), importiert Infor die API-Spezifikation von DocBits. **Verwenden Sie für Infor OS die Swagger-2.0-Spezifikation – nicht die OpenAPI-3.0-Spezifikation.**

DocBits veröffentlicht seine API-Spezifikation in zwei Dialekten:

| Spezifikation | Pfad | Verwendung |
| --- | --- | --- |
| OpenAPI 3.0 / 3.1 | `/openapi.json` | Standard-API-Clients, SDK-Generierung, die normale API-Dokumentation |
| **Swagger 2.0** | `/openapi-swagger2.json` | **Infor OS** (und jedes andere Tool, das ein älteres swagger-ui verwendet) |

{% hint style="warning" %}
**Warum Swagger 2.0 für Infor?** Infor OS verwendet eine ältere Version von swagger-ui, die aus der modernen OpenAPI-3.0-Darstellung (ein `requestBody` mit `format: binary`) keine Datei-Upload-Anfrage aufbauen kann. Sie sendet den Upload **ohne Multipart-Boundary**, und die API weist ihn ab mit:

`400 — Missing boundary in multipart`

Die Swagger-2.0-Spezifikation deklariert Datei-Uploads als `in: formData, type: file`, was das swagger-ui von Infor korrekt (mit Boundary) aufbaut. Dieselben Endpunkte, dieselben Daten – nur der Dialekt der Spezifikation unterscheidet sich.
{% endhint %}

### So erhalten Sie die Swagger-2.0-URL

1. Öffnen Sie die DocBits-API-Dokumentation in Ihrem Browser (z. B. `https://api.docbits.com/docs`).
2. Öffnen Sie oben auf der Seite das **Dropdown-Menü der Spezifikationen** und wählen Sie **Swagger 2.0 (Infor OS)**.
3. Kopieren Sie die für diese Spezifikation angezeigte URL – sie besteht aus Ihrer DocBits-API-Basis-URL gefolgt von `/openapi-swagger2.json`.

Verwenden Sie diese URL überall dort, wo Infor OS nach der API- bzw. Swagger-Spezifikation fragt. Wenn Sie sie aus dem Dropdown-Menü kopieren, ist der korrekte Host für Ihre Region und Umgebung gewährleistet.

{% hint style="info" %}
Alles Weitere an der Integration – Authentifizierung (API-Schlüssel / Token), Endpunkte und Payloads – bleibt unverändert. Nur der Dialekt der Spezifikation, den Sie in Infor importieren, unterscheidet sich.
{% endhint %}
