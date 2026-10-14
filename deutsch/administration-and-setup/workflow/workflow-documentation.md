# Zuweisung & Status — Praxisbeispiele

Um den Überblick zu behalten, können Sie den Workflows verschiedene Überschriften geben, damit Sie sofort erkennen, worum es bei diesem Workflow geht.

Erstellen Sie einen neuen Workflow: Klicken Sie auf + ADD WORKFLOW

![](<../../.gitbook/assets/workflow_add_button.png>)

Sie können diese Workflows (Test 1, 2, 3) verwenden, um verschiedene Dokumente automatisch dem richtigen Mitarbeiter im Unternehmen zuzuweisen.

![](<../../.gitbook/assets/workflow_list_overview.png>)

Wenn eine Rechnung oder ein anderes Dokument einen bestimmten Gesamtbetrag überschreitet, der eine vorherige Prüfung und Genehmigung erfordert, können diese Dokumente sofort der richtigen Person zugewiesen werden.

<figure><img src="../../.gitbook/assets/workflow_amount_check.png" alt="Workflow Amount Check"><figcaption></figcaption></figure>

**Test 1: Logic Card**

When: **Assignee is:** Amier Haider

And: **Document type is:** Invoice

Then: **Assign document to:** Stefan Reppermund

![](<../../.gitbook/assets/3 (1).png>)

**Test 2: Logic Card**

When: **Assignee is:** Amier Haider

And: **Document type is:** Delivery Note

Then: **Assign document to:** James Edwards

![](<../../.gitbook/assets/4 (1).png>)

**Test 3: Logic Card**

**When:** **Assignee is:** Amier Haider

**And:** **Document type is:** Order Confirmation

**Then:** **Assign document to:** Anian Sollinger

![](<../../.gitbook/assets/5 (1).png>)

Es ist auch möglich, ein Dokument von Anfang an einem bestimmten Mitarbeiter zuzuweisen, wenn es nicht einer einzelnen Person zugeordnet ist.

<figure><img src="../../.gitbook/assets/workflow_assign_to_employee_start.png" alt="Workflow Assign to Employee Start" width="375"><figcaption></figcaption></figure>

Für eine einfachere Übersicht darüber, was mit einem Dokument geschehen soll, können Sie in diesem Workflow den Status für eingehende Dokumente festlegen. Dieser Workflow ermöglicht es, sofort zu erkennen, ob beispielsweise eine ausstehende Genehmigung vorliegt.

**Test 4: Logic Card**

**When:** **Document type is:** Delivery Note

**And:** **Assignee is:** Amier Haider

**Then:** **Change Status to:** Pending Approval

<figure><img src="../../.gitbook/assets/workflow_test4_delivery_note_status.png" alt="Workflow Test 4 Delivery Note Status"><figcaption></figcaption></figure>

![](<../../.gitbook/assets/8 (1).png>)

**Test 5: Logic Card**

When: **Document type is:** Invoice

And: **Assignee is:** Stefan Reppermund

Then: **Change Status to:** Pending Second Approval

<figure><img src="../../.gitbook/assets/workflow_test5_invoice_approval_status.png" alt="Workflow Test 5 Invoice Approval Status"><figcaption></figcaption></figure>

![](<../../.gitbook/assets/10 (1).png>)

Wenn eine Rechnung oder ein anderes Dokument einen bestimmten Gesamtbetrag überschreitet, der eine vorherige Prüfung und Genehmigung erfordert, können diese Dokumente sofort der richtigen Person zugewiesen werden.

![](<../../.gitbook/assets/11 (1).png>)

**Test 6: Logic Card**

When: **Assignee is:** Amier Haider

And: Docfield **total\_amount** is **Greater than 500**

Then: **Assign document to:** Asad Usman Khan

<figure><img src="../../.gitbook/assets/workflow_test6_total_amount_assign.png" alt="Workflow Test 6 Total Amount Assign"><figcaption></figcaption></figure>

![](<../../.gitbook/assets/13 (1).png>)

Es ist auch möglich, den Status in den Workflow einzutragen, sodass die zugewiesene Person sofort erkennen kann, welchen Status dieses Dokument hat und was als Nächstes damit geschehen soll.

**Test 7: Logic Card**

**When:** **Assignee is:** Amier Haider

**And:** Docfield **total\_amount** is **Greater then 500**

**Then:** **Assign document to:** Asad Usman Khan

**Change Status to:** Pending Approval

<figure><img src="../../.gitbook/assets/workflow_test7_status_update.png" alt="Workflow Test 7 Status Update"><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/15 (1).png" alt=""><figcaption></figcaption></figure>

Wenn beispielsweise bestimmte oder wichtige Informationen in einem Dokument fehlen, die aber für die weitere Verarbeitung wichtig sind und enthalten sein müssen, können Sie den Workflow so einrichten, dass diese Dokumente sofort an den Einkäufer und einen Stellvertreter (Ersatz) weitergeleitet werden.

<figure><img src="../../.gitbook/assets/workflow_test8_missing_info.png" alt="Workflow Test 8 Missing Info"><figcaption></figcaption></figure>

**Test 9:**

Der Workflow mit diesen Logic Cards ist darauf ausgelegt, automatisch zu überprüfen, ob die in einer Auftragsbestätigung angegebene Menge, der Stückpreis oder der Rabatt mit den entsprechenden Angaben in der Bestellung übereinstimmen. Diese Überprüfung gewährleistet Konsistenz und Genauigkeit zwischen dem, was bestellt wurde, und dem, was der Lieferant zu liefern bestätigt.

Sie können diesen Dokumenten einen bestimmten Status geben oder sie einem bestimmten Mitarbeiter zuweisen.

<div align="center"><figure><img src="../../.gitbook/assets/workflow_test9_match_check_overview.png" alt="Workflow Test 9 Match Check Overview"><figcaption></figcaption></figure></div>

<figure><img src="../../.gitbook/assets/workflow_test9_match_check_detail.png" alt="Workflow Test 9 Match Check Detail"><figcaption></figcaption></figure>

**Logic Card: Quantity or Unit Price or Discount Match**

Diese Logic Card ist darauf ausgelegt, automatisch zu überprüfen, ob die in einer Auftragsbestätigung angegebene Menge, der Stückpreis oder der Rabatt mit den entsprechenden Angaben in der Bestellung übereinstimmen. Diese Überprüfung gewährleistet Konsistenz und Genauigkeit zwischen dem, was bestellt wurde, und dem, was der Lieferant zu liefern bestätigt.

**Auslösebedingung**

Die Logik wird aktiviert, wenn eine der folgenden Bedingungen in einer Auftragsbestätigung im Vergleich zur ursprünglichen Bestellung erfüllt ist:

* **Menge**: Die Menge der bestellten Artikel stimmt mit der vom Lieferanten bestätigten Menge überein.
* **Stückpreis**: Der vereinbarte Preis pro Artikel stimmt mit der Bestätigung des Lieferanten überein.
* **Rabatt**: Etwaige gewährte Rabatte sind zwischen Bestellung und Auftragsbestätigung konsistent.
* **Vergleichsparameter definieren**: Legen Sie die spezifischen Felder (Menge, Stückpreis, Rabatt) fest, die die Logic Card auf Übereinstimmung prüfen soll.
* **Überprüfung automatisieren**: Konfigurieren Sie das System so, dass es diese Details beim Eingang einer Auftragsbestätigung automatisch vergleicht.
* **Benachrichtigungen anpassen**: Legen Sie den Workflow für den Umgang mit Abweichungen fest, einschließlich der Anpassung von Benachrichtigungen für die manuelle Prüfung.

Diese Logic Card ist entscheidend, um sicherzustellen, dass die Details einer Auftragsbestätigung mit der ursprünglichen Bestellung übereinstimmen, und schützt so die Integrität des Beschaffungszyklus.

**Test 10:**

Wenn Sie eine andere Berechnung für Zuschläge haben oder diese nur bei einigen Artikeln auftreten, können Sie die generischen Tabellenberechnungs-Cards verwenden. Einige davon erlauben auch das Filtern nach regulären Ausdrücken.

<figure><img src="../../.gitbook/assets/19 (1).png" alt=""><figcaption></figcaption></figure>

Oben sehen Sie ein Berechnungsbeispiel für MTZ mit einem Filter für Artikelnummern, die mit 01, 06, 9, 001 oder 000 beginnen.

Bei einer manuellen Einrichtung wird empfohlen, Berechnungen, die von neuen Spalten abhängen, in einen separaten Workflow auszulagern. Um mit der Berechnung fortzufahren, können Sie die Run Workflow Card verwenden.

**Run Workflow**

<figure><img src="../../.gitbook/assets/20 (1).png" alt=""><figcaption></figcaption></figure>

Mit dieser Card können Sie den Namen eines Workflows angeben, der nach dem aktuellen Workflow ausgeführt werden soll, wenn dessen Bedingungen erfüllt sind und nach den vorherigen Then-Cards des aktuellen Workflows. Während sie ausführbare, aktive Workflows priorisiert, ermöglicht sie auch das Ausführen deaktivierter Workflows, sofern das Dokument die Bedingungen des Workflows erfüllt.

### **Berechnete Zuschläge in eine bestehende Spalte einfügen** <a href="#pekg4i18rshn" id="pekg4i18rshn"></a>

<figure><img src="https://lh7-us.googleusercontent.com/XYY1xsFpp7_-Bi0WOSbotiVzspDLdaufx_xgoopMHmxdZnSDhroLpb0AE_si5PhwMq1jHfndc9FwOte9MOoCoTP5_JUYawO5cr4uIctIDHmwVjz3KacQrLJd8iBQy5KY4N-dMaWEi3IeTcc5OBRNJk4" alt=""><figcaption></figcaption></figure>

Wenn Sie alle Zuschläge als negativen Rabatt in die Rabattspalte einfügen möchten, können Sie die Berechnungs-Card verwenden. Es kann sein, dass in dieser Spalte bereits Einträge vorhanden sind; Sie können sie als eine der Variablen auf der Card festlegen, davon den MTZ abziehen und das Ergebnis wieder in diese Spalte einfügen. Falls leere Felder vorhanden sind (Zuschläge nur für einige Artikel), wird für die Berechnung ein Wert von 0 angenommen.

**Benutzer benachrichtigen, um die Auftragsbestätigung in DocBits zu autorisieren**

Nach der Berechnung der Zuschläge möchten Sie möglicherweise einen bestimmten Benutzer benachrichtigen, um die Auftragsbestätigung zu autorisieren. Dafür können Sie die Benachrichtigungs-Card verwenden.

<figure><img src="../../.gitbook/assets/workflow_notification_card_overview.png" alt="Workflow Notification Card"><figcaption></figcaption></figure>

Je nach Einstellungen wird dem Benutzer eine neue Aufgabe in DocBits zugewiesen und optional eine E-Mail gesendet, um ihn über seine neue Aufgabe zu informieren.
