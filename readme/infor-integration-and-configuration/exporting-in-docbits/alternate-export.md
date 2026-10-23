# Esportazione alternativa

## **Passaggio 1: creare una nuova esportazione**

1. Vai su **Impostazioni** > **Elaborazione documenti** > **Esportazione**.
2. Fai clic su **Crea nuova esportazione** per definire una nuova configurazione di esportazione.
3. Salva la configurazione e assicurati che l'esportazione sia **disattivata**.

<figure><img src="../../.gitbook/assets/image (368).png" alt="Elenco delle impostazioni di esportazione con le righe Alternate-Export-Invoice-LN-IDM-BOD ed Export-Invoice-LN per il tipo di documento Invoice, il metodo di esportazione Infor-IoN-Cloud e le icone delle azioni"><figcaption></figcaption></figure>

### **Passaggio 2: abilitare l'esportazione alternativa**

1. Vai su **Impostazioni** > **Impostazioni globali** > **Tipo di documento** > **Altre impostazioni**.
2. Individua l'impostazione **Esportazione alternativa** e attivala.
3. Configura quanto segue:
   * **Stato del documento**: specifica lo stato dei documenti dopo l'esportazione alternativa.
   * **Configurazione di esportazione**: seleziona la configurazione di esportazione appena creata da utilizzare per l'esportazione alternativa.

<figure><img src="../../.gitbook/assets/image (369).png" alt="Pagina More Settings del tipo di documento Invoice che mostra l'opzione Alternate Export con lo stato Pending approval e l'Export Configuration Alternate-Export-Invoice-LN-IDM-BOD-8203"><figcaption></figcaption></figure>

## Utilizzo dell'esportazione alternativa

**Nella schermata PO-Matching**

* Dopo aver abilitato l'esportazione alternativa, potrai selezionarla direttamente nella schermata **PO-Matching**.

<figure><img src="../../.gitbook/assets/image (370).png" alt="Schermata PO Matching con la ricerca del numero d'ordine 100000300, i pulsanti CONFIRM &amp;amp; EXPORT e Reject e il pannello Document Alternate Export"><figcaption></figcaption></figure>

**Con la card del workflow**

* La card del workflow **Alternate Export** può essere utilizzata anche per automatizzare questo processo. Configura la card come necessario per applicare la logica di esportazione alternativa al tuo workflow.
