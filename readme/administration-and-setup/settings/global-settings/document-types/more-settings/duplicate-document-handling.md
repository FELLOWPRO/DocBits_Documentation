# Wykrywanie duplikatów

Funkcja **Wykrywanie duplikatów** oznacza dokumenty, które w wybranym okresie pasują do innego dokumentu według wybranych pól. Opcje te dotyczą każdego typu dokumentu osobno.

## Otwieranie ustawień

1. Otwórz **Ustawienia → Typy dokumentów**.
2. Przy typie dokumentu, który chcesz skonfigurować, wybierz **Ustawienia**.
3. W sekcji **Więcej ustawień** otwórz **Wykrywanie duplikatów**.

<figure><img src="../../../../../.gitbook/assets/dbdc665-duplicate-settings-off-pl-20261011.png" alt="Ustawienia faktury z otwartą sekcją Wykrywanie duplikatów i wyłączonymi przełącznikami wykrywania"><figcaption><p>Ustawienia faktury pokazują cztery osobne przełączniki. Selektory pól i interwału pojawiają się po włączeniu wykrywania.</p></figcaption></figure>

## Wybieranie kryteriów duplikatu

1. Włącz **Wykrywanie duplikatów dokumentów**. Pojawią się selektory **Pola wykrywania duplikatów** i **Interwał wykrywania duplikatów**.
2. Wybierz pola, które muszą się zgadzać. Dla faktury możesz wybrać **ID dostawcy** i **Numer faktury**. Wybierz pola, które odróżniają dokumenty w Twoim procesie.
3. Wybierz interwał: **1 miesiąc**, **3 miesiące (zalecane)**, **6 miesięcy** lub **1 rok**. Dłuższy interwał sprawdza szerszy zakres dat i może wydłużać ładowanie.

Każda zmiana jest zapisywana od razu po jej dokonaniu; w tej sekcji nie ma osobnego przycisku zapisu. Po wyłączeniu wykrywania selektory pól i interwału są ukrywane.

<figure><img src="../../../../../.gitbook/assets/dbdc665-duplicate-settings-on-pl-20261011.png" alt="Wykrywanie duplikatów dokumentów włączone, widoczne selektory pól i interwału"><figcaption><p>Włącz wykrywanie, zanim wybierzesz pola porównania i interwał czasowy.</p></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/dbdc665-duplicate-interval-options-pl-20261011.png" alt="Menu Interwał wykrywania duplikatów z opcjami jeden miesiąc, trzy miesiące, sześć miesięcy i jeden rok"><figcaption><p>Trzy miesiące są w menu oznaczone jako interwał zalecany.</p></figcaption></figure>

Dla typu dokumentu **Faktura** sekcja oferuje dodatkowo przełączniki **Wykrywanie duplikatów faktur**, **Blokuj eksport duplikatów dokumentów** oraz **Zignoruj linię wolną od podatku**. To osobne przełączniki; włącz tylko zachowania, których wymaga Twój proces obsługi faktur. Dodatkowe przełączniki nie są widoczne dla innych typów dokumentów.

## Sprawdzanie oznaczonego dokumentu

Gdy DocBits znajdzie dopasowanie, wiersz dokumentu na **Pulpicie** pokazuje ikonę duplikatu. Wybierz ikonę, aby porównać pasujące rekordy w panelu bocznym. Ikona pojawia się tylko wtedy, gdy istnieje dopasowanie.

Gdy otworzysz oznaczony dokument, ostrzeżenie o duplikacie oferuje przyciski **View Duplicate** (pokaż duplikat), **Proceed Anyway** (kontynuuj mimo to) oraz — jeśli dokument nie został jeszcze zarchiwizowany — **Archive** (archiwizuj). Przejrzyj pasujące rekordy, zanim wybierzesz działanie. Listę dokumentów opisuje [przewodnik po Pulpicie](../../dashboard/README.md).
