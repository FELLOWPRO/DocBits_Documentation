---
description: Dokumente mit einem lokalen Scanner und Doc Scan in DocBits erstellen.
---

# Doc Scan

## Scannersoftware herunterladen und installieren

Klicken Sie im DocBits-Dashboard auf Scan Document.

<figure><img src="../../../../.gitbook/assets/image (203).png" alt="Scan-Document-Schaltfläche im DocBits-Dashboard"><figcaption></figcaption></figure>

Wenn die lokale Scannersoftware noch nicht installiert ist, zeigt DocBits eine Download-Aufforderung. Wählen Sie den Download für Ihr Betriebssystem.

<figure><img src="../../../../.gitbook/assets/image (204).png" alt="Aufforderung zum Herunterladen der lokalen Scannersoftware"><figcaption></figcaption></figure>

Öffnen Sie die heruntergeladene Installationsdatei. Der abgebildete Installer ist für macOS; folgen Sie den Anweisungen für Ihr Betriebssystem.

<figure><img src="../../../../.gitbook/assets/image (205).png" alt="Start der Installation der Scannersoftware"><figcaption></figcaption></figure>

Klicken Sie im abgebildeten Installer auf Continue, akzeptieren Sie die Softwarelizenz mit Agree und fahren Sie fort. Prüfen Sie Installationsort und Speicherbedarf und klicken Sie auf Install. Die angezeigten 33,6 MB gelten für diese Installerversion; der Speicherbedarf kann sich je nach Version ändern.

Schließen Sie den Installer, sobald die Installation abgeschlossen ist.

<figure><img src="../../../../.gitbook/assets/image (206).png" alt="Abgeschlossene Installation der Scannersoftware"><figcaption></figcaption></figure>

Öffnen Sie https://local.polydocs.io:12500/ im Browser, um den lokalen Dienst zu testen. Falls der Browser ihn nicht erreicht und Sie eine FRITZ!Box verwenden, prüfen Sie die unten beschriebenen DNS-Rebind-Einstellungen.

<figure><img src="../../../../.gitbook/assets/image (207).png" alt="Browserfehler beim Test des lokalen Scannerdienstes"><figcaption></figcaption></figure>

Sobald die Seite des lokalen Dienstes erscheint, klicken Sie auf DocBits, um DocBits zu öffnen.

<figure><img src="../../../../.gitbook/assets/image (208).png" alt="Seite des lokalen Scannerdienstes nach erfolgreicher Verbindung"><figcaption></figcaption></figure>

Melden Sie sich auf der DocBits-Anmeldeseite an, um Ihr Dashboard aufzurufen.

<figure><img src="../../../../.gitbook/assets/image (209).png" alt="Über den lokalen Dienst aufgerufene DocBits-Anmeldeseite"><figcaption></figcaption></figure>

Aktivieren Sie Doc Scan in den Einstellungen unter Module.

<figure><img src="../../../../.gitbook/assets/image (210).png" alt="Doc-Scan-Moduleinstellung"><figcaption></figcaption></figure>

## Netzwerkeinstellungen der FRITZ!Box

Wenn https://local.polydocs.io:12500/ nicht erreichbar ist, weil eine FRITZ!Box DNS-Antworten mit privaten IP-Adressen blockiert, kann der Browser eine DNS-Zeitüberschreitung melden. Die FRITZ!Box verwendet diesen Schutz gegen DNS-Rebinding. Fügen Sie für diesen lokalen Dienst eine Hostnamen-Ausnahme hinzu:

1. Öffnen Sie in der deutschen FRITZ!Box-Oberfläche Heimnetz und anschließend Netzwerk.
2. Öffnen Sie den Reiter Netzwerkeinstellungen.
3. Tragen Sie unter DNS-Rebind-Schutz den Hostnamen local.polydocs.io als Ausnahme ein.
4. Klicken Sie auf Übernehmen und testen Sie den lokalen Dienst erneut.

## Doc2Scan Service Manager deinstallieren

Führen Sie zum Deinstallieren von Doc2Scan Manager unter macOS folgenden Befehl aus:

```bash
sudo bash /Library/doc2scan/uninstall.sh
```

## Scannerkompatibilität

sane-airscan ist ein SANE-Backend für Apple AirScan/eSCL und Microsoft WSD (WS-Scan, Web Services for Devices). Dabei handelt es sich um Protokolle für das Scannen über das Netzwerk.

Prüfen Sie die [gepflegten Kompatibilitätsinformationen von sane-airscan](https://github.com/alexpevzner/sane-airscan) auf gemeldete Geräte- und Protokollunterstützung. Die Verfügbarkeit eines Protokolls oder ein positiver sane-airscan-Bericht garantiert nicht, dass jede Gerätefunktion in Doc Scan funktioniert. Testen Sie Ihren Scanner mit dem benötigten Doc-Scan-Ablauf.
