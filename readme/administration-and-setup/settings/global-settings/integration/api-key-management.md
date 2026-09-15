---
description: >-
  Hoe u de API keys vindt en aanmaakt waarmee andere systemen toegang tot DocBits
  krijgen
---

# API Key Management

Met een API key kan een ander systeem — uw ERP, een script of een partnerapplicatie — met DocBits praten zonder dat een gebruiker inlogt. Uw organisatie kan zoveel sleutels aanhouden als u nodig hebt, en elke sleutel wordt apart beheerd: geef die een eigen naam, bepaal of die verloopt, en trek die afzonderlijk in als die ooit wordt blootgesteld.

Doordat elke integratie een eigen sleutel kan hebben, kunt u er één uitschakelen zonder de andere te storen.

## Het beheer van API keys openen

Ga naar **Settings** en selecteer **Integration & SSO** onder **System & Administration**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/api-key-settings-overview.png)

De sectie **API Key** bovenaan de pagina toont elke sleutel die uw organisatie heeft.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/api-key-list.png)

## De lijst begrijpen

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/api-key-list-row.png)

| Kolom | Wat die u vertelt |
| --- | --- |
| **Key** | De eerste tekens van de sleutel, gevolgd door `****`. De rest wordt na het aanmaken nooit meer getoond — zie [Een API-sleutel aanmaken](#een-api-sleutel-aanmaken). |
| **Name** | De naam die u de sleutel hebt gegeven, met de beschrijving eronder. |
| **Expires** | De datum waarop de sleutel stopt met werken, of **Never** als u er geen hebt ingesteld. |
| **Last Used** | Wanneer er voor het laatst een verzoek met deze sleutel binnenkwam. **Never used** betekent dat nog geen enkel systeem die heeft gebruikt — handig om sleutels op te sporen die u veilig kunt verwijderen. |
| **Status** | **Active** betekent dat de sleutel werkt. Een ingetrokken sleutel is permanent uitgeschakeld. |
| **Actions** | Het menu met drie puntjes, waar u de sleutel kunt intrekken. |

Als u meer sleutels hebt dan er op één pagina passen, gebruik dan de paginabesturing onderaan de lijst.

{% hint style="info" %}
**Last Used** is de snelste manier om sleutels te vinden die niemand meer nodig heeft. Een sleutel die nooit is gebruikt, of al maanden niet, is een goede kandidaat om in te trekken.
{% endhint %}

## Een API-sleutel aanmaken

1. Klik op **+ Create API Key** rechtsboven in de sectie API Keys.
2. Vul het dialoogvenster in:

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/api-key-create-dialog.png)

| Veld | Wat in te vullen |
| --- | --- |
| **Key Name** | Verplicht. Noem die naar het systeem dat die gaat gebruiken — `M3 Production`, `Invoice Import Script` — zodat u later kunt zien bij welke integratie een sleutel hoort. |
| **Description** | Optioneel. Ruimte voor een notitie over waar de sleutel voor is of wie die heeft ingesteld. |
| **Expiration** | Kies een vervaldatum, of laat die op **Never expires** staan. Een vervaldatum is de veiligere keuze: de sleutel trekt zichzelf terug als de integratie ooit wordt vergeten. |

3. Klik op **Create**. DocBits toont u de nieuwe sleutel:

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/api-key-created.png)

4. Kopieer de sleutel met het kopieerpictogram en plak die rechtstreeks in het systeem dat die gaat gebruiken, of in uw wachtwoordmanager.
5. Vink **I have copied and saved this key** aan en klik op **Done**.

{% hint style="danger" %}
**De volledige sleutel wordt maar één keer getoond.** DocBits slaat die versleuteld op in een vorm die niet terug te rekenen is naar het origineel, dus niemand — uw beheerders niet en DocBits-support niet — kan die daarna nog opzoeken. Raakt u die kwijt, trek de sleutel dan in en maak een nieuwe aan.
{% endhint %}

Behandel de sleutel als een wachtwoord. Wie die heeft, kan handelen met de documenten en gegevens van uw organisatie.
