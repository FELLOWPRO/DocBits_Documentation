---
hidden: true
---

# In Order Confirmation Purchase Order

### Compare with Purchase Order:

**In Order Confirmation Purchase Order**

<figure><img src="https://lh7-us.googleusercontent.com/glQHETatKah-1YugeLqBb7Jim6lNJxuarRv-KEMv4NPzFfcjSm6mVhTMdI30nxdJ0SHXZ55Oup6KH7K-J6IxjUOiG0wxUX8toAaCopgBJwPyr94CPjoKuauNTmoHGGhg6f3gwHD39W7gpvijg4LQVJ4" alt="" width="563"><figcaption></figcaption></figure>

#### Logic-Karte: Übereinstimmung von Menge, Stückpreis oder Rabatt

Diese Logic-Karte ist darauf ausgelegt, automatisch zu überprüfen, ob die in einer Auftragsbestätigung aufgeführte Menge, der Stückpreis oder der Rabatt mit den entsprechenden Werten in der Bestellung übereinstimmt. Diese Überprüfung gewährleistet Konsistenz und Genauigkeit zwischen dem, was bestellt wurde, und dem, was der Lieferant zu liefern bestätigt.

#### Auslösebedingung

Die Logik wird aktiviert, wenn eine der folgenden Bedingungen in einer Auftragsbestätigung im Vergleich zur ursprünglichen Bestellung erfüllt ist:

* **Menge**: Die Menge der bestellten Artikel stimmt mit der vom Lieferanten bestätigten Menge überein.
* **Stückpreis**: Der vereinbarte Preis pro Artikel stimmt mit der Bestätigung des Lieferanten überein.
* **Rabatt**: Eventuell angewendete Rabatte sind zwischen der Bestellung und der Auftragsbestätigung konsistent.

#### Ergebnisse

* **Gleich**: Stimmen Menge, Stückpreis oder Rabatt der Auftragsbestätigung exakt mit der Bestellung überein, betrachtet das System die Bestätigung als gültig und fährt mit den nächsten Schritten im Beschaffungsprozess fort.
* **Ungleich**: Gibt es eine Abweichung bei Menge, Stückpreis oder Rabatt, markiert das System die Auftragsbestätigung zur manuellen Prüfung. Dadurch wird sichergestellt, dass Abweichungen behoben werden, bevor es weitergeht.

#### Vorteile

* **Genauigkeit und Konsistenz**: Erhält die Genauigkeit im Beschaffungsprozess und stellt sicher, dass Zahlungen und Lieferungen auf Basis korrekter Werte erfolgen.
* **Effizienz**: Automatisiert den Überprüfungsprozess, reduziert den Bedarf an manuellen Prüfungen und beschleunigt die Auftragsverarbeitung.
* **Kostenkontrolle**: Hilft, Überzahlungen oder fehlerhafte Lieferungen zu vermeiden, indem Abweichungen frühzeitig im Prozess erkannt werden.

<figure><img src="https://lh7-us.googleusercontent.com/DRTMJxJ9XLeC5zWSU8QuZwPLkqHzmCUm9RwiUZIkcc8pVxMZsxLv56dX9spzqr7KeDkTigbeBX2DvAZRe-6MdqOgAnrO-QPnCbi4e6hP4--P_O0A0DSoQJxjGeefOS1p6GuXHs1YXv-A73DXYaE8qlI" alt="" width="563"><figcaption></figcaption></figure>

1. **Vergleichsparameter definieren**: Legen Sie die spezifischen Felder (Menge, Stückpreis, Rabatt) fest, die die Logic-Karte auf Übereinstimmung prüft.
2. **Überprüfung automatisieren**: Konfigurieren Sie das System so, dass diese Details beim Eingang einer Auftragsbestätigung automatisch verglichen werden.
3. **Warnungen anpassen**: Legen Sie den Workflow für den Umgang mit Abweichungen fest, einschließlich der Anpassung von Warnungen für die manuelle Prüfung.

Diese Logic-Karte ist unverzichtbar, um sicherzustellen, dass die Details einer Auftragsbestätigung mit der ursprünglichen Bestellung übereinstimmen, und schützt so die Integrität des Beschaffungszyklus. \`\`
