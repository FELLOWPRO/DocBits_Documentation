# Configurare sottotipi

Usare un sottotipo di documento quando fatture dello stesso tipo di documento richiedono campi diversi, un layout di convalida diverso o propri script di elaborazione. Prima [creare un sottotipo](creating-a-new-sub-type.md), poi aprire **Impostazioni → Tipi di Documento**, scegliere il tipo di documento e aprire **Sottotipi di Documento**. Nella riga del sottotipo, aprire **Azioni** (i tre puntini). Il menu offre **Campi**, **Costruttore di layout** e **Script**; contiene anche [Copia, Modifica ed Elimina](using-actions.md).

<figure><img src="../../../../.gitbook/assets/subtype-actions-menu-it.png" alt="Menu Azioni di un sottotipo di documento che mostra Campi, Costruttore di layout, Script, Copia, Modifica ed Elimina"><figcaption><p>Scegliere la parte del sottotipo che si desidera configurare.</p></figcaption></figure>

## Campi

Selezionare **Campi** per decidere quali informazioni gli utenti vedono e inseriscono per questo sottotipo. È possibile creare un campo in un gruppo, contrassegnare un campo esistente come obbligatorio, di sola lettura o nascosto e regolare le opzioni di riconoscimento. Selezionare **Salva le impostazioni** dopo aver apportato le modifiche. Usare [Aggiungere e modificare i campi](fields/adding-and-editing-fields.md) per i passaggi, [Configurazione delle proprietà dei campi](fields/configuring-field-properties-1.md) per le opzioni delle colonne e [Impostazioni dei dati master](fields/master-data-settings.md) quando un campo deve usare dati di ricerca.

<figure><img src="../../../../.gitbook/assets/subtype-fields-it.png" alt="Impostazioni dei campi in italiano per un sottotipo di fattura sintetico, con gruppi di campi, colonne delle proprietà e Salva le impostazioni"><figcaption><p>Impostazioni dei campi nell'organizzazione di test della documentazione. Non vengono mostrati dati di clienti.</p></figcaption></figure>

## Costruttore di layout

Selezionare **Costruttore di layout** per organizzare gruppi e campi nella schermata di convalida del documento. Il lato sinistro elenca gli elementi; il lato destro accetta un documento di esempio per l'anteprima. Verificare il risultato e selezionare **Salva** quando il layout è pronto. La [guida del Costruttore di Layout](../../../setup/document-types/layout-builder.md) spiega gli elementi, l'anteprima del documento e il salvataggio di un layout.

<figure><img src="../../../../.gitbook/assets/subtype-layout-it.png" alt="Costruttore di layout in italiano per un sottotipo di fattura sintetico, con gruppi, caricamento dell'anteprima e Salva"><figcaption><p>Layout del sottotipo prima di aggiungere un documento di esempio.</p></figcaption></figure>

## Script

Selezionare **Script** per visualizzare gli script di questo sottotipo. In un elenco vuoto, selezionare **Nuovo** o **Crea script** per iniziare. La ricerca e i filtri **Tutti**, **Attivo** e **Inattivo** aiutano a trovare gli script esistenti. Seguire [Creazione e modifica degli script](script/creating-and-editing-scripts.md) per crearne uno, e [Attivazione e gestione degli script](script/script-activation-and-management.md) prima di attivarlo per l'elaborazione.

<figure><img src="../../../../.gitbook/assets/subtype-scripts-it.png" alt="Elenco vuoto di script in italiano per un sottotipo di fattura sintetico, con Nuovo e i filtri di stato"><figcaption><p>Nessuno script è stato creato nel sottotipo di test della documentazione.</p></figcaption></figure>
