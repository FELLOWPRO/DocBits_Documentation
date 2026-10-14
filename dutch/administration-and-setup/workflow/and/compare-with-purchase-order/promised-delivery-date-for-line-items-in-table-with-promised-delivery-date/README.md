# Beloofde leverdatum voor regelitems in tabel met beloofde leverdatum

<figure><img src="../../../../../.gitbook/assets/image.png" alt="" width="375"><figcaption></figcaption></figure>

## Doel:

Deze workflowkaart is ontworpen om de **beloofde leverdatum van regelitems** te valideren tegen de **beloofde leverdatum op de inkooporder**, met behulp van vergelijkingsoperatoren en configureerbare tolerantieregels. Het stelt workflows in staat om automatisch conforme, vroege of late leverdatums te detecteren en dienovereenkomstig te reageren.

## Componenten van de Kaart:

1. **Operator**
   * **Beschrijving:**
     Definieert hoe de beloofde leverdatum van het regelitem wordt vergeleken met de beloofde leverdatum van de inkooporder.
   * **Opties:**
     * **Is Gelijk Aan (=):** De datum van het regelitem moet binnen het tolerantievenster vallen.
     * **Is Niet Gelijk Aan (≠):** De datum van het regelitem moet buiten het tolerantievenster vallen.
     * **Groter Dan (>):** De datum van het regelitem moet na het tolerantievenster liggen.
     * **Groter of Gelijk Aan (≥):** De datum van het regelitem moet op of na het begin van het tolerantievenster liggen.
     * **Kleiner Dan (<):** De datum van het regelitem moet voor het tolerantievenster liggen.
     * **Kleiner of Gelijk Aan (≤):** De datum van het regelitem moet op of voor het einde van het tolerantievenster liggen.<br>
2. **Tolerantiedagen**
   * **Beschrijving:**
     Specificeert het aantal dagen dat wordt gebruikt om het acceptabele tolerantievenster rond de beloofde leverdatum van de inkooporder te berekenen.
   * **Detail:**
     Deze waarde is een geheel getal en definieert hoeveel dagen voor en na de inkooporderdatum worden overwogen tijdens de validatie.<br>
3. **Toegestane Tolerantiedagen**
   * **Beschrijving:**
     Definieert welke weekdagen worden meegeteld bij het berekenen van tolerantiedagen.
   * **Detail:**
     Gebruikers kunnen specifieke weekdagen selecteren (bijvoorbeeld maandag tot en met vrijdag). Alleen de geselecteerde dagen worden opgenomen bij het berekenen van het tolerantievenster.

### Functionaliteit:

* **Conditie-evaluatie:** Het systeem berekent een tolerantievenster rond de beloofde leverdatum van de inkooporder op basis van de geconfigureerde **Tolerantiedagen** en **Toegestane Tolerantiedagen**.
  De beloofde leverdatum van elk regelitem wordt vervolgens vergeleken met dit venster met behulp van de geselecteerde operator.
* Actie-uitvoering:
  * **Ware Conditie:** Als het verschil in leverdatum binnen het tolerantiebereik valt en overeenkomt met de conditie die door de operator is ingesteld, gaat de workflow door.
  * **Onware Conditie:** Als niet aan de conditie wordt voldaan, gaat de workflow niet door.

### Instelling en Configuratie:

* Selecteer de juiste vergelijkingsoperator.
* Voer het aantal tolerantiedagen in.
* Kies welke weekdagen als tolerantiedagen moeten worden meegeteld.

### Conclusie:

De **Vergelijk met Inkooporder – Beloofde Leverdatum voor Regelitems** workflowkaart biedt een flexibele manier om regels voor leverdatums af te dwingen. Door operatoren te combineren met weekdagbewuste tolerantieafhandeling, maakt het nauwkeurige validatie van leveringsverplichtingen mogelijk, terwijl handmatige controles en uitzonderingen worden verminderd.
