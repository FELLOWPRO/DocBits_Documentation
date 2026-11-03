# eSLOG 1.6 en 2.0

**eSLOG 1.6** en **eSLOG 2.0** verschijnen in DocBits als aparte elektronische factuurformaten. Kies de versie die uw inkomende Sloveense facturen gebruiken. De afbeeldingen tonen de Nederlandse interface in een documentatietestorganisatie. Bestaande namen, versies en tijdstippen zijn afgeschermd; de afbeeldingen bewijzen niet dat een factuur van een van beide versies succesvol is verwerkt.

## De configuraties vinden

1. Ga naar **Instellingen → Documenttypen → Factuur → E-Doc**.
2. Vouw **E-SLOG 1.6** of **E-SLOG 2.0** open. Elk formaat heeft zijn eigen drie items.

<figure><img src="../../../../../.gitbook/assets/dbdc-106-eslog-16-native-nl-20261101.png" alt="Nederlandse E-Doc-lijst voor E-SLOG 1.6 met drie configuratierijen; bestaande namen, versies en tijdstippen afgeschermd"><figcaption>E-SLOG 1.6: van boven naar beneden Transformatie, Voorbeeld en Extractiepaden. Deze testweergave bevat twee rijen Standaard en één bestaande rij Aangepast. Namen, versies en tijdstippen zijn afgeschermd.</figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/dbdc-106-eslog-20-native-nl-20261101.png" alt="Nederlandse E-Doc-lijst voor E-SLOG 2.0 met drie configuratierijen; bestaande namen, versies en tijdstippen afgeschermd"><figcaption>E-SLOG 2.0: aparte items voor dezelfde drie stappen, hier alle drie aangeduid als Standaard. Namen, versies en tijdstippen zijn afgeschermd.</figcaption></figure>

| Item | Wat het stuurt | Volgende handleiding |
| --- | --- | --- |
| **TRANSFORMATION (XSLT)** | Zet de brondata van het formaat om naar gestructureerde XML. | [Transformatie](edi/edi-transformation-file-guide.md) |
| **PREVIEW (XSLT)** | Bepaalt de leesbare documentweergave. | [Voorbeeld](edi/edi-preview-file-guide.md) |
| **EXTRACTION PATHS (JSON)** | Wijst XML-waarden toe aan DocBits-velden en tabelkolommen. | [Extractiepaden](edi/edi-extraction-paths-file-guide.md) |

Klik op een rij om de versies en configuratie ervan te zien. **Standaard** markeert het meegeleverde item; **Aangepast** een eigen variant voor de organisatie. **Laatst gewijzigd op** toont wanneer dat item voor het laatst is gewijzigd. De knop **Nieuw** opent het formulier voor een extra configuratie-item. Het menu met de drie puntjes van een standaardrij biedt **Aanpassen** (maakt een organisatieafhankelijke kopie) en **Verwijderen**; controleer de geselecteerde rij zorgvuldig voordat u Verwijderen gebruikt.

Opent u een configuratie, dan maakt het potloodicoon naast een actieve versie een concept. Controleer een concept met het testpaneel **Voorvertoning** en een representatieve geüploade document-ID voordat u het activeert met het vinkje. Het prullenbakicoon van een concept verwijdert dat concept. De daadwerkelijke veldnamen en XML-padnamen hangen af van uw eSLOG-bestand; gebruik de bijbehorende handleiding hierboven voor de details in de editor.
