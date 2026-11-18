# Documenttypebewerking

<figure><img src="../../../.gitbook/assets/workflow_card_condition_doc_type_is_isnot_v1-nl-nl.png" alt="Documenttypebewerking, Versie 1" width="634"><figcaption><p>Versie 1</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/workflow_card_condition_doc_type_is_isnot_v2-nl-nl.png" alt="Documenttypebewerking, Versie 2" width="634"><figcaption><p>Versie 2</p></figcaption></figure>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-doc-type/v1/nl.mp4" %}

**Video:** Kaart: Documenttype is / is niet · 0:30 · [Ondertitels (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-doc-type/v1/nl.vtt)

<details>

<summary>Transcriptie</summary>

**Documenttype is / is niet** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-doc-type/v1/nl.mp4#t=0.25)

De kaart Documenttype controleert het type van een document. Kies Is of Is niet en dan het type, bijvoorbeeld Factuur. Is niet past bij elk type behalve het gekozen type.

**Voorbeeld: alleen facturen** · [0:17](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-doc-type/v1/nl.mp4#t=17.183)

Bijvoorbeeld een Workflow alleen voor facturen: Documenttype is Factuur als Wanneer-kaart, daarna een toewijzingskaart. Voor creditnota’s, offertes of orders start deze Workflow niet.

</details>

## **Doel:**

Deze workflowkaart is speciaal ontworpen om vooraf gedefinieerde bewerkingen uit te voeren op documenten die zijn gecategoriseerd op type. Het stroomlijnt de verwerking van verschillende documentvormen binnen een ERP-systeem, waarbij wordt gegarandeerd dat elk type wordt verwerkt volgens zijn unieke vereisten en organisatorische beleid.

## **Functionaliteit:**

* **Documenttypevalidatie**: Deze kaart controleert of een document overeenkomt met een bepaald type, zodat gebruikers de categorisatie kunnen bevestigen.
* **Exploitant**: Gebruikers kunnen voorwaarden instellen om het type document te bepalen. Beschikbare operators zijn onder andere:
  * **Is**: Bevestigt dat het document overeenkomt met het gespecificeerde documenttype.
  * **Is Niet**: Zorgt ervoor dat het document niet overeenkomt met het gespecificeerde documenttype.
* **Documenttypen**: Ondersteunde documenttypen zijn onder andere:
  * **Factuur**
  * **Creditnota**
  * **Debitnota**
  * **Inkooporder**
  * **Orderbevestiging**
  * **Vooruitbetaling kennisgeving**

## **Gebruik**:

Deze kaart is handig voor documentbeheerders en beheerders die moeten controleren of documenten correct zijn geclassificeerd voor een gestroomlijnde verwerking. Het valideren van documenttypen verbetert de automatisering van workflows, maakt documentspecifieke acties mogelijk en houdt records georganiseerd.

## **Voorbeeldscenario**:

* Een gebruiker uploadt een document dat is gelabeld als een "Debitnota." Met behulp van de "Is" operator bevestigt de kaart dat het documenttype inderdaad "Debitnota" is, waardoor het systeem relevante verwerkingsregels kan toepassen en het passend kan categoriseren.

Door de kaart "Documenttype" in te zetten, kunnen organisaties de classificatie van documenten automatiseren, consistentie in de verwerking van documenten waarborgen en de efficiëntie van documentbeheerworkflows verbeteren.
