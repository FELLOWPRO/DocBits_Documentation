# Tolerancje dat

Kilka kart przepływu pracy porównuje datę z datą referencyjną i akceptuje tolerancję wynoszącą określoną liczbę dni. Wszystkie obliczają tolerancję w ten sam sposób. Ta strona wyjaśnia to obliczenie, znaczenie poszczególnych operatorów, działanie pola **Dozwolone dni tolerancji** oraz sposób łączenia dwóch kart dla zakresów takich jak „dziś lub jutro”.

Karty, które korzystają z tego obliczenia:

* [Table Date to Current Date](table/table-date-to-current-date.md) – data w tabeli dokumentu porównywana z bieżącą datą.
* [Promised delivery date for line items in table with promised delivery date](compare-with-purchase-order/promised-delivery-date-for-line-items-in-table-with-promised-delivery-date/README.md) – obiecane daty dostawy pozycji porównywane z bieżącą datą.
* [Promised Delivery Date on Purchase Order](compare-with-purchase-order/promised-delivery-date-on-purchase-order.md) – daty dostawy pozycji porównywane z datą dostawy w zamówieniu zakupu.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/date-tolerances/v1/pl.mp4" %}

**Film:** Tolerancje dat i sprawdzanie zakresów · 2:44 · [Napisy (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/date-tolerances/v1/pl.vtt)

<details>

<summary>Transkrypcja</summary>

**Daty z tolerancją** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/date-tolerances/v1/pl.mp4#t=0.25)

Kilka kart Workflow porównuje datę z datą odniesienia i dopuszcza tolerancję w dniach. Wszystkie liczą tę tolerancję tak samo.

**Okno tolerancji** · [0:14](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/date-tolerances/v1/pl.mp4#t=14.283)

Od daty odniesienia tolerancja jest liczona wstecz i do przodu. Wynikiem jest okno, a oba jego końce do niego należą.

**Dwa dni: od wtorku do soboty** · [0:26](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/date-tolerances/v1/pl.mp4#t=26.65)

Przy dwóch dniach wokół czwartku, dwudziestego drugiego, okno trwa od wtorku, dwudziestego, do soboty, dwudziestego czwartego. Dziś to data na serwerach DocBits, w U T C.

**Sześć operatorów, jedno okno** · [0:46](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/date-tolerances/v1/pl.mp4#t=46.616)

Równa się akceptuje daty w oknie, Różny od daty poza nim. Większy lub równy zaczyna się na początku okna, Większy niż po jego końcu. Mniejszy lub równy oraz Mniejszy niż działają odwrotnie.

**Operator, dni i dni tygodnia** · [1:05](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/date-tolerances/v1/pl.mp4#t=65.45)

W karcie wybierz operator, tolerancję w dniach i liczone dni tygodnia.

**Liczą się tylko wybrane dni tygodnia** · [1:19](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/date-tolerances/v1/pl.mp4#t=79.05)

Dozwolone dni tolerancji liczą tylko wybrane dni tygodnia. Przy dniach od poniedziałku do piątku jeden dzień po piątku to poniedziałek, więc okno trwa od czwartku do poniedziałku.

**Zakresy wymagają dwóch kart** · [1:35](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/date-tolerances/v1/pl.mp4#t=95.016)

Jedna karta nie zaakceptuje dokładnie dziś lub jutro, bo jej okno sięga równie daleko w obie strony. Dwie karty, jedna po drugiej, to potrafią.

**Równa się 1 dzień, potem Większy lub równy 0 dni** · [1:50](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/date-tolerances/v1/pl.mp4#t=110.583)

Pierwsza karta, Równa się z jednym dniem, akceptuje wczoraj, dziś i jutro. Druga, Większy lub równy z zerem dni, akceptuje dziś i każdy późniejszy dzień. Przez obie przechodzą tylko dziś i jutro.

**Wyklucz dzień przez Różny od** · [2:09](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/date-tolerances/v1/pl.mp4#t=129.35)

Aby pominąć jeden dzień, dodaj kartę Różny od z zerem dni. Tutaj Równa się z trzema dniami i Większy lub równy z zerem dni dają dziś do trzech dni naprzód, a Różny od usuwa dziś.

**Trzy karty, jeden zakres** · [2:28](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/date-tolerances/v1/pl.mp4#t=148.583)

W projektancie trzy karty następują po sobie na ścieżce sukcesu. Workflow idzie dalej tylko, gdy wszystkie trzy dadzą sukces: od jutra do trzech dni naprzód.

</details>

## Okno tolerancji

Od daty referencyjnej tolerancja jest odliczana do tyłu i do przodu. Wynikiem jest **okno tolerancji**: od daty początkowej do daty końcowej, obie włącznie.

* Przy tolerancji **0 dni** okno obejmuje tylko samą datę referencyjną.
* Przy tolerancji **2 dni** okno sięga 2 dni przed datą referencyjną i 2 dni po niej.
* **Bieżąca data** to data na serwerach DocBits, które działają w **UTC**.

Każdy operator porównuje datę z tym oknem:

| Operator | Prawda, gdy data jest … |
|---|---|
| **Równa się** | wewnątrz okna |
| **Nie równe** | poza oknem |
| **Większy lub równy** | w dniu **początku** okna lub później |
| **Większy niż** | po **końcu** okna |
| **Mniej lub Równe** | w dniu **końca** okna lub wcześniej |
| **Mniej niż** | przed **początkiem** okna |

Warto zauważyć, że tolerancja poszerza również **Większy lub równy** i **Mniej lub Równe**: przy 2 dniach **Większy lub równy** akceptuje już datę 2 dni przed datą referencyjną.

<figure><img src="../../../.gitbook/assets/date-tolerance-operators-pl-pl.png" alt="Okno tolerancji 2 dni wokół czwartku i dni akceptowane przez poszczególne operatory"><figcaption><p>Data referencyjna czwartek 22, tolerancja 2 dni: okno trwa od wtorku 20 do soboty 24.</p></figcaption></figure>

## Dozwolone dni tolerancji

Karty oferujące pole **Dozwolone dni tolerancji** przy obliczaniu okna liczą tylko wybrane dni tygodnia. Niewybrane dni tygodnia są pomijane przy liczeniu, ale pozostają wewnątrz okna.

**Przykład:** data referencyjna piątek, tolerancja 1 dzień, wybrane tylko dni od poniedziałku do piątku. Odliczanie do tyłu dochodzi do czwartku. Odliczanie do przodu pomija sobotę i niedzielę i dochodzi do poniedziałku. Okno obejmuje **od czwartku do poniedziałku**.

**Table Date to Current Date** dodaje jeszcze jedną kontrolę: data w tabeli powinna również przypadać na jeden z wybranych dni tygodnia. Sobota wewnątrz okna nie jest więc akceptowana przez tę kartę. Dwie pozostałe karty nie mają tej dodatkowej kontroli.

<figure><img src="../../../.gitbook/assets/date-tolerance-weekdays-pl-pl.png" alt="Okno 1 dnia wokół piątku, w którym liczone są tylko dni od poniedziałku do piątku"><figcaption><p>Liczone są tylko dni od poniedziałku do piątku, więc 1 dzień po piątku to poniedziałek.</p></figcaption></figure>

## Przykład: dziś lub jutro

Pojedyncza karta nie może akceptować dokładnie zakresu „dziś lub jutro”, ponieważ okno zawsze sięga tej samej liczby dni w obu kierunkach. Mogą to zrobić dwie karty umieszczone jedna po drugiej:

1. **Równa się** z tolerancją **1 dzień** akceptuje wczoraj, dziś i jutro.
2. **Większy lub równy** z tolerancją **0 dni** akceptuje dziś i każdy późniejszy dzień.

Pozostają tylko daty, które przechodzą przez obie karty: **dziś i jutro**.

<figure><img src="../../../.gitbook/assets/date-tolerance-today-or-tomorrow-pl-pl.png" alt="Równa się z 1 dniem i Większy lub równy z 0 dni, razem akceptujące dziś i jutro"><figcaption><p>Dziś jest czwartek 22: razem obie karty akceptują czwartek 22 i piątek 23.</p></figcaption></figure>

W ten sam sposób można tworzyć inne zakresy:

| Zakres | Pierwsza karta | Druga karta |
|---|---|---|
| Dziś lub jutro | **Równa się**, 1 dzień | **Większy lub równy**, 0 dni |
| Wczoraj lub dziś | **Równa się**, 1 dzień | **Mniej lub Równe**, 0 dni |
| Od dziś do 3 dni naprzód | **Równa się**, 3 dni | **Większy lub równy**, 0 dni |
| Nie dziś | **Nie równe**, 0 dni | – |
| Od pojutrza | **Większy niż**, 1 dzień | – |

Gdy jako **Dozwolone dni tolerancji** wybrano tylko dni od poniedziałku do piątku, „jutro” w piątek oznacza następny poniedziałek.

## Podsumowanie

Wszystkie karty dat z tolerancją używają jednego okna wokół daty referencyjnej. Znajomość początku i końca okna pozwala jasno określić, co akceptuje każdy operator, a dwie karty razem mogą obejmować zakresy, których pojedyncza karta nie obejmuje.
