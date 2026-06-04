# Opis przepływu pracy: warunkowy wyzwalacz eksportu



<figure><img src="../../../.gitbook/assets/docbits_settings_workflow.png" alt="DocBits Ustawienia Przepływ pracy"><figcaption></figcaption></figure>

Ten przepływ pracy określa warunki, w jakich należy zainicjować proces eksportu. Zapewnia, że tylko dokumenty spełniające wszystkie określone kryteria są przetwarzane do eksportu, co zwiększa integralność danych i zgodność z regułami biznesowymi.

### When:

* Dokument w systemie jest oceniany pod kątem kwalifikowalności do eksportu.

### Logika:

1. **Sprawdzenie typu dokumentu**
   * Dokument musi być określonego typu (np. "Invoice" lub "Receipt"). Określ typ dokumentu, który kwalifikuje się do procesu eksportu.
2. **Weryfikacja statusu**
   * Bieżący status dokumentu musi spełniać wstępnie zdefiniowane kryteria (np. "Approved" lub "Ready for Export"), wskazując, że jest gotowy do dalszego przetwarzania.
3. **Warunki kontekstowe**
   * Wykonywane są dodatkowe kontrole, aby upewnić się, że szczegóły dokumentu są zgodne z określonymi wymaganiami. Kontrole te mogą obejmować weryfikację informacji w potwierdzeniach zamówień lub zamówieniach zakupu. Określ konkretne warunki, które muszą zostać spełnione. Na przykład:
     * Wszystkie pozycje wymienione w potwierdzeniu zamówienia są zgodne z tymi w zamówieniu zakupu.
     * Łączna kwota w potwierdzeniu zamówienia jest zgodna z łączną kwotą w zamówieniu zakupu.
     * Daty dostawy określone w potwierdzeniu zamówienia są zgodne z tymi w zamówieniu zakupu.

### Then:

#### Action:

* **Initiate Export**
  * Jeśli wszystkie powyższe warunki są spełnione, system automatycznie rozpoczyna proces eksportu dokumentu.
  * Może to obejmować wygenerowanie pliku eksportu, wysłanie danych do systemu zewnętrznego lub uruchomienie przepływu pracy w innej aplikacji.

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
