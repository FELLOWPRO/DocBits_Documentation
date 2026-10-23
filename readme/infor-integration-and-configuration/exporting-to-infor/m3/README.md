# M3

## Étape 1 : Créer un Connection Point

1. Naviguez vers **OS > ION > Connect > Connection Points**
2. Cliquez sur **Add** et sélectionnez **IMS via API Gateway** comme type de connexion.
3. Configurez les paramètres suivants :
   * **Name** : Définissez sur `DocBits_Export`.
   * **Description** : Définissez sur `DocBits_Export`.
   * **Décocher** : _L'application a IMS End Point_.
   * **ION API Client ID** :
     * Ouvrez le fichier ION API.
     * Recherchez `"ci"` dans le fichier.
     * Copiez la valeur entre guillemets (sans les guillemets).

![Page Infor Application Connection Point pour IMS via API Gateway avec le nom DocBits_Export, la description et les champs ION API Client ID](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_1.png)

4. Sous **Documents**, ajoutez `Sync.CaptureDocument`.

![Page Connection Point DocBits_Export avec la section Documents listant Sync.CaptureDocument défini sur Send from Application](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_2.png)

5. Cliquez sur **Save** pour finaliser la configuration.

## Étape 2 : Télécharger les Mappings

{% file src="../../../.gitbook/assets/CaptureDocument_to_ProcessSupplierInvoice.xml" %}

1. Téléchargez le fichier M3 Mapping.
2. Naviguez vers **Infor** > **OS** > **ION** > **Connect** > **Mappings**.
3. Cliquez sur **Import** et sélectionnez le fichier de mapping approprié pour **M3**.

![Bouton d'ajout dans la barre d'outils de la page Mappings d'Infor ION Connect](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_3.png)

4. Une fois les fichiers importés, approuvez les mappings pour les activer.

![Vue d'ensemble des mappages dans ION Connect montrant le mappage approuvé de Sync.CaptureDocument vers ProcessSupplierInvoice](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_4.png)

## Étape 3 : Créer le Data Flow

1. Naviguez vers **OS** -> **ION** -> **Connect** -> **Data Flows**.
2. Cliquez sur **Add** et sélectionnez **Document Flow**.
3. Remplissez les détails :
   * **Name** : `DocBits_Export_to_M3`
4. Ajoutez des nœuds au flux :

#### Nœud d’application

1. Ajoutez un **Application Node** au flux.
   * **Name** : `DocBits` ou `DocBits-Export`.
2. Cliquez sur **Add** et sélectionnez le **Connection Point** créé à l'Étape 1.

![Éditeur de Data Flow avec la palette de nœuds ouverte et le panneau Application Activity Properties nommant le nœud DocBits-Dev-Demo-Export](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_5.png)

3. Cliquez sur l'**Document Icon** à côté de l'Application Node.
   * Cliquez sur **Add** et sélectionnez `Sync.CaptureDocument`.

![Éditeur de Data Flow montrant la liste Documents du nœud d'application avec Sync.CaptureDocument ajouté](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_6.png)

#### Nœud de mappage

1. Ajoutez un **Mapping Node** à droite de l'Application Node.
   * **Name** : `Capt2process`.
   * **Mapping** : `CaptureDocument_to_ProcessSupplierInvoice`.

![Éditeur de Data Flow avec le panneau Mapping Properties affichant le nom et le mappage sélectionné pour le nœud](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_7.png)

#### Nœud d’application

1. Ajoutez un **Application Node** à droite du Mapping Node précédent.
   * **Name** : `M3`.
2. Cliquez sur **Add** et sélectionnez l'**M3 Application** du client.

![Éditeur de Data Flow avec le panneau Application Activity Properties montrant le nœud d'application M3 nommé M3 BODs](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_8.png)

3. Cliquez sur l'**Document Icon** à côté de l'Application Node.
   * Cliquez sur **Add** et sélectionnez `Acknowledge.SupplierInvoice`.

![Éditeur de Data Flow montrant la liste Documents du nœud d'application M3 avec Acknowledge.SupplierInvoice ajouté](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_9.png)

#### Nœud API

1. Ajoutez un **API Node** à droite de l'Application Node.
   * **Name** : `DocBits-Error`.
   * **ION API Connector** : `DocBits_Import`.
   * Si `DocBits_Import` n'existe pas, consultez l'**Étape 1** et l'**Étape 2** de la documentation Import from M3 pour créer le Connection Point.

![Éditeur de Data Flow avec le panneau ION API Activity Properties nommant le connecteur DocBits-Dev-Demo-Import pour le nœud API](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_10.png)

#### Enregistrer et activer le Flow

* Une fois tous les nœuds ajoutés et configurés, cliquez sur **Save**.
* Activez le flux pour terminer la configuration.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_11%20\(1\).png)

## Étape 4 : Configurer l'Export dans DocBits

### On-Premise :

1. Ouvrez **DocBits**.
2.  Naviguez vers **Paramètres > Traitement des documents > Exporter**.

    ![Page de paramètres dans DocBits avec la navigation Document Processing ouverte listant Import, OCR Settings, Classification and Extraction et Module](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_export.png)
3. Créez une nouvelle exportation :
   * **Sélectionner** : **Infor IDM + ION BOD**.
   * **Titre** : Choisissez un titre significatif.
   * **Type de document** : Définissez sur **Facture**.
   * **Sous-organisation** : Peut être laissé vide ou défini sur une sous-organisation spécifique si nécessaire.
4. **Téléchargez les fichiers requis** :
   * **ION Mapping File** : Vous pouvez le trouver dans **Infor OS → API Gateway → Authorized Apps**. Recherchez l'application **DocBits**, ouvrez-la et téléchargez les identifiants.
   * **IDM Mapping File** : (Indiquez le chemin du fichier ou l'emplacement pertinent).
   * **BOD Mapping File** : (Indiquez le chemin du fichier ou l'emplacement pertinent).

### Cloud :

1. Ouvrez **DocBits**.
2.  Naviguez vers **Paramètres > Traitement des documents > Exporter**.

    ![Page de paramètres dans DocBits avec la navigation Document Processing ouverte listant Import, OCR Settings, Classification and Extraction et Module](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_export.png)
3. Créez une nouvelle exportation :
   * **Sélectionner** : **Infor IDM + M3 (API)**.
   * **Titre** : Choisissez un titre significatif.
   * **Type de document** : Définissez sur **Facture**.
   * **Sous-organisation** : Peut être laissé vide ou défini sur une sous-organisation spécifique si nécessaire.
4. **Téléchargez les fichiers requis** :
   * **ION Mapping File** : Vous pouvez le trouver dans **Infor OS → API Gateway → Authorized Apps**. Recherchez l'application **DocBits**, ouvrez-la et téléchargez les identifiants.
   * **IDM Mapping File** : (Indiquez le chemin du fichier ou l'emplacement pertinent).
   * **M3 Mapping File** : (Indiquez le chemin du fichier ou l'emplacement pertinent).

### Cloud avec toml :

1. Ouvrez **DocBits**.
2.  Naviguez vers **Paramètres > Traitement des documents > Exporter**.

    ![Page de paramètres dans DocBits avec la navigation Document Processing ouverte listant Import, OCR Settings, Classification and Extraction et Module](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_export.png)
3. Créez une nouvelle exportation :
   * **Sélectionner** : **Infor IDM + M3 (API)**.
   * **Titre** : Choisissez un titre significatif.
   * **Type de document** : Définissez sur **Facture**.
   * **Sous-organisation** : Peut être laissé vide ou défini sur une sous-organisation spécifique si nécessaire.
4. **Téléchargez les fichiers requis** :
   * **ION Mapping File** : Vous pouvez le trouver dans **Infor OS → API Gateway → Authorized Apps**. Recherchez l'application **DocBits**, ouvrez-la et téléchargez les identifiants.
   * **IDM Mapping File** : (Indiquez le chemin du fichier ou l'emplacement pertinent).
   * **M3 toml Mapping File** : (Indiquez le chemin du fichier ou l'emplacement pertinent).
