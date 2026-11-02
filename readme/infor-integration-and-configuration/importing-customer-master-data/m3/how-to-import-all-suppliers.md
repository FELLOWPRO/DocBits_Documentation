# Jak zaimportować wszystkich dostawców

* [ ] Zaloguj się do środowiska InforOS i przejdź do aplikacji M3. Rekomendacja: Upewnij się, że masz uprawnienia administratora, aby móc uruchamiać wszystkie programy.

![Menu startowe Infor M3 w Infor OS z listą programów, panelami Favorites i Recent oraz otwartym polem wyszukiwania evs006](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/6cf93500-2e90-4cfc-a9fb-5873e5dcb953.png)

* [ ] Uruchom program _**evs006**_. Naciśnij command + R, a zobaczysz otwartą kartę wyszukiwania i uruchamiania.

![Menu startowe Infor M3 z polem wyszukiwania pokazującym pozycję evs006 Initial Load gotową do otwarcia w sekcji Recent](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/f77b242e-eb2f-43b6-8a2e-03d264198e0c.png)

* [ ] Gdy _**evs006**_ jest otwarty, zobaczysz pustą tabelę. Wypełnij kolumny “BOD noun” i “Table”. Dla “BOD noun” wprowadź “SupplierPartyMaster”, a dla “Table” użyjemy tabeli dostawców M3 o nazwie “CIDMAS”.

![Ekran menu Infor M3 z otwartym polem wyszukiwania umożliwiającym uruchomienie programu](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/827a9dbb-c974-4da7-9bd3-f8e87adad60f.png)

![Tabela EVS006 Initial Load z kolumnami BOD noun, BOD variant, Table i BOD description](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/e30c7b86-dcfb-41d2-bd32-447b60e4581b.png)

* [ ] Po wypełnieniu tych kolumn kliknij przycisk CREATE (na górnym pasku ekranu). Przejdziesz do następnego ekranu.

![Pusta tabela EVS006 Initial Load z nagłówkami kolumn BOD noun, BOD variant, Table i BOD description](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/30eee6b2-24ed-4e1f-8812-1304e7dede8e.png)

![Panel EVS006 Initial Load z Table CIDMAS Supplier, BOD noun SupplierPartyMaster oraz sekcjami Details i Table keys](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/461b72d3-d576-4c92-95c2-d175183088af.png)

* [ ] Wypełnij pole “BOD Description” wartością SupplierPartyMaster.

![Panel EVS006 Initial Load z wypełnionym opisem BOD SupplierPartyMaster w sekcji Details](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/4dc345a8-8eca-4e03-800a-37a670f8792e.png)

* [ ] Kliknij Next (w lewym dolnym rogu ekranu).

![Panel EVS006 Initial Load dla tabeli CIDMAS z rzeczownikiem BOD SupplierPartyMaster i przyciskiem Next w lewym dolnym rogu](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/315aa54b-f0bd-4057-a1ed-e476c9000725.png)

* [ ] Kliknij Next w tym oknie.

![Okno dialogowe Text w M3 z kolumnami Text block i Language oraz nazwą InvExt](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/c0ff3fe1-a393-43cc-96a5-3e0cb1d878b7.png)

* [ ] Gdy zobaczysz ten ekran z wypełnioną tabelą z BOD SupplierPartyMaster, kliknij prawym przyciskiem myszy na BOD i wybierz Related > Run.

![Tabela EVS006 Initial Load z wierszem SupplierPartyMaster i jego menu kontekstowym po kliknięciu prawym przyciskiem, obejmującym Related, Run i Change](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/d819fdd5-5b4a-48ef-9412-f211c0d2355f.png)

* [ ] W kolejnym oknie wybierz “Sync” i Next.

![Panel BOD Processor Administration w Infor M3 z zadaniem SupplierPartyMaster, czasownikiem Sync i statusem Pending](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/8fbed442-7deb-4c1e-9295-5038fe124331.png)

Po zakończeniu wszystkich tych kroków aktywowałeś BOD do importu wszystkich dostawców z tabeli CIDMAS. Po kilku minutach powinieneś zobaczyć dostawców w DocBits.
