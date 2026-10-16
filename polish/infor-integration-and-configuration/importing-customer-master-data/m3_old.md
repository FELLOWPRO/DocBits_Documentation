---
hidden: true
noIndex: true
---

# M3\_OLD

## Importowanie szablonu połączenia API w Infor M3

Ten przewodnik wyjaśnia, jak zaimportować szablon połączenia API, aby szybko skonfigurować kluczowe ustawienia integracji z Infor M3. Użycie szablonu pozwala ustanowić predefiniowaną konfigurację połączenia, upraszcza proces i zapewnia spójność.

<mark style="color:red;">**Uwaga**</mark>: Szczegółowe informacje o konfiguracji poszczególnych obszarów, takich jak Auto Accounting, integracja dostawców, zamówienia zakupu lub Table Extraction dla elementów kosztowych, znajdziesz w odpowiedniej dokumentacji:

* [Auto Accounting](m3/auto-accounting.md)
* [Dostawcy i zamówienia zakupu](m3/suppliers-and-purchase-orders.md)
* [Jak zaimportować wszystkich dostawców](m3/how-to-import-all-suppliers.md)
* [Table Extraction dla elementu kosztowego](m3/table-extraction-for-costing-element.md)

### **Pobierz szablon**

Przed importem pobierz wymagany szablon połączenia za pomocą poniższego pliku:

{% file src="../../.gitbook/assets/DocBits-Dev-Import-Template.xml" %}

### Import szablonu

#### Kroki importu szablonu połączenia

1. **Otwórz Infor ION Desk:**
   *   Przejdź do **InforOS** → **ION Desk** → **Connect** → **Connection Points**.

       ![](https://lh7-us.googleusercontent.com/ySRjNzMXFzwSOYKx9hnlKLPHPuXpmfTvRADBfV6cpT8ajiEUbS4oXpd9InhXG09mHLakhqBTJMH4yQJNG5z9RXmbAjh8YbuGhxnXSeooIH_r3RAGOvJE6Ok67ST_272zFfhB_TTFYg3b-NwFq0CAv2o)
2. **Zaimportuj szablon:**
   *   Kliknij przycisk **Import**.

       <figure><img src="../../.gitbook/assets/m3_import_2.png" alt=""><figcaption></figcaption></figure>
   * Wybierz odpowiedni **plik szablonu** ze swojego komputera.
   *   Kliknij **OK**, aby rozpocząć proces importu.

       <figure><img src="../../.gitbook/assets/m3_import_3.png" alt="" width="327"><figcaption></figcaption></figure>
3. **Potwierdzenie:**
   *   Jeśli import się powiedzie, zostanie wyświetlony komunikat potwierdzający.

       <figure><img src="../../.gitbook/assets/m3_import_4.png" alt=""><figcaption></figcaption></figure>
4. **Konfiguracja po imporcie:**
   * Po zaimportowaniu szablonu możesz w razie potrzeby dostosować wybrane ustawienia połączenia.
   * Nie zapomnij zaimportować lub skonfigurować **konta serwisowego** (Service Account) do uwierzytelniania i kontroli dostępu.

<figure><img src="../../.gitbook/assets/m3_import_5.png" alt=""><figcaption></figcaption></figure>
