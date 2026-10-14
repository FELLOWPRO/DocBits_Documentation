# Einstellungen zur Toleranz von Bestellungen / Zusätzliche Toleranz für Bestellungen

### **Einstellung zur Konfiguration von Bestelltoleranzen**

Gehe zu **Einstellungen → Allgemeine Einstellungen → Dokumenttypen → Weitere Einstellungen → Bestellungen → Eigener Bereich für Bestelltoleranz**

#### **So funktioniert es**

Wenn aktiviert, ermöglicht diese Einstellung, Toleranzen für **Menge** und/oder **Stückpreis** zu definieren. Diese Toleranzen können entweder als Prozentsatz oder als fester Wert festgelegt werden. Das bedeutet, dass eine Rechnung innerhalb des angegebenen Toleranzbereichs von der Bestellung (PO) abweichen kann, ohne als Abweichung markiert zu werden, was Flexibilität bietet und einen nahtlosen Ablauf gewährleistet.

<mark style="color:red;">**HINWEIS**</mark>**:** Toleranzen wirken in beide Richtungen; das heißt, der Rechnungswert kann sowohl höher als auch niedriger als der PO-Wert innerhalb des erlaubten Bereichs sein.

#### **Einrichten**

* **Einstellung aktivieren:**
  * Aktiviere die PO-Toleranzeinstellung.
* **Toleranzen konfigurieren:**
  * Es erscheinen vier Felder:
    * Ein Feld für den **Mengen-Toleranzbetrag**.
    * Ein Feld für den **Stückpreis-Toleranzbetrag**.
  * Hinter jedem Feld gibt es ein Dropdown-Menü, in dem du den Toleranztyp auswählen kannst:
    * **Prozent:** Gibt eine prozentuale Toleranz an.
    * **Wert:** Gibt einen festen Betrag an, um den sich der Wert unterscheiden kann.

<figure><img src="../../../../../../.gitbook/assets/docbits_docbits_image_11.jpg" alt="DocBits Bild"><figcaption></figcaption></figure>

#### **Beispielszenario:**

* Angenommen, die **Stückpreis** ist auf **5%** eingestellt.
* Die Bestellung umfasst zwei Zeilen:
  * **Zeile 1:** Stückpreis = **$5.00**
  * **Zeile 2:** Stückpreis = **$2.00**
* Auf der Rechnung:
  * **Zeile 1:** Der Stückpreis wird auf **$4.80** angepasst (**innerhalb** der 5% Toleranz).
  * **Zeile 2:** Der Stückpreis wird auf **$2.20** angepasst (**außerhalb** der 5% Toleranz).
* **Ergebnis:**
  * Zeile 1 wird **nicht als Abweichung markiert**, da $4.80 innerhalb von 5% von $5.00 liegt.
  * Zeile 2 **wird als Abweichung markiert**, da $2.20 die erlaubte Abweichung von 5% von $2.00 überschreitet. Der Benutzer muss nun Maßnahmen ergreifen, bevor die Rechnung weiter bearbeitet werden kann.

<figure><img src="../../../../../../.gitbook/assets/docbits_invoice_settings.jpg" alt="Rechnung Einstellungen Übersicht"><figcaption></figcaption></figure>

### Einstellung zur Konfiguration zusätzlicher Bestelltoleranzeinstellungen

Gehe zu **Einstellungen → Allgemeine Einstellungen → Dokumenttypen → Weitere Einstellungen → Bestellabschnitt → Zusätzliche PO-Toleranzeinstellung**

#### **So funktioniert es**

Wenn aktiviert, ermöglicht diese Einstellung, Toleranzen für **Fracht**, **Gebühren** und/oder **Steuern** zu definieren. Diese Toleranzen können entweder als Prozentsatz oder als fester Wert festgelegt werden, sodass Rechnungen leicht von den PO-Werten abweichen können, ohne als Abweichungen markiert zu werden. Dies bietet zusätzliche Flexibilität und stellt sicher, dass geringfügige Unterschiede den Arbeitsablauf nicht unterbrechen.

<mark style="color:red;">**HINWEIS**</mark>**:** Genau wie bei den standardmäßigen Toleranzeinstellungen gelten diese Toleranzen in beide Richtungen – sie erlauben sowohl Erhöhungen als auch Senkungen innerhalb der festgelegten Grenzen.

#### **Einrichten**

* **Einstellung aktivieren:**
  * Aktiviere die zusätzliche PO-Toleranzeinstellung.
* **Toleranzen konfigurieren:**
  * Sechs Felder werden sichtbar:
    * Je ein Feld für die Toleranzbeträge für **Fracht**, **Gebühren** und **Steuern**.
  * Jedes Feld hat ein begleitendes Dropdown-Menü, in dem du den Toleranztyp auswählen kannst:
    * **Prozent:** Die Toleranz wird als Prozentsatz definiert.
    * **Wert:** Die Toleranz wird als fester Betrag definiert.

<figure><img src="../../../../../../.gitbook/assets/docbits_docbits_image_12.jpg" alt="DocBits Bild"><figcaption></figcaption></figure>
