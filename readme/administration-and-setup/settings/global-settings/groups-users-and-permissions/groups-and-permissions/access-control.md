# Zugriffskontrolle

## Übersicht

Die Zugriffskontrolle legt für eine einzelne **Gruppe** (Rolle) genau fest, was deren Mitglieder tun dürfen — sowohl auf **Dokumenttyp-Ebene** (welche Dokumenttypen sie sehen und welche Aktionen sie ausführen dürfen) als auch auf **Feldebene** (welche einzelnen Felder sie lesen oder bearbeiten dürfen).

Berechtigungen werden immer **pro Gruppe** ausgewertet. Ein Benutzer erbt die Berechtigungen jeder Gruppe, der er angehört.

{% hint style="info" %}
Die Zugriffskontrolle greift nur, wenn das System **Gruppen & Berechtigungen** eingeschaltet ist (siehe [Berechtigungen aktivieren](activating-permissions.md)). **Administratoren umgehen die Zugriffskontrolle immer** und können unabhängig von den Einstellungen auf dieser Seite alles sehen und tun.
{% endhint %}

Jede Gruppe kann konfiguriert werden für:

* **Dokumentzugriff** — ob die Gruppe einen Dokumenttyp überhaupt nutzen darf.
* **Aktionsberechtigungen** — welche Aktionen (auflisten, anzeigen, bearbeiten, löschen, massenaktualisieren, genehmigen) die Gruppe ausführen darf und *für welche Dokumente*.
* **Feldberechtigungen** — ob jedes einzelne Feld eines Dokumenttyps bearbeitbar, schreibgeschützt oder ausgeblendet ist.

## Aktivierung

1. Navigieren Sie zu **Einstellungen**.
2. Wählen Sie **Dokumentenverarbeitung**.
3. Wählen Sie **Module.**
4. Aktivieren Sie die **Zugriffskontrolle**, indem Sie den Schieberegler aktivieren.

<figure><img src="../../../../../.gitbook/assets/Access-Control3_de.png" alt=""><figcaption></figcaption></figure>

## Zugriffskontrolle einer Gruppe öffnen

1. Navigieren Sie zu **Einstellungen**.
2. Gehen Sie zu **Globale Einstellungen**.
3. Wählen Sie **Gruppen, Benutzer und Berechtigungen**.
4. Wählen Sie **Gruppen und Berechtigungen**.
5. Um die Berechtigungen einer Gruppe (z. B. PROCUREMENT\_DIRECTOR) zu verwalten, klicken Sie auf die drei Punkte auf der rechten Seite.
6. Wählen Sie **Zugriffskontrolle verwalten**.

<figure><img src="../../../../../.gitbook/assets/access_control_open_menu.png" alt="Zeilenmenü einer Gruppe öffnen und Zugriffskontrolle verwalten wählen"><figcaption><p>Öffnen Sie auf der Seite „Gruppen und Berechtigungen" das <strong>⋮</strong>-Menü einer Gruppe und wählen Sie <strong>Zugriffskontrolle verwalten</strong>.</p></figcaption></figure>

## Wie eine Berechtigung ausgewertet wird

Wenn ein Benutzer etwas mit einem Dokument tun möchte, prüft DocBits der Reihe nach:

1. **Ist das System Gruppen & Berechtigungen eingeschaltet und der Benutzer kein Administrator?** Wenn aus oder der Benutzer ist Administrator → voller Zugriff.
2. **Ist der Dokumenttyp für eine der Gruppen des Benutzers aktiviert?** Wenn deaktiviert → der Benutzer kann diesen Dokumenttyp nicht sehen oder nutzen.
3. **Welcher Zugriffsbereich ist für die Aktion gesetzt?** (z. B. *Bearbeiten = Owner*). Der Bereich wird mit der Beziehung des Benutzers zu *diesem konkreten Dokument* abgeglichen — ist er Eigentümer, Zugewiesener, beides oder keines?
4. **Welche Feldberechtigung gilt?** Selbst wenn ein Benutzer ein Dokument öffnen darf, können einzelne Felder weiterhin ausgeblendet oder gesperrt sein.

## Dokumenttyp-Berechtigungen

Jede Zeile der Matrix ist ein Dokumenttyp (Invoice, Credit Note, Purchase Order, …).

Die erste Spalte ist ein Schalter **Aktiviert / Deaktiviert**. Deaktivieren Sie ihn, kann die Gruppe diesen Dokumenttyp gar nicht nutzen — er verschwindet aus ihrem Dashboard. Aktivieren Sie ihn, werden die sieben Aktionsspalten bearbeitbar.

| Aktion | Bestimmt, ob die Gruppe … |
|--------|----------------------------|
| **Liste** | den Dokumenttyp in der Dashboard-Liste sehen darf. |
| **Anzeigen** | ein Dokument öffnen und seine Details ansehen darf. |
| **Bearbeiten** | Feldwerte eines Dokuments ändern darf. |
| **Löschen** | ein Dokument löschen darf. |
| **Massenaktualisierung** | mehrere Dokumente auf einmal aktualisieren darf. |
| **Erste Genehmigung** | die Genehmigung der ersten Stufe erteilen darf. |
| **Zweite Genehmigung** | die Genehmigung der zweiten Stufe erteilen darf. |

### Zugriffsbereiche

Jede Aktionsspalte ist ein Dropdown. Der gewählte Wert beantwortet die Frage *„für welche Dokumente darf die Gruppe das tun?"*. Die Bereichsnamen erscheinen in der Oberfläche auf Englisch:

| Bereich | Wer ist erlaubt | Wirkung auf ein Dokument |
|---------|-----------------|--------------------------|
| **No Access** | Niemand in der Gruppe. | Die Aktion ist für alle in der Gruppe gesperrt — die Schaltfläche ist ausgeblendet oder deaktiviert. |
| **Everyone** | Jedes Mitglied der Gruppe. | Jedes Gruppenmitglied kann die Aktion bei **jedem** Dokument dieses Typs ausführen. |
| **Owner** | Nur der Benutzer, der das Dokument **erstellt / hochgeladen** hat. | Die Aktion funktioniert nur bei Dokumenten, die der Benutzer selbst hochgeladen hat. |
| **Assignee** | Nur der Benutzer (oder die Gruppe), dem das Dokument **zugewiesen** ist. | Die Aktion funktioniert nur bei Dokumenten, die dem Benutzer oder einer seiner Gruppen zugewiesen sind. |
| **Owner & Assignee** | Der Eigentümer **oder** der Zugewiesene. | Die Aktion funktioniert, wenn der Benutzer *entweder* der Hochladende *oder* der Zugewiesene ist. |

{% hint style="info" %}
**Owner** und **Assignee** hängen von der *Beziehung zwischen dem Benutzer und jedem einzelnen Dokument* ab. Zwei Mitglieder derselben Gruppe können daher beim selben Beleg unterschiedliche Rechte haben — siehe das durchgespielte Beispiel unten.
{% endhint %}

<figure><img src="../../../../../.gitbook/assets/access_control_matrix.png" alt="Zugriffskontroll-Matrix einer Gruppe"><figcaption><p>Die Dokumenttyp-Berechtigungsmatrix. Hier ist der Typ <strong>Invoice</strong> aktiviert und seine Aktionen sind auf verschiedene Zugriffsbereiche gesetzt; die übrigen Typen sind deaktiviert.</p></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/access_control_scope_dropdown.png" alt="Dropdown der Zugriffsbereiche"><figcaption><p>Jede Aktionsspalte bietet dieselben fünf Zugriffsbereiche.</p></figcaption></figure>

### Genehmigung erfordert auch Bearbeiten

Das Genehmigen eines Dokuments löst im Hintergrund **zwei Aktionen** aus: DocBits **speichert** zuerst das Dokument und setzt es dann auf den genehmigten Status. Der Speicherschritt benötigt die Berechtigung **Bearbeiten** — die beiden Berechtigungen sind also verknüpft.

Ein Benutzer, der nur **Erste Genehmigung** oder **Zweite Genehmigung** erhält — aber *nicht* **Bearbeiten** —, läuft beim Speicherschritt in einen Berechtigungsfehler und kann das Dokument nicht genehmigen.

{% hint style="warning" %}
Wann immer Sie **Erste Genehmigung** oder **Zweite Genehmigung** vergeben, vergeben Sie auch **Bearbeiten** (und **Anzeigen**) für denselben Dokumenttyp. Eine Genehmigungsberechtigung allein reicht nicht aus.
{% endhint %}

## Feldberechtigungen

Klicken Sie auf eine Dokumenttyp-Zeile, um darunter das Panel **Feldberechtigungen** zu öffnen. Felder sind in Reiter gegliedert (z. B. *Tabellenspalten*, *Details der Rechnung*, *Einzelheiten zur Zahlung*, *Steuersätze & Beträge*). Jedes Feld hat seine eigene Zugriffsstufe:

| Stufe | Wirkung auf das Feld |
|-------|----------------------|
| **Lesen/Schreiben** | Das Feld ist sichtbar **und** bearbeitbar. |
| **Nur Lesen** | Das Feld ist sichtbar, kann aber **nicht bearbeitet** werden (ausgegraut). |
| **Genehmigung** | Das Feld kann bearbeitet werden, die Änderung durchläuft aber zuerst einen **Genehmigungs-Workflow**. |
| **Kein Zugriff** | Das Feld ist **vollständig ausgeblendet** — der Benutzer sieht es nie. |

{% hint style="info" %}
Feldregeln gelten für **alle** Mitglieder der Gruppe gleichermaßen — sie hängen nicht von Eigentümer/Zugewiesenem ab. Nutzen Sie sie, um sensible Felder (z. B. einen Rabatt oder einen Gesamtbetrag) für eine ganze Gruppe auszublenden oder zu sperren.
{% endhint %}

<figure><img src="../../../../../.gitbook/assets/access_control_field_permissions.png" alt="Panel Feldberechtigungen"><figcaption><p>Das Panel „Feldberechtigungen" für den Typ Invoice. <code>CUSTOMER_DISCOUNT</code> ist ausgeblendet (Kein Zugriff), während die übrigen Felder auf Lesen/Schreiben stehen.</p></figcaption></figure>

## Durchgespieltes Beispiel: Was die Zugriffskontrolle bei einem echten Beleg bewirkt

Angenommen, Sie erstellen eine Gruppe **AP_CLERK** für Ihre Kreditorenbuchhalter und konfigurieren den Dokumenttyp **Invoice** wie folgt:

**Dokumenttyp-Berechtigungen für Invoice**

| Aktion | Bereich |
|--------|---------|
| Aktiviert | ✅ An |
| Liste | Everyone |
| Anzeigen | Everyone |
| Bearbeiten | Owner & Assignee |
| Löschen | No Access |
| Massenaktualisierung | No Access |
| Erste Genehmigung | Assignee |
| Zweite Genehmigung | No Access |

**Feldberechtigungen für Invoice**

| Feld | Stufe |
|------|-------|
| `TOTAL_AMOUNT` | Nur Lesen |
| `CUSTOMER_DISCOUNT` | Kein Zugriff |
| *(alle anderen Felder)* | Lesen/Schreiben |

Verfolgen Sie nun ein konkretes Dokument — den Beleg **INV-4711**, den **Maria hochgeladen** hat und der **Maria zugewiesen** ist. Sowohl Maria als auch ihr Kollege Tom sind in der Gruppe **AP_CLERK**.

**Maria (Eigentümerin *und* Zugewiesene von INV-4711):**

* ✅ Sieht INV-4711 in der Dashboard-Liste *(Liste = Everyone)*.
* ✅ Öffnet ihn *(Anzeigen = Everyone)*.
* ✅ Bearbeitet Lieferantennamen und Positionen *(Bearbeiten = Owner & Assignee — sie ist die Eigentümerin)*.
* 🔒 Sieht `TOTAL_AMOUNT`, das Feld ist aber ausgegraut und nicht änderbar *(Nur Lesen)*.
* 🚫 Sieht das Feld `CUSTOMER_DISCOUNT` gar nicht *(Kein Zugriff)*.
* 🚫 Die Schaltfläche **Löschen** ist ausgeblendet *(Löschen = No Access — niemand in der Gruppe darf löschen)*.
* ✅ Kann die **erste Genehmigung** erteilen *(Erste Genehmigung = Assignee — sie ist die Zugewiesene)*.

**Tom (gleiche Gruppe, hat INV-4711 aber *nicht* hochgeladen und er ist ihm *nicht* zugewiesen):**

* ✅ Sieht ihn in der Liste und ✅ öffnet ihn *(Liste & Anzeigen = Everyone)*.
* 🚫 Kann nichts bearbeiten — das Dokument öffnet **schreibgeschützt** *(Bearbeiten = Owner & Assignee — Tom ist keines von beiden)*.
* 🔒 / 🚫 Sieht genau dieselbe Feldsichtbarkeit wie Maria: `TOTAL_AMOUNT` gesperrt, `CUSTOMER_DISCOUNT` ausgeblendet *(Feldregeln gelten für die ganze Gruppe)*.
* 🚫 Kann die erste Genehmigung nicht erteilen *(Erste Genehmigung = Assignee — nicht Tom)*.
* 🚫 Kann nicht löschen *(No Access)*.

**Was dieses Beispiel zeigt**

* **Everyone** öffnet ein Dokument für alle Gruppenmitglieder; **Owner / Assignee** schränkt eine Aktion auf die Personen ein, die mit dem konkreten Dokument verbunden sind.
* **No Access** entfernt eine Aktion (Löschen) oder blendet ein Feld (`CUSTOMER_DISCOUNT`) für die gesamte Gruppe aus.
* **Nur Lesen** hält ein Feld sichtbar zur Referenz (`TOTAL_AMOUNT`), verhindert aber Änderungen.
* Zwei Personen in **derselben Gruppe** können beim **selben Beleg unterschiedliche Rechte** haben — allein deshalb, wer ihn hochgeladen hat und wem er zugewiesen ist.
