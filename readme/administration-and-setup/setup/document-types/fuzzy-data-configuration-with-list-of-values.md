---
hidden: true
---

# Configurazione dei dati fuzzy con elenco di valori

### **Panoramica**

Ogni tipo di documento ha le proprie configurazioni List of Values (LoV), che devono essere impostate separatamente. A differenza di **Fuzzy Data with Master Data**, **List of Values** non include gruppi di lookup predefiniti.

### Per configurare List of Values, vai a:

Settings → Global Settings → Document Types → Invoice → Fields → Master Data Settings → LOV Master Data

### **Creare una nuova configurazione List of Values**

Esistono due modi per creare una configurazione List of Values:

**1. Duplicare un lookup esistente**

* Copia tutte le informazioni e i campi di un gruppo esistente.
* Devi solo indicare un **nuovo nome**.

**2. Creare un lookup da zero**

* Fai clic su **"Create List of Values"**.
* Compila i dettagli richiesti:
  * **Configuration Name** → Nome della List of Values.
  * **Lookup Table** → La tabella da cui vengono recuperati i valori.
  * **Conflict Handler** → Scegline uno:
    * Best Score
    * Return None
    * Return First
  * **Context Type** → Determina se la LoV si applica al livello **Header** o **Line**.
  * **Match All** → _(Sono necessari ulteriori dettagli)_

### **Gestire i campi all'interno di un gruppo List of Values**

Ogni gruppo LoV contiene campi che possono essere **aggiunti, rimossi o modificati.**

**Aggiungere un nuovo campo**

Per aggiungere un nuovo campo all'interno di un gruppo:

* Fai clic su **"Create"** all'interno del gruppo interessato.
* Fornisci i seguenti dettagli:
  * **Lookup Field** → Il nome della colonna della tabella di lookup.
  * **Validation Field** → Il campo DocBits corrispondente.
  * **Parent Field** → _(Sono necessari ulteriori dettagli)_
  * **Search Operator** → Scegline uno:
    * Smart
    * Contains
    * Exact
    * Starts with
    * Ends with
  * **Caselle di controllo:**
    * **Auto Trigger** → Se abilitata, quando un altro campo in una diversa configurazione di lookup condivide la stessa colonna, questo campo viene aggiornato **automaticamente** ogni volta che l'altro campo viene aggiornato.
    * **Searchable** → Abilita il campo come campo **List of Values**, consentendo le ricerche nella tabella di lookup.

#### **Ultimo passaggio: aggiungere i campi al layout**

Dopo aver configurato i campi List of Values, **assicurati di aggiungerli al layout tramite il Layout Builder**. Se i campi non vengono aggiunti al layout, non saranno disponibili per l'uso.
