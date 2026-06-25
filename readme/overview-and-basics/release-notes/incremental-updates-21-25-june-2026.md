# Note della versione DocBits — 21–25 giugno 2026

_Cosa ha introdotto questo aggiornamento in produzione, spiegato in modo
semplice. Per ogni servizio viene indicata la versione ora attiva in produzione.
I servizi non elencati non hanno avuto modifiche visibili ai clienti in questo
periodo._

---

## Highlights

- **Ricerca più intelligente nella dashboard.** Cerca i documenti in modo
  affidabile per importi e numeri — trova le fatture al di sopra di un valore,
  oppure cerca per **numero di richiesta d'acquisto** — con intervalli di importi
  che confrontano numeri reali, non testo. I sotto-tipi di fattura sono ricercabili
  tramite i loro nomi tradotti.
- **Notifiche e-mail affidabili.** Gli avvisi di cambio stato vengono ora inviati
  per ogni stato (niente più e-mail scartate silenziosamente), e le ricevute di
  importazione in entrata e gli avvisi di errore presentano ora il marchio DocBits
  corretto, con controlli per singolo destinatario.
- **Accesso più fluido tra le regioni (EU/US).** Il cambio di regione è ora un
  piccolo banner anziché un'interruzione a schermo intero, il single sign-on
  approda nella regione corretta e rimanere connessi su più schede del browser è
  più affidabile.
- **Correzioni ai permessi.** Gli utenti ottengono l'accesso che il loro gruppo
  concede loro — aprire, modificare, approvare e riavviare i documenti ora funziona
  correttamente anche quando i gruppi e i permessi sono configurati in modi meno
  comuni.
- **Elaborazione dei documenti più stabile.** I documenti che in precedenza
  rimanevano bloccati dopo il caricamento vengono ripresi automaticamente, e un
  picco di attività di un cliente non rallenta più gli altri.

---

## Web App — live: `10.32.4`

- **Salto con la ricerca rapida (Cmd/Ctrl + K)** direttamente all'impostazione
  **Validazione fattura elettronica**.
- **Regione e accesso:** il cambio di regione è mostrato come banner persistente
  anziché come schermata bloccante; il single sign-on reindirizza ora alla regione
  corretta (EU/US); rimanere connessi su più schede è più affidabile.
- **Permessi:** corretti i casi in cui gli utenti non potevano **approvare**,
  **modificare**, **aprire** o **riavviare** i documenti pur avendo i permessi di
  gruppo corretti.
- **Impostazioni e-mail in entrata:** nuove opzioni "Notifica al mittente" e
  "Rispondi al mittente alla ricezione".
- **Usabilità:** l'avviso di documento duplicato deve ora essere chiuso prima di
  continuare; il banner "backend non disponibile" appare solo durante
  interruzioni reali; i contatori delle attività si aggiornano immediatamente al
  completamento delle attività; correzione della modalità scura nella schermata di
  validazione delle tabelle AI.
- **Prestazioni:** corretto un blocco nella schermata dei documenti elettronici
  durante la validazione dei campi e il PO matching.
- **Ricerca dei sotto-tipi di fattura tramite i loro nomi tradotti.**

## API Service — live: `12.41.9`

- **Revisione della ricerca nella dashboard:** il numero di richiesta d'acquisto e
  il richiedente sono ora ricercabili; le ricerche per importo e per numero
  restituiscono risultati corretti (vero confronto numerico); l'importo netto
  totale e le colonne calcolate vengono visualizzati correttamente.
- **E-mail di avviso di stato affidabili** per qualsiasi stato del documento, con
  gli errori di invio non più nascosti.
- **Permessi:** gli utenti senza un gruppo possono aprire e approvare i propri
  documenti; ripristinata la visibilità dei documenti per gli utenti senza gruppo.
- **Affidabilità dell'elaborazione dei documenti:** i documenti bloccati nello
  stato "nuovo" vengono rimessi automaticamente in coda; elaborazione a quote eque
  affinché un grande picco di attività di un'organizzazione non penalizzi le altre;
  auto-riparazione per rari problemi di sequenza del database.
- **I PDF scansionati con un livello di testo danneggiato vengono indirizzati
  all'OCR** anziché produrre testo poco affidabile.
- **Precisione di estrazione e PO:** nome del fornitore compilato a partire
  dall'ordine d'acquisto collegato; rimosse le colonne con numeri di articolo
  duplicate; gestione migliorata degli spazi speciali (non separabili).
- **Esportazione Infor ERP / SAP:** corretta l'autenticazione dell'esportazione
  SFTP.
- **Fatturazione elettronica:** affinamenti del percorso di estrazione
  ZUGFeRD / documento elettronico.

## Auth Service — live: `1.66.0`

- **Corretta l'assegnazione di organizzazione mancante** per alcuni utenti (id
  organizzazione vuoto).

## Docflow Service — live: `2.3.4`

- **Il tempo di attesa (cooldown) del trigger di workflow** è ora configurabile per
  ogni ambiente.

## Email Service — live: `1.35.9`

- **E-mail con marchio:** le ricevute di importazione in entrata e gli avvisi di
  errore usano ora il logo e i colori DocBits reali.
- **Controlli per organizzazione:** e-mail di conferma alla ricezione, "notifica al
  mittente" in caso di errore e opzioni di risposta al mittente.
- **Importazione in entrata più affidabile:** i risultati dell'importazione vengono
  registrati correttamente, gli errori parziali sono segnalati come errori (non
  come successi silenziosi) e i caratteri problematici nei corpi delle e-mail non
  interrompono più l'importazione.
- **Instradamento EU/US:** instradamento per organizzazione verso l'API regionale
  corretta.

## Fulltext Service — live: `1.34.5`

- **La ricerca per importi e numeri** funziona ora in modo affidabile, inclusi i
  separatori delle migliaia e gli intervalli di importi (il motore alla base della
  revisione della ricerca nella dashboard).
- **Infrastruttura di ricerca più stabile:** le code in background orfane vengono
  ripulite in modo da non occupare più le risorse condivise.

## PO Match Service — live: `1.54.7`

- **Abbinamento degli ordini d'acquisto più robusto:** i codici testuali di
  imballaggio/unità di confezionamento non bloccano più un abbinamento, e
  l'abbinamento manuale delle righe gestisce in modo sicuro i risultati vuoti.

---

## Nessuna modifica visibile ai clienti in questo periodo

Stabili, senza modifiche di prodotto rilevanti tra il 21 e il 25 giugno: Auto
Accounting (`1.18.5`), Barcode (`1.15.6`), Docnet (`1.54.6`), Extraction
(`1.48.6`), FTP (`1.30.0`), OCR (`1.6.8`), Operator (`1.39.5`).

<!-- Generated by the docbits-changelog skill (prod-delta mode). Versions read live
     from prod (do-fra1-polydocs/prod); window 2026-06-21 → 2026-06-25. -->
