# Einstellung der Logistikgesellschaft bei Wareneingangsabweichungen prüfen

Bei umfangreichen Beschaffungsprozessen kommt es nicht selten vor, dass bestimmte Datenpunkte nicht wie erwartet zusammenpassen. Beispielsweise kann eine Fehlermeldung wie die folgende erscheinen:

**“Delivery Note L1234, Order Type: Purchase, Order 100000211, Position 10, Subsequent Number 1, Logistic Company&#x20;**<mark style="color:red;">**XXXX**</mark>**, Goods Receipt WE0000293 and Entry Position 10 not found in direct debit.”**

Eine solche Meldung weist häufig auf eine Abweichung oder fehlende Informationen in Ihrer Konfiguration der Logistikgesellschaft hin. Die Logistikgesellschaft ist ein zentrales Element in ERP-Systemen (Enterprise Resource Planning), insbesondere in komplexen Lieferketten, die mehrere juristische oder logistische Einheiten umfassen.

**Warum passiert das?**

In Umgebungen mit mehreren Einheiten muss jede Transaktion – Einkauf, Wareneingang oder Zahlungsauslösung – der richtigen Logistikgesellschaft zugeordnet werden. Die „Logistikgesellschaft“ ist mehr als nur eine Kennung; sie bestimmt, welches Lager, welches Distributionszentrum oder welcher Knoten des Liefernetzwerks für die Bestell- und Erfüllungsaufgaben zuständig ist. Stimmt die Gesellschaftsnummer nicht mit der erwarteten Einheit überein, können nachgelagerte Prozesse wie die Wareneingangsprüfung oder Lastschriftabwicklungen fehlschlagen.

## **Wichtige durchzuführende Prüfungen:**

### 1. Zugeordnete Logistikgesellschaft prüfen:

Prüfen Sie in den Stammdatensätzen, ob die referenzierte Logistikgesellschaft (hier <mark style="color:red;">XXXX</mark>) die richtige Einheit für die jeweilige Bestellung ist. Ist <mark style="color:red;">XXXX</mark> der richtige Gesellschaftscode für Einkäufe bei diesem Lieferanten oder für diese Produktlinie?

### 2. Einrichtung der Bestellung (PO) prüfen:

Vergewissern Sie sich, dass die Logistikgesellschaft der Bestellung zum vorgesehenen Wareneingangsort passt. Manchmal wird eine Bestellung unter einer Logistikgesellschaft angelegt, die Ware aber unter einer anderen eingebucht, wenn die Einrichtung nicht konsistent ist.

### 3. Wareneingang und Lagerdaten abgleichen:

Sehen Sie sich den Wareneingang (WE0000293) an und stellen Sie sicher, dass er im Lager der richtigen Gesellschaft gebucht wurde. Gehört das Lager zu einer anderen Logistikgesellschaft, müssen Sie gegebenenfalls die Konfiguration korrigieren oder eine Umbuchung auf die richtige Einheit durchführen.

### 4. Konsistenz von Integration und Stammdaten prüfen:

Schnittstellen zwischen verschiedenen Modulen (Einkauf, Lagerverwaltung, Finanzen) beruhen auf konsistenten Codes. Stellen Sie sicher, dass die Logistikgesellschaft in allen relevanten Modulen einheitlich definiert ist.

### 5. Dokumentation und Support konsultieren:

Wenn interne Prüfungen das Problem nicht lösen, ziehen Sie Ihre Systemdokumentation zurate oder wenden Sie sich an Ihr ERP-Support-Team. Es kann prüfen, ob der Code der Logistikgesellschaft korrekt eingerichtet ist oder ob weitere Konfigurationsschritte erforderlich sind.

