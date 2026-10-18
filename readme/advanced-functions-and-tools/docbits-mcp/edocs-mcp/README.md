# eDocs MCP

Die DocBits-API stellt einen **Model Context Protocol (MCP)**-Server mit Tools bereit, um die Verarbeitung elektronischer Dokumente (eDocs) einzusehen und anzupassen. Jeder MCP-kompatible Client – Claude Code, Claude Desktop oder benutzerdefinierte Integrationen – kann sich verbinden und diese Tools verwenden.

## Was können Sie tun?

Mit den eDocs-MCP-Tools können Sie:

- **Einsehen**, wie jeder Typ eines elektronischen Dokuments klassifiziert wird und welche Extraktionsregeln gelten
- **Testen**, wie Dokumente die gesamte Verarbeitungspipeline durchlaufen, ohne in der Datenbank zu speichern
- **Benutzerdefinierte Regeln erstellen** für Ihre Organisation – XSLT-Vorschauen, Extraktionspfade, Transformationen
- Eine benutzerdefinierte Regel **aktualisieren** mit einer neuen Version (mit oder ohne sofortige Aktivierung)
- Eine benutzerdefinierte Regel **löschen**, um zum integrierten Standard zurückzukehren
- **Verifizieren**, dass alle unterstützten eDoc-Fixtures korrekt verarbeitet werden

## Berechtigungsmodell

DocBits wird mit einer Bibliothek integrierter Standardregeln ausgeliefert, die alle Kunden gemeinsam nutzen. Diese Standardregeln verwenden die reservierte Organisations-ID `00000000-0000-0000-0000-000000000000`.

**Die Standardregeln sind über MCP unveränderlich.** Jedes Schreib-Tool prüft Ihre Organisations-ID, bevor es eine Anfrage stellt. Wird sie als Standardorganisation aufgelöst, wird die Operation sofort abgelehnt – es wird nie ein API-Aufruf ausgeführt.

Kunden können Regeln nur **innerhalb ihrer eigenen Organisation** erstellen, ändern oder löschen. Existiert für Ihre Organisation eine benutzerdefinierte Regel, hat sie Vorrang vor dem Standard. Das Löschen einer benutzerdefinierten Regel stellt das Standardverhalten automatisch wieder her.

```
Your org rule  ──► used if present
      │
      ▼ (if absent)
Default rule   ──► built-in, immutable via MCP
```

## Tools-Übersicht

### Einsicht (schreibgeschützt)

| Tool | Beschreibung |
|------|-------------|
| `test_electronic_document` | Trockenlauf der gesamten eDoc-Pipeline – Klassifizierung, Extraktion, Vorschau – ohne zu speichern |
| `list_electronic_document_types` | Alle unterstützten eDoc-Typen mit Konfigurationsstatus auflisten |
| `get_extraction_rules` | Die XPath-Regeln anzeigen, die zum Extrahieren der Felder eines bestimmten Dokumenttyps verwendet werden |
| `get_extracted_fields` | Aus einem verarbeiteten Dokument extrahierte Kopffelder abrufen |
| `get_extracted_tables` | Aus einem verarbeiteten Dokument extrahierte Positionen abrufen |
| `get_preview_pdf` | Das per XSLT gerenderte Vorschau-PDF eines Dokuments abrufen |
| `get_preview_image` | Ein gerendertes Seitenbild eines verarbeiteten Dokuments abrufen |
| `extract_edoc_table` | Eine übergebene XML-/EDI-Datei extrahieren und die Felder als flache Tabelle zusammen mit der Regel zurückgeben, die jedes Feld erzeugt hat |
| `compare_edoc_extraction` | Die Standard- und Ihre benutzerdefinierte Extraktion (und optional eine Kandidatenregel) an einem Dokument vergleichen |

### Anpassung (auf die Organisation beschränkt, Standardorganisation gesperrt)

| Tool | Beschreibung |
|------|-------------|
| `list_edoc_custom_attributes` | Die benutzerdefinierten Überschreibungen Ihrer Organisation im Vergleich zu den integrierten Standards für einen Dokumenttyp auflisten |
| `create_edoc_custom_attribute` | Eine neue benutzerdefinierte Regel erstellen (EXTRACTION_PATHS, TRANSFORMATION oder PREVIEW) |
| `update_edoc_custom_attribute` | Eine neue Version einer benutzerdefinierten Regel hinzufügen, optional mit sofortiger Aktivierung |
| `delete_edoc_custom_attribute` | Eine benutzerdefinierte Regel löschen – das System fällt automatisch auf den Standard zurück |
| `preview_edoc_custom_xslt` | Eine XSLT-Transformation vor der Aktivierung im Trockenlauf gegen ein XML-Dokument prüfen |
| `get_edoc_attribute_source` | Den bearbeitbaren Quelltext eines Attributs (PREVIEW, EXTRACTION_PATHS, TRANSFORMATION) abrufen, um ihn zu ändern |
| `list_edoc_attribute_versions` | Versionsverlauf eines benutzerdefinierten Attributs: Entwürfe und die aktive Version |
| `activate_edoc_attribute_version` | Eine bestimmte Version oder einen Entwurf aktivieren (so führen Sie einen Rollback durch) |
| `delete_edoc_attribute_draft` | Einen Entwurf löschen, der nie aktiviert wurde |

### Verifizierung

| Tool | Beschreibung |
|------|-------------|
| `verify_electronic_documents` | Fixtures hochladen und Klassifizierung, Extraktion und Vorschau durchgängig verifizieren |
| `validate_all_edocs` | Alle eDoc-Fixtures im Trockenlauf durch die Pipeline schicken und Probleme melden |

## Attributtypen

Jede anpassbare Regel hat einen bestimmten Typ und ein bestimmtes Format:

| Attributname | Format | Zweck |
|----------------|--------|---------|
| `EXTRACTION_PATHS` | JSON | XPath-Ausdrücke, die XML-Knoten DocBits-Feldern zuordnen |
| `TRANSFORMATION` | XSLT | Stylesheet, das vor der Extraktion auf das XML angewendet wird |
| `PREVIEW` | XSLT | Stylesheet, das die menschenlesbare PDF-Vorschau rendert |
| `STRUCTURE_DESCRIPTOR` | JSON | Strukturzuordnung nur für EDI-Dokumente |

Das Tool `create_edoc_custom_attribute` leitet das richtige Format automatisch aus dem Attributnamen ab.

## Schnellstart

### Auflisten, was Ihre Organisation angepasst hat

```
list_edoc_custom_attributes
  electronic_document_type: "XRECHNUNG 2.1 CII"
```

Liefert zwei Listen: `custom` (die Überschreibungen Ihrer Organisation) und `default` (gemeinsame Regeln, die Sie erben).

### Eine benutzerdefinierte Vorschau für XRechnung erstellen

```
create_edoc_custom_attribute
  electronic_document_type: "XRECHNUNG 2.1 CII"
  attribute_name: "PREVIEW"
  attribute_value: "<xsl:stylesheet ...>...</xsl:stylesheet>"
```

Liefert die neue `attribute_id` – speichern Sie sie für Aktualisierungen und das Löschen.

### Eine bestehende benutzerdefinierte Regel aktualisieren

```
update_edoc_custom_attribute
  attribute_id: "069cd17c-673c-7c94-8000-b512417eefe3"
  new_value: "<xsl:stylesheet ...>...</xsl:stylesheet>"
  activate: true
```

Erstellt eine neue Version und aktiviert sie. Die vorherige Version bleibt im Verlauf erhalten.

### Zum Standard zurückkehren

```
delete_edoc_custom_attribute
  attribute_id: "069cd17c-673c-7c94-8000-b512417eefe3"
```

Entfernt die benutzerdefinierte Überschreibung. Das System fällt sofort auf die integrierte Standardregel zurück.

## Sicherheitsregeln

| Aktion | Erlaubt |
|--------|---------|
| Standardregeln lesen | ✅ Ja |
| Benutzerdefinierte Regel für Ihre Organisation erstellen | ✅ Ja |
| Benutzerdefinierte Regel für Ihre Organisation aktualisieren | ✅ Ja |
| Benutzerdefinierte Regel für Ihre Organisation löschen | ✅ Ja |
| Standardregeln ändern oder löschen | ❌ **Nie** – auf MCP-Ebene gesperrt |

Der Versuch, in `00000000-0000-0000-0000-000000000000` zu schreiben, liefert:

```json
{
  "error": true,
  "blocked": true,
  "detail": "Writing to the default org is forbidden via MCP. Default rules are immutable and shared across all customers."
}
```

[DocBits mit Claude oder Codex konfigurieren](../configuration-with-claude-or-codex.md): Verbindung, kopierbare Prompts, Vorschauen, versionierte Änderungen, Prüfungen und Rückkehr.
