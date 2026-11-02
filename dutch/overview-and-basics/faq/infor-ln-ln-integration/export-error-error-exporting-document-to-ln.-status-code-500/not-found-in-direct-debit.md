# niet gevonden bij automatische incasso

## **Stap 1: Controleer LN-configuratie**

1. Log in op **LN CE**.
2. Ga naar het **Opties** menu en selecteer **Programma uitvoeren**.
3. Typ in het invoerveld **ACP Parameters** en druk op Enter om het programma te openen.
4. Klik op de pijl naast het veld **Huidige set** om de instellingen uit te vouwen.
5. Ga naar de **Matching** sectie.
   * **Controleer de instelling voor Automatische Matching:**
     * Als de **Automatische Matching** is ingesteld op **Matchen met inkoopontvangst**, ga verder naar de volgende stap.
     * Als het **niet** is ingesteld op **Matchen met inkoopontvangst**, maar je krijgt nog steeds deze foutmelding, neem dan contact met ons op.

## **Stap 2: Open DocBits-instellingen**

Als de **Automatische Matching** is ingesteld op **Matchen met inkoopontvangst**, ga verder met de volgende stappen in DocBits:

1. Open **DocBits** en ga naar de **Instellingen** sectie.
2. Navigeer naar **Documentverwerking**.
3. Selecteer **Exporteren**.
4. Klik in de **Exporteren** sectie op het **drie puntjes** icoon naast de export die niet werkt en selecteer **Bewerken**.
5. In het menu **Exportinstellingen bewerken**, klik op **Download het LN-Mapping** bestand.

## **Stap 3: Bewerk LN-Mapping Bestand**

1. Open het gedownloade **LN-Mapping** bestand.
2. Zoek naar het veld **IRF\_PackingSlip**.
   * Als het veld **IRF\_PackingSlip** aanwezig is en ingesteld op **niets** (leeg), update het naar **TF\_packing\_slip**.
   * Als het veld **IRF\_PackingSlip** **niet aanwezig** is, voeg het toe aan het bestand en stel de waarde in op **TF\_packing\_slip**.
3. Voeg voor het veld **InvoiceReceiptFields** **PackingSlip** toe aan de waarden.

Het zou er als volgt uit moeten zien:

<figure><img src="../../../../.gitbook/assets/PackingSlip.png" alt=""><figcaption></figcaption></figure>

## **Stap 4: Voeg het bijgewerkte bestand terug naar DocBits toe**

1. Ga terug naar de **Exporteren** sectie in DocBits waar je eerder het **LN-Mapping** bestand hebt gedownload.
2. Upload het bewerkte **LN-Mapping** bestand met de nieuwe updates.

## Als je nog steeds de foutmelding **Fout bij exporteren van document naar LN** met statuscode **500** tegenkomt, neem dan contact met ons op
