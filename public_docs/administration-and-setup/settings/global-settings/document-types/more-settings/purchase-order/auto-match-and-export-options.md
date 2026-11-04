# Opties voor Auto Match & Export

Drie instellingen aan het einde van de kaart **Inkooporder** bepalen wie de snelkoppelingen voor PO-matching ziet en welke documenten na een match zelf mogen exporteren. Ze gelden telkens voor één documenttype.

<figure><img src="../../../../../../.gitbook/assets/doc-type-settings-po-options-nl.png" alt="De kaart Inkooporder van de documenttype-instellingen met alle PO-opties"><figcaption><p>De kaart Inkooporder. De drie onderstaande opties zijn de laatste drie rijen.</p></figcaption></figure>

## Automatische export toestaan voor niet-overeenkomende inkooporderregels

Automatische export na PO-matching vereist normaal een **volledig gematcht** document. Wanneer deze schakelaar is ingeschakeld, mogen ook documenten met de status **Geen overeenkomende PO-lijnen** automatisch exporteren. Die status betekent dat de inkooporder geen regels heeft waarmee de factuur kan worden gematcht.

* **Uit (standaard):** alleen volledig gematchte documenten exporteren automatisch.
* **Aan:** volledig gematchte documenten en documenten zonder matchbare PO-regels exporteren automatisch.

De schakelaar is alleen van belang wanneer documenten automatisch worden geëxporteerd, bijvoorbeeld met [**Automatische export indien inkooporder 100% overeenkomt**](../../../../document-processing/module/auto-export-if-po-matched-100.md) of een DocFlow-exportkaart. Hij verandert niets aan hoe regels worden gematcht.

## Automatische matching en export zichtbaar voor

Het PO-matchingscherm heeft de actie **Auto Match & Export**. Deze matcht het document en exporteert het direct na de match. Deze instelling bepaalt wie de actie krijgt:

| Waarde | Wie ziet de actie |
| ------ | ----------------- |
| **Alleen beheerder** (standaard) | Beheerders |
| **Alle gebruikers** | Elke gebruiker die het PO-matchingscherm kan openen |

Beheerders zien de actie altijd. De instelling schakelt de functie niet in. De module [**Automatische export indien inkooporder 100% overeenkomt**](../../../../document-processing/module/auto-export-if-po-matched-100.md) moet voor de organisatie actief zijn.

## Gebruik de regels 'Nettobedrag' voor het overeenkomende totaal dat zichtbaar is voor

Het PO-matchingscherm kan het **Totaal overeenkomend** berekenen op basis van het **Nettobedrag** van de gematchte factuurregels in plaats van het zelf uit te rekenen. Deze instelling bepaalt wie die berekening kan inschakelen:

| Waarde | Wie ziet de schakelaar |
| ------ | ---------------------- |
| **Alleen beheerder** (standaard) | Beheerders |
| **Alle gebruikers** | Elke gebruiker die het PO-matchingscherm kan openen |

Wanneer de schakelaar is ingeschakeld, gebruikt het Totaal overeenkomend direct de waarden van het Nettobedrag uit de gematchte factuurregels.
