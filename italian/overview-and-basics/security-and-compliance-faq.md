# DocBits (FELLOWPRO AG) — Questionario sulla Sicurezza e Conformità

**Fornitore:** DocBits di FELLOWPRO AG | **Hosting:** Francoforte, Germania | **Certificazione ISO 27001** | **Data:** 2026-03-04

---

## Legenda dello Stato

| Simbolo | Significato |
|---------|---------|
| ✅ Confermato | Risposta verificata dalla documentazione ufficiale di DocBits o da fonti pubbliche |
| ✅ Parziale | Risposta parziale; dettagli aggiuntivi necessari dal team di DocBits |
| ❓ Da Confermare | Nessuna informazione pubblica disponibile — deve essere confermato direttamente con DocBits/FELLOWPRO |
| ⚠️ Necessita Chiarimento | Le informazioni pubbliche sollevano dubbi o ambiguità che richiedono chiarimento esplicito dal fornitore |

---

## 🔹 Posizione dei Dati e Residenza

### 1. Dove esattamente è ospitato l'ambiente di produzione?

**Risposta:** Ospitato su infrastruttura cloud AWS a Francoforte, Germania. Utilizza S3 per l'archiviazione e OpenSearch per l'indicizzazione dei log. DocBits è certificato ISO 27001. Tutte le connessioni sono protette tramite SSH, HTTPS e protocolli di crittografia standard del settore.

**Stato:** ✅ Confermato

**Note:** Francoforte AWS confermato (S3 + OpenSearch). Richiedere il codice della regione AWS specifica (eu-central-1) e se singola o multi-AZ.

---

### 2. Dove è ospitato l'ambiente di Ripristino di Emergenza (DR)?

**Risposta:** Il DR sfrutta una posizione di backup secondaria ad Amsterdam, Paesi Bassi (UE). Combinato con il sito primario a Francoforte, questo fornisce ridondanza geografica all'interno dell'UE.

**Stato:** ✅ Confermato

**Note:** Francoforte (primario) + Amsterdam (secondario). Entrambe le posizioni nell'UE. Richiedere i target RTO/RPO e i dettagli del processo di failover.

---

### 3. Dove sono archiviati i backup?

**Risposta:** I backup sono archiviati in due posizioni nell'UE:
- **Primaria:** Francoforte, Germania
- **Secondaria:** Amsterdam, Paesi Bassi

Calendario dei backup: Backup giornalieri, settimanali, trimestrali e annuali.

**Stato:** ✅ Confermato

**Note:** Calendario completo dei backup (giornaliero/settimanale/trimestrale/annuale) su due posizioni nell'UE. Tutti i dati rimangono all'interno dell'UE. Confermare la crittografia dei backup e la frequenza del test di ripristino.

---

### 4. Sono disponibili opzioni di partizionamento geografico (ad es., solo UK)?

**Risposta:** Due aree del data center disponibili:
- **Francoforte, Germania** — per tutti i clienti dell'UE
- **New York, USA** — solo per clienti USA

I dati dei clienti dell'UE sono ospitati esclusivamente a Francoforte. Attualmente non è disponibile un'opzione solo per il Regno Unito.

**Stato:** ✅ Confermato

**Note:** Clienti dell'UE solo Francoforte — nessuna combinazione di dati tra regioni. L'hosting solo UK non è disponibile; i clienti del Regno Unito sarebbero serviti da Francoforte. Chiarire se aree aggiuntive sono sulla roadmap.

---

### 5. I dati sono crittografati a riposo e in transito?

**Risposta:** Tutte le connessioni tra i componenti sono protette utilizzando protocolli di crittografia standard del settore (SSH, HTTPS). La certificazione ISO 27001 richiede controlli di crittografia.

**Stato:** ✅ Confermato

**Note:** Confermare gli standard di crittografia specifici (ad es., AES-256 a riposo, TLS 1.2+ in transito).

---

## 🔹 Gestione dei Modelli AI/ML

### 6. I contenuti delle fatture sono inviati a un host di modelli di terze parti (ad es., OpenAI, Azure AI)?

**Risposta:** I modelli AI NON sono inviati agli host di terze parti. DocBits utilizza modelli Mistral AI in esecuzione a Francoforte, Germania — la stessa posizione dell'ambiente di produzione. Nessun dato esce dalla regione di Francoforte per l'elaborazione AI.

**Stato:** ✅ Confermato

**Note:** Modelli Mistral ospitati a Francoforte. Nessuna chiamata API di terze parti per l'elaborazione dei documenti. Completamente autonomo.

---

### 7. I documenti estratti sono utilizzati per addestrare modelli più ampi tra i clienti?

**Risposta:** Sì — DocBits utilizza l'"intelligenza collettiva AI" che addestra i modelli di classificazione ed estrazione su tutti i clienti. Tuttavia, la tecnologia funziona come una mappa attraverso i dati — apprende le coordinate/posizioni strutturali dei campi dati nei documenti, NON il contenuto effettivo del documento. I dati grezzi dei documenti non sono condivisi tra i tenant.

**Stato:** ✅ Confermato

**Note:** L'intelligenza collettiva apprende i modelli di layout strutturale (coordinate/posizioni dei campi), non il contenuto del documento. Ciò significa che nessun dato cliente (importi delle fatture, nomi dei fornitori, ecc.) è condiviso tra i tenant — solo la conoscenza della struttura del documento.

---

### 8. Puoi limitare l'addestramento del modello al solo tuo tenant?

**Risposta:** Nessuna opzione di isolamento del modello per tenant. Tuttavia, i modelli AI condivisi apprendono solo le coordinate del layout del documento e i modelli strutturali — non il contenuto effettivo del documento o i dati commerciali. I clienti possono inoltre addestrare tipi di documenti personalizzati limitati al loro tenant.

**Stato:** ✅ Confermato

**Note:** Rischio basso: i modelli condivisi apprendono solo dati posizionali/strutturali (coordinate), non il contenuto commerciale. L'addestramento del tipo di documento personalizzato rimane limitato al tenant.

---

### 9. Dove sono ospitati ed eseguiti i modelli AI/ML?

**Risposta:** I modelli AI/ML (Mistral) sono ospitati ed eseguiti a Francoforte, Germania — la stessa regione dell'ambiente di produzione.

**Stato:** ✅ Confermato

**Note:** Positivo: l'elaborazione AI rimane all'interno di Francoforte. Nessun trasferimento di dati all'infrastruttura AI esterna.

---

### 10. Quali tecnologie AI/ML vengono utilizzate (motore OCR, LLM, NLP)?

**Risposta:** DocBits utilizza AI, OCR, machine learning per l'estrazione. Supporta 120+ lingue. Sostiene un'accuratezza del 96%+. Utilizza anche Gen AI per la funzione "AI Tags".

**Stato:** ✅ Parziale

**Note:** Richiedere dettagli specifici del modello: OCR proprietario vs. di terze parti, quale LLM alimenta le funzioni Gen AI.

---

### 11. Esiste un'opzione per il deployment del modello AI in locale?

**Risposta:** La documentazione dell'architettura di DocBits fa riferimento sia alle opzioni di deployment "DocBits Cloud customer" che "DocBits On premise".

**Stato:** ✅ Parziale

**Note:** Confermare l'ambito dell'opzione on-premise: include l'elaborazione AI completa o solo l'archiviazione dei documenti?

---

## 🔹 Accesso ai Dati e Logging

### 12. Chi (supporto del fornitore/ingegneri) può accedere ai documenti grezzi e ai dati di Infor LN?

**Risposta:** FELLOWPRO AG ha un responsabile della protezione dei dati designato (Daniel Jordan). I DPA con subappaltatori sono in vigore per il GDPR. ISO 27001 richiede controlli di accesso.

**Stato:** ✅ Parziale

**Note:** Richiedere a DocBits: elenco esatto dei ruoli del personale con accesso ai documenti grezzi. L'accesso è basato sulla necessità / su richiesta solo?

---

### 13. Quali controlli di accesso e logging esistono per il personale del fornitore?

**Risposta:** La certificazione ISO 27001 richiede controlli di accesso documentati, audit trail e misure di sicurezza. DocBits mantiene un audit trail per la conformità e la revisione.

**Stato:** ✅ Parziale

**Note:** Richiedere: dettagli RBAC, requisiti MFA, gestione dell'accesso privilegiato (PAM), e se l'accesso è registrato con audit trail immutabili.

---

### 14. Quanto tempo vengono conservati i log di accesso?

**Risposta:** I log sono archiviati su AWS S3 a Francoforte e OpenSearch. I log accessibili ai clienti sono conservati per 30 giorni. I log interni sono conservati per 3 mesi.

**Stato:** ✅ Confermato

**Note:** S3 + OpenSearch a Francoforte. Conservazione di 30 giorni per l'accesso dei clienti / 3 mesi per la conservazione interna. Confermare se i log sono immutabili/a prova di manomissione.

---

### 15. Quanto tempo vengono conservati i documenti caricati / i dati estratti in DocBits?

**Risposta:** I clienti possono configurare la conservazione dei dati nelle impostazioni. Opzioni: 30 giorni o 3 mesi. Dopo il periodo configurato, i documenti e i dati estratti vengono eliminati automaticamente dai server di DocBits.

**Stato:** ✅ Confermato

**Note:** Conservazione configurabile dal cliente (30 giorni / 3 mesi). Confermare: l'eliminazione include tutte le copie (S3, OpenSearch, dati di addestramento AI)?

---

### 16. I clienti possono richiedere l'eliminazione dei dati su richiesta?

**Risposta:** FELLOWPRO AG rispetta i diritti degli interessati del GDPR incluse le richieste di cancellazione. Il DPO elabora queste richieste secondo l'Art. 17 del GDPR.

**Stato:** ✅ Confermato

**Note:** Confermare: l'eliminazione copre tutte le copie inclusi i backup e i dati di addestramento AI derivati dal tenant?

---

### 17. Quali subappaltatori hanno accesso ai dati dei clienti?

**Risposta:** Cloudflare viene utilizzato per la protezione da bot/DDoS. I DPA sono in vigore con tutti i subappaltatori per i requisiti GDPR.

**Stato:** ✅ Parziale

**Note:** Richiedere l'elenco completo dei subappaltatori. Cloudflare confermato; chiedere informazioni sul provider di cloud hosting, fornitori di servizi AI, ecc.

---

### 18. Quali certificazioni e framework di conformità detiene DocBits?

**Risposta:** Certificato ISO 27001. Conforme al GDPR. Mantiene DPA con tutti i subappaltatori. DPO designato.

**Stato:** ✅ Confermato

**Note:** Chiedere: SOC 2 Type II? Rapporti di penetration test? ISO 27701 (privacy)? Calendario del controllo annuale?

---

## 🔹 Ambito dell'Integrazione (Infor LN)

### 19. Qual è l'elenco esatto dei campi dati estratti da LN master per la convalida?

**Risposta:** Dati master importati tramite Infor BOD:
- **Fornitori:** Sync.SupplierPartyMaster, Sync.RemitToPartyMaster
- **Ordini di Acquisto:** Sync.PurchaseOrder
- **Piano dei Conti:** Sync.CodeDefinition (ChartOfAccounts)
- **Dimensioni Flex:** Sync.CodeDefinition (FlexDimensions)
- **Codici Fiscali:** tramite BOD publish

**Stato:** ✅ Confermato

**Note:** Richiedere a DocBits l'elenco completo dei BOD e la documentazione del mapping a livello di campo per la configurazione LN specifica.

---

### 20. Quali campi di intestazione specifici vengono esportati di nuovo in LN?

**Risposta:** I campi di esportazione dell'intestazione includono: SupplierCode, PurchaseType, InvoiceType, InvoiceNumberSupplier, InvoiceDate, InvoiceAmount, InvoiceCurrency, RateDeterminer, RateDate, TaxCountry, TransactionEntryDate, Reference, IDMReference, TaxBaseAmount, InvoiceDocumentType e altri.

**Stato:** ✅ Confermato

**Note:** Esaminare il file di mapping dei campi per l'ambiente specifico. Confermare che tutti i campi statici corrispondono alla configurazione LN della tua azienda.

---

### 21. Le operazioni di write-back sono limitate solo agli oggetti dell'interfaccia AP/PO?

**Risposta:** L'esportazione utilizza il BOD Sync.CaptureDocument che viene trasformato in BOD target (ad es., BOD fattura AP) in ION Desk. I dati vengono anche esportati a Infor IDM per l'archiviazione dei documenti.

**Stato:** ✅ Parziale

**Note:** Confermare: DocBits scrive SOLO su oggetti fattura AP e ricevuta PO? Quali altri moduli LN vengono toccati? Qual è l'ambito di scrittura di IDM?

---

### 22. Quale metodo di integrazione viene utilizzato (ION API, BOD, DB diretto)?

**Risposta:** Integrazione tramite Infor ION API, ION Desk e Infor Standard BOD. Nessun accesso diretto al database. Utilizza i file ION API e gli account di servizio per l'autenticazione.

**Stato:** ✅ Confermato

**Note:** Positivo: nessun accesso al DB diretto. Tutta la comunicazione tramite il livello di integrazione Infor standard.

---

### 23. Quale autenticazione/autorizzazione viene utilizzata per la connettività LN?

**Risposta:** Utilizza ION API Files (credenziali client OAuth2) con ION API Client ID e account di servizio creati in InforOS.

**Stato:** ✅ Confermato

**Note:** Assicurare che gli account di servizio seguano il principio del privilegio minimo. Esaminare i permessi concessi all'utente ION API di DocBits.

---

### 24. Il trasferimento dati tra DocBits e LN è crittografato end-to-end?

**Risposta:** Tutte le connessioni tra i componenti sono protette utilizzando crittografia standard del settore (SSH, HTTPS).

**Stato:** ✅ Confermato

**Note:** La comunicazione ION API utilizza HTTPS/TLS. Confermare la versione TLS minima (1.2+).

---

### 25. Quali tipi di documento sono supportati oltre alle fatture AP?

**Risposta:** Supporta fatture, bolle di consegna/bollette, quotazioni, conferme d'ordine, contratti e altri. Gestisce fatture con e senza PO.

**Stato:** ✅ Confermato

**Note:** Chiarire quali tipi di documento vengono scritti di nuovo in LN rispetto a quelli archiviati solo in IDM.
