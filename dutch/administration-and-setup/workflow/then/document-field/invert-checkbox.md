# Invert Checkbox

<figure><img src="../../../../.gitbook/assets/image (280).png" alt=""><figcaption></figcaption></figure>

## **Doel:**

Deze workflow-kaart is ontworpen om de huidige status van een selectievakjeveld om te keren. Als het selectievakje is aangevinkt (true), wordt het niet-aangevinkt (false), en omgekeerd. De omkering vindt plaats op basis van de voorwaarden die zijn ingesteld in de **"Where"**- en **"And"**-secties. Deze kaart helpt workflows te automatiseren waarbij een voorwaarde vereist dat een selectievakje wordt omgewisseld op basis van specifieke criteria.

## **Onderdelen van de kaart:**

1. **Field Name**
   * **Beschrijving**: Geeft het om te keren selectievakjeveld op.&#x20;
   * **Detail**: Bij het geselecteerde selectievakjeveld wordt de status omgewisseld van true naar false of van false naar true, op basis van de huidige status.

## **Functionaliteit:**

* **Voorwaarde-evaluatie**: Het systeem evalueert de voorwaarden die zijn gedefinieerd in de **"Where"**- en **"And"**-secties:
  * Als **beide voorwaarden true zijn**, wordt de actie in de **"Then"**-sectie uitgevoerd, wat in dit geval betekent dat het selectievakjeveld wordt omgewisseld.
  * Als **een van beide voorwaarden false is**, wordt de kaart niet uitgevoerd en wordt er geen wijziging aan het selectievakjeveld aangebracht.
* **Actie-uitvoering**: Als de voorwaarden in de **"Where"**- en **"And"**-secties als true worden geëvalueerd, wordt de status van het selectievakjeveld omgekeerd:
  * Als het selectievakje is aangevinkt (true), wordt het niet-aangevinkt (false).
  * Als het selectievakje niet is aangevinkt (false), wordt het aangevinkt (true).

## **Opzet en configuratie:**

Om deze kaart te configureren, moeten gebruikers:

1. **Het selectievakjeveld selecteren** (Field Name) dat wordt omgekeerd. De beschikbare selectievakjevelden in het document worden weergegeven om uit te selecteren.
2. Het selectievakjeveld wordt alleen omgekeerd als de voorwaarden in zowel de **"Where"**- als de **"And"**-secties true zijn.

## **Conclusie:**

De workflow-kaart **"Invert checkbox \[Field Name]"** biedt een eenvoudig maar krachtig automatiseringshulpmiddel om selectievakjewaarden om te wisselen op basis van specifieke voorwaarden. Door de noodzaak van handmatige aanpassingen aan selectievakjes te verminderen, verbetert deze kaart de efficiëntie in de documentverwerking en zorgt hij voor consistentie over workflows heen.
