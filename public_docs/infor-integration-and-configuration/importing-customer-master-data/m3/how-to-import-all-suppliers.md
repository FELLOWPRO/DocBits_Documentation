# Rozpocznij import początkowy dostawców z Infor M3

Używaj tej procedury dopiero po tym, jak Twój administrator Infor potwierdzi firmę, oddział, BOD `SupplierPartyMaster` i trasę ION w DocBits. Nieograniczony import początkowy może wysłać wszystkich kwalifikujących się dostawców, dlatego najpierw uzgodnij mały wybór. Jedenaście poniższych zrzutów ekranu Infor M3 to przykłady historyczne; porównaj je z własnym środowiskiem, zanim uruchomisz zadanie. Ta aktualizacja strony nie uruchomiła zadania M3 ani nie zaimportowała dostawców do DocBits.

Infor opisuje [procedurę importu początkowego w EVS006](https://docs.infor.com/m3core/latest/en-us/useradminlib_cloud/m3cecoreag_cloud/hmo1553266924239.html) oraz [opcje wyboru i uruchomienia w EVS007](https://docs.infor.com/m3udi/16.x/en-us/m3beud/appfoundhs/spl1567531742751.html). Jeśli etykiety się różnią, postępuj zgodnie z zatwierdzoną procedurą własnego środowiska.

* [ ] Otwórz Infor OS i aplikację M3 na koncie uprawnionym do importów początkowych. Przed kontynuowaniem potwierdź zamierzoną firmę i oddział.

<figure><img src="../../../.gitbook/assets/6cf93500-2e90-4cfc-a9fb-5873e5dcb953.png" alt="Historyczny ekran startowy Infor M3 z menu modułów po lewej i listą Recent z pozycjami EVS006 Initial Load i BOD Processor Administration"><figcaption><p>Historyczny ekran startowy Infor M3 z pozycjami EVS006 Initial Load i BOD Processor Administration na liście Recent.</p></figcaption></figure>

* [ ] Otwórz **Initial Load. Open (EVS006)** za pomocą wyszukiwania programów w swoim środowisku.

<figure><img src="../../../.gitbook/assets/f77b242e-eb2f-43b6-8a2e-03d264198e0c.png" alt="Historyczne okno Search and Start Infor M3 z pustym polem wprowadzania i przyciskiem OK"><figcaption><p>Historyczne okno Search and Start Infor M3 z polem wprowadzania i przyciskiem OK.</p></figcaption></figure>

* [ ] W EVS006 utwórz definicję importu początkowego dla **SupplierPartyMaster**. Historyczny przykład używa tabeli **CIDMAS**. Poproś administratora M3 o potwierdzenie, że ta kombinacja BOD i tabeli jest prawidłowa w Twojej wersji i integracji.

<figure><img src="../../../.gitbook/assets/827a9dbb-c974-4da7-9bd3-f8e87adad60f.png" alt="Historyczne okno Search and Start z wpisanym evs006 w polu wprowadzania"><figcaption><p>Historyczny przykład Search and Start z wpisanym EVS006 w polu wprowadzania.</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/e30c7b86-dcfb-41d2-bd32-447b60e4581b.png" alt="Historyczna lista Initial Load w EVS006 z SupplierPartyMaster jako BOD noun i CIDMAS jako tabelą"><figcaption><p>Historyczna lista Initial Load w EVS006 z SupplierPartyMaster jako BOD noun i CIDMAS jako tabelą.</p></figcaption></figure>

* [ ] Wybierz **Create** i sprawdź definicję przed kontynuowaniem.

<figure><img src="../../../.gitbook/assets/30eee6b2-24ed-4e1f-8812-1304e7dede8e.png" alt="Historyczna lista EVS006 z wyróżnionym na czerwono przyciskiem Create (plus) na pasku narzędzi"><figcaption><p>Historyczna lista EVS006 z wyróżnionym przyciskiem Create na pasku narzędzi.</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/461b72d3-d576-4c92-95c2-d175183088af.png" alt="Historyczny panel tworzenia w EVS006 dla tabeli CIDMAS z jeszcze pustym polem BOD description"><figcaption><p>Historyczny panel tworzenia w EVS006 dla CIDMAS z pustym polem BOD description.</p></figcaption></figure>

* [ ] Wpisz czytelny **BOD Description**, na przykład **SupplierPartyMaster initial load for DocBits**.

<figure><img src="../../../.gitbook/assets/4dc345a8-8eca-4e03-800a-37a670f8792e.png" alt="Historyczny panel tworzenia w EVS006 z wpisanym SupplierPartyMaster jako BOD description"><figcaption><p>Historyczny panel tworzenia w EVS006 z wpisanym SupplierPartyMaster jako BOD description.</p></figcaption></figure>

* [ ] Wybierz **Next** i zdefiniuj uzgodniony wybór, jeśli jest dostępny. Infor zaleca kryteria wyboru, aby nie wywołać zbyt wielu zdarzeń.

<figure><img src="../../../.gitbook/assets/315aa54b-f0bd-4057-a1ed-e476c9000725.png" alt="Historyczny panel tworzenia w EVS006 z wyróżnionym przyciskiem Next w prawym dolnym rogu"><figcaption><p>Historyczny panel tworzenia w EVS006 z wyróżnionym przyciskiem Next.</p></figcaption></figure>

* [ ] Przejdź do ustawień uruchomienia. Sprawdź ponownie firmę, oddział i wybór.

<figure><img src="../../../.gitbook/assets/c0ff3fe1-a393-43cc-96a5-3e0cb1d878b7.png" alt="Historyczne okno Text w EVS006 z pustymi polami bloków tekstu i przyciskiem Next"><figcaption><p>Historyczne okno Text w EVS006 z polami bloków tekstu i przyciskiem Next.</p></figcaption></figure>

* [ ] W definicji SupplierPartyMaster wybierz **Related → Run**. Otworzy się **Initial Load Job. Open (EVS007)**; to jeszcze nie dowód, że DocBits otrzymał dane.

<figure><img src="../../../.gitbook/assets/d819fdd5-5b4a-48ef-9412-f211c0d2355f.png" alt="Historyczna lista EVS006 z otwartym menu kontekstowym na wierszu SupplierPartyMaster i pozycją Related &gt; Run"><figcaption><p>Historyczna lista EVS006 z otwartym menu Related → Run na wierszu SupplierPartyMaster.</p></figcaption></figure>

* [ ] Wybierz **Sync** tylko wtedy, gdy odbierający przepływ ION oczekuje Sync.SupplierPartyMaster. Przed wysłaniem EVS007 potwierdź filtry i cel. Pełny import początkowy może wygenerować wiele zdarzeń.

<figure><img src="../../../.gitbook/assets/m3-supplier-initial-load-job-historical-id-masked-20261102.png" alt="Historyczne zadanie Initial Load Job w EVS007 dla CIDMAS i SupplierPartyMaster z czasownikiem BOD Sync i statusem 1-Pending; identyfikator zadania jest zamazany"><figcaption><p>Historyczne zadanie Initial Load Job w EVS007 z CIDMAS, SupplierPartyMaster, Sync i statusem 1-Pending. Identyfikator zadania jest zamazany; status Pending nie dowodzi zakończonego importu.</p></figcaption></figure>

## Sprawdź wynik

Po autoryzowanym uruchomieniu sprawdź w EVS006 w **Related → History** liczbę przetworzonych rekordów i ewentualne błędy. Następnie sprawdź komunikat SupplierPartyMaster w Infor ION i potwierdź, że dotarł do skonfigurowanej organizacji DocBits. Dopiero potem poszukaj w DocBits jednego oczekiwanego dostawcy w **Ustawienia → Wyszukaj dane główne**, na karcie **Dostawca**. Użyj pola wyszukiwania z numerem lub nazwą dostawcy; nie zakładaj, że wszyscy dostawcy M3 dotarli tylko dlatego, że zadanie zostało wysłane.

<figure><img src="../../../.gitbook/assets/m3-supplier-master-data-pl-20261112.png" alt="DocBits Sandbox 11.27.7 po polsku: Ustawienia, Wyszukaj Dane Główne, karta Dostawca z filtrem Szukaj według kolumny, polem Szukaj Tekst i wymyślonymi wierszami dostawców"><figcaption><p>DocBits Sandbox 11.27.7: <strong>Ustawienia → Wyszukaj Dane Główne</strong>, karta <strong>Dostawca</strong>, z filtrem <strong>Szukaj według kolumny</strong> i polem <strong>Szukaj Tekst</strong>. Wiersze SUP-1001 do SUP-1010 to wymyślone dane przykładowe i nie dowodzą importu z M3; nagłówki kolumn tego widoku pozostają w tej wersji interfejsu po angielsku.</p></figcaption></figure>

Zrzut pokazuje wymyślone dane Sandbox, które już znajdowały się w organizacji testowej. Podczas tej aktualizacji dokumentacji nie było podłączonego środowiska M3. Jeśli oczekiwany dostawca nie występuje, porównaj historię EVS006, routing ION i organizację DocBits, zanim ponownie uruchomisz import. Co robią filtr **Szukaj według kolumny**, pole **Szukaj Tekst**, przycisk **Akcje** i stronicowanie w tym widoku, opisuje instrukcja [Wyszukiwanie danych podstawowych](../../../administration-and-setup/settings/document-processing/master-data-lookup.md), sekcja Tabela danych.

### Alternatywa: Panel Dostawcy

Jeśli portal dostawców jest używany i w DocBits dostępny jest widok **Panel Dostawcy**, zaimportowani dostawcy pojawiają się również tam, ponieważ oba widoki czytają te same dane podstawowe dostawców. Szukaj po nazwie lub numerze dostawcy polem **Szukaj według nazwy, numeru**. Liczniki **Wszyscy dostawcy**, **Oczekujące na zatwierdzenie** i **Oczekująca rejestracja**, przycisk filtra w polu wyszukiwania oraz **Dostawca na stronę:** opisuje instrukcja [portalu dostawców](../../../administration-and-setup/setup/supplier-portal/README.md), sekcja Administrator: wyszukiwanie i filtrowanie dostawców.

<figure><img src="../../../.gitbook/assets/m3-supplier-management-search-pl-20261112.png" alt="Widok Panel Dostawcy w DocBits Sandbox po polsku z licznikami Wszyscy dostawcy, Oczekujące na zatwierdzenie i Oczekująca rejestracja, polem Szukaj według nazwy, numeru i wymyślonymi wierszami dostawców"><figcaption><p>DocBits Sandbox 11.27.7: <strong>Panel Dostawcy</strong> z polem <strong>Szukaj według nazwy, numeru</strong> oraz licznikami <strong>Wszyscy dostawcy</strong>, <strong>Oczekujące na zatwierdzenie</strong> i <strong>Oczekująca rejestracja</strong>. Osiem wierszy to wymyślone dane przykładowe i nie dowodzą importu z M3.</p></figcaption></figure>
