# Schermata di Abbinamento Ordini di Acquisto

Usa **Corrispondenza PO** per confrontare le righe dell'ordine di acquisto caricate per un documento con le righe di fattura estratte. I dati dell'ordine di acquisto possono provenire da un'integrazione ERP o da un altro import configurato. La schermata mostra il documento accanto alle due tabelle, così puoi controllare numeri, quantità, prezzi e differenze prima di salvare o esportare.

## Abbinare le righe della fattura a un ordine

Il percorso inizia con un numero d’ordine riconosciuto e tre righe di fattura abbinate. Mostra poi la ricerca manuale come eccezione, un collegamento intenzionalmente errato, un abbinamento parziale, quello automatico e il salvataggio. Verifica il risultato dopo il ricaricamento: salvare l’abbinamento non approva né esporta da solo la fattura.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/po-matching-customer/v4/it.mp4" %}

[Guarda il video con i sottotitoli](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/po-matching-customer/v4/it.html)

{% hint style="info" %}
La registrazione usa dati di prova sintetici con tre righe di fattura estratte e il relativo ordine. Carta, scatole per archivio e consegna ammontano a 118 EUR netti. L’abbinamento completo mostra 118 EUR abbinati e nessun importo aperto.
{% endhint %}

<figure><img src="../../../.gitbook/assets/po-tutorial-v4-full-it.png" alt="Abbinamento completo: tutte e tre le righe sono collegate, con 118 EUR abbinati e 0 EUR aperti."><figcaption><p>Abbinamento completo: tutte e tre le righe sono collegate, con 118 EUR abbinati e 0 EUR aperti.</p></figcaption></figure>

## Trovare e ispezionare un ordine di acquisto

1. Apri la fattura in **Corrispondenza PO**. Quando il numero d’ordine viene riconosciuto, DocBits carica l’ordine corrispondente. Usa la ricerca manuale se il numero manca o per controllare un altro ordine.
2. Seleziona l'icona del filtro accanto alla casella di ricerca per **Parola chiave**, **Fornitore**, **Stato**, **Stato ordine**, date, intervallo di importo, ordinamento e numero di record mostrati. Seleziona **Più** per criteri aggiuntivi. Seleziona **Applica** per cercare o **Elimina** per ripristinare i filtri.
3. Seleziona un numero di ordine di acquisto sopra la tabella per ispezionarne le righe. L'icona di aggiornamento accanto al numero ricarica i dati di quell'ordine. Un ricaricamento può dipendere dall'integrazione configurata.
4. Confronta ogni riga dell’ordine con la fattura e la tabella estratta. Il **+** apre i dettagli di abbinamento esistenti; non collega da solo la riga alla fattura.

<figure><img src="../../../.gitbook/assets/po-tutorial-v4-search-it.png" alt="La ricerca manuale mostra le tre righe dell’ordine di prova. Usa i filtri quando servono; un numero d’ordine riconosciuto non richiede una seconda ricerca."><figcaption><p>La ricerca manuale mostra le tre righe dell’ordine di prova. Usa i filtri quando servono; un numero d’ordine riconosciuto non richiede una seconda ricerca.</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/po-tutorial-v4-partial-it.png" alt="Abbinamento parziale: la carta corrisponde a 50 EUR abbinati; restano aperti 68 EUR. Non indica una soglia fissa del cinquanta per cento."><figcaption><p>Abbinamento parziale: la carta corrisponde a 50 EUR abbinati; restano aperti 68 EUR. Non indica una soglia fissa del cinquanta per cento.</p></figcaption></figure>

## Abbinare le righe e verificare il risultato

Quando entrambe le tabelle contengono righe, collega una riga di fattura alla riga corrispondente dell'ordine di acquisto trascinandola, oppure usa le azioni di abbinamento nel menu contestuale della riga. **Auto Match** tenta di collegare le righe idonee usando le regole della tua organizzazione. Verifica il risultato prima di salvare: il solo numero di articolo corrispondente non dimostra che quantità, prezzo o condizioni di consegna coincidano. Vedi [Strumenti di Abbinamento Ordine di Acquisto](purchase-order-matching-tools.md) per la barra degli strumenti, i controlli delle colonne e le azioni manuali, e [Scorciatoie da Tastiera](keyboard-shortcuts.md) per le azioni da tastiera.

Se un documento non è abbinato, leggi il motivo mostrato sopra l'area dell'ordine di acquisto. Può indicare che il numero PO è mancante, che l'ordine non è stato trovato, che le sue righe non sono disponibili o che la fattura non ha righe estratte. Correggi il documento o la configurazione indicata da quel motivo. Un amministratore può ispezionare le [regole di abbinamento](../../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-matching-rules.md) e l'[estrazione della tabella](../../../administration-and-setup/settings/document-processing/classification-and-extraction/README.md) quando non compaiono righe di fattura.

Messaggi comuni e passi successivi:

| Cosa vedi | Cosa controllare |
| --- | --- |
| Nessun numero di ordine di acquisto | Inserisci o correggi il numero PO sul documento, poi salva. |
| Nessun ordine di acquisto trovato | Controlla il numero e verifica che l'ordine sia stato importato in questa organizzazione. |
| L'ordine è stato trovato ma non è collegato | Prova **Auto Match**, oppure collega le righe manualmente dopo aver controllato entrambe le tabelle. |
| Nessuna riga dell'ordine corrisponde | Confronta i valori della fattura con l'ordine e controlla la cronologia dell'abbinamento. |
| Nessuna voce di linea nella fattura | Controlla l'[estrazione della tabella](../../../administration-and-setup/settings/document-processing/classification-and-extraction/README.md) prima di provare ad abbinare. |
| Nessuna riga aperta dell'ordine | Controlla gli [stati delle righe consumate](../../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/consumed-po-line-status.md) e gli stati esclusi. |

{% hint style="warning" %}
Il salvataggio può innescare di nuovo l'abbinamento dopo un numero PO cambiato o rilevato per la prima volta. Controlla il risultato mostrato dopo il salvataggio. Se un abbinamento non può essere salvato, leggi l'errore mostrato sullo schermo e chiedi a un amministratore di verificare la [regola di trasformazione](../../../administration-and-setup/settings/global-settings/document-types/transformation-rules.md) e le [regole di abbinamento](../../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-matching-rules.md).
{% endhint %}

Usa **Cronologia dell'abbinamento** (icona dell'orologio, dove i tuoi permessi lo consentono) per ispezionare come è stato deciso un abbinamento precedente. È una vista in sola lettura. Puoi rivedere quali regole sono state eseguite e perché un candidato non ha trovato corrispondenza; aprire la cronologia non esporta il documento.

### Più di una riga per abbinamento

Una singola riga di fattura può corrispondere a diverse righe dell'ordine, o viceversa, dove le tue regole di abbinamento lo consentono. Apri i dettagli **+** su una riga per ispezionare un eventuale abbinamento multiplo esistente. Controlla la quantità e il prezzo combinati, non solo una riga. Un pannello di dettagli vuoto significa che non c'è alcun abbinamento multiplo da ispezionare. Vedi [Strumenti di Abbinamento Ordine di Acquisto](purchase-order-matching-tools.md) per modificare i collegamenti.

### Quantità, differenze e sconti

A seconda della configurazione, l'abbinamento può confrontare la quantità ordinata, ricevuta o di consegna rimanente, oltre al prezzo unitario, al numero di articolo e ad altri campi mappati. Una differenza può essere accettata se il tipo di documento ha una tolleranza configurata. Controlla la discrepanza mostrata prima di accettarla. Le [impostazioni di tolleranza](../../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-tolerance-settings-additional-purchase-order-tolerance.md) e la [guida sugli sconti](discounts.md) spiegano questi casi.

L'area dei totali, quando disponibile, aiuta a riconciliare l'importo netto della fattura con le righe abbinate e le spese. Se rimane un **Importo non regolato**, ispeziona i valori delle singole righe e ogni [costing element](../../../administration-and-setup/settings/document-processing/classification-and-extraction/table-extraction-for-costing-element.md) prima dell'esportazione.

## Controllare i totali e salvare

Rivedi l'anteprima della fattura a destra e confronta i totali di riga e le eventuali spese. Per una spiegazione completa delle azioni nella barra degli strumenti superiore, vedi [Strumenti di Abbinamento Ordine di Acquisto](purchase-order-matching-tools.md). Seleziona **Salva** dopo aver modificato gli abbinamenti. Seleziona **Esportazione** solo dopo aver controllato il documento e il risultato dell'abbinamento; la freccia accanto a Esportazione mostra scelte di esportazione aggiuntive configurate. La tua organizzazione potrebbe avere azioni di esportazione diverse.

La barra degli strumenti dell'anteprima permette di spostarsi tra le pagine del documento, zoomare, scaricare l'originale e aprire una vista più grande. Usala per verificare che il numero dell'ordine di acquisto e i valori delle righe compaiano davvero sulla fattura. Se esci con modifiche di abbinamento non salvate, potrebbero andare perse.

I confronti disponibili e i valori di tolleranza dipendono dalle impostazioni del tuo tipo di documento. Leggi [Regole di Abbinamento PO](../../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-matching-rules.md), [Impostazioni di Tolleranza](../../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-tolerance-settings-additional-purchase-order-tolerance.md), [Stati di Disabilitazione](../../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-disable-statuses.md) e [Stato della Riga dell'Ordine Consumata](../../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/consumed-po-line-status.md) per le impostazioni dell'amministratore. Per righe da molti-a-uno, vedi [Sconti](discounts.md) e gli [Strumenti di Abbinamento](purchase-order-matching-tools.md).
