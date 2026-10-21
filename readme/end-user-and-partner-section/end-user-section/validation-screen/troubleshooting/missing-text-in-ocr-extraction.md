# Brakujący tekst w ekstrakcji OCR

## **Problem**

W niektórych przypadkach tekst może wydawać się brakujący w **Widoku OCR**, co uniemożliwia jego ekstrakcję za pomocą funkcji ekstrakcji.

<figure><img src="../../../../.gitbook/assets/s150-troubleshooting_ocr_5-pl.png" alt="Kontrola pól fikcyjnej faktury."><figcaption><p>Kontrola pól fikcyjnej faktury.</p></figcaption></figure>

Aby to zweryfikować, kliknij przycisk **Widok OCR** na pasku narzędzi po prawej stronie. Jeśli tekst się tam nie pojawia, oznacza to, że nie jest dostępny do ekstrakcji.

<figure><img src="../../../../.gitbook/assets/s150-troubleshooting_ocr_6-pl.png" alt="Widok OCR tekstu rozpoznanego na fikcyjnej fakturze."><figcaption><p>Widok OCR tekstu rozpoznanego na fikcyjnej fakturze.</p></figcaption></figure>

## **Przyczyna**

Najprawdopodobniej przyczyną jest to, że tekst, który próbujesz wyodrębnić, jest częścią obrazu (np. logo lub zeskanowany fragment) w dokumencie.\
Gdy funkcja E-Text jest włączona, tekst, który pojawia się na obrazach lub logo, nie jest uwzględniany w warstwie tekstu wyodrębnionego. W rezultacie ten tekst nie może być dostępny ani wyodrębniony za pomocą standardowej logiki ekstrakcji.

## **Rozwiązanie**

Aby rozwiązać ten problem, wyłącz funkcję E-Text—dla [konkretnego dostawcy](missing-text-in-ocr-extraction.md#wylacz-e-text-dla-konkretnego-dostawcy) lub dla [całej organizacji](missing-text-in-ocr-extraction.md#wylacz-e-text-dla-calej-organizacji). Po dezaktywowaniu E-Text, DocBits będzie polegać wyłącznie na OCR, który jest w stanie wyodrębnić tekst z obrazów i logo w dokumencie.

### **Wyłącz E-Text dla konkretnego dostawcy**

1. Otwórz dokument od konkretnego dostawcy w **Walidacji pól**.
2.  Kliknij menu z trzema kropkami na pasku narzędzi po prawej stronie.

<figure><img src="../../../../.gitbook/assets/s150-troubleshooting_ocr_2-pl.png" alt="Menu dodatkowych opcji walidacji pól."><figcaption><p>Menu dodatkowych opcji walidacji pól.</p></figcaption></figure>

3.  Odznacz **Użyj E-Textu, jeśli jest dostępny**.

<figure><img src="../../../../.gitbook/assets/s150-troubleshooting_ocr_3-pl.png" alt="Opcja tekstu elektronicznego w menu dokumentu."><figcaption><p>Opcja tekstu elektronicznego w menu dokumentu.</p></figcaption></figure>

4.  Kliknij **Potwierdzać**, aby ponownie uruchomić przetwarzanie dokumentu.

<figure><img src="../../../../.gitbook/assets/s150-troubleshooting_ocr_4-pl.png" alt="Potwierdzenie przed zmianą użycia tekstu elektronicznego."><figcaption><p>Potwierdzenie przed zmianą użycia tekstu elektronicznego.</p></figcaption></figure>

### Wyłącz E-Text dla całej organizacji

1.  Przejdź do **Ustawienia → Przetwarzanie dokumentów → Ustawienia OCR**.

<figure><img src="../../../../.gitbook/assets/s150-settings_ocr-pl.png" alt="Ustawienia OCR w polskim interfejsie."><figcaption><p>Ustawienia OCR w polskim interfejsie.</p></figcaption></figure>

2.  W sekcji **Ogólne ustawienia OCR** odznacz opcję **Użyj E-Textu, jeśli jest dostępny**.

<figure><img src="../../../../.gitbook/assets/s150-troubleshooting_ocr_1-pl.png" alt="Ogólne ustawienia OCR z opcją tekstu elektronicznego."><figcaption><p>Ogólne ustawienia OCR z opcją tekstu elektronicznego.</p></figcaption></figure>

Obrazy wykorzystują fikcyjną fakturę z dostępnym tekstem OCR. Pokazują elementy interfejsu, a nie odtworzony incydent brakującego tekstu.
