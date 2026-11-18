# Przypisz do grupy

<figure><img src="../../../../.gitbook/assets/workflow_card_doc_group_assign_v2-pl-pl.png" alt="Przypisz do grupy, Wersja 2" width="634"><figcaption><p>Wersja 2</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/workflow_card_doc_group_assign_v3-pl-pl.png" alt="Przypisz do grupy, Wersja 3" width="634"><figcaption><p>Wersja 3</p></figcaption></figure>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-assign-group/v1/pl.mp4" %}

**Film:** Karta: Przypisz dokument do grupy · 1:00 · [Napisy (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-assign-group/v1/pl.vtt)

<details>

<summary>Transkrypcja</summary>

**Przypisz dokument do grupy** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-assign-group/v1/pl.mp4#t=0.25)

Karta Przypisz do grupy daje dokument grupie: wybierz grupę, na przykład Accounts payable. Wersja trzecia, wybrana etykietą wersji, dodaje drugie ustawienie: czy zamiast tego grupę może wybrać tabela decyzyjna.

**Drzewo decyzyjne: najpierw grupa z tabeli** · [0:23](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-assign-group/v1/pl.mp4#t=23.05)

Gdy drzewo decyzyjne jest włączone, karta bierze grupę, którą zwróciła karta tabeli decyzyjnej wcześniej w Workflow. Jeśli tabela nie zwróciła grupy, dokument dostaje grupa z karty. Wersja druga zawsze przypisuje grupę z karty.

**Przykład: grupa z tabeli, zapas na karcie** · [0:44](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-assign-group/v1/pl.mp4#t=44.55)

Na przykład tabela decyzyjna zwraca grupę dla dostawcy, a karta przypisania jej używa. Gdy tabela nie znajdzie grupy, fakturę dostaje Accounts payable.

</details>

## Cel:

Karta przepływu pracy **"Assign to Group"** ułatwia przypisywanie dokumentów do określonej **grupy** w systemie. Zapewnia to, że dokument jest przetwarzany przez odpowiedni zespół, usprawniając przepływ pracy. Rozszerzona w późniejszych wersjach, wprowadza funkcjonalność drzewa decyzyjnego do dynamicznego przypisywania grup.

## Komponenty karty:

1. **Grupy**
   * **Opis:** Określa **grupę**, do której zostanie przypisany dokument.
   * **Szczegóły:** Wybierana z listy rozwijanej dostępnych **grup**.

## **Dodatkowe komponenty w Version 3**

1. **Decision Tree (tylko Version 3)**
   * **Opis:** Umożliwia użycie drzewa decyzyjnego do dynamicznego określania **grupy**, do której powinien zostać przypisany dokument.
   * **Opcje:**
     * **True:** Włącza przetwarzanie drzewa decyzyjnego.
     * **False:** Wyłącza przetwarzanie drzewa decyzyjnego.

## Funkcjonalność:

* **Ocena warunku:** Karta wykonuje swoją akcję tylko wtedy, gdy zarówno **„Kiedy”**, jak i **„I sekcje”** są prawdziwe.
* **Przypisanie dokumentu:** Przypisuje dokument do wybranej **grupy**. W **Wersja 3** **drzewo decyzyjne** dynamicznie określa grupę docelową, jeśli jest włączone.

## Konfiguracja:

* **Wybierz grupę:** Wybierz **grupę** z listy rozwijanej, aby przypisać dokument.
* **Użyj drzewa decyzyjnego (tylko wersja 3):** Włącz tę opcję, jeśli **drzewo decyzyjne** ma być używane do dynamicznego przypisywania.

## Podsumowanie:

Karta przepływu pracy **"Assign to Group"** automatyzuje przypisywanie dokumentów do predefiniowanych **grup**, zwiększając koordynację zespołu. **Wersja 3** wprowadza możliwość dynamicznego przypisywania grup na podstawie logiki drzewa decyzyjnego.

<!-- workflow-card-practical-example-20261021 -->

## Praktyczny przykład

**Kiedy używać:** Umieść dokument w udostępnionej kolejce recenzji.

**Konfiguracja:** Wybierz skonfigurowaną grupę `Demo Finance`.

**Oczekiwany wynik i kontrprzykład:** Dokument jest przypisany do wybranej grupy. To jest przypisanie dokumentu, a nie obietnica utworzenia dodatkowego zadania lub e-maila.

To jest ilustracyjna konfiguracja i oczekiwany wynik. Korzystaj z pól, użytkowników i grup skonfigurowanych w Twojej organizacji testowej; nie jest to twierdzenie, że ten przykład został wykonany.
