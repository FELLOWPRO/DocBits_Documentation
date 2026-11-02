# Strategia cyklu życia wydań DocBits

Wraz z wdrożeniem nadchodzącego wydania minor R1.1 DocBits wprowadzi nową strategię cyklu życia wydań opartą na dwóch kanałach wydań: VESTA i NOVA.

**NOVA** to kanał służący do wprowadzania nowych wydań major i minor, takich jak **Rx** i **Rx.y**. **VESTA** nadal udostępnia dotychczasowe wydanie produkcyjne.

{% hint style="success" %}
**Ważne: jeden adres URL dla VESTA i NOVA**

Proszę nadal korzystać ze zwykłego adresu URL aplikacji DocBits. VESTA i NOVA nie mają oddzielnych adresów dostępu: oba kanały wydań są dostępne pod tym samym standardowym adresem URL, którego Państwo już używają dla odpowiedniego środowiska.

Aby przełączyć kanał, proszę przejść do **Settings > Company Information > Release Channel** i wybrać **VESTA** lub **NOVA**. Nie ma potrzeby wylogowywania się i ponownego logowania. Następne kliknięcie w aplikacji automatycznie przeniesie Państwa do wydania w wybranym kanale.

Przed przełączeniem proszę sprawdzić, czy oba kanały są gotowe i dostępne w Państwa środowisku, zgodnie z opisem w sekcji [Sprawdź dostępność środowiska przed przełączeniem](#ważne-sprawdź-dostępność-środowiska-przed-przełączeniem).
{% endhint %}

## Kanały wydań

| Kanał | Rola w cyklu życia |
| --- | --- |
| **VESTA** | Udostępnia bieżące wydanie produkcyjne. |
| **NOVA** | Udostępnia kolejne wydanie na etapach rozwoju, testowania i dostępności produkcyjnej. W okresie równoległej produkcji zarówno NOVA, jak i VESTA oferują aktywne wydania produkcyjne. |

## Przegląd cyklu życia

![Trzyfazowy cykl życia wydań DocBits VESTA i NOVA](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/docbits-release-lifecycle-strategy.png)

Każdy cykl składa się z trzech faz. Następnie przejście (rollover) zarządzane przez FELLOWPRO przenosi wydanie produkcyjne NOVA do VESTA i rozpoczyna kolejny cykl.

| Faza | VESTA | NOVA | Co to oznacza dla Państwa organizacji |
| --- | --- | --- | --- |
| **1. Rozwój** | R1.0.x w produkcji | R1.1 w fazie rozwoju | Państwo nadal korzystają z VESTA, podczas gdy przygotowywane jest kolejne wydanie. |
| **2. QA i testy akceptacyjne** | R1.0.x w produkcji | R1.1 w fazie QA i UAT | Mogą Państwo ocenić nadchodzące wydanie w środowisku sandbox NOVA, podczas gdy praca produkcyjna jest kontynuowana w VESTA. |
| **3. Równoległa produkcja** | R1.0.x w produkcji | R1.1.x w produkcji | Mogą Państwo pozostać w VESTA lub samodzielnie przejść na NOVA, gdy będą Państwo gotowi. |

Po przejściu (rollover) wszyscy klienci korzystają z VESTA R1.1.x, a NOVA zostaje ponownie wykorzystana do rozwoju R1.2. Faza 1 rozpoczyna się ponownie z tymi zaktualizowanymi wersjami.

### Faza 1 — Rozwój

VESTA udostępnia bieżące wydanie produkcyjne R1.0.x, podczas gdy kolejne wydanie, R1.1, jest rozwijane w NOVA. Przez całą tę fazę Państwa organizacja kontynuuje codzienną pracę w VESTA.

### Faza 2 — QA i testy akceptacyjne

Nadchodzące wydanie NOVA przechodzi przez zapewnienie jakości (QA) oraz testy akceptacyjne użytkowników (UAT). Mogą Państwo ocenić je w środowisku sandbox NOVA, aby sprawdzić, jak zmiany wpisują się w procesy Państwa organizacji, i przygotować się do wdrożenia.

W tej fazie wydaniem produkcyjnym pozostaje VESTA R1.0.x. Mogą Państwo przejść na NOVA do użytku produkcyjnego, gdy stanie się ona dostępna w Fazie 3.

### Faza 3 — Równoległa produkcja

VESTA R1.0.x i NOVA R1.1.x są jednocześnie aktywnymi wydaniami produkcyjnymi. Państwa organizacja decyduje, czy i kiedy przejść na NOVA, w oparciu o swoje potrzeby i wyniki oceny w środowisku sandbox.

Aby wdrożyć NOVA w tej fazie:

1. Proszę ocenić wydanie w środowisku sandbox NOVA.
2. Proszę sprawdzić ogłoszenie o wydaniu lub potwierdzić z FELLOWPRO Support, że oba środowiska produkcyjne są gotowe i dostępne do przełączania.
3. Proszę zdecydować, kiedy Państwa organizacja będzie gotowa do korzystania z nowego wydania w produkcji.
4. W DocBits proszę przejść do **Settings > Company Information > Release Channel** i wybrać **NOVA**.

W okresie równoległej produkcji mogą Państwo również wrócić do VESTA, przechodząc do **Settings > Company Information > Release Channel** i wybierając **VESTA**.

Przełączanie kanałów odbywa się samodzielnie (self-service). FELLOWPRO nie wybiera, którzy klienci powinni przejść na NOVA. Mogą Państwo korzystać z VESTA przez cały okres równoległej produkcji i przyjąć nowe wydanie w ramach następującego po nim przejścia (rollover).

## Przejście wydania (rollover) i kolejny cykl

FELLOWPRO przeprowadza przejście (rollover), gdy wydanie NOVA jest gotowe, aby stać się wspólnym wydaniem produkcyjnym, a wszyscy klienci zaakceptowali planowaną zmianę:

**NOVA R1.1.x → VESTA R1.1.x**

### Wcześniejsze ogłoszenie i akceptacja klientów

FELLOWPRO z wyprzedzeniem ogłasza planowane przejście wszystkim klientom drogą e-mailową i prosi o akceptację tej zmiany. Zachęcamy Państwa do kontaktu z FELLOWPRO w przypadku jakichkolwiek wątpliwości lub zastrzeżeń, aby można je było omówić przed przejściem. Przejście oraz ponowne wykorzystanie NOVA następują dopiero wtedy, gdy wydanie jest gotowe, a wszyscy klienci zaakceptowali planowaną zmianę.

### Co zmienia się w momencie przejścia

| Zmiana | Rezultat |
| --- | --- |
| **Wydanie NOVA staje się wydaniem VESTA** | R1.1.x staje się wspólnym wydaniem produkcyjnym w VESTA dla wszystkich klientów. |
| **Poprzednie wydanie zostaje wycofane** | R1.0.x zostaje wyłączone z eksploatacji i nie jest już dostępne w żadnym z kanałów ani w jakikolwiek inny sposób. |
| **NOVA zostaje ponownie wykorzystana dla kolejnego wydania** | W NOVA rozpoczyna się rozwój R1.2, co otwiera Fazę 1 kolejnego cyklu. |

Te same trzy fazy powtarzają się następnie z nowymi numerami wersji.

Poniższy diagram przedstawia opisany powyżej cykl wydań bardziej szczegółowo.

![Szczegółowy cykl wydań DocBits VESTA i NOVA](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/docbits-release-lifecycle-strategy-details.png)

### Częstotliwość wydań

Planowana częstotliwość różni się w przypadku wydań major i minor wprowadzanych przez NOVA oraz hotfixów stosowanych w wydaniach produkcyjnych w VESTA i NOVA.

#### Wydania major i minor przez NOVA

FELLOWPRO obecnie planuje cykl trwający około **3–4 miesięcy dla wydań major i minor** wprowadzanych przez kanał wydań NOVA, takich jak **Rx** i **Rx.y**. To szacunkowe założenie dotyczy opisanego powyżej cyklu życia wydań, w tym następującego po nim przejścia (rollover) do VESTA oraz ponownego wykorzystania NOVA dla kolejnego wydania. Nie określa ono częstotliwości hotfixów.

Ten okres odzwierciedla nasze aktualne szacunki planistyczne; nie jest to stały harmonogram, maksymalny czas trwania cyklu ani gwarancja terminu wydania lub przejścia. Termin każdego przejścia oraz ponownego wykorzystania NOVA zależy zarówno od **gotowości wydania, jak i akceptacji planowanej zmiany przez wszystkich klientów**. Jeśli potrzebny będzie dodatkowy czas na osiągnięcie gotowości wydania, rozwiązanie wątpliwości klientów lub uzyskanie akceptacji od każdego klienta, cykl zostanie wydłużony i może trwać dłużej niż cztery miesiące.

FELLOWPRO informuje z wyprzedzeniem o każdym planowanym przejściu. Wszelkie orientacyjne terminy obowiązują pod warunkiem spełnienia tych warunków.

#### Hotfixy w produkcji VESTA

Hotfixy dla wydania produkcyjnego VESTA są oczekiwane mniej więcej **raz w miesiącu lub w nieco dłuższych odstępach**. Jest to orientacyjna częstotliwość, a nie stały harmonogram ani gwarantowany termin dostarczenia.

#### Hotfixy stabilizacyjne w produkcji NOVA

Dla hotfixów stabilizacyjnych w produkcji NOVA nie można określić ogólnej częstotliwości. NOVA wprowadza zupełnie nowe wydania, dlatego termin i częstotliwość tych hotfixów zależą od potrzeb stabilizacyjnych danego wydania. Nie podlegają więc orientacyjnej miesięcznej częstotliwości dla VESTA ani 3–4-miesięcznemu cyklowi dla wydań major i minor.

## Zakres odpowiedzialności i wybór klienta

| Zmiana | Kto nią zarządza | Czego się spodziewać |
| --- | --- | --- |
| **Przełączanie między VESTA a NOVA w Fazie 3** | Państwa organizacja | Proszę ocenić NOVA w środowisku sandbox i zdecydować, czy i kiedy przełączyć. Aby wybrać NOVA lub wrócić do VESTA w okresie równoległej produkcji, proszę użyć **Settings > Company Information > Release Channel**. |
| **Przejście (rollover) NOVA R1.1.x do VESTA R1.1.x** | FELLOWPRO | Zapoznanie się z wcześniejszym ogłoszeniem e-mailowym, zgłoszenie ewentualnych wątpliwości lub zastrzeżeń oraz potwierdzenie akceptacji planowanej zmiany. FELLOWPRO przeprowadza przejście, gdy wydanie jest gotowe, a wszyscy klienci wyrazili akceptację. |

## Ważne: sprawdź dostępność środowiska przed przełączeniem

Przełączać się między VESTA a NOVA za pomocą **Settings > Company Information > Release Channel** należy tylko wtedy, gdy wydania są dostępne równolegle i gotowe do użycia w **odpowiednim środowisku w obu kanałach**. Dostępność sandbox i produkcji należy oceniać oddzielnie:

- **Sandbox:** Mogą Państwo przełączyć się z VESTA Sandbox na NOVA Sandbox, gdy nowe wydanie jest gotowe i dostępne w NOVA Sandbox, a VESTA Sandbox pozostaje dostępny. To samo wymaganie gotowości dotyczy powrotu.
- **Produkcja:** Mogą Państwo przełączać się między VESTA Production a NOVA Production tylko wtedy, gdy oba wydania produkcyjne są gotowe i dostępne równolegle. Dostępność w NOVA Sandbox nie oznacza, że NOVA Production jest gotowa do użycia.

Przełączenie, gdy odpowiednie środowisko nie jest gotowe lub dostępne, może zakłócić Państwa działalność. FELLOWPRO wysyła e-maile z ogłoszeniami o wydaniach na kilka dni przed udostępnieniem wydań w środowisku sandbox lub produkcyjnym. Proszę sprawdzić te ogłoszenia przed przełączeniem. Jeśli nie są Państwo pewni, czy przełączenie jest dostępne lub odpowiednie dla Państwa organizacji, proszę skontaktować się z FELLOWPRO Support w celu potwierdzenia.

**Planowana kontrola dostępności:** FELLOWPRO pracuje nad kontrolką Tak/Nie, która umożliwi Support ustawienie Release Channel jako tylko do odczytu lub włączenie przełączania kanałów niezależnie od wdrożenia oprogramowania. Gdy kontrolka będzie dostępna, Support będzie jej używać, aby włączać przełączanie, gdy odpowiednie środowiska są gotowe, a w pozostałych przypadkach pozostawiać ustawienie tylko do odczytu. Ma to umożliwić klientom bezpieczne przełączanie się między VESTA a NOVA, gdy ustawienie jest włączone. Do czasu wprowadzenia tej kontrolki sama edytowalność ustawienia nie powinna być traktowana jako potwierdzenie, że przełączenie jest właściwe; proszę kierować się ogłoszeniami o wydaniach lub potwierdzić to z Support.

## Najczęściej zadawane pytania

### Skąd wiemy, czy bezpiecznie jest przełączyć się między VESTA a NOVA?

Proszę sprawdzić ogłoszenie o wydaniu dla środowiska, z którego zamierzają Państwo korzystać, lub poprosić FELLOWPRO Support o potwierdzenie, że przełączenie jest właściwe. Oba odpowiednie środowiska muszą być gotowe i dostępne równolegle; gotowość sandbox nie potwierdza gotowości produkcji. Pełne wskazówki, w tym informacje o planowanej kontrolce włączania lub wyłączania przełączania kanałów, znajdą Państwo powyżej w sekcji [Ważne: sprawdź dostępność środowiska przed przełączeniem](#ważne-sprawdź-dostępność-środowiska-przed-przełączeniem).

### Czy możemy pozostać w VESTA, gdy NOVA jest dostępna w produkcji?

Tak. W Fazie 3 mogą Państwo pozostać w VESTA lub przejść na NOVA, gdy Państwa organizacja będzie gotowa. Przy następującym po tym przejściu (rollover) nowe wydanie staje się VESTA, a poprzednie wydanie zostaje wycofane.

### Jak przełączyć się na NOVA lub wrócić do VESTA?

Najpierw proszę sprawdzić, czy odpowiednie środowisko jest gotowe i dostępne w obu kanałach, zgodnie z opisem w sekcji [Sprawdź dostępność środowiska przed przełączeniem](#ważne-sprawdź-dostępność-środowiska-przed-przełączeniem). Dostępność sandbox i dostępność produkcji są od siebie niezależne.

W Fazie 3 proszę przejść w DocBits do **Settings > Company Information > Release Channel** i wybrać **NOVA**, aby wdrożyć nowe wydanie produkcyjne, lub **VESTA**, aby wrócić do bieżącego wydania produkcyjnego VESTA. Państwa organizacja podejmuje tę decyzję samodzielnie, w oparciu o swoje potrzeby i ocenę NOVA w środowisku sandbox. Wybór ten obowiązuje, dopóki oba wydania są dostępne równolegle; poprzednie wydanie VESTA zostaje wycofane w momencie przejścia (rollover).

### Kiedy NOVA jest dostępna do użytku produkcyjnego?

NOVA staje się aktywnym wydaniem produkcyjnym w Fazie 3, po etapach rozwoju oraz QA/UAT. W tej fazie VESTA i NOVA działają w produkcji równolegle, z różnymi wersjami oprogramowania.

### Jak dowiemy się o przejściu i czy możemy zgłosić zastrzeżenia?

FELLOWPRO z wyprzedzeniem wysyła wiadomość e-mail do wszystkich klientów i prosi o akceptację planowanej zmiany. Zachęcamy Państwa do zgłaszania FELLOWPRO wszelkich wątpliwości lub zastrzeżeń. Przejście oraz ponowne wykorzystanie NOVA następują dopiero wtedy, gdy wydanie jest gotowe, a akceptacja została uzyskana od wszystkich klientów.

### Czy możemy nadal korzystać z R1.0.x po przejściu?

Nie. R1.0.x zostaje wyłączone z eksploatacji w momencie przejścia i nie jest już dostępne w żadnym z kanałów ani w jakikolwiek inny sposób. R1.1.x staje się wspólnym wydaniem produkcyjnym VESTA dla wszystkich klientów.

### Czym przejście (rollover) różni się od naszego przejścia na NOVA?

Państwa przejście na NOVA w Fazie 3 to samodzielna decyzja (self-service) o tym, kiedy wdrożyć nowe wydanie produkcyjne. Rollover to następująca później zmiana zarządzana przez FELLOWPRO: NOVA R1.1.x staje się VESTA R1.1.x, poprzednie wydanie zostaje wycofane i rozpoczyna się kolejny cykl.

### Co dzieje się z NOVA po przejściu?

NOVA zostaje ponownie wykorzystana do rozwoju kolejnego wydania, w tym przykładzie R1.2. VESTA udostępnia R1.1.x, podczas gdy NOVA ponownie przechodzi przez etapy rozwoju, QA/UAT i równoległej produkcji.

### Czy wydanie major lub minor jest gwarantowane co trzy do czterech miesięcy?

Nie. Przybliżona częstotliwość 3–4 miesięcy dla wydań major i minor wprowadzanych przez NOVA to aktualne szacunki planistyczne, a nie gwarantowany harmonogram ani maksymalny czas trwania. Przejście oraz ponowne wykorzystanie NOVA wymagają zarówno gotowości wydania, jak i akceptacji wszystkich klientów. Jeśli którykolwiek z tych warunków będzie wymagał więcej czasu, cykl zostanie wydłużony i może przekroczyć cztery miesiące. FELLOWPRO informuje z wyprzedzeniem o każdym planowanym przejściu.
