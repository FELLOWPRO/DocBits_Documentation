# Configurazione del paese fiscale predefinito per l'esportazione LN

### Panoramica

Il paese fiscale (Tax Country) predefinito per l'esportazione è impostato su **DE (Germania)** per evitare errori di esportazione. Può essere modificato nel file di mappatura in uno dei seguenti modi:

* Definendo un valore statico diverso.
* Mappandolo dinamicamente a un campo in DocBits.

<mark style="color:red;">**Nota:**</mark> se il campo specificato non esiste o è vuoto, l'esportazione tornerà al valore predefinito **DE**.

### Passaggi per modificare il paese fiscale

#### 1. Ottenere il file di mappatura

* Vai su **DocBits → Impostazioni → Elaborazione documenti → Esportazione**.
* Apri la configurazione di esportazione che desideri modificare.
*   Fai clic su **Download** per ottenere il file di mappatura.\\

    <figure><img src="../../../../.gitbook/assets/iScreen Shoter - Google Chrome - 250220120028.jpg" alt="Finestra di dialogo di Infor LN per il tipo di documento Invoice con il titolo Invoice LN, caselle di controllo per ION-Mapping File, IDM Mapping File e LN-Mapping File e un pulsante DOWNLOAD"><figcaption></figcaption></figure>
* Apri il file in un editor di testo.

#### 2. Modificare il file di mappatura

Scegli una delle due opzioni seguenti e applica le modifiche necessarie.

**Opzione 1: valore statico**

Per impostare un valore statico del paese fiscale, procedi come segue:

1.  Definisci un nuovo campo statico aggiungendo `,TaxCountry` alla riga `StaticFields`.

    ```properties
    StaticFields=FinancialCompany...,TaxCountry
    ```
2.  Imposta il codice del paese aggiungendo la seguente riga:

    ```properties
    SF_TaxCountry=CountryCode
    ```

    Sostituisci `CountryCode` con il codice paese effettivo, ad esempio `ES` per la Spagna o `DE` per la Germania:

    ```properties
    SF_TaxCountry=ES
    ```

**Esempio:**

```properties
StaticFields=FinancialCompany,TaxCountry
SF_TaxCountry=FR
```

<figure><img src="../../../../.gitbook/assets/image (415).png" alt="Frammento del file di mapping LN con StaticFields=FinancialCompany,RateDeterminer,ExternalRateFactor e voci HeaderFields come HF_SupplierCode=supplier_id e HF_InvoiceCurrency=currency"><figcaption></figcaption></figure>

**Opzione 2: mappatura dinamica da un campo DocBits**

Per mappare dinamicamente il paese fiscale da un campo in DocBits:

1.  Aggiungi `,TaxCountry` alla riga `HeaderFields`:

    ```properties
    HeaderFields=SupplierCode,...,TaxCountry
    ```
2.  Definisci la corrispondente mappatura del campo:

    ```properties
    HF_TaxCountry=DocBits_Field_name
    ```

    Sostituisci `DocBits_Field_Name` con il nome effettivo del campo in DocBits:

    ```properties
    HF_TaxCountry=tax_country_1
    ```

**Esempio:**

```properties
HeaderFields=SupplierCode,TaxCountry
HF_TaxCountry=tax_country_1
```

<figure><img src="../../../../.gitbook/assets/image (411).png" alt="Frammento del file di mapping LN con TaxCountry aggiunto alla riga StaticFields e una voce HF_TaxCountry mappata nell'elenco HeaderFields"><figcaption></figcaption></figure>

### Riepilogo

* Se il paese fiscale **non è definito o il campo è vuoto**, viene utilizzato per impostazione predefinita **DE**.
* **Usa un valore statico** se il paese fiscale rimane costante per tutte le esportazioni.
* **Usa una mappatura dinamica del campo** se il paese fiscale varia da documento a documento.

Seguendo questi passaggi, puoi modificare con successo la mappatura del paese fiscale in base alle tue esigenze.
