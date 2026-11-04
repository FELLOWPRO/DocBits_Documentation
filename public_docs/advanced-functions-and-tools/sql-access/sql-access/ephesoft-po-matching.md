# Ephesoft-Bestellabgleich

## Tabelle `public.ephesoft_po_matching`

### Spalten

* `id`: intern
* `org_id`: ID der Organisation
* `doc_id`: intern
* `doc_type`: Dokumenttyp
* `ephesoft_doc_id`: intern
* `extracted_data`: text
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean

### Analyse & Beschreibung

## Technische Dokumentation der Tabelle `public.ephesoft_po_matching`

### Einführung

Die Tabelle `public.ephesoft_po_matching` speichert und verwaltet Daten zum Abgleich von Bestellungen mit Dokumenten, etwa Rechnungen, die vom Ephesoft-System verarbeitet wurden. Die Tabelle erfasst verschiedene Details zu den Dokumenten, deren Extraktionsprozess und dem Abgleichstatus mit Bestellungen.

### Spaltenbeschreibungen

#### id

* **Bedeutung**: Eindeutige Kennung für jeden Datensatz in der Tabelle, die vermutlich ein bestimmtes verarbeitetes Dokument oder eine Transaktion darstellt.
* **Rolle**: Primärschlüssel.
* **Typischer Inhalt**: Universell eindeutige Kennung (UUID) als Zeichenfolge, z. B. `ea587c89-0d4f-4a47-a3ac-89cfb2bed9cb`.

#### org\_id

* **Bedeutung**: Kennung der Organisation, die dem Dokument oder der Transaktion zugeordnet ist.
* **Rolle**: Fremdschlüssel, der möglicherweise auf eine Organisationstabelle verweist.
* **Typischer Inhalt**: UUID als Zeichenfolge, z. B. `23f3d697-7411-4c95-981d-faf089d266be`.

#### doc\_id

* **Bedeutung**: Kennung des vom System verarbeiteten Dokuments.
* **Rolle**: Fremdschlüssel, der auf eine Dokumenttabelle oder Ähnliches verweist.
* **Typischer Inhalt**: UUID als Zeichenfolge, z. B. `f46c6c90-568b-42ee-ae71-c5a3c22211de`.

#### doc\_type

* **Bedeutung**: Typ des verarbeiteten Dokuments, der die Art des Dokuments angibt (z. B. INVOICE).
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Zeichenfolge, die den Dokumenttyp angibt, z. B. `INVOICE`.

#### ephesoft\_doc\_id

* **Bedeutung**: Kennung, die das Ephesoft-System zur Verfolgung des Dokuments verwendet.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Kurze Zeichenfolge, möglicherweise eine Kennung, z. B. `DOC1`.

#### extracted\_data

* **Bedeutung**: JSON-Daten mit aus dem Dokument extrahierten Informationen, einschließlich Feldern, Tabellen und Metadaten.
* **Rolle**: Datenspeicherfeld für extrahierte Dokumentinhalte.
* **Typischer Inhalt**: JSON-Struktur mit Details wie Dokumenttyp, Feldern, Tabellen und Metadaten.

#### created\_by

* **Bedeutung**: Kennung des Benutzers oder Systems, das den Datensatz erstellt hat.
* **Rolle**: Fremdschlüssel, der möglicherweise auf eine Benutzertabelle verweist.
* **Typischer Inhalt**: Ganzzahl, die die Benutzer-ID darstellt, z. B. `1`.

#### created\_on

* **Bedeutung**: Zeitstempel der Erstellung des Datensatzes.
* **Rolle**: Technisches Feld zur Datensatzverfolgung.
* **Typischer Inhalt**: Zeitstempel mit Zeitzone, z. B. `2022-02-19 10:43:37 UTC`.

#### last\_modified\_on

* **Bedeutung**: Zeitstempel der letzten Änderung des Datensatzes.
* **Rolle**: Technisches Feld zur Datensatzverfolgung.
* **Typischer Inhalt**: Zeitstempel mit Zeitzone, kann null sein, wenn seit der Erstellung nicht geändert.

#### is\_deleted

* **Bedeutung**: Kennzeichen, das angibt, ob der Datensatz als gelöscht markiert ist.
* **Rolle**: Technisches Feld für das logische Löschen.
* **Typischer Inhalt**: Boolescher Wert, `true`, wenn der Datensatz gelöscht ist, sonst `false`.
