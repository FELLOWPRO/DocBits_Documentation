---
description: Supporto per i documenti elettronici CHILE DTE in DocBits
---

# 🇨🇱 CHILE DTE

| Proprietà | Valore |
|----------|-------|
| **Paese / Regione** | Cile |
| **Tipi di documento** | Fattura, Nota di credito, Nota di addebito, Bolla di consegna |
| **Formato** | XML |
| **Standard** | DTE (Documento Tributario Electrónico), SII |
| **Locale** | `es_CL` |

DTE (Documento Tributario Electrónico) è lo standard cileno per i documenti fiscali elettronici regolato dal Servicio de Impuestos Internos (SII). Tutti i documenti DTE condividono il namespace `http://www.sii.cl/SiiDte`. DocBits rileva automaticamente il codice tipo DTE (`TipoDTE`) e instrada verso le regole di estrazione appropriate:

| Codice tipo | Tipo di documento |
|-----------|--------------|
| 33 | Factura Electrónica (Fattura) |
| 34 | Factura No Afecta o Exenta (Fattura esente) |
| 52 | Guía de Despacho (Bolla di consegna) |
| 56 | Nota de Débito (Nota di addebito) |
| 61 | Nota de Crédito (Nota di credito) |

## Stato del supporto

| Componente | Stato |
|-----------|--------|
| Anteprima | ✅ Supportato |
| Estrazione campi | ✅ Supportato |
| Trasformazione | ✅ Supportato |

## Anteprima predefinita

<figure><img src="chile-dte-preview.png" alt="Anteprima fattura Chile DTE in DocBits"><figcaption><p>Anteprima predefinita DocBits per una CHILE DTE FACTURA (tipo 33)</p></figcaption></figure>

## Mappatura dei campi

### Campi di intestazione

| Campo DocBits | Elemento XML sorgente | Note |
|---|---|---|
| `invoice_id` | `Folio` | Numero di folio del documento |
| `invoice_date` | `FchEmis` | Data di emissione ISO 8601 |
| `due_date` | `FchVenc` | Data di scadenza |
| `currency` | Fisso: `CLP` | Sempre peso cileno |
| `total_amount` | `MntTotal` | Importo totale IVA inclusa |
| `net_amount` | `MntNeto` | Importo netto imponibile |
| `tax_amount` | `IVA` | Importo IVA (aliquota standard 19%) |
| `supplier_name` | `RznSoc` (Emisor) | Nome dell'azienda emittente |
| `supplier_id` | `RUTEmisor` | RUT dell'emittente (es. `76123456-7`) |
| `supplier_address` | `DirOrigen` | Indirizzo dell'emittente |
| `supplier_city` | `CiudadOrigen` | Città dell'emittente |
| `supplier_country` | Fisso: `CL` | Sempre Cile |
| `buyer_name` | `RznSocRecep` | Nome dell'azienda destinataria |
| `buyer_id` | `RUTRecep` | RUT del destinatario |
| `buyer_address` | `DirRecep` | Indirizzo del destinatario |
| `buyer_city` | `CiudadRecep` | Città del destinatario |
| `buyer_country` | Fisso: `CL` | Sempre Cile |

### Tabella delle righe (`INVOICE_TABLE`)

Percorso della riga: `Detalle`

| Colonna | Elemento XML sorgente | Note |
|---|---|---|
| `POSITION` | `NroLinDet` | Numero di riga |
| `DESCRIPTION` | `NmbItem` | Descrizione dell'articolo |
| `QUANTITY` | `QtyItem` | Quantità |
| `UNIT` | `UnmdItem` | Unità di misura |
| `UNIT_PRICE` | `PrcItem` | Prezzo unitario netto |
| `VAT_RATE` | `TasaIVA` (dall'intestazione) | Aliquota IVA in % (tipicamente 19%) |
| `VAT` | Calcolato | IVA per riga |
| `NET_AMOUNT` | `MontoItem` | Totale della riga |

## Regole di classificazione

DocBits rileva i documenti Chile DTE confrontando il namespace XML e `TipoDTE`:

| Tipo di documento elettronico | Modello |
|--------------------------|---------|
| CHILE DTE FACTURA | `http://www.sii.cl/SiiDte` + `<TipoDTE>33</TipoDTE>` |
| CHILE DTE FACTURA ELECTRONICA | `http://www.sii.cl/SiiDte` + `<TipoDTE>34</TipoDTE>` |
| CHILE DTE GUIA DESPACHO | `http://www.sii.cl/SiiDte` + `<TipoDTE>52</TipoDTE>` |
| CHILE DTE NOTA CREDITO | `http://www.sii.cl/SiiDte` + `<TipoDTE>61</TipoDTE>` |

L'elemento involucro è `<EnvioDTE>` e ogni DTE è racchiuso in `<DTE><Documento>`.

## Vedi anche

- [Standard di e-fatturazione attualmente supportati](../../currently-supported-e-invoice-standards/)
- [Documenti elettronici supportati](./)
