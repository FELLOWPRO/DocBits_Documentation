# Faktura

## Geef het attribuut weer op elk regelitem

Als u op elk regelitem een specifiek kenmerk (zoals het inkoopordernummer) wilt weergeven, volgt u de onderstaande stappen. De aanpak zal verschillen afhankelijk van of u het attribuut nodig hebt in de JSON-extractie of in de XSL-uitvoer.

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 14.33.16.png" alt="Factuurtabel met de kolommen Position, Description, Quantity en Unit Price met inkooporderregels en totalen"><figcaption></figcaption></figure>

### Methode 1: Attribuut weergeven in de JSON-extractie (DocBits config)

1. Ga naar **Instellingen**
2. Go to **Document Types**
3. Select **Invoice/E-Doc**

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 15.07.58.png" alt="Instellingenpagina van het documenttype Invoice met de tabs Extraction type, Edit layout, Document Sub Types, Table columns, Fields en Model Training"><figcaption></figcaption></figure>

4. Open the **"FATTURAPA"** tab
5. Click on **JSON**

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 15.01.13.png" alt="FATTURAPA-formatlijst met de items Preview, Extraction Paths, FacturX ZUGFERD-varianten, Peppol en XRECHNUNG met XSLT"><figcaption></figcaption></figure>

6. Om een concept te maken, klikt u op het pictogram **pen**

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 14.58.56.png" alt="Instellingen van het documenttype Invoice met het item voor het elektronische documenttype FATTURAPA en een tijdstempel"><figcaption></figcaption></figure>

7. Voeg binnen de `"tables"`-array de specifieke kolom toe die u wilt weergeven door een naam en pad op te geven:

```
{ 
"name": "PURCHASE_ORDER",    
"path":"path_to_source" 
}
```

**NOTE:** Bij e-documenten is de oorsprong altijd ingesteld op **Groot-Brittannië**, dus de bedragen worden in internationaal formaat opgeslagen, met een **punt (.)** als decimaalteken.

8. Save the draft

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 15.11.04.png" alt="Draft-versie-item met de tijdstempel 28.01.2025 15:10:12 in de DocBits-testweergave"><figcaption></figcaption></figure>

9. Zorg ervoor dat uw concept **actief** is.

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 16.03.50.png" alt="Item in de Draft-versielijst met versie 91.20 en een tijdstempel die de actieve conceptversie bevestigt"><figcaption></figcaption></figure>

### Methode 2: Attribuut weergeven in de XSL-uitvoer (HTML/PDF voorbeeld)

1. Ga naar **Instellingen**
2. Go to **Document Types**
3. Select **Invoice/E-Doc**

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 15.07.58.png" alt="Instellingenpagina van het documenttype Invoice met de tabs Extraction type, Edit layout, Document Sub Types, Table columns, Fields en Model Training"><figcaption></figcaption></figure>

4. Open the **"FATTURAPA"** tab
5. **Click on XLST**

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 15.23.06.png" alt="FATTURAPA-tab met elektronische documentformaten, waaronder EDI, FacturX ZUGFERD-varianten, Peppol en XRECHNUNG-versies"><figcaption></figcaption></figure>

6. Om een concept te maken, klikt u op het pictogram **pen**

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 14.58.56.png" alt="Instellingen van het documenttype Invoice met het item voor het elektronische documenttype FATTURAPA en een tijdstempel"><figcaption></figcaption></figure>

7. In het `<xsl:for-each select="path">` blok dat de tabelrijen genereert, voegt u een fragment als dit toe waar u het attribuut wilt laten verschijnen (bijvoorbeeld in een eigen kolom):

```
<tr>
    <!-- Other columns ... -->

    <td>
        <!-- PO number -->
        <xsl:variable name="variable_name" select="value" />
        <xsl:value-of 
            select="path_to_attribute" 
        />
    </td>
</tr>
```

**NOTE:** Bij e-documenten is de oorsprong altijd ingesteld op **Groot-Brittannië**, dus de bedragen worden in internationaal formaat opgeslagen, met een **punt (.)** als decimaalteken.

8. Save the draft

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 15.11.04.png" alt="Draft-versie-item met de tijdstempel 28.01.2025 15:10:12 in de DocBits-testweergave"><figcaption></figcaption></figure>

9. Zorg ervoor dat uw concept **actief** is.

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 16.03.50.png" alt="Item in de Draft-versielijst met versie 91.20 en een tijdstempel die de actieve conceptversie bevestigt"><figcaption></figcaption></figure>
