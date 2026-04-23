# Notes de version

## **Release R1.0 12/13 mai 2026**

> **Disponibilité Sandbox :** 28 avril 2026

### Nouvelles fonctionnalités :

* **Activity Logging / Access Audit :**\
  Journalisation détaillée de l'activité et piste d'audit des accès dans toute l'application pour la conformité et la surveillance. Différents types de journalisation pour tous les microservices, basés sur des plages horaires.

* **Recherche rapide globale :**\
  Appuyez sur Cmd+K / Ctrl+K depuis n'importe où dans l'application pour rechercher parmi plus de 200 routes et plus de 40 fonctionnalités internes aux pages. Affiche les 8 meilleurs résultats avec correspondance approximative (fuzzy), navigation au clavier et liens vers la App Index Page complète.

* **Sitemap (App Index Page) :**\
  Page d'index consultable cataloguant chaque page navigable et chaque fonctionnalité interne (dialogues, barres latérales, panneaux) dans DocBits. Organisée en 18 catégories avec filtres par type, pastilles de catégorie, recherche synchronisée à l'URL et entrées protégées par permission affichées comme verrouillées pour les utilisateurs non administrateurs.

* **Analytics Dashboard :**\
  Analyses complètes du traitement des documents avec Executive Overview, API Metrics, Quality Metrics, Processing Performance, Document Flow Analytics, Activity Log, Event Log et Audit Trail.

* **Fonctionnalité d'exportation du dashboard :**\
  Nouvelle fonctionnalité d'exportation du dashboard permettant l'exportation d'une liste au format CSV ou XLSX.

* **Full-Text Search / DocSearch :**\
  Recherche vectorielle pilotée par IA sur tous les documents indexés, avec filtrage par fournisseur en temps réel, fonctionnalité "Find Similar" et paramètres d'indexation configurables.

* **Supplier Delivery Statistics :**\
  Nouvelles vues apportant des informations sur les métriques de traitement des documents liées aux fournisseurs.

* **Debug Collector :**\
  Appuyez sur Ctrl+Shift+P pour capturer un snapshot de débogage complet incluant appels API, état WebSocket, erreurs, logs de console, métriques de performance et informations d'environnement. Les snapshots peuvent être copiés dans le presse-papiers ou envoyés directement comme ticket de support avec un rapport au format HTML et un fichier JSON joint.

* **AI Agents (DocNet) :**\
  Agents autonomes en arrière-plan qui traitent automatiquement les e-mails entrants — classant, extrayant et routant les documents sans intervention manuelle. Les agents travaillent de manière indépendante sur les tâches qui leur sont assignées et escaladent vers les utilisateurs via des demandes d'approbation lorsque le jugement humain est nécessaire. Inclut un tableau de bord dédié pour surveiller l'activité et les performances des agents.

* **Nouveaux E-Documents :**\
  Plus de 80 nouveaux types de e-invoice mondiaux et plus de 40 nouveaux formats incluant XRechnung 3.0.2, ZUGFeRD 2.2/2.3.2, variantes Factur-X et Asia-Pacific PINT Credit Notes. 100 % de couverture de classification et d'extraction.

* **AI Script Chat :**\
  Assistant de chat alimenté par IA pour le développement basique de scripts, avec réponses en streaming en temps réel.

* **Script Versioning :**\
  Historique complet des versions des scripts avec suivi des modifications, comparaison et capacités de restauration. Offre une gestion des versions pour les scripts similaire à celle utilisée pour les versions d'E-Docs.

* **Historique d'exportation dans les Dashboard Actions :**\
  Accès à l'historique d'exportation d'un document directement depuis le menu d'actions du dashboard.

* **Generic API Exporter (APS450, GLS840) :**\
  Cible d'exportation API générique configurable via une configuration Mapping-File, pour une intégration flexible avec des systèmes externes. Le support pour APS450 et GLS840 a été implémenté.

* **Configurations d'exportation multiples :**\
  Prise en charge de plusieurs configurations d'exportation actives par type de document, avec ordre d'exécution et bouton de ré-exportation pour réessayer à partir de l'étape échouée.

* **Nouvelle version de Watchdog :**\
  Refonte complète de la page WatchDog Settings. Ajout de nouvelles fonctionnalités d'agrément, incluant le statut actuel de WatchDog, un guide et des commandes pour l'installation, la configuration des templates XSLT et un paramètre de mise à jour automatique. Implémentation également de la fonctionnalité permettant à WatchDog de gérer plusieurs configurations simultanément.

* **Intégration Vertex :**\
  Intégration Consumer Use Tax via Vertex pour le calcul automatisé des taxes et la conformité lors du traitement des documents.

* **Refonte de l'UI & réorganisation des paramètres :**\
  Rafraîchissement complet de l'UI dans toute l'application. Pages de login et d'authentification redessinées. Zone de paramètres redessinée avec barre latérale rétractable, sous-catégories organisées, navigation basée sur des ancres, panneau d'aide contextuel et badges de suivi de statut. Modifications de l'UI des scripts de document. Nouvelle UI pour Document flow. UI améliorée de List of Values.

* **Idea Board :**\
  Tableau de demandes de fonctionnalités permettant aux utilisateurs de soumettre, discuter et voter pour de nouvelles fonctionnalités, améliorations, corrections de bugs nécessaires, etc., avec éditeur de texte enrichi et prise en charge des images.

* **API Key Management :**\
  Page de paramètres dédiée à la création, la visualisation et la gestion de plusieurs clés API.

* **Fonctionnalité de recherche Master Data Lookup :**\
  Capacité de recherche Master Data améliorée grâce à des options de recherche adaptées aux champs sélectionnés.

* **User Activity Chart :**\
  Graphique visuel affichant les modèles d'activité des utilisateurs et les métriques d'engagement. Dashboard de l'activité de connexion avec graphiques de comparaison de tendances, agrégation quotidienne/hebdomadaire et géolocalisation basée sur GeoLite2.

* **User Login History :**\
  Users Detail View avec historique de connexion.

* **Barre latérale personnalisable :**\
  Réorganisation par drag-and-drop, bascule afficher/masquer et épinglage en haut pour les éléments de menu de la barre latérale. Les préférences sont conservées par utilisateur avec une option "Reset to default". Respecte les feature flags.

* **Video Carousel :**\
  Carousel vidéo avec lecture automatique sur la page prepare-dashboard affichant de courtes vidéos animées de conseils produit (Global Search, Keyboard Shortcuts, Document Upload, Table Customization). Mise en page à deux colonnes avec les vidéos à gauche et la préparation du dashboard à droite. La redirection automatique est mise en pause pendant que les utilisateurs parcourent les vidéos.

* **Advanced Workflow Designer :**\
  Constructeur d'automatisation visuel basé sur des nœuds, avec canvas drag-and-drop pour des pipelines de traitement multi-étapes. Prend en charge les wait steps, les chemins parallèles, les templates réutilisables, les Or condition cards, un bouton manuel de test/run, l'exécution partielle "Test from Here" et des logs d'exécution par nœud avec surlignage visuel du flux montrant exactement quels nœuds ont été exécutés.

* **Workflow KPI Dashboard :**\
  Dashboard de métriques clés pour surveiller l'exécution des workflows.

* **Workflow Partner Card SDK :**\
  SDK pour les développeurs tiers permettant de créer des cartes de workflow personnalisées, avec revue pilotée par IA, validation en sandbox et documentation de démarrage.

* **Workflow Test Manager :**\
  Gestionnaire de tests automatisés pour workflows, permettant aux administrateurs de créer et d'exécuter des tests individuellement ou en masse.

### Améliorations :

* **Base de données (tous les modules) — Migration des colonnes ID :**\
  Toutes les colonnes "ID" de la base de données DocBits ont été migrées en interne de chaînes de caractères vers un type ID dédié (UUID7). La base de données Postgres sous-jacente a été migrée vers V18 pour prendre en charge cette amélioration.

* **Traitement des documents — Améliorations supplémentaires :**\
  Modification de la logique d'exportation concernant le nombre maximum de pages à considérer — l'intégralité du document sera désormais exportée. Pendant la validation du document, l'utilisateur aura la possibilité de remplacer la limite maximale de pages par défaut pour ce document spécifique. Le calcul du Pending Document Counter a été amélioré.

* **Versions, statut et date de déploiement des services :**\
  Le statut de disponibilité des services est fourni dans le popup "Service Versions".

* **Extension linguistique :**\
  Prise en charge étendue à 22 langues avec sélecteur de langue mis à jour.

* **Design de l'Access Control au niveau du champ :**\
  Contrôle d'accès redessiné/amélioré avec un état d'activation plus clair, accès au niveau du champ, gestion cohérente des règles et permissions basées sur les groupes simplifiées. Corrige les conflits de règles entre Access Control et View Permissions, affiche le propriétaire de l'importation dans l'UI et applique le contrôle d'accès de manière cohérente à la validation des champs, aux tables extraites par IA et à toutes les vues.

* **Activity Stream pour tous les écrans :**\
  L'Activity Stream est désormais disponible sur tous les écrans de traitement de documents (Ready for Validation, PO Matching, Accounting, Quote Details, Reject) — pas seulement sur Pending Approval. Déplacé vers une position cohérente dans le panneau droit sur tous les écrans.

* **Page Document Flow :**\
  Page dédiée à la visualisation et au suivi du flux de traitement des documents, montrant les transitions de statut et la progression dans la pipeline.

* **Dual Monitor Mode (paramètre utilisateur global) :**\
  Dual Monitor Mode déplacé vers un paramètre utilisateur global, persistant entre les sessions.

* **Améliorations du Layout Builder :**\
  Prise en charge des champs cachés et en lecture seule avec indicateurs visuels, séparateur de panneau redimensionnable et paramètres de longueur de champ. Appliquez le Default Layout à plusieurs Origins sans avoir à visiter chacun individuellement.

## **Release HotFix 3 16 avril 2026**

### Améliorations de DocBits :

* **Extraction de code QR pour les factures polonaises :**\
  DocBits prend désormais en charge l'extraction de codes QR spécifiquement pour les factures polonaises, améliorant la capture automatisée des données pour les documents provenant de Pologne.

### Corrections de bugs :

* Correction d'un problème où l'exportation automatique échouait lorsque le PO Matching avait déjà eu lieu mais que le bon de commande n'était pas associé au document.
* Correction d'un problème où les prix unitaires étaient arrondis incorrectement pour les factures avec unités d'emballage (Verpackungseinheiten / VPE).
* Correction d'un problème où les messages d'erreur d'exportation d'ION/MEC (par ex. les échecs Acknowledge.PurchaseOrder) n'étaient pas affichés dans DocBits, le statut "Exported" étant affiché malgré l'échec de l'exportation.
* Correction d'un problème où le prix unitaire sur l'écran d'approbation était incorrect lorsque l'extraction de table par IA était utilisée.
* Correction d'un problème où le script Total Matching générait une erreur sur l'écran de validation.
* Correction d'un problème où le traitement de document échouait avec une erreur ("UserAuthentication object has no setter for 'org_id'").
* Correction d'un problème où l'entraînement des tables ne fonctionnait pas pour certains fournisseurs, les colonnes atterrissant dans des colonnes cachées au lieu des champs mappés.
* Correction d'un problème où le PO Matching échouait sur les grandes factures (plus de 10 pages) à cause du dépassement de la limite de taille de la requête multipart.
* Correction d'un problème où les valeurs de colonnes remplies par script n'étaient pas conservées après un redémarrage du document.
* Correction d'un problème où le toggle "Ignore Table Validation" s'affichait comme actif (vert) dans l'UI alors qu'il était en réalité désactivé en arrière-plan.
* Correction d'un problème où la qualité du document était significativement dégradée après l'importation.
* Correction d'un problème où les versions de microservices et les dates de déploiement affichées dans l'application étaient incohérentes entre les environnements après un déploiement complet.
* Correction d'un problème où l'extraction de code-barres échouait à cause d'une erreur lors de la construction de l'objet d'authentification utilisateur à partir des données de tâche.
* Correction d'un problème où les coordonnées de contact du fournisseur étaient vidées lors de la sauvegarde dans le Supplier Portal.
* Correction d'un problème où les documents rencontraient une erreur NoneType lors de l'exportation.
* Correction d'un problème où le corps de l'e-mail n'était pas inclus lorsque le premier fichier joint était une image PNG ou JPEG.
* Correction d'un problème où le corps de l'e-mail était manquant pour plusieurs documents.
* Correction d'un problème où le DocBits Operator "ai-exporting" ne produisait pas de résultats d'exportation dans les systèmes cibles (LN/D3).

## **Release HotFix 2 31 mars 2026**

### Améliorations de DocBits :

* **Traitement hybride des PDF — Extraction XML contrôlée par l'utilisateur :**\
  Lorsqu'un PDF contient des données XML intégrées, les utilisateurs peuvent désormais choisir si DocBits doit utiliser le XML intégré pour l'extraction ou traiter le document comme un PDF standard. Cela donne aux organisations un contrôle total sur la manière dont les documents hybrides sont traités, garantissant que la méthode d'extraction la plus adaptée à leur flux de travail est appliquée.

* **AP Assignment Code sur l'écran d'Approval :**\
  La page AP Manager Approval inclut désormais un champ AP Assignment Code, intégré avec Infor M3 CRS620. Cela permet aux approbateurs de vérifier et confirmer les codes d'affectation directement pendant le processus d'approbation sans passer par des systèmes externes.

* **Correspondance du total PO avec le total du document :**\
  DocBits prend désormais en charge la correspondance du total du bon de commande avec le total du document, fournissant une couche de validation supplémentaire lors du PO Matching pour détecter les écarts plus tôt dans le processus.

* **Mise à jour du numéro d'article fournisseur et VPE :**\
  DocBits prend désormais en charge la mise à jour des champs numéro d'article fournisseur et VPE (Verpackungseinheit / unité d'emballage) pendant le traitement des documents, avec synchronisation des valeurs vers M3 lors de l'exportation.

* **Classification améliorée du layout de document :**\
  L'identifiant de layout du document (tfidf_id) est désormais généré uniquement à partir du texte d'en-tête, en excluant le texte de pied de page. Cela améliore la précision de la classification en empêchant le contenu du pied de page d'influencer la détection du type de document.

* **Bouton Export & Next :**\
  Un nouveau bouton "Export & Next" a été ajouté, permettant aux utilisateurs d'exporter le document en cours et de passer immédiatement au suivant dans la file d'attente, rationalisant le flux de travail de révision et d'exportation.

* **Processus d'approbation pour les factures de coûts :**\
  Le processus d'approbation pour les factures de coûts a été amélioré avec une logique de routage et de validation optimisée.

### Corrections de bugs :

* Correction d'un problème où l'exportation Infor SFTP échouait avec une erreur due à une commande de bibliothèque incorrecte.
* Correction d'un problème où les cases à cocher booléennes ne pouvaient pas être affichées sur l'écran d'approbation.
* Correction d'un problème où des messages UNMU étaient envoyés même en l'absence de divergences dans l'unité d'achat.
* Correction d'un problème où la taxe de vente était incorrectement classifiée comme frais sur l'écran de PO Matching, entraînant un montant non réglé négatif.
* Correction d'un problème où l'exportation échouait lorsque l'unité d'achat n'était pas définie dans la confirmation de commande mais était présente dans le bon de commande.
* Correction d'un problème où le corps de l'e-mail était manquant pour plusieurs documents.
* Correction d'un problème où le numéro d'article du fournisseur n'était pas visible sur l'écran d'approbation et les mises à jour n'étaient pas envoyées à M3.
* Correction d'un problème où l'exportation des fournisseurs vers Infor retournait une erreur.
* Correction d'un problème où le PO Matching produisait des erreurs lors du traitement.
* Correction d'un problème où la fonction `findAll` ne fonctionnait pas correctement dans les scripts de documents.
* Correction d'un problème où la colonne "Updated By" de Watchdog affichait incorrectement l'utilisateur Fellow Admin au lieu de l'utilisateur réel.
* Correction d'un problème où le BOD-Mapping ne pouvait pas être configuré dans l'interface Watchdog.
* Correction d'un problème où les frais étaient incorrectement affichés comme montants non réglés au lieu d'être affichés comme frais.
* Correction d'un problème où l'appariement automatique ne fonctionnait pas pour les factures multi-lignes malgré une configuration d'appariement en place.
* Correction d'un problème où un tiret ("-") dans le numéro d'article était pris en compte lors du PO Matching pour le bon de commande mais ignoré sur la facture, provoquant une fausse divergence.
* Correction d'un problème où les fichiers PDF et XML étaient tous deux téléchargés dans le dossier d'exportation même lorsque le bouton "Export PDF" était désactivé.
* Correction d'un problème où un statut manquant sur la carte de workflow empêchait les documents de progresser dans le flux de travail.
* Correction d'un problème où la qualité du document était significativement dégradée après l'importation.
* Correction d'un problème où l'écran PO Match générait une erreur ("Cannot read properties of null").
* Correction d'un problème où la liste de valeurs par défaut ne pouvait pas être modifiée.
* Correction d'un problème où le workflow ne pouvait pas lire correctement le statut du champ, causant un routage incorrect.
* Correction d'un problème où les importations d'e-mails entrants échouaient avec une erreur.
* Correction d'un problème où des lignes manquantes n'arrivaient pas correctement dans M3 lors de l'exportation.
* Correction d'un problème où les factures codées et approuvées n'étaient occasionnellement pas mises à jour au statut "approuvé" dans M3 via l'API APS110.
* Correction d'un problème avec la configuration Multi Banking qui ne fonctionnait pas correctement.
* Correction de plusieurs problèmes avec l'affichage et le comportement de sauvegarde des dashboards partagés.
* Correction d'un problème où le champ numéro d'article fournisseur était limité à 30 caractères, empêchant le stockage de valeurs plus longues.
* Correction d'un problème où les valeurs de prix unitaire et prix unitaire par unité causaient une erreur lors de l'exportation.
* Correction d'un problème où les lignes PO avec un statut exclu (par ex. "Closed") pouvaient encore être glissées et appariées sur l'écran de PO Matching malgré leur exclusion par les règles d'appariement.

### Modifications de configuration :

* Mise à jour des modèles d'e-mail pour supprimer le bouton "Go to Task".
* Ajustement des scripts et des paramètres de champs obligatoires sur les éléments de coûts.

## **Release HotFix 1 16 mars 2026**

### Améliorations de DocBits :

* **Historique des documents dans l'exportation SFTP :**\
  DocBits prend désormais en charge l'inclusion de l'historique complet du document dans le payload XML exporté lors de l'exportation vers SFTP. Cette fonctionnalité est configurable via les Export Settings et fournit aux systèmes en aval un journal d'audit complet de chaque changement de statut et action effectuée sur un document dans DocBits — y compris qui a effectué le changement, quand il s'est produit, et quels étaient les statuts précédent et actuel. Ceci est particulièrement précieux pour la conformité, la traçabilité et l'analyse opérationnelle.
* **Mise à jour des frais sur la confirmation de commande pour Infor On Premise :**\
  Les clients Infor On Premise peuvent désormais traiter les confirmations de commande incluant des frais directement dans DocBits. Les frais sont entièrement mis à jour via l'exportation, rendant le processus de confirmation de commande de bout en bout transparent et éliminant le besoin d'ajustements manuels en aval.
*   **Appliquer le Layout par défaut à tous les Origins :**\
    Un nouveau bouton **Apply Default Layout to Origins** a été introduit dans l'écran de configuration du layout. Les administrateurs peuvent désormais déployer le layout par défaut sur tous les origins au sein d'une organisation en une seule action, éliminant le processus manuel fastidieux de copier-coller du JSON de layout pour chaque origin individuellement. Ceci est particulièrement utile lors de l'intégration de nouveaux clients où plusieurs origins doivent être configurés de manière cohérente.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/image%20(5).png)
*   **Sélection du type de document pour l'importation FTP :**\
    Les configurations d'importation FTP prennent désormais en charge l'attribution du type de document par dossier. Lors de la configuration d'une importation FTP, les utilisateurs peuvent spécifier quel type de document — tel que Facture ou Confirmation de commande — doit être appliqué à tous les documents importés depuis ce dossier. Les documents sont automatiquement classifiés lors de l'importation, supprimant le besoin d'attribution manuelle du type de document après l'ingestion. Cela prend en charge les organisations qui gèrent plusieurs types de documents à travers différentes sous-organisations et dossiers.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/image%20(4).png)
* **Exportation vers GLS840 pour Infor On Premise :**\
  DocBits prend désormais en charge l'exportation de documents vers le programme GLS840 pour les clients Infor On Premise, élargissant la gamme des cibles d'exportation prises en charge pour les environnements on-premise.
*   **Améliorations de l'interface pour Watchdog et la configuration d'exportation :**\
    Les écrans de configuration Watchdog et de configuration d'exportation ont été rafraîchis avec une interface utilisateur améliorée, offrant une mise en page plus claire et une expérience plus intuitive pour les administrateurs gérant ces paramètres.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/image%20(1).png)

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/image%20(2).png)

### Corrections de bugs :

* Correction d'un problème où les utilisateurs ayant des droits de consultation valides ne pouvaient pas voir les documents — la logique de permissions a été refactorisée avec une vérification du niveau d'accès remplaçant l'approche précédente de filtrage basé sur les groupes.
* Amélioration de la gestion des exceptions dans plusieurs domaines de l'application pour une meilleure stabilité.
* Résolution d'un problème où les colonnes de type booléen n'étaient pas correctement gérées lors de l'extraction des champs.
* Correction d'un problème d'authentification asynchrone dans le endpoint de téléchargement de fichiers.
* Résolution de problèmes d'affichage de l'interface pour la table PO sur l'écran de validation.
* Mise à jour du modèle de script pour inclure des commentaires de suivi des modifications pour une meilleure auditabilité.
* Correction d'un problème avec les champs déroulants qui ne se comportaient pas correctement sur l'écran de validation.
* Correction d'un problème où le champ de sous-organisation n'était pas pré-rempli lors de la mise à jour des affectations de documents depuis le dashboard.

## **Version Winter Summit 10 décembre 2025**

### Améliorations de DocBits :

*   **Personnalisation améliorée des règles de rapprochement des commandes :**\
    DocBits offre désormais un contrôle plus granulaire et personnalisable sur les règles de rapprochement des bons de commande. Les administrateurs peuvent configurer avec précision quelles colonnes doivent être évaluées pendant le processus de rapprochement pour chaque type de document, en s'assurant que seuls les champs les plus pertinents sont pris en compte. De plus, des tolérances peuvent être définies au niveau des colonnes, offrant une plus grande flexibilité lors du traitement des écarts mineurs. Chaque règle peut également être configurée pour s'appliquer au rapprochement manuel, au rapprochement automatique ou aux deux, donnant aux équipes la possibilité d'adapter le flux de travail de rapprochement à leurs exigences opérationnelles exactes. Ces améliorations améliorent considérablement l'adaptabilité et la précision du processus de rapprochement des bons de commande.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/release_notes_12_2025_3.png)
*   **Prise en charge de plusieurs comptes financiers fournisseurs :**\
    DocBits prend désormais en charge la gestion de plusieurs comptes financiers pour les fournisseurs via le RemitToPartyMaster BOD fourni par Infor. Cette amélioration permet aux organisations de maintenir plusieurs enregistrements de comptes de remise pour un seul fournisseur, améliorant la flexibilité et la précision du traitement des paiements. Un nouveau paramètre de configuration a été introduit pour activer ou désactiver cette capacité, permettant aux administrateurs d'activer la fonctionnalité en fonction de leurs besoins opérationnels.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/release_notes_12_2025_1.png)
*   **Ajout de l'accès utilisateur aux résultats d'extraction OCR :**\
    Le bouton **Vue OCR** sur l'écran de validation des champs est désormais accessible à tous les utilisateurs ayant un accès de validation, plutôt que d'être limité aux administrateurs. Avec cette mise à jour, tout utilisateur autorisé peut consulter directement les résultats d'extraction OCR, facilitant la validation de l'exactitude des données et le suivi des performances globales de l'OCR. Cette amélioration favorise une plus grande transparence et améliore l'efficacité du flux de travail de validation.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/release_notes_12_2025_2.png)
* **Rendu dynamique des colonnes dans les écrans d'approbation :**\
  Vues d'approbation améliorées pour afficher dynamiquement uniquement les colonnes configurées pour la comparaison dans les préférences de base de données de chaque organisation. Auparavant, certaines colonnes spécifiques à l'organisation apparaissaient vides lorsqu'elles n'étaient pas configurées pour la comparaison, causant de la confusion. Désormais, les vues d'approbation n'affichent que les champs qui sont activement comparés. Cela fournit des écrans d'approbation plus clairs et spécifiques à l'organisation sans colonnes vides ou non pertinentes.
* **Champ Type de commande ajouté à la recherche de données de référence** :\
  La liste d'en-tête de bon de commande inclut désormais une colonne "Type de commande" dans la recherche de données de référence, offrant des capacités de catégorisation supplémentaires.
* **Améliorations du tableau de bord de filtres personnalisés :**\
  La fonctionnalité de partage de tableau de bord a été améliorée pour offrir une plus grande flexibilité aux utilisateurs partagés. Les personnes avec lesquelles des tableaux de bord sont partagés peuvent désormais ajuster et modifier les filtres du tableau de bord, leur permettant d'adapter les informations affichées à leurs besoins spécifiques. Cette amélioration prend en charge une expérience de visualisation plus personnalisée et interactive, garantissant que les utilisateurs peuvent facilement affiner les informations sur les données les plus pertinentes pour leurs tâches.
* **Préfixes personnalisables pour les colonnes d'écran d'approbation :**\
  Une nouvelle option configurable a été introduite pour afficher des préfixes avant les colonnes de documents sur les écrans d'approbation. Cette fonctionnalité peut être gérée directement dans le générateur de mise en page, donnant aux administrateurs un contrôle total sur l'affichage des préfixes et les types de documents auxquels ils s'appliquent. En activant cette option, les utilisateurs bénéficient d'un contexte plus clair et d'une meilleure lisibilité lors de l'examen des documents pendant le processus d'approbation.

### Améliorations générales

* Amélioration de la journalisation des erreurs pour les tableaux mal formés dans l'extraction de tableaux.
* Ajout d'une limite de partage pour les tableaux de bord jusqu'à 10 utilisateurs ou 5 groupes, accompagnée d'un message d'erreur clair lorsque la limite est atteinte.
* Amélioration de la gestion des erreurs pour les tableaux de bord personnalisés lorsqu'un utilisateur tente de créer un tableau de bord avec un nom déjà existant.

### Corrections de Bugs:

* Correction d'un problème où les e-mails semblaient envoyés avec succès depuis la section Détails du Fournisseur mais n'étaient pas livrés aux destinataires.
* Correction d'un problème où les champs déroulants ajoutés aux écrans d'approbation/rejet ne s'affichaient pas.
* Correction d'un problème où tous les documents exportés étaient marqués comme dernièrement mis à jour par le mauvais utilisateur.
* Correction d'un problème où les documents affichaient le statut "Flux de travail en cours" mais aucun flux de travail ne s'exécutait et le journal restait vide.
* Correction d'un problème où des utilisateurs non concernés étaient assignés aux documents au moment de l'exportation sans avoir effectué de travail dessus.
* Correction d'un problème où les utilisateurs avec les permissions correctes ne pouvaient pas rejeter les documents assignés et recevaient des erreurs.
* Correction d'un problème où les icônes de flux de documents ne s'affichaient pas pour certaines organisations.
* Correction d'un problème où une fenêtre contextuelle apparaissait lors du téléchargement de documents par glisser-déposer sur le tableau de bord.
* Correction d'un problème où les drapeaux E-TEXT s'affichaient comme activés dans l'interface utilisateur alors que la réponse de l'API montrait toutes les valeurs comme fausses.
* Correction d'un problème où une erreur se produisait lors du téléchargement de documents contenant des pages vierges.
* Résolution d'un problème où les hyperliens de tâches dans les notifications par e-mail ne redirigaient pas les utilisateurs vers le bon écran d'approbation.
* Résolution d'un problème où la sélection de la sous-organisation transversale empêchait la Recherche de Données de Base d'afficher les fournisseurs. Les utilisateurs peuvent désormais afficher correctement les données de fournisseurs inter-organisationnelles.

## Release Autumn Summit 22 octobre 2025

### Améliorations de DocBits:

*   #### Améliorations de la conception des modèles d'e-mails:

    L'éditeur de modèles d'e-mails a été repensé pour offrir une structure plus claire et une expérience plus fluide. La sélection des champs de document est désormais plus intuitive, et les pièces jointes peuvent être incluses directement dans les modèles. Ces améliorations permettent de créer des e-mails professionnels et personnalisés plus rapidement et plus facilement.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fdv4oDlfkRyD0W9yWGAA4%252Fimage.png%3Falt%3Dmedia%26token%3D14bf7ebd-d886-4758-8184-d7b94447518a\&width=768\&dpr=4\&quality=100\&sign=88405d9c\&sv=2)
*   #### Améliorations du tableau de bord:

    Le tableau de bord a été étendu pour améliorer la navigation et la personnalisation. Avec de nouveaux onglets, les utilisateurs peuvent passer plus rapidement entre différents types de documents, réduisant ainsi le temps passé à rechercher la vue appropriée.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FmpO7WSIrkL0I8Rje3HQt%252Fimage.png%3Falt%3Dmedia%26token%3D77d03fe7-e626-4645-b191-e332715a25fb\&width=768\&dpr=4\&quality=100\&sign=93fa9925\&sv=2)
*   #### Tableaux de bord de filtres personnalisés:

    De plus, les tableaux de bord peuvent désormais être personnalisés et filtrés selon les préférences individuelles. Ces tableaux de bord personnalisés peuvent également être partagés avec des collègues, facilitant la création de vues de rapports cohérentes pour toute l'équipe.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fn5rPvGnRltT3mTIDoJwV%252Fimage.png%3Falt%3Dmedia%26token%3D22d065e3-81eb-4f16-828c-7f9134c25b1b\&width=768\&dpr=4\&quality=100\&sign=eb11d3a3\&sv=2)
*   #### Journaux de notifications par e-mail:

    Une nouvelle fonctionnalité de journalisation est disponible pour toutes les notifications par e-mail. Les utilisateurs peuvent désormais consulter l'historique des notifications envoyées, ce qui facilite la vérification des livraisons et le dépannage en cas de non-réception des e-mails.
*   #### Support de la facturation électronique: e-SLOG 1.6 & 2.0:

    Le support de formats de facturation électronique supplémentaires a été introduit. Le système peut désormais traiter et générer les versions e-SLOG 1.6 et 2.0, élargissant la compatibilité avec les partenaires et les exigences réglementaires.
*   #### Améliorations de la détection des doublons:

    La détection des doublons a été améliorée avec deux options de configuration puissantes. L'**Intervalle de détection des doublons** vous permet de définir une plage de temps pour vérifier les doublons de manière plus précise, tandis que le paramètre **Interdire l'exportation des doublons** empêche automatiquement l'exportation des documents détectés comme des doublons. Ensemble, ces améliorations offrent plus de contrôle et garantissent une plus grande précision des données.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FXHRKTmuSxTlDt9lDEkE7%252Fimage.png%3Falt%3Dmedia%26token%3D96b56af6-c644-4b0f-a488-8bc16a03c11f\&width=768\&dpr=4\&quality=100\&sign=9b723b7f\&sv=2)
*   #### Améliorations de l'arbre de décision:

    Les arbres de décision sont désormais plus polyvalents, avec la capacité de renvoyer les valeurs des champs de document. Cela permet une logique d'automatisation plus avancée, permettant aux workflows de prendre des décisions basées sur les données réelles des documents.
*   #### Nouvelles cartes de workflow:

    Deux nouvelles cartes de workflow étendent les capacités d'automatisation. La première vous permet de vérifier si un document appartient à une sous-organisation spécifique, facilitant la gestion des configurations multi-entités. La seconde introduit une vérification de tolérance de la date de livraison, qui compare les dates de livraison à la date actuelle en jours ouvrables pour aider à gérer et à appliquer plus efficacement les exigences de livraison.
*   #### Améliorations de l'export CSV:

    La fonctionnalité d'export CSV a été considérablement améliorée. Au lieu d'exporter uniquement les documents affichés sur la page actuelle, le système exporte désormais tous les documents d'un ensemble de données. Chaque export crée une entrée de journal, et le CSV résultant est automatiquement envoyé par e-mail, offrant un processus d'export plus complet et fiable.
*   #### Délai de suppression des bons de commande:

    Une nouvelle option de configuration permet aux administrateurs de définir un délai de suppression des bons de commande. Cette amélioration ajoute de la flexibilité et du contrôle sur les politiques de conservation des données, garantissant que les bons de commande ne sont supprimés que lorsque c'est approprié.

### Corrections de bugs

* Correction d'un problème où d'anciennes données étaient incluses lors de l'exportation de documents.
* Correction du filtre pour les erreurs d'exportation, qui montrait précédemment d'autres statuts également.
* Résolution d'un désaccord de validation de tableau où "Prix unitaire" déclenchait des erreurs mais "Prix unitaire par" ne le faisait pas, malgré des valeurs correctes.
* Correction d'un problème où l'ajout d'une nouvelle colonne au tableau de bord échouait.
* Correction d'un problème où les tâches n'étaient pas visibles dans la colonne des tâches du tableau de bord.
* Correction du comportement de tri aléatoire pour que les listes suivent désormais un ordre cohérent.
* Résolution d'un problème où l'arrêt de la modification de la taille de la colonne était impossible.
* Correction d'un bogue empêchant l'appariement manuel des lignes dans l'écran d'appariement des bons de commande.
* Correction d'un problème où l'option de pièce jointe par e-mail était réinitialisée après l'enregistrement.
* Correction d'un problème où la comptabilité automatique affichait initialement des identifiants de base de données lors de l'ouverture pour la première fois.
* Correction du comportement flou des champs pour que les valeurs ne soient plus écrasées incorrectement.
* Correction d'un problème où les champs dans le compte automatique disparaissaient après la suppression du contenu.
* Correction d'un bogue où l'utilisateur ne pouvait pas renommer "Prénom" et "Nom" dans la fenêtre contextuelle des paramètres.
* Résolution d'un problème où les documents pouvaient rester bloqués dans "workflow en cours."
* Correction d'un problème de couleur d'icône de menu où les couleurs d'organisation sélectionnées n'étaient pas appliquées correctement.
* Correction d'un problème où les codes QR n'étaient parfois pas reconnus.
* Correction d'un problème où les comptes ne pouvaient pas être supprimés avec la touche de retour pour en saisir un différent.
* Résolution d'un mélange de langues après la connexion suivant la mise en production.

## Release Spring Bloom – 23 avril 2025

### Améliorations de DocBits :

* **Option de filtre pour le journal d'importation des e-mails :** Les utilisateurs ont désormais la possibilité de filtrer les journaux d'importation et de trier le tableau pour une vue d'ensemble plus claire et plus efficace. Cette amélioration simplifie le processus d'identification et de gestion des entrées d'e-mails, améliorant le dépannage et la gestion globale des journaux.
* **Support multilingue pour la liste de valeurs :** Nous avons élargi les capacités multilingues de la fonctionnalité Liste de valeurs. Les administrateurs peuvent désormais définir des étiquettes dans plusieurs langues, garantissant que l'étiquette correcte est automatiquement affichée en fonction des paramètres de langue du système de l'utilisateur. Cette amélioration favorise une plus grande accessibilité et localisation, facilitant l'interaction des utilisateurs du monde entier avec la plateforme dans leur langue maternelle.
* **Améliorations des détails utilisateur dans les paramètres :** L'interface des paramètres affiche désormais des informations utilisateur complètes. Les administrateurs peuvent facilement voir les affiliations de groupe, les détails de sous-organisation et d'autres données clés, permettant une meilleure gestion des rôles des utilisateurs et une compréhension plus claire des structures d'équipe.
* **Informations comptables automatiques sur l'écran d'approbation :** L'écran d'approbation présente désormais des détails comptables automatiques aux côtés des informations de facturation. Cette amélioration offre un aperçu plus approfondi des données de transaction, facilitant des processus de révision plus fluides et une prise de décision plus éclairée concernant les factures.
* **Compteur de Tâches pour les Documents dans la Vue du Tableau de Bord :** Les documents sur le tableau de bord peuvent désormais indiquer les tâches ouvertes qui leur sont associées et afficher le nombre total de tâches en attente. Cette fonctionnalité offre aux utilisateurs un aperçu rapide des actions en cours, améliorant la gestion des tâches et l'efficacité des flux de travail.
* **Sélection du Modèle AI Basé sur le Fournisseur :** Les utilisateurs peuvent désormais sélectionner le modèle AI utilisé pour l'extraction de données sur une base par fournisseur. Cette amélioration permet une optimisation fine, garantissant une meilleure précision d'extraction pour différents fournisseurs et améliorant les résultats globaux du traitement des données.
* **Journaux de Flux de Travail Améliorés pour les Cartes d'Arbre de Décision :** Les journaux affichent désormais la sortie de l'arbre de décision, facilitant le suivi et la compréhension de la manière dont les décisions ont été prises dans les flux de travail.
*   **Introduction d'un nouveau système de test automatique pour améliorer la fonctionnalité et la stabilité du système :**

    Nous sommes ravis d'annoncer la mise en œuvre d'un nouveau système de test automatisé conçu pour améliorer la fonctionnalité et la fiabilité globales de notre plateforme. Ce nouveau système effectuera des vérifications constantes et approfondies de notre système pour identifier tout problème avant qu'il n'affecte votre expérience. En automatisant ces tests, nous pouvons garantir des réponses plus rapides aux problèmes potentiels et maintenir les normes de qualité les plus élevées pour notre système.

    ​

### Corrections de bugs

* Résolu un problème où les tâches n'apparaissaient pas sur l'écran de validation/approbation.
* Corrigé le positionnement du bouton Suivant/Précédent afin qu'il reste statique.
* Corrigé les problèmes de défilement dans les vues de script et d'arbre de décision, garantissant que les boutons d'action restent fixes pendant le défilement.
* Supprimé le champ pays d'origine des e-factures.
* Corrigé un problème avec le compteur de tâches affichant un nombre inexact de tâches.
* Ajouté des traductions manquantes.
* Corrigé les champs personnalisés pour afficher des noms descriptifs au lieu d'ID.
* Mis à jour la liste des raccourcis pour l'écran de correspondance des commandes d'achat.
* Résolu un problème où les documents étaient téléchargés avec un nom de fichier incorrect.
* Corrigé les incohérences de tri dans le tableau des lignes de factures au sein de la correspondance des commandes d'achat.
* Corrigé un problème affectant la fonctionnalité de création de tâches.
* Corrigé un problème dans la correspondance des commandes d'achat où le tri du tableau des factures se réinitialisait lors de la correspondance d'une ligne.
* Résolu des problèmes de comptabilité automatique en s'assurant que les références de réservation se divisent correctement lorsque le montant est divisé.
* Mis à jour les informations d'hôte ClickHouse.
* Résolu un problème où les documents en double n'étaient pas reconnus comme des doublons.
* Corrigé des problèmes d'exportation causés par des références de réservation trop longues.
* Résolu un problème où les cases à cocher en lecture seule n'étaient pas en lecture seule.
* Correction d'un problème où les utilisateurs pouvaient être ajoutés à une sous-organisation deux fois.
* Correction d'un problème où le changement de la sous-organisation pour un document entraînait la réinitialisation de l'utilisateur ou du groupe assigné.

​

## Correctif de version Winter Frost 10 avril 2025

### Améliorations de DocBits :

* **Amélioration de la fonction de script** **`set_column_date_value` :** La fonction `set_column_date_value` inclut désormais le support de l'option `skip_weekend`, permettant aux valeurs de date de sauter automatiquement les week-ends lorsqu'elles sont appliquées.
* **Amélioration du support de téléchargement de fichiers :** Les fichiers PNG et JPEG peuvent désormais être téléchargés directement et sont automatiquement convertis en format PDF pour une gestion simplifiée des documents.
* **Améliorations de la fonctionnalité Watchdog :**
  * Prend désormais en charge l'exportation vers **Enaio** pour une meilleure intégration système.
  * Capacités de parsing améliorées pour extraire des informations des structures XML `Sync.ContentDocument`, permettant un traitement des données plus efficace.

### Corrections de bogues

* Correction d'un problème sur une fonction de script.
* Résolution d'un problème où les commandes d'achat avaient un statut incorrect après leur mise à jour.

## Release Hot Fix Winter Frost 11 mars 2025

### Améliorations de DocBits :

* **Extraction de données améliorée :** Ajouté une option pour extraire le **Bon de commande** ou le **Numéro d'article** d'une ligne au-dessus ou en dessous.
* **Accès élargi aux sous-organisations croisées :** Les utilisateurs non administrateurs peuvent désormais également accéder à la fonctionnalité **Sous-organisations croisées**.

### **Corrections de bugs :**

* Corrigé un problème où les utilisateurs ne pouvaient pas être ajoutés à un groupe.
* Corrigé un problème avec les échecs d'importation d'e-mails.
* Résolu un problème avec la formation sur les documents de plus d'une page
* Corrigé un problème où les scripts ne fonctionnaient pas correctement.
* Résolu un problème où les données du document n'étaient pas affichées correctement
* Corrigé un problème avec le paramètre de mise à jour automatique des commandes d'achat
* Correction d'un problème où les jetons d'abonnement étaient affichés de manière incorrecte
* Résolution d'un problème où l'écran de tâche affichait une version de document obsolète
* Correction d'un problème qui empêchait les documents de changer leur statut
