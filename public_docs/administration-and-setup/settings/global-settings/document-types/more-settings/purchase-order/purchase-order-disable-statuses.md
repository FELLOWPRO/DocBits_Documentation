# PO-Deaktivierungsstatus

## **Überblick**

Die Einstellung **PO disable statuses** legt fest, welche Status von Purchase-Order-Zeilen (PO) im Matching-Bildschirm gesperrt sind. Eine Zeile mit einem konfigurierten deaktivierten Status wird durchgestrichen dargestellt und lässt sich nicht auf eine Zuordnung ziehen. Nutzen Sie die Einstellung, um die Matching-Berechtigung für den jeweiligen Dokumenttyp zu steuern.

## **Aktivierungsschritte**

1. Öffnen Sie **Settings → Document Types**.
2. Suchen Sie den Dokumenttyp, den Sie konfigurieren möchten. Das folgende Beispiel verwendet **Invoice**. Öffnen Sie über die Zahnrad-Schaltfläche die **More settings**.

<figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/po-disable-statuses-invoice-card-native-en-20261102.png" alt="Aktueller englischer Kopf der Dokumenttyp-Karte Invoice mit den Steuerelementen Activate und Extraction sowie dem Zahnrad More settings"><figcaption><p>Die vorhandene Invoice-Karte und ihr Zahnrad More settings. Die Steuerelemente Activate und Extraction sind von der PO-Statusauswahl getrennt.</p></figcaption></figure>

3. Öffnen Sie das Accordion **Purchase Order** und suchen Sie **PO disable statuses**.

<figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/po-disable-statuses-field-native-en-20261102.png" alt="Aktuelles englisches Feld PO disable statuses mit Dropdown-Pfeil und der Schaltfläche Apply"><figcaption><p>Das Feld PO disable statuses und seine Schaltfläche Apply. Die hier gezeigte leere Auswahl ist ein Beispiel der bestehenden Testkonfiguration.</p></figcaption></figure>

### **So erkennen Sie eine deaktivierte Purchase Order**

Im [Purchase Order Matching Screen](https://docs.docbits.com/end-user-and-partner-section/end-user-section/purchase-order-matching) wird eine Zeile, deren Status deaktiviert ist, durchgestrichen markiert und kann nicht in eine Zuordnung gezogen werden. Prüfen Sie den Status der Zeile und die Liste der deaktivierten Status des Dokumenttyps, wenn Sie untersuchen, warum die Zeile nicht verfügbar ist.

<figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/po-disabled-row-historical-strike-strokes-masked-20261102.png" alt="Historische Zeile einer stornierten PO mit maskierten Kennungen und Zahlenwerten; die ursprünglichen Durchstreichungen bleiben sichtbar"><figcaption><p>Eine erhaltene historische Zeile einer stornierten PO. Graue Blöcke verdecken Kennungen und Zahlenwerte, einschließlich der zugeordneten Menge. Die kurzen waagerechten Striche erhalten die ursprüngliche Durchstreichung.</p></figcaption></figure>

### **So richten Sie es ein**

1. Klicken Sie auf das Feld **PO disable statuses**, um die verfügbaren Status zu öffnen.
2. Wählen Sie die Kontrollkästchen der Status aus, die Ihr Prozess vom Matching ausschließt. Entfernen Sie ein Kontrollkästchen, um diesen Status aus der Auswahl zu nehmen.

<figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/po-disable-statuses-options-native-en-20261102.png" alt="Aktuelles englisches Dropdown PO disable statuses mit allen elf Status-Kontrollkästchen und der Schaltfläche Apply; der umgebende Seiteninhalt ist maskiert"><figcaption><p>Die aktuellen Statusoptionen mit ihrem bestehenden, nicht angehakten Zustand. Der umgebende Seiteninhalt ist maskiert; das Dropdown und die Schaltfläche Apply sind unverändert.</p></figcaption></figure>

3. Klicken Sie auf **Apply**, um die Auswahl für diesen Dokumenttyp zu speichern. Allein das Öffnen des Dropdowns speichert keine Änderung.

**Available Statuses**

* Canceled
* Deleted
* Invoiced
* Open
* Partially Invoiced
* Partially Received
* Received
* Rejected
* Unapproved
* Hold
* Closed
