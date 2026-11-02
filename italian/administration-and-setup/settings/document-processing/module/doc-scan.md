---
description: Crea documenti in DocBits con uno scanner locale e Doc Scan.
---

# Doc Scan

## Scaricare e installare il software dello scanner

Nella dashboard di DocBits, fare clic su Scan Document.

<figure><img src="../../../../.gitbook/assets/image (203).png" alt="Pulsante Scan Document nella dashboard di DocBits"><figcaption></figcaption></figure>

Se il software locale dello scanner non è installato, DocBits mostra una richiesta di download. Scegliere il download per il proprio sistema operativo.

<figure><img src="../../../../.gitbook/assets/image (204).png" alt="Richiesta di download del software locale dello scanner"><figcaption></figcaption></figure>

Aprire il file di installazione scaricato. Il programma di installazione illustrato è per macOS; seguire le istruzioni per il proprio sistema operativo.

<figure><img src="../../../../.gitbook/assets/image (205).png" alt="Avvio del programma di installazione del software dello scanner"><figcaption></figcaption></figure>

Nel programma di installazione illustrato, fare clic su Continue, accettare la licenza software con Agree e proseguire. Controllare la destinazione e lo spazio richiesto, quindi fare clic su Install. I 33,6 MB visualizzati si riferiscono a quella versione del programma di installazione; lo spazio richiesto può cambiare con la versione.

Al termine dell’installazione, chiudere il programma di installazione.

<figure><img src="../../../../.gitbook/assets/image (206).png" alt="Installazione del software dello scanner completata"><figcaption></figcaption></figure>

Aprire https://local.polydocs.io:12500/ nel browser per verificare il servizio locale. Se il browser non riesce a raggiungerlo e si utilizza un FRITZ!Box, controllare le impostazioni di protezione dal DNS rebinding descritte di seguito.

<figure><img src="../../../../.gitbook/assets/image (207).png" alt="Errore del browser durante la verifica del servizio locale dello scanner"><figcaption></figcaption></figure>

Quando viene visualizzata la pagina del servizio locale, fare clic su DocBits per aprire DocBits.

<figure><img src="../../../../.gitbook/assets/image (208).png" alt="Pagina del servizio locale dello scanner dopo una connessione riuscita"><figcaption></figcaption></figure>

Accedere nella pagina di login di DocBits per aprire la dashboard.

<figure><img src="../../../../.gitbook/assets/image (209).png" alt="Pagina di accesso a DocBits aperta dal servizio locale"><figcaption></figcaption></figure>

Attivare Doc Scan nelle impostazioni, sotto Moduli.

<figure><img src="../../../../.gitbook/assets/image (210).png" alt="Impostazione del modulo Doc Scan"><figcaption></figcaption></figure>

## Impostazioni di rete del FRITZ!Box

Se https://local.polydocs.io:12500/ non è raggiungibile perché un FRITZ!Box blocca le risposte DNS con indirizzi privati, il browser può segnalare un timeout DNS. Il FRITZ!Box utilizza questa protezione contro il DNS rebinding. Aggiungere un’eccezione per il nome host di questo servizio locale:

1. Nell’interfaccia tedesca del FRITZ!Box, aprire Heimnetz (rete domestica), quindi Netzwerk (rete).
2. Aprire la scheda Netzwerkeinstellungen (impostazioni di rete).
3. In DNS-Rebind-Schutz (protezione dal DNS rebinding), aggiungere local.polydocs.io alle eccezioni per i nomi host.
4. Fare clic su Übernehmen (applica) e verificare nuovamente il servizio locale.

## Disinstallare Doc2Scan Service Manager

Per disinstallare Doc2Scan Manager su macOS, eseguire:

```bash
sudo bash /Library/doc2scan/uninstall.sh
```

## Compatibilità degli scanner

sane-airscan è un backend SANE per Apple AirScan/eSCL e Microsoft WSD (WS-Scan, Web Services for Devices). Si tratta di protocolli per la scansione in rete.

Consultare le [informazioni di compatibilità aggiornate di sane-airscan](https://github.com/alexpevzner/sane-airscan) per i dispositivi e i protocolli di cui è stato segnalato il supporto. La disponibilità di un protocollo o una segnalazione relativa a sane-airscan non garantisce che tutte le funzioni del dispositivo funzionino in Doc Scan. Provare lo scanner con il flusso di lavoro Doc Scan necessario.
