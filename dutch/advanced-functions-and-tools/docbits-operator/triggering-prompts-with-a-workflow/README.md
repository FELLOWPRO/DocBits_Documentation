# Het activeren van prompts met een workflow

Deze handleiding legt uit hoe je een DocBits-workflow configureert om automatisch een opgeslagen prompt te activeren. Hiermee kun je Operator-prompts integreren in documentverwerkingsstromen zonder handmatige invoer.

## Stap 1: Maak een prompt aan

Voordat je een prompt aan een workflow koppelt:

* Zorg ervoor dat je prompt al is aangemaakt
* Neem alle benodigde **variabelen** op in de prompttekst.

Als je hulp nodig hebt bij het schrijven of opslaan van prompts, raadpleeg dan de [Prompt Writing Guide](../prompt-writing-guide.md) en [Operator Interface Overview](../).

## Stap 2: Stel de workflow in

Voordat je de Operator Prompt-kaart configureert, zorg ervoor dat je workflow correct is aangemaakt.

1. Ga naar de **Workflow Builder** in de DocBits-interface.
2. Maak een nieuwe workflow aan of open een bestaande.
3. Definieer de **triggercondities** - deze bepalen wanneer de workflow zal starten (bijv. documenttype, status, veld aanwezigheid, enz.).
4. Voeg de benodigde **actiestappen** toe aan je workflow zoals vereist.

<div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fd3qJJhFDHTXDUfUedjaF%252Fimage.png%3Falt%3Dmedia%26token%3D310f9e9c-9e79-4987-af01-2d914f1abbe7&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=873cf566&#x26;sv=2" alt="" width="375"></div>

## Stap 3: Configureer de Operator Prompt-kaart in de workflow

In de Workflow Builder, gebruik de **Operator Prompt-kaart** om een prompt te configureren die moet worden uitgevoerd wanneer aan de voorwaarden van de workflow is voldaan.

<div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fg11jtpdL4j3mJveYvWSX%252Fimage.png%3Falt%3Dmedia%26token%3Db208669e-b6a8-4879-b08b-d9ba353e908d&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=974876f7&#x26;sv=2" alt="" width="375"></div>

### Belangrijke configuratieopties

* **Script:** Selecteer de opgeslagen **Organisatieprompt** die moet worden uitgevoerd.
* **Scriptgegevens (Variabelen):** Als de geselecteerde prompt variabelen bevat, definieer dan hier hun waarden met behulp van key-value-paren.
  * Als een variabele hier leeg wordt gelaten, zal het systeem proberen deze automatisch in te vullen **vanuit het document**.
  * Om dit te laten werken, moet de variabelenaam in de prompt **exact overeenkomen** met de **veld-ID** van het documentattribuut.
* **Max Steps:** Definieer het maximale aantal stappen dat de operator mag uitvoeren tijdens deze prompt.
* **Max Retries:** Stel in hoe vaak het systeem de prompt opnieuw moet proberen in geval van mislukking.
* **Uitvoeringsmodus:** Kies of de prompt moet worden uitgevoerd:
  * **In de cloud**
  * **Lokaal** (vereist als je ERP of doelsysteem lokaal wordt gehost)
