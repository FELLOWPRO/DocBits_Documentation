---
description: "P1: wariant eksportu, otwarte zadania i status końcowy"
---

# P1: wariant eksportu, otwarte zadania i status końcowy

**Start Export** używa skonfigurowanej drogi eksportu. **Export with Export Configuration** uruchamia wybraną konfigurację. Wariant odroczony kolejkuje ją do eksportu końcowego na końcu bieżącego wykonania. Kolejkowanie nie oznacza automatycznej wysyłki po wszystkich późniejszych zgodach użytkowników.

Sprawdzone nowsze wersje oferują `status=finished` lub `status=exported`: finished zamyka dokument, exported pozwala dalej go edytować. Start Export udostępnia wybór od v4, eksport konfigurowany i odroczony od v3. Wcześniejsze wersje używają finished. Brak wyboru w nowych również przyjmuje finished; nieprawidłowa wartość jest błędem konfiguracji.

Przy `ignore_pending_tasks=false` sprawdzane są otwarte zadania. Usługa może więc odmówić natychmiastowego eksportu konfigurowanego. Ta karta nie dowodzi automatycznego wznowienia po późniejszym zamknięciu zadań. Określ nowe zdarzenie i sprawdź istniejący rekord docelowy przed ponowną wysyłką. Pomijanie zadań nie zastępuje zatwierdzenia.

Podłącz eksport dopiero po jawnie sprawdzonym warunku zatwierdzenia. Odbiór obejmuje otwarte i zakończone zadanie, brak zgody, odbiór w celu testowym oraz powtórne wykonanie. Odróżniaj żądanie eksportu, odbiór i przetworzenie ERP. Pakiet nie zawiera rzeczywistych celów, a jego testy nie dowodzą dostarczenia.

## Karty i przykładowe parametry

Wartości opisują parametry kart, a nie pełny workflow do importu. Zastąp YOUR_* własnymi wyborami testowymi. Projektant zarządza ukrytym ID wywołującego. Katalog: Dev, DocFlow 2.10.38, 21 października 2026; osobno sprawdź wersje i uprawnienia swojej organizacji.

### `export` · v4

Identyfikacja: `757f30ca-ed60-4e04-8131-2779df17f019`

| Parametr | Typ / opcje | Przykład |
| --- | --- | --- |
| `boolean` | `boolean:bool` | `true` |
| `status` | `finished / exported` | `"finished"` |

### `action_export_with` · v3

Identyfikacja: `ebcd854d-68b3-4b5f-8d45-1bcf8c675b21`

| Parametr | Typ / opcje | Przykład |
| --- | --- | --- |
| `export_configuration` | `export_configuration:int` | `"YOUR_TEST_EXPORT_CONFIGURATION_ID"` |
| `ignore_pending_tasks` | `ignore_pending_tasks:bool` | `false` |
| `status` | `finished / exported` | `"exported"` |

### `action_export_with_config_deferred` · v3

Identyfikacja: `060ef4c8-625f-447c-83c9-2ca3f680d88d`

| Parametr | Typ / opcje | Przykład |
| --- | --- | --- |
| `export_configuration` | `export_configuration:int` | `"YOUR_TEST_EXPORT_CONFIGURATION_ID"` |
| `ignore_pending_tasks` | `ignore_pending_tasks:bool` | `false` |
| `status` | `finished / exported` | `"finished"` |

## Biznesowe przypadki testowe

| Przypadek | Wejście / konfiguracja | Oczekiwany wynik |
| --- | --- | --- |
| EXPORT-01 | status=finished | zamknięty |
| EXPORT-02 | status=exported | edytowalny |
| EXPORT-03 | ignore_pending_tasks=false; pending_tasks>0 | możliwa odmowa; automatyczne wznowienie niepotwierdzone |
| EXPORT-04 | action_export_with_config_deferred | w kolejce ≠ odebrane |
| EXPORT-05 | RUN-1 → RUN-2 | destination_records=1 |

## Dowody i ograniczenia

Parametry i zachowanie porównano z katalogiem Dev oraz sprawdzonym kodem. Przypadki biznesowe są instrukcją odbioru. W tym rozdziale nie wykonano osobistych zatwierdzeń, rzeczywistych zmian ani dostarczeń.

[Dalsza nauka](../workflow-learning-path.md) · [Pakiet ćwiczeń](../workflow-training-kit.md)
