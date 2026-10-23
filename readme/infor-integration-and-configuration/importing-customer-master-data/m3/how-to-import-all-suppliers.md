# Comment importer tous les fournisseurs

* [ ] Connectez-vous à l’environnement Infor OS et allez dans l’application M3. Recommandation : Assurez-vous d’avoir des droits d’administrateur afin de pouvoir exécuter tous les programmes.

![Menu de démarrage Infor M3 dans Infor OS avec la liste des programmes, les panneaux Favorites et Recent et le champ de recherche evs006 ouvert](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/6cf93500-2e90-4cfc-a9fb-5873e5dcb953.png)

* [ ] Exécutez le programme _**evs006**_. Appuyez sur command + R et vous verrez l’onglet ouvert pour rechercher et démarrer.

![Menu de démarrage Infor M3 avec le champ de recherche affichant evs006 Initial Load prêt à ouvrir sous Recent](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/f77b242e-eb2f-43b6-8a2e-03d264198e0c.png)

* [ ] Lorsque _**evs006**_ est ouvert, vous verrez un tableau vide. Veuillez remplir les colonnes “BOD noun” et “Table”. Pour “BOD noun”, saisissez “SupplierPartyMaster” et pour “Table”, nous allons utiliser la table fournisseur M3 appelée “CIDMAS”.

![Écran de menu d'Infor M3 avec le champ de recherche ouvert pour démarrer un programme](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/827a9dbb-c974-4da7-9bd3-f8e87adad60f.png)

![Table EVS006 Initial Load avec les colonnes BOD noun, BOD variant, Table et BOD description](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/e30c7b86-dcfb-41d2-bd32-447b60e4581b.png)

* [ ] Une fois ces colonnes renseignées, cliquez simplement sur le bouton CREATE (sur la barre supérieure de l’écran). Vous arriverez à l’écran suivant.

![Table vide EVS006 Initial Load avec les en-têtes de colonnes BOD noun, BOD variant, Table et BOD description](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/30eee6b2-24ed-4e1f-8812-1304e7dede8e.png)

![Panneau EVS006 Initial Load avec Table CIDMAS Supplier, BOD noun SupplierPartyMaster et les sections Details et Table keys](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/461b72d3-d576-4c92-95c2-d175183088af.png)

* [ ] Renseignez “BOD Description” avec SupplierPartyMaster.

![Panneau EVS006 Initial Load avec la description BOD SupplierPartyMaster renseignée sous Details](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/4dc345a8-8eca-4e03-800a-37a670f8792e.png)

* [ ] Cliquez sur Next. (En bas à gauche de l’écran).

![Panneau EVS006 Initial Load pour la table CIDMAS avec le nom BOD SupplierPartyMaster et le bouton Next en bas à gauche](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/315aa54b-f0bd-4057-a1ed-e476c9000725.png)

* [ ] Cliquez sur Next dans cette fenêtre.

![Boîte de dialogue Text dans M3 avec les colonnes Text block et Language et le nom InvExt](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/c0ff3fe1-a393-43cc-96a5-3e0cb1d878b7.png)

* [ ] Maintenant, lorsque vous voyez cet écran avec le tableau rempli avec le BOD SupplierPartyMaster, faites un clic droit sur le BOD et choisissez Related > Run.

![Table EVS006 Initial Load avec la ligne SupplierPartyMaster et son menu contextuel du clic droit incluant Related, Run et Change](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/d819fdd5-5b4a-48ef-9412-f211c0d2355f.png)

* [ ] Dans la fenêtre suivante, sélectionnez “Sync” puis Next.

![Panneau BOD Processor Administration dans Infor M3 avec le travail SupplierPartyMaster, le verbe Sync et le statut Pending](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/8fbed442-7deb-4c1e-9295-5038fe124331.png)

Après avoir terminé toutes ces étapes, vous avez activé le BOD pour importer tous les fournisseurs depuis la table CIDMAS. Après quelques minutes, vous devriez voir le fournisseur dans DocBits.
