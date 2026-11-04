# Regelmanager

Dieses Dokument bietet eine umfassende Erklärung der Konfliktlösungsregeln, die im DocBits-Rechnungssystem verwendet werden. Diese Regeln sind darauf ausgelegt, automatisch Abweichungen zwischen Rechnungsdetails und Bestelldaten (PO) zu behandeln und eine genaue finanzielle Abstimmung zu gewährleisten. Das System wendet diese Regeln an, um Rechnungszeilen, Gebühren und Steuern zu verarbeiten und bei Bedarf entsprechende Anpassungen oder Notizen zu generieren.

**Struktur der Regeln**

1. **Metadaten**\
   • **version:** Identifiziert die Version der Mapping-Datei.\
   • **revision:** Revisionsnummer zur Nachverfolgung von Änderungen.\
   • **author:** Gibt den Ersteller der Mapping-Datei an.\
   • **description:** Eine kurze Beschreibung des Zwecks der Datei.\
   • **created\_at & updated\_at:** Zeitstempel für die Erstellung und die letzte Aktualisierung der Datei.
2. **Exportkonfiguration**\
   Der Abschnitt zur Exportkonfiguration definiert die Zuordnung zwischen den Datenfeldern im System und den entsprechenden Feldern in den Exportdateien.\
   • **Header:** Definiert die Kopfzeilenfelder für die exportierten Rechnungsdaten.\
   • **Tax Lines:** Gibt die Felder für Steuerzeilen in dem Export an.\
   • **Order Header Charges:** Ordnet Felder zu, die mit zusätzlichen Gebühren auf der Ebene des Bestellkopfes verbunden sind.\
   • **Receipt Lines:** Ordnet Felder für einzelne Zeilenartikel in einem Beleg zu.\
   • **Order Line Charges:** Definiert die Felder für Gebühren, die sich auf spezifische Bestellzeilen beziehen.\
   • **Cost Lines:** Gibt Felder für Kostenverteilungszeilen an.\
   • **Debit Note & Credit Note:** Definiert Felder zur Erstellung von Belastungs- und Gutschriften in Fällen von Abweichungen.
3. **Konfliktlösungsregeln**\
   Diese Regeln behandeln Abweichungen zwischen Rechnungsdaten und den entsprechenden Bestelldaten. Jede Regel besteht aus mehreren Komponenten:\
   • **Name:** Der beschreibende Name der Regel, der den Typ der behandelten Abweichung angibt.\
   • **Section:** Gibt an, auf welchen Teil der Rechnung (z. B. receipt\_lines, line\_charges) die Regel angewendet wird.\
   • **Active:** Boolescher Wert (true oder false), der angibt, ob die Regel derzeit aktiv ist.\
   • **Match Criteria:** Bedingungen, die die Regel auslösen, basierend auf Vergleichen zwischen den tatsächlichen Rechnungsdaten und den erwarteten Bestelldaten.\
   • **Actions:** Definiert, was das System tun soll, wenn die Regel ausgelöst wird, einschließlich der Anpassung von Werten, der Anwendung von Gebühren oder der Generierung von Gutschriften/Beschwerden.

**Gemeinsame Elemente in den Regeln**

**Vergleichsoperatoren**\
Diese Operatoren definieren, wie die tatsächlichen Rechnungswerte mit den erwarteten Bestellwerten verglichen werden:\
• gleich\
• größer als\
• größer oder gleich\
• kleiner als\
• kleiner oder gleich\
• innerhalb der Toleranz\
• außerhalb der Toleranz



**Genehmigungsstatus**\
Gibt an, ob eine Abweichung genehmigt ist oder nicht:\
• genehmigt\
• abgelehnt\
• beliebig

**Aktionstypen**\
Definiert spezifische Maßnahmen, die ergriffen werden sollen, wenn eine Abweichung festgestellt wird:\
• Empfangszeile\
• Kostenzeile\
• Kopfgebühr\
• Zeilengebühr\
• Steuerzeile\
• Belastungsnote Empfangszeile\
• Belastungsnote Kostenzeile\
• Belastungsnote Kopfgebühr\
• Belastungsnote Zeilengebühr\
• Gutschrift Empfangszeile\
• Gutschrift Kostenzeile\
• Gutschrift Kopfgebühr\
• Gutschrift Zeilengebühr\
• Gutschrift Steuerzeile

**Regelbeispiele**\
**Fall 1, 2, 3:** Menge und Stückpreis innerhalb der Toleranz\
• Zweck: Behandelt Szenarien, in denen sowohl die Menge als auch der Stückpreis auf der Rechnung innerhalb der akzeptierten Toleranzgrenzen im Vergleich zur Bestellung liegen.\
• Aktion: Das System akzeptiert die Rechnungswerte und berechnet den Gesamtbetrag.

**Fall 4, 5:** Menge innerhalb der Toleranz, Stückpreis außerhalb der Toleranz (genehmigt)\
• Zweck: Gilt, wenn die Menge innerhalb der Toleranz liegt, der Stückpreis jedoch außerhalb der Toleranz liegt und genehmigt wurde.\
• Aktion: Das System passt den Stückpreis an, um mit der Bestellung übereinzustimmen, und wendet erforderliche Zeilengebühren an.

**Fall 6:** Menge innerhalb der Toleranz, Stückpreis außerhalb der negativen Toleranz (abgelehnt)\
• Zweck: Behandelt Fälle, in denen der Stückpreis geringer ist als erwartet und außerhalb des Toleranzbereichs liegt, was zu einer Ablehnung führt.\
• Aktion: Das System passt den Stückpreis an, um mit der Bestellung übereinzustimmen, generiert eine Gutschrift für die Differenz und wendet bei Bedarf Kopfgebühren an.

**Behandlung von Gebühren und Steuern**\
**Gebühr pro Einheit Toleranz**\
• Regeln in dieser Kategorie behandeln Abweichungen bei Gebühren pro Einheit, mit spezifischen Maßnahmen, basierend darauf, ob die Gebühr innerhalb oder außerhalb der Toleranz liegt und ob sie genehmigt oder abgelehnt ist.

**Steuerzeilenanpassungen**\
• Diese Regeln verwalten Steuerabweichungen, indem sie die Steuerzeilen anpassen oder entsprechende Gutschriften oder Belastungsnoten basierend auf den Unterschieden zwischen Rechnungs- und Bestelldaten generieren.

**Enums und Optionen**\
• **Enums:** Vorgegebene Wertelisten, die Konsistenz über die Regeln hinweg gewährleisten (z. B. Vergleichsoperatoren, Genehmigungsarten).\
• **Optionen:** Vorgegebene Auswahlmöglichkeiten für die Handhabung von Mengen oder Stückpreisen, die Flexibilität bei der Regeldefinition bieten.

**Screenshots Erklärung**\
**Screenshot 1:** Regelmanagement-Oberfläche\
Dieser Screenshot zeigt die Regelmanagement-Oberfläche, auf der Administratoren alle Konfliktlösungsregeln einsehen und verwalten können. Wichtige Elemente sind:\
• **Regel hinzufügen Schaltfläche:** Ermöglicht das Hinzufügen neuer Regeln.\
• **Regelliste:** Zeigt alle aktiven Regeln mit Details wie Name, Abschnitt und aktivem Status an.\
• **Abschnitt Dropdown:** Filtert die Regeln basierend auf dem Abschnitt, auf den sie sich beziehen (z. B. Empfangszeilen, Zeilengebühren).

**Screenshot 2:** Detaillierte Regelbearbeitung\
Dieser Screenshot zeigt die detaillierte Ansicht einer bestimmten Regel, die bearbeitet wird. Wichtige Elemente sind:\
• **Kriterienbereich:** Definiert die Bedingungen, unter denen die Regel ausgelöst wird. Beispielsweise könnte das Kriterium angeben, dass, wenn die Menge und der Stückpreis von der Bestellung abweichen, aber innerhalb der Toleranz liegen, die Regel angewendet werden sollte.\
• **Aktionsbereich:** Gibt an, welche Maßnahmen ergriffen werden sollen, wenn die Kriterien erfüllt sind. Dies kann die Anpassung der Rechnungszeilen, die Generierung von Gutschriften oder Belastungsnoten oder die Anwendung zusätzlicher Gebühren umfassen.\
• **Dokumenttyp und Kostenbestandteile:** Ermöglicht es dem Administrator, spezifische Maßnahmen den Dokumenttypen und Kostenbestandteilen zuzuordnen, was Flexibilität bei der Handhabung verschiedener Szenarien bietet.
