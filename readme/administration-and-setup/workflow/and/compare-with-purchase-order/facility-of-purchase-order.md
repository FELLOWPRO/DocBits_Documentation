# Einrichtung der Bestellung

<figure><img src="../../../../.gitbook/assets/workflow_card_condition_check_facility_in_po_v2-de-de.png" alt="Einrichtung der Bestellung, Version 2" width="634"><figcaption><p>Version 2</p></figcaption></figure>

## Zweck:

Diese Workflow-Karte prüft die Einrichtung der einem Dokument zugeordneten Bestellungen gegen eine Liste von Einrichtungscodes. Sie kann verwendet werden, um Dokumente je nach der Einrichtung (dem Standort), für die bestellt wurde, unterschiedlich zu behandeln, zum Beispiel um sie an das für diese Einrichtung zuständige Team weiterzuleiten.

Der Bestellabgleich sollte vor dieser Karte laufen. Ohne zugeordnete Bestellung meldet die Karte fehlende Daten.

## Bestandteile der Karte:

1. **Beliebig/Alle**
   * **Beschreibung:** Wie die Einrichtungscodes der zugeordneten Bestellungen gegen die Liste ausgewertet werden.
   * **Optionen:**
     * **Irgendeine:** Mindestens ein Eintrag der Liste wird in den Einrichtungscodes der zugeordneten Bestellungen gefunden.
     * **Alle:** Jeder Einrichtungscode der zugeordneten Bestellungen steht in der Liste. Ist kein Wert festgelegt, verwendet die Karte **Alle**.
2. **Operator**
   * **Beschreibung:** Ob die Einrichtung in der Liste stehen soll oder nicht.
   * **Optionen:**
     * **Ist**
     * **Ist nicht**
3. **Codes für den Namen der Einrichtung**
   * **Beschreibung:** Die Einrichtungscodes, mit denen die Einrichtung der Bestellung verglichen wird.
   * **Detail:** Es können mehrere Codes eingegeben werden, durch Kommas getrennt.

## Funktionalität:

* **Bedingungsauswertung:** Die Karte liest die dem Dokument zugeordneten Bestellnummern, lädt diese Bestellungen und sammelt die Einrichtung (den Standort) jeder einzelnen. Bestellungen ohne Einrichtung werden übersprungen. Die gesammelten Einrichtungscodes werden dann mit den **Codes für den Namen der Einrichtung** auf der Karte verglichen.
  * Mit **Irgendeine** und **Ist** wird Groß- und Kleinschreibung nicht beachtet, und ein Eintrag der Liste zählt auch dann, wenn er Teil eines längeren Einrichtungscodes ist (zum Beispiel wird der Eintrag `WH` in `WH01` gefunden).
  * Mit **Alle** und **Ist** sollte jeder Einrichtungscode der Bestellungen in exakt derselben Schreibweise, einschließlich Groß- und Kleinschreibung, in der Liste stehen.
  * Hat keine der zugeordneten Bestellungen eine Einrichtung, ist **Alle** erfüllt und **Irgendeine** nicht.
  * Mit **Ist nicht** ist das Ergebnis nicht einfach das Gegenteil von **Ist**. Das Kartenprotokoll zeigt, welche Codes gefunden und welche nicht zugeordnet wurden, was hilft, das Verhalten für eine bestimmte Einrichtung zu prüfen.
* **Ausführung der Aktion:**
  * **True-Bedingung:**\
    Ist die Bedingung erfüllt, wird der Workflow fortgesetzt, zum Beispiel mit einem Schritt, der speziell für die aufgeführten Einrichtungen gilt.
  * **False-Bedingung:**\
    Ist die Bedingung nicht erfüllt, stoppt der Workflow mit einer nicht erfüllten Bedingung.
* **Fehlende Daten:** Sind auf der Karte keine Einrichtungscodes eingegeben oder hat das Dokument keine zugeordnete Bestellung, wertet die Karte die Bedingung nicht aus und meldet die fehlenden Daten im Workflow-Protokoll.

## Einrichtung und Konfiguration:

* Die Karte kann als And-Bedingung nach dem Bestellabgleich aus der Kategorie **Mit Bestellung vergleichen** hinzugefügt werden. Danach können **Irgendeine** oder **Alle**, der Operator und die durch Kommas getrennten Einrichtungscodes festgelegt werden. Die Codes in derselben Schreibweise wie auf der Bestellung einzugeben, ist die sicherste Wahl, da **Alle** sie exakt vergleicht.
* Mit **Testkarte** im Kartenmenü des Workflow Builders kann die Konfiguration an einem vorhandenen Dokument ausprobiert werden. Das Kartenprotokoll listet die zugeordneten Bestellungen, die darauf gefundenen Einrichtungscodes und die nicht zugeordneten Codes auf.

## Fazit:

Die Workflow-Karte „Facility of Purchase Order“ stellt die Einrichtung der bestellten Waren als Workflow-Bedingung zur Verfügung. So kann ein Workflow Dokumente für verschiedene Einrichtungen unterschiedlich behandeln, auf Basis der Bestelldaten statt dessen, was auf dem Dokument gedruckt ist.
