# Panoramica di XRechnung

## Introduzione

XRechnung è uno standard tedesco per la fatturazione elettronica progettato per la pubblica amministrazione. Si basa sullo standard europeo EN 16931 ed esiste in due formati tecnici: **UBL** (Universal Business Language) e **CII** (Cross Industry Invoice).

DocBits fornisce il pieno supporto per XRechnung, consentendo l'estrazione di dati strutturati e l'esportazione senza soluzione di continuità verso i sistemi ERP Infor.

## Versioni XRechnung supportate (CII)

DocBits supporta le seguenti versioni XRechnung CII:

* [XRechnung 1.2](versions/xrechnung-1-2.md)
* [XRechnung 2.1](versions/xrechnung-2-1.md)
* [XRechnung 3.0](versions/xrechnung-3-0.md)
* [XRechnung 3.0.1](versions/xrechnung-3-0-1.md)
* [XRechnung 3.0.2](versions/xrechnung-3-0-2.md)

## Flusso di dati

Il flusso di dati da un documento XRechnung al sistema ERP segue questi passaggi:

1. **Estrazione**: DocBits analizza i dati XML in base alla versione e al formato XRechnung (CII o UBL).
2. **DocBits Mappatura campi**: i dati estratti vengono mappati sui campi DocBits standard.
3. **Allineamento con l’ERP**: i campi DocBits sono mappati sui campi Infor BOD (documento oggetto business), in genere utilizzando i campi `SyncSupplierInvoice` BOD.
4. **Export**: i dati mappati vengono esportati nel sistema Infor.

## Standard di mappatura

La mappatura si basa sui seguenti standard:
* **UN/CEFACT CII**: La base per la struttura XRechnung CII XML.
* **OAGIS/OASIS**: lo standard per i BOD Infor.
* **EN 16931**: lo standard europeo per la fatturazione elettronica.

## Guide per paese

Consultate le guide per paese per le etichette esatte dei formati, la sintassi, i limiti delle versioni e lo stato di configurazione esaminato. [Formati eDocs, versioni e guide per paese](../supported-electronic-documents/README.md).
