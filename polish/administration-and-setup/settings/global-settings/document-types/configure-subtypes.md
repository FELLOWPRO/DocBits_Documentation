# Konfigurowanie podtypów

Użyj podtypu dokumentu, gdy faktury tego samego typu dokumentu wymagają innych pól, innego układu walidacji lub własnych skryptów przetwarzania. Najpierw [utwórz podtyp](creating-a-new-sub-type.md), następnie otwórz **Ustawienia → Typy Dokumentów**, wybierz typ dokumentu i otwórz **Podtypy Dokumentów**. W wierszu podtypu otwórz **Actions** (trzy kropki). Menu oferuje **Pola**, **Kreator układów** i **Skrypty**; zawiera także [Kopia, Redagować i Usuwać](using-actions.md).

<figure><img src="../../../../.gitbook/assets/document-types-configure-subtypes-subtype-actions-menu-pl-20261011.png" alt="Menu Actions podtypu dokumentu z pozycjami Pola, Kreator układów, Skrypty, Kopia, Redagować i Usuwać"><figcaption><p>Wybierz część podtypu, którą chcesz skonfigurować.</p></figcaption></figure>

## Pola

Wybierz **Pola**, aby zdecydować, jakie informacje użytkownicy widzą i wprowadzają dla tego podtypu. Możesz utworzyć pole w grupie, oznaczyć istniejące pole jako wymagane, tylko do odczytu lub ukryte oraz dostosować opcje rozpoznawania. Po zmianach wybierz **Zapisz ustawienia**. Kroki opisuje [Dodawanie i Edytowanie Pól](fields/adding-and-editing-fields.md), opcje kolumn [Konfiguracja właściwości pól](fields/configuring-field-properties-1.md), a gdy pole ma korzystać z danych wyszukiwania, [Ustawienia danych głównych](fields/master-data-settings.md).

<figure><img src="../../../../.gitbook/assets/document-types-configure-subtypes-subtype-fields-pl-20261011.png" alt="Ustawienia pól po polsku dla syntetycznego podtypu faktury, z grupami pól, kolumnami właściwości i przyciskiem Zapisz ustawienia"><figcaption><p>Ustawienia pól w organizacji testowej dokumentacji. Nie są pokazywane żadne dane klientów.</p></figcaption></figure>

## Kreator układów

Wybierz **Kreator układów**, aby rozmieścić grupy i pola na ekranie walidacji dokumentu. Lewa strona zawiera listę elementów; prawa przyjmuje przykładowy dokument do podglądu. Sprawdź wynik i wybierz **Ratować**, gdy układ będzie gotowy. [Przewodnik po Kreatorze Układów](../../../setup/document-types/layout-builder.md) wyjaśnia elementy, podgląd dokumentu i zapisywanie układu.

<figure><img src="../../../../.gitbook/assets/document-types-configure-subtypes-subtype-layout-pl-20261011.png" alt="Kreator układów po polsku dla syntetycznego podtypu faktury, z grupami, wczytywaniem podglądu i przyciskiem Ratować"><figcaption><p>Układ podtypu przed dodaniem przykładowego dokumentu.</p></figcaption></figure>

## Skrypty

Wybierz **Skrypty**, aby wyświetlić skrypty tego podtypu. Na pustej liście wybierz **Utwórz skrypt** lub **Nowy**, aby zacząć. Wyszukiwanie oraz filtry **Wszystko**, **Aktywny** i **Nieaktywny** pomagają znaleźć istniejące skrypty. Aby utworzyć skrypt, postępuj zgodnie z [Tworzenie i edycja skryptów](script/creating-and-editing-scripts.md), a przed włączeniem go do przetwarzania z [Aktywacja i zarządzanie skryptami](script/script-activation-and-management.md).

<figure><img src="../../../../.gitbook/assets/document-types-configure-subtypes-subtype-scripts-pl-20261011.png" alt="Pusta lista skryptów po polsku dla syntetycznego podtypu faktury, z przyciskiem Nowy i filtrami statusu"><figcaption><p>W testowym podtypie dokumentacji nie utworzono żadnych skryptów.</p></figcaption></figure>
