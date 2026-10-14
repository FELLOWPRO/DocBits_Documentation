# Duplicaatdetectie

## Overzicht

In **DocBits** kun je filteren op dubbele documenten door aan te geven welke velden moeten overeenkomen en door een tijdsinterval te definiëren waarin duplicaten moeten worden gedetecteerd.

Deze pagina biedt een gedetailleerde gids over hoe je de functie **Duplicaatdetectie** effectief kunt inschakelen en gebruiken.

## Duplicaatdetectie inschakelen

Om de detectie van dubbele documenten in **DocBits** in te schakelen, volg je deze stappen:

1.  Navigeer naar **Instellingen** → **Globale instellingen** → **Documenttypen**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/Calculate_PO_unit_price_1.png)
2.  Selecteer het gewenste **Documenttype** en klik op **Meer instellingen**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/Calculate_PO_unit_price_2.png)
3.  Ga naar de sectie **Duplicaatdetectie**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/DuplicateDocument_3.png)

DocBits biedt twee opties voor het identificeren van dubbele documenten:

1. **Detectie van dubbele documenten**:\
   Deze functie controleert op dubbele documenten die zijn geüpload naar **DocBits** op basis van de geselecteerde criteria. Als een document overeenkomt met de geselecteerde criteria in andere documenten, wordt het gemarkeerd als een duplicaat.
2.  **Detectie van dubbele facturen** (Alleen beschikbaar voor het **Factuur** documenttype):\
    Deze functie vereist het synchroniseren van leveranciersfacturen van Infor naar DocBits. Het vergelijkt de factuurnummers in het DocBits-dashboard met die in Infor. Als hetzelfde factuurnummer meer dan eens voorkomt, wordt het gemarkeerd als een duplicaat.

    <mark style="color:red;">**Opmerking**</mark>: Het gebruik van de functie **Detectie van dubbele facturen** resulteert in een extra kredietkosten.

## Filter welke documenten als duplicaat moeten worden gedetecteerd

Zodra **Duplicaatdetectie** is ingeschakeld, zijn er twee dropdown-menu's beschikbaar voor configuratie:

*   **Duplicaatdetectievelden**\
    Selecteer de velden die moeten worden gebruikt om duplicaten te identificeren (bijv. Leveranciers-ID, Datum, Factuurnummer, enz.). Documenten die overeenkomen met deze velden worden gemarkeerd als duplicaten.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/DuplicateDocument_4.png)
*   **Duplicaatdetectie-interval**

    Gebruik deze instelling om het tijdsbereik te definiëren waarin duplicaten worden gedetecteerd. Documenten die binnen het geselecteerde interval zijn geüpload, worden met elkaar vergeleken op basis van de geselecteerde velden.

    **Beschikbare opties:**

    * 1 maand
    * 3 maanden (Aanbevolen)
    * 6 maanden
    * 1 jaar

    <mark style="color:red;">**Opmerking**</mark>: Een interval van 3 maanden wordt aanbevolen om optimale prestaties te garanderen. Het selecteren van een langer interval kan leiden tot langzamere laadtijden van het dashboard.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/DuplicateDocument_6.png)

## Dubbele documenten bekijken op het Dashboard

Zodra **Duplicaatdetectie** is ingeschakeld, worden documenten die als duplicaten zijn geïdentificeerd, weergegeven met een duplicaatindicatorpictogram op het dashboard.

*   Klik op dit pictogram om de overeenkomende records in een zij-aan-zij gesplitst scherm te openen voor gemakkelijke vergelijking.\
    <mark style="color:red;">**Opmerking**</mark>: Het pictogram verschijnt alleen als er minstens één duplicaat is gedetecteerd voor het document.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/DuplicateDocument_7.png)
*   Wanneer je een gemarkeerd document bekijkt, verschijnt er een waarschuwingsbalk bovenaan, die aangeeft dat het document een duplicaat is.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/DuplicateDocument_5.png)
