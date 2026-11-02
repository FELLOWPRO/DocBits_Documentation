# Barcode Extracties

## Overzicht

Deze functie maakt automatische detectie van barcodes op documenten mogelijk. Wanneer geactiveerd, worden alle ondersteunde barcodetypen gescand en geëxtraheerd tijdens de verwerking.

## Hoe Barcode Extractie In te Schakelen

Volg deze stappen om de functie Barcode Extractie in te schakelen:

1. **Navigeer naar Instellingen**:
   * Ga vanuit het Dashboard naar **Instellingen**.
   * Selecteer **Documentverwerking** en kies vervolgens **Module**.
2. **Schakel de Functie In**:
   * Scroll naar beneden om de optie **Bar-Code Extraction** te vinden.
   * Gebruik de schuifregelaar om Barcode Extractie in te schakelen.\\

## **Aanvullende Instellingen**

### **Barcode Toewijzing**

#### **Doel:** Stelt validators in staat om tijdens de veldvalidatie handmatig een geëxtraheerde barcodewaarde aan een specifiek documentveld toe te wijzen.

#### Hoe **Barcode Toewijzing** In te Schakelen

Volg deze stappen om de functie **Barcode Assignment** in te schakelen:

1. **Navigeer naar Instellingen**:
   * Ga vanuit het Dashboard naar **Instellingen**.
   * Selecteer **Documentverwerking** en kies vervolgens **Module**.
2. **Schakel de Functie In**:
   * Scroll naar beneden om de optie **Barcode Assignment** te vinden.
   * Gebruik de schuifregelaar om **Barcode Assignment** in te schakelen.\\

#### **Hoe het werkt:**

* Schakelt een optie "Assign Barcode" in op het veldvalidatiescherm.\\
* Gebruikers kunnen een gedetecteerde barcodewaarde selecteren en deze toewijzen aan een documentveld zoals PO Number of Invoice Number.\\

### Splitsen van Document per Barcode / QR-Code

**Doel:** Splitst documenten met meerdere pagina's automatisch in afzonderlijke documenten op basis van de aanwezigheid van specifieke barcodes of QR-codes.

#### Hoe Splitsen van Document per Barcode / QR-Code In te Schakelen

Volg deze stappen om de functie **Split of Document by Barcode / QR Code** in te schakelen:

1. **Navigeer naar Instellingen**:
   * Ga vanuit het Dashboard naar **Instellingen**.
   * Selecteer **Documentverwerking** en kies vervolgens **Classificatie en Extractie**.
2. **Schakel de Functie In**:
   * Zoek de optie **Document Splitting**.
   * Selecteer voor **Split** de optie **Split by Barcode / QR Code**.
   * Kies voor **Barcode Type** een of meer ondersteunde barcodetypen uit de lijst.
   * Definieer voor **Barcode Pattern** het patroon dat een splitsing moet activeren. U kunt een **reguliere expressie** (regex) gebruiken om dynamische barcodewaarden te matchen.

**Hoe het werkt:**

* U selecteert de barcodetypen die een splitsing moeten activeren.
* U definieert een patroon waaraan de barcode moet voldoen. Dit kan een vaste tekenreeks of een regex zijn (bijv. `^INV\d{6}$` om barcodes zoals `INV123456` te matchen).
* Tijdens de documentverwerking wordt telkens wanneer een pagina een overeenkomende barcode bevat, een **nieuw document aangemaakt** dat bij die pagina begint.

### Ondersteunde Codetypen

Zie de [Overzichtspagina](./) voor de volledige lijst van ondersteunde barcode- en QR-codeformaten.
