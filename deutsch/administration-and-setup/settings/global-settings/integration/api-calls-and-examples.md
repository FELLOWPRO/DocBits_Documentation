# API-Aufrufe und Beispiele

Mit einer API-Anfrage kann ein anderes Programm Informationen in DocBits lesen oder aktualisieren. Beginnen Sie mit einer rein lesenden Anfrage, damit Sie die Verbindung prüfen können, ohne Dokumente zu verändern.

## Bevor Sie eine Anfrage senden

1. Bitten Sie einen Organisationsadministrator um Zugriff und [erstellen Sie einen API-Schlüssel](api-key-management.md) für die Integration. Bewahren Sie den Schlüssel in einem Secret Store auf; legen Sie ihn nicht in einem Screenshot, Dokument oder einer Quelldatei ab.
2. Öffnen Sie die [aktuelle API-Referenz der Sandbox](https://sandbox.api.docbits.com/docs). Sie listet die verfügbaren Operationen, erforderlichen Werte und Beispielantworten für diese Umgebung auf. Verwenden Sie die Referenz Ihrer eigenen Umgebung, wenn Sie die Sandbox verlassen.

<figure><img src="../../../../.gitbook/assets/api-calls-key-context-en.png" alt="Englischer Bereich API Key von DocBits mit der Schaltfläche Create API Key; es ist kein Schlüsselwert sichtbar"><figcaption><p>API-Schlüssel finden Sie unter Settings → Integration &amp; SSO. Das Bild enthält keinen Schlüsselwert.</p></figcaption></figure>

## Beispiel: Dokumenttypen lesen

Die Sandbox-Referenz listet **GET `/document_type/get_document_types`** auf. Der Aufruf liefert die Dokumenttypen, die Ihrer Organisation zur Verfügung stehen. `GET` liest Informationen; es erstellt oder ändert kein Dokument.

Setzen Sie Ihren API-Schlüssel als lokale Umgebungsvariable und senden Sie dann die Anfrage:

```sh
curl --fail-with-body \
  -H "X-API-KEY: ${DOCBITS_API_KEY}" \
  "https://sandbox.api.docbits.com/sandbox-api/document_type/get_document_types"
```

Eine erfolgreiche Antwort enthält `success: true` und eine `data`-Liste mit Dokumenttypen. Eine Antwort `401` bedeutet, dass die Anfrage nicht authentifiziert war; prüfen Sie den Schlüssel und die Umgebung, bevor Sie es erneut versuchen. Die obige URL gilt nur für die Sandbox.

## Die nächste Operation finden

Suchen Sie in der API-Referenz nach dem, was Sie tun möchten, lesen Sie die Beschreibung und die erforderlichen Felder der Operation und prüfen Sie, ob sie `GET`, `POST` oder eine andere Methode verwendet. Verwenden Sie die Beispielantwort der Referenz, um das Ergebnis zu bestätigen. Eine Anleitung für Postman finden Sie unter [Postman für DocBits](../../../../advanced-functions-and-tools/postman-for-docbits/README.md); prüfen Sie die dortigen älteren Beispiel-URLs anhand der aktuellen API-Referenz, bevor Sie eine Anfrage senden.

Die vier älteren Bilder auf dieser Seite beschrieben allgemeine APIs für OCR, NLP, Dateikonvertierung und Dokumentenmanagement, ohne verifizierte DocBits-Endpunkte zu zeigen. Sie wurden entfernt; als ausführbares Beispiel wird nur die oben dokumentierte DocBits-Operation gezeigt.
