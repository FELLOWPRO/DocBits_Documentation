# Esportazione

## Panoramica

La pagina Esportazione mostra tutte le configurazioni di esportazione impostate, incluso se sono attive o inattive. Da qui, gli utenti possono:

* Visualizzare e gestire le configurazioni di esportazione esistenti
* Creare nuove connessioni di esportazione (ad es. verso **Infor**, **Infor & IDM**, **Webhook** o **SFTP**)
* Modificare o eliminare configurazioni di esportazione esistenti

## Dove trovarlo

Lo trovi in: **Impostazioni** → **Elaborazione documenti** → **Esportazione**

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_settings_menu_access.png)

## **Utilizzo della pagina Esportazione**

Quando apri la pagina Esportazione, vedrai un elenco di tutte le configurazioni di esportazione esistenti.

Ogni riga nell'elenco mostra:

* **Indicatore di stato**
  * **Verde** significa che l'esportazione è attiva
  * **Rosso** significa che l'esportazione è disattivata
* **Nome** – il nome della configurazione di esportazione
* **Tipo di documento** – il tipo di documento per cui è configurata l'esportazione
* **Sotto-organizzazione** – se l'esportazione è limitata a una sotto-organizzazione specifica
* **Metodo di esportazione** – dove verrà inviato il documento (ad es. Infor, IDM, SFTP)
* **Azioni** – pulsanti per **modificare, eliminare** o **attivare/disattivare** la configurazione

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_list_view.png)

#### **Regole importanti per la configurazione dell'esportazione**

Per ogni **tipo di documento** **all'interno di una data organizzazione o sotto-organizzazione**, si applicano le seguenti regole:

* Puoi avere **solo un'esportazione Infor attiva**
* Puoi avere **solo un'esportazione non-Infor attiva** (ad es. Webhook, SFTP)

Tuttavia, è possibile avere:

* **Un'esportazione Infor attiva** _e_ **un'esportazione non-Infor attiva** contemporaneamente per lo stesso tipo di documento
* **Diverse configurazioni di esportazione per diverse sotto-organizzazioni** — ad esempio, un'esportazione Infor per la Sotto-Org A e un'altra esportazione Infor per la Sotto-Org B

## **Creazione di una nuova esportazione**

Per creare una nuova esportazione:

1. Clicca sul pulsante **"Nuovo"**. ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_create_new_button.png)
2. Seleziona il **Tipo di esportazione** che vuoi configurare (ad es. Infor, IDM, SFTP).
3. Compila i campi richiesti in base al tipo di esportazione.
4. Salva la configurazione.

## Opzioni di esportazione

#### Webhook

<details>

<summary>Webhook</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_webhook_configuration.png)

**Descrizione dei campi**

* **Title** Il nome della configurazione di esportazione. Apparirà nell'elenco delle esportazioni.
* **Sub-Organization** _(opzionale)_ Un menu a tendina con tutte le sotto-organizzazioni disponibili.
  * Se lasciato vuoto: si applica all'organizzazione principale.
  * Se selezionato: l'esportazione si applicherà solo alla sotto-organizzazione scelta.
* **Document Type** Menu a tendina che elenca tutti i tipi di documento disponibili. Questo determina a quale tipo di documento si applica questa configurazione di esportazione.
* **Export URL** L'URL di destinazione dove il documento deve essere esportato.

</details>

#### SFTP

<details>

<summary>SFTP</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_sftp_configuration.png)

**Descrizione dei campi**

* **Title** Il nome della configurazione di esportazione. Apparirà nell'elenco delle esportazioni.
* **Sub-Organization** _(opzionale)_ Un menu a tendina con tutte le sotto-organizzazioni disponibili.
  * Se lasciato vuoto: si applica all'organizzazione principale.
  * Se selezionato: l'esportazione si applicherà solo alla sotto-organizzazione scelta.
* **Document Type** Menu a tendina che elenca tutti i tipi di documento disponibili. Questo determina a quale tipo di documento si applica questa configurazione di esportazione.
* **Username** Il nome utente utilizzato per autenticarsi sul server SFTP.
* **Password** La password corrispondente per l'account SFTP. Assicurati che l'account abbia accesso in scrittura alla cartella specificata.
* **Server URL** Il nome host o l'indirizzo IP del server SFTP di destinazione.
* **Port** La porta utilizzata per connettersi al server SFTP.
* **Folder** Il percorso sul server SFTP dove i documenti devono essere caricati (ad es. `/incoming/invoices/`). Deve esistere ed essere scrivibile.
*   **XSLT File (Opzionale)**

    Il **file XSLT** permette la trasformazione del formato di esportazione predefinito di DocBits.

    * **Quando usarlo:** Solo se il sistema ricevente richiede una struttura diversa o una formattazione specifica diversa da quella predefinita di DocBits.
    * **Lasciarlo vuoto** se il formato di esportazione predefinito soddisfa i requisiti.



**Impostazioni avanzate:**

* **Filename Export Mode** Specifica se il file esportato mantiene il nome file originale o viene rinominato usando l'ID documento DocBits.
* **Include Document History** Quando abilitato, il file esportato includerà la cronologia del documento basata sui log disponibili nella dashboard.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_sftp_2.png)

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_sftp_3.png)

</details>

#### Esportazione Infor su SFTP

<details>

<summary>Esportazione Infor su SFTP</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_infor_sftp_configuration.png)

**Descrizione dei campi**

* **Title** Il nome della configurazione di esportazione. Apparirà nell'elenco delle esportazioni.
* **Sub-Organization** _(opzionale)_ Un menu a tendina con tutte le sotto-organizzazioni disponibili.
  * Se lasciato vuoto: si applica all'organizzazione principale.
  * Se selezionato: l'esportazione si applicherà solo alla sotto-organizzazione scelta.
* **Document Type** Menu a tendina che elenca tutti i tipi di documento disponibili. Questo determina a quale tipo di documento si applica questa configurazione di esportazione.
* **IDM Mapping File** Seleziona un file di mapping dal file manager. [Hai bisogno di aiuto per crearne uno? Consulta la Guida al Mapping IDM](../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
* **BOD Mapping File** Seleziona un file di mapping dal file manager. [Hai bisogno di aiuto per crearne uno? Consulta la Guida al Mapping BOD](../../../infor-integration-and-configuration/exporting-to-infor/creating-a-bod-mapping-file.md)
* **Folder** Il percorso sul server SFTP dove i documenti devono essere caricati (ad es. `/incoming/invoices/`). Deve esistere ed essere scrivibile.

</details>

#### **SMB**

<details>

<summary>SMB</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_smb_configuration.png)

**Descrizione dei campi**

* **Title** Il nome della configurazione di esportazione. Apparirà nell'elenco delle esportazioni.
* **Sub-Organization** _(opzionale)_ Un menu a tendina con tutte le sotto-organizzazioni disponibili.
  * Se lasciato vuoto: si applica all'organizzazione principale.
  * Se selezionato: l'esportazione si applicherà solo alla sotto-organizzazione scelta.
* **Document Type** Menu a tendina che elenca tutti i tipi di documento disponibili. Questo determina a quale tipo di documento si applica questa configurazione di esportazione.
* **Username** Il nome utente utilizzato per connettersi alla condivisione SMB.
* **Password** La password corrispondente per l'autenticazione SMB.
* **Server URL** L'indirizzo del server SMB.
* **Port** Numero di porta utilizzato per accedere alla condivisione SMB.
* **Folder** Il percorso della cartella all'interno della condivisione SMB dove i documenti devono essere salvati (ad es. `/incoming/invoices/`). Deve esistere ed essere scrivibile.
*   **JPL Mapping File (Opzionale)**

    Il **file JPL** è utilizzato per definire una trasformazione dei dati esportati prima che vengano scritti sulla condivisione SMB.

    * **Quando usarlo:** Solo quando i dati del documento esportato devono essere adattati per corrispondere alla formattazione esterna o alle aspettative del sistema.
    * **Lasciarlo vuoto** se non è necessaria alcuna trasformazione.

</details>

#### **Infor IDM**

<details>

<summary>Infor IDM</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_infor_idm_configuration.png)

**Descrizione dei campi**

* **Title** Il nome della configurazione di esportazione. Apparirà nell'elenco delle esportazioni.
* **Sub-Organization** _(opzionale)_ Un menu a tendina con tutte le sotto-organizzazioni disponibili.
  * Se lasciato vuoto: si applica all'organizzazione principale.
  * Se selezionato: l'esportazione si applicherà solo alla sotto-organizzazione scelta.
* **Document Type** Menu a tendina che elenca tutti i tipi di documento disponibili. Questo determina a quale tipo di documento si applica questa configurazione di esportazione.
* **ION Mapping File** Seleziona un file di mapping dal file manager.
* **IDM Mapping File** Seleziona un file di mapping dal file manager. [Hai bisogno di aiuto per crearne uno? Consulta la Guida al Mapping IDM](../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
* **Cloud / On-Prem Toggle** Un interruttore per indicare il tipo di distribuzione Infor:
  * **Cloud**: Seleziona questo se sei un cliente Infor CloudSuite.
  * **On-Prem**: Seleziona questo se Infor è self-hosted.

</details>

#### **Infor ION**

<details>

<summary>Infor ION</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_infor_ion_configuration.png)

**Descrizione dei campi**

* **Title** Il nome della configurazione di esportazione. Apparirà nell'elenco delle esportazioni.
* **Sub-Organization** _(opzionale)_ Un menu a tendina con tutte le sotto-organizzazioni disponibili.
  * Se lasciato vuoto: si applica all'organizzazione principale.
  * Se selezionato: l'esportazione si applicherà solo alla sotto-organizzazione scelta.
* **Document Type** Menu a tendina che elenca tutti i tipi di documento disponibili. Questo determina a quale tipo di documento si applica questa configurazione di esportazione.
* **ION Mapping File** Seleziona un file di mapping dal file manager.
* **BOD Mapping File** Seleziona un file di mapping dal file manager. [Hai bisogno di aiuto per crearne uno? Consulta la Guida al Mapping BOD](../../../infor-integration-and-configuration/exporting-to-infor/creating-a-bod-mapping-file.md)
* **Cloud / On-Prem Toggle** Un interruttore per indicare il tipo di distribuzione Infor:
  * **Cloud**: Seleziona questo se sei un cliente Infor CloudSuite.
  * **On-Prem**: Seleziona questo se Infor è self-hosted.

</details>

#### Infor IDM + ION BOD

<details>

<summary>Infor IDM + ION BOD</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_infor_idm_ion_bod_configuration.png)

**Descrizione dei campi**

* **Title** Il nome della configurazione di esportazione. Apparirà nell'elenco delle esportazioni.
* **Sub-Organization** _(opzionale)_ Un menu a tendina con tutte le sotto-organizzazioni disponibili.
  * Se lasciato vuoto: si applica all'organizzazione principale.
  * Se selezionato: l'esportazione si applicherà solo alla sotto-organizzazione scelta.
* **Document Type** Menu a tendina che elenca tutti i tipi di documento disponibili. Questo determina a quale tipo di documento si applica questa configurazione di esportazione.
* **ION Mapping File** Seleziona un file di mapping dal file manager.
* **IDM Mapping File** Seleziona un file di mapping dal file manager. [Hai bisogno di aiuto per crearne uno? Consulta la Guida al Mapping IDM](../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
* **BOD Mapping File** Seleziona un file di mapping dal file manager. [Hai bisogno di aiuto per crearne uno? Consulta la Guida al Mapping BOD](../../../infor-integration-and-configuration/exporting-to-infor/creating-a-bod-mapping-file.md)
* **Cloud / On-Prem Toggle** Un interruttore per indicare il tipo di distribuzione Infor:
  * **Cloud**: Seleziona questo se sei un cliente Infor CloudSuite.
  * **On-Prem**: Seleziona questo se Infor è self-hosted.

</details>

### Per i clienti Infor CloudSuite

#### Infor IDM + LN

<details>

<summary>Infor IDM + LN</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_infor_idm_ln_configuration.png)

**Descrizione dei campi**

* **Title** Il nome della configurazione di esportazione. Apparirà nell'elenco delle esportazioni.
* **Sub-Organization** _(opzionale)_ Un menu a tendina con tutte le sotto-organizzazioni disponibili.
  * Se lasciato vuoto: si applica all'organizzazione principale.
  * Se selezionato: l'esportazione si applicherà solo alla sotto-organizzazione scelta.
* **Document Type** Menu a tendina che elenca tutti i tipi di documento disponibili. Questo determina a quale tipo di documento si applica questa configurazione di esportazione.
* **ION Mapping File** Seleziona un file di mapping dal file manager.
* **IDM Mapping File** Seleziona un file di mapping dal file manager. [Hai bisogno di aiuto per crearne uno? Consulta la Guida al Mapping IDM](../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
* **LN Mapping File** Seleziona un file di mapping dal file manager. [Hai bisogno di aiuto per crearne uno? Consulta l'Esempio di Mapping LN](../../../infor-integration-and-configuration/exporting-to-infor/ln/example-export-ln/)

</details>

#### Infor IDM + M3

<details>

<summary>Infor IDM + M3</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_infor_idm_m3_configuration.png)

**Descrizione dei campi**

* **Title** Il nome della configurazione di esportazione. Apparirà nell'elenco delle esportazioni.
* **Sub-Organization** _(opzionale)_ Un menu a tendina con tutte le sotto-organizzazioni disponibili.
  * Se lasciato vuoto: si applica all'organizzazione principale.
  * Se selezionato: l'esportazione si applicherà solo alla sotto-organizzazione scelta.
* **Document Type** Menu a tendina che elenca tutti i tipi di documento disponibili. Questo determina a quale tipo di documento si applica questa configurazione di esportazione.
* **ION Mapping File** Seleziona un file di mapping dal file manager.
* **IDM Mapping File** Seleziona un file di mapping dal file manager. [Hai bisogno di aiuto per crearne uno? Consulta la Guida al Mapping IDM](../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
* **M3 Mapping File** Seleziona un file di mapping dal file manager. [Hai bisogno di aiuto per crearne uno? Consulta l'Esempio di Mapping M3](../../../infor-integration-and-configuration/exporting-to-infor/m3/example-export-m3.md)

</details>

#### Infor IDM + M3 (toml)

<details>

<summary>Infor IDM + M3 (toml)</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_infor_idm_m3_toml_configuration.png)

**Descrizione dei campi**

* **Title** Il nome della configurazione di esportazione. Apparirà nell'elenco delle esportazioni.
* **Sub-Organization** _(opzionale)_ Un menu a tendina con tutte le sotto-organizzazioni disponibili.
  * Se lasciato vuoto: si applica all'organizzazione principale.
  * Se selezionato: l'esportazione si applicherà solo alla sotto-organizzazione scelta.
* **Document Type** Menu a tendina che elenca tutti i tipi di documento disponibili. Questo determina a quale tipo di documento si applica questa configurazione di esportazione.
* **ION Mapping File** Seleziona un file di mapping dal file manager.
* **IDM Mapping File** Seleziona un file di mapping dal file manager. [Hai bisogno di aiuto per crearne uno? Consulta la Guida al Mapping IDM](../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
* **M3 toml Mapping File** Seleziona un file di mapping dal file manager o usa l'opzione seleziona Toml per usare un toml creato con il gestore delle regole. [Hai bisogno di aiuto per crearne uno? Consulta la Guida al Gestore delle Regole](rule-manager/)

</details>
