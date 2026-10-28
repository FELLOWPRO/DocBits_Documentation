# Export nicht übereinstimmender PO-Zeilen

## Den Exportumfang an drei Positionen verstehen

<figure><img src="../../../../../../.gitbook/assets/intro-process-03-po-export-de-20261028.png" alt="Den Exportumfang an drei Positionen verstehen"><figcaption><p>Den Exportumfang an drei Positionen verstehen</p></figcaption></figure>

Im Beispiel hat die Bestellung drei Positionen; nur eine ist einer Position der Auftragsbestätigung zugeordnet. Ist „Export Not Matched PO Lines“ ausgeschaltet, wird nur die zugeordnete Bestellposition exportiert. Ist die Option eingeschaltet, werden auch die beiden offenen Bestellpositionen mitgegeben. Das erzeugt keine zusätzliche Zuordnung.


## **Wo Sie es Finden**

Gehen Sie zu **Einstellungen → Allgemeine Einstellungen → Dokumenttypen → Weitere Einstellungen → Einkaufsbestellabschnitt → Export nicht übereinstimmender PO-Zeilen**. Schalten Sie den Schalter um, um diese Einstellung zu aktivieren.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F1oYek9ovYpdxvJfOQLPf%252Fimage.png%3Falt%3Dmedia%26token%3D469348b8-eaad-4887-805a-ca14d573a227\&width=768\&dpr=4\&quality=100\&sign=d0b89044\&sv=2)

### **Wie es Funktioniert**

* **Wenn deaktiviert**, exportiert das System nur Einkaufsbestellzeilen, die mit einer Auftragsbestätigungszeile übereinstimmen. Nicht übereinstimmende Einkaufsbestellzeilen werden nicht in den Export einbezogen.
* **Wenn aktiviert**, exportiert das System alle Einkaufsbestellzeilen, auch wenn sie nicht mit einer Auftragsbestätigungszeile übereinstimmen.

Zum Beispiel, wenn eine Einkaufsbestellung **drei Zeilen** hat, aber der Lieferant eine **Auftragsbestätigung mit nur einer Zeile** sendet, ordnen Sie diese Zeile einer Einkaufsbestellzeile zu. Die verbleibenden zwei nicht übereinstimmenden Einkaufsbestellzeilen werden:

* **Vom Export ausgeschlossen**, wenn die Einstellung deaktiviert ist.
* **Im Export enthalten**, wenn die Einstellung aktiviert ist.
