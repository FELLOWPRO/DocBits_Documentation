# E-Mail-templates

## **Overzicht**

E-mailtemplates stellen u in staat om aangepaste geautomatiseerde e-mailmeldingen aan te passen die vanuit DocBits worden verzonden. Templates kunnen dynamische velden bevatten (bijv., `{{FieldID}}`), afbeeldingen en HTML-opmaak.

## **Toegang tot e-mailtemplates**

1.  Navigeer naar: **Instellingen → Algemene instellingen → E-mailtemplates**

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FWzjaI1Jinpw0PQHCuwM0%252Fimage.png%3Falt%3Dmedia%26token%3D21f7af41-6ebe-4e25-952f-9ae0b11cade2\&width=768\&dpr=4\&quality=100\&sign=ae789081\&sv=2)
2. Het dashboard toont alle templates met:
   * **Naam**
   * **Onderwerp**
   * **Laatst gewijzigd** datum
   * **Acties** (Bewerken of Verwijderen).

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FENN4zipGg75mpi2OooPP%252Fimage.png%3Falt%3Dmedia%26token%3Ddff6d8a8-e5b3-4e52-bee1-e311daba7b64\&width=768\&dpr=4\&quality=100\&sign=4202a84f\&sv=2)

## **Een nieuwe template maken**

### **1 Basisinstellingen**

* Klik op **Nieuw**.
* Vul de velden aan de rechterkant in:
  * **Naam**: Template-identificatie (bijv., "Documentfout").
  * **Onderwerp**: E-mailonderwerpregel (bijv., "Actie vereist: Documentfout").
  *   **Documenttype**: Selecteer uit de vervolgkeuzelijst (bijv., "Factuur").

      ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FXzmfZBIoyoDS7tTz1qo4%252Fimage.png%3Falt%3Dmedia%26token%3D24547984-2406-41b5-95d6-0f7f45e06258\&width=768\&dpr=4\&quality=100\&sign=f7aa9b89\&sv=2)

### **2 Template-editor**

* **Menu**: Tekst opmaken, links toevoegen of tabellen invoegen.
* **HTML-editor**: Klik op het `<>`-pictogram om ruwe HTML te bewerken.
* **Afbeeldingen toevoegen**: Gebruik de **Upload**-functie.
*   **Dynamische velden**: Voeg documentveldwaarden in door

    * **Variabele veldoptie**: Selecteer uit een vervolgkeuzelijst.
    * **Handmatige invoer**: Typ `{{FieldID}}` (bijv., `{{InvoiceNumber}}`).

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/email_templates_4.png)

### **3 Opslaan**

* Klik op **Opslaan** om de template op te slaan.

## **Een test-e-mail verzenden**

1.  Open de template en klik op **Test verzenden**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FZTskZNsVfWj6IwBmwoR5%252Fimage.png%3Falt%3Dmedia%26token%3D62229942-2ee7-4d58-833c-eb863b18f2d3\&width=768\&dpr=4\&quality=100\&sign=b804f787\&sv=2)
2. Voer in:
   * **Ontvanger e-mail** (verplicht).
   * **Veldwaarden** (optioneel; nepgegevens voor tijdelijke aanduidingen). ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FO2yw8EgefTPSCIhxUFH6%252Fimage.png%3Falt%3Dmedia%26token%3D2acc0067-3698-4565-92d8-6c4ddabe497c\&width=300\&dpr=4\&quality=100\&sign=461ae8e7\&sv=2)
3. Bekijk de test-e-mail en pas de template indien nodig aan.

## **Templates gebruiken in meldingen**

Opgeslagen templates kunnen worden gekoppeld aan [**E-mailmelding**](email-notification/)-workflows (bijv., goedkeuringsherinneringen, statusupdates).
