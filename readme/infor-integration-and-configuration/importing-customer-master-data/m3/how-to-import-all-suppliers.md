# Come importare tutti i fornitori

* [ ] Effettua l’accesso all’ambiente Infor OS e vai all’applicazione M3. Raccomandazione: Assicurati di avere diritti admin per poter eseguire tutti i programmi.

![Menu di avvio di Infor M3 in Infor OS con l'elenco dei programmi, i pannelli Favorites e Recent e il campo di ricerca evs006 aperto](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/6cf93500-2e90-4cfc-a9fb-5873e5dcb953.png)

* [ ] Esegui il programma _**evs006**_. Premi Command + R e vedrai la scheda aperta per cercare e avviare.

![Menu di avvio di Infor M3 con il campo di ricerca che mostra evs006 Initial Load pronto per l'apertura sotto Recent](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/f77b242e-eb2f-43b6-8a2e-03d264198e0c.png)

* [ ] Quando _**evs006**_ è aperto vedrai una tabella vuota. Compila le colonne “BOD noun” e “Table”. Per “BOD noun” inserisci “SupplierPartyMaster” e per “Table” useremo la tabella fornitori di M3 chiamata “CIDMAS”.

![Schermata del menu di Infor M3 con il campo di ricerca aperto per avviare un programma](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/827a9dbb-c974-4da7-9bd3-f8e87adad60f.png)

![Tabella EVS006 Initial Load con le colonne BOD noun, BOD variant, Table e BOD description](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/e30c7b86-dcfb-41d2-bd32-447b60e4581b.png)

* [ ] Una volta compilate queste colonne, fai clic sul pulsante CREATE (nella barra superiore dello schermo). Arriverai alla seguente schermata.

![Tabella vuota EVS006 Initial Load con le intestazioni di colonna BOD noun, BOD variant, Table e BOD description](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/30eee6b2-24ed-4e1f-8812-1304e7dede8e.png)

![Pannello EVS006 Initial Load con Table CIDMAS Supplier, BOD noun SupplierPartyMaster e le sezioni Details e Table keys](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/461b72d3-d576-4c92-95c2-d175183088af.png)

* [ ] Compila “BOD Description” con SupplierPartyMaster.

![Pannello EVS006 Initial Load con la descrizione BOD SupplierPartyMaster compilata in Details](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/4dc345a8-8eca-4e03-800a-37a670f8792e.png)

* [ ] Fai clic su Next. (Nella parte in basso a sinistra dello schermo).

![Pannello EVS006 Initial Load per la tabella CIDMAS con il nome BOD SupplierPartyMaster e il pulsante Next in basso a sinistra](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/315aa54b-f0bd-4057-a1ed-e476c9000725.png)

* [ ] Fai clic su Next in questa finestra.

![Finestra di dialogo Text in M3 con le colonne Text block e Language e il nome InvExt](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/c0ff3fe1-a393-43cc-96a5-3e0cb1d878b7.png)

* [ ] Ora, quando vedi questa schermata con la tabella compilata con il BOD SupplierPartyMaster, fai clic destro sul BOD e scegli Related > Run.

![Tabella EVS006 Initial Load con la riga SupplierPartyMaster e il suo menu contestuale del clic destro che include Related, Run e Change](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/d819fdd5-5b4a-48ef-9412-f211c0d2355f.png)

* [ ] Nella finestra successiva seleziona “Sync” e Next.

![Pannello BOD Processor Administration in Infor M3 con il job SupplierPartyMaster, il verbo Sync e lo stato Pending](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/8fbed442-7deb-4c1e-9295-5038fe124331.png)

Dopo aver completato tutti questi passaggi hai attivato il BOD per importare tutti i fornitori dalla tabella CIDMAS. Dopo alcuni minuti dovresti vedere il fornitore in DocBits. \\
