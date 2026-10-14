# Module active

<figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Zweck:**

Diese DocBits-Karte prüft, ob ein bestimmtes Modul im System aktiv oder inaktiv ist. Sie ermöglicht es Workflows, basierend auf dem Aktivierungsstatus eines Moduls fortzufahren, und stellt sicher, dass Aktionen nur ausgeführt werden, wenn das erforderliche Modul verfügbar ist.

## **Funktionalität:**

* **Validierung des Modulstatus:** Diese Karte überprüft den Aktivierungsstatus eines angegebenen Moduls und wertet ihn anhand einer benutzerdefinierten Bedingung aus.
* **Modulauswahl:** Benutzer geben den Namen des zu prüfenden Moduls an und gewährleisten so eine präzise Validierung.
* **Operatoren:** Die folgenden Bedingungen können angewendet werden:
  * **Is:** Der Workflow wird fortgesetzt, wenn das ausgewählte Modul aktiv ist.
  * **Is Not:** Der Workflow wird fortgesetzt, wenn das ausgewählte Modul inaktiv ist.

## **Verwendung:**

Diese Karte ist besonders nützlich für Administratoren oder Systemverantwortliche, die Workflows erstellen müssen, die von der Verfügbarkeit oder Funktionalität bestimmter Module abhängen. Sie hilft sicherzustellen, dass Workflows nur ausgeführt werden, wenn alle erforderlichen Module ordnungsgemäß konfiguriert sind.

## **Beispiel-Szenario**

* Ein Benutzer konfiguriert die Karte so, dass sie prüft, ob das Modul **"Document Processing"** **aktiv ist.** Ist das Modul aktiv, wird der Workflow fortgesetzt und löst automatisierte Aufgaben zur Dokumentverarbeitung aus. Ist das Modul inaktiv, wird der Workflow angehalten, um unnötige Aktionen zu verhindern.

Durch die Verwendung der Karte "Module Active Check" können Organisationen die Zuverlässigkeit von Workflows verbessern, Fehler durch inaktive Module vermeiden und sicherstellen, dass Prozesse mit der Systemkonfiguration übereinstimmen.
