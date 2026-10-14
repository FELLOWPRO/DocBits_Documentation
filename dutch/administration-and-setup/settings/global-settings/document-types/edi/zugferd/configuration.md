# ZUGFeRD-configuratie

{% embed url="https://youtu.be/AxrHNEmmXtg" %}
DocBits E-Invoice Tutorial: XRechnung / ZUGFeRD (Factur-X) verwerken, gegevens valideren en workflows automatiseren
{% endembed %}

## **Ondersteunde versies van ZUGFeRD**

DocBits ondersteunt alle belangrijke versies van ZUGFeRD, waaronder:

* **1.0**
* **2.0**
* **2.1** (voldoet aan FACTUR-X 1.0.05)
* **2.2**
* **2.3** (voldoet aan FACTUR-X 1.07.2)
* **2.3.2**

#### Standaard activering en wijziging

De ZUGFeRD-standaard is standaard altijd actief, maar u kunt indien nodig wijzigingen aanbrengen.

### **Stappen om ZUGFeRD-instellingen te wijzigen:**

1. Navigeer naar **Instellingen → Globale Instellingen → Documenttypes → Factuur**.
2. Klik op **E-Doc**.
3. Er verschijnt een lijst met alle beschikbare e-docs.
4. Zoek de **ZUGFeRD**-versie die u wilt wijzigen.

## **Configuratie van transformatie en XML-pad:**

In de **transformatie-instellingen** kunt u het pad definiëren om specifieke informatie in het XML-bestand te vinden en in een nieuwe structuur op te slaan, waardoor het gemakkelijker wordt om toegang te krijgen tot de gegevens. <mark style="color:red;">**Opmerking**</mark>: Als u deze functionaliteit gebruikt, moet u de nieuw aangemaakte XML-paden gebruiken, niet de originele XML-paden, in de **Preview** en het **Extractiepad**.

### **Stappen om het transformatiebestand te wijzigen:**

1. Open de **Transformatie**.
2. Maak een nieuw concept door op het **potloodpictogram** te klikken.
3. Selecteer het nieuw aangemaakte concept.
4. Maak een nieuw veld aan of wijzig een bestaand veld.
5. Stel het gewenste pad in voor gegevensextractie.
6. Klik op **Opslaan**.

### Belangrijke opmerkingen:

* Het **preview-bestand** wordt alleen gebruikt voor **FACTUR-X** en niet voor **ZUGFeRD**. ZUGFeRD gebruikt de originele **PDF**.

## Configuratie Preview PDF

De **Configuratie Preview PDF** wordt gebruikt om een door de gebruiker leesbare versie van het document te genereren. U kunt deze aanpassen met HTML om aan uw behoeften te voldoen.

### **Stappen om het preview-bestand te wijzigen:**

1. Open de **Preview**.
2. Maak een nieuw concept door op het **potloodpictogram** te klikken.
3. Selecteer het nieuw aangemaakte concept.
4. Maak een nieuw veld aan of wijzig een bestaand veld.
5. Stel het gewenste pad in voor gegevensextractie.
6. Klik op **Opslaan**.

## Configuratie extractiepaden

De **Configuratie extractiepaden** wordt gebruikt om gegevens te extraheren en velden in het **validatiescherm** in te vullen, zoals de factuurtabel of velden die in de factuurlay-out zijn geconfigureerd.

### **Stappen om** **extractiepaden** te wijzigen:

1. Open de **Extractiepaden**.
2. Maak een nieuw concept door op het **potloodpictogram** te klikken.
3. Selecteer het nieuw aangemaakte concept.
4. Maak een nieuw veld aan of wijzig een bestaand veld.
5. De linkerkant vertegenwoordigt het **DocBits veld-ID**, dat te vinden is in **Instellingen → Globale Instellingen → Documenttypes → Factuur → Velden**.
6. De rechterkant vertegenwoordigt het **pad naar het veld** dat in de transformatie is aangemaakt.
7. Klik op **Opslaan**.

Door deze stappen te volgen, kunt u zorgen voor nauwkeurige gegevensextractie en validatie voor ZUGFeRD-facturen.
