# eSLOG 1.6 und 2.0

**eSLOG 1.6** und **eSLOG 2.0** erscheinen in DocBits als getrennte Formate für elektronische Rechnungen. Wählen Sie die Version, die Ihre eingehende slowenische Rechnung verwendet. Die Screenshots unten zeigen die aktuelle englische Sandbox-Oberfläche in einer Dokumentations-Testorganisation; sie belegen nicht, dass eine Rechnung der jeweiligen Version erfolgreich verarbeitet wurde.

## Die Konfigurationen finden

1. Gehen Sie zu **Settings → Document Types → Invoice → E-Doc**.
2. Klappen Sie **E-SLOG 1.6** oder **E-SLOG 2.0** auf. Jedes Format hat seine eigenen drei Einträge.

<figure><img src="../../../../../.gitbook/assets/dbdc-142-eslog-16-en.png" alt="Englisches Sandbox-Format E-SLOG 1.6 mit den Zeilen Transformation, Preview und Extraction Paths"><figcaption>E-SLOG 1.6 in der E-Doc-Liste der Rechnung.</figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/dbdc-142-eslog-20-en.png" alt="Englisches Sandbox-Format E-SLOG 2.0 mit den Zeilen Transformation, Preview und Extraction Paths"><figcaption>E-SLOG 2.0 hat getrennte Konfigurationen für dieselben drei Schritte.</figcaption></figure>

| Eintrag | Was er steuert | Nächste Anleitung |
| --- | --- | --- |
| **TRANSFORMATION (XSLT)** | Wandelt die Quelldaten des Formats in strukturiertes XML um. | [Transformation](edi/edi-transformation-file-guide.md) |
| **PREVIEW (XSLT)** | Definiert die lesbare Dokumentansicht. | [Vorschau](edi/edi-preview-file-guide.md) |
| **EXTRACTION PATHS (JSON)** | Ordnet XML-Werte den DocBits-Feldern und Tabellenspalten zu. | [Extraktionspfade](edi/edi-extraction-paths-file-guide.md) |

Klicken Sie auf eine Zeile, um ihre Versionen und Konfiguration zu sehen. **Default** kennzeichnet den mitgelieferten Eintrag. **Last Modified At** zeigt, wann dieser Eintrag zuletzt geändert wurde. Die Schaltfläche **New** startet einen zusätzlichen Konfigurationseintrag. Das Drei-Punkte-Menü einer Default-Zeile bietet **Customize**, wodurch eine organisationsspezifische Kopie erstellt wird, und **Delete**; prüfen Sie die ausgewählte Zeile sorgfältig, bevor Sie Delete verwenden.

Innerhalb einer Konfiguration erstellt der Stift neben einer aktiven Version einen Entwurf. Prüfen Sie einen Entwurf mit dem Testbereich **Preview** und der ID eines repräsentativen hochgeladenen Dokuments, bevor Sie ihn mit dem Häkchen aktivieren. Das Papierkorb-Symbol eines Entwurfs entfernt diesen Entwurf. Die tatsächlichen Feldnamen und XML-Pfade hängen von Ihrer eSLOG-Datei ab; Details zum Editor finden Sie in der jeweiligen Anleitung oben.
