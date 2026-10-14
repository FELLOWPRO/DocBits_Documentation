---
description: >-
  Come trovare e creare le chiavi API che danno ad altri sistemi l'accesso a
  DocBits
---

# API Key Management

Una API key consente a un altro sistema — il proprio ERP, uno script o un'applicazione partner — di dialogare con DocBits senza che un utente effettui l'accesso. La propria organizzazione può avere tutte le chiavi che servono, e ognuna si gestisce separatamente: le si dà un nome proprio, si decide se scade e la si revoca singolarmente se dovesse mai essere esposta.

Poiché ogni integrazione può avere la propria chiave, se ne può disattivare una senza disturbare le altre.

## Aprire la gestione delle chiavi API

Andare in **Settings** e selezionare **Integration & SSO** sotto **System & Administration**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/api-key-settings-overview.png)

La sezione **API Key** in cima alla pagina elenca tutte le chiavi che la propria organizzazione possiede.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/api-key-list.png)

## Capire l'elenco

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/api-key-list-row.png)

| Colonna | Che cosa indica |
| --- | --- |
| **Key** | I primi caratteri della chiave, seguiti da `****`. Il resto non viene più mostrato dopo la creazione — vedere [Creare una chiave API](#creare-una-chiave-api). |
| **Name** | Il nome dato alla chiave, con la sua descrizione sotto. |
| **Expires** | La data in cui la chiave smette di funzionare, o **Never** se non se ne è impostata una. |
| **Last Used** | Quando è arrivata l'ultima richiesta con questa chiave. **Never used** significa che nessun sistema l'ha ancora usata — utile per individuare chiavi che si possono rimuovere senza rischi. |
| **Status** | **Active** significa che la chiave funziona. Una chiave revocata è disattivata in modo permanente. |
| **Actions** | Il menu a tre puntini, da cui si può revocare la chiave. |

Se si hanno più chiavi di quante ne stiano in una pagina, usare i controlli di paginazione in fondo all'elenco.

{% hint style="info" %}
**Last Used** è il modo più rapido per trovare chiavi di cui nessuno ha più bisogno. Una chiave mai usata, o non usata da mesi, è una buona candidata alla revoca.
{% endhint %}

## Creare una chiave API

1. Fare clic su **+ Create API Key** in alto a destra nella sezione API Keys.
2. Compilare la finestra di dialogo:

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/api-key-create-dialog.png)

| Campo | Cosa inserire |
| --- | --- |
| **Key Name** | Obbligatorio. Darle il nome del sistema che la userà — `M3 Production`, `Invoice Import Script` — così da poter capire in seguito a quale integrazione appartiene una chiave. |
| **Description** | Facoltativo. Spazio per una nota su a cosa serve la chiave o su chi l'ha configurata. |
| **Expiration** | Scegliere una data di scadenza, oppure lasciare **Never expires**. Una data di scadenza è la scelta più sicura: la chiave si ritira da sé se l'integrazione dovesse essere dimenticata. |

3. Fare clic su **Create**. DocBits mostra la nuova chiave:

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/api-key-created.png)

4. Copiare la chiave con l'icona di copia e incollarla direttamente nel sistema che la userà, oppure nel proprio gestore di password.
5. Spuntare **I have copied and saved this key** e fare clic su **Done**.

{% hint style="danger" %}
**La chiave completa viene mostrata una sola volta.** DocBits la memorizza in una forma cifrata che non può essere ricondotta all'originale, quindi nessuno — né i propri amministratori né il supporto DocBits — può più recuperarla in seguito. Se la si perde, revocare la chiave e crearne una nuova.
{% endhint %}

Trattare la chiave come una password. Chiunque la possieda può operare sui documenti e sui dati della propria organizzazione.
