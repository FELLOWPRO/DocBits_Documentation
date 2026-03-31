# Notes de version

## **Version Spring Spark 13 mai 2026**

Disponibilité sur Sandbox : 27–29 avril 2026

### Améliorations de DocBits :

*   **Advanced Workflow Designer :**\
    DocBits présente un tout nouveau Advanced Workflow Designer — un constructeur d'automatisation visuel basé sur des nœuds qui met l'orchestration complète des flux de travail à portée de main. Grâce à un canevas intuitif de glisser-déposer, les administrateurs peuvent connecter des cartes de flux de travail DocBits dans des pipelines de traitement complexes à plusieurs étapes. Chaque nœud sur le canevas représente une action ou un point de décision, et les connexions entre les nœuds définissent le flux des documents à travers le pipeline. Le concepteur prend en charge les étapes d'attente pour introduire des délais temporisés, les chemins parallèles où toutes ou certaines branches doivent être complétées avant de continuer, et la possibilité d'enchaîner n'importe quelle combinaison de cartes intégrées ou créées par des partenaires. Les flux de travail peuvent être sauvegardés comme modèles réutilisables, importés et exportés entre environnements, et testés directement depuis le concepteur avant la mise en production. L'éditeur dispose d'un canevas avec accrochage à la grille et navigation par mini-carte pour les grands flux de travail, des raccourcis clavier pour copier et coller, une validation en temps réel avec mise en surbrillance des erreurs pendant la construction, et une protection contre l'édition concurrente pour empêcher l'écrasement des modifications par d'autres utilisateurs. Des journaux d'exécution détaillés fournissent une surveillance par nœud, permettant aux administrateurs de tracer exactement comment chaque étape d'un flux de travail a été exécutée et où les problèmes sont survenus.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/release_may_2026_advanced_workflow_designer.png)

*   **Améliorations du Workflow Designer :**\
    Le concepteur de flux de travail existant a été amélioré avec une logique de branchement if/else, permettant des flux de travail basés sur des décisions plus sophistiqués. Plusieurs nouvelles cartes de condition ont été ajoutées, élargissant encore la gamme de logique d'automatisation disponible. Un nouveau Workflow Test Manager permet aux administrateurs de créer et d'exécuter des tests automatisés pour les flux de travail individuellement ou tous en même temps, garantissant que les modifications se comportent comme prévu avant le déploiement. La section Workflow comprend désormais aussi un tableau de bord KPI avec des métriques clés sur les performances d'exécution des flux de travail.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/release_may_2026_workflow_branching.png)

*   **DocNet AI Agents :**\
    DocBits inclut désormais les DocNet AI Agents — des agents intelligents et autonomes qui fonctionnent en arrière-plan pour gérer les tâches de traitement de documents telles que le rapprochement des bons de commande et la validation des factures. Les agents opèrent de manière indépendante, traitant les tâches assignées et ne faisant appel aux utilisateurs que lorsqu'un jugement humain est nécessaire. Lorsqu'un agent rencontre une exception ou a besoin d'une confirmation, il crée une demande d'approbation qui apparaît directement dans la boîte de réception de l'utilisateur, garantissant que rien n'est manqué sans nécessiter une supervision constante. Les agents peuvent se coordonner entre eux, déléguer des sous-tâches et organiser le travail en missions et projets pour des processus complexes à plusieurs étapes. Un tableau de bord dédié aux agents offre une visibilité complète sur l'activité des agents, les métriques de performance et les journaux d'audit, permettant aux administrateurs de surveiller ce que font les agents et avec quelle efficacité ils travaillent. Des notifications en temps réel tiennent les utilisateurs informés lorsque les agents terminent des tâches ou signalent des éléments à examiner.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/release_may_2026_docnet_ai_agents.png)

*   **Partner Card SDK :**\
    Un nouveau Partner Card SDK permet aux développeurs tiers et aux partenaires de créer des cartes de flux de travail personnalisées pour DocBits. Les partenaires peuvent télécharger des paquets de cartes pour validation et examen, importer des cartes depuis des dépôts GitHub et gérer les soumissions via une page dédiée de paramètres du Card SDK. Un système d'examen alimenté par l'IA évalue automatiquement les cartes soumises en termes de qualité et de conformité. Le SDK comprend des téléchargements basés sur des exemples avec des dialogues de sélection de cartes, une validation comportementale dans un environnement sandbox et une documentation complète pour démarrer. Le Card SDK est protégé par des vérifications de licence et est désormais visible pour tous les utilisateurs, pas seulement les administrateurs.

*   **Full-Text Search / DocSearch :**\
    Une nouvelle capacité de recherche en texte intégral a été ajoutée à DocBits, alimentée par la recherche vectorielle basée sur l'IA. Les utilisateurs peuvent rechercher dans tous les documents indexés avec un filtrage en temps réel par fournisseur et une fonction « Find Similar » pour localiser des documents similaires à un document sélectionné. Une page de paramètres dédiée permet aux administrateurs de configurer l'indexation des données IA, les préférences de stockage vectoriel et de surveiller la progression de l'indexation en temps réel. L'accès à DocSearch est géré via les plans d'abonnement.

*   **Expansion des formats E-Invoice :**\
    DocBits a considérablement élargi sa prise en charge des formats de facture électronique avec plus de 80 nouveaux types de e-invoice mondiaux et plus de 40 nouveaux formats. Les formats nouvellement pris en charge incluent Taiwan EGUI, Thailand E-Tax, India GST Credit Note, SPS Commerce RSX 7.7.4, XRechnung 3.0.2, ZUGFeRD 2.2 et 2.3.2, variantes Factur-X, Uruguay CFE, Ecuador SRI Retención, SVEFAKTURA 1.0, EHF 3.0, OIOUBL, Finvoice et Asia-Pacific PINT Credit Notes, entre autres. DocBits atteint désormais une couverture de classification et d'extraction de 100 % pour tous les formats de documents électroniques pris en charge.

*   **Login Analytics :**\
    Un nouveau tableau de bord Login Analytics offre aux administrateurs une visibilité complète sur l'activité de connexion dans toute l'organisation. Le tableau de bord comprend des graphiques comparatifs montrant les tendances de connexion dans le temps, des vues d'agrégation quotidienne et hebdomadaire, et une géolocalisation basée sur GeoLite2 pour voir d'où proviennent les connexions. Cela offre un moyen rapide de repérer les schémas de connexion inhabituels et de surveiller la sécurité des comptes.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/release_may_2026_login_analytics.png)

*   **Analytics Dashboard :**\
    Un module complet d'analyse du traitement des documents a été introduit avec plusieurs vues de tableau de bord incluant Executive Overview, API Metrics, Quality Metrics et Processing Performance. Document Flow Analytics offre des métriques au niveau de l'organisation sur les temps de traitement des documents et les transitions de statut. Un système complet d'Activity Log et Event Log permet aux administrateurs de parcourir, rechercher, filtrer et exporter les données d'événements avec des visualisations graphiques et la mise en surbrillance de la syntaxe JSON. Une fonction Audit Trail fournit un suivi détaillé de l'historique des modifications avec des détails contextuels pour chaque modification.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/release_may_2026_analytics_dashboard.png)

*   **Améliorations du contrôle d'accès :**\
    Le contrôle d'accès a été appliqué à l'ensemble de l'application, couvrant l'écran de validation des champs, les tables extraites par IA et plusieurs autres vues. Les administrateurs ont désormais la possibilité de désactiver le contrôle d'accès globalement si nécessaire. Le design du contrôle d'accès a été revu pour une expérience plus cohérente et intuitive sur tous les écrans.

*   **Améliorations du Layout Builder :**\
    Le Layout Builder prend désormais en charge les champs masqués et en lecture seule avec des indicateurs visuels, facilitant la compréhension par les administrateurs des champs visibles et modifiables pour les utilisateurs. Un séparateur redimensionnable entre les panneaux améliore la flexibilité de l'espace de travail, et les paramètres de longueur de champ offrent un contrôle plus précis sur les champs de saisie de données.

*   **Historique d'exportation dans les actions du Dashboard :**\
    Les utilisateurs peuvent désormais accéder à l'historique d'exportation d'un document directement depuis le menu d'actions du tableau de bord, rendant plus rapide la vérification des tentatives d'exportation passées sans quitter la vue principale.

*   **Améliorations de l'exportation :**\
    Les configurations d'exportation prennent désormais en charge l'ordonnancement de l'exécution, permettant aux administrateurs de définir la séquence dans laquelle les multiples méthodes d'exportation sont traitées. Un nouveau bouton de ré-exportation sur les écrans d'erreur permet aux utilisateurs de réessayer à partir de l'étape qui a échoué plutôt que de redémarrer l'ensemble du processus. DocBits prend également en charge la cible d'exportation API GLS840MI, avec une interface mise à jour pour gérer plusieurs configurations d'exportation actives par type de document.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/release_may_2026_export_improvements.png)

*   **Script Versioning & AI Chat :**\
    Les scripts de documents prennent désormais en charge l'historique complet des versions, permettant aux administrateurs de suivre les modifications, comparer les versions et restaurer les versions précédentes des scripts. Les scripts par défaut sont protégés contre les modifications accidentelles, et les noms de scripts peuvent être modifiés en ligne avec une navigation par fil d'Ariane. Les champs peuvent désormais être définis en lecture seule par programmation via la nouvelle fonction set\_is\_readonly. Un nouvel assistant de chat alimenté par l'IA aide au développement de scripts, fournissant des réponses en streaming en temps réel.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/release_may_2026_script_versioning.png)

*   **API Key Management :**\
    Une nouvelle page API Key Management dans les paramètres d'intégration permet aux administrateurs de créer, visualiser et gérer plusieurs clés API avec un cache Redis pour la performance.

*   **Idea Board :**\
    Une nouvelle fonctionnalité Idea Board permet aux utilisateurs de soumettre, discuter et voter pour des idées de fonctionnalités et des suggestions. Le tableau comprend un éditeur de texte riche avec support de téléchargement d'images, commentaires et fonctionnalité de vote.

*   **Statistiques fournisseurs :**\
    De nouvelles vues de statistiques fournisseurs offrent des informations sur les métriques de traitement des documents liées aux fournisseurs.

*   **Expansion linguistique :**\
    DocBits prend désormais en charge 22 langues, élargi par rapport à la sélection précédente. Le sélecteur de langue a été mis à jour avec une disposition en grille à 4 colonnes, et les utilisateurs peuvent désormais définir leur langue préférée directement dans leurs paramètres utilisateur.

*   **Refonte du plan d'abonnement :**\
    Le sélecteur de plan d'abonnement a été repensé avec un affichage amélioré des informations sur les jetons et une nouvelle ligne d'utilisation DocNet dans le tableau d'abonnement.

*   **Dual Monitor Mode :**\
    Le Dual Monitor Mode a été déplacé vers un paramètre utilisateur global, le rendant accessible et persistant entre les sessions pour les utilisateurs qui travaillent avec plusieurs écrans.

*   **Recherche floue pour les caractères allemands :**\
    La fonctionnalité de recherche prend désormais correctement en charge les caractères spéciaux allemands (trémas), garantissant que les recherches de mots comme « Rechnungsnummer » correspondent également aux représentations de caractères alternatives.

*   **Améliorations des notifications par e-mail :**\
    Le remplacement des paramètres dans les modèles d'e-mail a été amélioré avec une meilleure validation des destinataires et une gestion des préférences utilisateur.

*   **Suivi de l'utilisation des crédits :**\
    Les organisations peuvent désormais visualiser et suivre leur utilisation de crédits IA au fil du temps avec des options de filtrage, offrant une meilleure visibilité sur les schémas de consommation.

### Améliorations générales :

*   La zone Settings a été repensée avec une barre latérale pliable, des sous-catégories organisées et une navigation par ancres pour un accès plus rapide. Un panneau d'aide contextuelle fournit des conseils en ligne, et des badges de suivi de statut montrent la complétude de la configuration en un coup d'œil.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/release_may_2026_settings_redesign.png)

* Les documents avec des codes-barres se divisent désormais de manière plus fiable, avec une meilleure gestion des cas limites et la récupération des erreurs.
* Le rapprochement PO détecte et convertit désormais automatiquement les prix unitaires lors de la division des lignes rapprochées, réduisant les corrections manuelles.
* Les documents ne restent plus bloqués pendant l'extraction — un nouveau système de suivi de statut garantit que chaque document progresse dans le pipeline.
* Lorsque des erreurs d'extraction surviennent, DocBits fournit désormais des messages d'erreur plus clairs avec des détails étape par étape pour aider à résoudre le problème plus rapidement.
* Les performances globales de l'application ont été améliorées avec des temps de réponse plus rapides sur tous les écrans.
* Les règles d'Auto Accounting prennent désormais en charge le filtrage basé sur les nombres pour des conditions de correspondance plus précises.

### Corrections de bugs :

* Correction d'un problème où le nom personnalisé du tableau de bord n'était pas aligné avec l'icône du tableau de bord.
* Correction d'un problème où le tableau de bord affichait des colonnes non incluses dans la configuration des colonnes visibles.
* Correction d'un problème où le nom de l'onglet sélectionné n'était pas affiché sur le tableau de bord.
* Correction d'un problème où la fenêtre contextuelle « Nouvelle version disponible » apparaissait à chaque changement de sous-organisation.
* Correction d'un problème où le paramètre de documents par page n'était pas conservé après actualisation de la page.
* Correction d'un problème où le décompte des documents du tableau de bord ne se mettait pas à jour correctement.
* Correction d'un problème où les utilisateurs recevaient incorrectement le message d'erreur « Le tableau de bord existe déjà ».
* Correction d'un problème où la fenêtre contextuelle de confirmation de suppression en masse n'était pas affichée.
* Correction de plusieurs problèmes d'affichage et de comportement de sauvegarde des tableaux de bord partagés.
* Correction d'un problème où les tableaux de documents n'étaient pas affichés sur l'écran de validation.
* Correction d'un problème où un message d'erreur incorrect était affiché pour les fichiers PDF invalides.
* Correction d'un problème où le redimensionneur de colonnes apparaissait derrière les boutons d'action de ligne.
* Correction d'un problème où des valeurs incorrectes étaient extraites pour le montant net, le montant de la taxe et le taux de taxe.
* Correction d'un problème où les configurations d'exportation ne pouvaient pas être créées sans spécifier un type de document lorsqu'il était marqué comme optionnel.
* Correction d'un problème où une erreur de configuration en double se produisait lors de l'ajout de nouvelles configurations d'exportation.
* Correction d'un problème où des erreurs survenaient lors de la création de plusieurs configurations d'exportation.
* Correction d'un problème où le titre de configuration était effacé après la sélection de Watchdog comme type d'exportation.
* Correction d'une erreur de serveur interne lors de la création de configurations d'exportation Infor.
* Correction d'un problème empêchant le redémarrage multiple de documents exportés.
* Correction d'un problème où certaines pages de paramètres ne pouvaient pas être trouvées.
* Correction d'un problème où le lien de téléchargement de Watchdog renvoyait une erreur.
* Correction d'un problème où le bouton de création List of Values ne déclenchait aucune action.
* Correction d'un problème où les descriptions de groupes n'étaient pas affichées.
* Correction d'un problème où l'état de validation du mot de passe persistait après l'annulation de la modification d'un utilisateur.
* Correction d'un problème où les documents en statut « Pending Watcher Export » n'étaient pas cliquables.
* Correction d'un problème où des configurations de recherche en double pouvaient être créées.
* Correction d'un problème où le tri des utilisateurs ne fonctionnait pas correctement.
* Correction d'un problème d'affichage où tout le texte de l'application apparaissait en bleu.
* Correction d'un problème où l'affichage du format de langue était incohérent.
* Correction d'un problème où le paramètre de langue apparaissait vide lorsqu'aucune préférence n'était sélectionnée.
* Correction d'un problème où la casse du nom de l'entreprise était ignorée.
* Correction d'un problème où la recherche ne fonctionnait pas pour les groupes et les permissions.
* Correction d'un problème où l'action de suppression d'utilisateur ne supprimait pas correctement l'utilisateur.
* Correction d'un problème où les icônes de flux de documents n'étaient pas visibles.
* Correction d'une erreur de serveur interne lors de la sauvegarde des modèles d'e-mail.
* Correction d'un problème où des variables en double étaient insérées dans les sujets des modèles d'e-mail.
* Correction d'une erreur lors de la sauvegarde des détails du compte de messagerie entrant.
* Correction d'un problème où les documents restaient bloqués au statut « nouveau » après le téléchargement.
* Correction d'un problème où les colonnes de tableau n'étaient pas disponibles après désactivation puis réactivation.
* Correction d'un problème où la création d'arbres de décision échouait pour les types de documents personnalisés.
* Correction d'un problème où l'extraction de tableaux ne renvoyait aucun résultat.
* Correction d'un problème où le type de document CREDIT\_NOTE n'était pas reconnu correctement.
* Correction d'un problème où les utilisateurs sans droits d'administrateur pouvaient voir toutes les tâches créées.
* Correction d'un problème où la fenêtre contextuelle de sous-organisation ne se fermait pas après le téléchargement par glisser-déposer.
* Correction d'un problème où les filtres de période n'étaient pas appliqués correctement.
* Correction d'un problème de conversion de date et heure au format américain.
* Correction d'un problème où les flux de travail étaient déclenchés dans le mauvais ordre — l'exécution des flux de travail utilise désormais un verrouillage de document et des priorités de file d'attente appropriés.

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
