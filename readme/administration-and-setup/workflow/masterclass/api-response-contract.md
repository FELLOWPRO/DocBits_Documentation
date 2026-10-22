---
description: "P1: API-Aufruf und Weiterverwendung der Antwort prüfen"
---

# P1: API-Aufruf und Weiterverwendung der Antwort prüfen

**Call API**, Version 2, ergänzt den konfigurierten Pfad um die DocBits-API-Basis und verwendet den aktuellen Organisationskontext. **Send HTTPS Request**, Version 2, verwendet eine externe URL und eigene Header. Ein vollständig fremder URL-Wert ist kein austauschbarer Call-API-Pfad. Beide Karten simulieren im Advanced-Test den Versand.

Die geprüfte HTTPS-Aktion protokolliert Status und Antworttext, stellt aber keinen frei benannten JSON-Antwortspeicher für Folgekarten bereit. Call API wertet den Antworttext über eine Bool-Konvertierung aus. HTTP 200, ein gültiger JSON-Body und eine fachlich erfolgreiche Folgeaktion sind daher getrennte Nachweise. Erfinden Sie keine Zugriffssyntax wie `api.response.cost_center`.

Für `{"cost_center":"4711"}` aus einem Fremdsystem vereinbaren Sie einen ausdrücklich unterstützten Rückschreibweg oder Callback in ein Dokumentfeld. Prüfen Sie das gespeicherte Feld und lesen Sie es im dafür vorgesehenen Folgelauf. Für direkten Antwortdatentransfer ist eine Karte oder Erweiterung mit dokumentiertem Ausgabevertrag erforderlich. JSON in der Kartenkonfiguration bestätigt außerdem nicht automatisch die tatsächlich gesendeten JSON-Bytes.

Verwenden Sie ein eigenes Testziel und prüfen Sie Methode, Header, tatsächlichen Body, Status und Antwortschema. Nehmen Sie 4xx, 5xx, Timeout, ungültiges JSON und doppelte Auslösung ab. Wiederholen Sie Schreibaufrufe erst, nachdem ein möglicher erster Empfang geprüft wurde. Die URL im Beispiel ist ein reservierter Platzhalter; sie wurde nicht als erreichbarer Dienst getestet.

## Karten und Beispielparameter

Die Werte zeigen einzelne Kartenparameter, keinen importierbaren Gesamtworkflow. YOUR_* muss durch eine eigene Testauswahl ersetzt werden. Die versteckte Aufrufer-ID verwaltet der Designer. Katalogstand: Dev, DocFlow 2.10.38, 21. Oktober 2026; verfügbare Versionen und Freigaben in Ihrer Organisation separat prüfen.

### `call_api` · v2

Identität: `6ca5e621-af72-4f55-aa2e-b3caa288722a`

| Parameter | Typ / Auswahl | Beispiel |
| --- | --- | --- |
| `params` | `params:str` | `"{}"` |
| `api_endpoint` | `api_endpoint:str` | `"YOUR_RELATIVE_API_PATH"` |
| `data` | `data:str` | `"{}"` |
| `method` | `put / post / delete / get` | `"get"` |

### `action_https_request` · v2

Identität: `18d06ca4-3aca-4e49-b75c-566ade2fcb10`

| Parameter | Typ / Auswahl | Beispiel |
| --- | --- | --- |
| `data` | `data` | `"{}"` |
| `params` | `params` | `"{}"` |
| `url` | `url:str` | `"https://training.example.invalid/status"` |
| `headers` | `headers:str` | `"{}"` |
| `method` | `put / post / delete / get` | `"get"` |

## Fachliche Prüffälle

| Fall | Eingabe / Aufbau | Erwartung |
| --- | --- | --- |
| API-01 | Advanced Test | simuliert; kein Zustellnachweis |
| API-02 | HTTPS: 4xx / 5xx | error |
| API-03 | timeout | Empfang vor Wiederholung prüfen |
| API-04 | {"cost_center":"4711"} | kein automatisches api.response.cost_center |
| API-05 | POST × 2 | Doppelverarbeitung beim Ziel prüfen |

## Prüfstand und Aussagegrenzen

Parameter und Verhalten wurden gegen den Dev-Katalog und den geprüften Quellstand abgeglichen. Die fachlichen Prüffälle sind eine Abnahmeanleitung. Persönliche Freigaben, reale Datenänderungen und Zustellungen wurden für dieses Kapitel nicht durchgeführt.

[Weiter im Lernweg](../workflow-learning-path.md) · [Übungspaket](../workflow-training-kit.md)
