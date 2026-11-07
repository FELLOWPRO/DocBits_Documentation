# Een nieuwe kolom toevoegen

Voeg een kolom toe wanneer per regelitem een waarde moet worden vastgelegd die de standaardkolommen niet dekken: een kostenplaats, een projectnummer, een intern artikelnummer.

## Voordat u begint

* Bepaal bij welke **tabel** de kolom hoort. De meeste documenttypen hebben één tabel (bijvoorbeeld `INVOICE_TABLE`). Als de lijst leeg is, klikt u eerst op **Nieuwe tabel maken**; het dialoogvenster vraagt alleen om een tabelnaam.
* Bepaal het **type**: `AMOUNT` voor geldbedragen, `NUMBER` voor hoeveelheden, `DATE`, `BOOLEAN` voor ja/nee, `CURRENCY` voor een ISO-valutacode, `STRING` voor al het andere. Het type kan na het opslaan niet meer worden gewijzigd.
* Controleer of er al een **standaardkolom** met dezelfde betekenis bestaat die verborgen is. Verborgen kolommen staan in de lijst met de vlag *Hidden* ingeschakeld; maak die zichtbaar in plaats van een duplicaat aan te maken.

## Stappen

1. Open **Settings → Document Processing → Document Types → Table Columns**.
2. Klik op **Nieuwe tabelkolom toevoegen**.

<figure><img src="../../../../../.gitbook/assets/table-columns_add-dialog.png" alt="Dialoogvenster Nieuwe tabelkolom toevoegen met Titel, Is kolom verplicht, Selecteer kolomtype en Selecteer tabel"><figcaption><p>Nieuwe tabelkolom toevoegen</p></figcaption></figure>

3. Vul het dialoogvenster in:

| Veld | Wat u invoert |
|---|---|
| **Title** | Label dat de gebruiker op het validatiescherm ziet, bijvoorbeeld `Cost Centre`. Alleen letters en cijfers. DocBits leidt hieruit de technische *Kolomnaam* af (`COST_CENTRE`). |
| **Is kolom verplicht?** | Vink aan wanneer het document niet mag worden goedgekeurd zolang de kolom in een rij leeg is. |
| **Selecteer kolomtype** | Zie de typelijst hierboven. |
| **Selecteer tabel** | De tabel die de kolom krijgt. |

4. Klik op **Doorgaan**. Een bevestigingsvenster wijst erop dat de nieuwe kolom geldt voor **alle toekomstige facturen van elke leverancier**, niet alleen voor het geopende document.

<figure><img src="../../../../../.gitbook/assets/mef178-column-create-confirm-nl.png" alt="Bevestigingsvenster ‘Een nieuwe tabelkolom aanmaken?’ met de knoppen Annuleren en Kolom maken"><figcaption><p>Bevestig voordat de kolom voor alle leveranciers wordt aangemaakt.</p></figcaption></figure>

5. Controleer na het aanmaken de instellingen in de lijst. Alleen-lezen en Verborgen staan aanvankelijk uit. Use AI begint op Standaard; een eigen kolom wordt daarmee normaal niet gevraagd. Kies Ja als gestructureerde extractie haar moet vragen.

## Na het toevoegen

* De kolom is **leeg op bestaande documenten**. Ze wordt gevuld op documenten die na de wijziging worden geüpload of opnieuw gestart.
* Voor leveranciers met **getrainde regels** opent u een van hun documenten in de tabeltraining en koppelt u de nieuwe kolom; anders blijft de kolom voor die leverancier leeg. Zie [Tabellen en kolommen definiëren](../../../../setup/document-training/training-line-fields-table-training/defining-tables-and-columns.md).
* Zet voor gestructureerde AI-extractie Use AI van de eigen kolom op Ja en controleer het voorbeeld. Alleen de kolom aanmaken vraagt haar niet aan. Controleer leverancierskoppelingen en instructies, verwerk een testdocument opnieuw en controleer het resultaat.
* Voeg de kolom toe aan de **exportmapping** als het ERP de kolom moet ontvangen, zie [Exporteren](../../../document-processing/export.md).

## Meldingen

| Melding | Betekenis |
|---|---|
| *Column name already exists* | Een kolom met deze technische naam staat al in de tabel. Kies een andere titel. |
| *Column name already exists – Please activate it in Table Column settings* | Een verborgen standaardkolom heeft deze naam. Schakel de vlag *Hidden* van die kolom uit in plaats van een nieuwe kolom aan te maken. |
| *No table exists. Please create table before creating columns.* | Het documenttype heeft nog geen tabel: klik eerst op **Nieuwe tabel maken**. |

[Structured Output voor tabellen](../../../../../end-user-and-partner-section/end-user-section/ai-table/structured-output.md).
