# Navigare nel Layout Builder

Usa il **Layout Builder** per disporre i campi e i gruppi che gli utenti vedono in un documento. Questa guida utilizza il layout **Invoice** in inglese in un'organizzazione sandbox.

## Aprire il layout Invoice

1. Vai su **Settings → Document Types**.
2. Trova **Invoice** e seleziona **Layouts** nella sua scheda. Il Layout Builder si apre per quel tipo di documento.
3. Controlla il selettore del layout in alto a sinistra. L'esempio seguente mostra **DEFAULT**.

<figure><img src="../../../../../.gitbook/assets/dbdc177-document-types-en.png" alt="Pagina Document Types in inglese con la scheda Invoice e il relativo link Layouts"><figcaption>Apri **Layouts** dalla scheda Invoice.</figcaption></figure>

## Trovare gruppi e campi

Il pannello **Elements** a sinistra ha tre sezioni. **Groups** elenca le sezioni del documento; l'area di lavoro centrale ne mostra la disposizione attuale. Seleziona un campo nell'area di lavoro e apri **Properties** per modificarne le impostazioni di visualizzazione. Per le opzioni disponibili, vedi [Configurazione delle proprietà dei campi](configuring-field-properties.md).

<figure><img src="../../../../../.gitbook/assets/dbdc177-layout-elements-en.png" alt="Layout Builder Invoice in inglese con Groups nel pannello Elements e i campi raggruppati nell'area di lavoro"><figcaption>L'elenco Groups e l'area di lavoro del layout Invoice.</figcaption></figure>

Apri **Fields** per trovare i campi del documento disponibili. Usa la casella di ricerca quando l'elenco è lungo, quindi trascina il campo nel gruppo desiderato nell'area di lavoro. I campi già inseriti nel layout possono risultare non disponibili nell'elenco.

<figure><img src="../../../../../.gitbook/assets/dbdc177-layout-fields-en.png" alt="Pannello Fields del Layout Builder in inglese con ricerca e campi Invoice disponibili"><figcaption>Cerca tra i campi disponibili prima di inserirne uno.</figcaption></figure>

Apri **Form Elements** per i controlli visivi come Text, Label, Check Box, separatore, Button e Sub Group. Trascina l'elemento che ti serve nell'area di lavoro, quindi controlla le sue **Properties**.

<figure><img src="../../../../../.gitbook/assets/dbdc177-layout-form-elements-en.png" alt="Pannello Form Elements del Layout Builder in inglese con testi, etichette, caselle di controllo, pulsanti e sottogruppi"><figcaption>La palette Form Elements attuale.</figcaption></figure>

## Disporre e salvare

- Seleziona il titolo di un gruppo nell'area di lavoro per modificarlo. Il **+** sopra l'area di lavoro aggiunge un gruppo; l'icona con le parentesi graffe accanto apre il modulo JSON avanzato del gruppo.
- Passa il mouse su un gruppo per le azioni copia JSON, sposta su, sposta giù, elimina e maniglia di trascinamento. Per riordinare i campi, trascinali all'interno di un gruppo o tra gruppi diversi.
- Seleziona un campo nell'area di lavoro per aprire **Properties**. La sua icona di eliminazione lo rimuove da questo layout. Per configurare convalida, OCR o corrispondenza, usa le [impostazioni dei campi](../fields/configuring-field-properties-1.md) separate.
- Dopo le modifiche, seleziona **Save** nella barra superiore. Prima di usare le altre azioni della barra superiore, comprese la generazione dei template, i template predefiniti e l'applicazione di un layout alle origini, vedi [Salvare e applicare le modifiche](save-and-apply-changes.md).
