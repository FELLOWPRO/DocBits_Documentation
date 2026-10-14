# All Value of

<figure><img src="../../../../.gitbook/assets/image (45).png" alt="" width="563"><figcaption></figcaption></figure>

## **Doel:**

Deze DocBits-kaart wordt gebruikt om te valideren of **alle waarden** in een specifieke kolom van een tabel overeenkomen met een opgegeven regex-patroon. Om de workflow te laten doorgaan, moet elke vermelding in de kolom aan de voorwaarde voldoen, waardoor deze kaart ideaal is om consistentie en data-integriteit over alle vermeldingen heen te waarborgen.

## **Functionaliteit:**

* **Regex-patroonvalidatie:** Deze kaart controleert of **alle waarden** in een opgegeven kolom van een tabel overeenkomen met het opgegeven reguliere-expressiepatroon. De workflow gaat alleen verder als elke vermelding in de kolom aan de voorwaarde voldoet.
* **Operator:** Gebruikers definiëren de kolom en geven het regex-patroon op. De beschikbare voorwaarde is:
  * **Matches Regex Pattern:** Verifieert dat elke waarde in de opgegeven kolom overeenkomt met het regex-patroon.
* **Tabel- en kolomselectie:** Gebruikers geven de tabel en kolom op die ze willen controleren op volledige regex-patroonovereenkomsten.

## **Gebruik:**

Deze kaart is ideaal voor gevallen waarin data-uniformiteit vereist is, zoals het waarborgen dat alle telefoonnummers, product-ID's of andere veldvermeldingen voldoen aan een specifiek formaat. Hij zorgt ervoor dat workflows alleen doorgaan wanneer elke relevante vermelding consistent is met het patroon.

## **Voorbeeldscenario:**

* Een gebruiker stelt de kaart in om de kolom "Phone Number" in de tabel "Contacts" te controleren, met behulp van een regex-patroon om telefoonnummerformaten te valideren. Als elke telefoonnummervermelding in de kolom overeenkomt met het patroon, triggert de kaart de volgende stap in de workflow, wat een uniforme gegevensopmaak bevestigt.

Door de kaart "All Values Regex Pattern Matching" te gebruiken, kunnen organisaties strikte datastandaarden afdwingen en de workflow-nauwkeurigheid verbeteren, en zo ervoor zorgen dat elke vermelding in een opgegeven kolom aan het vereiste formaat voldoet voordat er wordt verdergegaan.
