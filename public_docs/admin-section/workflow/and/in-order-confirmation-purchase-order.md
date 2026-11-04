# In Order Confirmation Purchase Order

### Vergleich mit Bestellung:&#x20;

**In Order Confirmation Purchase Order**

<figure><img src="https://lh7-us.googleusercontent.com/glQHETatKah-1YugeLqBb7Jim6lNJxuarRv-KEMv4NPzFfcjSm6mVhTMdI30nxdJ0SHXZ55Oup6KH7K-J6IxjUOiG0wxUX8toAaCopgBJwPyr94CPjoKuauNTmoHGGhg6f3gwHD39W7gpvijg4LQVJ4" alt="" width="563"><figcaption></figcaption></figure>

#### Logikkarte: Übereinstimmung von Menge, Stückpreis oder Rabatt

Diese Logikkarte ist darauf ausgelegt, automatisch zu überprüfen, ob die Menge, der Stückpreis oder der Rabatt in einer Auftragsbestätigung mit den entsprechenden Angaben in der Bestellung übereinstimmen. Diese Überprüfung gewährleistet Konsistenz und Genauigkeit zwischen dem Bestellten und dem, was der Lieferant bestätigt zu liefern.

#### Auslösebedingung

Die Logik wird aktiviert, wenn eine der folgenden Bedingungen in einer Auftragsbestätigung im Vergleich zur ursprünglichen Bestellung erfüllt ist:

* **Menge**: Die bestellte Menge an Artikeln entspricht der vom Lieferanten bestätigten Menge.
* **Stückpreis**: Der vereinbarte Preis pro Artikel entspricht der Bestätigung des Lieferanten.
* **Rabatt**: Angewendete Rabatte stimmen zwischen Bestellung und Auftragsbestätigung überein.

#### Ergebnisse

* **Gleich**: Wenn die Menge, der Stückpreis oder der Rabatt der Auftragsbestätigung genau mit der Bestellung übereinstimmt, betrachtet das System die Bestätigung als gültig und fährt mit den nächsten Schritten im Beschaffungsprozess fort.
* **Nicht gleich**: Wenn es eine Diskrepanz in der Menge, dem Stückpreis oder dem Rabatt gibt, kennzeichnet das System die Auftragsbestätigung zur manuellen Überprüfung. Dies stellt sicher, dass Unstimmigkeiten behoben werden, bevor es weitergeht.

#### Vorteile

* **Genauigkeit und Konsistenz**: Erhält die Genauigkeit im Beschaffungsprozess, um sicherzustellen, dass Zahlungen und Lieferungen auf korrekten Zahlen basieren.
* **Effizienz**: Automatisiert den Überprüfungsprozess, reduziert die Notwendigkeit manueller Überprüfungen und beschleunigt die Auftragsabwicklung.
* **Kostenkontrolle**: Hilft, Überzahlungen oder falsche Lieferungen zu verhindern, indem Unstimmigkeiten früh im Prozess erkannt werden.

<figure><img src="https://lh7-us.googleusercontent.com/DRTMJxJ9XLeC5zWSU8QuZwPLkqHzmCUm9RwiUZIkcc8pVxMZsxLv56dX9spzqr7KeDkTigbeBX2DvAZRe-6MdqOgAnrO-QPnCbi4e6hP4--P_O0A0DSoQJxjGeefOS1p6GuXHs1YXv-A73DXYaE8qlI" alt="" width="563"><figcaption></figcaption></figure>

1. **Vergleichsparameter definieren**: Legen Sie die spezifischen Felder (Menge, Stückpreis, Rabatt) fest, die die Logikkarte auf Übereinstimmung überprüfen wird.
2. **Überprüfung automatisieren**: Konfigurieren Sie das System, um diese Details automatisch beim Erhalt einer Auftragsbestätigung zu vergleichen.
3. **Benachrichtigungen anpassen**: Entscheiden Sie über den Workflow zur Behandlung von Diskrepanzen, einschließlich der Anpassung von Benachrichtigungen für die manuelle Überprüfung.

Diese Logikkarte ist entscheidend, um sicherzustellen, dass die Details einer Auftragsbestätigung mit der ursprünglichen Bestellung übereinstimmen und die Integrität des Beschaffungszyklus zu schützen. \`\`
