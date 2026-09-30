---
description: >-
  Da dove proviene il valore di un campo di intestazione e come viene creato:
  la spiegazione dietro il Controllo dei campi di intestazione nella schermata
  di validazione.
---

# Controllo dei campi di intestazione: da dove provengono i dati

Il pulsante **Controllo dei campi di intestazione** si trova accanto a **Salva** nella schermata di validazione. Apre il report *Da dove viene ogni valore?*: per ogni campo di intestazione mostra cosa c'era sul documento, cosa ha modificato il valore lungo il percorso, cosa mostra ora DocBits e perché.

Questa pagina spiega come viene creato un valore e cosa significa ciascuna fonte. Non servono competenze tecniche.

{% hint style="info" %}
Il Controllo dei campi di intestazione fa parte del modulo **Analytics**. Se il pulsante è disattivato, un amministratore può concederlo al vostro ruolo in **Impostazioni › Ruoli**.
{% endhint %}

## Un valore viene sempre creato in quest'ordine

| Passaggio | Cosa succede |
| --- | --- |
| **1. Leggere** | Il valore viene letto dal documento — da una regola addestrata, dall'IA o direttamente da una fattura elettronica. |
| **2. Trasformare** | Gli script e le regole di trasformazione del cliente modificano il valore letto: accorciarlo, integrarlo, adattarne il formato. |
| **3. Cercare** | Il valore viene cercato nei dati anagrafici. Se viene trovato qualcosa, il record anagrafico sostituisce il valore letto. |
| **4. Mostrare** | L'utente vede solo il risultato. Ciò che è accaduto lungo il percorso lo mostra il Controllo dei campi di intestazione. |

I passaggi 2 e 3 non vengono sempre eseguiti — ma quando lo sono, modificano il valore. È proprio da qui che provengono la maggior parte dei casi segnalati.

## Le fonti — cosa significa ciascuna

Le icone sono le stesse che il report mostra nella colonna **Azione** e nella barra dei filtri in alto.

### Regola addestrata

DocBits ricorda dove si trova un campo in questo tipo di documento, perché qualcuno lo ha una volta contrassegnato lì.

* **Esempio:** fornitore “Bornemann” — sempre nello stesso punto in alto a sinistra.
* **Se è sbagliato:** contrassegnare il punto corretto sul documento e salvare — la regola ne trae insegnamento.

### IA

Nessun modello fisso. L'IA legge il documento come una persona e decide da sola quale testo appartiene a quale campo.

* **Esempio:** data della fattura, importi, condizioni di pagamento.
* **Se è sbagliato:** correggere. Può essere attivata e disattivata in **Impostazioni › Campi di intestazione OCR**.

### Fattura elettronica

Con XRechnung o ZUGFeRD non viene riconosciuto nulla: il valore è già un campo dati nel documento e viene acquisito direttamente.

* **Esempio:** numero di fattura dal campo XML del mittente.
* **Se è sbagliato:** l'errore è del mittente. DocBits mostra esattamente da quale campo XML proviene il valore.

### Script / regola di trasformazione

Dopo la lettura interviene la logica del cliente e rimodella il valore. Il documento resta lo stesso — il valore no.

* **Esempio:** `1001 / LS 206776` diventa `1001`.
* **Se è sbagliato:** non cercarlo sul documento. Controllare **Impostazioni › Script** oppure **Regole di trasformazione**.

### Dati anagrafici

Il valore letto viene cercato nei vostri dati — ordini, fornitori. Una corrispondenza sostituisce il valore e trascina con sé altri campi.

* **Esempio:** `1001` trova l'ordine `06O051001` — e anche fornitore e acquirente provengono da lì.
* **Se è sbagliato:** controllare **Impostazioni › Configurazione Lookup**. Vi si indica se la ricerca è esatta o accetta anche corrispondenze parziali.

### Calcolato

Non letto, ma calcolato da altri campi.

* **Esempio:** data di scadenza dalla data della fattura più le condizioni di pagamento.
* **Se è sbagliato:** di solito è sbagliato uno dei campi da cui viene calcolato.

### Codice a barre

Letto da un codice a barre o da un codice QR sul documento.

* **Esempio:** il numero di fattura è codificato nel codice QR.
* **Se è sbagliato:** controllare le impostazioni dei codici a barre del tipo di documento.

## Ciò che viene frainteso più spesso

{% hint style="warning" %}
Quando un campo contiene improvvisamente un valore che sul documento non compare in quel modo, quasi mai è stata l'IA, ma il passaggio 2 o il passaggio 3. Più spesso la corrispondenza nei dati anagrafici, che accetta anche corrispondenze parziali: `1001` corrisponde a `06O051001`, e con l'ordine trovato cambia anche il fornitore.
{% endhint %}

Nel report un campo del genere è contrassegnato in rosso. La colonna **Azione** mostra il record anagrafico insieme a un chip rosso *solo corrispondenza parziale*, e la parte corrispondente del valore è evidenziata.

## Leggere il report

* **Chip di stato** in alto contano i campi arrivati invariati dal documento, modificati lungo il percorso o non presenti sul documento così come mostrati. Cliccare su un chip per mostrare solo quei campi; cliccare di nuovo per mostrarli tutti.
* **Filtro fonte:** la riga di icone mostra ogni metodo di estrazione. Cliccare su una per mostrare solo i campi che l'hanno attraversata.
* **Azione:** ogni passaggio attraversato dal valore, con l'icona della sua fonte. Il passaggio da cui proviene il valore attuale è evidenziato. Passando il cursore si vede cosa ha fatto ogni passaggio, da quale valore a quale.
* **Motivo:** lo stato del campo. L'icona (i) spiega perché il valore è quello che è. Se indica *Il campo non esisteva*, il campo non era presente sul documento.
* I valori lunghi vengono abbreviati con … — passare il cursore per vedere il valore completo.
* **Apri come pagina** mostra lo stesso report su una pagina propria, da stampare o inoltrare.
