# When

<figure><img src="../../../.gitbook/assets/image (34).png" alt=""><figcaption></figcaption></figure>

#### Das "When" in Workflow-Konfigurationen verstehen

**Zweck von "When"**

* Der Abschnitt "When" in einer Workflow-Konfiguration definiert die Auslösebedingungen, die eine bestimmte Workflow-Aktion in Gang setzen. Diese Bedingungen basieren auf festgelegten Kriterien, die sich auf Dokumentattribute oder Benutzeraktivitäten innerhalb des ERP-Systems beziehen.

**So funktioniert es**

* In Ihrer Oberfläche stellt "When" einen Ausgangspunkt dar, an dem Benutzer verschiedene Auslöser-Karten auswählen können. Jede Karte legt Bedingungen fest, unter denen die nachfolgenden Aktionen (definiert im Abschnitt "And") ausgeführt werden.

**Bedingungskarten für Dokumenttypen**

* Die Karten mit dem Dokumentsymbol im Screenshot sind Varianten von "Document Type"-Bedingungen, die verwendet werden, um Workflows basierend auf der Art des verarbeiteten Dokuments auszulösen. Hier eine Aufschlüsselung der einzelnen abgebildeten Bedingungskarten:
  * **Document type (Operator) one of (Type)**: Diese Karte löst eine Aktion aus, wenn der Typ eines Dokuments mit einem der in einer Liste angegebenen Typen übereinstimmt. Der Operator kann Optionen wie "ist" oder "ist nicht" umfassen und ermöglicht so einschließende oder ausschließende Bedingungen.
  * **Document type (Operator) (Type)**: Diese einfachere Variante löst basierend auf einer einzelnen Dokumenttyp-Bedingung aus. Sie prüft typischerweise, ob der Dokumenttyp ein bestimmter Typ "ist" oder "ist nicht", ohne die Möglichkeit, aus mehreren Typen auszuwählen.
  *

**Celery Beat**

* Die Karte mit dem Uhrsymbol im Screenshot ist eine "Celery Beat"-Bedingung, die verwendet wird, um Workflows basierend auf Datum und Uhrzeit auszulösen.

#### Einrichten einer "When"-Auslöser-Karte

1. **Auswahl des Bedingungstyps**: Benutzer beginnen mit der Auswahl eines Bedingungstyps, der für den zu automatisierenden Workflow relevant ist. In diesem Fall stehen Dokumenttypen im Mittelpunkt.
2. **Festlegen des Operators**: Benutzer müssen den logischen Operator bestimmen – etwa "ist" oder "ist nicht" –, der die Grundlage für den Vergleich der tatsächlichen Dokumenttypen mit den definierten Bedingungen bildet.
3. **Angeben der Dokumenttypen**: Je nach Karte können Benutzer einen oder mehrere Dokumenttypen auswählen, die den Workflow auslösen, wenn Dokumente dieser Typen verarbeitet werden.
4. **Abschließen des Auslösers**: Sobald die Bedingung eingerichtet ist, bildet sie die Grundlage für das Auslösen bestimmter, im Workflow definierter Aktionen. Erfüllt ein Dokument die festgelegte Bedingung, werden die definierten Aktionen automatisch in Gang gesetzt.

#### Praktische Anwendung

In der Praxis sind diese Auslöser-Karten entscheidend für die Automatisierung von Prozessen wie Freigaben, Benachrichtigungen oder jedem Vorgang, der vom Typ des bearbeiteten Dokuments abhängt. Wenn ein Dokumenttyp beispielsweise eine "Rechnung" "ist" und die in der "When"-Karte festgelegten Bedingungen erfüllt, kann der Workflow das Dokument automatisch zur Zahlungsabwicklung weiterleiten.

Diese Konfiguration stellt sicher, dass Workflows nicht nur effizient, sondern auch auf die spezifischen betrieblichen Anforderungen der Organisation zugeschnitten sind, wodurch manuelle Kontrolle reduziert und die Dokumentenbearbeitung beschleunigt wird.

Zusammengefasst geht es beim "When"-Teil Ihrer Workflow-Konfiguration darum, die Voraussetzungen für automatisierte Aktionen auf Basis bestimmter, vordefinierter Bedingungen zu schaffen. Es ist ein leistungsstarkes Werkzeug, um sicherzustellen, dass Ihr ERP-System dynamisch auf die Anforderungen des Unternehmens reagiert und sowohl die Produktivität als auch die Genauigkeit im Dokumentenmanagement steigert.
