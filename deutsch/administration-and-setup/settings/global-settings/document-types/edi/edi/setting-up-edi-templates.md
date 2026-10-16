---
hidden: true
---

# Einrichten von EDI-Vorlagen

## Hier sind Schritt-für-Schritt-Anleitungen zum Einrichten von EDI-Vorlagen:

<figure><img src="../../../../../../.gitbook/assets/docbits_sso_cert_metadata.png" alt="Docbits Sso Cert Metadata"><figcaption></figcaption></figure>

**Definieren Sie den Strukturbeschreiber:**

* Identifizieren Sie den Typ der EDI-Nachricht, mit der Sie arbeiten, z. B. ANSI X12, EDIFACT oder ein benutzerdefiniertes Format.
* Bestimmen Sie die Segmente, Elemente und Subelemente innerhalb der EDI-Struktur.
* Erstellen Sie einen Strukturbeschreiber, der die Hierarchie und Organisation der EDI-Nachricht genau widerspiegelt. Dies kann mit einer speziellen Syntax wie XML oder JSON erfolgen.

<figure><img src="../../../../../../.gitbook/assets/docbits_sso_access_settings.png" alt="Docbits Sso Access Settings" width="273"><figcaption></figcaption></figure>

**Richten Sie Transformationen ein:**

* Verwenden Sie ein geeignetes Tool oder eine Software, die EDI-Transformationen unterstützt, wie z. B. einen EDI-Übersetzer.
* Definieren Sie die Regeln für die Konvertierung der EDI-Nachricht in das interne Format Ihres Systems und umgekehrt.
* Konfigurieren Sie die Transformationen, um Segmente, Elemente und Subelemente gemäß den Anforderungen Ihres Systems zu interpretieren und zu verarbeiten. Testen Sie die Transformationen gründlich, um sicherzustellen, dass die Daten korrekt interpretiert und formatiert werden.

<figure><img src="../../../../../../.gitbook/assets/docbits_sso_idp_config.png" alt="Docbits Sso Idp Config" width="268"><figcaption></figcaption></figure>

**Konfigurieren Sie Extraktionspfade für eine optimale Datenextraktion und -formatierung:**

* Identifizieren Sie die Datenfelder, die extrahiert und an Ihr internes System übertragen werden sollen.
* Definieren Sie Extraktionspfade oder Regeln, um die relevanten Datenfelder aus den EDI-Nachrichten zu extrahieren.
* Berücksichtigen Sie die verschiedenen Variationen und Formate, die in den eingehenden EDI-Nachrichten auftreten können, und stellen Sie sicher, dass die Extraktionspfade flexibel genug sind, um diese zu berücksichtigen.
* Validieren Sie die Extraktionsergebnisse, um sicherzustellen, dass die richtigen Datenfelder extrahiert und korrekt formatiert werden.

<figure><img src="../../../../../../.gitbook/assets/docbits_edi_validate_extraction.png" alt="Docbits Edi Validate Extraction" width="92"><figcaption></figcaption></figure>

Durch die sorgfältige Definition des Strukturbeschreibers, das Einrichten von Transformationen und die Konfiguration von Extraktionspfaden können Sie sicherstellen, dass die Datenextraktion und -formatierung in Ihren EDI-Vorlagen optimal durchgeführt werden. Dies trägt dazu bei, die Effizienz und Genauigkeit Ihrer elektronischen Geschäftskommunikation zu verbessern.
