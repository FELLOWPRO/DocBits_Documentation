---
description: MYINVOIS elektronische Dokumentenunterstützung in DocBits
---

# 🇲🇾 MYINVOIS

<!-- edocs-country-scope -->

{% hint style="info" %}
Die Länderanleitung enthält Versionsgrenzen, die tatsächlich verwendete Konfiguration und das Erklärvideo zum Land. [Malaysia](countries/malaysia.md). Der geprüfte Extraktionspfad ist XML-basiert. Die nationale Plattform akzeptiert auch JSON. Das belegt jedoch keine JSON-Importunterstützung in dieser DocBits-Zuordnung.
{% endhint %}

| Eigenschaft          | Wert                                                              |
| -------------------- | ----------------------------------------------------------------- |
| **Land / Region**    | Malaysia                                                          |
| **Dokumenttypen**    | Rechnung, Gutschrift, Belastungsanzeige, Selbstfakturierte Rechnung |
| **Format**           | UBL 2.1 XML                                                |
| **Standard**         | MyInvois (LHDN - Lembaga Hasil Dalam Negeri)                      |

MyInvois ist Malaysias E-Invoicing-System, das von der Steuerbehörde (Inland Revenue Board, LHDN) betrieben wird. Seit August 2024 für Großunternehmen gültig, müssen alle Rechnungen zur Validierung an das MyInvois-Portal übermittelt werden und erhalten dort eine eindeutige Kennung. Das System verwendet UBL 2.1 und unterstützt sowohl XML- als auch JSON-Übermittlungsformate.

## Unterstützungsstatus

| Komponente       | Status         |
| ---------------- | -------------- |
| Vorschau         | ✅ Unterstützt |
| Feldextraktion   | ✅ Unterstützt |
| Transformation   | ✅ Unterstützt |

## Standard-Vorschau

<figure><img src="../../../../../../.gitbook/assets/myinvois-preview.png" alt="MyInvois-Rechnungsvorschau in DocBits"><figcaption><p>Standard-DocBits-Vorschau für eine malaysische MyInvois-Rechnung</p></figcaption></figure>

## Verwandte Seiten

* [Unterstützte elektronische Dokumente](./)
