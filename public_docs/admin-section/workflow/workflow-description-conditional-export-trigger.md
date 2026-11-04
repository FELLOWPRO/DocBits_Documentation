# Przykład procesu roboczego: Wyzwalacz eksportu warunkowego



<figure><img src="../../.gitbook/assets/docbits_settings_workflow.png" alt="DocBits Ustawienia Przepływ pracy"><figcaption></figcaption></figure>

Ten proces roboczy określa warunki, w których powinien zostać uruchomiony proces eksportu. Zapewnia, że tylko dokumenty spełniające wszystkie określone kryteria są przetwarzane do eksportu, zwiększając integralność danych i zgodność z zasadami biznesowymi.

### Kiedy:

* Dokument w systemie jest oceniany pod kątem kwalifikowalności do eksportu.

### Logika:

1. **Sprawdzenie typu dokumentu**
* Dokument musi być określonego typu (np. "Faktura" lub "Paragon"). Określ typ dokumentu kwalifikujący się do procesu eksportu.
2. **Weryfikacja statusu**
* Obecny status dokumentu musi spełniać wstępnie określone kryteria (np. "Zatwierdzony" lub "Gotowy do eksportu"), wskazujące, że jest gotowy do dalszego przetwarzania.
3. **Warunki kontekstowe**
* Wykonywane są dodatkowe kontrole, aby upewnić się, że szczegóły dokumentu są zgodne z określonymi wymaganiami. Kontrole te mogą obejmować weryfikację informacji w potwierdzeniach zamówień lub zamówieniach zakupu. Określ konkretne warunki, które muszą zostać spełnione. Na przykład:
* Wszystkie pozycje wymienione w potwierdzeniu zamówienia odpowiadają tym w zamówieniu zakupu.
* Całkowita kwota w potwierdzeniu zamówienia odpowiada całkowitej kwocie w zamówieniu zakupu.
* Daty dostawy określone w potwierdzeniu zamówienia są zgodne z tymi w zamówieniu zakupu.

### Następnie:

#### Działanie:

* **Uruchom eksport**
* Jeśli wszystkie powyższe warunki są spełnione, system automatycznie rozpoczyna proces eksportu dokumentu.
* Może to obejmować generowanie pliku eksportu, wysyłanie danych do zewnętrznego systemu lub wyzwalanie procesu roboczego w innej aplikacji.

#### Przykład implementacji:
```yaml
rules:
- description: "Conditional Export Trigger"
conditions:
- type: "DocumentType"
criteria: "<SpecifyDocumentType>"
- type: "Status"
criteria: "<SpecifyStatus>"
- type: "DetailMatch"
criteria:
- "ItemMatch"
- "AmountMatch"
- "DateMatch"
actions:
- operation: "StartExport"
```

