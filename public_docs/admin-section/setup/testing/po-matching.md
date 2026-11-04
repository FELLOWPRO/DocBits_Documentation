# Corrispondenza PO

Quando si tratta di testare la configurazione di corrispondenza PO, sarà necessario creare un ordine di acquisto in LN/M3 per verificare se INFOR è sincronizzato con DocBits.&#x20;

## Creazione di un ordine di acquisto in INFOR

* LN: https://docs.infor.com/ln/10.4/en-us/lnolh/docs/ln\_10.4\_procpoug\_\_en-us.pdf&#x20;
* M3: https://docs.infor.com/m3udi/16.x/en-us/m3beud/default.html?helpcontent=ois610.html&#x20;

Una volta creato il tuo ordine di acquisto, vai su Impostazioni → Ricerca dati principali e cerca il numero dell'ordine di acquisto del PO appena creato poiché dovrebbe ora comparire nei dati principali dell'ordine di acquisto in DocBits.

![](https://lh7-us.googleusercontent.com/JKGJdww6uF6U5mc1s1X\_uCcEMPYeqcikfrFOFjxpxpuaNjw-XmzNmIV2G2x6R-ZpwN2KlZACQe5Hs\_UB26klGU5XZyu6srVVLPVkS9AgEDZ1SO75YF-4ZTIt-aAuxoyyoW5sNPLsl0UxXwk193QNrFs)

Dovresti vedere qui il tuo numero univoco di PO, ciò significa che DocBits e INFOR sono correttamente sincronizzati.

Ora carica la tua fattura che corrisponde alla quantità e ai prezzi unitari dell'ordine di acquisto che hai creato. Convalida il documento e seleziona la Corrispondenza PO sulla schermata di convalida.

Le righe dell'ordine di acquisto e della fattura dovrebbero corrispondere automaticamente, quindi seleziona semplicemente l'opzione di esportazione e verifica se il documento viene esportato senza errori. Se incontri un errore di esportazione, crea un ticket per il team di supporto di DocBits per assisterti. Se non sei sicuro su come creare un ticket all'interno di DocBits, consulta la nostra documentazione panoramica di DocBits per assistenza.
