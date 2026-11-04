# Dashboard

## Panoramica

Le impostazioni del Cruscotto sono progettate per aiutare gli amministratori a controllare la presentazione dei dati e l'interazione all'interno del cruscotto DocBits. Queste impostazioni determinano quali informazioni sono immediatamente disponibili al momento del login, garantendo che gli utenti abbiano accesso rapido ai dati più rilevanti per i loro compiti.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/dashboard_settings_1.png)

## Accesso alle Impostazioni del Cruscotto

Per accedere alle impostazioni del cruscotto, navigare a:\
**Impostazioni → Impostazioni globali → Cruscotto**

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_dashboard.png)

## **Generale**

* **Azzeramento dei filtri**: Consente di configurare quando i filtri del cruscotto devono essere azzerati, ad esempio dopo il caricamento di documenti, il riavvio di documenti o l'esportazione di documenti. Questo aiuta a mantenere una visualizzazione pulita dei dati in base a specifiche fasi del flusso di lavoro.
* **Dati del cruscotto**:
  * **Caricamento automatico del cruscotto**: Controlla se il cruscotto deve caricare automaticamente i dati all'accesso dell'utente, il che può aiutare a ridurre i tempi di caricamento e migliorare l'esperienza utente caricando solo i dati quando necessario.
  *   **Esportazione dei dati del cruscotto**: Questa funzione aggiunge un nuovo pulsante **Esporta** alla barra degli strumenti del cruscotto, consentendo di esportare la vista attuale del cruscotto come file **.csv** o **.xlsx**.

      ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/dashboard_settings_3.png)

## **Cronologia delle esportazioni**

Nella **Cronologia delle esportazioni**, vedrai una tabella che elenca tutte le esportazioni passate insieme alle informazioni chiave su ciascuna richiesta.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/dashboard_settings_4.png)

I seguenti dettagli sono inclusi:

* **Posta elettronica**: L'indirizzo email da cui è stata richiesta l'esportazione.
* **Stato**: Lo stato attuale dell'esportazione (In attesa, Completato).
* **Richiesta effettuata il**: La data e l'ora in cui è stata avviata l'esportazione.
* **Completato il**: La data e l'ora in cui è stata completata l'esportazione.
* **Formato**: Il formato del file utilizzato per l'esportazione (CSV, XLSX).
* **Filtri utilizzati**: Qualsiasi filtro che è stato applicato al cruscotto al momento dell'esportazione.

<mark style="color:red;">**Nota**</mark>: Per esportare le tabelle, l'opzione Esporta dati del cruscotto nella sezione [Generale](./#generale) deve essere attiva.

## **Azione**

* **Assegnare a**: Questa funzione consente agli utenti di definire i permessi per l'assegnazione dei documenti.
  * **Solo per Admin**: Solo gli utenti admin possono assegnare documenti, indipendentemente dai permessi concessi agli utenti non admin.
  * **Tutti gli utenti**: Tutti gli utenti che hanno ricevuto i necessari [permessi](../groups-users-and-permissions/groups-and-permissions/activating-permissions.md) possono assegnare documenti.
* **Riavvio**: Questa funzione consente agli utenti di definire i permessi per il riavvio dei documenti.
  * **Solo per Admin**: Solo gli utenti con privilegi di Admin possono riavviare documenti, indipendentemente dai permessi concessi agli utenti non admin.
  * **Solo Admin e Assegnatario**: Solo gli utenti con privilegi di Admin e l'utente assegnato possono riavviare il documento.
  * **Tutti gli utenti**: Tutti gli utenti che hanno ricevuto i necessari [permessi](../groups-users-and-permissions/groups-and-permissions/activating-permissions.md) possono riavviare documenti.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/dashboard_settings_2.png)

## **Filtri**

* **Stile del filtro di stato**: Determina lo stile di presentazione dei filtri di stato, che può essere impostato su predefinito o personalizzato in base al focus operativo degli utenti.
* **Filtro di stato personalizzato**: Consente la creazione e l'applicazione di filtri personalizzati che possono mirare a specifici stati dei documenti come "Nuovo", "In validazione" o "In esportazione". Questo consente agli utenti di accedere rapidamente ai documenti in specifiche fasi di elaborazione.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/dashboard_settings_5.png)

## Cruscotto spedizioni anticipate

* **Visibilità degli ordini consegnati**: Questa funzione consente all'utente di specificare la durata per la quale gli ordini consegnati saranno visibili.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/dashboard_settings_6.png)

Queste impostazioni del cruscotto sono cruciali per garantire che la piattaforma DocBits sia il più reattiva e utile possibile, fornendo agli utenti uno strumento potente per monitorare e gestire le attività di elaborazione dei documenti direttamente dal cruscotto.
