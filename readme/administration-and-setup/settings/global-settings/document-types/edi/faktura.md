# Fattura

## Visualizzare l'attributo su ogni riga

Se si desidera visualizzare un attributo specifico (come il numero dell'ordine di acquisto) su ogni riga, seguire i passaggi seguenti. L'approccio differirà a seconda che l'attributo sia necessario nell'estrazione JSON o nell'output XSL.

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 14.33.16.png" alt="Tabella della fattura con le colonne Position, Description, Quantity e Unit Price che elenca le voci dell'ordine di acquisto con totali"><figcaption></figcaption></figure>

### Metodo 1: Visualizzare l'attributo nell'estrazione JSON (configurazione DocBits)

1. Andare su **Impostazioni**
2. Andare su **Tipi di documento**
3. Selezionare **Invoice/E-Doc**

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 15.07.58.png" alt="Pagina di impostazioni del tipo di documento Invoice con le schede Extraction type, Edit layout, Document Sub Types, Table columns, Fields e Model Training"><figcaption></figcaption></figure>

4. Aprire la scheda **"FATTURAPA"**
5. Fare clic su **JSON**

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 15.01.13.png" alt="Elenco dei formati FATTURAPA con le voci Preview, Extraction Paths, varianti FacturX ZUGFERD, Peppol e XRECHNUNG con XSLT"><figcaption></figcaption></figure>

6. Per creare una bozza, fare clic sull'icona della **penna**

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 14.58.56.png" alt="Impostazioni del tipo di documento Invoice con la voce del tipo di documento elettronico FATTURAPA e un timestamp"><figcaption></figcaption></figure>

7. All'interno dell'array `"tables"`, aggiungere la colonna specifica che si desidera visualizzare fornendo un nome e un percorso:

```
{ 
"name": "PURCHASE_ORDER",    
"path":"path_to_source" 
}
```

**NOTA:** I documenti elettronici avranno sempre l'origine impostata su **Gran Bretagna**, quindi gli importi saranno salvati in formato internazionale, utilizzando un **punto (.)** come separatore decimale.

8. Salvare la bozza

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 15.11.04.png" alt="Voce della versione Draft con il timestamp 28.01.2025 15:10:12 nella vista di test di DocBits"><figcaption></figcaption></figure>

9. Assicurarsi che la bozza sia quella **attiva**.

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 16.03.50.png" alt="Voce dell'elenco delle versioni Draft con la versione 91.20 e un timestamp che conferma la bozza attiva"><figcaption></figcaption></figure>

### Metodo 2: Visualizzare l'attributo nell'output XSL (anteprima HTML/PDF)

1. Andare su **Impostazioni**
2. Andare su **Tipi di documento**
3. Selezionare **Invoice/E-Doc**

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 15.07.58.png" alt="Pagina di impostazioni del tipo di documento Invoice con le schede Extraction type, Edit layout, Document Sub Types, Table columns, Fields e Model Training"><figcaption></figcaption></figure>

4. Aprire la scheda **"FATTURAPA"**
5. **Fare clic su XLST**

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 15.23.06.png" alt="Scheda FATTURAPA che elenca i formati di documenti elettronici, tra cui EDI, varianti FacturX ZUGFERD, Peppol e versioni XRECHNUNG"><figcaption></figcaption></figure>

6. Per creare una bozza, fare clic sull'icona della **penna**

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 14.58.56.png" alt="Impostazioni del tipo di documento Invoice con la voce del tipo di documento elettronico FATTURAPA e un timestamp"><figcaption></figcaption></figure>

7. Nel blocco `<xsl:for-each select="path">` che genera le righe della tabella, aggiungere uno snippet come questo dove si desidera che appaia l'attributo (ad esempio, in una colonna propria):

```
<tr>
    <!-- Altre colonne ... -->

    <td>
        <!-- Numero d'ordine -->
        <xsl:variable name="variable_name" select="value" />
        <xsl:value-of 
            select="path_to_attribute" 
        />
    </td>
</tr>
```

**NOTA:** I documenti elettronici avranno sempre l'origine impostata su **Gran Bretagna**, quindi gli importi saranno salvati in formato internazionale, utilizzando un **punto (.)** como separatore decimale.

8. Salvare la bozza

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 15.11.04.png" alt="Voce della versione Draft con il timestamp 28.01.2025 15:10:12 nella vista di test di DocBits"><figcaption></figcaption></figure>

9. Assicurarsi che la bozza sia quella **attiva**.

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 16.03.50.png" alt="Voce dell'elenco delle versioni Draft con la versione 91.20 e un timestamp che conferma la bozza attiva"><figcaption></figcaption></figure>
