# Fuzzy Data-configuratie met Mastergegevens

## **Overzicht**

Elk documenttype heeft zijn eigen standaardconfiguraties en moet apart worden ingesteld. Hoewel dit voorbeeld de configuratie voor **Facturen** uitlegt, is hetzelfde proces van toepassing op alle documenttypen.

## Om Fuzzy Data te configureren, navigeer naar:

Instellingen → Globale instellingen → Documenttypen → Factuur → Velden → Mastergegevensinstellingen → Mastergegevens opzoeken

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fhnn2NcPGzVkUO0mLQWTy%252Fimage.png%3Falt%3Dmedia%26token%3De2f87385-fc48-4149-9bef-ca917a7328bd\&width=768\&dpr=4\&quality=100\&sign=116ee1da\&sv=2)

## **Standaard opzoekingen**

Er zijn **vier standaard opzoekgroepen** voor facturen:

1. **Bedrijfsgegevens**
2. **Inkooporderkop**
3. **Leverancier**
4. **Belastingcode**

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F4VxYFu8M62dXi6qGsPl3%252Fimage.png%3Falt%3Dmedia%26token%3Db2bc4690-805b-4b19-aa89-73f315889d88\&width=768\&dpr=4\&quality=100\&sign=835f513a\&sv=2)

Elke groep bevat specifieke velden. Klik op een groep om deze te **uitklappen** en de velden te bekijken. Standaard opzoekgroepen zijn gelabeld met een **"Standaard" tag**.

## **Status van opzoekconfiguratie**

* **Actieve configuraties** zijn gemarkeerd met een **"Geactiveerd" tag**.
* **Gedeactiveerde configuraties** zijn gemarkeerd met een **"Gedeactiveerd" tag**.

## **Vereiste: Importeren van Mastergegevens**

Om Fuzzy Data correct te laten functioneren, moeten de relevante **mastergegevens** worden geïmporteerd. Zonder dit heeft het systeem geen referentiegegevens om te gebruiken. Hier is hoe u mastergegevens importeert:

{% content-ref url="../../../infor-integration-and-configuration/importing-customer-master-data/" %}
[importing-customer-master-data](../../../infor-integration-and-configuration/importing-customer-master-data/)
{% endcontent-ref %}

## **Beheer van opzoekgroepen**

Elke opzoekgroep is **standaard geactiveerd** maar kan worden aangepast door op de drie puntjes te klikken:

* **Deactiveren** → Deactiveert een groep. _(Alleen beschikbaar voor geactiveerde groepen)_
* **Activeren** → Activeert een groep. _(Alleen beschikbaar voor gedeactiveerde groepen)_
* **Dupliceren** → Maakt een kopie die kan worden aangepast zonder de originele te beïnvloeden.
* **Weergeven** → Toont informatie zoals het **documenttype** waartoe het behoort en de **opzoektafel** die het gebruikt. _(Alleen beschikbaar voor standaardgroepen)_
* **Bewerken** → Beschikbaar voor **niet-standaard** groepen. Hiermee kunnen groepsdetails worden aangepast.
* **Verwijderen** → Verwijdert de groep volledig. _(Alleen voor niet-standaard groepen)_

## **Een nieuwe opzoekconfiguratie maken**

Er zijn **twee manieren** om een opzoekconfiguratie te maken:

1.  **Dupliceer een bestaande opzoek**

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FZUlPcWGrx1oITQS3tgZP%252Fimage.png%3Falt%3Dmedia%26token%3D59fb300d-836e-40d0-84b7-4a405cf7f321\&width=768\&dpr=4\&quality=100\&sign=3442db8f\&sv=2)

    * Dit kopieert alle informatie en velden van een bestaande groep.
    * U hoeft alleen een **nieuwe naam** op te geven.
2.  **Maak een opzoek vanaf nul**

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FNbEpo2p5Q8D1d7DUchBF%252Fimage.png%3Falt%3Dmedia%26token%3D401314b5-44d0-47df-b3e6-69fea83cce82\&width=768\&dpr=4\&quality=100\&sign=1d0ce322\&sv=2)

    * Klik op **"Opzoekconfiguratie maken"**.
    * Vul de vereiste details in:
      * **Configuratienaam**
      * **Opzoektafel** (Te gebruiken mastergegevenstabel)
      * **Conflictbehandelaar** (Kies een: Beste score, Geen retour, Eerste retour)
      * **Contexttype** (Kop of regel) context nodig
      * **Alles matchen** (Checkbox-optie) context nodig

## **Beheer van velden binnen een opzoekgroep**

Elke groep bevat velden die kunnen worden **toegevoegd, verwijderd, bewerkt of bekeken**, afhankelijk van of het standaardvelden of aangepaste velden zijn.

### **Standaardvelden**

*   Gemarkeerd met een **"Standaard" tag**.

    <div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fh37McVpB0tBo5wqiAttR%252Fimage.png%3Falt%3Dmedia%26token%3Dcabce083-83a5-4881-a64f-88a8757df49b&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=b3739019&#x26;sv=2" alt="" width="375"></div>
* **Alleen te bekijken**, niet te bewerken of verwijderen.

### **Niet-standaardvelden**

* **Kunnen worden bewerkt of verwijderd** door op de drie puntjes te klikken en **Bewerken** of **Verwijderen** te selecteren.

### **Een nieuw veld toevoegen**

**Opmerking:** U kunt velden maken binnen standaard Opzoekconfiguraties.

Om een nieuw veld toe te voegen binnen een groep:

1.  Klik op **"Maken"** binnen de relevante groep.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FvmIXTEQQHKKNbvTJj1b4%252Fimage.png%3Falt%3Dmedia%26token%3D8569867b-9f5b-4865-90bd-f2e41e846979\&width=768\&dpr=4\&quality=100\&sign=603cb7df\&sv=2)
2. Geef de volgende details op:
   * **Opzoekveld** → Kolomnaam uit de mastergegevens opzoektafel.
   * **Validatieveld** → Overeenkomstig DocBits-veld.
   * **Ouder veld** → _(Meer details nodig)_
   * **Zoekoperator** → Kies een:
     * Slim
     * Bevat
     * Exact
     * Begint met
     * Eindigt op
   * **Selectievakjes:**
     * **Automatisch activeren** → Wanneer ingeschakeld, als een ander veld in een andere opzoekconfiguratie dezelfde kolom deelt, wordt dit veld **automatisch** bijgewerkt telkens wanneer het andere veld wordt bijgewerkt
     * **Doorzoekbaar** → Activeert het veld als een **Fuzzy Data**-veld, waardoor zoekopdrachten mogelijk zijn in de mastergegevensopzoek (blauw pictogram in validatiescherm).

## **Laatste stap: Velden toevoegen aan het ontwerp**

Na het configureren van Fuzzy Data-velden, **zorg ervoor dat u ze toevoegt aan het ontwerp met de Layout Builder**. Als velden niet aan het ontwerp worden toegevoegd, zijn ze niet beschikbaar voor gebruik.

{% content-ref url="../../settings/global-settings/document-types/layout-manager/" %}
[layout-manager](../../settings/global-settings/document-types/layout-manager/)
{% endcontent-ref %}

## **Hoe DocBits één leverancier kiest**

Wanneer een document binnenkomt, zoekt DocBits de leverancier in uw mastergegevens. Drie instellingen bepalen het resultaat. Dit hoofdstuk legt ze stap voor stap uit, met voorbeelden.

### **Stap 1 — Welke velden voor de zoekopdracht worden gebruikt**

DocBits gebruikt een veld alleen voor de zoekopdracht als beide punten kloppen:

* het veld is aangevinkt als **Doorzoekbaar (Searchable)** of **Auto Trigger** in de opzoekconfiguratie, en
* het veld heeft een waarde op het document.

Hoe de waarde in het veld is gekomen, maakt niet uit. Een getraind veld, een door AI gevuld veld en een door een gebruiker getypte waarde worden hetzelfde behandeld.

{% hint style="warning" %}
**Doorzoekbaar doet twee dingen.** Het toont het blauwe zoekicoon in het validatiescherm **en** het voegt het veld toe aan de automatische leverancierszoekopdracht. Een veld dat alleen handmatig doorzocht moet worden, blijft uitgevinkt.
{% endhint %}

### **Stap 2 — Eén zoekopdracht, niet één per veld**

DocBits zoekt **niet** per veld apart. Het bouwt **één** zoekopdracht over alle gebruikte velden. **Alles matchen (Match All)** bepaalt hoe ze worden gecombineerd:

* **Alles matchen uit** (standaard) → "vind elke leverancier die overeenkomt met het btw-nummer **OF** met de leveranciersnaam". Dit geeft een **langere** lijst.
* **Alles matchen aan** → "vind elke leverancier die overeenkomt met het btw-nummer **EN** met de leveranciersnaam". Dit geeft een **kortere** lijst.

Houd er ook rekening mee dat de zoekoperatoren **Smart** en **Contains** naar een deel van de tekst zoeken. De naam "Meier" vindt ook "Meier Bau GmbH" en "Meier & Sons Ltd". Een leveranciersnaam vindt daarom vaak meerdere leveranciers.

### **Stap 3 — Wat gebeurt er als de lijst meerdere leveranciers bevat**

De **Conflictafhandeling (Conflict Handler)** beslist:

* **Best Score** → neemt de leverancier die met de meeste velden overeenkomt. Laat de leverancier nooit leeg.
* **Return None** → laat de leverancier leeg, zodat een gebruiker hem kiest.
* **Return First** → neemt de eerste leverancier uit de lijst.

### **Voorbeelden**

In alle voorbeelden heeft het document een btw-nummer en een leveranciersnaam, en beide velden zijn **Doorzoekbaar**.

<table><thead><tr><th width="150">Btw-nummer vindt</th><th width="150">Naam vindt</th><th width="150">Alles matchen uit + Return None</th><th width="150">Alles matchen aan + Return None</th><th width="150">Alles matchen uit + Best Score</th></tr></thead><tbody>
<tr><td>alleen A</td><td>A en B</td><td>leeg</td><td><strong>A</strong></td><td><strong>A</strong></td></tr>
<tr><td>A en B</td><td>alleen B</td><td>leeg</td><td><strong>B</strong></td><td><strong>B</strong></td></tr>
<tr><td>A, B en C</td><td>C, D en E</td><td>leeg</td><td><strong>C</strong></td><td><strong>C</strong></td></tr>
<tr><td>A, B en C</td><td>B, C en D</td><td>leeg</td><td>leeg</td><td>B of C, niet betrouwbaar</td></tr>
<tr><td>alleen A</td><td>niets</td><td><strong>A</strong></td><td>leeg</td><td><strong>A</strong></td></tr>
</tbody></table>

Hoe u de tabel leest:

* **Rij 1 tot 3** is het normale geval. Eén veld is uniek, het andere niet. Met **Alles matchen uit** bevat de lijst meerdere leveranciers en laat **Return None** het veld leeg. **Alles matchen aan** houdt alleen de leverancier over die met beide velden overeenkomt en vindt hem.
* **Rij 4** heeft helemaal geen unieke leverancier. Het veld leeg laten is juist. **Best Score** kiest er toch een, en dat kan de verkeerde zijn.
* **Rij 5** is het risico van **Alles matchen aan**. Zie de waarschuwing hieronder.

{% hint style="warning" %}
**Alles matchen kan een leverancier verliezen.** Met **Alles matchen aan** moet elk gebruikt veld overeenkomen. Als één veld een waarde bevat die niet in uw mastergegevens bestaat — een typefout, een oude bedrijfsnaam, een van de pagina gelezen waarde — levert de hele zoekopdracht niets op en wordt geen leverancier gevonden, terwijl het btw-nummer alleen de juiste had gevonden.
{% endhint %}

### **Een leverancier werd eerder herkend en nu niet meer**

Bijna altijd levert één veld extra nu een waarde. Controleer in deze volgorde:

1. Open het document. Welk veld van de opzoekgroep bevat nu een waarde die eerder leeg was?
2. Open de opzoekconfiguratie. Is dat veld aangevinkt als **Doorzoekbaar** of **Auto Trigger**? Zo ja, dan doet het nu mee aan de zoekopdracht en maakt het de resultatenlijst langer.
3. Kies een van de drie oplossingen:
   * **Het veld mag niet meedoen aan de zoekopdracht** → vink **Doorzoekbaar** en **Auto Trigger** uit voor dat veld. Het veld behoudt zijn waarde op het document en blijft zichtbaar voor de gebruiker. Dit is de kleinste wijziging.
   * **Het veld moet meedoen** → zet **Alles matchen** aan, maar lees eerst de waarschuwing hierboven.
   * **U wilt in elk geval een leverancier** → zet de **Conflictafhandeling** op **Best Score**. Accepteer dat er dan een verkeerde leverancier gekozen kan worden in plaats van een leeg veld.
