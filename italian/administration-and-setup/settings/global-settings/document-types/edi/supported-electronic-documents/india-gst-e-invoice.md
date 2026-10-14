---
description: Supporto per la fattura elettronica GST indiana in DocBits
---

# 🇮🇳 India GST E-Invoice

| Proprietà | Valore |
|----------|-------|
| **Paese / Regione** | India |
| **Tipi di documento** | Fattura (INV), Nota di credito (CRN), Nota di debito (DBN) |
| **Formato** | XML (`<SignedInvoice>`) |
| **Standard** | GST E-Invoice (GSTN Invoice Registration Portal) |
| **Locale** | `en_IN` |

La fattura elettronica GST indiana è lo standard obbligatorio di fatturazione elettronica nell'ambito del regime GST (Goods and Services Tax) indiano, gestito dal GSTN (GST Network). Le aziende che superano la soglia di fatturato prescritta devono generare e-fatture tramite il portale IRP (Invoice Registration Portal), che firma la fattura e restituisce un **IRN** (Invoice Reference Number — un hash SHA-256 di 64 caratteri) e un codice QR.

DocBits rileva i documenti GST E-Invoice dalla presenza di `<SignedInvoice>` come elemento radice. Il formato include tre componenti fiscali GST:

| Componente fiscale | Descrizione |
|--------------|-------------|
| IGST | GST integrata — applicata alle transazioni inter-statali |
| CGST | GST centrale — applicata alle transazioni intra-statali (componente centrale) |
| SGST | GST statale — applicata alle transazioni intra-statali (componente statale) |

L'identificatore del contribuente è il **GSTIN** (Goods and Services Tax Identification Number), un codice alfanumerico di 15 caratteri nel formato `29AABCU9603R1ZM` (codice stato a 2 cifre + PAN a 10 cifre + numero entità + cifra di controllo). Le date utilizzano il formato `GG/MM/AAAA`.

## Stato supporto

| Componente | Stato |
|-----------|--------|
| Anteprima | ✅ Supportato |
| Estrazione campi | ✅ Supportato |
| Trasformazione | ✅ Supportato |

## Anteprima predefinita

<figure><img src="india-gst-e-invoice-preview.png" alt="India GST E-Invoice preview in DocBits"><figcaption><p>Anteprima predefinita DocBits per una fattura elettronica GST indiana</p></figcaption></figure>

## Mappatura campi

### Campi intestazione

| Campo DocBits | Elemento XML sorgente | Note |
|---|---|---|
| `invoice_id` | `Invoice/DocDtls/No` | Numero fattura |
| `invoice_date` | `Invoice/DocDtls/Dt` | Data di emissione (`GG/MM/AAAA`) |
| `invoice_type` | `Invoice/DocDtls/Typ` | INV=Fattura, CRN=Nota di credito, DBN=Nota di debito |
| `currency` | Fisso: `INR` | Sempre in rupia indiana |
| `net_amount` | `Invoice/ValDtls/AssVal` | Valore imponibile / tassabile |
| `tax_amount` | `Invoice/ValDtls/IgstVal` + `CgstVal` + `SgstVal` | Importo totale GST |
| `total_amount` | `Invoice/ValDtls/TotInvVal` | Valore totale fattura incl. GST |
| `igst_amount` | `Invoice/ValDtls/IgstVal` | Importo GST integrata |
| `cgst_amount` | `Invoice/ValDtls/CgstVal` | Importo GST centrale |
| `sgst_amount` | `Invoice/ValDtls/SgstVal` | Importo GST statale |
| `cess_amount` | `Invoice/ValDtls/CesVal` | Importo cess (se applicabile) |
| `supplier_name` | `Invoice/SellerDtls/LglNm` | Nome legale del venditore |
| `supplier_id` | `Invoice/SellerDtls/Gstin` | GSTIN venditore (15 caratteri, es. `29AABCU9603R1ZM`) |
| `supplier_trade_name` | `Invoice/SellerDtls/TrdNm` | Nome commerciale del venditore |
| `supplier_address` | `Invoice/SellerDtls/Addr1` | Indirizzo venditore riga 1 |
| `supplier_city` | `Invoice/SellerDtls/Loc` | Città / localizzazione venditore |
| `supplier_postal_code` | `Invoice/SellerDtls/Pin` | Codice PIN venditore |
| `supplier_state_code` | `Invoice/SellerDtls/Stcd` | Codice stato venditore (2 cifre) |
| `buyer_name` | `Invoice/BuyerDtls/LglNm` | Nome legale dell'acquirente |
| `buyer_id` | `Invoice/BuyerDtls/Gstin` | GSTIN acquirente |
| `buyer_trade_name` | `Invoice/BuyerDtls/TrdNm` | Nome commerciale dell'acquirente |
| `buyer_address` | `Invoice/BuyerDtls/Addr1` | Indirizzo acquirente riga 1 |
| `buyer_city` | `Invoice/BuyerDtls/Loc` | Città / localizzazione acquirente |
| `buyer_postal_code` | `Invoice/BuyerDtls/Pin` | Codice PIN acquirente |
| `buyer_state_code` | `Invoice/BuyerDtls/Stcd` | Codice stato acquirente |
| `irn` | `Irn` | Numero di riferimento fattura (hash SHA-256 di 64 caratteri) |
| `ack_number` | `AckNo` | Numero di ricevuta IRP |
| `ack_date` | `AckDt` | Data di ricevuta IRP |

### Tabella righe (`INVOICE_TABLE`)

Percorso riga: `Invoice/ItemList/Item`

| Colonna | Elemento XML sorgente | Note |
|---|---|---|
| `POSITION` | `SlNo` | Numero sequenziale riga |
| `DESCRIPTION` | `PrdDesc` | Descrizione prodotto / servizio |
| `QUANTITY` | `Qty` | Quantità fatturata |
| `UNIT` | `Unit` | Unità di misura (es. `OTH`, `NOS`, `KGS`) |
| `UNIT_PRICE` | `UnitPrice` | Prezzo unitario |
| `VAT_RATE` | `GstRt` | Aliquota GST in % (es. 18%) |
| `VAT` | `IgstAmt` (o `CgstAmt` + `SgstAmt`) | Importo GST per riga |
| `NET_AMOUNT` | `AssAmt` | Importo imponibile per riga |

## Regola di classificazione

DocBits rileva i documenti India GST E-Invoice confrontando l'elemento radice:

| Tipo di documento elettronico | Pattern |
|--------------------------|---------|
| INDIA GST E-INVOICE | L'elemento radice contiene `<SignedInvoice` |

## Correlati

- [Standard di fatturazione elettronica attualmente supportati](../../currently-supported-e-invoice-standards/)
- [Documenti elettronici supportati](./)
