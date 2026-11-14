# Een eerste leveranciersimport vanuit Infor M3 starten

Gebruik deze procedure pas nadat je Infor-beheerder het bedrijf, de divisie, de BOD `SupplierPartyMaster` en de DocBits ION-route heeft bevestigd. Een onbeperkte eerste import kan elke in aanmerking komende leverancier versturen, dus spreek eerst een kleine selectie af. De elf onderstaande Infor M3-schermafbeeldingen zijn historische voorbeelden; vergelijk ze met je eigen omgeving voordat je een taak start. Bij deze update van de pagina is geen M3-taak uitgevoerd en zijn geen leveranciers in DocBits geïmporteerd.

Infor beschrijft de [procedure voor een eerste import in EVS006](https://docs.infor.com/m3core/latest/en-us/useradminlib_cloud/m3cecoreag_cloud/hmo1553266924239.html) en de [selectie- en uitvoeringsopties van EVS007](https://docs.infor.com/m3udi/16.x/en-us/m3beud/appfoundhs/spl1567531742751.html). Volg de goedgekeurde procedure van je eigen omgeving als de labels afwijken.

* [ ] Open Infor OS en de M3-toepassing met een account dat bevoegd is voor eerste imports. Bevestig het bedoelde bedrijf en de divisie voordat je verdergaat.

<figure><img src="../../../.gitbook/assets/6cf93500-2e90-4cfc-a9fb-5873e5dcb953.png" alt="Historisch Infor M3-startscherm met het modulemenu links en de lijst Recent met EVS006 Initial Load en BOD Processor Administration"><figcaption><p>Historisch Infor M3-startscherm met EVS006 Initial Load en BOD Processor Administration in de lijst Recent.</p></figcaption></figure>

* [ ] Open **Initial Load. Open (EVS006)** met de programmazoekfunctie van je eigen omgeving.

<figure><img src="../../../.gitbook/assets/f77b242e-eb2f-43b6-8a2e-03d264198e0c.png" alt="Historisch dialoogvenster Search and Start van Infor M3 met een leeg invoerveld en de knop OK"><figcaption><p>Historisch dialoogvenster Search and Start van Infor M3 met het invoerveld en de knop OK.</p></figcaption></figure>

* [ ] Maak in EVS006 een definitie voor een eerste import voor **SupplierPartyMaster**. Het historische voorbeeld gebruikt **CIDMAS** als tabel. Vraag de M3-beheerder te bevestigen dat deze combinatie van BOD en tabel geldig is in jouw versie en integratie.

<figure><img src="../../../.gitbook/assets/827a9dbb-c974-4da7-9bd3-f8e87adad60f.png" alt="Historisch dialoogvenster Search and Start met evs006 ingevuld in het invoerveld"><figcaption><p>Historisch voorbeeld van Search and Start met EVS006 ingevuld in het invoerveld.</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/e30c7b86-dcfb-41d2-bd32-447b60e4581b.png" alt="Historische EVS006-lijst Initial Load met SupplierPartyMaster als BOD noun en CIDMAS als tabel"><figcaption><p>Historische EVS006-lijst Initial Load met SupplierPartyMaster als BOD noun en CIDMAS als tabel.</p></figcaption></figure>

* [ ] Selecteer **Create** en controleer de definitie voordat je verdergaat.

<figure><img src="../../../.gitbook/assets/30eee6b2-24ed-4e1f-8812-1304e7dede8e.png" alt="Historische EVS006-lijst met de knop Create (plus) in de werkbalk rood gemarkeerd"><figcaption><p>Historische EVS006-lijst met de knop Create in de werkbalk gemarkeerd.</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/461b72d3-d576-4c92-95c2-d175183088af.png" alt="Historisch aanmaakvenster van EVS006 voor tabel CIDMAS met een nog leeg veld BOD description"><figcaption><p>Historisch aanmaakvenster van EVS006 voor CIDMAS met het veld BOD description nog leeg.</p></figcaption></figure>

* [ ] Vul een duidelijke **BOD Description** in, bijvoorbeeld **SupplierPartyMaster initial load for DocBits**.

<figure><img src="../../../.gitbook/assets/4dc345a8-8eca-4e03-800a-37a670f8792e.png" alt="Historisch aanmaakvenster van EVS006 met SupplierPartyMaster ingevuld als BOD description"><figcaption><p>Historisch aanmaakvenster van EVS006 met SupplierPartyMaster ingevuld als BOD description.</p></figcaption></figure>

* [ ] Selecteer **Next** en stel waar mogelijk een afgesproken selectie in. Infor raadt selectiecriteria aan om te voorkomen dat te veel gebeurtenissen worden gestart.

<figure><img src="../../../.gitbook/assets/315aa54b-f0bd-4057-a1ed-e476c9000725.png" alt="Historisch aanmaakvenster van EVS006 met de knop Next rechtsonder gemarkeerd"><figcaption><p>Historisch aanmaakvenster van EVS006 met de knop Next gemarkeerd.</p></figcaption></figure>

* [ ] Ga verder naar de instellingen voor de uitvoering. Controleer bedrijf, divisie en selectie nog een keer.

<figure><img src="../../../.gitbook/assets/c0ff3fe1-a393-43cc-96a5-3e0cb1d878b7.png" alt="Historisch dialoogvenster Text in EVS006 met lege tekstblokvelden en de knop Next"><figcaption><p>Historisch dialoogvenster Text in EVS006 met tekstblokvelden en een knop Next.</p></figcaption></figure>

* [ ] Kies in de definitie SupplierPartyMaster **Related → Run**. Daarmee open je **Initial Load Job. Open (EVS007)**; dat is nog geen bewijs dat DocBits de gegevens heeft ontvangen.

<figure><img src="../../../.gitbook/assets/d819fdd5-5b4a-48ef-9412-f211c0d2355f.png" alt="Historische EVS006-lijst met het contextmenu geopend op de regel SupplierPartyMaster en de optie Related &gt; Run"><figcaption><p>Historische EVS006-lijst met het menu Related → Run geopend op de regel SupplierPartyMaster.</p></figcaption></figure>

* [ ] Kies **Sync** alleen als de ontvangende ION-flow Sync.SupplierPartyMaster verwacht. Bevestig de filters en het doel voordat je EVS007 indient. Een volledige eerste import kan veel gebeurtenissen opleveren.

<figure><img src="../../../.gitbook/assets/m3-supplier-initial-load-job-historical-id-masked-20261102.png" alt="Historische EVS007 Initial Load Job voor CIDMAS en SupplierPartyMaster met BOD-werkwoord Sync en status 1-Pending; de taakidentificatie is gemaskeerd"><figcaption><p>Historische EVS007 Initial Load Job met CIDMAS, SupplierPartyMaster, Sync en status 1-Pending. De taakidentificatie is gemaskeerd; de status Pending bewijst geen voltooide import.</p></figcaption></figure>

## Het resultaat controleren

Controleer na een geautoriseerde uitvoering in EVS006 onder **Related → History** hoeveel records zijn verwerkt en of er fouten zijn opgetreden. Controleer daarna het bericht SupplierPartyMaster in Infor ION en bevestig dat het de geconfigureerde DocBits-organisatie heeft bereikt. Zoek pas daarna in DocBits naar één verwachte leverancier onder **Instellingen → Stamgegevens Opzoeken**, tabblad **Leverancier**. Gebruik het zoekveld met het leveranciersnummer of de naam; ga er niet van uit dat alle M3-leveranciers zijn aangekomen alleen omdat de taak is ingediend.

<figure><img src="../../../.gitbook/assets/m3-supplier-master-data-nl-20261112.png" alt="DocBits Sandbox 11.27.7 in het Nederlands: Instellingen, Stamgegevens Opzoeken, tabblad Leverancier met het filter Zoeken op kolom, het veld Zoekopdracht Tekenreeks en verzonnen leveranciersregels"><figcaption><p>DocBits Sandbox 11.27.7: <strong>Instellingen → Stamgegevens Opzoeken</strong>, tabblad <strong>Leverancier</strong>, met het filter <strong>Zoeken op kolom</strong> en het veld <strong>Zoekopdracht Tekenreeks</strong>. De regels SUP-1001 tot en met SUP-1010 zijn verzonnen voorbeeldgegevens en bewijzen geen M3-import; de kolomkoppen van deze weergave blijven in deze versie van de interface Engels.</p></figcaption></figure>

De opname toont verzonnen gegevens uit de Sandbox die al in de testorganisatie aanwezig waren. Er was geen M3-omgeving aangesloten bij deze update van de documentatie. Ontbreekt de verwachte leverancier, vergelijk dan de EVS006-geschiedenis, de ION-routering en de DocBits-organisatie voordat je de import opnieuw start. Wat het filter **Zoeken op kolom**, het veld **Zoekopdracht Tekenreeks**, de knop **Acties** en de paginering in deze weergave doen, staat in de handleiding [Stamgegevens opzoeken](../../../administration-and-setup/settings/document-processing/master-data-lookup.md), sectie Gegevenstabel.

### Alternatief: Leveranciersdashboard

Als de leveranciersportal in gebruik is en de ingang **Leveranciersdashboard** in het hoofdmenu staat, verschijnen de geïmporteerde leveranciers daar ook, omdat beide weergaven dezelfde stamgegevens van leveranciers lezen. Zoek op leveranciersnaam of -nummer met **Zoeken op naam, nummer**. De totalen **Alle leveranciers**, **In afwachting van goedkeuring** en **In afwachting van registratie**, de filterknop in het zoekveld en **Leverancier per pagina** worden uitgelegd in de handleiding van de [leveranciersportal](../../../administration-and-setup/setup/supplier-portal/README.md), sectie Admin: leveranciers zoeken en filteren.

<figure><img src="../../../.gitbook/assets/m3-supplier-management-search-nl-20261112.png" alt="Leveranciersdashboard van de DocBits Sandbox in het Nederlands met de tabbladen Alle leveranciers, In afwachting van goedkeuring en In afwachting van registratie, het veld Zoeken op naam, nummer en verzonnen leveranciersregels"><figcaption><p>DocBits Sandbox 11.27.7: <strong>Leveranciersdashboard</strong> met het veld <strong>Zoeken op naam, nummer</strong> en de tabbladen <strong>Alle leveranciers</strong>, <strong>In afwachting van goedkeuring</strong> en <strong>In afwachting van registratie</strong>. De acht regels zijn verzonnen voorbeeldgegevens en bewijzen geen M3-import.</p></figcaption></figure>
