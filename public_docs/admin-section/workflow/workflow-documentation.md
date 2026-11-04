# Workflow-Dokumentation

**Workflow-Dokumentation**

Um den Überblick zu behalten, können Sie den Workflows verschiedene Überschriften geben, damit Sie sofort wissen, um welche Aufgabe es sich bei diesem Workflow handelt.

Erstellen Sie einen neuen Workflow: Klicken Sie auf + WORKFLOW HINZUFÜGEN

![](<../../.gitbook/assets/0 (1).png>)

Sie können diese Workflows (Test 1,2,3) verwenden, um verschiedene Dokumente automatisch dem richtigen Mitarbeiter im Unternehmen zuzuweisen.

![](<../../.gitbook/assets/1 (1).png>)

Wenn eine Rechnung oder ein anderes Dokument einen bestimmten Gesamtbetrag überschreitet, der eine vorherige Überprüfung und Genehmigung erfordert, können diese Dokumente sofort der richtigen Person zugewiesen werden.

<figure><img src="../../.gitbook/assets/docbits_export_sftp.png" alt="DocBits Export Sftp"><figcaption></figcaption></figure>

**Test 1:              Logik-Karte**

Wenn:             **Zuständiger ist:**                    Amier Haider

Und:                **Dokumententyp ist:**        Rechnung

Dann:              **Dokument zuweisen an:**   Stefan Reppermund

![](<../../.gitbook/assets/3 (1).png>)

**Test 2:              Logik-Karte**

Wenn:              **Zuständiger ist:**                    Amier Haider

Und:                 **Dokumententyp ist:**        Lieferschein

Dann:               **Dokument zuweisen an:**   James Edwards

![](<../../.gitbook/assets/4 (1).png>)

**Test 3:             Logik-Karte**

**Wenn:**             **Zuständiger ist:**                    Amier Haider

**Und:**                **Dokumententyp ist:**        Auftragsbestätigung

**Dann:**              **Dokument zuweisen an:**   Anian Sollinger

![](<../../.gitbook/assets/5 (1).png>)





Es ist auch möglich, wenn das Dokument nicht einer einzelnen Person zugewiesen ist, es von Anfang an einem bestimmten Mitarbeiter zuzuweisen.

<figure><img src="../../.gitbook/assets/docbits_db_access_creation.png" alt="Docbits Db Access Creation" width="375"><figcaption></figcaption></figure>





Für einen einfacheren Überblick darüber, was mit einem Dokument geschehen soll, können Sie den Status für eingehende Dokumente in diesem Workflow festlegen. Dieser Workflow ermöglicht es sofort zu sehen, ob beispielsweise eine Genehmigung aussteht.



**Test 4:             Logik-Karte**

**Wenn:**             **Dokumententyp ist:**         Lieferschein

**Und:**                **Zuständiger ist:**                     Amier Haider

**Dann:**              **Status ändern zu:**         Ausstehende Genehmigung

<figure><img src="../../.gitbook/assets/docbits_export_smb.png" alt="DocBits Export Smb"><figcaption></figcaption></figure>

![](<../../.gitbook/assets/8 (1).png>)



**Test 5:                Logik-Karte**

Wenn:                **Dokumententyp ist:**           Rechnung

Und:                   **Zuständiger ist:**                       Stefan Reppermund

Dann:                 **Status ändern zu:**           Ausstehende zweite Genehmigung

<figure><img src="../../.gitbook/assets/docbits_workflow_test_9_replacement.png" alt="Docbits Workflow Test 9 Replacement"><figcaption></figcaption></figure>

![](<../../.gitbook/assets/10 (1).png>)





Wenn eine Rechnung oder ein anderes Dokument einen bestimmten Gesamtbetrag überschreitet, der eine vorherige Überprüfung und Genehmigung erfordert, können diese Dokumente sofort der richtigen Person zugewiesen werden.

![](<../../.gitbook/assets/11 (1).png>)



**Test 6:                    Logik-Karte**

Wenn:                   **Zuständiger ist:**                   Amier Haider

Und:                      Feld        **total\_amount**     ist      **Größer als       500**

Dann:                    **Dokument zuweisen an:**   Asad Usman Khan

<figure><img src="../../.gitbook/assets/image (8) (1).png" alt=""><figcaption></figcaption></figure>

![](<../../.gitbook/assets/13 (1).png>)



Es ist auch möglich, den Status in den Workflow einzugeben, damit die zugewiesene Person sofort sehen kann, welchen Status dieses Dokument hat und was als nächstes damit geschehen soll.



**Test 7:                 Logik-Karte**

**Wenn:** **Zuständiger ist:**                     Amier Haider

**Und:**                   Feld           **total\_amount**      ist        **Größer als      500**

**Dann:**                 **Dokument zuweisen an:**     Asad Usman Khan

&#x20;                            **Status ändern zu:**          Ausstehende Genehmigung

<figure><img src="../../.gitbook/assets/docbits_approval_2.png" alt="Genehmigung Übersicht"><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/docbits_workflow_purchase_order_2.png" alt="Workflow Bestellung Import Übersicht"><figcaption></figcaption></figure>





Wenn beispielsweise bestimmte oder wichtige Informationen in einem Dokument fehlen, aber wichtig sind und für die weitere Bearbeitung enthalten sein müssen, können Sie den Workflow so einrichten, dass diese Dokumente sofort an den Käufer und einen Vertreter weitergeleitet werden.

<figure><img src="../../.gitbook/assets/docbits_workflow_5.png" alt="Workflow Übersicht"><figcaption></figcaption></figure>



**Test 9:**

Der Workflow mit diesen Logikkarten ist darauf ausgelegt, automatisch zu überprüfen, ob die Menge, der Stückpreis oder der Rabatt, die in einer Auftragsbestätigung angegeben sind, mit den entsprechenden Zahlen im Kaufauftrag übereinstimmen. Diese Überprüfung gewährleistet Konsistenz und Genauigkeit zwischen dem Bestellten und dem, was der Lieferant bestätigt zu liefern.

Sie können diesen Dokumenten einen spezifischen Status geben oder sie einem bestimmten Mitarbeiter zuweisen.

<div align="center">

<figure><img src="../../.gitbook/assets/docbits_approval_permission.png" alt="Genehmigung Berechtigung Übersicht"><figcaption></figcaption></figure>

</div>

<figure><img src="../../.gitbook/assets/docbits_purchase_order_4.png" alt="Bestellung Übersicht"><figcaption></figcaption></figure>

**Logik-Karte: Menge oder Stückpreis oder Rabatt stimmen überein**

Diese Logikkarte ist darauf ausgelegt, automatisch zu überprüfen, ob die Menge, der Stückpreis oder der Rabatt, die in einer Auftragsbestätigung angegeben sind, mit den entsprechenden Zahlen im Kaufauftrag übereinstimmen. Diese Überprüfung gewährleistet Konsistenz und Genauigkeit zwischen dem Bestellten und dem, was der Lieferant bestätigt zu liefern.



**Auslösebedingung**

Die Logik wird aktiviert, wenn eine der folgenden Bedingungen in einer Auftragsbestätigung im Vergleich zum ursprünglichen Kaufauftrag erfüllt ist:

* **Menge**: Die bestellte Menge an Artikeln entspricht der vom Lieferanten bestätigten Menge.
* **Stückpreis**: Der vereinbarte Preis pro Artikel entspricht der Bestätigung des Lieferanten.
* **Rabatt**: Angewendete Rabatte stimmen zwischen dem Kaufauftrag und der Auftragsbestätigung überein.



* **Vergleichsparameter definieren**: Legen Sie die spezifischen Felder (Menge, Stückpreis, Rabatt) fest, die die Logikkarte auf Übereinstimmung überprüfen wird.
* **Automatisierte Überprüfung**: Konfigurieren Sie das System so, dass es diese Details automatisch vergleicht, sobald eine Auftragsbestätigung eingeht.
* **Benutzerdefinierte Benachrichtigungen**: Entscheiden Sie über den Workflow zur Behandlung von Abweichungen, einschließlich der Anpassung von Benachrichtigungen für manuelle Überprüfung.

Diese Logikkarte ist entscheidend, um sicherzustellen, dass die Details einer Auftragsbestätigung mit dem ursprünglichen Kaufauftrag übereinstimmen und die Integrität des Beschaffungszyklus gewährleisten.



**Test 10:**

Wenn Sie eine andere Berechnung für Zuschläge haben oder diese nur bei einigen Artikeln haben, können Sie die generischen Tabellenberechnungskarten verwenden, einige von ihnen ermöglichen auch das Filtern nach regulären Ausdrücken.

<figure><img src="../../.gitbook/assets/docbits_table_invoice.png" alt="Tabelle Rechnung Übersicht"><figcaption></figcaption></figure>

Oben ist ein Berechnungsbeispiel für MTZ mit einem Filter für Artikelnummern, die mit 01, 06, 9, 001 oder 000 beginnen.



Bei einer manuellen Einrichtung wird empfohlen, Berechnungen, die von neuen Spalten abhängen, in einem separaten Workflow aufzuteilen. Um mit der Berechnung fortzufahren, können Sie die Karte "Workflow ausführen" verwenden.

**Workflow ausführen**

<figure><img src="../../.gitbook/assets/docbits_workflow_2.png" alt="Workflow Übersicht"><figcaption></figcaption></figure>

Mit dieser Karte können Sie den Namen eines Workflows angeben, der nach dem aktuellen Workflow ausgeführt werden soll, wenn seine Bedingungen erfüllt sind und nach den vorherigen "Dann"-Karten des aktuellen Workflows. Während es ausführbare, aktive Workflows priorisiert, ermöglicht es auch, deaktivierte Workflows auszuführen, wenn das Dokument die Bedingungen der Workflows erfüllt.
### **Hinzufügen von berechneten Zuschlägen in eine vorhandene Spalte** <a href="#pekg4i18rshn" id="pekg4i18rshn"></a>

<figure><img src="https://lh7-us.googleusercontent.com/XYY1xsFpp7_-Bi0WOSbotiVzspDLdaufx_xgoopMHmxdZnSDhroLpb0AE_si5PhwMq1jHfndc9FwOte9MOoCoTP5_JUYawO5cr4uIctIDHmwVjz3KacQrLJd8iBQy5KY4N-dMaWEi3IeTcc5OBRNJk4" alt=""><figcaption></figcaption></figure>

Wenn Sie alle Zuschläge als negativen Rabatt in die Rabattspalte einfügen möchten, können Sie die Berechnungskarte verwenden. Es können Einträge in dieser Spalte vorhanden sein. Sie können es als eine der Variablen auf der Karte festlegen, von dieser den MTZ abziehen und das Ergebnis wieder in diese Spalte einfügen. Falls leere Felder vorhanden sind (nur Zuschläge für einige Artikel), wird für die Berechnung davon ausgegangen, dass es sich um eine 0 handelt.

**Benutzer benachrichtigen, um die Auftragsbestätigung in DocBits zu autorisieren**

Nachdem Sie die Zuschläge berechnet haben, möchten Sie möglicherweise einen bestimmten Benutzer benachrichtigen, um die Auftragsbestätigung zu autorisieren. Hierfür können Sie die Benachrichtigungskarte verwenden.

<figure><img src="../../.gitbook/assets/docbits_settings_email.png" alt="Einstellungen E-Mail Import Bestellung Tabelle Übersicht"><figcaption></figcaption></figure>

Je nach Einstellungen wird dem Benutzer eine neue Aufgabe in DocBits zugewiesen und optional eine E-Mail gesendet, um ihn über seine neue Aufgabe zu informieren.
