# Het standaardbelastingland voor LN-export configureren

### Overzicht

Het standaardbelastingland voor de export is **DE (Duitsland)** om exportfouten te voorkomen. U kunt dit in het mappingbestand wijzigen door:

* Een andere statische waarde te definiëren.
* Het belastingland dynamisch aan een veld in DocBits te koppelen.

<mark style="color:red;">**Opmerking:**</mark> Als het opgegeven veld niet bestaat of leeg is, gebruikt de export **DE** als standaardwaarde.

### Het belastingland wijzigen

#### 1. Het mappingbestand ophalen

* Ga naar **DocBits → Settings → Document Processing → Export**.
* Open de exportconfiguratie die u wilt wijzigen.
*   Klik op **Download** om het mappingbestand te downloaden.\


    <figure><img src="../../../../.gitbook/assets/iScreen Shoter - Google Chrome - 250220120028.jpg" alt="Infor LN-dialoog voor het documenttype Invoice met de titel Invoice LN, selectievakjes voor ION-Mapping File, IDM Mapping File en LN-Mapping File en een knop DOWNLOAD"><figcaption></figcaption></figure>
* Open het bestand in een teksteditor.

#### 2. Het mappingbestand wijzigen

Kies een van de onderstaande opties en voer de benodigde wijzigingen uit.

**Optie 1: statische waarde**

Stel als volgt een statische waarde voor het belastingland in:

1.  Voeg `,TaxCountry` toe aan de regel `StaticFields` om een nieuw statisch veld te definiëren.

    ```properties
    StaticFields=FinancialCompany...,TaxCountry
    ```
2.  Stel de landcode in door de volgende regel toe te voegen:

    ```properties
    SF_TaxCountry=CountryCode
    ```

    Vervang `CountryCode` door de juiste landcode, bijvoorbeeld `ES` voor Spanje of `DE` voor Duitsland:

    ```properties
    SF_TaxCountry=ES
    ```

**Voorbeeld:**

```properties
StaticFields=FinancialCompany,TaxCountry
SF_TaxCountry=FR
```

<figure><img src="../../../../.gitbook/assets/image (415).png" alt="Purchase order-nummer 2054032 met een vernieuwingspictogram ernaast voor het bijwerken van de purchase order"><figcaption></figcaption></figure>

**Optie 2: dynamische mapping vanuit een DocBits-veld**

Koppel het belastingland als volgt dynamisch aan een veld in DocBits:

1.  Voeg `,TaxCountry` toe aan de regel `HeaderFields`:

    ```properties
    HeaderFields=SupplierCode,...,TaxCountry
    ```
2.  Definieer de bijbehorende veldmapping:

    ```properties
    HF_TaxCountry=DocBits_Field_name
    ```

    Vervang `DocBits_Field_Name` door de werkelijke veldnaam in DocBits:

    ```properties
    HF_TaxCountry=tax_country_1
    ```

**Voorbeeld:**

```properties
HeaderFields=SupplierCode,TaxCountry
HF_TaxCountry=tax_country_1
```

<figure><img src="../../../../.gitbook/assets/image (412).png" alt="Nederlandse exportinstellingenpagina met een opmerking dat exports met hetzelfde documenttype opeenvolgend worden uitgevoerd en een tabel met type, titel, exportmethode en actie"><figcaption></figcaption></figure>

### Samenvatting

* Als het belastingland **niet is gedefinieerd of het veld leeg is**, wordt **DE** gebruikt.
* **Gebruik een statische waarde** als het belastingland voor alle exports gelijk is.
* **Gebruik een dynamische veldmapping** als het belastingland per document verschilt.

Met deze stappen kunt u de mapping van het belastingland aanpassen aan uw behoeften.





