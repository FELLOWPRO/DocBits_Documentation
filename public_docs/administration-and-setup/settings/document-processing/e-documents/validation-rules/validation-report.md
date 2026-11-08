# Prüfbericht

> Einzelne Produkttexte können in dieser Version noch Englisch oder sprachlich fehlerhaft sein. Die Anleitung erklärt die Bedeutung; die Screenshots zeigen die unveränderte Oberfläche.

Wenn DocBits eine E-Rechnung ablehnt, können Sie genau nachlesen, warum. Der **Prüfbericht** listet jeden Prüfhinweis in verständlicher Sprache auf, sagt Ihnen, was zu korrigieren ist, und zeigt den nächsten Schritt. Sie öffnen ihn am Dokument, nicht in den Einstellungen. Die Ansicht, in der Sie ihn finden, ist beschrieben unter [Die Fehleransicht einer abgelehnten E-Rechnung](validation-error-screen.md).

Diese Seite richtet sich an Personen, die Rechnungen bearbeiten. Administratoren legen die Regeln auf der Seite [E-Rechnungs-Prüfung](./) fest und wählen je Dokumenttyp, ob eine fehlgeschlagene Prüfung die Rechnung blockiert, siehe [Prüfung je Dokumenttyp](validation-per-document-type.md).

## Wann ein Dokument den Status „Fehler" erhält

Ist die Prüfung für den Dokumenttyp **aktiviert** und **blockierend**, erhält eine Rechnung mit einem blockierenden Prüfhinweis den Status **Error**. Öffnen Sie das Dokument über das Dashboard. Die Fehleransicht zeigt links das XML und rechts den Grund.

<figure><img src="../../../../../.gitbook/assets/einvoice-error-view-de.png" alt="Die Fehleransicht: das XML der Rechnung und der erste blockierende Prüfhinweis mit einem nächsten Schritt. Beispielrechnung mit fiktiven Namen."><figcaption><p>Die Fehleransicht: das XML der Rechnung und der erste blockierende Prüfhinweis mit einem nächsten Schritt. Beispielrechnung mit fiktiven Namen.</p></figcaption></figure>

Die Karte rechts nennt die Ebene, die die Rechnung abgelehnt hat (zum Beispiel **L3 · Business Rules**), den Regelcode (zum Beispiel `BR-CO-26`), eine kurze Erklärung und einen **Next step**. Wählen Sie **View validation details**, um den vollständigen Bericht zu öffnen.

## Den Bericht lesen

<figure><img src="../../../../../.gitbook/assets/einvoice-report-top-de.png" alt="Prüfbericht der synthetischen Beispielrechnung mit Dateiangaben und Prüfergebnis."><figcaption><p>Prüfbericht der synthetischen Beispielrechnung mit Dateiangaben und Prüfergebnis.</p></figcaption></figure>

Der Bericht beginnt mit den Fakten zur Datei:

| Feld | Was es zeigt |
| --- | --- |
| **Reference** | Der Dateiname der Rechnung. |
| **Time of check** | Wann DocBits die Prüfung ausgeführt hat. Ein gespeicherter Bericht ändert sich später nicht. |
| **Document type / profile** | Das Format der Rechnung, zum Beispiel CII und EN 16931. |
| **Rule sets** | Die Version der Regelwerke, die DocBits verwendet hat. |
| **Seller** | Der Verkäufer, aus dem XML gelesen. |
| **Number / date** | Die Rechnungsnummer und das Rechnungsdatum, aus dem XML gelesen. |

Unter den Dateiangaben sehen Sie das **Ergebnis**, zum Beispiel **Not conformant**, mit der Anzahl der Fehler, Warnungen und Informationen. Hat Ihre Organisation den Schweregrad einer Regel geändert, zeigt eine zweite Angabe **Organisation severity** die Anzahlen nach den Einstellungen Ihrer Organisation.

### Ergebnis je Ebene

Die Tabelle **Result per level** zeigt, wie viele Fehler, Warnungen und Hinweise jede Prüfung gefunden hat. Die Prüfungen bauen aufeinander auf:

| Ebene | Was geprüft wird |
| --- | --- |
| **1 Syntax** | Das XML ist wohlgeformt. |
| **2 Schema** | Die Struktur entspricht dem offiziellen XML-Schema. |
| **3 Business rules** | Pflichtfelder sind vorhanden und korrekt (Regeln `BR-…`). |
| **4 Cross-check rules** | Felder stimmen miteinander überein, zum Beispiel Summen. |
| **5 CIUS rules (XRechnung)** | Die zusätzlichen deutschen XRechnung-Regeln. |
| **Other rules** | Weitere Regeln, zum Beispiel die PEPPOL-Regeln. |
| **Value checks of DocBits** | Prüfungen, die DocBits ergänzt, zum Beispiel IBAN und USt-IdNr. |

> Bei Rechnungen im Profil EN 16931 oder EXTENDED werden die XRechnung-spezifischen Regeln als **Warnungen** angezeigt, nicht als Fehler.

## Die Prüfhinweise

<figure><img src="../../../../../.gitbook/assets/einvoice-report-findings-de.png" alt="Jeder Prüfhinweis hat einen Code, eine Ebene, einen lesbaren Text und einen Hinweis zur Behebung"><figcaption><p>Jeder Prüfhinweis hat einen Code, eine Ebene, einen lesbaren Text und einen Hinweis zur Behebung</p></figcaption></figure>

Jeder Prüfhinweis ist eine Zeile im Abschnitt **Pos**:

* **Pos** und **Code**: die Position im Bericht und der Regelcode, zum Beispiel `BR-CO-26`.
* **Level**: **Error**, **Warning** oder **Information**.
* **Your organisation**: der Schweregrad nach den Einstellungen Ihrer Organisation. Ein Strich bedeutet, dass Ihre Organisation den Schweregrad nicht geändert hat.
* **Field and text**: das Problem in verständlicher Sprache, das betroffene Feld (zum Beispiel *BT-29*), die **Technische Meldung** des Validators und **How to fix**.
* **Line** und **Show in XML**: Wählen Sie **Show in XML**, um den Bericht zu schließen und zur Zeile im XML-Viewer zu springen.

DocBits hat verständliche Texte für die häufigsten Regeln. Für eine Regel ohne einen solchen Text zeigt der Bericht die technische Meldung des Validators.

## Weiter

* [Nächster Schritt und Dokument ablehnen](validation-next-step-and-reject.md): was Sie nach dem Lesen des Berichts tun.

## Verwandte Seiten

* [E-Rechnungs-Prüfung](./): akzeptierte Versionen, Profile und der Schweregrad jeder Regel.
* [Prüfung je Dokumenttyp](validation-per-document-type.md): Prüfung aktivieren und Blockieren festlegen.
* [Benachrichtigungsrouting](../notification-routing.md): wer welchen Prüfhinweis bearbeitet.
