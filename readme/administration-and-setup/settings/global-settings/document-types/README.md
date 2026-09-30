# Documenttypes

{% embed url="https://youtu.be/pFz_6tvNlU4" %}
DocBits Admin Guide: Adding, Editing & Configuring Document Types (Full Walkthrough)
{% endembed %}

<figure><img src="../../../../.gitbook/assets/docbits_document_types_overview_screenshot.png" alt="Docbits Document Types Overview Screenshot"><figcaption><p>Document Types Screenshot </p></figcaption></figure>

## **Overzicht**

De sectie Documenttypes vermeldt alle documenttypes die door Docbits worden herkend en verwerkt. Beheerders kunnen verschillende aspecten beheren, zoals lay-out, velddefinities, extractieregels en meer voor elk type document. Deze aanpassing is essentieel voor een nauwkeurige gegevensverwerking en naleving van de organisatorische normen.

## **Belangrijkste Kenmerken en Opties**

1. **Documenttype Lijst**:
   * Elke rij vertegenwoordigt een documenttype zoals Factuur, Creditnota, Leveringsbon, enz.
   * Documenttypes kunnen standaard of op maat zijn, zoals aangegeven door labels zoals "Standaard."
2. **Lay-out bewerken**: Deze optie stelt beheerders in staat om de instellingen voor de documentlay-out te wijzigen, waaronder het definiëren van hoe het document eruitziet en waar de gegevensvelden zich bevinden.
3. **Document Subtypes**: Als er documenttypes zijn met subcategorieën, kan deze optie beheerders in staat stellen om instellingen specifiek voor elk subtype te configureren.
4. **Tabelkolommen**: Pas aan welke datakolommen moeten verschijnen wanneer het documenttype in lijsten of rapporten wordt bekeken.
5. **Velden**: Beheer de gegevensvelden die aan het documenttype zijn gekoppeld, inclusief het toevoegen van nieuwe velden of het wijzigen van bestaande.
6. **Modeltraining**: Configureer en train het model dat wordt gebruikt voor het herkennen en extraheren van gegevens uit de documenten. Dit kan inhouden dat parameters worden ingesteld voor machine learning-modellen die in de loop van de tijd verbeteren met meer gegevens.
7. **Regex**: Stel reguliere expressies in die worden gebruikt om gegevens uit documenten te extraheren op basis van patronen. Dit is bijzonder nuttig voor gestructureerde gegevensextractie.
8. **Scripts**: Schrijf of wijzig scripts die aangepaste verwerkingsregels of workflows voor documenten van dit type uitvoeren.
9. **E-DOC**: Configureer instellingen met betrekking tot de uitwisseling van documenten in gestandaardiseerde elektronische formaten. U kunt XRechnung, EDI, FakturaPA of EDI configureren.

#### Aangepaste validatieregels

Open een documenttype en selecteer **Aangepaste validatieregels** om de eigen validatieregels van dat type te beheren. Om een bestaande regel over te nemen zonder haar opnieuw te bouwen, volgt u de handleiding [Een aangepaste validatieregel dupliceren](duplicate-a-custom-validation-rule.md). Daarin worden de regelnaam, de regelsleutel en de bevestigingsknoppen uitgelegd.

{% hint style="info" %}
See [Setup Document Type](../../../setup/document-types/)
{% endhint %}
