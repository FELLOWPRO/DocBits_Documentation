---
hidden: true
---

# EDI-Attribute konfigurieren

Wählen Sie das tatsächliche Nachrichtenformat und den Dokumenttyp. Prüfen Sie die vorhandenen Attribute und aktiven Versionen, bevor Sie die Konfiguration ändern.

<figure><img src="../../../../../../.gitbook/assets/site-all-edi-list-de.png" alt="Vorhandenes EDI-Format mit seinen vier konfigurierten Attributen."><figcaption><p>Vorhandenes EDI-Format mit seinen vier konfigurierten Attributen.</p></figcaption></figure>

Definieren Sie Segmente, Elemente und Schleifen in einer JSON-Strukturbeschreibung. Testen Sie repräsentative Nachrichten und prüfen Sie das erzeugte XML-Zwischenformat.

<figure><img src="../../../../../../.gitbook/assets/site-all-edi-detail-de.png" alt="Aktives Attribut STRUCTUREDESCRIPTOR: JSON-Strukturbeschreibung im schreibgeschützten Editor."><figcaption><p>Aktives Attribut STRUCTUREDESCRIPTOR: JSON-Strukturbeschreibung im schreibgeschützten Editor.</p></figcaption></figure>

Ordnen Sie mit TRANSFORMATION-XSLT das XML-Zwischenformat dem benötigten Standard-XML zu. Konfigurieren Sie PREVIEW getrennt für die Darstellung; XSLT verarbeitet dabei nicht unmittelbar JSON.

<figure><img src="../../../../../../.gitbook/assets/site-all-edi-transformation-de.png" alt="Aktives Attribut TRANSFORMATION: XSLT-Quelltext zur Transformation des XML-Zwischenformats."><figcaption><p>Aktives Attribut TRANSFORMATION: XSLT-Quelltext zur Transformation des XML-Zwischenformats.</p></figcaption></figure>

Konfigurieren Sie EXTRACTIONPATHS als JSON mit XPath-Ausdrücken für das resultierende XML. Prüfen Sie Felder, Zeilen und Beträge anhand echter Beispiele. Validieren Sie einen Entwurf vor der Aktivierung; die Bilder zeigen eine vorhandene aktive Konfiguration.

<figure><img src="../../../../../../.gitbook/assets/site-all-edi-extraction-paths-de.png" alt="Aktives Attribut EXTRACTIONPATHS: JSON-Konfiguration mit XPath-Ausdrücken für die Extraktion."><figcaption><p>Aktives Attribut EXTRACTIONPATHS: JSON-Konfiguration mit XPath-Ausdrücken für die Extraktion.</p></figcaption></figure>
