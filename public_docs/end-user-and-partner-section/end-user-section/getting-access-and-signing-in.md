# Ottenere l'accesso e accedere

Questa pagina spiega come ottenere un account DocBits e come accedere:

* [Accedi con un account esistente](#accedi-con-un-account-esistente) — i campi della schermata di accesso e il selettore della regione.
* [Registrazione](#registrazione) — crea il tuo account DocBits.
* [Password dimenticata](#password-dimenticata) — reimposta la tua password con un link di reimpostazione.
* [Prima password per gli account creati dall'amministratore](#prima-password-per-gli-account-creati-dallamministratore) — imposta la prima password di un account che il tuo amministratore ha creato per te.

L'Autenticazione a Due Fattori, le passkey e il secondo passaggio di accesso sono trattati in [Autenticazione a Due Fattori (2FA)](../../security/two-factor-authentication.md). Usa il menu della lingua in alto a destra di questi moduli se ti serve un'altra lingua di visualizzazione.

## Accedi con un account esistente

Apri l'indirizzo web DocBits fornito alla tua organizzazione — per esempio `https://app.docbits.com` — e accedi nella schermata di accesso.

<figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/getting-access-login-en-20261107.png" alt="Schermata di accesso DocBits in inglese con i campi E-Mail e Password vuoti, Remember me, il selettore Auth region impostato su Europe, Log In, Sign in with a passkey, Sign in with Google e Sign in with Microsoft"><figcaption><p>La schermata di accesso: email e password, Remember me, il selettore Auth region, Log In, la passkey e i pulsanti di accesso Google e Microsoft.</p></figcaption></figure>

1. **E-Mail** — l'indirizzo con cui è stato creato il tuo account DocBits.
2. **Password** — la tua password DocBits. L'icona a forma di occhio nel campo mostra o nasconde quanto hai digitato.
3. **Remember me** — compila il tuo indirizzo email la prossima volta che apri la schermata di accesso.
4. **Auth region** — DocBits funziona in due regioni, **Europe** e **United States**, e ciascuna ha il proprio servizio di accesso. Il selettore è mostrato nelle installazioni che usano entrambe (production, dev e sandbox). DocBits preseleziona la tua ultima scelta, altrimenti la regione corrispondente al fuso orario del tuo computer, altrimenti Europe. Se il tuo account è stato creato nell'altra regione, selezionala qui prima di fare clic su **Log In**.
5. Fai clic su **Log In**.

Sotto i campi della password:

* **Sign in with a passkey** — compare quando il browser supporta le passkey. Ti consente di accedere senza password. Vedi [Accesso senza password](../../security/two-factor-authentication.md).
* **Sign in with Google** e **Sign in with Microsoft** — per le organizzazioni che usano il single sign-on con questi provider. Il provider di identità gestisce l'accesso, quindi la password DocBits e il requisito a due fattori di DocBits non si applicano.
* **Forgot password?** — vedi [Password dimenticata](#password-dimenticata) più sotto.
* **Register** — vedi [Registrazione](#registrazione) più sotto.

{% hint style="info" %}
Scegli la **Auth region** usata dalla tua organizzazione prima di fare clic su **Log In**: la scelta decide quale servizio di accesso della regione riceve le tue credenziali. Se non sei sicuro, chiedi al tuo amministratore.
{% endhint %}

## Registrazione

Puoi creare tu stesso un account DocBits nella pagina di registrazione. Aprila dal link **Registro** nella schermata di accesso, oppure vai a `https://app.docbits.com/register` (usa l'indirizzo web che è stato comunicato alla tua organizzazione).

<figure><img src="../../.gitbook/assets/dbdc-8-register-native-it-20261101.png" alt="Modulo italiano di registrazione DocBits con cinque campi vuoti, reCAPTCHA non selezionato, termini, Iniziare, Google, Microsoft e Accesso"><figcaption><p>Registrazione: compila Nome, Cognome, Posta elettronica, Password e Confermare la password. Risolvi reCAPTCHA se compare, accetta i Termini e Condizioni e seleziona Iniziare. Accesso torna alla schermata di accesso.</p></figcaption></figure>

Compila il modulo:

1. **Nome** e **Cognome** — il tuo nome così come deve apparire in DocBits.
2. **Posta elettronica** — il tuo indirizzo email di lavoro. È il tuo identificativo di accesso.
3. **Password** e **Confermare la password** — vedi le regole per la password più sotto. Una lista di controllo sotto il campo della password mostra quali regole la tua password soddisfa già.
4. Se la pagina mostra un widget **reCAPTCHA**, completalo. Il widget appare solo quando il tuo deployment DocBits ha la protezione dai bot attivata.
5. Spunta la casella per confermare che accetti i **Termini e Condizioni**.
6. Fai clic su **Iniziare**. Se hai già un account, fai clic su **Accesso** in fondo per tornare alla schermata di accesso. **Visita il sito web** apre il sito web di DocBits per le informazioni sul prodotto.

Usa l'icona a forma di occhio accanto a un campo della password per mostrare o nascondere i caratteri che hai inserito.

### Regole per la password

La tua password deve:

* essere lunga tra **8 e 20 caratteri**,
* contenere almeno una lettera **maiuscola** e una **minuscola**,
* contenere almeno una **cifra**,
* contenere almeno un **carattere speciale** (`!@#$%^&*()_+=\[{]\};:,.<>?/\|~-`).

Sono ammessi solo lettere, cifre e questi caratteri speciali.

### Iscriviti con Google o Microsoft

Invece di una password, puoi fare clic sul pulsante **Google** o **Microsoft** sotto **OPPURE ISCRIVETEVI CON**. DocBits crea il tuo account tramite il tuo provider di identità, e in seguito accedi allo stesso modo.

### Conferma il tuo indirizzo email

Dopo aver inviato il modulo, DocBits mostra una pagina di conferma e invia una **email di verifica** all'indirizzo che hai inserito. Apri l'email e fai clic sul link al suo interno — ti porta a una pagina di conferma che verifica il tuo indirizzo. Se l'email non arriva, la pagina di conferma offre un'opzione di **reinvio**. Una volta verificato l'indirizzo, fai clic su **Accesso** ed effettua l'accesso con la tua email e la tua password.

## Password dimenticata

DocBits memorizza le password come hash unidirezionali con salt. Una password esistente non può essere recuperata dal suo hash, quindi questa procedura ne imposta una nuova. Vedere [Archiviazione sicura delle credenziali](../../security/secure-storage-of-credentials.md).

Se hai dimenticato la tua password:

1. Nella schermata di accesso, fai clic su **Ha dimenticato la password?**.
2. Nella pagina **Password dimenticata**, inserisci il tuo indirizzo di **Posta elettronica** e fai clic su **Reimpostare la password**. Se viene mostrato un widget reCAPTCHA, completalo prima.

   <figure><img src="../../.gitbook/assets/dbdc-8-forget-password-native-it-20261101.png" alt="Modulo italiano Password dimenticata con Posta elettronica vuota, reCAPTCHA non selezionato, Reimpostare la password e Torna al login"><figcaption><p>Inserisci la Posta elettronica e seleziona Reimpostare la password per richiedere un link, oppure usa Torna al login. Risolvi reCAPTCHA quando compare.</p></figcaption></figure>

   Se non vuoi reimpostare la tua password, fai clic su **Torna al login** per tornare all'accesso.

3. DocBits ti invia per email un **link di reimpostazione della password**. Apri l'email e fai clic sul link — si apre la pagina di reimpostazione.
4. Inserisci la tua **nuova password due volte**. Si applicano le stesse regole per la password della [registrazione](#regole-per-la-password), e una lista di controllo mostra quali regole sono soddisfatte.
5. Fai clic su **Reimpostare la password**. DocBits conferma la modifica e ti riporta alla schermata di accesso, dove puoi accedere con la nuova password.

{% hint style="info" %}
I link di reimpostazione scadono dopo poco tempo. Se il link non funziona più, ripeti i passaggi precedenti per richiederne uno nuovo.
{% endhint %}

## Prima password per gli account creati dall'amministratore

Quando il tuo amministratore ti aggiunge come utente (vedi [Utenti](../../administration-and-setup/settings/global-settings/groups-users-and-permissions/users/README.md)), ricevi un'email con i tuoi dati di accesso e un link per impostare la tua **prima password**. Il link apre la pagina **Imposta password**:

<figure><img src="../../.gitbook/assets/dbdc-8-set-password-native-it-20261101.png" alt="Modulo italiano Imposta password con il messaggio di benvenuto, Password e Confermare la password vuoti, icone a forma di occhio, Imposta password e Vai al login"><figcaption><p>Prima password per un account creato dall’amministratore: compila Password e Confermare la password e seleziona Imposta password. Vai al login torna alla schermata di accesso.</p></figcaption></figure>

1. Fai clic sul link nell'email di invito. La pagina ti accoglie con "Benvenuti su DocBits! Il tuo account è stato creato. Imposta la tua password per iniziare."
2. Inserisci la tua password due volte — si applicano le stesse [regole per la password](#regole-per-la-password).
3. Fai clic su **Imposta password**. Puoi quindi accedere con la tua email e questa password.

Le icone a forma di occhio mostrano o nascondono ciò che hai inserito. Se esci prima di impostare una password, **Vai al login** riporta alla schermata di accesso.

Il link è legato al tuo account e funziona una sola volta. Se scade prima che tu lo usi, chiedi al tuo amministratore di inviare nuovamente l'invito oppure usa **Ha dimenticato la password?** con il tuo indirizzo email.
