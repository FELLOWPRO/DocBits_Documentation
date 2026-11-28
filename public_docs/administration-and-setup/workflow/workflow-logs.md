# Dzienniki przepływów pracy

Objaśnienia w formie narracji do widoku zaawansowanych dzienników znajdziesz w rozdziałach [Znajdź właściwe wykonanie](advanced-workflow-builder/videos.md#find-the-relevant-execution) i [Śledź węzły i diagnozuj](advanced-workflow-builder/videos.md#trace-nodes-and-diagnose). Oba rozdziały są dostępne w języku angielskim i niemieckim, wraz z plikami napisów i transkrypcjami.

## **Przegląd**

Funkcja **Dzienniki przepływów pracy** pozwala użytkownikom analizować, które przepływy pracy zostały wykonane dla dokumentu, zrozumieć wyniki wykonania oraz zagłębić się w szczegóły na poziomie warunków w celu debugowania lub walidacji.

## **Dostęp do dzienników przepływów pracy**

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.mp4" %}

**Film:** Czytanie dzienników przepływów pracy · 1:34 · [Captions (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.vtt)

<details>

<summary>Transkrypcja</summary>

**Otwórz dzienniki przepływów pracy** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.mp4#t=0.25)

Każdy dokument przechowuje dzienniki przepływów pracy, które zostały na nim uruchomione. W widoku **Dashboard** otwórz akcje dokumentu i wybierz Workflow Logs.

**Przebiegi i ich wyniki** · [0:12](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.mp4#t=12.15)

U góry widzisz, ile było przebiegów i ile zakończyło się błędem, niespełnionym warunkiem lub sukcesem. Poniżej każdy przebieg jest wymieniony wraz z jego przepływem pracy, znacznikiem czasu, czasem trwania i wynikiem.

**Ścieżka jednego przebiegu** · [0:25](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.mp4#t=25.716)

Przeciągnij separator w lewo, aby dać dziennikom więcej miejsca. Następnie kliknij przebieg, aby zobaczyć ścieżkę, którą przeszedł. Każda karta pokazuje swój wynik: zielony oznacza sukces, pomarańczowy niespełniony warunek, czerwony błąd. Tutaj karta And zakończyła się niespełnionym warunkiem, więc karta Then za nią się nie wykonała.

**Dlaczego karta zakończyła się w ten sposób** · [0:45](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.mp4#t=45.35)

Wybierz kartę, aby przeczytać jej dziennik. Mówi on, co karta porównała i dlaczego zakończyła się w ten sposób. Tutaj dokument jest gotowy do walidacji, ale karta oczekuje drugiej akceptacji w toku.

**Błąd i jego przyczyna** · [0:58](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.mp4#t=58.283)

Przebieg, który kończy się błędem, pokazuje kartę, która zawiodła, na czerwono. Tutaj karta And nie mogła odczytać adresu dostawy z dokumentu. Brakujące dane to zawsze błąd, więc karta Then za nią się nie wykonała.

**Znajdź przebiegi** · [1:13](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.mp4#t=73.216)

Przy wielu przebiegach użyj wyszukiwania, aby znaleźć przepływ pracy po nazwie, oraz przycisku filtra, aby zawęzić listę według statusu lub daty.

**Uwaga o limicie wykonania** · [1:23](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.mp4#t=83.116)

Uwaga u góry pojawia się, gdy przepływ pracy osiągnął swój limit wykonania dla tego dokumentu. Wyjaśnia to film o limitach wykonania.

</details>

Aby uzyskać dostęp do dzienników przepływów pracy:

1. Przejdź do **Dashboard**.
2. Kliknij **Actions menu** (ikona trzech kropek) obok wybranego dokumentu.
3. Wybierz **Workflow Logs** z menu.
   * <mark style="color:red;">**Note**</mark>: Funkcja Workflow musi być włączona, aby uzyskać dostęp do tej opcji.
4.  Otwiera się **side panel** z podsumowaniem wykonanych przepływów pracy.\\

    <div align="left"><figure><img src="../../.gitbook/assets/image (5).png" alt="Dashboard with the workflow logs side panel showing summary counters and a table of executed workflows with result icons" width="563"><figcaption></figcaption></figure></div>

## **Otwórz dziennik jako osobną stronę**

Side panel zasłania listę dokumentów. Jeśli przez dłuższy czas analizujesz przepływ pracy dla jakiegoś dokumentu, otwórz ten sam dziennik jako pełną stronę: wybierz ikonę nowego okna w nagłówku panelu. Strona ma adres `/workflows/logs/<document id>`, więc możesz trzymać ją otwartą w drugim oknie przeglądarki lub wysłać ten adres współpracownikowi, który ma dostęp do dokumentu.

Strona pokazuje te same liczniki podsumowania, tę samą tabelę wykonanych przepływów pracy i ten sam widok szczegółów co panel.

## **Przełącz się na inny dokument**

Na pełnej stronie pole wyszukiwania nad listą znajduje dokument po nazwie lub po jego identyfikatorze. Wyniki pokazują datę przesłania, osobę odpowiedzialną i status każdego dokumentu, dzięki czemu odróżnisz dokumenty o podobnych nazwach. Wybranie wyniku wczytuje dziennik przepływu pracy tego dokumentu i umieszcza dokument w adresie. Wyszukiwanie obejmuje dokumenty Twojej organizacji, które możesz zobaczyć zgodnie ze swoimi uprawnieniami; gdy nic nie pasuje, DocBits informuje o tym pod polem zamiast pokazywać pustą listę.

## **Elementy panelu dzienników przepływów pracy**

#### **1. Liczniki podsumowania przepływów pracy**

Znajdują się na górze panelu dzienników:

* **Niebieski**: Łączna liczba wykonanych przepływów pracy.
* **Czerwony**: Przepływy pracy, które zakończyły się **błędami**.
* **Żółty**: Przepływy pracy, które **nie zostały zakończone** z powodu niezgodności warunków.
* **Zielony**: Przepływy pracy **wykonane** pomyślnie.

#### **2. Tabela wykonania przepływów pracy**

Każdy wiersz tabeli reprezentuje jedno wykonanie przepływu pracy i zawiera:

* **Workflow Name**
* **Timestamp** (Created On)
* **Runtime** (w sekundach)
* **Result Icon**:
  * Zielony znak zaznaczenia: Przepływ pracy został wykonany pomyślnie.
  * Czerwony krzyżyk: Przepływ pracy został wykonany z błędem.
  * Pomarańczowy myślnik: Wykonanie zostało zatrzymane, ponieważ warunek nie został spełniony

Kliknięcie **strzałki** po lewej stronie każdego wiersza rozwija **widok szczegółów przepływu pracy**.

<div align="left"><figure><img src="../../.gitbook/assets/workflow_test9_match_check_overview.png" alt="Expanded workflow log row showing When and And condition cards with green checks and a grayed card that was not met, plus card logs" width="563"><figcaption></figcaption></figure></div>

### **Widok szczegółów przepływu pracy**

Kliknięcie konkretnego wiersza przepływu pracy otwiera jego **szczegółowy dziennik wykonania**, pokazujący:

#### **Ocena warunków**

* Blok **When...**: Warunek początkowy.
* Blok(i) **And...**: Dodatkowe warunki.
* Blok(i) **Then...**: Akcje wykonywane, gdy wszystkie warunki są spełnione.

Każda linia warunku pokazuje:

* **Zielone zaznaczenie**: Warunek został spełniony.
* **Pomarańczowy myślnik**: Warunek nie został spełniony.
* **Czerwony krzyżyk**: Warunek nie powiódł się **z powodu błędu**

### **Ważna uwaga o zachowaniu**

Jeśli warunek w przepływie pracy **nie jest spełniony**, system **przestaje oceniać kolejne karty przepływu pracy** w ramach tego przepływu. Takie zachowanie zapobiega niepotrzebnemu przetwarzaniu\
Jako wskaźnik wizualny karta, która **nie spełniła warunku**, jest pokazana na **szaro**, a wszystkie **kolejne karty** w tym samym przepływie również będą wyświetlane na **szaro**, co oznacza, że nie zostały **wykonane**.
