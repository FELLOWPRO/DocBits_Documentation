# Appearance

**Appearance** pozwala administratorowi nadać kopii DocBits w organizacji własny wygląd: kolory, promień narożników, gęstość i czcionkę. Wszyscy w organizacji widzą wynik — w trybie jasnym i ciemnym — po następnym odświeżeniu. Nigdy nie zmienia układu ani tego, co robi funkcja, tylko sposób jej rysowania.

> **Dostęp:** Appearance to strona tylko dla administratorów. Otwórz **Settings → Organization & Access → Appearance**.

<!-- screenshot: /settings/appearance light -->

## Kto może to zmieniać

Tylko administratorzy organizacji mogą otworzyć **Settings → Appearance** i zapisać lub zresetować motyw. Wszyscy pozostali w organizacji widzą wyłącznie wynik.

## Co jest na stronie

Strona jest podzielona na edytor po lewej i podgląd na żywo po prawej.

| Obszar | Co zawiera |
|---|---|
| **General** | Nazwę motywu, czcionkę, promień narożników i gęstość. |
| **Colors** | Zakładki Light i Dark, dla każdego koloru próbkę i pole szesnastkowe, pogrupowane w Surfaces, Brand, Neutrals, Status i Charts. Panel „Derived colours” tylko do odczytu pod spodem pokazuje kolory, które DocBits wylicza dla Ciebie (stany hover, pierścienie fokusu i podobne) z kolorów powyżej. |
| **Advanced overrides** | Jedną linię `--token: value` na wpis, na rzadki przypadek, gdy powyższe kontrolki koloru, promienia, gęstości i czcionki nie wystarczają — zobacz [Advanced overrides](#advanced-overrides). |

### Zmiana kolorów

Każdy kolor ma próbkę (kliknij ją, aby otworzyć próbnik kolorów przeglądarki) i pole szesnastkowe obok, w którym możesz wpisywać lub wklejać. Pozostaw kolor pusty, aby zachować domyślną wartość DocBits dla tego tokenu — próbka pokazuje wtedy przerywaną ramkę. Przełącz się między zakładkami **Light** / **Dark** nad listą kolorów, aby ustawić drugi tryb; kolor, którego nie ustawisz w trybie ciemnym, zachowuje własną domyślną wartość DocBits dla trybu ciemnego i nie kopiuje wartości jasnej.

{% hint style="info" %}
Kolory wprowadza się w zapisie szesnastkowym (`#2388ae` lub `#2388aeaa` z kanałem alfa). Nie ma pola na nazwy kolorów ani `rgb()`.
{% endhint %}

### Promień narożników, gęstość i czcionka

* **Corner radius** — `None`, `Small`, `Medium` (domyślnie), `Large` lub `Extra large`. Określa zaokrąglenie kart, przycisków, pól wejściowych i okien dialogowych w całej aplikacji.
* **Density** — `Compact`, `Comfortable` (domyślnie) lub `Spacious`. Określa wysokość przycisków, pól wejściowych i wierszy tabel oraz podstawowy rozmiar tekstu.
* **Font** — krótka lista dołączonych czcionek (Geist jest domyślną czcionką DocBits; także Inter, Roboto, IBM Plex Sans, Source Sans 3, Nunito Sans, Manrope, Kanit lub czcionka systemowa odwiedzającego). Wszystkie czcionki są już dołączone, nie trzeba niczego przesyłać.

### Advanced overrides

Dla tokenu designu, którego powyższe kontrolki nie udostępniają bezpośrednio (na przykład konkretnej wysokości wiersza tabeli), dodaj linię w **Advanced overrides**:

```
--table-row-h: 30px
```

Jedno nadpisanie na linię, `--token: value`. Nieprawidłowa linia — nieznany token, token, którego nie można dostosować, lub wartość, która nie pasuje do oczekiwań tokenu — jest wyświetlana jako błąd pod polem i nie jest stosowana; reszta strony nadal zapisuje się normalnie.

## Podgląd

Każda zmiana natychmiast aktualizuje panel **Preview** po prawej, nie wpływając na to, co widzą inni — nigdy nie dotyka działającej aplikacji ani zapisanego motywu. Podgląd ma własne zakładki: przegląd z trybem jasnym i ciemnym obok siebie, a następnie osobne strony przycisków, pól formularzy, powierzchni i wskaźników statusu, aby sprawdzić kontrast i czytelność w częściach interfejsu najbardziej wrażliwych na kolor.

<!-- screenshot: /settings/appearance dark -->

Jeśli zmiana sprawi, że motyw będzie nieprawidłowy (patrz niżej), podgląd nadal pokazuje ostatnią prawidłową wersję, zamiast się zepsuć.

## Zapisywanie i resetowanie

* **Save** zapisuje motyw dla całej organizacji. Jest nieaktywny, dopóki coś naprawdę się nie zmieniło, a motyw jest prawidłowy.
* **Reset** prosi o potwierdzenie, a następnie całkowicie usuwa motyw organizacji i przywraca wszystkim domyślny motyw DocBits. Tego nie można cofnąć ze strony — kolory trzeba wprowadzić ponownie ręcznie (lub zaimportować ponownie, patrz niżej), jeśli organizacja chce je odzyskać.
* Nieudany zapis lub reset (na przykład z powodu problemu z walidacją) wyświetla problem nad edytorem i pozostawia stronę bez zmian; nic nie jest stosowane.

Przed zapisaniem nie ma sprawdzania kontrastu — patrz [Wskazówki](#wskazówki) poniżej.

## Eksport i import

* **Export** pobiera motyw aktualnie wyświetlany w edytorze (zapisany lub nie) jako plik `.json`, nazwany od motywu.
* **Import** odczytuje plik motywu `.json` i wczytuje go do edytora. Nadal trzeba go przejrzeć i zapisać, aby zadziałał — sam import nie zmienia tego, co ktoś widzi. Nieprawidłowy lub zbyt duży plik (powyżej 32 KB) jest odrzucany z błędem i nic się nie zmienia.

Eksport to wygodny sposób zapisania kopii motywu przed eksperymentami lub przeniesienia wyglądu jednej organizacji do innej.

## Co widzą użytkownicy

Po zapisaniu motyw obowiązuje w całej aplikacji — na każdej stronie, w trybie jasnym i ciemnym — dla każdego członka organizacji, po jego następnym odświeżeniu (nie od razu w innych otwartych sesjach). Użytkownik, który nigdy nie wczytał organizacji, widzi domyślny wygląd DocBits, dopóki ustawienia organizacji nie zostaną raz wczytane; potem motyw przejmuje kontrolę.

Reset przywraca wszystkim domyślny wygląd DocBits przy następnym odświeżeniu, dokładnie tak, jakby motyw organizacji nigdy nie został ustawiony.

## Wskazówki

* **Sprawdź kontrast w obu trybach.** Edytor nie ostrzega o kombinacjach o niskim kontraście (na przykład jasny kolor marki z jasnym tekstem). Użyj jasnego i ciemnego panelu podglądu, aby przed zapisaniem sprawdzić, czy tekst pozostaje czytelny.
* **Nie zmieniaj kolorów statusu, jeśli nie masz ku temu powodu.** Destructive (błędy), success, warning i info zachowują swoje znaczenie w całej aplikacji — ich zmiana może sprawić, że błąd na pierwszy rzut oka wygląda jak sukces. Zmień kolor marki, a kolory statusu pozostaw na wartościach domyślnych, chyba że organizacja potrzebuje czegoś więcej niż typowej czerwieni/zieleni/bursztynu/niebieskiego.
* **Zacznij od pełnej palety.** Wyeksportowanie bieżącego motywu lub start od domyślnego DocBits daje każdej podstawowej barwie wartość do edycji, zamiast zgadywania, które tokeny istnieją.
* **Zmiana motywu dotyczy każdego użytkownika w organizacji natychmiast przy następnym odświeżeniu.** Nie ma etapu podglądu tylko dla części użytkowników; sam sprawdź wynik w trybie jasnym i ciemnym, zanim powiesz zespołowi, że jest gotowy.
