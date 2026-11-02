---
description: So importieren Sie Stammdaten direkt in DocBits.
---

# Benutzerdefinierte Stammdaten

#### Benutzerdefinierte Stammdaten aktivieren <a href="#activating-custom-master-data" id="activating-custom-master-data"></a>

Navigieren Sie vom Dashboard zu Settings → Document Processing → Module.

![](<../../.gitbook/assets/DocBits_CMD_1 (1).png>)

<div align="left"><figure><img src="../../.gitbook/assets/site-extra-modules-document-integration-de.png" alt="Module der Dokumentintegration: Skripte, Dokumentenscan, Barcode-Erkennung und benutzerdefinierte Stammdaten."><figcaption><p>Module der Dokumentintegration: Skripte, Dokumentenscan, Barcode-Erkennung und benutzerdefinierte Stammdaten.</p></figcaption></figure></div>

Aktivieren Sie im Bereich Module die Option Custom Master Data, indem Sie wie unten gezeigt auf den Schieberegler klicken.

<div align="left"></div>

#### Funktionsübersicht <a href="#feature-overview" id="feature-overview"></a>

Um eigene Stammdaten in DocBits hinzuzufügen, navigieren Sie in den Settings zu Master Data Lookup.

<div align="left"><figure><img src="../../.gitbook/assets/site-extra-master-data-overview-de.png" alt="Deutsche Stammdatenansicht mit ausgeblendeten Datensätzen. Spaltenbezeichnungen der Datenquelle wie Address und Custom Field bleiben im Bild englisch."><figcaption><p>Deutsche Stammdatenansicht mit ausgeblendeten Datensätzen. Spaltenbezeichnungen der Datenquelle wie Address und Custom Field bleiben im Bild englisch.</p></figcaption></figure></div>

Klicken Sie auf „Custom Master Data“.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_5.png" alt="" width="375"><figcaption></figcaption></figure></div>

Anschließend haben Sie die Möglichkeit, ein Template oder einen Endpoint zu erstellen.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_6.png" alt="" width="375"><figcaption></figcaption></figure></div>

#### Ein Template erstellen <a href="#create-a-template" id="create-a-template"></a>

Im ersten Schritt wählen Sie, ob Sie die ION-API-Datei Ihrer Organisation verwenden oder OAuth2 nutzen und die erforderlichen Daten eingeben.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_7.png" alt="" width="375"><figcaption></figcaption></figure></div>

Als Nächstes konfigurieren wir die Voreinstellungen. Hier geben Sie den Namen der Stammdatentabelle und die URL des API-Aufrufs ein.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_8.png" alt="" width="375"><figcaption></figcaption></figure></div>

Danach müssen Sie den JSON-Pfad in Punktnotation angeben. Weitere Informationen zur Punktnotation finden Sie [hier](https://docs.hevodata.com/sources/engg-analytics/streaming/rest-api/writing-jsonpath-expressions/).

Zum Schluss ordnen Sie die Daten den Spalten zu, die Sie erstellen möchten, wie im folgenden Beispiel.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_9.png" alt="" width="375"><figcaption></figcaption></figure></div>

Klicken Sie danach auf Done, damit Ihre neuen Stammdaten erstellt und befüllt werden.

#### Einen Endpoint erstellen <a href="#create-an-endpoint" id="create-an-endpoint"></a>

Im ersten Schritt wählen Sie, ob Sie die ION-API-Datei Ihrer Organisation oder OAuth2 verwenden oder dieses Feld leer lassen und die erforderlichen Daten eingeben.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_10.png" alt="" width="375"><figcaption></figcaption></figure></div>

Als Nächstes konfigurieren wir die Voreinstellungen. Hier geben Sie den Namen der Stammdatentabelle und die URL des API-Aufrufs ein.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_8.png" alt="" width="375"><figcaption></figcaption></figure></div>

Danach müssen Sie den JSON-Pfad in Punktnotation angeben. Weitere Informationen zur Punktnotation finden Sie [hier](https://docs.hevodata.com/sources/engg-analytics/streaming/rest-api/writing-jsonpath-expressions/).

Zum Schluss ordnen Sie die Daten den Spalten zu, die Sie erstellen möchten, wie im folgenden Beispiel.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_9.png" alt="" width="375"><figcaption></figcaption></figure></div>

Klicken Sie danach auf Done, damit Ihre neuen Stammdaten erstellt und befüllt werden.
