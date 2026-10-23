# Alle leveranciers importeren

* [ ] Log jezelf in op de InforOS-omgeving en ga naar de M3-applicatie. Aanbeveling: Zorg ervoor dat je adminrechten hebt zodat je alle programma’s kunt uitvoeren.

![Startmenu van Infor M3 in Infor OS met de programmalijst, de panelen Favorites en Recent en het geopende zoekveld evs006](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/6cf93500-2e90-4cfc-a9fb-5873e5dcb953.png)

* [ ] Voer het programma _**evs006**_ uit. Druk op command + R en je ziet het tabblad om te zoeken en te starten.

![Infor M3-startmenu met het zoekveld dat onder Recent evs006 Initial Load klaar om te openen toont](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/f77b242e-eb2f-43b6-8a2e-03d264198e0c.png)

* [ ] Wanneer _**evs006**_ is geopend, zie je een lege tabel. Vul de kolommen “BOD noun” en “Table” in. Voor “BOD noun” voer je “SupplierPartyMaster” in en voor “Table” gebruiken we de M3 supplier table genaamd “CIDMAS”.

![Menuscherm van Infor M3 met het zoekveld geopend om een programma te starten](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/827a9dbb-c974-4da7-9bd3-f8e87adad60f.png)

![Tabel EVS006 Initial Load met de kolommen BOD noun, BOD variant, Table en BOD description](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/e30c7b86-dcfb-41d2-bd32-447b60e4581b.png)

* [ ] Wanneer je deze kolommen hebt ingevuld, klik op de knop CREATE (aan de bovenkant van het scherm). Je komt op het volgende scherm.

![Lege tabel EVS006 Initial Load met de kolomkoppen BOD noun, BOD variant, Table en BOD description](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/30eee6b2-24ed-4e1f-8812-1304e7dede8e.png)

![Paneel EVS006 Initial Load met Table CIDMAS Supplier, BOD noun SupplierPartyMaster en de secties Details en Table keys](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/461b72d3-d576-4c92-95c2-d175183088af.png)

* [ ] Vul “BOD Description” met SupplierPartyMaster.

![Paneel EVS006 Initial Load met de BOD-beschrijving SupplierPartyMaster ingevuld onder Details](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/4dc345a8-8eca-4e03-800a-37a670f8792e.png)

* [ ] Klik op Next. (Linksonder in het scherm).

![EVS006 Initial Load-paneel voor de tabel CIDMAS met het BOD-naamwoord SupplierPartyMaster en de knop Next linksonder](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/315aa54b-f0bd-4057-a1ed-e476c9000725.png)

* [ ] Klik in dit venster op Next.

![Dialoogvenster Text in M3 met de kolommen Text block en Language en de naam InvExt](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/c0ff3fe1-a393-43cc-96a5-3e0cb1d878b7.png)

* [ ] Wanneer je dit scherm ziet met de ingevulde tabel met de BOD SupplierPartyMaster, klik met de rechtermuisknop op de BOD en kies Related > Run.

![EVS006 Initial Load-tabel met de rij SupplierPartyMaster en het rechtsklik-contextmenu ervan met Related, Run en Change](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/d819fdd5-5b4a-48ef-9412-f211c0d2355f.png)

* [ ] Selecteer in het volgende venster “Sync” en Next.

![Paneel BOD Processor Administration in Infor M3 met de job SupplierPartyMaster, het werkwoord Sync en de status Pending](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/8fbed442-7deb-4c1e-9295-5038fe124331.png)

Na het voltooien van al deze stappen heb je de BOD geactiveerd om alle leveranciers uit tabel CIDMAS te importeren. Na enkele minuten zou je de leveranciers in DocBits moeten zien. \\
