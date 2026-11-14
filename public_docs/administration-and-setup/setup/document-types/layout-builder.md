# Edytor układu

Edytor układu służy do rozmieszczania pól i elementów sterujących, które użytkownik widzi podczas walidacji lub zatwierdzania dokumentu. Układ jest przypisany do jednego typu dokumentu, jednego pochodzenia i jednego typu układu, więc przed zapisaniem sprawdź te trzy wartości w nagłówku strony.

{% embed url="https://youtu.be/-m45XGiIeig" %}
DocBits Layout Builder Tutorial: Create Custom Document Layouts for Faster, Cleaner Validation
{% endembed %}

## Otwieranie układu

1. Otwórz **Settings → Document Types**.
2. Wybierz typ dokumentu, który chcesz edytować, i otwórz **Layout Builder**. W przypadku podtypu dokumentu otwórz akcję Layout Builder tego podtypu.
3. Sprawdź nagłówek. Lewy selektor to **origin** (na przykład **Default**), po nim następują **Document Type** (na przykład **Invoice**) i **Layout type** (na przykład **Field Validation**). Każdy selektor otwiera listę; wybranie innej pozycji wczytuje dany układ. Jeśli Layout Builder jest niedostępny, administrator może musieć włączyć ten moduł dla Twojej organizacji.

<figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/layout-builder-overview.png" alt="Edytor układu dla faktury w DocBits: selektory pochodzenia, typu dokumentu i typu układu, karty Structure, Fields i Elements, obszar układu oraz panel Properties po prawej"><figcaption><p>Edytor układu: selektory w nagłówku, listy elementów po lewej, obszar układu pośrodku i panel Properties po prawej.</p></figcaption></figure>

## Praca z nagłówkiem

* **Document Type** i **Layout type** przełączają między układami. Strona wczytuje układ, który wybierzesz.
* Obok **Save** DocBits pokazuje, czy układ ma **unsaved changes**. Po zapisaniu pokazuje, kiedy układ został ostatnio zapisany.
* **Save** zapisuje układ dla wybranego typu dokumentu, pochodzenia i typu układu.
* Menu **More** (trzy kropki) zawiera **Auto Generate template**, **Apply Default layout to Origins**, **Use default template**, **Edit JSON**, **Copy JSON** i **Layout settings**. **Auto Generate template** i **Use default template** zastępują układ niestandardowy, więc najpierw sprawdź wybrany typ dokumentu i układ. **Edit JSON** służy do zaawansowanej konfiguracji i powinien być używany tylko wtedy, gdy rozumiesz format szablonu.
* Jeśli opuścisz stronę z niezapisanymi zmianami, DocBits zapyta, czy je zapisać, czy odrzucić.

## Obszary edytora

Po lewej stronie są trzy karty:

| Karta | Zastosowanie |
| --- | --- |
| **Structure** | Widok układu w formie drzewa. Grupy i ich pola są wymienione w kolejności występowania w obszarze układu, z liczbą pól umieszczonych i dostępnych. |
| **Fields** | Wszystkie pola skonfigurowane dla typu dokumentu, pogrupowane według grupy pól i domyślnie zwinięte. Filtr przełącza między polami **All**, **Unused** i **Hidden**, a pod etykietą pola widoczna jest techniczna nazwa pola. |
| **Elements** | Elementy prezentacji i interakcji, takie jak Text, Label, Check Box, separatory, tabele, przyciski i podgrupy. |

<figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/layout-builder-structure.png" alt="Karta Structure edytora układu z rozwiniętymi grupami Invoice details, Payment details, Purchase Order i Delivery Details wraz z ich polami"><figcaption><p>Karta Structure pokazuje zbudowany układ jako drzewo grup i pól.</p></figcaption></figure>

Wybierz element, aby go dodać, albo przeciągnij go do obszaru układu. Tytuł grupy mówi osobie walidującej dokument, co należy do danej sekcji. Pola dokumentu wielokrotnego użytku utwórz lub zmień ich nazwy najpierw w sekcji [Typy dokumentów](README.md).

## Praca w obszarze układu

* **Main layout** pokazuje układ samego dokumentu. **Table** pokazuje układ tabeli używany dla pozycji.
* **Document** otwiera lub zamyka przykładowy dokument obok obszaru układu, dzięki czemu możesz porównać układ z rzeczywistym dokumentem.
* Grupy są rysowane jako karty; pola wewnątrz grupy można rozmieścić w wierszach i nadać im różne szerokości.

## Zmiana właściwości elementu

Wybierz element lub grupę w obszarze układu. **Properties** po prawej jest zawsze widoczne i podzielone na sekcje:

* **Display** – etykieta, nazwa pola, położenie etykiety i szerokość elementu.
* **Behaviour** – tylko do odczytu, ukrycie i indeks Tab.
* **Values & lists** – wartości oferowane dla elementu.
* **Automation** – reguły, które wypełniają lub zmieniają element.
* **Borders & spacing** – wygląd elementu.

Dla szerokości wybierz jedną z gotowych wartości (25, 33, 50, 66, 75 lub 100 procent) zamiast wpisywać wartość; sprawdź wynik w obszarze układu. To, które sekcje i opcje są widoczne, zależy od wybranego elementu. Więcej informacji znajdziesz w artykule [Konfigurowanie właściwości pól](../../settings/global-settings/document-types/layout-manager/configuring-field-properties.md).

## Tłumaczenie etykiet przycisków

Przyciski, takie jak **Save Rules**, **Auto Accounting**, **PO Match**, **Export**, **Export Without Validation** i **Reject**, pobierają etykietę z klucza tłumaczenia. Podgląd pokazuje etykietę w języku osoby, która otwiera układ. Jeśli klucz nie ma tekstu w tym języku, DocBits pokazuje etykietę zapisaną w układzie.

* Pojedynczy przycisk ma pole **Translation Key** w **Properties**.
* **Invoice Buttons** grupuje kilka przycisków. Ustaw klucz dla pojedynczego przycisku podrzędnego albo ustaw jeden klucz dla każdego przycisku podrzędnego na liście w panelu grupy.

Układy zbudowane przed tą zmianą zachowują swoje etykiety: DocBits uzupełnia w nich domyślny klucz każdego typu przycisku. Układy zapisane z kluczem zachowują ten klucz, także po ponownym wczytaniu.

## Save and go back to Dashboard

Przycisk typu **Save and go back to Dashboard** zapisuje wartości dokumentu tak jak **Save**, a następnie otwiera Dashboard. Ten typ sprawdza się w układach, w których osoba sprawdzająca pracuje kolejno z kolejką dokumentów.

* Dodaj element przycisku w obszarze układu i wybierz typ w jego **Properties**.
* Jeśli zapis się nie powiedzie, przycisk pozostaje na ekranie walidacji i nie otwiera Dashboard, więc problem można najpierw poprawić.
* Etykieta jest ustalana jak etykieta każdego innego przycisku; zobacz *Tłumaczenie etykiet przycisków* powyżej.

## Sprawdzanie i zapisywanie

Rozmieść grupy i pola, sprawdź układ w obszarze układu i użyj **Save** w nagłówku, gdy wynik jest prawidłowy. Informacje o układach specyficznych dla pochodzenia znajdziesz w artykule [Układy według pochodzenia](origin-layouts.md).

{% hint style="info" %}
Zrzuty ekranu przedstawiają syntetyczne ustawienia w organizacji testowej DocBits z wybranym językiem angielskim w aplikacji. Podczas ich wykonywania żaden układ nie został zapisany ani zastąpiony.
{% endhint %}
