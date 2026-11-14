# Instelling Validatie en Overeenkomstscore

In **Velden** kunt u de validatie- en herkenningsdrempels voor een documenttype instellen. Deze pagina gebruikt **Factuur** in een testorganisatie van de documentatie. Ze legt het huidige selectievakje **FORCE VALIDATIE** en de besturingselementen voor de **OVEREENKOMSTSCORE** uit.

## De veldinstellingen openen

1. Ga naar **Instellingen → Documenttypen → Factuur → Velden**.
2. Gebruik **Zoeken op naam** om een veld te vinden, bijvoorbeeld `invoice_number` (weergegeven als **Factuurnummer**).
3. Controleer de veldrij voordat u een instelling wijzigt. **VEREIST**, **Alleen Lezen**, **Verborgen** en **FORCE VALIDATIE** zijn afzonderlijke selectievakjes.

<figure><img src="../../../../../.gitbook/assets/fields-validation-match-score-overview-nl-20261111.png" alt="Nederlandse pagina Velden met de kolommen VEREIST, Alleen Lezen, Verborgen, FORCE VALIDATIE, OCR en OVEREENKOMSTSCORE, de groep Factuurgegevens en de rij Factuurnummer"><figcaption><p>De herkenningsinstellingen en de veldkolommen staan boven de veldenlijst.</p></figcaption></figure>

## Force Validatie

Vink **FORCE VALIDATIE** aan in de veldrij om voor dat veld een strengere validatie toe te passen. Het selectievakje staat los van **VEREIST**: een veld als vereist markeren vinkt Force Validatie niet automatisch aan. Het selectievakje kan niet beschikbaar zijn wanneer een veld verborgen of alleen-lezen is. Klik op **Instellingen opslaan** nadat u de veldconfiguratie hebt gewijzigd.

De oude instructies stelden voor om hier numerieke grenzen of reguliere expressies in te voeren. De huidige Velden-tabel toont geen regeleditor in de cel FORCE VALIDATIE. Voor veldspecifieke regels zie [Veldeigenschappen configureren](configuring-field-properties-1.md).

## Overeenkomstscore

**OVEREENKOMSTSCORE** is een numerieke drempelwaarde, geen vaste referentiewaarde. De schuifregelaar **OVEREENKOMSTSCORE** onder **HERKENNINGSINSTELLINGEN** past zijn waarde toe op de veldrijen van het documenttype; gebruik de invoer **OVEREENKOMSTSCORE** van een veldrij voor een individuele waarde. In de testorganisatie toont de schuifregelaar **80** en toont de rij `invoice_number` **60**. Controleer de betrokken velden en klik vervolgens op **Instellingen opslaan**.

<figure><img src="../../../../../.gitbook/assets/fields-validation-match-score-invoice-number-nl-20261111.png" alt="Gefilterde rij Factuurnummer (invoice_number) met aangevinkte vakjes VEREIST en FORCE VALIDATIE en de waarden 60 bij OCR en OVEREENKOMSTSCORE"><figcaption><p>Zoek een veld om FORCE VALIDATIE en de overeenkomstscore van die rij te controleren.</p></figcaption></figure>

**OCR** is een afzonderlijke herkenningsdrempel naast de Overeenkomstscore. **STANDAARDINSTELLINGEN HERSTELLEN** zet de instellingen terug; gebruik het alleen wanneer u uw eigen drempelwaarden wilt verwijderen. Voor andere veldopties zie het [Velden-overzicht](README.md).

## Overzicht op veldniveau

<figure><img src="../../../../../.gitbook/assets/fields-validation-match-score-field-level-nl-20261111.png" alt="Velden van de groep Leveranciergegevens met per rij eigen waarden voor FORCE VALIDATIE, OCR en OVEREENKOMSTSCORE"><figcaption><p>Elke veldrij heeft eigen waarden voor OCR en OVEREENKOMSTSCORE.</p></figcaption></figure>

Force Validatie, OCR en Overeenkomstscore zijn afzonderlijke instellingen. De overeenkomstscore is een numerieke drempelwaarde; het is geen vaste referentietekst of een kiezer voor een vergelijkingswaarde.
