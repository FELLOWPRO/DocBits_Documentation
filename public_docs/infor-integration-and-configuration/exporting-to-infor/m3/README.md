# Exportation vers Infor M3

Cette page décrit le flux Infor ION et la configuration d’exportation dans DocBits. Les images Infor ci-dessous sont des exemples historiques ; leurs menus et leurs réglages de flux de données doivent être vérifiés dans votre propre tenant avant l’activation. La section DocBits utilise des captures françaises de l’interface de la sandbox (version 11.27.7) avec des données d’exemple inventées, réalisées le 12 novembre 2026. Pour cette mise à jour, ni une connexion Infor ni une exportation de facture n’ont été testées.

## Étape 1 : Créer un Connection Point dans Infor ION

1. Accédez à **OS > ION > Connect > Connection Points**.
2. Cliquez sur **Add** et sélectionnez **IMS via API Gateway** comme type de connexion.
3. Configurez les paramètres suivants :
   * **Name** : saisissez `DocBits_Export`.
   * **Description** : saisissez `DocBits_Export`.
   * **Décochez** : _Application has IMS End Point_.
   * **ION API Client ID** :
     * Ouvrez le fichier ION API.
     * Recherchez `"ci"` dans le fichier.
     * Copiez la valeur de l’identifiant client `ci`. Gardez le fichier `.ionapi` complet confidentiel, car il contient aussi des identifiants d’accès. Infor décrit les [champs du fichier](https://docs.infor.com/crm/9.4.x/en-us/webclient/upi1639111995644.html).

<figure><img src="../../../.gitbook/assets/export_to_m3_from_docbits_1.png" alt="Exemple historique d’Infor ION en anglais, onglet Connection : le Connection Point DocBits_Export utilise IMS via API Gateway, la case Application has IMS End Point n’est pas cochée et le champ ION API Client ID est vide."><figcaption><p>Exemple historique d’un Connection Point. L’onglet Connection est sélectionné ; utilisez l’identifiant client de votre propre fichier ION API, conservé confidentiellement.</p></figcaption></figure>

4. Sous **Documents**, ajoutez `Sync.CaptureDocument`.

<figure><img src="../../../.gitbook/assets/export_to_m3_from_docbits_2.png" alt="Exemple historique d’Infor ION en anglais, onglet Documents : Sync.CaptureDocument est sélectionné comme Send from Application."><figcaption><p>Onglet Documents historique : Sync.CaptureDocument est activé pour Send from Application.</p></figcaption></figure>

5. Cliquez sur **Save** pour finaliser la configuration.

## Étape 2 : Télécharger les mappages

{% file src="../../../.gitbook/assets/CaptureDocument_to_ProcessSupplierInvoice.xml" %}

1. Téléchargez l’exemple de mappage M3 (XML) ci-dessus. Faites-le vérifier par votre administrateur d’intégration pour votre tenant avant de l’importer.
2. Accédez à **Infor** > **OS** > **ION** > **Connect** > **Mappings**.
3. Cliquez sur **Import** et sélectionnez le fichier de mappage correspondant à **M3**.

<figure><img src="../../../.gitbook/assets/export_to_m3_from_docbits_3.png" alt="Extrait historique et recadré de la zone des mappages Infor ION : une flèche cyan désigne l’icône Import au-dessus de la zone Add."><figcaption><p>Action d’importation historique dans la zone des mappages. La flèche cyan marque l’icône Import.</p></figcaption></figure>

4. Vérifiez le mappage importé ainsi que ses BOD source et cible, puis utilisez **Approve** conformément au processus de modification de votre tenant.

<figure><img src="../../../.gitbook/assets/export_to_m3_from_docbits_4.png" alt="Exemple historique d’Infor ION en anglais : le mappage est affiché et l’action Approve est visible."><figcaption><p>Exemple de mappage historique : vérifiez les BOD source et cible avant d’utiliser Approve.</p></figcaption></figure>

## Étape 3 : Créer le Data Flow

1. Accédez à **OS** -> **ION** -> **Connect** -> **Data Flows**.
2. Cliquez sur **Add** et sélectionnez **Document Flow**.
3. Saisissez les détails :
   * **Name** : `DocBits_Export_to_M3`
4. Ajoutez des nœuds au flux :

#### Nœud d’application

1. Ajoutez un **Application Node** au flux.
   * **Name** : `DocBits` ou `DocBits-Export`.
2. Cliquez sur **Add** et sélectionnez le **Connection Point** créé à l’étape 1.

<figure><img src="../../../.gitbook/assets/export_to_m3_from_docbits_5.png" alt="Exemple historique d’Infor ION en anglais : nœud d’application DocBits sélectionné dans le flux, avec les Application Activity Properties sous la zone de dessin et un connection point de démonstration."><figcaption><p>Nœud d’application DocBits historique. Sélectionnez le Connection Point créé pour votre propre tenant ; le nom de démonstration est un exemple.</p></figcaption></figure>

3. Cliquez sur l’**icône de document** à côté du nœud d’application.
   * Cliquez sur **Add** et sélectionnez `Sync.CaptureDocument`.

<figure><img src="../../../.gitbook/assets/export_to_m3_from_docbits_6.png" alt="Exemple historique d’Infor ION en anglais : nœud d’application DocBits avec la zone Documents sous la zone de dessin, contenant Sync.CaptureDocument."><figcaption><p>Zone Documents historique du nœud DocBits : Sync.CaptureDocument.</p></figcaption></figure>

#### Nœud de mappage

1. Ajoutez un **Mapping Node** à droite du nœud d’application.
   * **Name** : `Capt2process`.
   * **Mapping** : sélectionnez le mappage importé de `Sync.CaptureDocument` vers `Process.SupplierInvoice`. Son nom affiché peut différer du nom du fichier XML téléchargé ; l’exemple historique ci-dessous utilise `SyncCaptDoc_SyncSuppInv`.

<figure><img src="../../../.gitbook/assets/export_to_m3_from_docbits_7.png" alt="Exemple historique d’Infor ION en anglais : nœud de mappage Capt2process avec les Mapping Properties sous la zone de dessin et le mappage d’exemple SyncCaptDoc_SyncSuppInv sélectionné."><figcaption><p>Nœud de mappage historique. SyncCaptDoc_SyncSuppInv est le nom du mappage dans cet exemple ; le vôtre peut porter un autre nom.</p></figcaption></figure>

#### Nœud d’application

1. Ajoutez un **Application Node** à droite du nœud de mappage précédent.
   * **Name** : `M3`.
2. Cliquez sur **Add** et sélectionnez l’**Application M3** du client.

<figure><img src="../../../.gitbook/assets/export_to_m3_from_docbits_8.png" alt="Exemple historique d’Infor ION en anglais : nœud d’application M3 avec les Application Activity Properties sous la zone de dessin et une application de démonstration pour les BOD M3."><figcaption><p>Nœud d’application M3 historique. Sélectionnez le Connection Point M3 fourni pour votre tenant.</p></figcaption></figure>

3. Cliquez sur l’**icône de document** à côté du nœud d’application.
   * Cliquez sur **Add** et sélectionnez `Acknowledge.SupplierInvoice`.

<figure><img src="../../../.gitbook/assets/export_to_m3_from_docbits_9.png" alt="Exemple historique d’Infor ION en anglais : nœud d’application M3 avec la zone Documents sous la zone de dessin, contenant Acknowledge.SupplierInvoice."><figcaption><p>Zone Documents historique du nœud M3 : Acknowledge.SupplierInvoice.</p></figcaption></figure>

#### Nœud API

1. Ajoutez un **API Node** à droite du nœud d’application.
   * **Name** : `DocBits-Error`.
   * **ION API Connector** : `DocBits_Import`.
   * Si votre connecteur d’importation n’existe pas, consultez le guide [Importer les données de base Infor M3 via l’API ION](../../importing-customer-master-data/m3/import-from-infor-m3-to-docbits-via-api.md) et faites-le vérifier par votre administrateur Infor avant l’activation.

<figure><img src="../../../.gitbook/assets/export_to_m3_from_docbits_10.png" alt="Exemple historique d’Infor ION en anglais : nœud API DocBits-Error avec les ION API Activity Properties sous la zone de dessin et un connecteur d’importation de démonstration sélectionné."><figcaption><p>Nœud API historique pour le traitement des erreurs. Le connecteur de démonstration sélectionné est un exemple ; utilisez votre propre connecteur d’importation.</p></figcaption></figure>

#### Enregistrer et activer le flux

* Une fois tous les nœuds ajoutés et configurés, cliquez sur **Save**.
* Activez le flux pour terminer la configuration.

<figure><img src="../../../.gitbook/assets/m3-historical-ion-activation-example.png" alt="Extrait historique et recadré de la barre d’outils d’un flux : une flèche cyan désigne l’icône d’activation."><figcaption><p>Barre d’activation historique. La flèche cyan marque l’activation ; cet extrait ne montre pas le flux complet.</p></figcaption></figure>

## Étape 4 : Configurer l’exportation dans DocBits

Dans la bonne organisation DocBits, ouvrez **Paramètres → Exporter** et choisissez **Nouveau**. La page porte le titre **Exporter** ; une configuration d’exportation encore non enregistrée s’ouvre.

<figure><img src="../../../.gitbook/assets/m3-export-liste-fr-20261112.png" alt="Page DocBits française Exporter (version 11.27.7) avec des données d’exemple inventées : la liste des configurations est vide et affiche Aucune configuration, le bouton Nouveau se trouve au-dessus des colonnes Type, Sous-Organisations, Titre, Méthode D’exportation et Actions."><figcaption><p>Capture française de la sandbox avec des données d’exemple inventées : la page Exporter est encore vide. Choisissez Nouveau pour créer une configuration.</p></figcaption></figure>

Sous **Informations de base**, saisissez un **Titre de la configuration** explicite, choisissez le **Type de document** (pour ce flux de factures : la facture) et une **Sous-organisation** seulement si nécessaire. Réglez **Exporter** sur **Informations** : c’est le libellé que l’interface française de la version 11.27.7 affiche pour la méthode d’exportation Infor. Le champ **Type d’information** apparaît alors. Dans l’interface française de la version 11.27.7, ce champ propose entre autres **Infor IDM + ION BOD**, **Infor IDM + M3** et **Infor IDM + M3 (TOML)**, ainsi que d’autres entrées comme **Charges Infor M3 OC** et **Unité d’emballage Infor M3**. Choisissez le type qui correspond aux fichiers de connexion et de mappage fournis par votre administrateur d’intégration ; l’ancien libellé « Infor IDM + M3 (API) » n’est plus proposé dans cet écran.

Pour **Infor IDM + M3**, le formulaire demande un **Fichier API ION** (`.ionapi`, obligatoire), un **Fichier de mappage IDM** (`.properties`) et un **Fichier de cartographie M3** (`.properties`). Les variantes TOML et ION BOD ont d’autres champs ; ne remplacez pas un fichier par un autre. Demandez les fichiers propres à votre tenant à l’administrateur Infor autorisé. Le fichier `.ionapi` contient des identifiants d’accès et ne doit apparaître ni dans les captures d’écran, ni dans les tickets, ni dans le dépôt Git.

<figure><img src="../../../.gitbook/assets/m3-export-basic-fr-20261112.png" alt="Section française Informations de base d’une configuration d’exportation non enregistrée, avec des données d’exemple inventées : le champ Titre de la configuration montre seulement le texte indicatif Par exemple, ma configuration d’exportation, aucune Sous-organisation n’est choisie, le Type de document est vide, Exporter affiche Informations et Type d’information affiche Infor IDM + M3."><figcaption><p>Configuration d’exemple française non enregistrée avec le type d’information Infor IDM + M3. La Sous-organisation et le Type de document ne sont pas choisis ; toutes les données sont inventées et rien n’a été enregistré.</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/m3-export-files-fr-20261112.png" alt="Section française Configuration d’exportation avec des données d’exemple inventées : les zones Fichier API ION avec l’indication .ionapi (max 10 Mo), Fichier de mappage IDM et Fichier de cartographie M3 avec l’indication .properties (max 10 Mo) sont vides ; le texte d’information indique que les documents seront exportés vers Infor M3 à l’aide de l’API ION et des fichiers de mappage fournis."><figcaption><p>Exemple français avec des données inventées : les trois champs de fichiers pour Infor IDM + M3. Aucun fichier n’a été téléchargé ; ces fichiers contiennent des identifiants et ne doivent pas figurer dans des captures d’écran ou des tickets.</p></figcaption></figure>

Vérifiez le type de document, l’organisation et les noms de fichiers avant **Enregistrer**. Une fois le flux Infor actif, testez avec une seule facture hors production et contrôlez son statut dans DocBits, Infor ION et M3. Une configuration enregistrée ne prouve pas qu’une facture a atteint M3.

### Vérification par Infor requise

Les onze images Infor des étapes 1 à 3 sont conservées comme exemples commentés. Elles n’ont pas été actualisées, faute de tenant Infor autorisé. Demandez à l’administrateur Infor de comparer les Connection Points, le flux de documents, les noms de mappage et les autorisations avec l’interface actuelle du tenant. L’[explication des Connection Points et des flux de documents](https://docs.infor.com/ln/10.8/en-us/lnesolh/lnoshybridng/wxa1699288671147.html) d’Infor décrit le lien entre ces éléments.
