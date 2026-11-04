# When

<figure><img src="../../../../.gitbook/assets/docbits_workflow_4.png" alt="Workflow Übersicht"><figcaption></figcaption></figure>

#### Verständnis des "Wann" in Workflow-Konfigurationen

**Zweck von "Wann"**

* Der Abschnitt "Wann" in einer Workflow-Konfiguration definiert die Auslösebedingungen, die eine bestimmte Workflow-Aktion initiieren. Diese Bedingungen basieren auf festgelegten Kriterien in Bezug auf Dokumentattribute oder Benutzeraktivitäten innerhalb des ERP-Systems.

**Wie es funktioniert**

* In Ihrer Benutzeroberfläche erscheint "Wann" als Ausgangspunkt, an dem Benutzer verschiedene Trigger-Karten auswählen können. Jede Karte legt Bedingungen fest, unter denen nachfolgende Aktionen (definiert in einem anderen Abschnitt der Workflow-Konfiguration, wahrscheinlich mit der Bezeichnung "Aktion") ausgeführt werden.

**Bedingungskarten für Dokumententypen**

* Die in der Abbildung angezeigten Karten sind Varianten von "Dokumententyp"-Bedingungen, die verwendet werden, um Workflows basierend auf dem Typ des zu verarbeitenden Dokuments auszulösen. Hier ist eine Aufschlüsselung jeder Art von Bedingungskarte:
* **Dokumententyp (Operator) einer von (Typ)**: Diese Karte löst eine Aktion aus, wenn der Typ eines Dokuments mit einem der angegebenen Typen in einer Liste übereinstimmt. Der Operator könnte Optionen wie "ist" oder "ist nicht" enthalten, was inclusive oder exklusive Bedingungen ermöglicht.
* **Dokumententyp (Operator) (Typ)**: Diese einfachere Variante wird basierend auf einer einzelnen Dokumententyp-Bedingung ausgelöst. Es würde typischerweise überprüfen, ob der Dokumententyp "ist" oder "ist nicht" ein bestimmter Typ ist, ohne die Möglichkeit, aus mehreren Typen auszuwählen.

#### Einrichten einer "Wann"-Triggerkarte

1. **Auswahl des Bedingungstyps**: Benutzer beginnen mit der Auswahl eines für den zu automatisierenden Workflow relevanten Bedingungstyps. In diesem Fall stehen Dokumententypen im Mittelpunkt.
2. **Definition des Operators**: Benutzer müssen den logischen Operator festlegen – wie "ist" oder "ist nicht" – der die Grundlage für den Vergleich der tatsächlichen Dokumententypen mit den definierten Bedingungen bildet.
3. **Spezifizierung der Dokumententypen**: Abhängig von der Karte können Benutzer einen oder mehrere Dokumententypen auswählen, die den Workflow auslösen, wenn Dokumente dieser Typen verarbeitet werden.
4. **Abschließen des Triggers**: Sobald die Bedingung eingerichtet ist, bildet sie die Grundlage für das Auslösen spezifischer Aktionen, die im Workflow definiert sind. Wenn ein Dokument die festgelegte Bedingung erfüllt, werden die definierten Aktionen automatisch initiiert.

#### Praktische Anwendung

In der Praxis sind diese Triggerkarten entscheidend für die Automatisierung von Prozessen wie Genehmigungen, Benachrichtigungen oder jedem Verfahren, das vom Typ des behandelten Dokuments abhängt. Wenn beispielsweise ein Dokumententyp "Rechnung" ist und er den in der "Wann"-Karte festgelegten Bedingungen entspricht, könnte der Workflow das Dokument automatisch zur Zahlungsabwicklung weiterleiten.

Diese Einrichtung gewährleistet, dass Workflows nicht nur effizient, sondern auch auf die spezifischen betrieblichen Anforderungen der Organisation zugeschnitten sind, was die manuelle Überwachung reduziert und die Bearbeitung von Dokumenten beschleunigt.

Zusammenfassend geht es bei dem "Wann"-Teil Ihrer Workflow-Konfiguration darum, die Bühne für automatisierte Aktionen basierend auf spezifischen, vordefinierten Bedingungen zu setzen. Es ist ein leistungsstarkes Werkzeug, um sicherzustellen, dass Ihr ERP-System dynamisch auf die Bedürfnisse des Unternehmens reagiert und sowohl die Produktivität als auch die Genauigkeit im Dokumentenmanagement verbessert.
