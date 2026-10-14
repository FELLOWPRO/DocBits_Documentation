# Veldeigenschappen configureren

Gebruik **Settings → Document Types → Fields** om te bepalen hoe velden zich gedragen voor een documenttype. Selecteer eerst het documenttype; het onderstaande voorbeeld toont **Invoice** in de Engelse interface.

<figure><img src="../../../../../.gitbook/assets/dbdc155-field-properties-overview-en.png" alt="Engelse veldinstellingen voor Invoice met herkenningsdrempels, zoekfunctie, kolommen met veldeigenschappen en Save Settings"><figcaption>Veldinstellingen voor Invoice in een DocBits-sandboxorganisatie.</figcaption></figure>

## Een veld zoeken en de eigenschappen wijzigen

1. Voer in **Search by Name** de veldnaam of het label in. Hiermee wordt de lijst gefilterd; het veld zelf wordt niet gewijzigd.
2. Zoek de rij van het veld. **Invoice number** heeft bijvoorbeeld de technische naam `invoice_id`.
3. Pas de bedieningselementen in die rij aan en selecteer vervolgens **Save Settings**. Dezelfde opslaanknop is beschikbaar boven en onder de tabel.

<figure><img src="../../../../../.gitbook/assets/dbdc155-field-properties-filtered-en.png" alt="Engels veld Invoice number met de bedieningselementen Required, Read Only, Hidden, Force Validation, Use AI, OCR en Match Score"><figcaption>De rij Invoice number na het zoeken naar `invoice_id`.</figcaption></figure>

| Bedieningselement | Waarvoor u het gebruikt |
| --- | --- |
| **Required** | Markeer informatie die aanwezig moet zijn voor de validatie. Controleer het validatieresultaat van het document nadat u deze instelling hebt gewijzigd. |
| **Read Only** | Toon een veld zonder dat gebruikers de waarde kunnen bewerken. |
| **Hidden** | Houd het veld buiten de normale documentweergave. |
| **Force Validation** | Eis dat het veld de validatie doorstaat. Configureer gedetailleerde regels apart; dit selectievakje is geen regeleditor. |
| **Use AI** | Schakel AI-extractie voor dit veld in of uit. De rij toont of extractie is aangevraagd. |
| **OCR** | Voer de OCR-betrouwbaarheidsdrempel van het veld in. Dit is een getal, geen aan/uit-schakelaar en geen taalinstelling. |
| **Match Score** | Voer de matchingdrempel van het veld in. Dit is een getal, geen aan/uit-schakelaar. |

De schuifregelaars **OCR** en **Match Score** onder **Recognition Settings** passen waarden toe op de hele veldenlijst. De selectievakjes direct onder de kolomtitels passen **Required**, **Read Only**, **Hidden** of **Force Validation** toe op de hele lijst. Controleer de betreffende rijen voordat u **Save Settings** selecteert. **Restore Defaults** zet de veldconfiguratie terug; gebruik dit alleen als u uw wijzigingen wilt vervangen.

## Overige bedieningselementen in deze weergave

- **Create new group** en **Create field** voegen een groep of een veld toe. Zie [Velden toevoegen en bewerken](adding-and-editing-fields.md).
- **Master Data Settings** opent de [configuratie van stamgegevens](master-data-settings.md).
- De meest linkse selectievakjes selecteren velden. Het aangrenzende menu biedt **Reassign Field Group** voor geselecteerde velden.
- De plusknop **Formula** opent de formule-editor voor dat veld. Het pictogram **info** toont veldinformatie. Het verwijderpictogram is niet beschikbaar voor standaardvelden.

Zie voor meer informatie over validatie en matching [Validatie en Match Score instellen](setting-validation-and-match-score.md).
