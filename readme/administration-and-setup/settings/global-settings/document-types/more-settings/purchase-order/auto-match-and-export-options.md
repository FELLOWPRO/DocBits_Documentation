# Opcje automatycznego dopasowania i eksportu

Trzy ustawienia na końcu karty **Zamówienie zakupu** określają, kto widzi skróty dopasowania PO i które dokumenty mogą być eksportowane samodzielnie po dopasowaniu. Obowiązują dla jednego typu dokumentu naraz.

<figure><img src="../../../../../../.gitbook/assets/doc-type-settings-po-options-pl.png" alt="Karta Zamówienie zakupu w ustawieniach typu dokumentu ze wszystkimi opcjami PO"><figcaption><p>Karta Zamówienie zakupu. Trzy poniższe opcje to ostatnie trzy wiersze.</p></figcaption></figure>

## Zezwalaj na automatyczny eksport dla niepasujących wierszy zamówienia zakupu

Automatyczny eksport po dopasowaniu PO zwykle wymaga **w pełni dopasowanego** dokumentu. Gdy ten przełącznik jest włączony, automatycznie mogą być eksportowane także dokumenty o statusie **Brak pasujących linii PO**. Ten status oznacza, że zamówienie zakupu nie ma linii, do których można dopasować fakturę.

* **Wyłączony (domyślnie):** automatycznie eksportowane są tylko w pełni dopasowane dokumenty.
* **Włączony:** automatycznie eksportowane są w pełni dopasowane dokumenty oraz dokumenty bez pasujących linii PO.

Przełącznik ma znaczenie tylko wtedy, gdy dokumenty są eksportowane automatycznie, na przykład przez [**Automatyczny eksport, jeśli zamówienie zostało dopasowane w 100%**](../../../../document-processing/module/auto-export-if-po-matched-100.md) lub kartę eksportu DocFlow. Nie zmienia sposobu dopasowywania linii.

## Automatyczne dopasowanie i eksport widoczne dla

Ekran dopasowania PO zawiera akcję **Automatyczne dopasowanie i eksport**. Dopasowuje ona dokument i eksportuje go zaraz po dopasowaniu. To ustawienie określa, kto dostaje tę akcję:

| Wartość | Kto widzi akcję |
| ------- | --------------- |
| **Tylko administrator** (domyślnie) | Administratorzy |
| **Wszyscy użytkownicy** | Każdy użytkownik, który może otworzyć ekran dopasowania PO |

Administratorzy zawsze widzą tę akcję. Ustawienie nie włącza funkcji. Moduł [**Automatyczny eksport, jeśli zamówienie zostało dopasowane w 100%**](../../../../document-processing/module/auto-export-if-po-matched-100.md) musi być aktywny dla organizacji.

## Użyj wierszy kwoty netto dla dopasowanej kwoty całkowitej widocznej dla

Ekran dopasowania PO może obliczać **Całkowita liczba dopasowań** na podstawie **Kwoty netto** dopasowanych linii faktury, zamiast ją wyliczać. To ustawienie określa, kto może włączyć to obliczenie:

| Wartość | Kto widzi przełącznik |
| ------- | --------------------- |
| **Tylko administrator** (domyślnie) | Administratorzy |
| **Wszyscy użytkownicy** | Każdy użytkownik, który może otworzyć ekran dopasowania PO |

Gdy przełącznik jest włączony, Całkowita liczba dopasowań używa wartości Kwoty netto bezpośrednio z dopasowanych linii faktury.
