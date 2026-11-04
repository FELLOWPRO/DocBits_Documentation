# Standard-Steuerland für den Export LN konfigurieren

### Übersicht

Das Standard-Steuerland (Tax Country) für den Export ist auf **DE (Deutschland)** gesetzt, um Exportfehler zu vermeiden. Dies kann in der Mapping-Datei geändert werden, indem Sie entweder:

* einen anderen statischen Wert definieren oder
* es dynamisch einem Feld in DocBits zuordnen.

<mark style="color:red;">**Hinweis:**</mark> Wenn das angegebene Feld nicht existiert oder leer ist, wird beim Export wieder auf **DE** zurückgegriffen.

### Schritte zum Ändern des Steuerlands

#### 1. Mapping-Datei beziehen

* Navigieren Sie zu **DocBits → Settings → Document Processing → Export**.
* Öffnen Sie die Exportkonfiguration, die Sie ändern möchten.
*   Klicken Sie auf **Download**, um die Mapping-Datei zu erhalten.\\

    <figure><img src="../../../../.gitbook/assets/iScreen Shoter - Google Chrome - 250220120028.jpg" alt=""><figcaption></figcaption></figure>
* Öffnen Sie die Datei in einem Texteditor.

#### 2. Mapping-Datei ändern

Wählen Sie eine der beiden folgenden Optionen und nehmen Sie die erforderlichen Änderungen vor.

**Option 1: Statischer Wert**

Um einen statischen Wert für das Steuerland festzulegen, gehen Sie wie folgt vor:

1.  Definieren Sie ein neues statisches Feld, indem Sie `,TaxCountry` an die Zeile `StaticFields` anhängen.

    ```properties
    StaticFields=FinancialCompany...,TaxCountry
    ```
2.  Legen Sie den Ländercode fest, indem Sie die folgende Zeile hinzufügen:

    ```properties
    SF_TaxCountry=CountryCode
    ```

    Ersetzen Sie `CountryCode` durch den tatsächlichen Ländercode, z. B. `ES` für Spanien oder `DE` für Deutschland:

    ```properties
    SF_TaxCountry=ES
    ```

**Beispiel:**

```properties
StaticFields=FinancialCompany,TaxCountry
SF_TaxCountry=FR
```

<figure><img src="../../../../.gitbook/assets/image (415).png" alt=""><figcaption></figcaption></figure>

**Option 2: Dynamische Zuordnung aus einem DocBits-Feld**

Um das Steuerland dynamisch aus einem Feld in DocBits zuzuordnen:

1.  Fügen Sie `,TaxCountry` zur Zeile `HeaderFields` hinzu:

    ```properties
    HeaderFields=SupplierCode,...,TaxCountry
    ```
2.  Definieren Sie die entsprechende Feldzuordnung:

    ```properties
    HF_TaxCountry=DocBits_Field_name
    ```

    Ersetzen Sie `DocBits_Field_Name` durch den tatsächlichen Feldnamen in DocBits:

    ```properties
    HF_TaxCountry=tax_country_1
    ```

**Beispiel:**

```properties
HeaderFields=SupplierCode,TaxCountry
HF_TaxCountry=tax_country_1
```

<figure><img src="../../../../.gitbook/assets/image (411).png" alt=""><figcaption></figcaption></figure>

### Zusammenfassung

* Wenn das Steuerland **nicht definiert oder das Feld leer ist**, wird standardmäßig **DE** verwendet.
* **Verwenden Sie einen statischen Wert**, wenn das Steuerland für alle Exporte gleich bleibt.
* **Verwenden Sie eine dynamische Feldzuordnung**, wenn das Steuerland je Dokument variiert.

Mit diesen Schritten können Sie die Zuordnung des Steuerlands erfolgreich an Ihre Anforderungen anpassen.
