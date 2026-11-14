# Konfiguracja LN

Ten przewodnik łączy historyczne przykłady z Infor ION z aktualnym formularzem eksportu LN w DocBits. Obrazy z Infor pokazują poszczególne kroki; nazwy firm, nazwy mapowań i układ na tych obrazach są przykładami. Przed aktywowaniem przepływu poproś administratora Infor o sprawdzenie punktów połączenia, pakietu mapowań i uprawnień BOD dla Twojej firmy LN. Na potrzeby tej aktualizacji dokumentacji nie testowano połączenia z firmą Infor ani eksportu faktury.

## Wymagania wstępne

Przygotuj:

* punkt końcowy API ION
* plik API ION
* plik mapowania BOD
* plik mapowania IDM

## Importowanie plików mapowania

Zanim skonfigurujesz przepływ danych, zaimportuj pliki mapowania do InforOS.

W ION Desk otwórz **Connect → Mappings**.

<figure><img src="https://lh7-us.googleusercontent.com/fAUUcBUSxIWqLjYEHH78O2Mfq0P4d4D42OgCNFPdpUQTM5ZHu_BcKz9DmWe0AlHe3--ff7z9mfYTrt7oAkf2uknBwkV2VWayEpiJ_aAIxcJil5LNiep4U6KZr3_tBfs1RRwXoW749q3FUxurXy_pT_k" alt="Historyczny przykład: nawigacja ION Desk z rozwiniętą grupą Connect i pozycjami Data Flows, API Flows, Connection Points, File Templates oraz Enterprise Locations."><figcaption><p>Historyczny przykład: nawigacja ION Desk z rozwiniętą grupą Connect i pozycjami Data Flows, API Flows, Connection Points, File Templates oraz Enterprise Locations. Sprawdź odpowiednie ustawienia w swojej firmie Infor.</p></figcaption></figure>

Kliknij ikonę importu.

<figure><img src="https://lh7-us.googleusercontent.com/d_KYA9LgiiW1A95CH9hwU1AC1u5x25T4ET-4sAqpZkVOexHc4WcbwPXUaKt3O9fR3Btvv-NEGbCWwnnb8SfomnnO22M8YTIqWdvan-SkbG0cu1MWkjwOn_Vd_b6rJaQng8A92JTa5YKBms4RuIvwmb0" alt="Historyczny przykład: pasek narzędzi Mappings w ION Desk z zaznaczoną ikoną importu."><figcaption><p>Historyczny przykład: pasek narzędzi Mappings w ION Desk z zaznaczoną ikoną importu. Sprawdź odpowiednie ustawienia w swojej firmie Infor.</p></figcaption></figure>

* Wybierz potrzebne pliki mapowania: SyncCaptDoc\_SyncSuppInv, SyncSupplierInvoice\_LoadSupplierInvoice oraz LoadSupplierInvoice\_ProcessSupplierInvoice.
* Po zaimportowaniu wszystkich plików mapowania zatwierdź każdy z nich, klikając ikonę znacznika w jego kafelku na pulpicie mapowań.

## Z DocBits do LN

Następnie skonfiguruj przepływ danych w ION Desk: otwórz aplikację ION Desk i wybierz **Data Flow → + ADD → Document Flow**, jak pokazano poniżej.

<figure><img src="https://lh7-us.googleusercontent.com/rjPVR1EFKw_gZI1Ztg9Aqt4pFw10rii7WU-yddLIz22a_Fn3s1HSYDRmQVvgZtX_85nb2ipNqJ1JU49NIE8a57TIur7jqoMuKFKlb-RrfnRFxiA1TefzofKPJ32fzIdDWI8PmnD-aDw4qhQj4e0dd9I" alt="Historyczny przykład: strona Data Flows w ION Desk z nawigacją po lewej, przepływem DF_SLTStAPI na liście oraz pozycjami menu Document Flow i Data Lake Flow."><figcaption><p>Historyczny przykład: strona Data Flows w ION Desk z nawigacją po lewej, przepływem DF_SLTStAPI na liście oraz pozycjami menu Document Flow i Data Lake Flow. Sprawdź odpowiednie ustawienia w swojej firmie Infor.</p></figcaption></figure>

Na tym obszarze roboczym zbudujesz przepływ informacji z DocBits do LN.

<figure><img src="https://lh7-us.googleusercontent.com/9C7BaoiHWRaav0ytCbYkxEYG12f-64qyagsl8H2eq5TXUySRE1s3x_-lVRbK6tpTxvbRYKvwyWO_6ASSQ6Rn62LQR9ZvMRpRXq9UymZLS0I8IZ-hOzX58iYtTruqSo5WdgIXwEPjMlb1dnuFuhN8IS8" alt="Historyczny przykład: nowy Document Flow z pustym panelem właściwości oraz komunikatami Document flow name must be specified i The document flow has no activities."><figcaption><p>Historyczny przykład: nowy Document Flow z pustym panelem właściwości oraz komunikatami Document flow name must be specified i The document flow has no activities. Sprawdź odpowiednie ustawienia w swojej firmie Infor.</p></figcaption></figure>

Przepływ danych LN wygląda podobnie do poniższego. Widocznych jest kilka ścieżek, ponieważ każda z nich jest przeznaczona dla innego typu dokumentu; w tym opisie skupiamy się na przepływie danych faktury.

<figure><img src="https://lh7-us.googleusercontent.com/gltDE9JxeGb7Ufg9Ldl-JIJ95zfWHnQtyOqys2QKCiTlIn_PdAyBLFYmTVCh9c-TxF5xNQR3G8Hmn4EXK94t6MJ-1WzlZg1Zl7HNoxfR56zC8dT1skmxLTj7rtnSl0JTQJD_3myQY4Qcd9motySYh9U" alt="Historyczny przykład: obszar roboczy Data Flow z kilkoma ścieżkami dla różnych typów dokumentów; każda ścieżka składa się z punktu połączenia DocBits, mapowania i punktu połączenia LN."><figcaption><p>Historyczny przykład: obszar roboczy Data Flow z kilkoma ścieżkami dla różnych typów dokumentów; każda ścieżka składa się z punktu połączenia DocBits, mapowania i punktu połączenia LN. Sprawdź odpowiednie ustawienia w swojej firmie Infor.</p></figcaption></figure>

Wszystkie elementy łańcucha przeciągasz z górnej sekcji.

W łańcuchu DocBits i LN są aplikacjami, a pomiędzy nimi znajdują się mapowania. Przekształcają one dane do postaci zrozumiałej dla następnego elementu przepływu i przypisują informacje do właściwych miejsc.

<figure><img src="https://lh7-us.googleusercontent.com/Gwk0C0gsnMSlgEwRx0_1GDMJEu8Z1TAhKo8gxHN8GxFFKGgb257a684Hj0eNSLTIK5v8F7yzJ1hIHrC_3I9RLY0S-u3ZDhmkD6iJbYAvtCAeFPWHBVLOqyCH7FKsl2SKAfXL-AdtNowqdol9PzS4qJM" alt="Historyczny przykład: paleta działań i przepływ w ION, w których działania aplikacji reprezentują DocBits i LN, a pomiędzy nimi znajdują się działania mapowania."><figcaption><p>Historyczny przykład: paleta działań i przepływ w ION, w których działania aplikacji reprezentują DocBits i LN, a pomiędzy nimi znajdują się działania mapowania. Sprawdź odpowiednie ustawienia w swojej firmie Infor.</p></figcaption></figure>

### Aplikacja DocBits

Nadaj jej odpowiednią nazwę, na przykład „DocBits”, następnie wybierz znak plus, wyszukaj utworzony wcześniej punkt połączenia — na przykład DocBits\_Export — i kliknij go.

Aby utworzyć ten punkt połączenia, przejdź do **ION Desk → Connect → Connection Points**.

<figure><img src="https://lh7-us.googleusercontent.com/1SZJN-GW7BP-fvUHZ-tCJ4xNXx0ABRP3J9eMzF3BTKIY54J-pK4bYy4fOVHCaI6A2sdrYekWJsY9ky8dXz36l_FwwzzEnO1IjxNkMqlV-Y4UvyFIei73Z9C19m9bzTr3gCL3IpTUqiV280id1vJE530" alt="Historyczny przykład: nawigacja ION Desk z rozwiniętą grupą Connect i pozycjami Data Flows, API Flows, Mappings oraz Connection Points."><figcaption><p>Historyczny przykład: nawigacja ION Desk z rozwiniętą grupą Connect i pozycjami Data Flows, API Flows, Mappings oraz Connection Points. Sprawdź odpowiednie ustawienia w swojej firmie Infor.</p></figcaption></figure>

Kliknij **+ Add**.

<figure><img src="https://lh7-us.googleusercontent.com/ZJ1212Gwdk-b2-LVbEd2ZDzc_AqaEEYtIN0fC6d6P4EaWdTKj6nOzGDbA5sxdBtMcTrWopfDmd7GTahbwkDpj3uvmMYgvEUQa6qmi58NFGvtcgAtIwYr952Yu7Lcj802iHtQ_vj_-XPdegP1P0ySdos" alt="Historyczny przykład: strona Connection Points w ION Desk z otwartą grupą Connect w nawigacji."><figcaption><p>Historyczny przykład: strona Connection Points w ION Desk z otwartą grupą Connect w nawigacji. Sprawdź odpowiednie ustawienia w swojej firmie Infor.</p></figcaption></figure>

Wybierz **IMS via API Gateway** i wypełnij poniższe informacje.

<figure><img src="https://lh7-us.googleusercontent.com/H4YCH-324EzrxKkrbRs0SFTsHch5eK74gXleSpfI03uJ5frIEFjwofu7p6bsYO1lS7sVqamWDZMXrGfEgewdROyhTYLkn7MuCgwb7oQxOLJoH3NsnMsqTOgT3WxlihUkJdNy-WTai5kPz8ZjdtTDQ9I" alt="Historyczny przykład: punkt połączenia IMS via API Gateway z przykładowym identyfikatorem logicznym i zamazanym polem ION API Client Id."><figcaption><p>Historyczny przykład: punkt połączenia IMS via API Gateway z przykładowym identyfikatorem logicznym i zamazanym polem ION API Client Id. Sprawdź odpowiednie ustawienia w swojej firmie Infor.</p></figcaption></figure>

Identyfikator klienta ION API to wartość `ci` w pliku `.ionapi`. Plik dla Twojej firmy otrzymasz od upoważnionego administratora Infor. Zawiera dane dostępowe, dlatego nie umieszczaj go na zrzutach ekranu, w zgłoszeniach ani w Git. Zobacz [objaśnienie pól danych dostępowych ION API w dokumentacji Infor](https://docs.infor.com/crm/9.4.x/en-us/webclient/upi1639111995644.html).

Przejdź do karty dokumentów i dodaj BOD **Sync.CaptureDocument** do punktu połączenia DocBits, jak pokazano poniżej.

<figure><img src="https://lh7-us.googleusercontent.com/Wy2BIr1z_RqU-yMkXo6vOu64QC6c66OdHOxdI6PPy0yJv1jIAJF0OYITULxTFoPUK93SK3jvNm67tcxqjiEBIk0Wbu1Q1s-mSIUuPjJorcYyXY7vjsHOnoutn6tE8r6yE_333uCWuKvKiVoo99FrXVg" alt="Historyczny przykład: punkt połączenia DocBits-Sandbox-Export z otwartą kartą Documents i przypisanym dokumentem Sync.CaptureDocument."><figcaption><p>Historyczny przykład: punkt połączenia DocBits-Sandbox-Export z otwartą kartą Documents i przypisanym dokumentem Sync.CaptureDocument. Sprawdź odpowiednie ustawienia w swojej firmie Infor.</p></figcaption></figure>

Następnie zapisz punkt połączenia, klikając ikonę dysku w lewym górnym rogu.

Wróć do sekcji Dataflow w ION Desk, aby otworzyć swój przepływ danych. Aplikacja DocBits powinna wyglądać podobnie do poniższej.

<figure><img src="https://lh7-us.googleusercontent.com/cDWHmRP85YNLu7JRzq4CSezncTgP2ZOkEfZSqXK9JEq4bSwsddU7VKg8leoxaJ5zeFAbDzXrNkztmeWDIXbHwjxfUa_IpATDDwykv-OlZ2zaOVGHVqRZZpVLJ5Cq5Qla1pZk5sBV39I98lUfGao65Mw" alt="Historyczny przykład: okno Application Activity Properties z nazwą aplikacji DocBits-Sandbox i wybranym punktem połączenia DocBits-Sandbox-Export."><figcaption><p>Historyczny przykład: okno Application Activity Properties z nazwą aplikacji DocBits-Sandbox i wybranym punktem połączenia DocBits-Sandbox-Export. Sprawdź odpowiednie ustawienia w swojej firmie Infor.</p></figcaption></figure>

### Mapowanie 1

Pierwszy węzeł mapowania powinien wyglądać następująco:

<figure><img src="https://lh7-us.googleusercontent.com/9tlIun_ipbTp15aMX3xN2DGlDjAZ1oI4AFWXwbP7yoFLeQNqcw_L3Z1djaqcbxP1tsp1R-nq6ZJqEzsoKe1-SmLrJNmYrJ4HJircLEwMxfmif-p2T8nqbuuxHLLLzQJ6E6tNG6MzghOpoEAt41ea2GY" alt="Historyczny przykład: właściwości pierwszego mapowania, Capture2sync, z przykładowym mapowaniem LN_CaptureDocumentToSupplierInvoice_1."><figcaption><p>Historyczny przykład: właściwości pierwszego mapowania, Capture2sync, z przykładowym mapowaniem LN_CaptureDocumentToSupplierInvoice_1. Sprawdź odpowiednie ustawienia w swojej firmie Infor.</p></figcaption></figure>

### Mapowanie 2

Drugi węzeł mapowania powinien wyglądać następująco:

<figure><img src="https://lh7-us.googleusercontent.com/ZDYzTAfm3MHnEIKHa2tDl7NPbjzxv8jH-KL8O0pRhi1JYtqiiVz0-GQv5N4roVWi1STopQkFV9YHbEXdyzwYxK2Oq6mUv6tuqKDp-2bc-aPVgEXdEBd2hmW-6j6JRhEympyw9yUTrCDQRKlDQ41C5Ao" alt="Historyczny przykład: właściwości drugiego mapowania, Load2Process, z przykładowym mapowaniem LoadSupplierToProcessSupplierInvoice."><figcaption><p>Historyczny przykład: właściwości drugiego mapowania, Load2Process, z przykładowym mapowaniem LoadSupplierToProcessSupplierInvoice. Sprawdź odpowiednie ustawienia w swojej firmie Infor.</p></figcaption></figure>

### Aplikacja LN

W Infor powinien już istnieć punkt połączenia o nazwie LN lub podobnej, utworzony dla właściwej firmy LN. Wybierz go tak samo jak aplikację DocBits, klikając znak „+”. Wynik powinien wyglądać następująco:

<figure><img src="https://lh7-us.googleusercontent.com/mRXL11f68EtQHHjl40QmCisy7S1aUezqCzufPTZWgYHhWLK2Yw0UY82O_dgbAhBChFHHYUMBDSWWb-PEKyohJWOp5gvufat431ezpA2cIHMtry7XEDxhnNzPB68uSMkFAXhX1x4GyiH6Cxp-USxDnHE" alt="Historyczny przykład: okno Application Activity Properties aplikacji LN z przykładową nazwą LN-200 i wybranym połączeniem aplikacji In01_0200."><figcaption><p>Historyczny przykład: okno Application Activity Properties aplikacji LN z przykładową nazwą LN-200 i wybranym połączeniem aplikacji In01_0200. Sprawdź odpowiednie ustawienia w swojej firmie Infor.</p></figcaption></figure>

### BODs

<figure><img src="https://lh7-us.googleusercontent.com/de8OyDF4yMoHaXsxM9weJdm8mKDzL97kFRr00fhoHAxxKXb2BgMcMM2shyxi1S7cBwzSAUy2u8bZV4sJOVqgXt8Mcge6L2CXxbfVGiqXUwKwF6A5mgt4zfGPYltaZuLazOJYu2u7arszJE6IonMOskk" alt="Historyczny przykład: obszar roboczy Data Flow z węzłami DocBits-DEV, MappingDeliver, Load Supplier, PurchaseOrder, SalesOrder i AdvancedShip powyżej pozycji End."><figcaption><p>Historyczny przykład: obszar roboczy Data Flow z węzłami DocBits-DEV, MappingDeliver, Load Supplier, PurchaseOrder, SalesOrder i AdvancedShip powyżej pozycji End. Sprawdź odpowiednie ustawienia w swojej firmie Infor.</p></figcaption></figure>

Poniższe konfiguracje powinny wyglądać następująco:

#### Pierwszy

<figure><img src="https://lh7-us.googleusercontent.com/rj_qpiML1a2dNxj6ItiRxescymVtD6LHIAum3UPrPERAavhkt81lpjcyAFmn_lmxtqUDVTm_kiZ9f02Lqh9w-SAWmcxvGuxWITVvhv9qg04HaJXGH7VfRiO4Iv1LtDxfKYFyUWPLzCE4L3yP4hcdGnY" alt="Historyczny przykład: lista dokumentów pierwszego kroku z pozycją Sync.CaptureDocument."><figcaption><p>Historyczny przykład: lista dokumentów pierwszego kroku z pozycją Sync.CaptureDocument. Sprawdź odpowiednie ustawienia w swojej firmie Infor.</p></figcaption></figure>

#### Drugi

<figure><img src="https://lh7-us.googleusercontent.com/TCxMS-RhoJcUyBko36Lfpa8D71qk-ZSN-lME7Oq8cfPACVV0Ci7Lnv6y_MF_53U763ZA74xq6icEfgDUwYYJ9UJK0kCiLHQZpJYmc_ywjB32UGrpDnh7AjoHpI5AtWd3yZR3RsMaki1AYenpdG4X9X8" alt="Historyczny przykład: lista dokumentów drugiego kroku z pozycją Load.SupplierInvoice."><figcaption><p>Historyczny przykład: lista dokumentów drugiego kroku z pozycją Load.SupplierInvoice. Sprawdź odpowiednie ustawienia w swojej firmie Infor.</p></figcaption></figure>

#### Trzeci

<figure><img src="https://lh7-us.googleusercontent.com/VPYJyfpO0RZueW46s2Y8W2H-tQFlMfIdP1Sf8qMB8BfTxefgQ5dhsaAxL36R7cdvmKR26Q_epAj9_i6CzUO6C-PHjStEynBDkjtwId4BSuH6-zJklmsr25XcNH2AY7pSwOQ_rbCCixhWcaJg2kHyyYw" alt="Historyczny przykład: lista dokumentów trzeciego kroku z pozycją Process.SupplierInvoice."><figcaption><p>Historyczny przykład: lista dokumentów trzeciego kroku z pozycją Process.SupplierInvoice. Sprawdź odpowiednie ustawienia w swojej firmie Infor.</p></figcaption></figure>

Ostatnia ikona powinna być pusta, ponieważ nie przenosi żadnego dokumentu ani informacji.

Gdy administrator Infor sprawdzi wszystkie węzły, mapowania i subskrypcje dokumentów, aktywuj przeznaczony przepływ przyciskiem aktywacji. Poniższy historyczny obrazek wskazuje ten przycisk; jego stara nazwa przepływu zawiera M3 i nie może być użyta jako nazwa ani cel konfiguracji LN.

<figure><img src="https://lh7-us.googleusercontent.com/WjQeGz_effl_RlkWC4CdJS9Dg_9DpsIz3meKOsa7GbU9RFSrYMw3PpbXFat6cGsA4gvEGS-0D-YFrZj9K2wK3Irap-30mcQ5kr5k4Gy2gm7DLJdYpzJgeBRVInyAYfGmGXu2dCQvmX9ballRbSwyq3o" alt="Historyczny przykład: pasek narzędzi Document Flow z zaznaczonym przyciskiem aktywacji. Stary przykładowy przepływ nazywa się DocBits-Export-M3; w swojej firmie wybierz właściwy przepływ LN."><figcaption><p>Historyczny przykład: pasek narzędzi Document Flow z zaznaczonym przyciskiem aktywacji. Stary przykładowy przepływ nazywa się DocBits-Export-M3; w swojej firmie wybierz właściwy przepływ LN. Sprawdź odpowiednie ustawienia w swojej firmie Infor.</p></figcaption></figure>

## Konfiguracja eksportu w DocBits

W wybranej organizacji DocBits otwórz **Ustawienia → Eksport**. Lista pokazuje istniejące konfiguracje eksportu wraz z kolumnami Typ, Podorganizacje, Tytuł, Metoda Eksportu i Akcje. Wybierz **Nowy**, aby przygotować nową konfigurację.

<figure><img src="../../../.gitbook/assets/dbdc1113-export-list-pl-20261112.png" alt="Aktualna polska lista eksportu w DocBits z przyciskiem Nowy, kolumnami Typ, Podorganizacje, Tytuł, Metoda Eksportu i Akcje oraz komunikatem o braku konfiguracji."><figcaption><p>W tym przykładzie lista jest pusta i pokazuje komunikat „Nie znaleziono konfiguracji. Utwórz pierwszą konfigurację, aby rozpocząć.” Przycisk Nowy otwiera formularz konfiguracji; żadna zapisana konfiguracja nie została otwarta ani zmieniona. Wszystkie dane to wymyślony przykład z aplikacji 11.27.7.</p></figcaption></figure>

W sekcji **Informacje podstawowe** wpisz **Tytuł konfiguracji** i wybierz **Typ dokumentu** (w przykładzie fakturę). Pole **Podorganizacja** wypełnij tylko wtedy, gdy wymaga tego Twoja konfiguracja. W polu **Eksport** wybierz **Infor**, a w polu **Typ informacji** — **Infor IDM + LN**; polska wersja interfejsu określa to pole jako „Typ informacji”, chodzi o typ eksportu Infor.

W sekcji **Eksportuj konfigurację** przygotuj wszystkie trzy pliki wymagane dla nowej konfiguracji LN: **Plik API ION** (`.ionapi`), **Plik mapowania IDM** (`.properties`) i **Plik mapowania LN** (`.properties`). Kliknij **Kliknij, aby przesłać** albo przeciągnij plik do pola. Pliki dla tej firmy i firmy LN otrzymasz od upoważnionego administratora Infor. Zrzut ekranu celowo pozostawia wszystkie pola przesyłania puste i nie zawiera danych dostępowych.

<figure><img src="../../../.gitbook/assets/dbdc1113-export-ln-pl-20261112.png" alt="Aktualny polski formularz LN w DocBits z sekcjami Informacje podstawowe i Eksportuj konfigurację, wybranym eksportem Infor, typem informacji Infor IDM + LN, pustym polem Typ dokumentu oraz trzema pustymi polami przesyłania."><figcaption><p>Aktualny formularz LN rozdziela trzy pola przesyłania: Plik API ION, Plik mapowania IDM i Plik mapowania LN. W tym przykładzie nie wybrano typu dokumentu, nie przesłano żadnego pliku i nie zapisano konfiguracji. Wszystkie dane to wymyślony przykład z aplikacji 11.27.7.</p></figcaption></figure>

Gdy administrator potwierdzi przepływ ION i pliki, zapisz konfigurację przyciskiem **Zapisz** i przetestuj jedną autoryzowaną fakturę poza środowiskiem produkcyjnym. Sprawdź wynik w DocBits, Infor ION i LN. Zapisana konfiguracja sama nie dowodzi, że LN otrzymał fakturę. Jeśli tylko przeglądasz dostępne pola, zamknij formularz przyciskiem **Anulować**.

Informacje o roli punktów połączenia i przepływów dokumentów znajdziesz w [objaśnieniu Infor ION](https://docs.infor.com/ln/10.8/en-us/lnesolh/lnoshybridng/wxa1699288671147.html).
