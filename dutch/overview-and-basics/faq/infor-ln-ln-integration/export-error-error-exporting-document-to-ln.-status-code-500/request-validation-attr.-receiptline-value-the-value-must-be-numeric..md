# de waarde moet numeriek zijn.

## **Stap 1: Onderzoek de Inkooporder**

**1. Controleer de Inkooporder vanaf het Dashboard**

* Als de status van het document **Exportfout** is:
  1. Zoek het document op het dashboard.
  2. Klik erop en selecteer vervolgens de knop **Veldvalidatie** om terug te gaan naar het scherm voor veldvalidatie.
* Als de status van het document **Klaar voor validatie** is:
  1. Klik op het document om rechtstreeks naar het scherm **Veldvalidatie** te gaan.
* Als het document de status **In afwachting van goedkeuring** heeft:
  1. Ga naar het **Goedkeuringsscherm**.
  2. Naast de **Factuurregelitems**, zoek de **Inkoopordertabel**.
  3. Ga naar 3. Controleer de stap voor het leveringsnummer.

**2. Controleer de Inkooporder**

1. Op het scherm **Veldvalidatie**, zorg ervoor dat de juiste Inkooporder is geselecteerd.
2. Zodra de juiste Inkooporder is bevestigd, klik op de Inkooporder naast de geëxtraheerde tabel, om de weergave van de **Inkoopordertabel** te openen.

**3. Controleer het leveringsnummer**

* In de Inkoopordertabel, zoek de kolom **Leveringsnummer**:
  * **Als er een leveringsnummer aanwezig is**, ga naar het **Goedkeuringsscherm** en controleer opnieuw of het aanwezig is, als het aanwezig is ga naar **Stap 3**.
  * **Als er geen leveringsnummer aanwezig is**, volg **Stap 2** om dit probleem aan te pakken.

## Stap 2: Controleer de Inkooporder in LN

Voordat u de Inkooporder naar DocBits stuurt, controleer of het **Leveringsnummer** correct is toegewezen in **LN**. Controleer de details van de **Inkooporder** in **LN** om ervoor te zorgen dat deze volledig en nauwkeurig is. Als het **Leveringsnummer** ontbreekt of onjuist is, kan dit de oorzaak zijn van de exportfout.

Als de **Inkooporder** er correct uitziet en de benodigde details bevat, kunt u doorgaan naar de volgende stap.

## **Stap 3: Open DocBits-instellingen**

1. Open **DocBits** en ga naar de sectie **Instellingen**.
2. Navigeer naar **Documentverwerking**.
3. Selecteer **Export**.
4. In de **Export** sectie, klik op het **drie puntjes** icoon naast de export die niet werkt en selecteer **Bewerken**.
5. In het menu **Exportinstellingen bewerken**, klik op **Download het LN-Mapping** bestand.

## **Stap 3: Bewerk LN-Mappingbestand**

1. Open het gedownloade **LN-Mapping** bestand.
2. Zoek naar het veld **IRF\_ReceiptLine**.
   * Als het veld **IRF\_ReceiptLine** aanwezig is en is ingesteld op **niets** (leeg), update het dan naar **TF\_delivery\_line**.
   * Als het veld **IRF\_ReceiptLine** **niet aanwezig** is, voeg het toe aan het bestand en stel de waarde in op **TF\_delivery\_line**.
3. Voeg voor het veld **InvoiceReceiptFields,** **ReceiptLine** toe aan de waarden.

Het zou er als volgt uit moeten zien:

<figure><img src="../../../../.gitbook/assets/ReceiptLine.png" alt="" width="563"><figcaption></figcaption></figure>

## **Stap 4: Voeg het bijgewerkte bestand terug toe aan DocBits**

1. Ga terug naar de **Export** sectie in DocBits waar u eerder het **LN-Mapping** bestand hebt gedownload.
2. Upload het bewerkte **LN-Mapping** bestand met de nieuwe updates.

## Stap 5: Probeer de export opnieuw

Na bevestiging dat de **Inkooporder** een **Leveringsnummer** heeft en ervoor zorgen dat het **Exportbestand correct** is, volg deze stappen om de export opnieuw te proberen:

1. **Ga terug naar het Dashboard:**
   * Ga terug naar het dashboard en zoek het document met de exportfout.
2. **Probeer het exportproces opnieuw:**
   * Klik op het document met de exportfout.
   * Als de **Inkooporder** een geldig **Leveringsnummer** heeft en het **Exportbestand** correct is, ga verder met het opnieuw proberen van de export.
3. **Controleer het exportresultaat:**
   * Na het opnieuw proberen, controleer het exportproces opnieuw om te zien of het probleem is opgelost en het document niet langer wordt weergegeven als een exportfout.
   * Als de export succesvol is, zou het probleem opgelost moeten zijn.
4. **Verdere onderzoek (indien het probleem aanhoudt):**
   * Als het probleem aanhoudt na het opnieuw proberen van de export, neem dan contact op met de ondersteuning voor verder onderzoek naar mogelijke configuratie- of systeemproblemen.
