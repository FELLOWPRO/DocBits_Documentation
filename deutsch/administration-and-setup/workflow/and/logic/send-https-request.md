# Send HTTPS Request

<figure><img src="../../../../.gitbook/assets/image (4) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Zweck:**

Diese DocBits-Karte ist darauf ausgelegt, die Interaktion mit externen Systemen zu ermöglichen, indem sie HTTPS-Anfragen an angegebene URLs sendet. Sie ermöglicht es Workflows, Aktionen wie Datenabruf, Aktualisierungen oder Löschungen durch API-Aufrufe durchzuführen, und gewährleistet so eine nahtlose Integration mit externen Diensten.

## **Funktionalität:**

* **Ausführung der HTTPS-Anfrage:** Die Karte sendet eine Anfrage an eine angegebene URL unter Verwendung der konfigurierten HTTP-Methode (z. B. GET, POST, PUT, DELETE).
* **Header und Parameter:** Benutzer können benutzerdefinierte Header und Abfrageparameter einbinden, um sicherzustellen, dass die Anfrage den Anforderungen der externen API entspricht.
* **Anfragedaten:** Ermöglicht es Benutzern, die mit der Anfrage zu sendende Datennutzlast (falls zutreffend) zu definieren, etwa JSON- oder formularcodierte Daten.
* **Auswertung der Antwort:** Der Workflow prüft, ob der empfangene Statuscode mit dem erwarteten Wert übereinstimmt, und stellt so eine erfolgreiche Kommunikation sicher, bevor fortgefahren wird.
* **Unterstützte HTTP-Methoden:**
  * GET: Ruft Daten von der angegebenen URL ab.
  * POST: Übermittelt Daten an die angegebene URL, um Ressourcen zu erstellen.
  * PUT: Aktualisiert vorhandene Ressourcen unter der angegebenen URL.
  * DELETE: Entfernt Ressourcen von der angegebenen URL.

## **Verwendung:**

Diese Karte ist besonders nützlich in Szenarien, in denen Workflows mit externen APIs zum Datenaustausch interagieren müssen, etwa beim Senden von Aktualisierungen an ein CRM, beim Abrufen von Auftragsstatus oder beim Anlegen neuer Einträge in einer Datenbank.

## **Beispiel-Szenario:**

* Ein Benutzer konfiguriert die Karte so, dass sie eine POST-Anfrage an ein externes Auftragsmanagementsystem mit einer Nutzlast sendet, die neue Auftragsdetails enthält. Es werden benutzerdefinierte Header hinzugefügt, um API-Authentifizierungstoken einzubinden. Die Karte ist so eingestellt, dass sie nur fortfährt, wenn der Antwort-Statuscode 201 (Created) lautet. Weicht der Statuscode ab, löst der Workflow eine Fehlerbenachrichtigung für einen manuellen Eingriff aus.

Durch die Verwendung der Karte "Send HTTPS Request" können Organisationen externe Integrationen automatisieren, die Kommunikation zwischen Systemen verbessern und komplexe Workflows optimieren.
