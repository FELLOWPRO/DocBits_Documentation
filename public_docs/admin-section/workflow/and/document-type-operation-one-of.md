# Dokumententyp-Operation einer von

<figure><img src="../../../.gitbook/assets/userlmn_14ab8ac5e693d9bbe68d178795d12a9f.png" alt=""><figcaption></figcaption></figure>

**Zweck**

Diese Karte ist darauf ausgelegt, Aktionen auf Dokumenten abhängig von ihrem Typ zu verwalten, indem einfache bedingte Logik (ist/ist nicht) angewendet wird, um spezifische Workflows auszulösen oder zu verhindern. Dies ermöglicht eine präzise Kontrolle darüber, wie verschiedene Arten von Dokumenten im ERP-System verarbeitet werden.

**Komponenten der Karte**

1. **Operator**
* **Beschreibung**: Bestimmt die bedingte Logik, die auf die Dokumententypen angewendet wird.
* **Optionen**:
* **ist**: Die Operation wird ausgelöst, wenn der Typ des Dokuments mit einem der angegebenen Typen in der Liste übereinstimmt.
* **ist nicht**: Die Operation wird ausgelöst, wenn der Typ des Dokuments mit keinem der aufgeführten Typen übereinstimmt.
2. **Liste der Dokumententypen**
* **Beschreibung**: Legt eine Liste von Dokumententypen fest, auf die die Bedingung angewendet wird.
* **Details**: Dies kann eine Vielzahl von Dokumententypen wie "Rechnung", "Bestellung", "Vertrag", "Mitarbeiterakte" usw. umfassen, basierend auf denen die Bedingung (ist/ist nicht) ausgewertet wird.

**Funktionalität**

* **Dokumentenidentifikation**: Das System identifiziert zunächst den Typ jedes eingehenden oder vorhandenen Dokuments anhand vordefinierter Attribute oder Metadaten.
* **Bedingungsauswertung**:
* Wenn der Operator **ist** ist, überprüft die Karte, ob der Dokumententyp in der bereitgestellten Liste enthalten ist.
* Wenn der Operator **ist nicht** ist, überprüft die Karte, ob der Dokumententyp nicht in der Liste enthalten ist.
* **Aktionstrigger**: Abhängig vom Ergebnis der Bedingungsauswertung:
* **Wahr**: Initiiert die zugehörigen Operationen oder Workflows, wenn die Bedingung erfüllt ist.
* **Falsch**: Der Prozess wird umgangen oder es wird eine alternative Operation ausgelöst, wenn die Bedingung nicht erfüllt ist.
* **Integration und Automatisierung**: Integriert nahtlos mit anderen Systemkomponenten, um sicherzustellen, dass die Dokumentenverarbeitung automatisiert ist und den organisatorischen Workflows und Richtlinien entspricht.

**Benutzerinteraktionen**

* **Konfiguration**: Benutzer müssen den Operator angeben und die Dokumententypen auflisten, wenn sie die Karte einrichten. Diese Einrichtung kann Interface-Elemente wie Dropdown-Listen oder Kontrollkästchen umfassen, um Dokumententypen und Operatoren auszuwählen.
* **Überwachung und Anpassungen**: Benutzer können die Ergebnisse und die Wirksamkeit dieser Karte über Protokolle und Berichte überwachen, die vom ERP-System generiert werden. Anpassungen können basierend auf sich entwickelnden Geschäftsanforderungen an der Liste oder dem Operator vorgenommen werden.
* **Fehlerbehandlung und Feedback**: Bietet Feedback-Mechanismen für während des Betriebs aufgetretene Fehler. Benutzer können Warnmeldungen einrichten, wenn Bedingungen fehlschlagen, um eine schnelle Behebung von Problemen sicherzustellen.

#### Fazit

Die Workflow-Karte "Dokumententyp-Bedingung" spielt eine entscheidende Rolle bei der Verwaltung von dokumentenbasierten Operationen mit Präzision und Flexibilität. Durch die Verwendung einfacher bedingter Logik wird sichergestellt, dass Dokumente angemessen verarbeitet werden, was die Effizienz und Einhaltung verbessert. Eine klare Dokumentation dieser Karte hilft Benutzern zu verstehen, wie sie diese effektiv implementieren und nutzen können, was sie zu einem wertvollen Bestandteil der Dokumentation Ihres ERP-Systems macht.
