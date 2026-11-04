# Infor OS z integracją API DocBits



{% embed url="https://youtu.be/0aeSDWi9cV8" %}



## Import API DocBits do Infor OS — użyj specyfikacji Swagger 2.0

Gdy łączysz Infor OS z API DocBits (na przykład podczas tworzenia własnej aplikacji lub przepływu API w Infor OS), Infor importuje specyfikację API DocBits. **W przypadku Infor OS użyj specyfikacji Swagger 2.0, a nie OpenAPI 3.0.**

DocBits publikuje swoją specyfikację API w dwóch dialektach:

| Specyfikacja | Ścieżka | Do czego jej użyć |
| --- | --- | --- |
| OpenAPI 3.0 / 3.1 | `/openapi.json` | Standardowi klienci API, generowanie SDK, zwykła dokumentacja API |
| **Swagger 2.0** | `/openapi-swagger2.json` | **Infor OS** (oraz każde inne narzędzie używające starszego swagger-ui) |

{% hint style="warning" %}
**Dlaczego Swagger 2.0 dla Infor?** Infor OS używa starszej wersji swagger-ui, która nie potrafi zbudować żądania przesłania pliku na podstawie nowoczesnej reprezentacji OpenAPI 3.0 (`requestBody` z `format: binary`). Wysyła przesyłanie **bez granicy multipart (boundary)**, a API odrzuca je z komunikatem:

`400 — Missing boundary in multipart`

Specyfikacja Swagger 2.0 deklaruje przesyłanie plików jako `in: formData, type: file`, co swagger-ui w Infor buduje poprawnie (wraz z granicą). Te same endpointy, te same dane — różni się tylko dialekt specyfikacji.
{% endhint %}

### Jak uzyskać adres URL Swagger 2.0

1. Otwórz dokumentację API DocBits w przeglądarce (np. `https://api.docbits.com/docs`).
2. U góry strony otwórz **listę rozwijaną specyfikacji** i wybierz **Swagger 2.0 (Infor OS)**.
3. Skopiuj adres URL wyświetlony dla tej specyfikacji — to bazowy adres URL API DocBits, po którym następuje `/openapi-swagger2.json`.

Użyj tego adresu URL wszędzie tam, gdzie Infor OS prosi o specyfikację API / Swagger. Skopiowanie go z listy rozwijanej gwarantuje właściwy host dla Twojego regionu i środowiska.

{% hint style="info" %}
Wszystko inne w integracji — uwierzytelnianie (klucz API / token), endpointy i ładunki danych — pozostaje bez zmian. Różni się tylko dialekt specyfikacji importowany do Infor.
{% endhint %}
