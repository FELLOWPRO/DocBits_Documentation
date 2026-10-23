# Faktura

## Attribut in jedem Einzelposten anzeigen

Wenn Sie ein bestimmtes Attribut (wie die Bestellnummer) in jedem Einzelposten anzeigen möchten, befolgen Sie die folgenden Schritte. Die Vorgehensweise unterscheidet sich je nachdem, ob Sie das Attribut in der JSON-Extraktion oder in der XSL-Ausgabe benötigen.

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 14.33.16.png" alt="Rechnungstabelle mit den Spalten Position, Description, Quantity und Unit Price, die Bestellpositionen mit Summen auflistet"><figcaption></figcaption></figure>

### Methode 1: Attribut in der JSON-Extraktion anzeigen (DocBits-Konfiguration)

1. Gehen Sie zu **Einstellungen**
2. Gehen Sie zu **Dokumenttypen**
3. Wählen Sie **Invoice/E-Doc**

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 15.07.58.png" alt="Einstellungsseite des Dokumenttyps Invoice mit den Tabs Extraction type, Edit layout, Document Sub Types, Table columns, Fields und Model Training"><figcaption></figcaption></figure>

4. Öffnen Sie den Reiter **"FATTURAPA"**
5. Klicken Sie auf **JSON**

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 15.01.13.png" alt="FATTURAPA-Formatliste mit den Einträgen Preview, Extraction Paths, FacturX ZUGFERD-Varianten, Peppol und XRECHNUNG samt XSLT"><figcaption></figcaption></figure>

6. Um einen Entwurf zu erstellen, klicken Sie auf das **Stift**-Symbol

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 14.58.56.png" alt="Einstellungen des Dokumenttyps Invoice mit dem Eintrag des elektronischen Dokumenttyps FATTURAPA und einem Zeitstempel"><figcaption></figcaption></figure>

7. Fügen Sie innerhalb des `"tables"`-Arrays die spezifische Spalte hinzu, die Sie anzeigen möchten, indem Sie einen Namen und einen Pfad angeben:

```
{ 
"name": "PURCHASE_ORDER",    
"path":"path_to_source" 
}
```

**HINWEIS:** E-Dokumente haben immer den Ursprung **Großbritannien**, daher werden die Beträge im internationalen Format mit einem **Punkt (.)** als Dezimaltrennzeichen gespeichert.

8. Speichern Sie den Entwurf

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 15.11.04.png" alt="Draft-Versionseintrag mit dem Zeitstempel 28.01.2025 15:10:12 in der DocBits-Testansicht"><figcaption></figcaption></figure>

9. Stellen Sie sicher, dass Ihr Entwurf der **aktive** ist.

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 16.03.50.png" alt="Eintrag in der Draft-Versionsliste mit Version 91.20 und einem Zeitstempel, der den aktiven Draft bestätigt"><figcaption></figcaption></figure>

### Methode 2: Attribut in der XSL-Ausgabe anzeigen (HTML/PDF-Vorschau)

1. Gehen Sie zu **Einstellungen**
2. Gehen Sie zu **Dokumenttypen**
3. Wählen Sie **Invoice/E-Doc**

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 15.07.58.png" alt="Einstellungsseite des Dokumenttyps Invoice mit den Tabs Extraction type, Edit layout, Document Sub Types, Table columns, Fields und Model Training"><figcaption></figcaption></figure>

4. Öffnen Sie den Reiter **"FATTURAPA"**
5. **Klicken Sie auf XSLT**

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 15.23.06.png" alt="FATTURAPA-Tab mit elektronischen Dokumentformaten wie EDI, FacturX ZUGFERD-Varianten, Peppol- und XRECHNUNG-Versionen"><figcaption></figcaption></figure>

6. Um einen Entwurf zu erstellen, klicken Sie auf das **Stift**-Symbol

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 14.58.56.png" alt="Einstellungen des Dokumenttyps Invoice mit dem Eintrag des elektronischen Dokumenttyps FATTURAPA und einem Zeitstempel"><figcaption></figcaption></figure>

7. Fügen Sie im `<xsl:for-each select="path">`-Block, der die Tabellenzeilen generiert, ein Snippet wie dieses dort hinzu, wo das Attribut erscheinen soll (z. B. in einer eigenen Spalte):

```
<tr>
    <!-- Andere Spalten ... -->

    <td>
        <!-- PO-Nummer -->
        <xsl:variable name="variable_name" select="value" />
        <xsl:value-of 
            select="path_to_attribute" 
        />
    </td>
</tr>
```

**HINWEIS:** E-Dokumente haben immer den Ursprung **Großbritannien**, daher werden die Beträge im internationalen Format mit einem **Punkt (.)** als Dezimaltrennzeichen gespeichert.

8. Speichern Sie den Entwurf

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 15.11.04.png" alt="Draft-Versionseintrag mit dem Zeitstempel 28.01.2025 15:10:12 in der DocBits-Testansicht"><figcaption></figcaption></figure>

9. Stellen Sie sicher, dass Ihr Entwurf der **aktive** ist.

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 16.03.50.png" alt="Eintrag in der Draft-Versionsliste mit Version 91.20 und einem Zeitstempel, der den aktiven Draft bestätigt"><figcaption></figcaption></figure>
