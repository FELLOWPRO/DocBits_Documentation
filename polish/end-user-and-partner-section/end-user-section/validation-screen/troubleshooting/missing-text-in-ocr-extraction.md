# Brakujący tekst w ekstrakcji OCR

## **Problem**

W niektórych przypadkach tekst może wydawać się brakujący w **Widoku OCR**, co uniemożliwia jego ekstrakcję za pomocą funkcji ekstrakcji.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/troubleshooting_ocr_5.png)

Aby to zweryfikować, kliknij przycisk **Widok OCR** na pasku narzędzi po prawej stronie. Jeśli tekst się tam nie pojawia, oznacza to, że nie jest dostępny do ekstrakcji.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/troubleshooting_ocr_6.png)

## **Przyczyna**

Najprawdopodobniej przyczyną jest to, że tekst, który próbujesz wyodrębnić, jest częścią obrazu (np. logo lub zeskanowany fragment) w dokumencie.\
Gdy funkcja E-Text jest włączona, tekst, który pojawia się na obrazach lub logo, nie jest uwzględniany w warstwie tekstu wyodrębnionego. W rezultacie ten tekst nie może być dostępny ani wyodrębniony za pomocą standardowej logiki ekstrakcji.

## **Rozwiązanie**

Aby rozwiązać ten problem, wyłącz funkcję E-Text—dla [konkretnego dostawcy](missing-text-in-ocr-extraction.md#wylacz-e-text-dla-konkretnego-dostawcy) lub dla [całej organizacji](missing-text-in-ocr-extraction.md#wylacz-e-text-dla-calej-organizacji). Po dezaktywowaniu E-Text, DocBits będzie polegać wyłącznie na OCR, który jest w stanie wyodrębnić tekst z obrazów i logo w dokumencie.

### **Wyłącz E-Text dla konkretnego dostawcy**

1. Otwórz dokument od konkretnego dostawcy w **Walidacji pól**.
2.  Kliknij menu z trzema kropkami na pasku narzędzi po prawej stronie.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/troubleshooting_ocr_2.png)
3.  Odznacz **Użyj E-Textu, jeśli jest dostępny**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/troubleshooting_ocr_3.png)
4.  Kliknij **Potwierdzać**, aby ponownie uruchomić przetwarzanie dokumentu.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/troubleshooting_ocr_4.png)

### Wyłącz E-Text dla całej organizacji

1.  Przejdź do **Ustawienia → Przetwarzanie dokumentów → Ustawienia OCR**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_ocr.png)
2.  W sekcji **Ogólne ustawienia OCR** odznacz opcję **Użyj E-Textu, jeśli jest dostępny**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/troubleshooting_ocr_1.png)
