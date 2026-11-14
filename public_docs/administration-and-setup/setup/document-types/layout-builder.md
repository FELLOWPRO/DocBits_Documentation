# Costruttore di Layout

Usa il Costruttore di Layout per organizzare i campi e i controlli che le persone vedono quando convalidano o approvano un documento. Un layout appartiene a un tipo di documento, a un'origine e a un tipo di layout: prima di salvare, controlla questi tre elementi nella parte superiore della pagina.

{% embed url="https://youtu.be/-m45XGiIeig" %}
DocBits Layout Builder Tutorial: Create Custom Document Layouts for Faster, Cleaner Validation
{% endembed %}

## Aprire il layout

1. Apri **Settings → Document Types**.
2. Seleziona il tipo di documento che vuoi modificare e apri **Layout Builder**. Per un sottotipo di documento, apri il Costruttore di Layout di quel sottotipo.
3. Controlla l'intestazione. Il selettore a sinistra è **origin** (ad esempio **Default**), seguito da **Document Type** (ad esempio **Invoice**) e **Layout type** (ad esempio **Field Validation**). Ogni selettore apre un elenco; scegliendo un'altra voce viene caricato il layout corrispondente. Se il Costruttore di Layout non è disponibile, un amministratore potrebbe dover attivare il modulo per la tua organizzazione.

<figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/layout-builder-overview.png" alt="Il Costruttore di Layout per una fattura in DocBits, con i selettori origin, tipo di documento e tipo di layout, le schede Structure, Fields ed Elements, l’area del layout e il pannello Properties a destra"><figcaption><p>Il Costruttore di Layout: i selettori nell’intestazione, gli elenchi di elementi a sinistra, l’area del layout al centro e il pannello Properties a destra.</p></figcaption></figure>

## Lavorare con l'intestazione

* **Document Type** e **Layout type** cambiano layout. La pagina ricarica il layout scelto.
* Accanto a **Save**, DocBits indica se il layout presenta **unsaved changes**. Dopo un salvataggio mostra quando il layout è stato salvato l'ultima volta.
* **Save** memorizza il layout per il tipo di documento, l'origine e il tipo di layout selezionati.
* Il menu **More** (tre punti) contiene **Auto Generate template**, **Apply Default layout to Origins**, **Use default template**, **Edit JSON**, **Copy JSON** e **Layout settings**. **Auto Generate template** e **Use default template** sostituiscono un layout personalizzato: controlla prima il tipo di documento e il layout selezionati. **Edit JSON** serve alla configurazione avanzata e va usato solo se conosci il formato del modello.
* Se esci dalla pagina con modifiche non salvate, DocBits chiede se salvarle o scartarle.

## Trovare elementi: Structure, Fields, Elements

A sinistra sono disponibili tre schede:

| Scheda | A cosa serve |
| --- | --- |
| **Structure** | Visualizza il layout come struttura ad albero. I gruppi e i relativi campi sono elencati nell'ordine in cui compaiono nell'area del layout, con il numero di campi posizionati e disponibili. |
| **Fields** | Tutti i campi configurati per il tipo di documento, raggruppati per gruppo di campi e compressi per impostazione predefinita. Il filtro passa tra i campi **All**, **Unused** e **Hidden**, e sotto l'etichetta del campo è indicato il nome tecnico. |
| **Elements** | Controlli di presentazione e interazione come Text, Label, Check Box, separatori, tabelle, pulsanti e sottogruppi. |

<figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/layout-builder-structure.png" alt="La scheda Structure del Costruttore di Layout con i gruppi Invoice details, Payment details, Purchase Order e Delivery Details espansi nei rispettivi campi"><figcaption><p>La scheda Structure mostra il layout costruito come struttura ad albero di gruppi e campi.</p></figcaption></figure>

Seleziona un elemento per aggiungerlo oppure trascinalo nell'area del layout. Il titolo di un gruppo indica a chi convalida il documento che cosa appartiene a quella sezione. Crea o rinomina prima i campi riutilizzabili del documento in [Document Types](README.md).

## Lavorare sull'area del layout

* **Main layout** mostra il layout del documento stesso. **Table** mostra il layout di tabella usato per le righe.
* **Document** apre o chiude il documento di esempio accanto all'area del layout, così puoi confrontare il layout con un documento reale.
* I gruppi sono rappresentati come card; i campi all'interno di un gruppo possono essere disposti su righe e avere larghezze diverse.

## Modificare le proprietà di un elemento

Seleziona un elemento o un gruppo nell'area del layout. **Properties** a destra è sempre visibile ed è organizzato in sezioni:

* **Display** – etichetta, nome del campo, posizione dell'etichetta e larghezza dell'elemento.
* **Behaviour** – sola lettura, nascosto e indice di tabulazione.
* **Values & lists** – i valori offerti per l'elemento.
* **Automation** – regole che compilano o modificano l'elemento.
* **Borders & spacing** – l'aspetto dell'elemento.

Per la larghezza scegli uno dei valori preimpostati (25, 33, 50, 66, 75 o 100 per cento) invece di digitare un valore; controlla il risultato nell'area del layout. Le sezioni e le opzioni visualizzate dipendono dall'elemento selezionato. Per maggiori dettagli, vedi [Configuring Field Properties](../../settings/global-settings/document-types/layout-manager/configuring-field-properties.md).

## Tradurre le etichette dei pulsanti

I pulsanti come **Save Rules**, **Auto Accounting**, **PO Match**, **Export**, **Export Without Validation** e **Reject** ricavano l'etichetta da una chiave di traduzione. Il visualizzatore mostra l'etichetta nella lingua della persona che apre il layout. Se la chiave non contiene un testo per quella lingua, DocBits mostra l'etichetta salvata nel layout.

* Un pulsante singolo ha un campo **Translation Key** in **Properties**.
* **Invoice Buttons** raggruppa più pulsanti. Imposta la chiave per un singolo pulsante figlio oppure una chiave per ciascun figlio nell'elenco del pannello del gruppo.

I layout creati prima di questa modifica mantengono le proprie etichette: DocBits vi inserisce la chiave predefinita di ciascun tipo di pulsante. I layout salvati con una chiave conservano quella chiave anche dopo un ricaricamento.

## Save and go back to Dashboard

Un pulsante del tipo **Save and go back to Dashboard** memorizza i valori del documento come **Save** e poi apre il Dashboard. Il tipo è adatto ai layout in cui un revisore elabora una coda di documenti uno dopo l'altro.

* Aggiungi un elemento pulsante nell'area del layout e scegli il tipo in **Properties**.
* Se il salvataggio non riesce, il pulsante resta nella schermata di validazione e non apre il Dashboard, così il problema può essere corretto prima.
* L'etichetta viene risolta come quella di qualsiasi altro pulsante; vedi *Tradurre le etichette dei pulsanti* sopra.

## Rivedere e salvare

Organizza i gruppi e i campi, controlla il layout nell'area del layout e, quando il risultato è corretto, usa **Save** nell'intestazione. Per i layout specifici di un'origine, vedi [Origin Layouts](origin-layouts.md).

{% hint style="info" %}
Le schermate mostrano impostazioni sintetiche nell'organizzazione di test di DocBits con l'inglese selezionato nell'applicazione. Durante la loro acquisizione non è stato salvato né sostituito alcun layout.
{% endhint %}
