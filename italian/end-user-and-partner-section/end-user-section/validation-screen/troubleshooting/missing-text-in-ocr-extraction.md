# Testo mancante nell'estrazione OCR

## **Problema**

In alcuni casi, il testo potrebbe sembrare mancante nella **Vista OCR**, il che impedisce di essere estratto utilizzando la funzione di estrazione.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/troubleshooting_ocr_5.png)

Per verificare questo, fai clic sul pulsante **Vista OCR** nella barra degli strumenti a destra. Se il testo non appare lì, significa che non è disponibile per l'estrazione.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/troubleshooting_ocr_6.png)

## **Causa**

La causa più probabile è che il testo che stai cercando di estrarre fa parte di un'immagine (ad es. un logo o una sezione scansionata) all'interno del documento.\
Quando la funzione E-Text è attivata, il testo che appare su immagini o loghi non è incluso nel livello di testo estratto. Di conseguenza, questo testo non può essere accessibile o estratto tramite la logica di estrazione standard.

## **Soluzione**

Per risolvere questo problema, disabilita la funzione E-Text—sia per il [fornitore specifico](missing-text-in-ocr-extraction.md#disabilita-e-text-per-un-fornitore-specifico) sia per [l'intera organizzazione](missing-text-in-ocr-extraction.md#disabilita-e-text-per-lintera-organizzazione). Una volta disattivato E-Text, DocBits si baserà esclusivamente su OCR, che è in grado di estrarre testo da immagini e loghi all'interno del documento.

### **Disabilita E-Text per un Fornitore Specifico**

1. Apri un documento del fornitore specifico in **Validazione del campo**.
2.  Fai clic sul menu a tre punti nella barra degli strumenti a destra.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/troubleshooting_ocr_2.png)
3.  Deseleziona **Utilizzare il testo elettronico, se disponibile**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/troubleshooting_ocr_3.png)
4.  Fai clic su **Confermare** per riavviare l'elaborazione del documento.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/troubleshooting_ocr_4.png)

### Disabilita E-Text per l'Intera Organizzazione

1.  Vai su **Impostazioni → Elaborazione dei documenti → Impostazioni OCR**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_ocr.png)
2.  Sotto **Impostazioni generali OCR**, deseleziona l'opzione **Utilizzare il testo elettronico, se disponibile**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/troubleshooting_ocr_1.png)
