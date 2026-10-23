# Faktura

## Wyświetlanie atrybutu w każdym elemencie linii

Jeśli chcesz wyświetlić konkretny atrybut (np. numer zamówienia zakupu) w każdym elemencie linii, wykonaj poniższe kroki. Podejście będzie się różnić w zależności od tego, czy potrzebujesz atrybutu w ekstrakcji JSON, czy w wyjściu XSL.

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 14.33.16.png" alt="Tabela faktury z kolumnami Position, Description, Quantity i Unit Price zawierająca pozycje zamówienia z sumami"><figcaption></figcaption></figure>

### Metoda 1: Wyświetlanie atrybutu w ekstrakcji JSON (konfiguracja DocBits)

1. Przejdź do **Ustawień**
2. Przejdź do **Typów Dokumentów**
3. Wybierz **Invoice/E-Doc**

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 15.07.58.png" alt="Strona ustawień typu dokumentu Invoice z kartami Extraction type, Edit layout, Document Sub Types, Table columns, Fields i Model Training"><figcaption></figcaption></figure>

4. Otwórz kartę **"FATTURAPA"**
5. Kliknij **JSON**

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 15.01.13.png" alt="Lista formatów FATTURAPA z wpisami Preview, Extraction Paths, wariantami FacturX ZUGFERD, Peppol i XRECHNUNG z XSLT"><figcaption></figcaption></figure>

6. Aby utworzyć wersję roboczą, kliknij ikonę **pióra**

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 14.58.56.png" alt="Ustawienia typu dokumentu Invoice z wpisem elektronicznego typu dokumentu FATTURAPA i znacznikiem czasu"><figcaption></figcaption></figure>

7. Wewnątrz tablicy `"tables"` dodaj konkretną kolumnę, którą chcesz wyświetlić, podając nazwę i ścieżkę:

```
{ 
"name": "PURCHASE_ORDER",    
"path":"path_to_source" 
}
```

**UWAGA:** Dokumenty elektroniczne zawsze będą miały ustawione pochodzenie na **Wielką Brytanię**, więc kwoty będą zapisywane w formacie międzynarodowym, przy użyciu **kropki (.)** jako separatora dziesiętnego.

8. Zapisz wersję roboczą

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 15.11.04.png" alt="Wpis wersji Draft ze znacznikiem czasu 28.01.2025 15:10:12 w widoku testowym DocBits"><figcaption></figcaption></figure>

9. Upewnij się, że Twoja wersja robocza jest tą **aktywną**.

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 16.03.50.png" alt="Wpis na liście wersji Draft pokazujący wersję 91.20 ze znacznikiem czasu potwierdzającym aktywny Draft"><figcaption></figcaption></figure>

### Metoda 2: Wyświetlanie atrybutu w wyjściu XSL (podgląd HTML/PDF)

1. Przejdź do **Ustawień**
2. Przejdź do **Typów Dokumentów**
3. Wybierz **Invoice/E-Doc**

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 15.07.58.png" alt="Strona ustawień typu dokumentu Invoice z kartami Extraction type, Edit layout, Document Sub Types, Table columns, Fields i Model Training"><figcaption></figcaption></figure>

4. Otwórz kartę **"FATTURAPA"**
5. **Kliknij XSLT**

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 15.23.06.png" alt="Karta FATTURAPA z listą formatów dokumentów elektronicznych, w tym EDI, wariantów FacturX ZUGFERD, Peppol i wersji XRECHNUNG"><figcaption></figcaption></figure>

6. Aby utworzyć wersję roboczą, kliknij ikonę **pióra**

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 14.58.56.png" alt="Ustawienia typu dokumentu Invoice z wpisem elektronicznego typu dokumentu FATTURAPA i znacznikiem czasu"><figcaption></figcaption></figure>

7. W bloku `<xsl:for-each select="path">`, który generuje wiersze tabeli, dodaj fragment kodu taki jak ten, w miejscu, w którym chcesz, aby pojawił się atrybut (np. w jego własnej kolumnie):

```
<tr>
    <!-- Other columns ... -->

    <td>
        <!-- PO number -->
        <xsl:variable name="variable_name" select="value" />
        <xsl:value-of 
            select="path_to_attribute" 
        />
    </td>
</tr>
```

**UWAGA:** Dokumenty elektroniczne zawsze będą miały ustawione pochodzenie na **Wielką Brytanię**, więc kwoty będą zapisywane w formacie międzynarodowym, przy użyciu **kropki (.)** jako separatora dziesiętnego.

8. Zapisz wersję roboczą

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 15.11.04.png" alt="Wpis wersji Draft ze znacznikiem czasu 28.01.2025 15:10:12 w widoku testowym DocBits"><figcaption></figcaption></figure>

9. Upewnij się, że Twoja wersja robocza jest tą **aktywną**.

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 16.03.50.png" alt="Wpis na liście wersji Draft pokazujący wersję 91.20 ze znacznikiem czasu potwierdzającym aktywny Draft"><figcaption></figcaption></figure>
