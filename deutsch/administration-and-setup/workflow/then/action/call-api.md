# Call Api

<figure><img src="../../../../.gitbook/assets/Then_Call_API.png" alt="" width="563"><figcaption></figcaption></figure>

## Zweck:

Die Workflow-Karte **"Call API"** ermöglicht es Benutzern, HTTP-Anfragen direkt aus dem Workflow an angegebene API-Endpunkte zu senden. Diese Karte unterstützt verschiedene HTTP-Methoden und ermöglicht eine dynamische Interaktion mit externen Systemen durch das Senden von Parametern und Daten. Sie optimiert die Integration mit Drittanbieterdiensten und benutzerdefinierten APIs und gewährleistet eine nahtlose Kommunikation.

## Bestandteile der Karte:

1. **API-Endpunkt**
   * **Beschreibung:** Der Ziel-Endpunkt der **DocBits API**, mit dem diese Karte interagiert.
   * **Detail:** Ein Textfeld, in dem Benutzer den Endpunkt für die API-Anfrage angeben.
2. **HTTP-Methode**
   * **Beschreibung:** Die Art der durchzuführenden HTTP-Anfrage.
   * **Optionen:**
     1. **GET:** Ruft Daten vom angegebenen Endpunkt ab.
     2. **POST:** Sendet Daten an den Endpunkt.
     3. **PUT:** Aktualisiert vorhandene Daten am Endpunkt.
     4. **DELETE:** Entfernt Daten am Endpunkt.
3. **Parameter**
   * **Beschreibung:** Abfrageparameter, die in die API-Anfrage aufgenommen werden.
   * **Detail:** Ein Textfeld oder eine Liste zur Eingabe von Schlüssel-Wert-Paaren für die Anfrage-URL.
4. **Daten**
   1. **Beschreibung:** Die im Body der API-Anfrage zu sendende Nutzlast (gilt für die Methoden POST und PUT).
   2. **Detail:** Ein Feld zur Eingabe der Daten in JSON.

## Funktionalität:

**Bedingungsauswertung:** Das System wertet die in den Abschnitten "Where" und "And" definierten Bedingungen aus:

* Sind beide Bedingungen **erfüllt**, wird die API-Anfrage wie konfiguriert ausgeführt.
* Ist eine der Bedingungen **nicht erfüllt**, wird die Karte nicht ausgeführt, und es erfolgt kein API-Aufruf.

**Ausführung der API-Anfrage:**

* Die Karte sendet die HTTP-Anfrage mit der ausgewählten Methode an den angegebenen Endpunkt.
* Alle angegebenen Parameter werden an die URL angehängt, und die Daten werden (falls zutreffend) in den Anfrage-Body aufgenommen.

## Einrichtung und Konfiguration:

1. **API-Endpunkt definieren:**\
   Geben Sie die URL der API ein, die Sie aufrufen möchten.
2. **HTTP-Methode auswählen:**\
   Wählen Sie eine der unterstützten Methoden (GET, POST, PUT, DELETE) entsprechend den Anforderungen Ihrer API.
3. **Parameter angeben:**\
   Fügen Sie die erforderlichen Abfrageparameter als Schlüssel-Wert-Paare hinzu.
4. **Daten einfügen (falls zutreffend):**\
   Geben Sie bei den Methoden POST oder PUT die im Anfrage-Body zu sendenden Daten an.
5. **Bedingungskonfiguration:**\
   Konfigurieren Sie die Abschnitte "Where" und "And", um festzulegen, wann der API-Aufruf erfolgen soll.

## Fazit:

Die Workflow-Karte **"Call API"** verbessert die Workflow-Automatisierung, indem sie eine direkte Interaktion mit externen Systemen ermöglicht. Durch flexible Konfigurationen für Endpunkte, Methoden und Daten stellt sie sicher, dass Workflows nahtlos in Drittanbieter-APIs oder benutzerdefinierte Backends integriert werden können. Die Möglichkeit, API-Aufrufe bedingt auszuführen, gewährleistet Präzision und Effizienz bei der Automatisierung externer Kommunikation.

***
