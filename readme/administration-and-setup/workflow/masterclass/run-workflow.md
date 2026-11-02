---
description: "P0: Run Workflow, warunki celu i obsługa błędów"
---

# P0: Run Workflow, warunki celu i obsługa błędów

**Run Workflow** wywołuje workflow przez ID i czeka na wykonanie. Nazwa nie wystarcza. Projektant zarządza ukrytym ID wywołującego workflow; nie zmieniaj go jako parametru biznesowego. Bieżący dokument trafia do celu, gdzie wejście i warunki są oceniane ponownie.

Sprawdzone jawne wywołanie dociera również do **nieaktywnego** celu. Nieaktywny nie oznacza więc nieosiągalny przez Run Workflow. Testy Dev obejmowały własny nieaktywny cel szkoleniowy, wywołanie siebie i nieznane ID. Dwa ostatnie przypadki wybrały Error. Wbudowane limity rekursji i łańcucha nie zastępują reguł ograniczających powtórne wywołania.

Odróżniaj zmienne organizacji i pola dokumentu od wyników lokalnych dla wykonania. Wywołanie nie przekazuje automatycznie wszystkich wyników tabel decyzyjnych ani HTTP rodzica. Uzgodnij wymagane pola i sprawdź ich rzeczywiste wartości w kolejnej karcie.

Zielone wywołanie nie potwierdza wszystkich warunków biznesowych celu: wynik Advanced bez błędu technicznego jest uznawany za udane wywołanie i może obejmować `failed_condition`. Sprawdź wybraną ścieżkę celu i jej skutek. Jawnie obsłuż błąd u wywołującego; unikaj A→B→A oraz powtórnych wywołań tego samego celu.

## Karty i przykładowe parametry

Wartości opisują parametry kart, a nie pełny workflow do importu. Zastąp YOUR_* własnymi wyborami testowymi. Projektant zarządza ukrytym ID wywołującego. Katalog: Dev, DocFlow 2.10.38, 21 października 2026; osobno sprawdź wersje i uprawnienia swojej organizacji.

### `run_workflow` · v2

Identyfikacja: `bb773bc7-b258-49b9-b0e9-b1c28ac227cb`

| Parametr | Typ / opcje | Przykład |
| --- | --- | --- |
| `hidden_workflow_id` | `hidden_workflow_id` | `"MANAGED_BY_DESIGNER"` |
| `workflow` | `workflow:str` | `"YOUR_TARGET_WORKFLOW_ID"` |

## Biznesowe przypadki testowe

| Przypadek | Wejście / konfiguracja | Oczekiwany wynik |
| --- | --- | --- |
| CHILD-01 | enabled=false; workflow=VALID_ID | call=success |
| CHILD-02 | caller_id=target_id | error |
| CHILD-03 | workflow=UNKNOWN_ID | error |
| CHILD-04 | Advanced target=failed_condition | wywołanie może się udać; sprawdź cel |

## Dowody i ograniczenia

Wybrane wyniki kart i węzłów sprawdzono na danych syntetycznych w Advanced Test. Odpowiedzi są w pakiecie. Działania dokumentalne są symulowane i nie dowodzą zapisanego wykonania ani zewnętrznego dostarczenia.

[Dalsza nauka](../workflow-learning-path.md) · [Pakiet ćwiczeń](../workflow-training-kit.md)
