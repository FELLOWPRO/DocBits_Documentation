# Promised Delivery Date on Purchase Order

<figure><img src="../../../../.gitbook/assets/image (7) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Doel**

Deze DocBits-kaart is ontworpen om de nauwkeurige vergelijking te faciliteren van toegezegde leverdata op inkooporders met leverdata die voor regelitems in een tabel zijn opgegeven. Door een tolerantiewaarde te integreren, zorgt de kaart voor flexibiliteit bij het monitoren van levertermijnen, wat helpt de nauwkeurigheid van de voorraadplanning en de klanttevredenheid te behouden.

## **Onderdelen van de kaart**

1. **Operator**
   * **Beschrijving:** Definieert de voorwaarde die wordt toegepast om leverdata te vergelijken.
   * **Opties:**
     * **Equals (=):** Controleert of de toegezegde leverdatum op het regelitem overeenkomt met de leverdatum van de inkooporder.
     * **Not Equal (≠):** Zorgt ervoor dat de toegezegde leverdatum op het regelitem niet overeenkomt met de datum op de inkooporder.
     * **Greater Than (>):** Verifieert of de toegezegde leverdatum van het regelitem later is dan de leverdatum van de inkooporder.
     * **Greater or Equals (≥):** Controleert of de toegezegde leverdatum van het regelitem gelijk is aan of later is dan de leverdatum van de inkooporder.
     * **Less Than (<):** Bevestigt of de toegezegde leverdatum van het regelitem eerder is dan de leverdatum van de inkooporder.
     * **Less or Equals (≤):** Valideert of de toegezegde leverdatum van het regelitem gelijk is aan of eerder is dan de leverdatum van de inkooporder.
2. **Value**
   * **Beschrijving:** Geeft een toegestane foutmarge in de vergelijking van leverdata op.
   * **Detail:** Gebruikers definiëren het aantal dagen waarmee de leverdatum van het regelitem mag afwijken van de toegezegde leverdatum.

## **Functionaliteit**

* **Voorwaarde-evaluatie:**\
  De kaart berekent het verschil tussen de toegezegde leverdatum van de inkooporder en de leverdata voor regelitems in de tabel. De geselecteerde operator wordt vervolgens toegepast om te bepalen of aan de voorwaarde wordt voldaan.
* **Actie-uitvoering:**
  * **True-voorwaarde:** Als het verschil in leverdatum binnen het tolerantiebereik valt en overeenkomt met de door de operator ingestelde voorwaarde, gaat de workflow verder.
  * **False-voorwaarde:** Als niet aan de voorwaarde wordt voldaan, gaat de workflow niet verder.

## **Opzet en configuratie**

* De operator wordt geselecteerd om de gewenste vergelijkingsvoorwaarde te definiëren, zoals gelijk aan, groter dan of kleiner dan. Ten slotte geven gebruikers een tolerantiewaarde in dagen op, waarmee kleine variaties in de vergelijking worden toegestaan zonder waarschuwingen te triggeren.

## **Voorbeeldscenario**

* Een inkooporder geeft een toegezegde leverdatum van 1 december op. Een regelitem in de tabel heeft een toegezegde leverdatum van 3 december. Met een tolerantiewaarde van 2 dagen en de operator **Equals (≥)** geselecteerd, beschouwt de kaart de leverdatum als binnen het acceptabele bereik. Er wordt geen waarschuwing getriggerd, zodat kleine afwijkingen worden getolereerd zonder de bedrijfsvoering te verstoren.

## **Conclusie**

De kaart "Promised Delivery Date Comparison" helpt de toeleveringsketenactiviteiten te stroomlijnen door nauwkeurige monitoring van levertermijnen mogelijk te maken. Met de mogelijkheid om toleranties en flexibele vergelijkingsoperatoren te integreren, zorgt hij voor naleving van de leververwachtingen en voorkomt hij onnodige waarschuwingen voor kleine afwijkingen. Dit verbetert het leveranciersbeheer en de algehele workflow-efficiëntie.
