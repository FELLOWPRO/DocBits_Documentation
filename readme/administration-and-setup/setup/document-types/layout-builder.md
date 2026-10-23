# Costruttore di Layout

Usa il Layout Builder per organizzare i campi e i controlli che gli utenti vedono quando convalidano o approvano un documento. Un layout appartiene a un tipo di documento, a un'origine e a un tipo di layout, quindi controlla questi tre elementi in cima alla pagina prima di salvare.

## Aprire il layout

1. Apri **Impostazioni → Tipi di Documento**.
2. Seleziona il tipo di documento che vuoi modificare e apri **Layout Builder**. Per un sottotipo di documento, apri l'azione Layout Builder di quel sottotipo.
3. Controlla l'intestazione. Il selettore a sinistra è l'**Origine** (ad esempio **Predefinito**), seguito da **Tipo di documento** (ad esempio **Fattura**) e **Tipo di layout** (ad esempio **Convalida campi**). Ogni selettore apre un elenco; scegliendo un'altra voce si carica il layout corrispondente. Se il Layout Builder non è disponibile, un amministratore potrebbe dover attivare il modulo per la tua organizzazione.

<figure><img src="../../../.gitbook/assets/layout-builder-overview-it.png" alt="Il Layout Builder di una fattura in DocBits, con i selettori di origine, tipo di documento e tipo di layout, le schede Struttura, Campi ed Elementi, l'area di lavoro del layout e il pannello Proprietà a destra"><figcaption><p>Il Layout Builder: i selettori dell'intestazione, gli elenchi degli elementi a sinistra, l'area di lavoro al centro e il pannello Proprietà a destra.</p></figcaption></figure>

## Lavorare con l'intestazione

* **Tipo di documento** e **Tipo di layout** permettono di passare da un layout all'altro. La pagina ricarica il layout che scegli.
* Accanto a **Salva**, DocBits indica se il layout presenta **Modifiche non salvate**. Dopo un salvataggio mostra quando il layout è stato salvato l'ultima volta.
* **Salva** memorizza il layout per il tipo di documento, l'origine e il tipo di layout selezionati.
* Il menu **Di più** (tre punti) contiene **Generazione automatica del modello**, **Applica il layout predefinito alle origini**, **Usa il modello predefinito**, **Modifica JSON**, **Copiare JSON** e **Impostazioni di layout**. **Generazione automatica del modello** e **Usa il modello predefinito** sostituiscono un layout personalizzato, quindi controlla prima il tipo di documento e il layout selezionati. **Modifica JSON** serve per la configurazione avanzata e va usato solo quando conosci il formato del modello.
* Se esci dalla pagina con modifiche non salvate, DocBits chiede se salvarle o scartarle.

## Trovare gli elementi: Struttura, Campi, Elementi

Il lato sinistro ha tre schede:

| Scheda | A cosa serve |
| --- | --- |
| **Struttura** | Visualizza il layout come un albero. I gruppi e i relativi campi sono elencati nell'ordine in cui compaiono sull'area di lavoro, con il numero di campi posizionati e disponibili. |
| **Campi** | Tutti i campi configurati per il tipo di documento, raggruppati per gruppo di campi e compressi per impostazione predefinita. Il filtro passa tra i campi **Tutti**, **Inutilizzato** e **Nascosto**, e sotto l'etichetta del campo viene mostrato il nome tecnico del campo. |
| **Elementi** | Controlli di presentazione e interazione come Testo, Etichetta, Casella di controllo, separatori, tabelle, pulsanti e sottogruppi. |

<figure><img src="../../../.gitbook/assets/layout-builder-structure-it.png" alt="La scheda Struttura del Layout Builder con i gruppi Dettagli fattura, Dettagli del pagamento, Ordine di acquisto e Dettagli di consegna espansi nei rispettivi campi"><figcaption><p>La scheda Struttura mostra il layout costruito come un albero di gruppi e campi.</p></figcaption></figure>

Seleziona un elemento per aggiungerlo, oppure trascinalo nell'area di lavoro. Il titolo di un gruppo indica alla persona che convalida il documento cosa appartiene a quella sezione. Crea o rinomina i campi riutilizzabili del documento prima in [Tipi di Documento](README.md).

## Lavorare sull'area di lavoro

* **Layout principale** mostra il layout del documento stesso. **Tabella** mostra il layout a tabella usato per le voci di riga.
* **Documento** apre o chiude il documento di esempio accanto all'area di lavoro, così puoi confrontare il layout con un documento reale.
* I gruppi sono disegnati come schede; i campi all'interno di un gruppo possono essere disposti su righe e avere larghezze diverse.

## Modificare le proprietà di un elemento

Seleziona un elemento o un gruppo sull'area di lavoro. **Proprietà** a destra è sempre visibile ed è organizzato in sezioni:

* **Visualizzazione** – etichetta, nome campo, posizione dell'etichetta e larghezza dell'elemento.
* **Comportamento** – sola lettura, nascosto e indice delle schede.
* **Valori ed elenchi** – i valori offerti per l'elemento.
* **Automazione** – regole che compilano o modificano l'elemento.
* **Bordi e spaziatura** – l'aspetto dell'elemento.

Per la larghezza, scegli uno dei valori preimpostati (25, 33, 50, 66, 75 o 100 per cento) invece di digitare un valore; controlla il risultato sull'area di lavoro. Quali sezioni e opzioni compaiono dipende dall'elemento selezionato. Per maggiori dettagli, vedi [Configurazione delle proprietà dei campi](../../settings/global-settings/document-types/layout-manager/configuring-field-properties.md).

## Rivedere e salvare

Disponi i gruppi e i campi, controlla il layout sull'area di lavoro e usa **Salva** nell'intestazione quando il risultato è corretto. Per i layout specifici di un'origine, vedi [Layout per origine](origin-layouts.md).

{% hint style="info" %}
Le schermate mostrano impostazioni sintetiche nell'organizzazione di test di DocBits con l'inglese selezionato nell'applicazione. Durante la loro acquisizione non è stato salvato né sostituito alcun layout.
{% endhint %}
