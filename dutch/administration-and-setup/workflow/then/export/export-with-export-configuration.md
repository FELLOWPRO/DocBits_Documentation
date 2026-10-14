# Export with Export Configuration

<figure><img src="../../../../.gitbook/assets/image (284).png" alt="" width="563"><figcaption></figcaption></figure>

## **Doel:**

De workflow-kaart **"Export Document with Export Configuration"** is ontworpen om een document te exporteren met een opgegeven exportconfiguratie. Hij biedt de flexibiliteit om eventuele openstaande taken die aan het document zijn gekoppeld te negeren, wat zorgt voor een soepel exportproces, ongeacht de huidige status van het document.

## **Onderdelen van de kaart:**

1. **Export Configuration**
   * **Beschrijving**: Geeft de exportconfiguratie op die voor het verwerken van het document wordt gebruikt.
   * **Detail**: Deze configuratie bepaalt het formaat, de structuur en de bestemming van het geëxporteerde document.
2. **Ignore Pending Tasks**
   * **Beschrijving**: Bepaalt of openstaande taken die aan het document zijn gekoppeld tijdens het exportproces moeten worden genegeerd.
   * **Opties**:
     * **True**: Exporteert het document ongeacht openstaande taken.
     * **False**: Zorgt ervoor dat openstaande taken worden voltooid voordat de export plaatsvindt.

## **Functionaliteit:**

* **Voorwaarde-evaluatie**: Het systeem evalueert de voorwaarden die zijn ingesteld in de **"Where"**- en **"And"**-secties van de workflow. Als beide voorwaarden true zijn, wordt het exportproces gestart.
* **Documentexport**: Met de opgegeven **Export Configuration** wordt het document verwerkt en geëxporteerd in het gedefinieerde formaat en de gedefinieerde bestemming.
* **Afhandeling van openstaande taken**: Als **Ignore Pending Tasks** op **True** is ingesteld, omzeilt het exportproces eventuele uitstaande taken die aan het document zijn gekoppeld. Als het op **False** is ingesteld, wordt de export uitgesteld totdat alle taken zijn opgelost.

## **Opzet en configuratie:**

Om deze kaart te configureren, moeten gebruikers:

1. De gewenste **Export Configuration** selecteren om te definiëren hoe het document wordt geëxporteerd.
2. Kiezen of **Ignore Pending Tasks** wordt ingesteld door de waarde op **True** of **False** in te stellen.
3. Ervoor zorgen dat de voorwaarden in de **"Where"**- en **"And"**-secties correct zijn ingesteld, aangezien de kaart de actie alleen uitvoert wanneer deze voorwaarden true zijn.

## **Conclusie:**

De workflow-kaart **"Export Document with Export Configuration"** zorgt ervoor dat documenten efficiënt en volgens vooraf gedefinieerde configuraties worden geëxporteerd. Met de mogelijkheid om openstaande taken te negeren, biedt deze kaart flexibiliteit bij het afhandelen van documenten in verschillende fasen, wat vertragingen vermindert en het exportproces stroomlijnt.
