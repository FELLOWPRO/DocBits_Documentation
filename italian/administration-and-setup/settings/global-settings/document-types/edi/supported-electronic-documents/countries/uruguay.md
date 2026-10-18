---
description: "Uruguay CFE ha voci generiche, 24 e 25. Sono elencate anche E-Factura ed E-Nota Credito."
---

# Uruguay

Usate questa guida per identificare la famiglia configurata e l’ambito delle versioni prima di provare un file sorgente.

[Tutti i paesi e ambito del supporto](../README.md)

## Video esplicativo del paese

La narrazione localizzata e i sottotitoli WebVTT spiegano la selezione del formato, la configurazione e le verifiche di accettazione.

Questa panoramica in sola lettura mostra la configurazione esistente del paese in DocBits. Verificate la fonte utilizzata e la versione attiva, quindi provate fatture, note di credito ed esportazioni rappresentative nella vostra organizzazione.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/edocs_country_uruguay/v2/it.mp4" %}

[Uruguay — Video esplicativo del paese](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/edocs_country_uruguay/v2/it.mp4)

[WebVTT](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/edocs_country_uruguay/v2/it.vtt)

## Varianti e limiti delle versioni

Uruguay CFE ha voci generiche, 24 e 25. Sono elencate anche E-Factura ed E-Nota Credito.

**Sintassi:** XML

Le voci per le note di credito non hanno insiemi di componenti di estrazione dedicati nello stato esaminato. Confermate la versione CFE e la mappatura effettivamente utilizzata per fatture o note di credito.

Le tabelle riportano una verifica del catalogo di sviluppo effettuata il 17 ottobre 2026 e del relativo codice di elaborazione. Descrivono le regole e i componenti di configurazione disponibili, senza certificare ogni file, requisito legale o distribuzione in produzione. L’organizzazione può sostituire le impostazioni predefinite.

## Matrice delle regole e dei componenti esaminati

| Etichetta esatta del formato | Chiave del documento della regola | Componenti disponibili |
| --- | --- | --- |
| `URUGUAY E-FACTURA` | `CREDIT_NOTE` | C / — / — / — |
| `URUGUAY E-NOTA CREDITO` | `CREDIT_NOTE` | C / — / — / — |
| `URUGUAY CFE` | `INVOICE` | C / T / P / E |
| `URUGUAY CFE 24` | `INVOICE` | C / T / P / E |
| `URUGUAY CFE 25` | `INVOICE` | C / T / P / E |
| `URUGUAY E-FACTURA` | `INVOICE` | C / T / P / E |

C = classificazione, T = Transformation, P = Preview, E = Extraction Paths. La chiave del documento è la chiave di ricerca della regola o configurazione; non garantisce il valore finale memorizzato di invoice_type. Una trasformazione può classificare una nota di credito tramite una mappatura INVOICE.

Un trattino indica che la verifica dello stato non ha rilevato un componente dedicato per questa esatta combinazione di formato e chiave del documento. Non esclude una mappatura condivisa o di ripiego. Verificate il meccanismo di risoluzione effettivamente utilizzato e un file rappresentativo prima di fare affidamento su quel percorso.

## Trovare la mappatura in DocBits

<figure><img src="../../../../../../../.gitbook/assets/edocs-support-uruguay-it.png" alt="Uruguay: URUGUAY CFE 25"><figcaption><p>Interfaccia reale di sviluppo: il formato rappresentativo e i relativi componenti di configurazione disponibili. Le altre versioni sono elencate nella matrice.</p></figcaption></figure>

## Verifiche di accettazione

La verifica di un componente conferma la presenza della configurazione. Non è un test di elaborazione completo per ogni versione. Provate il contenuto esatto e il percorso di elaborazione di fatture o note di credito richiesto dall’integrazione.

## Verificare un formato nell’organizzazione

1. Conservate l’XML originale o il PDF con il relativo XML incorporato. Leggete lo spazio dei nomi, lo schema o l’identificatore di personalizzazione, nonché la versione e il profilo dichiarati.

2. Aprite Impostazioni → Tipi di documento → E-Doc per il documento aziendale pertinente. Cercate il formato esatto del documento elettronico indicato nella guida.

3. Verificate la sorgente Default o Custom effettivamente utilizzata e la sua versione di configurazione attiva. Esaminate Transformation, Preview ed Extraction Paths. Salvare una bozza non la attiva.

4. Provate file sorgente rappresentativi per ogni sintassi, versione e documento aziendale necessari. Verificate i campi principali, gli importi, le imposte, la classificazione fattura/nota di credito e l’esportazione ERP.

5. Confermate separatamente i criteri di validazione e il trasporto. Conservate le mappature personalizzate e controllate le approvazioni e la cronologia delle esportazioni prima di riavviare l’elaborazione dei documenti esistenti.

## Riferimento al formato correlato

- [🇺🇾 URUGUAY CFE](../uruguay-cfe.md)
- [🇺🇾 URUGUAY CFE 24](../uruguay-cfe-24.md)
- [🇺🇾 URUGUAY CFE 25](../uruguay-cfe-25.md)
- [🇺🇾 URUGUAY E-FACTURA](../uruguay-e-factura.md)
- [🇺🇾 URUGUAY E-NOTA CREDITO](../uruguay-e-nota-credito.md)
