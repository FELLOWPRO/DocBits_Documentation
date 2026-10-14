# Leverancierspecifiek AI-model voor Veld- en Tabelextractie

In de gereedschapssectie van het **Validatiescherm** kunt u het AI-model kiezen dat wordt gebruikt voor **Veldextractie** en **Tabelextractie**.\
Het geselecteerde **AI-model** wordt alleen toegepast op alle documenten van de huidige leverancier.

Om het model te wijzigen, opent u het optiemenu door op de knop **Meer opties** (de drie puntjes) aan de rechterkant van het scherm te klikken en kiest u vervolgens een van de beschikbare modellen:<br>

* **Full** – Hoogste nauwkeurigheid; kost 2 tokens per document
* **Fast** – Standaardtier; kost 1 token per document
* **Nexus** – Kost 1 token per document
* **Nexus Flash** – Snellere tier van de Nexus-familie; kost 1 token per document
* **Auto** – DocBits beslist per document of Fast volstaat of Full nodig is; kost 1 token per document
* **Auto Nexus** – Zoals Auto, maar beperkt tot de Nexus-modelfamilie; kost 1 token per document

<figure><img src="../../../.gitbook/assets/dbdc863-supplier-menu-nl-20261012.png" alt="Optiemenu van het validatiescherm met de keuzelijst AI-model"><figcaption><p>Open het optiemenu en kies het AI-model voor deze leverancier.</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/dbdc863-supplier-options-nl-20261012.png" alt="Geopende keuzelijst AI-model met Full, Fast, Nexus, Nexus Flash, Auto en Auto Nexus"><figcaption><p>De keuzelijst AI-model met de zes beschikbare opties.</p></figcaption></figure>

Als de resultaten van de **veldextractie** of **tabelextractie** niet bevredigend zijn, probeer dan over te schakelen naar een ander model om de nauwkeurigheid te verbeteren.

Om het AI-model **globaal te configureren voor leveranciers zonder aangepast model** of om te **beheren welk model actief is voor elke leverancier**, raadpleegt u de bijbehorende documentatie [**hier**](../../../administration-and-setup/settings/document-processing/classification-and-extraction/ai-model.md).
