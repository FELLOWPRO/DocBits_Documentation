# Appearance

**Appearance** consente a un amministratore di dare alla copia di DocBits dell'organizzazione un aspetto proprio: colori, raggio degli angoli, densità e carattere. Tutti i membri dell'organizzazione vedono il risultato — in modalità chiara e scura — dopo il successivo ricaricamento. Non cambia mai il layout né ciò che fa una funzione, solo come viene disegnata.

> **Accesso:** Appearance è una pagina riservata agli amministratori. Apri **Settings → Organization & Access → Appearance**.

<!-- screenshot: /settings/appearance light -->

## Chi può modificarlo

Solo gli amministratori dell'organizzazione possono aprire **Settings → Appearance** e salvare o reimpostare un tema. Tutti gli altri membri dell'organizzazione vedono solo il risultato.

## Cosa c'è nella pagina

La pagina è divisa in un editor a sinistra e un'anteprima dal vivo a destra.

| Area | Cosa contiene |
|---|---|
| **General** | Il nome del tema, il carattere, il raggio degli angoli e la densità. |
| **Colors** | Le schede Light e Dark, un selettore di colore più un campo esadecimale per ogni colore, raggruppati in Surfaces, Brand, Neutrals, Status e Charts. Un pannello «Derived colours» in sola lettura sotto mostra i colori che DocBits calcola per te (stati hover, anelli di focus e simili) a partire dai colori sopra. |
| **Advanced overrides** | Una riga `--token: value` per voce, per il caso raro in cui i controlli di colore, raggio, densità e carattere qui sopra non bastino — vedi [Advanced overrides](#advanced-overrides). |

### Modificare i colori

Ogni colore ha un campione (cliccalo per aprire il selettore di colore del browser) e accanto un campo esadecimale in cui puoi digitare o incollare. Lascia un colore vuoto per mantenere il valore predefinito di DocBits per quel token — il campione mostra allora un bordo tratteggiato. Passa tra le schede **Light** / **Dark** sopra l'elenco dei colori per impostare l'altra modalità; un colore che non imposti in modalità scura mantiene il proprio valore predefinito DocBits per lo scuro e non copia il valore chiaro.

{% hint style="info" %}
I colori si inseriscono in esadecimale (`#2388ae` oppure `#2388aeaa` con alfa). Non esiste un input per nomi di colore o `rgb()`.
{% endhint %}

### Raggio degli angoli, densità e carattere

* **Corner radius** — `None`, `Small`, `Medium` (predefinito), `Large` o `Extra large`. Controlla quanto sono arrotondati schede, pulsanti, campi di input e finestre di dialogo, in tutta l'app.
* **Density** — `Compact`, `Comfortable` (predefinito) o `Spacious`. Controlla l'altezza di pulsanti, campi di input e righe di tabella e la dimensione di testo di base.
* **Font** — un breve elenco di caratteri inclusi (Geist è quello predefinito di DocBits; anche Inter, Roboto, IBM Plex Sans, Source Sans 3, Nunito Sans, Manrope, Kanit o il carattere di sistema del visitatore). Ogni carattere è già incluso, non c'è nulla da caricare.

### Advanced overrides

Per un design token che i controlli qui sopra non espongono direttamente (ad esempio un'altezza specifica di una riga di tabella), aggiungi una riga sotto **Advanced overrides**:

```
--table-row-h: 30px
```

Un override per riga, `--token: value`. Una riga non valida — un token sconosciuto, un token che non può essere personalizzato o un valore che non corrisponde a ciò che il token si aspetta — viene elencata come errore sotto il riquadro e non viene applicata; tutto il resto della pagina viene comunque salvato normalmente.

## Anteprima

Ogni modifica aggiorna subito il pannello **Preview** a destra, senza influire su ciò che vedono gli altri — non tocca mai l'app in uso né il tema salvato. L'anteprima ha schede proprie: una panoramica con chiaro e scuro affiancati, poi pagine dedicate a pulsanti, campi di form, superfici e indicatori di stato, così puoi controllare contrasto e leggibilità nelle parti dell'interfaccia più sensibili al colore.

<!-- screenshot: /settings/appearance dark -->

Se una modifica rende il tema non valido (vedi sotto), l'anteprima continua a mostrare l'ultima versione valida invece di rompersi.

## Salvare e reimpostare

* **Save** scrive il tema per tutta l'organizzazione. È disattivato finché qualcosa non è realmente cambiato e il tema non è valido.
* **Reset** chiede conferma, poi rimuove completamente il tema dell'organizzazione e riporta tutti al tema predefinito di DocBits. Non è possibile annullarlo dalla pagina — i colori vanno reinseriti a mano (o reimportati, vedi sotto) se l'organizzazione li vuole di nuovo.
* Un salvataggio o una reimpostazione che fallisce (per esempio per un problema di validazione) elenca il problema sopra l'editor e lascia la pagina com'era; non viene applicato nulla.

Non ci sono controlli di contrasto prima del salvataggio — vedi [Suggerimenti](#suggerimenti) sotto.

## Esportare e importare

* **Export** scarica il tema attualmente mostrato nell'editor (salvato o no) come file `.json`, con il nome del tema.
* **Import** legge un file di tema `.json` e lo carica nell'editor. Deve comunque essere rivisto e salvato per avere effetto — il solo import non cambia ciò che vede qualcuno. Un file non valido o troppo grande (oltre 32 KB) viene rifiutato con un errore e nulla cambia.

L'export è un modo comodo per salvare un tema prima di sperimentare, o per copiare l'aspetto di un'organizzazione in un'altra.

## Cosa vedono gli utenti

Una volta salvato, il tema si applica all'intera applicazione — ogni pagina, in modalità chiara e scura — per ogni membro dell'organizzazione, dopo il successivo ricaricamento (non subito per le altre sessioni aperte). Un utente che non ha mai caricato l'organizzazione vede il valore predefinito di DocBits finché le impostazioni dell'organizzazione non sono state caricate una volta; poi il tema prende il sopravvento.

La reimpostazione riporta tutti all'aspetto predefinito di DocBits al successivo ricaricamento, esattamente come se non fosse mai stato impostato un tema dell'organizzazione.

## Suggerimenti

* **Controlla il contrasto in entrambe le modalità.** L'editor non avvisa delle combinazioni a basso contrasto (per esempio un colore di brand chiaro con testo chiaro). Usa i pannelli chiaro e scuro dell'anteprima per verificare che il testo resti leggibile prima di salvare.
* **Non toccare i colori di stato se non hai un motivo per cambiarli.** Destructive (errori), success, warning e info mantengono il loro significato in tutta l'app — cambiarli può far sembrare un errore un successo a prima vista. Cambia il colore di brand e lascia i colori di stato ai valori predefiniti, a meno che l'organizzazione non abbia bisogno di più del consueto rosso/verde/ambra/blu.
* **Parti da una palette completa.** Esportare il tema attuale o partire dal valore predefinito di DocBits dà a ogni colore di base un valore da cui modificare, invece di indovinare quali token esistono.
* **Un cambio di tema riguarda ogni utente dell'organizzazione al successivo ricaricamento.** Non esiste un passaggio di anteprima riservato a un sottoinsieme di utenti; prova tu stesso il risultato in chiaro e scuro prima di dire al team che è pronto.
