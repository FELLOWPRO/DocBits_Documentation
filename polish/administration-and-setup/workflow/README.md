---
description: DocBits Workflow Engine
---

# Workflow

<figure><img src="../../.gitbook/assets/Bildschirmfoto 2024-03-12 um 19.42.57.png" alt=""><figcaption></figcaption></figure>

## DocBits Workflow Engine: uproszczona automatyzacja procesów

### Zrozumienie i przygotowanie przepływów pracy <a id="workflow-orientation"></a>

Zobacz prawdziwe konto testowe DocBits: osiem wykonań w panelu, dwa zapisane workflow z kolejnością wykonania 100/200 i trzy zaliczone scenariusze testowe. Samouczek wyjaśnia również workflow Standard i Advanced, licencje, szablony oraz Card SDK.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/pl.mp4" %}

[Oglądaj z napisami](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/pl.html) · [Otwórz film](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/pl.mp4) · [Napisy (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/pl.vtt) · [Transkrypcja](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/pl.txt) · 3:04

<details>
<summary>Rozdziały i transkrypcja</summary>

| Rozdział | Początek |
| --- | --- |
| Poznaj administratora | [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/pl.mp4#t=0.000) |
| Organizacja i dostęp | [0:01](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/pl.mp4#t=1.875) |
| Panel i filtry | [0:13](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/pl.mp4#t=13.792) |
| Lista workflow | [0:50](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/pl.mp4#t=50.750) |
| Kolejność wykonania | [1:04](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/pl.mp4#t=64.458) |
| Standard Workflow | [1:21](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/pl.mp4#t=81.750) |
| Advanced Workflow | [1:33](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/pl.mp4#t=93.458) |
| Licencje | [1:50](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/pl.mp4#t=110.250) |
| Szablony | [2:08](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/pl.mp4#t=128.750) |
| Test Manager | [2:22](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/pl.mp4#t=142.458) |
| Card SDK | [2:35](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/pl.mp4#t=155.833) |
| Sprawdzenie przygotowania | [2:50](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/pl.mp4#t=170.167) |

**Poznaj administratora**

Zarządzam DocBits.

**Organizacja i dostęp**

Dobrze, najpierw sprawdzam organizację widoczną u góry. Te ustawienia workflow dotyczą wybranej organizacji. W tej demonstracji korzystam z konta testowego dokumentacji.

**Panel i filtry**

Panel workflow daje ogólny obraz. Do tego widoku uruchomiłem ręcznie dwa szkoleniowe przepływy pracy osiem razy na przykładowej fakturze. Tutaj widzę osiem uruchomień łącznie, w tym sześć zakończonych sukcesem. W dwóch uruchomieniach warunek kwoty nie został spełniony. Wskaźnik sukcesu uwzględnia również te poprawnie zakończone kontrole. Filtruję według nazwy przepływu i sprawdzam zakres dat. Liczniki i wykres zmieniają się zgodnie z wyborem. Po prawej przełączam zapisane przepływy i scenariusze testowe. Uruchomienia w Test Managerze są liczone osobno.

**Lista workflow**

Na liście zarządzam poszczególnymi workflow. Sprawdzam nazwę, typ Standard lub Advanced, kolejność wykonania, wyzwalacz i dostępne działania. Przed utworzeniem kolejnego szukam istniejącego workflow.

**Kolejność wykonania**

Kolejność wykonania ma znaczenie, gdy kilka workflow przetwarza ten sam dokument. Sprawdzam, który powinien działać pierwszy i jakich danych potrzebuje następny. Tutaj kontrola faktury ma kolejność sto, a następna kontrola dwieście. Niższe wartości są wykonywane wcześniej.

**Standard Workflow**

Dla reguły liniowej wybieram Standard Workflow. Kiedy określa wyzwalacz, I dodaje warunki, a Wtedy wykonuje działania. Biblioteka zawiera dostępne karty.

**Advanced Workflow**

Dla alternatywnych ścieżek używam Advanced Workflow. Ten podgląd projektanta pokazuje Start i jawne połączenia. Sukces, niespełniony warunek oraz błąd mogą prowadzić różnymi drogami. Położenie kart nie określa kolejności.

**Licencje**

W zakładce Licencja osobno sprawdzam Workflow i Advanced Workflow. Tutaj obie opcje są nieaktywne. Okno planów pokazuje dostępne subskrypcje. Zamykam ten podgląd bez zmian. Otwarcie projektanta nie uruchamia silnika.

**Szablony**

Szablony pozwalają ponownie wykorzystać punkt wyjścia. Otwieram bibliotekę oraz opcję domyślnych szablonów. Nadal sprawdzam pola, odbiorców i działania dla własnego procesu.

**Test Manager**

Test Manager przechowuje zapisane scenariusze dla workflow Standard i Advanced. Po konfiguracji dodaję reprezentatywne dane oraz oczekiwane wyniki. Uruchom wszystkie testy pomaga sprawdzić zmiany.

**Card SDK**

Card SDK służy do własnych rozszerzeń. Programiści mogą użyć szablonu, przesłać pakiet lub zaimportować go z GitHub. Zwykłą administrację zaczynam od istniejącej biblioteki kart.

**Sprawdzenie przygotowania**

Przed budową potwierdzam organizację, dostęp, potrzebną licencję, pola dokumentu i oczekiwany wynik. Decyduję, czy wystarczy reguła liniowa. W następnym filmie tworzymy Standard Workflow krok po kroku.

</details>

### Wprowadzenie

W dziedzinie automatyzacji procesów DocBits Workflow Engine wyróżnia się prostym i intuicyjnym podejściem. Silnik ten usprawnia tworzenie przepływów pracy i zarządzanie nimi dzięki przejrzystej, prostej strukturze opartej na regułach. Główna zasada jego konstrukcji to reguła „Easy When-And-Then”, która dzieli proces automatyzacji na trzy podstawowe elementy: wyzwalacz (Trigger), warunek (Condition) i akcję (Action). Ten przewodnik wyjaśnia, jak każdy z tych elementów działa w systemie i jak współpracują one ze sobą, umożliwiając płynną automatyzację.

### Reguła „Easy When-And-Then” w szczegółach

DocBits Workflow Engine działa w oparciu o prostą, a zarazem potężną zasadę, dzięki której automatyzacja przepływów pracy jest dostępna dla użytkowników na każdym poziomie zaawansowania. Zasada ta jest ujęta w regule „Easy When-And-Then”, którą można rozłożyć w następujący sposób:

#### [When](./#when-wyzwalacz) (Wyzwalacz)

* **Definicja**: Element „When” reprezentuje _wyzwalacz_ przepływu pracy. Jest to zdarzenie lub warunek, który inicjuje wykonanie przepływu pracy. Wyzwalaczem może być wiele zdarzeń, takich jak nadejście nowej wiadomości e-mail, określona data i godzina albo utworzenie nowego dokumentu.
* **Przykład**: „Gdy zostanie przesłany nowy formularz klienta...”

#### [And](./#and-warunek) (Warunek)

* **Definicja**: Element „And” wprowadza _warunek_, który musi zostać spełniony, aby akcja mogła być kontynuowana. Warunki działają jak filtry lub kryteria, które zawężają działanie wyzwalacza, dzięki czemu przepływ pracy jest wykonywany tylko w określonych okolicznościach.
* **Przykład**: „...i klient należy do segmentu „Enterprise”...”

#### [Then](./#then-akcja) (Akcja)

* **Definicja**: Wreszcie część „Then” określa _akcję_, która ma zostać wykonana, gdy wystąpi wyzwalacz i zostanie spełniony warunek. Akcje to zadania lub operacje wykonywane przez przepływ pracy, takie jak wysłanie wiadomości e-mail, aktualizacja bazy danych lub utworzenie zadania w narzędziu do zarządzania projektami.
* **Przykład**: „...wtedy przypisz lead do zespołu sprzedaży korporacyjnej i wyślij wiadomość powitalną.”

### Łączenie elementów w zaawansowane automatyzacje

Łącząc te trzy elementy — wyzwalacz, warunek i akcję — DocBits Workflow Engine pozwala użytkownikom tworzyć wysoce dostosowane i wydajne przepływy pracy. Takie modułowe podejście nie tylko upraszcza konfigurowanie automatyzacji, ale także daje elastyczność w tworzeniu złożonych przepływów pracy, które radzą sobie z szerokim zakresem zadań i procesów.

### Podsumowanie

Reguła „Easy When-And-Then” w DocBits Workflow Engine jest przykładem tego, jak silnik ten dąży do zapewnienia przyjaznej dla użytkownika platformy do automatyzacji procesów. Ta prosta reguła, dzieląc automatyzację na podstawowe elementy wyzwalacza, warunku i akcji, ułatwia użytkownikom zrozumienie, tworzenie i zarządzanie przepływami pracy. Niezależnie od tego, czy dopiero zaczynasz z automatyzacją przepływów pracy, czy jesteś doświadczonym profesjonalistą, DocBits Workflow Engine oferuje wydajne i dostępne narzędzie, które zwiększa produktywność i usprawnia działanie.

## Ścieżka od początkującego do eksperta

[Ścieżka od początkującego do eksperta](workflow-learning-path.md). Przechodź poziomy po kolei. Samo czytanie nie wystarcza: każdy kończy się własną konfiguracją, sprawdzalnym oczekiwaniem i dowodem. P0 zapobiega podstawowym błędom wykonania; P1 rozwija dane, decyzje biznesowe i integracje.
