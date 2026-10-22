---
description: "Individuate la famiglia eDocs configurata, la sintassi, la versione e il profilo prima di testare l’elaborazione dei documenti."
---

# Formati eDocs, versioni e guide per paese

Partite dal documento sorgente e dalla guida del paese corrispondente. Il solo nome di un paese non identifica un formato di file. Un’etichetta di versione, una sintassi XML e un profilo aziendale descrivono elementi diversi.

{% hint style="info" %}
Le tabelle riportano una verifica del catalogo di sviluppo effettuata il 17 ottobre 2026 e del relativo codice di elaborazione. Descrivono le regole e i componenti di configurazione disponibili, senza certificare ogni file, requisito legale o distribuzione in produzione. L’organizzazione può sostituire le impostazioni predefinite.
{% endhint %}

## Leggere correttamente la matrice di supporto

- Famiglia: il formato del documento elettronico, per esempio XRechnung, Factur-X, KSeF o CFDI.
- Sintassi: il contenuto effettivo, per esempio XML UBL, XML CII o un PDF con XML incorporato. Un PDF acquisito tramite scansione, un’esportazione JSON o un’immagine QR non costituiscono un contenuto XML equivalente.
- Versione: la pubblicazione o la versione dello schema dichiarata. Un’etichetta generica di famiglia non dimostra il supporto per ogni versione.
- Profilo: un sottoinsieme aziendale o di dati, per esempio BASIC, EN16931, EXTENDED o la fatturazione da parte del cliente. Un profilo non è una versione di pubblicazione.
- Regola e componenti: classificazione, Transformation, Preview ed Extraction Paths sono distinti. Un profilo configurato non ha necessariamente una propria regola di classificazione.
- Validazione e trasmissione: il rendering o l’estrazione di un file non verifica, di per sé, tutte le regole legali, le firme, l’autorizzazione fiscale o la consegna tramite rete.

## Guide per paese

La panoramica rimanda a 39 guide nazionali e a una guida internazionale. Ogni guida elenca le etichette esatte dei formati e i componenti di configurazione, insieme alle schermate DocBits, ai video e alle verifiche di accettazione disponibili.

| Paese / regione | Famiglie e ambito delle versioni | Risultato del catalogo |
| --- | --- | --- |
| [Austria](countries/austria.md) | ebInterface 4.3, 5.0, 6.0 e 6.1 hanno voci separate. | Voci trovate |
| [Danimarca](countries/denmark.md) | OIOUBL 2.1 è la voce danese indicata. | Voci trovate |
| [Finlandia](countries/finland.md) | Finvoice 1.3, 2.0, 2.01 e 3.0 hanno voci separate. TEAPPSXML è un’altra famiglia. | Voci trovate |
| [Francia](countries/france.md) | Factur-X ha voci generiche e specifiche per pubblicazione, tra cui 1.0.05, 1.08 e 1.09. VRBL FR CIUS 1.0 è distinto. | Voci trovate |
| [Germania](countries/germany.md) | XRechnung ha tredici etichette di versione da 1.0 a 3.0.2, ciascuna in CII e UBL. ZUGFeRD comprende profili precedenti e voci 2.5 CII e UBL. | Voci trovate |
| [Italia](countries/italy.md) | FatturaPA è la famiglia italiana configurata. | Voci trovate |
| [Paesi Bassi](countries/netherlands.md) | SI-UBL 2.0 ha una voce dedicata. | Voci trovate |
| [Norvegia](countries/norway.md) | EHF Invoice 3.0 è elencato insieme a EHF Order, Order Response e Despatch Advice. | Voci trovate |
| [Polonia](countries/poland.md) | KSeF ha voci generiche, FA2 e FA3. | Voci trovate |
| [Slovenia](countries/slovenia.md) | e-SLOG 1.6 e 2.0 hanno voci separate. | Voci trovate |
| [Spagna](countries/spain.md) | Facturae ha voci generiche, 3.2, 3.2.1 e 3.2.2. | Voci trovate |
| [Svezia](countries/sweden.md) | Svefaktura 1.0 è la voce svedese indicata. | Voci trovate |
| [Australia](countries/australia.md) | PINT A-NZ ha voci di regole per fatture e note di credito condivise con la Nuova Zelanda. | Voci trovate |
| [Nuova Zelanda](countries/new-zealand.md) | PINT A-NZ ha voci di regole per fatture e note di credito condivise con l’Australia. | Voci trovate |
| [India](countries/india.md) | India GST E-Invoice e GST CreditNote hanno voci separate. | Voci trovate |
| [Indonesia](countries/indonesia.md) | Indonesia E-Faktur è la famiglia configurata. | Voci trovate |
| [Cina](countries/china.md) | Il catalogo comprende Fapiao, E-Fapiao, General VAT Invoice e Special VAT Invoice. | Voci trovate |
| [Giappone](countries/japan.md) | JP PINT e JP PINT Self-Billing hanno voci separate. | Voci trovate |
| [Corea del Sud](countries/korea.md) | Korea E-Tax Invoice e Korea NTS sono famiglie configurate. | Voci trovate |
| [Malaysia](countries/malaysia.md) | MyInvois ha voci di regole per fatture e note di credito. | Voci trovate |
| [Filippine](countries/philippines.md) | Philippines EIS è la famiglia configurata. | Voci trovate |
| [Singapore](countries/singapore.md) | InvoiceNow ha voci per fatture e note di credito; InvoiceNow SG è un’altra etichetta configurata. | Voci trovate |
| [Taiwan](countries/taiwan.md) | Taiwan eGUI è la famiglia configurata. | Voci trovate |
| [Thailandia](countries/thailand.md) | Thailand E-Tax Invoice è la famiglia configurata. | Voci trovate |
| [Vietnam](countries/vietnam.md) | Vietnam E-Invoice è la famiglia configurata. | Voci trovate |
| [Argentina](countries/argentina.md) | Argentina AFIP e Factura Electronica sono etichette configurate. | Voci trovate |
| [Brasile](countries/brazil.md) | Il Brasile ha voci NF-e, NFC-e, CT-e, NFS-e e SPED NFS-e. NFS-e comprende le versioni 1.00 e da 2.00 a 2.04; SPED comprende 1.00.02 e 1.01. | Voci trovate |
| [Cile](countries/chile.md) | Chile DTE ha voci per fatture, note di credito e guide di spedizione. | Voci trovate |
| [Colombia](countries/colombia.md) | Colombia Factura Electronica e Documento Soporte hanno voci separate. | Voci trovate |
| [Costa Rica](countries/costa-rica.md) | La documentazione precedente cita il Costa Rica, ma nel catalogo di sviluppo esaminato non è stata trovata alcuna voce di classificazione o configurazione corrispondente. | Non confermato |
| [Ecuador](countries/ecuador.md) | Ecuador SRI ha voci generiche, 1.0.0, 1.1.0, 2.0.0 e 2.1.0. La ritenuta è un tipo di documento separato. | Voci trovate |
| [Messico](countries/mexico.md) | Mexico CFDI 3.3 e 4.0 hanno voci separate. | Voci trovate |
| [Paraguay](countries/paraguay.md) | Paraguay DTE, SIFEN e SIFEN 150 sono etichette configurate. | Voci trovate |
| [Perù](countries/peru.md) | Peru CPE ha voci generiche, UBL 2.0 e UBL 2.1. Factura Electronica è un’altra etichetta. | Voci trovate |
| [Uruguay](countries/uruguay.md) | Uruguay CFE ha voci generiche, 24 e 25. Sono elencate anche E-Factura ed E-Nota Credito. | Voci trovate |
| [Kazakistan](countries/kazakhstan.md) | Kazakhstan ESF è la famiglia configurata. | Voci trovate |
| [Arabia Saudita](countries/saudi-arabia.md) | ZATCA Fatoorah, Reporting, Semplificato e Fattura Fiscale hanno voci separate. | Voci trovate |
| [Turchia](countries/turkey.md) | Turkey E-Fatura ed E-Arsiv sono famiglie configurate separate. | Voci trovate |
| [Emirati Arabi Uniti](countries/united-arab-emirates.md) | UAE VAT Invoice è l’etichetta configurata. | Voci trovate |
| [Internazionale](countries/international.md) | Le voci internazionali comprendono Peppol BIS 3.0, UBL 2.1, CII puro, EDI, INVOIC02, cXML, OCI, BOD e SPS Commerce RSX 7.7.4. | Voci trovate |

## Factur-X / ZUGFeRD: non inventare una versione di pubblicazione

Un Guideline ID CII armonizzato può identificare una famiglia e un profilo pur condividendo lo stesso marcatore 1p0 tra più versioni. Factur-X XMP Version 1.0 è un marcatore di schema, non una pubblicazione come 1.08 o 1.09. I metadati XMP di ZUGFeRD possono dichiararne la versione. In assenza di metadati autorevoli, mantenete il risultato della famiglia generica e confermate il file originale con il mittente.

MINIMUM e BASIC WL possono omettere informazioni sulle righe necessarie alle elaborazioni successive. BASIC, EN16931/COMFORT ed EXTENDED offrono coperture di dati diverse. Un profilo più esteso può contenere campi non utilizzati dalla vostra mappatura di estrazione. Verificate i campi richiesti con esempi reali.

## Verificare un formato nell’organizzazione

1. Conservate l’XML originale o il PDF con il relativo XML incorporato. Leggete lo spazio dei nomi, lo schema o l’identificatore di personalizzazione, nonché la versione e il profilo dichiarati.

2. Aprite Impostazioni → Tipi di documento → E-Doc per il documento aziendale pertinente. Cercate il formato esatto del documento elettronico indicato nella guida.

3. Verificate la sorgente Default o Custom effettivamente utilizzata e la sua versione di configurazione attiva. Esaminate Transformation, Preview ed Extraction Paths. Salvare una bozza non la attiva.

4. Provate file sorgente rappresentativi per ogni sintassi, versione e documento aziendale necessari. Verificate i campi principali, gli importi, le imposte, la classificazione fattura/nota di credito e l’esportazione ERP.

5. Confermate separatamente i criteri di validazione e il trasporto. Conservate le mappature personalizzate e controllate le approvazioni e la cronologia delle esportazioni prima di riavviare l’elaborazione dei documenti esistenti.

[Verifiche di accettazione](../credit-note-recognized-as-invoice.md)

[Configurare DocBits con Claude o Codex](../../../../../../advanced-functions-and-tools/docbits-mcp/configuration-with-claude-or-codex.md): connessione, prompt, anteprime, modifiche con versioni, verifiche e ripristino.
