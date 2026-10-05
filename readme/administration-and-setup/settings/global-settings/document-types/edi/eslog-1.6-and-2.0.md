# e-SLOG 1.6 und 2.0

**eSLOG 1.6** und **eSLOG 2.0** erscheinen in DocBits als getrennte elektronische Rechnungsformate. Wählen Sie die Version, die Ihre eingehenden slowenischen Rechnungen verwenden. Die folgenden Bilder zeigen die aktuelle deutsche Sandbox-Oberfläche in einer Dokumentations-Testorganisation; sie belegen nicht, dass eine Rechnung einer der beiden Versionen bereits erfolgreich verarbeitet wurde.

## Die Konfigurationen finden

1. Gehen Sie zu **Einstellungen → Dokumenttypen → Rechnung → E-Doc**.
2. Klappen Sie **E-SLOG 1.6** oder **E-SLOG 2.0** auf. Jedes Format hat eigene drei Einträge.

<figure><img src="../../../../../.gitbook/assets/dbdc-371-eslog-16-de.png" alt="Deutsche Sandbox-Liste des Formats E-SLOG 1.6 mit den Zeilen Transformation, Vorschau und Extraktionspfade"><figcaption>E-SLOG 1.6 in der E-Doc-Liste der Rechnung.</figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/dbdc-371-eslog-20-de.png" alt="Deutsche Sandbox-Liste des Formats E-SLOG 2.0 mit den Zeilen Transformation, Vorschau und Extraktionspfade"><figcaption>E-SLOG 2.0 hat eigene Konfigurationen für dieselben drei Schritte.</figcaption></figure>

| Eintrag | Was er steuert | Nächster Leitfaden |
| --- | --- | --- |
| **TRANSFORMATION (XSLT)** | Wandelt die Quelldaten des Formats in strukturiertes XML um. | [Transformation](edi/edi-transformation-file-guide.md) |
| **PREVIEW (XSLT)** | Definiert die lesbare Dokumentansicht. | [Vorschau](edi/edi-preview-file-guide.md) |
| **EXTRACTION PATHS (JSON)** | Ordnet XML-Werte DocBits-Feldern und Tabellenspalten zu. | [Extraktionspfade](edi/edi-extraction-paths-file-guide.md) |

Klicken Sie auf eine Zeile, um deren Versionen und Konfiguration zu sehen. **Standard** kennzeichnet den mitgelieferten Eintrag. **Zuletzt geändert am** zeigt, wann der Eintrag zuletzt geändert wurde. Die Schaltfläche **Neu** startet einen zusätzlichen Konfigurationseintrag. Das Drei-Punkte-Menü einer Standard-Zeile bietet **Anpassen**, wodurch eine organisationsbezogene Kopie entsteht, und **Löschen**; prüfen Sie die ausgewählte Zeile sorgfältig, bevor Sie **Löschen** verwenden.

Öffnen Sie eine Konfiguration, erstellt das Stift-Symbol neben einer aktiven Version einen Entwurf. Prüfen Sie einen Entwurf mit dem Testbereich **Preview** und einer repräsentativen hochgeladenen Dokument-ID, bevor Sie ihn mit dem Häkchen aktivieren. Das Papierkorb-Symbol eines Entwurfs entfernt diesen Entwurf. Die tatsächlichen Feldnamen und XML-Pfade hängen von Ihrer eSLOG-Datei ab; verwenden Sie den jeweiligen Leitfaden oben für die Einzelheiten im Editor.
