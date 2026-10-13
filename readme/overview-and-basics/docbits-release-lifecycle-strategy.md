# Strategia cyklu życia wydań DocBits

DocBits korzysta z dwóch kanałów wydań, **VESTA** i **NOVA**, aby wprowadzać nowe wydania i zapewnić Państwa organizacji czas na ich ocenę przed wdrożeniem. W okresie równoległej produkcji to Państwo decydują, czy i kiedy przejść na nowe wydanie. Następnie FELLOWPRO przeprowadza przejście (rollover), w wyniku którego nowe wydanie staje się wspólnym wydaniem produkcyjnym dla wszystkich klientów.

Numery wersji użyte w tym przewodniku — R1.0.x, R1.1.x i R1.2 — mają charakter przykładowy. Ten sam cykl życia powtarza się w kolejnych wydaniach; `x` oznacza aktualizacje w ramach danej serii wydań.

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
2. Proszę zdecydować, kiedy Państwa organizacja będzie gotowa do korzystania z niego w produkcji.
3. Proszę przejść z VESTA na NOVA za pomocą ustawienia **Release Channel** w aplikacji DocBits.

Przejście to odbywa się samodzielnie (self-service). FELLOWPRO nie wybiera, którzy klienci powinni przejść na NOVA. Mogą Państwo korzystać z VESTA przez cały okres równoległej produkcji i przyjąć nowe wydanie w ramach następującego po nim przejścia (rollover).

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

FELLOWPRO obecnie planuje cykl wydań trwający około **3–4 miesięcy**. Ten okres odzwierciedla nasze aktualne szacunki planistyczne; nie jest to stały harmonogram, maksymalny czas trwania cyklu ani gwarancja terminu wydania lub przejścia.

Termin każdego przejścia oraz ponownego wykorzystania NOVA zależy zarówno od **gotowości wydania, jak i akceptacji planowanej zmiany przez wszystkich klientów**. Jeśli potrzebny będzie dodatkowy czas na osiągnięcie gotowości wydania, rozwiązanie wątpliwości klientów lub uzyskanie akceptacji od każdego klienta, cykl zostanie wydłużony i może trwać dłużej niż cztery miesiące.

FELLOWPRO informuje z wyprzedzeniem o każdym planowanym przejściu. Wszelkie orientacyjne terminy obowiązują pod warunkiem spełnienia tych warunków.

## Zakres odpowiedzialności i wybór klienta

| Zmiana | Kto nią zarządza | Czego się spodziewać |
| --- | --- | --- |
| **Przejście z VESTA na NOVA w Fazie 3** | Państwa organizacja | Ocena NOVA w środowisku sandbox oraz decyzja, czy i kiedy przejść, za pomocą ustawienia Release Channel w aplikacji. |
| **Przejście (rollover) NOVA R1.1.x do VESTA R1.1.x** | FELLOWPRO | Zapoznanie się z wcześniejszym ogłoszeniem e-mailowym, zgłoszenie ewentualnych wątpliwości lub zastrzeżeń oraz potwierdzenie akceptacji planowanej zmiany. FELLOWPRO przeprowadza przejście, gdy wydanie jest gotowe, a wszyscy klienci wyrazili akceptację. |

## Najczęściej zadawane pytania

### Czy możemy pozostać w VESTA, gdy NOVA jest dostępna w produkcji?

Tak. W Fazie 3 mogą Państwo pozostać w VESTA lub przejść na NOVA, gdy Państwa organizacja będzie gotowa. Przy następującym po tym przejściu (rollover) nowe wydanie staje się VESTA, a poprzednie wydanie zostaje wycofane.

### Jak przejść na NOVA?

Gdy NOVA jest dostępna w produkcji, proszę skorzystać z ustawienia **Release Channel** w aplikacji DocBits. Państwa organizacja podejmuje tę decyzję samodzielnie, w oparciu o swoje potrzeby i ocenę wydania w środowisku sandbox NOVA.

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

### Czy nowe wydanie jest gwarantowane co trzy do czterech miesięcy?

Nie. Przybliżona częstotliwość 3–4 miesięcy to aktualne szacunki planistyczne, a nie gwarantowany harmonogram ani maksymalny czas trwania. Przejście oraz ponowne wykorzystanie NOVA wymagają zarówno gotowości wydania, jak i akceptacji wszystkich klientów. Jeśli którykolwiek z tych warunków będzie wymagał więcej czasu, cykl zostanie wydłużony i może przekroczyć cztery miesiące. FELLOWPRO informuje z wyprzedzeniem o każdym planowanym przejściu.
