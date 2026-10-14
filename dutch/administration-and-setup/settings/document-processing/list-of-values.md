# Lijst van Waarden

## Overzicht

De **Lijst met waarden** functie stelt je in staat om vooraf gedefinieerde sets van waarden te creëren en te beheren. Dit is bijzonder nuttig voor het configureren van dropdownmenu's in de [**Velden**](../global-settings/document-types/fields/) sectie, die later gebruikt kunnen worden in **Veldvalidatie**.

Deze lijsten kunnen worden aangepast voor verschillende sub-organisaties en ondersteunen meerdere talen, wat flexibiliteit biedt binnen **DocBits**.

## Hoe te Toegang?

Je kunt de **Lijst met waarden** openen door naar **Instellingen → Documentverwerking → Lijst met waarden** te navigeren.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_list_of_values.png)

## Hoe een Lijst Toevoegen of Verwijderen

### Maak een Nieuwe Lijst met Waarden

1.  Klik op **Nieuw** in de rechterbovenhoek van het scherm.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_1.png)
2. Voer een **Naam** in voor je lijst.
3. _(Optioneel)_ Selecteer een **Sub-organisatie** waarvoor de lijst actief moet zijn.
4.  Klik op **Opslaan** om de lijst te creëren.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_2.png)

### Hoe een Lijst Verwijderen

Om een lijst te verwijderen, klik je op het prullenbakpictogram naast de overeenkomstige lijst.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_13.png)

<mark style="color:red;">**Opmerking**</mark>: De lijst zal onmiddellijk worden verwijderd. Lijsten gemarkeerd met de [**Standaard**](list-of-values.md#systeem-gedefinieerde-lijsten-en-rijen) tag kunnen niet worden verwijderd.

## Hoe Waarden Toevoegen, Bewerken of Verwijderen uit een Bestaande Lijst

Je kunt waarden in een bestaande **Lijst met waarden** beheren met behulp van een van de volgende methoden:

* [**Waarden handmatig toevoegen**](list-of-values.md#waarden-handmatig-toevoegen) – Voer waarden individueel in via de interface.
* [**Waarden importeren vanuit een CSV-bestand**](list-of-values.md#waarden-importeren-vanuit-een-csv-bestand) – Upload een CSV-bestand om meerdere waarden tegelijk toe te voegen.

### Waarden Handmatig Toevoegen

1.  Klik op de lijst die je wilt wijzigen.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_3.png)
2.  Klik op **Acties**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_4.png)
3.  Klik op **Rij toevoegen**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_5.png)

Nu kun je meerdere eigenschappen voor elke invoer specificeren:

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_6.png)

**Waarde**: Dit is hoe het item intern zal worden opgeslagen binnen **DocBits**. Het blijft hetzelfde in alle talen en dient ook als de standaard weergavetekst tijdens veldvalidatie als er geen label is opgegeven voor de geselecteerde taal.

**Label**: Dit is de tekst die op het validatiescherm wordt weergegeven, gebaseerd op de geselecteerde taal. Als er geen label beschikbaar is voor de actieve taal in DocBits, zal het systeem standaard de **Waarde** weergeven.

**Taal**: Geeft de taal aan waarin het label zal worden weergegeven.\
Een meer gedetailleerde uitleg is te vinden [hier](list-of-values.md#voeg-vertalingen-toe-aan-je-waarden).

**Sub-organisaties**: Geeft aan voor welke **sub-organisatie** de rij actief moet zijn. Als dit leeg wordt gelaten, is de rij beschikbaar voor alle organisaties.

**Synoniemen**: Hier kun je aanvullende waarden specificeren die helpen bij het trainen van je document.\
Bijvoorbeeld, als **EUR** je primaire **waarde** is, kun je EURO en € als **synoniemen** toevoegen. Wanneer het document wordt getraind met een van deze **synoniemen**, zal **DocBits** automatisch EUR herkennen en selecteren als de overeenkomstige waarde uit je lijst. <mark style="color:red;">**Opmerking**</mark>: Elk synoniem moet worden bevestigd door op **Enter** te drukken om het aan de lijst toe te voegen.

4.  Nadat je alle gewenste eigenschappen hebt ingevoerd, klik je op de **Opslaan** knop om de rij toe te voegen.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_11.png)

### Waarden Importeren vanuit een CSV-bestand

Om meerdere waarden tegelijk toe te voegen via CSV-import:

1.  Klik op de lijst die je wilt bijwerken.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_3.png)
2.  Klik op **Acties**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_4.png)
3.  Klik op **CSV uploaden**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_7.png)
4. Klik op **Bestand** om het CSV-bestand te doorbladeren en te selecteren dat je wilt uploaden.
5. Kies het juiste **scheidingsteken** dat in het CSV-bestand wordt gebruikt (`;` of `,`).
6.  Klik op **Uploaden** om de waarden te importeren.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_8.png)

### Bestaande Waarden Bewerken

1. Zoek de rij die je wilt bewerken.
2. Klik op de drie stippen in de **Acties** kolom.
3.  Selecteer **Bewerking** uit het dropdownmenu.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_10.png)
4. Maak de vereiste wijzigingen.
5.  Klik op **Opslaan** om je wijzigingen toe te passen.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_11.png)

### Waarden Verwijderen

1. Zoek de rij die je wilt verwijderen.
2. Klik op de drie stippen in de **Acties** kolom.
3.  Selecteer **Verwijderen** uit het dropdownmenu.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_12.png)

<mark style="color:red;">**Opmerking**</mark>: De rij zal onmiddellijk worden verwijderd. Rijen gemarkeerd met de [**Standaard**](list-of-values.md#systeem-gedefinieerde-lijsten-en-rijen) tag kunnen niet worden verwijderd.

## Voeg Vertalingen toe aan je Waarden

Je kunt zoveel vertalingen toevoegen als er ondersteunde talen zijn in **DocBits**.

Om een vertaling toe te voegen:

1.  Klik op het plus (+) pictogram.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_14.png)
2.  Selecteer een taal uit het dropdownmenu.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_15.png)
3.  Voer de gewenste vertaling in het **Label** veld in.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_16.png)
4.  Om een andere vertaling toe te voegen, klik je opnieuw op het plus (+) pictogram.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_17.png)
5.  Om een vertaling te verwijderen, klik je op het prullenbakpictogram.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_18.png)
6.  Wanneer je klaar bent, klik je op de **Opslaan** knop om je vertalingen op te slaan.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_19.png)

<mark style="color:red;">**Opmerking**</mark>: Als er geen **Label** beschikbaar is voor de actieve taal, zal DocBits standaard de **Waarde** weergeven.

## Systeem-gedefinieerde Lijsten en Rijen

Sommige lijsten zijn vooraf gemaakt door het systeem en zijn gemarkeerd met de **Standaard** tag. Deze lijsten kunnen niet worden verwijderd, maar je kunt nieuwe rijen aan hen toevoegen en die nieuw toegevoegde rijen indien nodig verwijderen.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_9.png)

Binnen deze standaard lijsten zijn bepaalde rijen gemarkeerd met de **Standaard** tag—dit zijn systeem-gedefinieerde invoeren. Je kunt nieuwe **labels** in verschillende talen toevoegen, maar deze standaard rijen kunnen niet worden verwijderd.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_20.png)
