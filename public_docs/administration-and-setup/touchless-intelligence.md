# Touchless Intelligence

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence/v1/de.mp4" %}

Touchless Intelligence erklärt zwei unterschiedliche Fragen: **Hat DocBits die Rechnung richtig ausgelesen?** Und: **Konnte der gesamte Prozess ohne Bearbeitungseingriff abschließen?** Korrekte Auslesung kann bei abweichenden Infor-Daten trotzdem Nacharbeit auslösen. AP bezeichnet die menschliche Kreditorenbuchhaltung.

<figure><img src="../.gitbook/assets/anatomy-touchless-de.svg" alt="Isometrische Sortierstrecke: ein Förderband mit 14 Toren, ein Schieber, der ein Dokument in ein Prüffach umleitet, ein Exportbehälter mit einem Dokumentenstapel und eine Anzeige mit 78,9 Prozent"><figcaption><p>Touchless als Sortierstrecke, mit den Beispielzahlen aus der Rechenbeispiel-Tabelle: Die 14 Tore sind die Schritte des Verarbeitungspfads, Blätter, die noch auf dem Band liegen, sind in Bearbeitung und werden nicht gezählt, ein Dokument, das an einem Tor stoppt, landet im Prüffach bei den Dokumenten mit AP Assisted (30) und den Prozessausnahmen (10), und die Dokumente mit Pure Touchless (120) und reiner Freigabe (30) im Exportbehälter ergeben 150 von 190 beziehungsweise 78,9 % auf der Anzeige, über der Zielmarke von 70 %.</p></figcaption></figure>

## Die passende Unterseite finden

| Unterseite | Inhalt |
| --- | --- |
| [Kennzahlen und Berechnung](touchless-metrics.md) | Kategorien, Zähler und Nenner, AP-Eingriffe und Rechenbeispiele |
| [Dashboard bedienen](touchless-dashboard.md) | Filter, Kennzahlenkarten, Trend, erste Blocker und Bedienung |
| [Praxisbeispiele: Preis und Menge](touchless-examples.md) | Fiktive Rechnungen und echte Dev-Bestellansichten mit Preis- und Mengenabweichungen |
| [Touchless Intelligence: Lieferantendiagnose und Fehlermuster](touchless-supplier-diagnosis.md) | Lieferanten und wiederkehrende Ursachen priorisieren |
| [Touchless Intelligence: Bestellabgleich-Diagnose](touchless-po-matching-diagnosis.md) | Aktive Regeln, Toleranzen und Entscheidungsablauf verstehen |
| [Touchless Intelligence: Dokumentverlauf](touchless-document-trace.md) | Originalwerte, Verarbeitungsläufe, Blocker und Eingriffe prüfen |
| [Touchless Intelligence: Änderungsvorschläge und Berichte](touchless-change-proposals.md) | Vorschau, Anwendung, Wirkungsmessung und Rücknahme unterscheiden |
| [Touchless mit MCP erklären und verbessern](touchless-mcp.md) | Über MCP erklären, diagnostizieren und kontrolliert verbessern |

<figure><img src="../.gitbook/assets/touchless-overview-de.png" alt="Der Tab Touchless Intelligence mit fünf Kennzahlen, Verbesserungsvorschlägen und dem Diagramm der Touchless-Quote"><figcaption><p>Der Tab Touchless Intelligence: Kennzahlen, Verbesserungen, die Quote im Zeitverlauf und das Diagramm „Wo Touchless zuerst verloren geht“. Beispielorganisation mit Demodaten; die Lieferantennamen sind frei erfunden.</p></figcaption></figure>

## Zugriff

Der Bereich gehört zum [Analytics Dashboard](analytics-dashboard.md). Administratoren haben Zugriff; weitere Benutzer benötigen die entsprechende Rollenzuweisung. KI-Analyse, unterstützte Änderungen und Consulting-Berichte können zusätzliche Administratorrechte erfordern.

<!-- Source notes (not shown): screenshots come from the dev test organisation with synthetic demo data (seed script) and fictional supplier names; the PO matching decision flow is illustrated on the matching-diagnosis subpage. facts read from the doc2app code (TouchlessIntelligence pages and components) and the dev UI on 14 Oct 2026; NOVA gates the tab with its own organisation flag, VESTA with the Analytics module. Consulting report export format not verified, so no export is described. -->
<!-- Doku-Prüfung 04.11.2026: Auslesequalität getrennt von Prozessergebnissen; Kennzahlen und Endergebnisse gegen DocBits_API c51f350c728acb8ac964098d15f7b006bce273f4, module/automation_intelligence/kpi.py und bucket.py, geprüft. Bestehende deutsche Originalaufnahmen getrennt von den Schulungsbeispielen geprüft. -->
<!-- Completion review 2026-11-04: AP actions, original-value evidence, overlapping KPI labels, sequential blockers and screenshot proof limits checked. -->
