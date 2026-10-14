# Any Value of

<figure><img src="../../../../.gitbook/assets/image (46).png" alt="" width="563"><figcaption></figcaption></figure>

## **Doel:**

Deze DocBits-kaart wordt gebruikt om te valideren of een willekeurige waarde in een specifieke kolom van een tabel overeenkomt met een opgegeven regex-patroon. Als een enkele vermelding in de kolom overeenkomt met het patroon, gaat de workflow verder, waardoor deze kaart ideaal is voor gebruikssituaties waarin het identificeren van zelfs maar één match de volgende stappen in het proces triggert.

## **Functionaliteit:**

* **Regex-patroonvalidatie:** Deze kaart controleert of een willekeurige waarde in een bepaalde kolom van een tabel overeenkomt met het opgegeven reguliere-expressiepatroon. De kaart wordt getriggerd en laat de workflow doorgaan als ten minste één vermelding in de kolom aan de voorwaarde voldoet.
* **Operator:** Gebruikers definiëren de kolom en geven het regex-patroon op. De beschikbare voorwaarde is:
  * **Matches Regex Pattern:** Verifieert dat ten minste één waarde in de opgegeven kolom overeenkomt met het regex-patroon.
* **Tabel- en kolomselectie:** Gebruikers geven de tabel en kolom op die ze willen controleren op regex-patroonovereenkomsten.

## **Gebruik:**

Deze kaart is met name nuttig voor scenario's waarin een tabel gegevens bevat die mogelijk specifieke matches vereisen, zoals het valideren van e-mailadressen, factuurnummers of product-ID's. Hij zorgt ervoor dat workflows doorgaan wanneer een willekeurige relevante vermelding overeenkomt met het gedefinieerde patroon, zonder dat elke vermelding hoeft te worden gecontroleerd.

## **Voorbeeldscenario:**

* Een gebruiker stelt de kaart in om vermeldingen in de kolom "Email Address" van de tabel "Customers" te controleren, met behulp van een regex-patroon voor geldige e-mailformaten. Als ten minste één e-mailadres in de kolom overeenkomt met het patroon, triggert de kaart de volgende workflow-stap, zodat het systeem de geldige vermelding verwerkt.

Door de kaart "Regex Pattern Matching" te gebruiken, kunnen organisaties workflows automatiseren op basis van dynamische, patroongebaseerde validaties, processen stroomlijnen en ervoor zorgen dat alleen relevante vermeldingen verdere acties triggeren.
