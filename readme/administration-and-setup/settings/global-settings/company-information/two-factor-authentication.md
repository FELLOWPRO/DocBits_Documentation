# Autenticazione a due fattori (Admin)

## Panoramica

In qualità di amministratore dell'organizzazione puoi **richiedere a ogni membro di usare l'autenticazione a due fattori (2FA)** quando accede con una password. Quando il requisito è attivo, un membro che non ha ancora configurato un secondo fattore viene guidato attraverso la registrazione prima di poter completare l'accesso.

Gli accessi tramite single sign-on (SSO) — Google, Microsoft, SAML — sono **esenti**: il loro provider di identità applica già la propria MFA, quindi il requisito riguarda solo gli accessi con password.

Questa impostazione si trova in **Impostazioni → Impostazioni Globali → Informazioni sulla Società → Autenticazione a due fattori** ed è disponibile solo per gli amministratori dell'organizzazione.

## Richiedere la MFA per la tua organizzazione

1. Vai su **Impostazioni → Impostazioni Globali → Informazioni sulla Società**.
2. Apri la sezione **Autenticazione a due fattori**.
3. Attiva **Richiedi l'autenticazione a due fattori per tutti i membri** e fai clic su **Salva**.

<figure><img src="../../../../.gitbook/assets/mfa-admin-requirement.png" alt="The organisation MFA requirement toggle and adoption report"><figcaption><p>Attiva il requisito per tutti i membri e monitora l'adozione più in basso.</p></figcaption></figure>

Una volta salvato, la modifica ha effetto entro un minuto. Da quel momento in poi:

* A un membro **con** un secondo fattore viene richiesto di fornirlo dopo la password, come al solito.
* Un membro **senza** un secondo fattore deve registrarne uno prima di ricevere una sessione.
* Gli accessi SSO / social non sono interessati.

{% hint style="warning" %}
Attivare questa opzione blocca gli accessi con password per i membri che non hanno un secondo fattore finché non completano la registrazione. Comunica la modifica al tuo team e valuta di abilitarla al di fuori delle ore di punta.
{% endhint %}

## Rapporto sull'adozione della MFA

Sotto l'interruttore, il pannello **Adozione della MFA** mostra quanto è diffuso l'uso della 2FA nella tua organizzazione prima di renderla obbligatoria:

* la **percentuale di adozione** complessiva e una barra di avanzamento,
* quanti dei tuoi membri hanno la 2FA abilitata (ad es. *0 di 74 membri*),
* una suddivisione per fattore — **Autenticatore**, **Email** e **Passkey**.

<figure><img src="../../../../.gitbook/assets/mfa-adoption-report.png" alt="The MFA adoption report"><figcaption><p>Il rapporto sull'adozione della MFA: percentuale complessiva, membri registrati e una suddivisione per fattore.</p></figcaption></figure>

Usalo per valutare la prontezza: aumenta prima l'adozione, poi attiva il requisito con meno membri bloccati al passaggio di registrazione.

## Cosa vedono i membri

Un membro a cui è richiesta la registrazione viene indirizzato alla configurazione 2FA al suo prossimo accesso e sceglie un metodo (app di autenticazione, codice via email o passkey). I passaggi per l'utente finale sono descritti in [Autenticazione a due fattori (2FA)](../../../../overview-and-basics/two-factor-authentication.md).

## Controlli di sicurezza correlati

Il requisito MFA a livello di organizzazione integra le protezioni integrate che si applicano sempre una volta che un utente ha attivato la 2FA: codici di accesso monouso, una protezione contro il replay TOTP, limiti di tentativi per sfida e per account (un account viene temporaneamente bloccato dopo troppi tentativi falliti) e la revoca automatica dei dispositivi attendibili quando un membro cambia la password.
