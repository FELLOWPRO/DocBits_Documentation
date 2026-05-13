# Supplier BOD Mapping

Questa pagina documenta come DocBits ingerisce i dati anagrafici fornitori di Infor M3 tramite i BOD `SyncSupplierPartyMaster` e `SyncRemitToPartyMaster`. Entrambi i BOD popolano la stessa tabella di dati anagrafici `SUPPLIER` in DocBits.

{% file src="../../../../.gitbook/assets/Sync.SupplierPartyMaster.pdf" %}
SupplierPartyMaster — Riferimento originale della mappatura BOD (PDF)
{% endfile %}

{% file src="../../../../.gitbook/assets/Sync.RemitToPartyMaster.pdf" %}
RemitToPartyMaster — Riferimento originale della mappatura BOD (PDF)
{% endfile %}

## Principi chiave

- **CONO + SUNO è la chiave di match.** Una riga `supplier_header` in DocBits è identificata univocamente da `(customer_number = sharedCONO, supplier_number = sharedSUNO)`. Questo consente a una singola organizzazione DocBits di consolidare più aziende M3.
- **`variationID` protegge contro BOD fuori sequenza.** M3 può emettere lo stesso record anagrafico più volte in rapida successione; la `variationID` in ingresso deve essere maggiore di quella salvata affinché un aggiornamento venga accettato. Entrambi i BOD tracciano la propria `variationID` indipendentemente (`variation_id_supplier_bod`, `variation_id_remit_to_party`).
- **Nessuna sovrascrittura silenziosa.** SupplierPartyMaster e RemitToPartyMaster condividono diversi campi (nome, telefono, partita IVA, banca, stato). Ogni BOD aggiorna solo i campi che possiede e solo se la sua `variationID` avanza. All'interno del set condiviso, il BOD ricevuto più di recente (per tipo di BOD) vince.
- **La sincronizzazione multi-banca è controllata da preference.** Comportamento di default: l'ultima `FinancialParty` viene scritta in `bank_id` sull'intestazione. Con la preference `ALLOW_MULTIPLE_SUPPLIER_ACCOUNTS_SYNC` attivata, ogni voce `FinancialParty` viene persistita in `supplier_account` (IBAN, ID conto, codice valuta, indicatore di preferenza).
- **Trimming opzionale del suffisso CONO.** Alcune installazioni M3 aggiungono un suffisso di divisione al numero azienda (es. `100_01`). La preference `EXCLUDE_DIVISION_FOR_CUSTOMER_NUMBER` taglia i suffissi `_*` per mantenere coerenti le chiavi DocBits.

## Sync.SupplierPartyMaster

→ Tabella dati anagrafici DocBits: **SUPPLIER**

```python
header_mappings = {
            "sharedCONO": "//DataArea/Sync/AccountingEntityID",
            "sharedSUNO": "//SupplierPartyMaster/PartyIDs/ID",
            "variationID": "//SupplierPartyMaster/PartyIDs/ID/@variationID",
            "supplierName": "//SupplierPartyMaster/Name",
            "phone": '//Communication[ChannelCode="Phone"]/DialNumber',
            "vatNo": "//SupplierPartyMaster/PartyIDs/TaxID",
            "paymentTermId": "//SupplierPartyMaster/PaymentTermID",
            "paymentMethodCode": "//SupplierPartyMaster/PaymentMethodCode",
            "buyerPersonReferenceId": "//SupplierPartyMaster/BuyerPersonReference/IDs/ID",
            "buyerPersonReference": "//SupplierPartyMaster/BuyerPersonReference/Name",
            "supplier_category": "//SupplierPartyMaster/Classification/Codes/Code[@listID='Supplier Categories']",
            "supplier_group": "//SupplierPartyMaster/Classification/Codes/Code[@listID='Supplier Group']",
            "discount_terms_description": "//SupplierPartyMaster/UserArea/Property/NameValue[@name='eam.UDFCHAR06']",
            "status": "//SupplierPartyMaster/Status/Code",
            "bank_id": "//SupplierPartyMaster/FinancialParty[last()]/FinancialAccount/ID",
        }
```

### Riferimento campi

| Campo DocBits | Origine M3 | Descrizione |
|---|---|---|
| `sharedCONO` | Numero azienda M3 | Mappa su `customer_number` in `supplier_header`. Parte della chiave di match. |
| `sharedSUNO` | `CIDMAS.IDSUNO` | Numero fornitore M3. Parte della chiave di match. |
| `variationID` | Attributo del BOD | Salvato come `variation_id_supplier_bod`. I BOD in ingresso vengono accettati solo se la loro `variationID` supera quella salvata. Un attributo mancante è trattato come `0` (force-update). |
| `supplierName` | `CIDMAS.IDSUNM` | Nome di visualizzazione del fornitore. |
| `phone` | `CIDMAS.PHNO/PHN2/IDTFNO` | Numero di telefono dal canale di comunicazione `Phone`. |
| `vatNo` | `CIDMAS.IDVRNO` | Identificativo partita IVA. Letto da `PartyIDs/TaxID` (senza filtro `@schemeName` nel percorso di ingestion M3). |
| `paymentTermId` | `CIDVEN.IITEPY` | Identificatore termini di pagamento. |
| `paymentMethodCode` | — | Codice metodo di pagamento, quando fornito. |
| `buyerPersonReferenceId` / `buyerPersonReference` | `CIDVEN.IIBUYE` / `CSYUSR.CRRENM` | Riferimento (utente M3) e nome di visualizzazione del buyer assegnato. |
| `supplier_category` | — | Letto da `Classification/Codes/Code[@listID='Supplier Categories']`. Estensione UserArea specifica del cliente; rimane NULL su installazioni M3 standard. |
| `supplier_group` | `CIDVEN.IISUCL` | Gruppo di classificazione del fornitore. |
| `discount_terms_description` | — | Estensione UserArea specifica del cliente (`eam.UDFCHAR06`) usata dalla logica di calcolo della data di sconto di DocBits. Quando il fornitore fornisce qui un valore di giorni di sconto, DocBits lo combina con la data fattura per produrre una data di scadenza dello sconto per il team AP. |
| `status` | `CIDMAS.IDSTAT` | Stato attivo/inattivo del fornitore, preso da `SupplierPartyMaster/Status/Code`. |
| `bank_id` | `CBANAC.BCBKNO` | Conto bancario di default, preso dall'*ultima* `FinancialParty`. Attiva `ALLOW_MULTIPLE_SUPPLIER_ACCOUNTS_SYNC` per sincronizzare invece ogni `FinancialParty` nella tabella `supplier_account`. |

## Sync.RemitToPartyMaster

→ Tabella dati anagrafici DocBits: **SUPPLIER**

```python
header_mappings = {
            "sharedCONO": "//DataArea/Sync/AccountingEntityID",
            "sharedSUNO": "//RemitToPartyMaster/PartyIDs/ID",
            "variationID": "//RemitToPartyMaster/PartyIDs/ID/@variationID",
            "supplierName": "//RemitToPartyMaster/Name",
            "phone": '//Communication[ChannelCode="Phone"]/DialNumber',
            "vatNo": "//RemitToPartyMaster/PartyIDs/TaxID",
            "bank_id": "//RemitToPartyMaster/FinancialParty[last()]/FinancialAccount/ID",
            "status": "//RemitToPartyMaster/Status/Code",
        }
```

### Riferimento campi

| Campo DocBits | Origine M3 | Descrizione |
|---|---|---|
| `sharedCONO` / `sharedSUNO` | Azienda M3 / `CIDMAS.IDSUNO` | Stessa semantica di `SupplierPartyMaster`. Si unisce alla stessa riga `supplier_header`. |
| `variationID` | Attributo del BOD | Salvato come `variation_id_remit_to_party` — tracciato indipendentemente dalla `variationID` di SupplierPartyMaster. |
| `supplierName` | `CIDMAS.IDSUNM` | Nome di visualizzazione della parte remit-to. Scrive nella colonna condivisa `supplier_name`. |
| `phone` | `CIDREF.IRPHNO` | Numero di telefono dal blocco di comunicazione remit-to. |
| `vatNo` | `CIDMAS.IDCORG` | Identificativo partita IVA della parte remit-to. |
| `bank_id` | `CBANAC.BCBKNO` | Conto bancario remit-to (`FinancialParty[last()]`). Si applica la stessa preference multi-banca. |
| `status` | `CIDMAS.IDSTAT` | Stato attivo/inattivo della parte remit-to. |

## Come i due BOD interagiscono sulla tabella `SUPPLIER` condivisa

Entrambi i BOD popolano la stessa riga `supplier_header`. Per i campi che condividono (`supplierName`, `phone`, `vatNo`, `bank_id`, `status`), DocBits applica le seguenti regole:

1. Trovare la riga tramite `(customer_number = sharedCONO, supplier_number = sharedSUNO)`.
2. Confrontare la `variationID` in ingresso con la `variationID` salvata *per lo stesso tipo di BOD*.
3. Se la `variationID` in ingresso è maggiore (o `0`, force-update), aggiornare i campi posseduti da quel BOD. Altrimenti scartare il BOD.
4. La `variationID` dell'altro tipo di BOD non viene toccata; i suoi valori precedentemente salvati restano in essere.

Le righe `supplier_address` e `supplier_account` associate al fornitore vengono cancellate e reinserite all'aggiornamento, in modo che le tabelle secondarie riflettano sempre il BOD più recente.

## Domande frequenti

### Perché DocBits traccia CONO se tutti i miei fornitori vengono da una sola azienda M3?

Il routing CONO è obbligatorio perché DocBits è multi-tenant per progetto: un'organizzazione può ingerire BOD da più aziende M3. CONO fa parte della chiave di match per evitare che i fornitori di aziende diverse collidano. Con una sola azienda puoi ignorare il valore, ma la colonna chiave viene comunque riempita.

### Entrambi i BOD scrivono sulla stessa riga fornitore — l'ultimo BOD sovrascrive tutto?

No. Ogni tipo di BOD possiede solo i campi che invia, e gli aggiornamenti sono governati da una `variationID` indipendente. Un SupplierPartyMaster che cambia solo il nome del fornitore non annulla il numero di telefono che un successivo RemitToPartyMaster aveva scritto.

### `Supplier Categories` e `eam.UDFCHAR06` non vengono mai inviati dal mio M3 — cosa faccio?

Sono estensioni UserArea specifiche del cliente. Senza l'estensione, le colonne restano NULL e nessuna funzione DocBits ne dipende. Attiva la logica di data sconto solo quando il tuo M3 è configurato per emettere `eam.UDFCHAR06`.

### `vatNo` deve filtrare per `schemeName='TaxIdentificationNumber'`?

Il percorso di ingestion BOD M3 attualmente legge `PartyIDs/TaxID` senza filtro `schemeName`. Il filtro è usato nei percorsi XSLT di e-fattura (Facturae, XRechnung, KSeF), non nell'ingestion M3. Se il tuo M3 emette più elementi TaxID con diversi attributi `schemeName`, contattaci con un BOD di esempio prima di affidarti al comportamento non filtrato.

### Voglio sincronizzare tutti i conti bancari del fornitore, non solo l'ultimo. Come?

Attiva la preference `ALLOW_MULTIPLE_SUPPLIER_ACCOUNTS_SYNC`. Con il flag attivo, ogni `FinancialParty` del BOD viene persistita nella tabella `supplier_account` (IBAN, ID conto finanziario, codice valuta, indicatore di preferenza). La colonna legacy `bank_id` nell'intestazione continua a contenere l'ultima voce per retrocompatibilità.
