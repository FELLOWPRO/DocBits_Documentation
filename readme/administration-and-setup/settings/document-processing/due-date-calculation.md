# Obliczanie terminu płatności

<figure><img src="../../../.gitbook/assets/due_date_calc_overview.png" alt="Ustawienia obliczania terminu płatności"><figcaption><p>Ustawienia obliczania terminu płatności</p></figcaption></figure>

Strona **Obliczanie terminu płatności** (**Przetwarzanie dokumentów → Obliczanie terminu płatności**) kontroluje, w jaki sposób DocBits oblicza terminy płatności faktur, terminy płatności rabatu (Skonto) oraz warunki płatności na podstawie kodów warunków płatności znalezionych na fakturach.

## Pokaż obliczone pola

Włącz **Pokaż obliczone pola**, aby automatycznie obliczone pola faktury — termin płatności, termin płatności rabatu, warunki płatności i kod przypisania AP — pojawiały się w Ustawieniach pól oraz jako zmienne w Szybkim wyszukiwaniu i szablonach e-mail. Niestandardowe typy dokumentów nigdy nie są objęte.

## Obliczanie terminu płatności faktury

### Obsługa weekendów

<figure><img src="../../../.gitbook/assets/due_date_calc_weekend_options.png" alt="Opcje konwencji weekendowej"><figcaption><p>Opcje konwencji weekendowej</p></figcaption></figure>

Wybierz, jak dostosowywany jest termin płatności przypadający w sobotę lub niedzielę. Dotyczy to **zarówno** terminu płatności faktury, jak i terminu płatności rabatu (Skonto).

| Konwencja | Efekt |
|-----------|-------|
| **Brak** | Zachowaj datę kalendarzową (bez dostosowania). |
| **Następna** | Przenieś sob./niedz. na następny poniedziałek. |
| **Poprzednia** | Przenieś sob./niedz. na poprzedni piątek. |
| **Najbliższa** | Sobota → piątek, niedziela → poniedziałek. |
| **Zmodyfikowana następna** | Następny poniedziałek, chyba że wypada w następnym miesiącu; wtedy poprzedni piątek. |

### Kod przypisania AP

Przypisz warunki płatności dostawcy do kodów przypisania AP dla zautomatyzowanego routingu faktur, wybierając **pole kodu przypisania AP**.

## Nadpisania warunków rabatu

<figure><img src="../../../.gitbook/assets/due_date_calc_mappings.png" alt="Nadpisania warunków rabatu"><figcaption><p>Nadpisania warunków rabatu</p></figcaption></figure>

Użyj **Nadpisań warunków rabatu**, aby przypisać określony prefiks do procentu rabatu i liczby dni. Kliknij **+ Dodaj mapowanie**, aby dodać wiersz z polami **Prefiks**, **Procent** i **Dni**.

## Obsługiwane formaty

<figure><img src="../../../.gitbook/assets/due_date_calc_formats.png" alt="Obsługiwane formaty warunków płatności i rabatu"><figcaption><p>Obsługiwane formaty warunków płatności i rabatu</p></figcaption></figure>

DocBits rozpoznaje następujące kody warunków płatności i rabatu.

**Obsługiwane formaty warunków płatności**

| Format | Przykład | Znaczenie |
|--------|----------|-----------|
| Infor M3 | `N90`, `N30` | Netto 90 / 30 dni |
| Infor M3 | `NET` | Płatne przy odbiorze |
| Infor M3 | `M20` | 20. dnia następnego miesiąca |
| Infor M3 | `E15` | Koniec miesiąca + 15 dni |
| Infor LN | `030`, `30` | Netto 30 dni |
| Reversed | `14N`, `30N` | Netto 14 / 30 dni |
| Kody tekstowe | `REC`, `DUE`, `COD` | Płatne przy odbiorze |

**Format warunków rabatu** — warunki rabatu kodują rabaty za wcześniejszą płatność jako kody 3-cyfrowe: pierwsza cyfra to procent rabatu, dwie ostatnie to liczba dni, w ciągu których należy zapłacić.

| Kod | Znaczenie |
|-----|-----------|
| `210` | 2% rabatu przy płatności w ciągu 10 dni |
| `130` | 1% rabatu przy płatności w ciągu 30 dni |
| `545` | 5% rabatu przy płatności w ciągu 45 dni |
| `0` | Brak rabatu |
