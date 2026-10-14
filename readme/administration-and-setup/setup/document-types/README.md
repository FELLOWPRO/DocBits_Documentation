# Tipi di Documento

I tipi di documento indicano a DocBits con quali tipi di documenti lavora la tua organizzazione. Un amministratore li trova in **Settings → Document Types** nella sezione **Document Processing** del menu delle impostazioni.

La pagina mostra i **Default Document Types**, che DocBits mette a disposizione e che non puoi eliminare, seguiti dai **Custom Document Types** creati per la tua organizzazione. Ogni tipo ha una propria scheda.

<figure><img src="../../../.gitbook/assets/document-types-overview-en-20260928.png" alt="Pagina Document Types con la scheda Invoice e altre schede di tipi di documento predefiniti, interruttori di attivazione ed estrazione, ingranaggio delle impostazioni e link di configurazione"><figcaption><p>Scegli la scheda di un tipo di documento per configurare quel tipo.</p></figcaption></figure>

## Cosa puoi fare su una scheda

| Controllo | Cosa fa |
| --- | --- |
| **Activate** | Rende questo tipo di documento disponibile o non disponibile nella tua organizzazione. Un interruttore blu è attivo; un interruttore grigio è disattivato. |
| **Extraction** | Sceglie la modalità di estrazione: **Flex** se attivo o **Fix** se disattivo. Non attiva né disattiva semplicemente l'estrazione. Passa il mouse sull'interruttore per vedere la modalità corrente. |
| **Settings** (ingranaggio) | Apre **More Settings** per questo tipo. Espandi una categoria per visualizzarne le opzioni. Le categorie dipendono dal tipo di documento. |
| **Layouts** | Apre la configurazione dei layout. Consulta [Layout Builder](layout-builder.md) per i passaggi successivi. |
| **Fields** | Apre i campi e le impostazioni di riconoscimento per questo tipo. Consulta [Fields](../../settings/global-settings/document-types/fields/README.md) per sapere come configurarli. |
| **Tables** | Apre la configurazione delle colonne della tabella per questo tipo. |
| **Scripts** | Apre gli script di elaborazione quando questa funzione è disponibile. |
| **Model Training** | Apre l'allenamento del modello per questo tipo. |
| **E-Doc** | Apre le impostazioni dei documenti elettronici quando il tipo le supporta. |
| **Document Sub Types** | Apre i sottotipi di questo tipo di documento. |

A seconda delle funzionalità della tua organizzazione, potresti vedere altri link, ad esempio per le regole di validazione o di trasformazione. Scegli il link sulla scheda del tipo che vuoi modificare.

## Modificare campi e impostazioni di riconoscimento

Clicca su **Fields** su una scheda per visualizzarne i gruppi di campi. In alto nella pagina, **OCR** e **Match Score** impostano le soglie di riconoscimento, **Restore Defaults** ripristina tali soglie e **Search by Name** trova un campo. Usa **Create new group** per organizzare i campi e **Create field** all'interno di un gruppo per aggiungerne uno. **Master Data Settings** apre la relativa configurazione dei dati anagrafici.

Ogni riga di campo ha controlli come **Required**, **Read Only**, **Hidden**, **Force Validation**, **Use AI**, OCR, Match Score e Formula. Consulta la [guida ai Fields](../../settings/global-settings/document-types/fields/README.md) prima di modificare i singoli valori. Clicca su **Save Settings** nella pagina Fields per conservare le modifiche.

<figure><img src="../../../.gitbook/assets/document-types-invoice-fields-en-20260928.png" alt="Pagina Fields di Invoice con impostazioni di riconoscimento, gruppi di campi, controlli per campo e Save Settings"><figcaption><p>La pagina Fields ha un proprio pulsante Save Settings.</p></figcaption></figure>

## Creare un tipo di documento personalizzato

Scorri fino a **Custom Document Types** e clicca su **+ New**. Segui [Adding/Editing Document Types](../../settings/global-settings/document-types/adding-editing-document-types.md) per configurare il nuovo tipo.

<figure><img src="../../../.gitbook/assets/document-types-custom-new-en-20260928.png" alt="Parte inferiore della pagina Document Types con la sezione Custom Document Types e il pulsante New"><figcaption><p>Usa New sotto Custom Document Types per iniziare a creare un tipo.</p></figcaption></figure>
