# Kiedy

<figure><img src="../../../.gitbook/assets/docbits_workflow_4.png" alt="DocBits Przepływ pracy 4"><figcaption></figcaption></figure>

#### Zrozumienie sekcji "Kiedy" w Konfiguracjach Przepływu Pracy

**Cel sekcji "Kiedy"**

* Sekcja "Kiedy" w konfiguracji przepływu pracy definiuje warunki wyzwalające określoną akcję w przepływie pracy. Warunki te opierają się na określonych kryteriach dotyczących atrybutów dokumentu lub aktywności użytkownika w systemie ERP.

**Jak to działa**

* W interfejsie "Kiedy" wydaje się być punktem wyjścia, w którym użytkownicy mogą wybrać różne karty wyzwalaczy. Każda karta określa warunki, na podstawie których następne akcje (zdefiniowane w innej sekcji konfiguracji przepływu pracy, najprawdopodobniej oznaczonej jako "Akcja") zostaną wykonane.

**Karty Warunków Typu Dokumentu**

* Karty wyświetlone na zrzucie ekranu są wariantami warunków "Typ Dokumentu", które służą do wyzwalania przepływów pracy na podstawie typu przetwarzanego dokumentu. Oto analiza każdej karty warunków typu:

* **Typ dokumentu (Operator) jeden z (Typ)**: Ta karta wyzwalająca akcję, gdy typ dokumentu pasuje do jednego z określonych typów na liście. Operator może zawierać opcje takie jak "jest" lub "nie jest", pozwalając na warunki włączające lub wyłączające.
* **Typ dokumentu (Operator) (Typ)**: Ten prostszy wariant wyzwalacza działa na podstawie pojedynczego warunku typu dokumentu. Zazwyczaj sprawdza, czy typ dokumentu "jest" lub "nie jest" określonym typem, bez możliwości wyboru spośród wielu typów.

#### Konfigurowanie Karty Wyzwalacza "Kiedy"

1. **Wybór Typu Warunku**: Użytkownicy rozpoczynają od wybrania typu warunku, który jest istotny dla przepływu pracy, który chcą zautomatyzować. W tym przypadku skupiamy się na typach dokumentów.
2. **Określenie Operatora**: Użytkownicy muszą zdecydować o operatorze logicznym, takim jak "jest" lub "nie jest", który stanowi podstawę porównania rzeczywistych typów dokumentów z zdefiniowanymi warunkami.
3. **Określenie Typów Dokumentów**: W zależności od karty, użytkownicy mogą wybrać jeden lub wiele typów dokumentów, które wywołają przepływ pracy, gdy dokumenty tych typów zostaną przetworzone.
4. **Finalizacja Wyzwalacza**: Po skonfigurowaniu warunku staje się on podstawą do wyzwalania określonych akcji zdefiniowanych w przepływie pracy. Jeśli dokument spełnia ustawiony warunek, zdefiniowane akcje zostaną automatycznie uruchomione.

#### Zastosowanie W Praktyce

W praktyce te karty wyzwalaczy są kluczowe do automatyzacji procesów takich jak zatwierdzanie, powiadomienia lub dowolna procedura zależna od typu przetwarzanego dokumentu. Na przykład, jeśli typ dokumentu "jest" "Fakturą" i spełnia warunki ustawione na karcie "Kiedy", przepływ pracy może automatycznie przekierować dokument do procesu płatności.

To ustawienie zapewnia, że przepływy pracy są nie tylko wydajne, ale także dostosowane do konkretnych potrzeb operacyjnych organizacji, zmniejszając ręczne nadzorowanie i przyspieszając procesy obsługi dokumentów.

Podsumowując, część "Kiedy" w konfiguracji przepływu pracy służy do ustawiania sceny dla automatycznych działań na podstawie określonych, wstępnie zdefiniowanych warunków. Jest to potężne narzędzie zapewniające, że system ERP reaguje dynamicznie na potrzeby biznesu, poprawiając zarówno produktywność, jak i dokładność zarządzania dokumentami.
