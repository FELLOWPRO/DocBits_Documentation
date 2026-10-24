# Modul aktiv

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-405c9bb87c62-de.png" alt="Kartenfelder in der angezeigten Version. Die Platzhalter sind noch nicht ausgefüllt." width="563"><figcaption><p>Kartenfelder in der angezeigten Version. Die Platzhalter sind noch nicht ausgefüllt.</p></figcaption></figure>

## **Zweck:**

Diese DocBits-Karte prüft, ob ein bestimmtes Modul im System aktiv oder inaktiv ist. Sie ermöglicht es Workflows, basierend auf dem Aktivierungsstatus eines Moduls fortzufahren, und stellt sicher, dass Aktionen nur ausgeführt werden, wenn das erforderliche Modul verfügbar ist.

## **Funktionalität:**

* **Validierung des Modulstatus:** Diese Karte überprüft den Aktivierungsstatus eines angegebenen Moduls und wertet ihn anhand einer benutzerdefinierten Bedingung aus.
* **Modulauswahl:** Benutzer geben den Namen des zu prüfenden Moduls an und gewährleisten so eine präzise Validierung.
* **Operatoren:** Die folgenden Bedingungen können angewendet werden:
  * **Is:** Der Workflow wird fortgesetzt, wenn das ausgewählte Modul aktiv ist.
  * **Ist nicht:** Der Workflow wird fortgesetzt, wenn das ausgewählte Modul inaktiv ist.

## **Verwendung:**

Diese Karte ist besonders nützlich für Administratoren oder Systemverantwortliche, die Workflows erstellen müssen, die von der Verfügbarkeit oder Funktionalität bestimmter Module abhängen. Sie hilft sicherzustellen, dass Workflows nur ausgeführt werden, wenn alle erforderlichen Module ordnungsgemäß konfiguriert sind.

## **Beispiel-Szenario**

* Ein Benutzer konfiguriert die Karte so, dass sie prüft, ob das **Bestellmodul (`PO_DASHBOARD`)** **aktiv ist.** Ist das Modul aktiv, wird der Workflow fortgesetzt und löst automatisierte Aufgaben zur Dokumentverarbeitung aus. Ist das Modul inaktiv, ist diese Bedingung nicht erfüllt; die Karte aktiviert es nicht.

Durch die Verwendung der Karte "Module Active Check" können Organisationen die Zuverlässigkeit von Workflows verbessern, Fehler durch inaktive Module vermeiden und sicherstellen, dass Prozesse mit der Systemkonfiguration übereinstimmen.

<!-- workflow-card-practical-example-20261021 -->

## Praxisbeispiel

**Wann nutzen:** Eine Regel nur verwenden, wenn das benötigte Modul aktiv ist.

**Wo:** Standard-Workflow-Designer → Und → Logik.

**Konfiguration:** Wählen Sie in Version 2 das angebotene Bestellmodul (`PO_DASHBOARD`) und den Operator „ist“ (`is`).

**Erwartetes Ergebnis und Gegenbeispiel:** Die Bedingung ist bei aktivem Modul erfüllt und bei inaktivem Modul nicht erfüllt. Die Karte aktiviert das Modul nicht. Prüfen Sie vor dem Einsatz den tatsächlichen Modulzustand und die passende Berechtigung.

Die Beispiele beschreiben erwartete Ergebnisse. Verwenden Sie die in Ihrer Organisation tatsächlich konfigurierten Felder und angebotenen Werte.

## Admin-Beispielvideo

Wann ich die Verfügbarkeit eines Moduls als Bedingung prüfe. Die Karte prüft den Modulzustand; sie aktiviert das Modul nicht. Die Beispiele zeigen erwartete Ergebnisse.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-module-active-admin/v1/de.mp4" %}

[Video mit deutschen Untertiteln öffnen](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-module-active-admin/v1/de.html)

[Transkript lesen](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-module-active-admin/v1/de.txt)
