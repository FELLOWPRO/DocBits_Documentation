# Auto Accounting z Infor LN

## Od rekordu danych podstawowych LN do sprawdzonego przypisania konta

<figure><img src="../../../.gitbook/assets/process-accounting-pl-20261028.png" alt="Podstawowe dane finansowe dla Auto Accounting: Ścieżka danych i punkty kontrolne dla integracji Infor LN."><figcaption><p>Ścieżka danych i punkty kontrolne dla integracji Infor LN. Schemat ma charakter schematyczny; aktywne ustawienia Twojej organizacji określają rzeczywiste zachowanie.</p></figcaption></figure>

Ten przewodnik opisuje dostarczanie podstawowych danych finansowych dla integracji LN. Wybranie **LN** lub włączenie **Auto Accounting** nie zastępuje podania danych ani sprawdzenia wyniku przypisania rachunku.

| Przekazanie | Co powinieneś udowodnić |
| --- | --- |
| **LN → Publikacja BOD** | Popraw dane firmy i wymagane dane konta lub wymiaru; Najpierw policz lub zasymuluj wybór. |
| **BOD → ION** | Dopasowanie wersji dokumentu, źródła, filtrów i mapowania; prześledź identyfikator testu w ION OneView. |
| **ION → DocBits** | Otrzymanie odpowiedzi z punktu końcowego, poprawna organizacja i zaakceptowany zapis. Sam aktywowany przepływ nie wystarczy. |
| **DocBits → Wynik przypisania konta** | Po zatwierdzonej aktywacji użyj reprezentatywnych dokumentów testowych, aby sprawdzić, czy konta i wymiary są prawidłowe dla procesu biznesowego. |

**Przykład identyfikowalności:** Użyj niewrażliwego identyfikatora testu z zatwierdzonego zestawu danych testowych. Znajdź ten sam identyfikator w źródle BOD, w ION i w logach odbiorczych DocBits. Pomaga to zlokalizować brakujące mapowanie przy konkretnym przekazaniu, zamiast wielokrotnie zmieniać przełącznik.

Późniejszy eksport i zaksięgowanie ERP należy zweryfikować osobno. Istniejące obrazy w tym przewodniku przedstawiają elementy sterujące DocBits; nie dowodzą, że został wykonany przelew LN. W poniższej sekcji opisano przygotowanie i kompleksową weryfikację przeprowadzaną przez odpowiedzialnych administratorów. Informacje dotyczące przekazania technicznego można znaleźć w [Eksport z DocBits](../../exporting-in-docbits/README.md).

Skorzystaj z tego przewodnika, gdy administrator Infor LN chce, aby DocBits używał zaimportowanych danych finansowych do automatycznej księgowości. Poprzednia strona pokazywała 48 ekranów z konkretnej dzierżawy Infor. Nazwy punktów połączeń, mapowania, dane logowania i adresy punktów końcowych z tej dzierżawy nie stanowią konfiguracji wielokrotnego użytku.

## Znajdowanie ustawienia w DocBits

Otwórz **Ustawienia → Moduł → Zamówienia i finanse → Automatyczne rozliczanie** przy użyciu konta administratora. Menu **Typ** oferuje opcje **LN** i **M3**. W przypadku integracji z LN sprawdź, czy wybranym typem jest **LN**. Włącz przełącznik dopiero po sprawdzeniu docelowej spółki LN, przepływu BOD i zaimportowanych danych głównych. Zmiana typu lub przełącznika może wpłynąć na zachowanie księgowania, dlatego postępuj zgodnie z procesem zmian obowiązującym w Twojej organizacji.

Poniższe zrzuty ekranu pochodzą z syntetycznej piaskownicy **DocBits Documentation Test A**. W tej organizacji wybrano **LN**, a automatyczne rozliczanie było **wyłączone**. Menu zostało otwarte bez wyboru innej wartości; żadne ustawienie nie zostało zapisane.

<figure><img src="../../../.gitbook/assets/dbdc785-auto-accounting-settings-pl-20261012.png" alt="Polskie ustawienia DocBits dla modułu Zamówienia i finanse z wyłączonym Automatycznym rozliczaniem i wybranym typem LN"><figcaption><p>Znajdź Automatyczne rozliczanie i sprawdź wybrany typ przed jego włączeniem.</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/dbdc785-auto-accounting-type-options-pl-20261012.png" alt="Polskie menu Typ automatycznego rozliczania w DocBits z opcjami LN i M3"><figcaption><p>LN i M3 to dostępne typy w tej piaskownicy; nie zmieniono żadnego wyboru.</p></figcaption></figure>

## Przygotowanie LN i ION

1. Potwierdź spółkę LN, jednostkę księgową, organizację DocBits i środowisko docelowe. Uzgodnij z administratorem DocBits, która bieżąca operacja API i mapowanie pól będą odbierać konta i wymiary. Dane logowania do API przechowuj w zatwierdzonym magazynie sekretów, nigdy na zrzucie ekranu ani w załączniku Jira.
2. Skonfiguruj publikowanie BOD w LN i sprawdź konfigurację danych publikowania. Infor dokumentuje **BOD Parameters (tcbod0100m000)** i **Validate Publishing Data Setup (tcbod0300m000)** w swoim [przewodniku publikowania BOD w LN](https://docs.infor.com/ln/10.7.in/en-us/lnolh/help/tc/onlinemanual/000520.html).
3. Sprawdź, jakich notatek (nouns) wymaga Twoja wersja LN i operacja odbierająca w DocBits. Dawniej przykład używał `Sync.ChartOfAccounts` i `Sync.CodeDefinition` dla danych planu kont i wymiarów. Infor wymienia opcje Chart of Accounts i CodeDefinition w [Publish Financial Master Data (tfbia0200m000)](https://docs.infor.com/ln/2025.x/en-us/lnolh/tfolh/help/tf/bia/tfbia0200m000.html). Niektóre karty CodeDefinition pojawiają się dopiero po określeniu i zatwierdzeniu mapowania wymiarów. Potwierdź dokładne wersje dokumentów i pola w swojej dzierżawie przed ich routingiem.
4. W **ION Desk → Connect → Connection Points** połącz źródło LN z zatwierdzonym miejscem docelowym API DocBits. W **Data Flows** skieruj wybrane dokumenty, sprawdź filtry i mapowanie, a następnie zapisz i aktywuj. Infor rozróżnia [zapisanie i aktywowanie przepływu](https://docs.infor.com/inforos/latest/en-us/useradminlib_cloud/iondeskceug/lsm1436532178755.html).
5. W LN użyj niewrażliwego identyfikatora testowego. W **Publish Financial Master Data** najpierw użyj **Count** lub **Simulate**, aby przejrzeć wybór, a **Publish** tylko w ramach zmiany zatwierdzonej przez administratora. Akcja publikowania nie jest zależna od celu: Infor dostarcza dane do wszystkich subskrybentów. Śledź ten identyfikator i ewentualne błędy w [ION OneView](https://docs.infor.com/inforos/latest/en-us/useradminlib_cloud/iondeskceug/lsm1436532196155.html).

## Potwierdzenie wyniku w DocBits

Poproś administratora DocBits o sprawdzenie odebranego rekordu, organizacji i pól księgowych w bieżących dziennikach importu lub API. Jeśli odpowiednia tabela wyszukiwania jest dostępna, wyszukaj ten sam identyfikator w **Ustawienia → Przetwarzanie dokumentów → Wyszukaj dane główne**. Sam pomyślnie aktywowany przepływ ION nie dowodzi, że DocBits przyjął rekord. Jeśli wartości brakuje, porównaj źródłowy BOD, mapowanie ION, odpowiedź API i organizację docelową, zanim włączysz automatyczne rozliczanie.

Do testu end-to-end nie była dostępna żadna dzierżawa LN ani rzeczywisty transfer finansowych BOD. Nowe zrzuty z piaskownicy potwierdzają wyłącznie bieżące elementy sterujące DocBits. Administrator dzierżawy musi zweryfikować końcowe mapowanie i wynik księgowania.
