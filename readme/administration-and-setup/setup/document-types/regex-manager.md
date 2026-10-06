# Regex Manager

Questa funzione di DocBits è un'alternativa alla classificazione tramite modello: consente di scrivere espressioni regolari ricercabili per un tipo di documento, per la classificazione e altri scopi.

**Tipo di documento:** Il Regex Manager consente di scrivere espressioni regolari e DocBits cerca queste espressioni nel documento. Se un documento corrisponde alla regex di un documento definito, viene classificato nel tipo di documento corrispondente. Se, ad esempio, scrivete un'espressione regolare che trova «Gutschrift», DocBits classifica come nota di credito qualsiasi documento contenente questo termine.

**Origine del documento:** Questo indica a DocBits, tramite espressioni regolari, il paese di origine di un documento. Se, ad esempio, l'espressione regolare di un documento spagnolo contiene il termine «Factura» e DocBits trova questo termine in un documento, riconosce che il documento è di origine spagnola e lo classifica come tale.

## Accesso al Regex Manager

Per usare questa funzione, andate in Impostazioni → Tipi di Documento e fate clic su «Nuovo». Nella procedura «Creare un nuovo tipo di documento», inserite un nome per il tipo di documento e selezionate «Regex» al posto di «Auto» come metodo di estrazione, quindi proseguite con «Avanti».

<figure><img src="../../../.gitbook/assets/regex-manager-create-it-20261006.png" alt="La procedura guidata di DocBits per creare un nuovo tipo di documento, con il nome inserito e l'opzione «Regex» selezionata."><figcaption><p>La procedura «Creare un nuovo tipo di documento» con il nome del tipo di documento e la scelta tra «Auto» e «Regex».</p></figcaption></figure>

## Aggiungere e rimuovere Regex

Il passaggio Regex mostra una tabella delle espressioni regolari esistenti, con Origine e Modello, insieme al pulsante «Aggiungi» per creare nuove voci regex.

<figure><img src="../../../.gitbook/assets/regex-manager-list-it-20261006.png" alt="La tabella del Regex Manager con le espressioni regolari esistenti per origine e modello."><figcaption><p>Il passaggio Regex con la tabella delle espressioni regolari esistenti e il pulsante «Aggiungi».</p></figcaption></figure>
