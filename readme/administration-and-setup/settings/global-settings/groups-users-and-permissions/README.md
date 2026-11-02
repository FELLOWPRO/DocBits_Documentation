# Gruppi, Utenti e Autorizzazioni

## Creare un gruppo e verificare l’accesso ai documenti

Con le autorizzazioni di gruppo già attive, crea un gruppo di revisione e aggiungi un utente di prova senza diritti di amministratore. Consenti di elencare, visualizzare e modificare le fatture assegnate; lascia disabilitate eliminazione, modifiche massive e approvazioni. Salva e riapri le impostazioni, poi accedi come utente normale: la fattura assegnata è visibile e il documento di controllo non assegnato non compare.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/groups-permissions-admin/v1/it.mp4" %}

[Guarda con i sottotitoli](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/groups-permissions-admin/v1/it.html)

Queste impostazioni rispondono a tre domande diverse: chi può accedere, in quale sotto-organizzazione lavora e che cosa può fare il suo gruppo.

| Se devi… | Apri… |
| --- | --- |
| Aggiungere o modificare l'account di una persona | **Impostazioni** → **Utenti**; poi leggi [Utenti](users/README.md). |
| Organizzare l'accesso tra le unità dell'azienda | **Impostazioni** → **Sotto-organizzazioni**; poi leggi [Sotto-organizzazioni](sub-organizations/README.md). |
| Controllare l'accesso per gruppo | **Impostazioni** → **Gruppi e autorizzazioni**; poi leggi [Gruppi e Autorizzazioni](groups-and-permissions/README.md). |

<figure><img src="../../../../.gitbook/assets/prior-t008-it.png" alt="Pannello di selezione dei gruppi."><figcaption><p>Pannello di selezione dei gruppi.</p></figcaption></figure>

Se un utente non riesce a vedere un documento o un'azione, controlla prima il suo account e la sua organizzazione. Poi controlla le autorizzazioni del gruppo pertinente. Usa un account di test non amministratore per verificare l'accesso che avrà realmente un utente normale prima di modificare un'organizzazione in produzione.
