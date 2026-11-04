# Kontrola Dostępu

## Przegląd

Kontrola Dostępu określa dla pojedynczej **grupy** (roli) dokładnie to, co mogą robić jej członkowie — zarówno na **poziomie typu dokumentu** (które typy dokumentów widzą i jakie akcje mogą wykonywać), jak i na **poziomie pola** (które poszczególne pola mogą odczytywać lub edytować).

Uprawnienia są zawsze oceniane **dla każdej grupy**. Użytkownik dziedziczy uprawnienia każdej grupy, do której należy.

{% hint style="info" %}
Kontrola Dostępu działa tylko wtedy, gdy system **Grupy i Uprawnienia** jest włączony (zobacz [Aktywowanie Uprawnień](activating-permissions.md)). **Administratorzy zawsze omijają Kontrolę Dostępu** i mogą widzieć oraz robić wszystko, niezależnie od ustawień na tej stronie.
{% endhint %}

Każdą grupę można skonfigurować pod kątem:

* **Dostępu do dokumentu** — czy grupa może używać danego typu dokumentu.
* **Uprawnień do akcji** — jakie akcje (wyświetlanie na liście, podgląd, edycja, usuwanie, aktualizacja masowa, zatwierdzanie) grupa może wykonywać i *dla których dokumentów*.
* **Uprawnień do pól** — czy każde poszczególne pole danego typu dokumentu jest edytowalne, tylko do odczytu czy ukryte.

## Aktywacja

1. Przejdź do **Ustawień**.
2. Wybierz **Przetwarzanie Dokumentów**.
3. Wybierz **Moduł.**
4. Aktywuj **Kontrolę Dostępu**, włączając przełącznik.

<figure><img src="../../../../../.gitbook/assets/Access-Control3.png" alt=""><figcaption></figcaption></figure>

## Otwieranie Kontroli Dostępu grupy

1. Przejdź do **Ustawień**.
2. Przejdź do **Ustawień Globalnych**.
3. Wybierz **Grupy, Użytkownicy i Uprawnienia**.
4. Wybierz **Grupy i Uprawnienia**.
5. Aby zarządzać uprawnieniami grupy (np. PROCUREMENT\_DIRECTOR), kliknij trzy kropki po prawej stronie.
6. Wybierz **Zarządzaj Kontrolą Dostępu**.

<figure><img src="../../../../../.gitbook/assets/access_control_open_menu.png" alt="Otwórz menu wiersza grupy i wybierz Zarządzaj Kontrolą Dostępu"><figcaption><p>Na stronie „Grupy i Uprawnienia" otwórz menu <strong>⋮</strong> grupy i wybierz <strong>Zarządzaj Kontrolą Dostępu</strong>.</p></figcaption></figure>

## Jak oceniane jest uprawnienie

Gdy użytkownik próbuje coś zrobić z dokumentem, DocBits sprawdza po kolei:

1. **Czy system Grupy i Uprawnienia jest włączony, a użytkownik nie jest administratorem?** Jeśli wyłączony lub użytkownik jest administratorem → pełny dostęp.
2. **Czy typ dokumentu jest włączony dla jednej z grup użytkownika?** Jeśli wyłączony → użytkownik nie może widzieć ani używać tego typu dokumentu.
3. **Jaki zakres dostępu jest ustawiony dla akcji?** (np. *Edycja = Owner*). Zakres jest porównywany z relacją użytkownika do *tego konkretnego dokumentu* — czy jest właścicielem, przypisanym, obydwoma czy żadnym?
4. **Jakie uprawnienie do pola obowiązuje?** Nawet gdy użytkownik może otworzyć dokument, poszczególne pola mogą nadal być ukryte lub zablokowane.

## Uprawnienia na poziomie typu dokumentu

Każdy wiersz macierzy to typ dokumentu (Invoice, Credit Note, Purchase Order, …).

Pierwsza kolumna to przełącznik **Włączone / Wyłączone**. Wyłącz go, a grupa w ogóle nie będzie mogła używać tego typu dokumentu — znika on z jej pulpitu. Włącz go, a siedem kolumn akcji stanie się edytowalnych.

| Akcja | Określa, czy grupa może… |
|-------|--------------------------|
| **Lista** | widzieć typ dokumentu na liście pulpitu. |
| **Podgląd** | otworzyć dokument i zobaczyć jego szczegóły. |
| **Edycja** | zmieniać wartości pól dokumentu. |
| **Usuwanie** | usunąć dokument. |
| **Aktualizacja masowa** | zastosować masową aktualizację wielu dokumentów naraz. |
| **Pierwsze Zatwierdzenie** | udzielić zatwierdzenia pierwszego poziomu. |
| **Drugie Zatwierdzenie** | udzielić zatwierdzenia drugiego poziomu. |

### Zakresy dostępu

Każda kolumna akcji to lista rozwijana. Wybrana wartość odpowiada na pytanie *„dla których dokumentów grupa może to robić?"*. Nazwy zakresów pojawiają się w interfejsie po angielsku:

| Zakres | Kto jest uprawniony | Wpływ na dokument |
|--------|---------------------|-------------------|
| **No Access** | Nikt w grupie. | Akcja jest zablokowana dla wszystkich w grupie — przycisk jest ukryty lub wyłączony. |
| **Everyone** | Każdy członek grupy. | Każdy członek grupy może wykonać akcję na **dowolnym** dokumencie tego typu. |
| **Owner** | Tylko użytkownik, który **utworzył / przesłał** dokument. | Akcja działa tylko na dokumentach przesłanych przez samego użytkownika. |
| **Assignee** | Tylko użytkownik (lub grupa), do którego dokument jest **przypisany**. | Akcja działa tylko na dokumentach przypisanych do użytkownika lub grupy, do której należy. |
| **Owner & Assignee** | Właściciel **lub** przypisany. | Akcja działa, jeśli użytkownik jest *albo* osobą przesyłającą, *albo* przypisanym. |

{% hint style="info" %}
**Owner** i **Assignee** zależą od *relacji między użytkownikiem a każdym pojedynczym dokumentem*, więc dwóch członków tej samej grupy może mieć różne prawa do tej samej faktury — zobacz przykład poniżej.
{% endhint %}

<figure><img src="../../../../../.gitbook/assets/access_control_matrix.png" alt="Macierz Kontroli Dostępu grupy"><figcaption><p>Macierz uprawnień według typu dokumentu. Tutaj typ <strong>Invoice</strong> jest włączony, a jego akcje mają różne zakresy dostępu; pozostałe typy są wyłączone.</p></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/access_control_scope_dropdown.png" alt="Lista rozwijana zakresów dostępu"><figcaption><p>Każda kolumna akcji oferuje te same pięć zakresów dostępu.</p></figcaption></figure>

### Zatwierdzanie wymaga również Edycji

Zatwierdzenie dokumentu uruchamia w tle **dwie akcje**: DocBits najpierw **zapisuje** dokument, a następnie przenosi go do statusu zatwierdzonego. Krok zapisu wymaga uprawnienia **Edycja**, więc oba uprawnienia są powiązane.

Użytkownik, któremu przyznano wyłącznie **Pierwsze Zatwierdzenie** lub **Drugie Zatwierdzenie** — ale *nie* **Edycję** — napotyka błąd uprawnień na kroku zapisu i nie może zatwierdzić dokumentu.

{% hint style="warning" %}
Za każdym razem, gdy przyznajesz **Pierwsze Zatwierdzenie** lub **Drugie Zatwierdzenie**, przyznaj również **Edycję** (i **Podgląd**) dla tego samego typu dokumentu. Samo uprawnienie do zatwierdzania nie wystarczy.
{% endhint %}

## Uprawnienia na poziomie pola

Kliknij wiersz typu dokumentu, aby otworzyć poniżej panel **Uprawnienia Pól**. Pola są podzielone na karty (np. *Kolumny tabeli*, *Szczegóły faktury*, *Szczegóły płatności*, *Podatki i kwoty*). Każde pole ma własny poziom dostępu:

| Poziom | Wpływ na pole |
|--------|---------------|
| **Odczyt/Zapis** | Pole jest widoczne **i** edytowalne. |
| **Tylko odczyt** | Pole jest widoczne, ale **nie można go edytować** (wyszarzone). |
| **Zatwierdzenie** | Pole można edytować, ale zmiana musi przejść przez **przepływ zatwierdzania** przed zastosowaniem. |
| **Brak dostępu** | Pole jest **całkowicie ukryte** — użytkownik nigdy go nie widzi. |

{% hint style="info" %}
Reguły pól obowiązują jednakowo **wszystkich** członków grupy — nie zależą od właściciela/przypisanego. Używaj ich, aby ukryć lub zablokować wrażliwe pola (np. rabat lub kwotę całkowitą) dla całej grupy.
{% endhint %}

<figure><img src="../../../../../.gitbook/assets/access_control_field_permissions.png" alt="Panel Uprawnienia Pól"><figcaption><p>Panel „Uprawnienia Pól" dla typu Invoice. <code>CUSTOMER_DISCOUNT</code> jest ukryte (Brak dostępu), podczas gdy pozostałe pola pozostają na Odczyt/Zapis.</p></figcaption></figure>

## Przykład praktyczny: co Kontrola Dostępu robi z prawdziwą fakturą

Załóżmy, że tworzysz grupę **AP_CLERK** dla swoich księgowych ds. zobowiązań i konfigurujesz typ dokumentu **Invoice** w ten sposób:

**Uprawnienia typu dokumentu dla Invoice**

| Akcja | Zakres |
|-------|--------|
| Włączone | ✅ Tak |
| Lista | Everyone |
| Podgląd | Everyone |
| Edycja | Owner & Assignee |
| Usuwanie | No Access |
| Aktualizacja masowa | No Access |
| Pierwsze Zatwierdzenie | Assignee |
| Drugie Zatwierdzenie | No Access |

**Uprawnienia pól dla Invoice**

| Pole | Poziom |
|------|--------|
| `TOTAL_AMOUNT` | Tylko odczyt |
| `CUSTOMER_DISCOUNT` | Brak dostępu |
| *(wszystkie pozostałe pola)* | Odczyt/Zapis |

Prześledź teraz jeden konkretny dokument — fakturę **INV-4711**, którą **przesłała Maria** i która jest **przypisana do Marii**. Zarówno Maria, jak i jej kolega Tom należą do grupy **AP_CLERK**.

**Maria (właścicielka *i* przypisana do INV-4711):**

* ✅ Widzi INV-4711 na liście pulpitu *(Lista = Everyone)*.
* ✅ Otwiera ją *(Podgląd = Everyone)*.
* ✅ Edytuje nazwę dostawcy i pozycje *(Edycja = Owner & Assignee — jest właścicielką)*.
* 🔒 Widzi `TOTAL_AMOUNT`, ale pole jest wyszarzone i nie może go zmienić *(Tylko odczyt)*.
* 🚫 W ogóle nie widzi pola `CUSTOMER_DISCOUNT` *(Brak dostępu)*.
* 🚫 Przycisk **Usuń** jest ukryty *(Usuwanie = No Access — nikt w grupie nie może usuwać)*.
* ✅ Może udzielić **pierwszego zatwierdzenia** *(Pierwsze Zatwierdzenie = Assignee — jest przypisana)*.

**Tom (ta sama grupa, ale *nie* przesłał INV-4711 i *nie* jest do niego przypisana):**

* ✅ Widzi ją na liście i ✅ otwiera *(Lista i Podgląd = Everyone)*.
* 🚫 Nie może niczego edytować — dokument otwiera się **tylko do odczytu** *(Edycja = Owner & Assignee — Tom nie jest żadnym z nich)*.
* 🔒 / 🚫 Widzi dokładnie taką samą widoczność pól jak Maria: `TOTAL_AMOUNT` zablokowane, `CUSTOMER_DISCOUNT` ukryte *(reguły pól obowiązują całą grupę)*.
* 🚫 Nie może udzielić pierwszego zatwierdzenia *(Pierwsze Zatwierdzenie = Assignee — nie Tom)*.
* 🚫 Nie może usuwać *(No Access)*.

**Co pokazuje ten przykład**

* **Everyone** otwiera dokument dla wszystkich członków grupy; **Owner / Assignee** zawęża akcję do osób powiązanych z tym konkretnym dokumentem.
* **No Access** usuwa akcję (Usuwanie) lub ukrywa pole (`CUSTOMER_DISCOUNT`) dla całej grupy.
* **Tylko odczyt** utrzymuje pole widoczne jako odniesienie (`TOTAL_AMOUNT`), ale uniemożliwia zmiany.
* Dwie osoby w **tej samej grupie** mogą mieć **różne prawa do tej samej faktury**, wyłącznie ze względu na to, kto ją przesłał i do kogo jest przypisana.
