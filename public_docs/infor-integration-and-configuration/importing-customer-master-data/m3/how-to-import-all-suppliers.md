# Démarrer un chargement initial de fournisseurs depuis Infor M3

N'utilisez cette procédure qu'après que votre administrateur Infor a confirmé la société, la division, le BOD `SupplierPartyMaster` et la route ION DocBits. Un chargement initial sans restriction peut envoyer chaque fournisseur éligible ; convenez donc d'abord d'une petite sélection. Les onze captures d'écran Infor M3 ci-dessous sont des exemples historiques ; comparez-les avec votre locataire avant de lancer une tâche. Cette mise à jour de la page n'a exécuté aucune tâche M3 et n'a importé aucun fournisseur dans DocBits.

Infor décrit la [procédure de chargement initial EVS006](https://docs.infor.com/m3core/latest/en-us/useradminlib_cloud/m3cecoreag_cloud/hmo1553266924239.html) et les [options de sélection et d'exécution EVS007](https://docs.infor.com/m3udi/16.x/en-us/m3beud/appfoundhs/spl1567531742751.html). Si les libellés diffèrent, suivez la procédure approuvée de votre locataire.

* [ ] Ouvrez Infor OS et l'application M3 avec un compte autorisé aux chargements initiaux. Confirmez la société et la division prévues avant de continuer.

<figure><img src="../../../.gitbook/assets/6cf93500-2e90-4cfc-a9fb-5873e5dcb953.png" alt="Écran de démarrage Infor M3 historique avec le menu des modules à gauche et la liste Recent contenant EVS006 Initial Load et BOD Processor Administration"><figcaption><p>Écran de démarrage Infor M3 historique avec EVS006 Initial Load et BOD Processor Administration dans la liste Recent.</p></figcaption></figure>

* [ ] Ouvrez **Initial Load. Open (EVS006)** à l'aide de la recherche de programmes de votre locataire.

<figure><img src="../../../.gitbook/assets/f77b242e-eb2f-43b6-8a2e-03d264198e0c.png" alt="Boîte de dialogue Search and Start d'Infor M3 historique avec un champ de saisie vide et le bouton OK"><figcaption><p>Boîte de dialogue Search and Start d'Infor M3 historique avec son champ de saisie et le bouton OK.</p></figcaption></figure>

* [ ] Dans EVS006, créez une définition de chargement initial pour **SupplierPartyMaster**. L'exemple historique utilise **CIDMAS** comme table. Demandez à l'administrateur M3 de confirmer que cette combinaison de BOD et de table est valide dans votre version et votre intégration.

<figure><img src="../../../.gitbook/assets/827a9dbb-c974-4da7-9bd3-f8e87adad60f.png" alt="Boîte de dialogue Search and Start historique avec evs006 saisi dans le champ de saisie"><figcaption><p>Exemple historique de Search and Start avec EVS006 saisi dans le champ de saisie.</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/e30c7b86-dcfb-41d2-bd32-447b60e4581b.png" alt="Liste de chargement initial EVS006 historique avec SupplierPartyMaster comme BOD noun et CIDMAS comme table"><figcaption><p>Liste de chargement initial EVS006 historique avec SupplierPartyMaster comme BOD noun et CIDMAS comme table.</p></figcaption></figure>

* [ ] Sélectionnez **Create** et vérifiez la définition avant de poursuivre.

<figure><img src="../../../.gitbook/assets/30eee6b2-24ed-4e1f-8812-1304e7dede8e.png" alt="Liste EVS006 historique avec le bouton Create (plus) de la barre d'outils mis en évidence en rouge"><figcaption><p>Liste EVS006 historique avec le bouton Create de la barre d'outils mis en évidence.</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/461b72d3-d576-4c92-95c2-d175183088af.png" alt="Panneau de création EVS006 historique pour la table CIDMAS avec le champ BOD Description encore vide"><figcaption><p>Panneau de création EVS006 historique pour CIDMAS avec le champ BOD Description encore vide.</p></figcaption></figure>

* [ ] Saisissez une **BOD Description** explicite, par exemple **SupplierPartyMaster initial load for DocBits**.

<figure><img src="../../../.gitbook/assets/4dc345a8-8eca-4e03-800a-37a670f8792e.png" alt="Panneau de création EVS006 historique avec SupplierPartyMaster saisi comme BOD Description"><figcaption><p>Panneau de création EVS006 historique avec SupplierPartyMaster saisi comme BOD Description.</p></figcaption></figure>

* [ ] Sélectionnez **Next** et définissez, lorsque cela est possible, une sélection convenue. Infor recommande des critères de sélection pour éviter de déclencher trop d'événements.

<figure><img src="../../../.gitbook/assets/315aa54b-f0bd-4057-a1ed-e476c9000725.png" alt="Panneau de création EVS006 historique avec le bouton Next mis en évidence en bas à droite"><figcaption><p>Panneau de création EVS006 historique avec le bouton Next mis en évidence.</p></figcaption></figure>

* [ ] Poursuivez avec les paramètres d'exécution. Vérifiez à nouveau la société, la division et la sélection.

<figure><img src="../../../.gitbook/assets/c0ff3fe1-a393-43cc-96a5-3e0cb1d878b7.png" alt="Boîte de dialogue Text d'EVS006 historique avec des champs de bloc de texte vides et le bouton Next"><figcaption><p>Boîte de dialogue Text d'EVS006 historique avec des champs de bloc de texte et un bouton Next.</p></figcaption></figure>

* [ ] Dans la définition SupplierPartyMaster, choisissez **Related → Run**. Cela ouvre **Initial Load Job. Open (EVS007)** ; cela ne prouve pas encore que DocBits a reçu les données.

<figure><img src="../../../.gitbook/assets/d819fdd5-5b4a-48ef-9412-f211c0d2355f.png" alt="Liste EVS006 historique avec le menu contextuel ouvert sur la ligne SupplierPartyMaster et l'entrée Related &gt; Run"><figcaption><p>Liste EVS006 historique avec le menu Related → Run ouvert sur la ligne SupplierPartyMaster.</p></figcaption></figure>

* [ ] Choisissez **Sync** uniquement si le flux ION récepteur attend Sync.SupplierPartyMaster. Confirmez les filtres et la cible avant de soumettre EVS007. Un chargement initial complet peut générer de nombreux événements.

<figure><img src="../../../.gitbook/assets/m3-supplier-initial-load-job-historical-id-masked-20261102.png" alt="Tâche de chargement initial EVS007 historique pour CIDMAS et SupplierPartyMaster avec le verbe BOD Sync et le statut 1-Pending ; l'identifiant de la tâche est masqué"><figcaption><p>Tâche de chargement initial EVS007 historique avec CIDMAS, SupplierPartyMaster, Sync et le statut 1-Pending. L'identifiant de la tâche est masqué ; le statut Pending ne prouve pas un import terminé.</p></figcaption></figure>

## Vérifier le résultat

Après une exécution autorisée, vérifiez sous **Related → History** dans EVS006 le nombre traité et les éventuelles erreurs. Vérifiez ensuite le message SupplierPartyMaster dans Infor ION et confirmez qu'il a atteint l'organisation DocBits configurée. Cherchez seulement ensuite un fournisseur attendu dans DocBits sous **Paramètres → Consultation des données de base**, onglet **Fournisseur**. Utilisez la recherche avec le numéro ou le nom du fournisseur ; ne partez pas du principe que tous les fournisseurs M3 sont arrivés simplement parce que la tâche a été soumise.

<figure><img src="../../../.gitbook/assets/m3-supplier-master-data-fr-20261112.png" alt="Interface DocBits de la Sandbox 11.27.7 en français : Paramètres, Consultation des données de base, onglet Fournisseur avec le filtre Rechercher par colonne, le champ Recherche Chaîne et des lignes de fournisseurs inventées"><figcaption><p>DocBits Sandbox 11.27.7 : <strong>Paramètres → Consultation des données de base</strong>, onglet <strong>Fournisseur</strong>, avec le filtre <strong>Rechercher par colonne</strong> et le champ <strong>Recherche Chaîne</strong>. Les lignes SUP-1001 à SUP-1010 sont des données d'exemple inventées et ne prouvent pas un import M3 ; les en-têtes de colonnes de cette vue restent en anglais dans cette version de l'interface.</p></figcaption></figure>

La capture montre des données de Sandbox inventées, déjà présentes dans l'organisation de test. Aucun locataire M3 n'était connecté lors de cette mise à jour de la documentation. Si le fournisseur attendu manque, comparez l'historique EVS006, le routage ION et l'organisation DocBits avant de relancer le chargement.

### Alternative : Tableau de Bord Fournisseur

Si le portail fournisseurs est utilisé et que l'entrée **Tableau De Bord Fournisseur** apparaît dans le menu principal, les fournisseurs importés y apparaissent aussi, car les deux vues lisent les mêmes données de base fournisseurs. Recherchez par nom ou par numéro de fournisseur avec le champ **Recherche par nom, numéro**. Le fonctionnement de cette vue est décrit dans le guide du [portail fournisseurs](../../../administration-and-setup/setup/supplier-portal/README.md).

<figure><img src="../../../.gitbook/assets/m3-supplier-management-search-fr-20261112.png" alt="Tableau De Bord Fournisseur de la Sandbox DocBits en français avec les onglets tous les fournisseurs, En attente de validation et Enregistrement en cours, le champ Recherche par nom, numéro et des lignes de fournisseurs inventées"><figcaption><p>DocBits Sandbox 11.27.7 : <strong>Tableau De Bord Fournisseur</strong> avec le champ <strong>Recherche par nom, numéro</strong> et les onglets <strong>tous les fournisseurs</strong>, <strong>En attente de validation</strong> et <strong>Enregistrement en cours</strong>. Les huit lignes sont des données d'exemple inventées et ne prouvent pas un import M3.</p></figcaption></figure>
