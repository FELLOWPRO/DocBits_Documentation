# NOVA — Version majeure

**Instantané de version : 16 octobre 2026**

NOVA intègre l'ensemble des fonctionnalités précédemment disponibles en bêta dans VESTA en tant que fonctionnalités standard, ainsi que la validation guidée des documents, de nouvelles façons d'améliorer l'automatisation, des contrôles de factures électroniques plus clairs et un meilleur contrôle des imports et du traitement des documents. Ces notes décrivent les ajouts destinés aux clients dans les versions de service listées ci-dessous, par rapport au dernier [correctif VESTA publié, R1.0.15 du 14 octobre 2026](incremental-updates-14-october-2026.md), y compris les correctifs VESTA antérieurs.

L'instantané identifie les builds couverts par ces notes. Pour la disponibilité dans votre environnement bac à sable ou de production et le basculement entre les canaux, consultez le [cycle de vie des versions DocBits](../docbits-release-lifecycle-strategy.md). Les fonctionnalités disposant d'un interrupteur au niveau de l'organisation ou du type de document doivent toujours être activées par un administrateur.

## Anciennes fonctionnalités bêta VESTA : incluses dans NOVA <a href="#former-vesta-beta-features-included-in-nova" id="former-vesta-beta-features-included-in-nova"></a>

**Toutes les anciennes fonctionnalités bêta VESTA font désormais partie de l'ensemble de fonctionnalités standard de NOVA.** Pour les clients qui n'utilisaient pas la bêta VESTA, cela élargit les fonctionnalités disponibles pour leur équipe, notamment **Gestion des mises en page**, [**Règles de validation personnalisées**](../../administration-and-setup/settings/global-settings/document-types/custom-validation-rules.md) et [**Règles de transformation**](../../administration-and-setup/settings/global-settings/document-types/transformation-rules.md). Les paramètres de l'organisation, les interrupteurs de type de document et les autorisations d'accès continuent de s'appliquer.

Les mêmes anciennes fonctionnalités bêta deviendront des fonctionnalités standard VESTA avec le **prochain correctif VESTA, prévu pour le [11 novembre 2026](vesta-hotfix-11-november-2026.md)**. Cette annonce couvre les anciennes fonctionnalités bêta VESTA ; les sections ci-dessous décrivent également d'autres ajouts et améliorations NOVA.

## Ce que NOVA apporte aux clients <a href="#what-nova-adds-for-customers" id="what-nova-adds-for-customers"></a>

La comparaison ci-dessous couvre les anciennes fonctionnalités bêta nouvellement disponibles, les nouvelles capacités et les extensions des fonctionnalités existantes. La base de référence VESTA inclut des fonctionnalités qui n'étaient disponibles qu'en bêta ; leur inclusion dans l'ensemble de fonctionnalités standard de NOVA constitue un changement de version visible par les clients.

| Capacité | Base de référence VESTA (y compris bêta) | Ce que les clients obtiennent avec NOVA |
| --- | --- | --- |
| **Utiliser les anciennes fonctionnalités bêta** | Fonctionnalités disponibles via la bêta VESTA | **Fonctionnalités régulières NOVA :** toutes les anciennes fonctionnalités bêta VESTA sont incluses. Leur introduction régulière dans VESTA est prévue pour le correctif du 11 novembre 2026. |
| **Aide lors de la validation d'un document** | Assistant de configuration et Vérification des champs d'en-tête | **Nouvel Assistant de validation :** identifier les champs bloquants, accéder à la valeur concernée, examiner les corrections suggérées et conserver le chat dans une fenêtre séparée. |
| **Améliorer l'automatisation à partir des corrections quotidiennes** | Tableau de bord Touchless Intelligence, diagnostic fournisseur et propositions de modification | **Nouveau processus d'examen et de mesure :** soumettre des demandes d'amélioration, examiner les propositions de règles apprises, consulter les preuves sur les documents affectés, classer les opportunités et mesurer les résultats après activation. |
| **Comprendre et résoudre les erreurs de factures électroniques** | Contrôles des documents électroniques, catalogue de règles et visionneuse XML | **Validation des factures électroniques étendue :** rapports regroupés par niveau de validation, contrôles de politique et historique des modifications, rejet depuis le rapport et inspection XML dans les factures PDF prises en charge. |
| **Contrôler les imports FTP/SFTP** | Connexions d'import et rétention ou archivage des fichiers sources | **Nouvelle configuration guidée et nouveaux contrôles :** assistant de connexion, journaux étape par étape, tentatives configurables et notifications d'échec, et suppression des fichiers sources après un import réussi. |
| **Travailler avec les règles et les mises en page** | Moteurs de règles, journaux d'exécution et transformations après recherche des données de référence ; les panneaux de gestion nécessitaient un lien bêta | **Accès élargi et meilleurs outils :** ouvrir les panneaux de gestion directement, rechercher et prévisualiser les mises en page cibles, ouvrir l'éditeur de mise en page d'un document et enregistrer l'exécution de la sélection de mise en page. |
| **Agir depuis l'Assistant de configuration** | Chat de configuration, prévisualisation/confirmation/annulation et alertes proactes sur l'état des imports | **Actions supplémentaires :** gérer les connexions défaillantes, consulter l'historique de désactivation, modifier les éléments de configuration sélectionnés, créer une règle de validation inactive depuis un catalogue et consulter les explications des pages. |
| **Contrôler le traitement des documents** | Limites de pages par organisation et redémarrage de document | **Nouveaux choix au niveau du document :** redémarrer avec un nombre de pages choisi, voir les pages traitées par rapport au total, et choisir si les champs masqués sont extraits. |
| **Rapprocher les livraisons complexes** | Rapprochement des commandes d'achat et liaison manuelle des lignes | **Rapprochement plus flexible :** sélectionner les lignes dans les deux sens, conserver éventuellement chaque sous-ligne de document rapprochée et regrouper les demandes d'export par colonnes de lignes configurées. |
| **Gardez les travaux exportés et finalisés distincts** | Flux de travail d'exportation et Finished existants | **Nouveaux contrôles de statut :** utilisez Exported pour le traitement de suivi, verrouillez éventuellement les documents Finished, et identifiez les documents bloqués par la limite d'exécution du flux de travail. |

### Activez les fonctionnalités nécessitant une configuration

* **Assistant de validation :** un administrateur de l'organisation l'active sous **Paramètres → Informations de l'entreprise → Assistants**. Il est distinct de l'Assistant de configuration et reste désactivé tant qu'il n'est pas activé.
* **Examen des améliorations et rapports de conseil :** nécessitent les droits d'administrateur de l'organisation et l'accès à Analytics. Les propositions apprises reposent sur l'historique des corrections. Pour obtenir un résultat mesuré, il faut disposer de données suffisantes et attendre la fin de la période de suivi.
* **Contrôles de règles et de mises en page :** leurs interrupteurs d'activation par type de document s'appliquent toujours. NOVA rend les panneaux de gestion accessibles sans lien bêta.
* **Comportements de traitement facultatifs :** configurez le nettoyage FTP et les nouvelles tentatives pour chaque connexion. L'expansion des sous-lignes un-à-plusieurs et le verrouillage des documents terminés doivent être activés explicitement.

Pour la disponibilité dans votre environnement et le basculement de canal de publication, consultez le [cycle de vie des versions](../docbits-release-lifecycle-strategy.md).

## Regardez les vidéos des fonctionnalités <a href="#watch-the-feature-videos" id="watch-the-feature-videos"></a>

Utilisez ces démonstrations en complément des notes de version pour comprendre les fonctionnalités associées et leur configuration. Les vidéos disponibles en français sont liées ci-dessous ; les autres vidéos sont clairement identifiées comme étant en anglais.

| Sujet | Vidéo |
| --- | --- |
| Choisir la bonne automatisation — y compris où s'insèrent les Règles de rapprochement des commandes | [Vidéo en français](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/choose-automation/v1/fr.mp4) · [Vidéo en anglais](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/choose-automation/v1/en.mp4) |
| Règles de transformation | [Vidéo en français](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/transformation-rules/v1/fr.mp4) · [Vidéo en anglais](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/transformation-rules/v1/en.mp4) |
| Règles de validation personnalisées | [Vidéo en français](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/custom-validation-rules/v1/fr.mp4) · [Vidéo en anglais](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/custom-validation-rules/v1/en.mp4) |
| Mises en page et règles de sélection | [Vidéo en anglais](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/layouts/v1/en.mp4) |
| Touchless Intelligence | [Vidéo en français](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence/v1/fr.mp4) · [Vidéo en anglais](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence/v1/en.mp4) |
| Validation des factures électroniques | [Vidéo en français](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/einvoice-validation/v1/fr.mp4) · [Vidéo en anglais](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/einvoice-validation/v1/en.mp4) |
| Utilisateurs et accès administrateur | [Vidéo en français](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/users/v1/fr.mp4) · [Vidéo en anglais](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/users/v1/en.mp4) |
| Sous-organisations | [Vidéo en français](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/sub_organizations/v1/fr.mp4) · [Vidéo en anglais](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/sub_organizations/v1/en.mp4) |

### AI Table : six vidéos courtes

Ces vidéos sont en anglais. Regardez la série complète ou choisissez le sujet qui vous intéresse.

1. [Lire le tableau AI](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/ai-table-part1/v1/en.mp4)
2. [Corriger une colonne et enseigner à DocBits](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/ai-table-part2/v1/en.mp4)
3. [Trois problèmes typiques](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/ai-table-part3/v1/en.mp4)
4. [Lignes de remise, de taxe et de quantité nulle](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/ai-table-part4/v1/en.mp4)
5. [Ce que l'IA lit déjà correctement](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/ai-table-part5/v1/en.mp4)
6. [L'Assistant et qui peut modifier quoi](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/ai-table-part6/v2/en.mp4)

Pour des captures d'écran et des instructions détaillées, consultez le [guide AI Table](../../end-user-and-partner-section/end-user-section/ai-table/README.md).

## Assistant de validation : une aide sur le document devant vous

* **Identifiez ce qui bloque la progression.** Demandez pourquoi un document ne peut pas continuer. L'assistant identifie les champs concernés, explique le problème et propose un accès direct au champ ou à la cellule du tableau. Il utilise le document courant et les droits d'accès de l'utilisateur.
* **Examinez les corrections proposées dans leur contexte.** Lorsque c'est pris en charge, les réviseurs peuvent appliquer une valeur de champ ou de tableau proposée, utiliser un candidat de données de référence, répéter une recherche ou ouvrir l'écran de rapprochement concerné. Les modifications du formulaire restent soumises au processus normal de revue et d'enregistrement du document. Les documents en lecture seule et les utilisateurs sans droit de modification ne disposent pas d'actions d'édition.
* **Posez des questions sur le rapprochement et la comptabilité.** L'assistant peut expliquer le contexte de commande d'achat ou de comptabilité lorsqu'il est ouvert sur ces écrans. Les modifications du formulaire de validation s'effectuent sur l'écran de validation.
* **Comprenez une amélioration avant de l'utiliser.** Les explications relient une règle ou un paramètre proposé aux valeurs réelles du document. Elles peuvent inclure un schéma et une explication narrée dans la langue de l'utilisateur lorsque disponible. Les suggestions restent centrées sur le document courant.
* **Travaillez avec le chat dans une fenêtre séparée.** Détachez la conversation tout en consultant le document. Les actions qui modifient le formulaire restent dans la fenêtre du document.
* **Consultez plus de détails derrière les valeurs extraites.** La vue d'origine des valeurs ajoute des détails tels que l'OCR par rapport à la couche de texte du PDF, la correspondance des règles d'extraction et la recherche qui a fourni une valeur. L'explication du tableau AI ajoute des conseils de configuration plus exploitables et des compteurs plus clairs.

Un administrateur d'organisation active l'Assistant de validation séparément de l'Assistant de configuration sous **Paramètres → Informations sur l'entreprise → Assistants**.

## Transformez les corrections répétées en améliorations de l'automatisation

Le tableau de bord [Touchless Intelligence](../../administration-and-setup/touchless-intelligence.md) existant intègre un processus de revue et de suivi :

* **Propositions de règles apprises.** Des corrections manuelles répétées peuvent suggérer une [règle de transformation](../../administration-and-setup/settings/global-settings/document-types/transformation-rules.md). Les administrateurs voient ce qu'elle écrirait, les exemples à l'appui et les documents sur lesquels elle remplacerait une valeur que l'équipe avait acceptée. Une proposition est révisée avant de devenir une règle active.
* **Demandes d'amélioration des réviseurs.** Les utilisateurs peuvent soumettre une amélioration depuis l'assistant de document pour qu'un administrateur la révise dans Touchless Intelligence. La demande conserve son explication et sa décision ensemble.
* **Mesurez ce qui s'est passé après l'activation.** Pour les règles de transformation prises en charge, DocBits compare les corrections manuelles avant et après l'activation et affiche le taux sans intervention à côté. La mesure utilise des périodes de 14 jours et identifie les données insuffisantes plutôt que d'inventer une amélioration. Modifier une règle démarre une nouvelle mesure pour cette révision.
* **Rapport de conseil.** Les administrateurs peuvent générer une vue classée des opportunités d'amélioration couvrant l'extraction, les données de base, le rapprochement des commandes d'achat, la comptabilité, les paramètres et le flux de traitement. L'impact estimé est étiqueté comme une estimation tant qu'il n'a pas été mesuré.
* **Conseils de rapprochement spécifiques aux fournisseurs.** Des problèmes répétés de rapprochement des fournisseurs et des articles peuvent alimenter des propositions de tolérances ou de [règles de rapprochement des commandes](../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-matching-rules.md). Les conseils distinguent une commande d'achat manquante d'un problème de règle ou de tolérance.
* **Résumés de suivi.** Un résumé hebdomadaire pour administrateurs rassemble les demandes d'amélioration ouvertes, les principales opportunités et les mesures terminées lorsqu'il y a quelque chose à signaler. Les demandeurs peuvent être notifiés lorsqu'un résultat mesuré est disponible.

## Assistant de configuration : actions supplémentaires et explications des pages

L'[Assistant de configuration](../../administration-and-setup/settings/global-settings/company-information/settings-assistant.md), y compris les alertes de santé proactives pour les e-mails/FTP, est déjà disponible dans VESTA. NOVA ajoute des actions et du contexte à cette expérience existante :

* **Actions de connexion depuis une alerte de santé.** Ouvrez la connexion concernée, examinez l'action disponible et confirmez-la depuis l'assistant. Les alertes de santé peuvent également être ignorées. Les cartes d'alerte de base par canal et leurs informations d'erreur/de nouvelle tentative existent déjà dans VESTA.
* **Historique de désactivation visible.** Lorsqu'il est enregistré, un import désactivé indique quand il a été désactivé et par qui.
* **Actions supplémentaires révisées.** Les administrateurs peuvent prévisualiser et confirmer des modifications prises en charge telles que l'activation de types de documents, le renommage d'un groupe, la modification du mode de recherche d'un champ de recherche, la suppression d'un champ ou la création d'une règle de validation personnalisée inactive depuis le catalogue.
* **Gérez les connexions d'importation défaillantes.** Les cartes prises en charge peuvent désactiver ou supprimer une connexion après confirmation. Les actions réversibles proposent une annulation ; la suppression permanente est identifiée comme telle.
* **Explications des pages.** Certaines pages de paramètres proposent des vidéos avec sous-titres et transcriptions, y compris les mises en page, les utilisateurs, les sous-organisations, les règles de transformation et la validation des factures électroniques lorsqu'une version linguistique est disponible.

## Règles et mises en page : accès direct et meilleurs diagnostics

* **Les anciennes fonctionnalités bêta deviennent des fonctionnalités standard.** Gérer les mises en page, les [règles de validation personnalisées](../../administration-and-setup/settings/global-settings/document-types/custom-validation-rules.md) et les [règles de transformation](../../administration-and-setup/settings/global-settings/document-types/transformation-rules.md) sont visibles dans les paramètres avancés du type de document de NOVA sans lien bêta. Leurs interrupteurs d'activation restent sous le contrôle de l'administrateur. Ces fonctionnalités sont incluses dans le correctif VESTA prévu le 11 novembre 2026 avec toutes les autres anciennes fonctionnalités bêta de VESTA.
* **Des diagnostics de règles plus utiles.** Les règles de sélection de mise en page gagnent une option **Journaliser l'exécution**. La recherche de règles accepte les identifiants de règles, et l'ouverture d'un éditeur charge la règle enregistrée actuelle. Le journal d'exécution des règles existant reste l'endroit pour examiner ce qui a été exécuté.
* **Choisir et ouvrir des mises en page avec plus de contexte.** Recherchez les mises en page cibles, prévisualisez leur contenu et ouvrez directement la cible depuis une règle de sélection. Les règles de sélection d'approbation acceptent correctement les types de mise en page d'approbation pris en charge. Les administrateurs disposent également d'un raccourci depuis la validation de document vers l'éditeur de mise en page du type de document concerné.
* **Sélectionner plusieurs valeurs de condition.** Les conditions telles que **est l'une des** prennent en charge la sélection de plusieurs valeurs.
* **Trouver plus rapidement les champs de détection de doublons.** Le sélecteur de champs dans les paramètres de doublons du type de document est désormais consultable par recherche.

Les transformations après recherche de données de base, le journal d'exécution de base des règles, les éditeurs de règles élargis et les correctifs de duplication des règles standard disposent déjà d'implémentations dans la base VESTA. NOVA reprend ces fonctionnalités et rend les anciens contrôles de gestion bêta disponibles en tant que fonctionnalités standard.

Pour les étapes de configuration, les exemples et les tests, consultez [Règles de validation personnalisées](../../administration-and-setup/settings/global-settings/document-types/custom-validation-rules.md) et [Règles de transformation](../../administration-and-setup/settings/global-settings/document-types/transformation-rules.md). Pour choisir la mise en page utilisée par un document, consultez [Règles de sélection de mise en page](../../administration-and-setup/settings/global-settings/document-types/layout-manager/layout-selection-rules.md).

## Validation des factures électroniques : constats plus clairs et contrôles de politique

* **Un rapport organisé par niveau de validation.** Les constats sont regroupés en syntaxe, schéma, règles métier, règles de vérification croisée et règles spécifiques au pays, avec des groupes supplémentaires pour les autres vérifications de normes et les vérifications de valeurs. Les messages et les résumés utilisent la langue de l'utilisateur lorsque des traductions sont disponibles.
* **Des vérifications plus complètes et des résultats plus clairs.** Le validateur et le rapport mis à jour distinguent les erreurs, les avertissements et la sévérité effective après configuration spécifique à l'organisation. La page est nommée **Validation des factures électroniques**.
* **Politiques par type de document.** Les administrateurs peuvent vérifier si la validation des factures électroniques est activée et si les échecs bloquent le traitement. La vue des politiques identifie les remplacements par sous-type, et les modifications de politique sont enregistrées dans un historique des modifications.
* **Inspecter le XML dans une facture PDF.** Le visualiseur XML peut lire le XML intégré dans les PDF ZUGFeRD/Factur-X pris en charge, ouvrir la position référencée par un constat et revenir au document.
* **Rejeter avec une raison enregistrée.** Un réviseur autorisé peut rejeter un document éligible depuis le rapport de validation. Le rapport prépare une raison à partir de ses erreurs pour que le réviseur la vérifie avant de confirmer.
* **Corrections de format supplémentaires.** Les factures CII utilitaires EDNA sont reconnues, et les corrections apportées au mappage de la TVA XRechnung améliorent la manière dont les valeurs de facture pertinentes atteignent les champs DocBits.

Consultez [Règles de validation des documents électroniques](../../administration-and-setup/settings/document-processing/e-documents/validation-rules.md).

## Imports FTP/SFTP et e-mail

* **Configuration guidée FTP/SFTP.** L'assistant de connexion sépare les détails du serveur, les options d'import et la configuration. Les vérifications de connexion et les messages d'erreur plus clairs aident les administrateurs à identifier une connexion incorrecte ou un dossier source manquant.
* **Journaux d'import par étape.** Consultez la progression d'un fichier à travers l'import FTP, y compris le téléchargement et l'action configurée sur le fichier source.
* **Comportement configurable de nouvelle tentative et de notification.** Définissez l'intervalle entre les nouvelles tentatives ultérieures, la durée des nouvelles tentatives et les destinataires des notifications. Lorsque la fenêtre de nouvelle tentative est épuisée, la connexion peut être désactivée automatiquement et les destinataires notifiés ; l'assistant affiche l'avis de désactivation.
* **Suppression après import réussi.** En plus de conserver ou archiver les fichiers sources, les administrateurs peuvent choisir de les supprimer du serveur FTP/SFTP après un import réussi. L'archivage et la suppression sont des alternatives distinctes.
* **Reprise des imports plus fiable.** Les exécutions FTP simultanées ne peuvent plus envoyer deux fois le même fichier source. Lors de la modification d'une connexion, le mot de passe enregistré est conservé tant qu'il n'est pas remplacé. Le traitement des e-mails ne marque pas un message pour suppression si sa copie a échoué.
* **Prise en charge des e-mails signés.** Les messages S/MIME à signature opaque contenant des factures peuvent être décompressés au lieu d'être ignorés.
* **Historique et état de la configuration e-mail.** Les paramètres d'import indiquent qui a enregistré ou activé une configuration pour la dernière fois. Le commutateur d'e-mails entrants reflète l'état actif enregistré, y compris une configuration nouvellement enregistrée.

Consultez [Import FTP](../../end-user-and-partner-section/end-user-section/how-to-import-documents/ftp.md) et [Tester une connexion d'import FTP](../../administration-and-setup/settings/document-processing/import/test-ftp-import-connection.md).

## Traitement et extraction de documents

* **Redémarrer avec un nombre de pages choisi.** Le tableau de bord ajoute une action de redémarrage qui permet aux réviseurs de spécifier le nombre de pages à traiter pour ce document, dans la limite de son nombre réel de pages.
* **Consulter la limite de traitement.** Le tableau de bord peut afficher le nombre de pages traitées par rapport au nombre total de pages pour un document limité. Le paramètre **Pages à traiter** de l'organisation est regroupé sous Traitement des documents dans **Classer & Extraire**.
* **Contrôler l'extraction des champs masqués.** Les administrateurs peuvent choisir si les champs masqués participent à l'extraction via le paramètre **Extraire les champs masqués**.
* **Traitement plus rapide des lots volumineux.** Les redémarrages en masse de documents, les imports CSV de données de base, le traitement PDF et l'extraction de champs par règles bénéficient d'améliorations de performance.
* **Extraction IA plus résiliente.** Les dépassements de délai sont signalés comme tels, et les défaillances d'un modèle pris en charge peuvent basculer vers un autre modèle disponible. Des corrections supplémentaires gèrent les clés répétées dans la sortie IA, les synonymes de champs configurés et les définitions de tableaux enregistrées vides.
* **Conserver la valeur saisie.** Enregistrer une cellule de tableau sans cliquer ailleurs au préalable conserve la valeur saisie. Les dates dont les noms de mois sont confondus par l'OCR sont gérées de manière plus fiable.

## Rapprochement, approbation et export des commandes d'achat

Le [guide des Règles de rapprochement des commandes](../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-matching-rules.md) explique comment activer le rapprochement par règles, configurer les types de rapprochement et les tolérances, définir l'ordre d'exécution et gérer les versions de règles.

* **Effectuer le rapprochement dans les deux sens.** Sélectionnez les lignes du document et reliez-les aux lignes de commande d'achat, ou partez des lignes de commande d'achat. Cette option est utile lorsque plusieurs lignes de bon de livraison sont liées à une seule ligne de commande d'achat.
* **Préserver le détail des lignes un-à-plusieurs.** Une configuration de rapprochement peut désormais conserver une sous-ligne individuelle pour chaque ligne de document lorsque plusieurs lignes correspondent à une seule ligne de commande d'achat. Cette option est désactivée par défaut. L'export API générique peut regrouper les requêtes par colonnes de lignes configurées, prenant en charge les livraisons ou conteneurs nécessitant des enregistrements cibles distincts.
* **Configurer le repli sur la dernière ligne.** Les organisations peuvent contrôler si la ligne restante du document et de la commande d'achat peut être rapprochée par le repli sur ligne unique.
* **Rapprochement et affichage plus précis.** Les corrections préservent la base de prix correcte pour les rapprochements convertis en conditionnement, héritent du statut de la ligne de commande d'achat sur les lignes d'échéancier et affichent les quantités reçues à partir des lignes de réception.
* **Empêcher l'approbation prématurée et les doublons.** L'approbation finale est bloquée tant que des écarts pertinents sur la commande d'achat restent non approuvés. L'exécution répétée du flux de travail ne crée pas de nouvelle tâche ouverte pour le même groupe, et les vérifications de doublons d'export sont effectuées avant l'approbation.
* **Distinguer Exported de Finished.** Les actions d'export peuvent sélectionner le statut après un export réussi. **Exported** dispose de son propre badge sur le tableau de bord. Les organisations qui activent le verrouillage des documents terminés empêchent les flux de travail ordinaires ou les redémarrages de rouvrir des documents terminés ; les dérogations autorisées sont enregistrées.
* **Diagnostic plus clair des flux de travail.** Un filtre du tableau de bord permet de trouver les documents bloqués par la limite d'exécution du flux de travail. Les exécutions de flux de travail peuvent être consultées dans une fenêtre contextuelle, et un refus de changement de statut indique le statut du document.
* **Corrections supplémentaires pour l'export.** Les tentatives de validation et d'approbation M3 sont ajustées, et les configurations d'export fournisseur conditionnelles sont correctement gérées.

## Utilisabilité et accès au quotidien

* **Navigation plus fiable.** Les adresses de documents mises à jour disposent de redirections pour les anciens liens. Les liens profonds NOVA conservent le canal souhaité à travers la connexion, et la progression du chargement indique quelle partie de la page est en cours de préparation.
* **Préférences de travail personnelles.** L'ordre des colonnes de commande d'achat est enregistré par utilisateur, et l'écran d'approbation mémorise le panneau latéral ouvert de l'utilisateur.
* **Vues des tâches et tableaux de bord plus fiables.** Les tâches sans assigné peuvent être listées, ouvertes et assignées. Le tableau des tâches se recharge lorsque l'organisation sélectionnée est prête, les plages de dates personnalisées du tableau de bord sont correctement appliquées, et les lignes de documents en double sont évitées.
* **Meilleures étiquettes et journaux.** Les administrateurs peuvent modifier les clés de traduction des champs et des colonnes de tableaux. Les colonnes du journal des documents peuvent être redimensionnées, les colonnes de tableau de bord personnalisées gèrent les identifiants de champs en casse mixte, et les étiquettes et noms de fichiers longs s'affichent de manière plus cohérente.
* **Périmètre des notifications.** Les règles d'e-mail de statut de document peuvent être limitées à une sous-organisation.
* **Intégration des fournisseurs.** Les liens d'inscription sans mot de passe au portail fournisseurs restent valides pendant **21 jours au lieu de 7 jours**. Les administrateurs peuvent également configurer le titre du message d'erreur de téléversement d'un champ de fichier dans une mise en page fournisseur.
* **Fiabilité de la connexion.** La connexion SAML ne réutilise plus les sessions expirées ou révoquées. La connexion de gestion prend en charge l'étape MFA requise, et les adhésions inactives ne peuvent pas recevoir de nouvelle invitation de définition de mot de passe.
* **Images du tableau d'idées.** Les images téléchargées sont stockées et servies séparément de la description de l'idée, améliorant ainsi la gestion des images.
* **Basculement contrôlé entre canaux.** Le paramètre de canal de publication peut être rendu en lecture seule lorsque le basculement n'est pas activé pour l'environnement. Consultez l'annonce de publication pour connaître la disponibilité.

## Assistants connectés et outils d'intégration

Pour les organisations et les partenaires utilisant l'intégration DocBits MCP, NOVA ajoute des outils permettant de lister les règles de validation résolues, de tester une règle sur un document sans enregistrer de modifications, et d'expliquer les preuves d'exécution de règles stockées. Les assistants connectés peuvent également lister les demandes d'amélioration et soumettre une approbation autorisée par un administrateur via le même processus de revue que l'application web. Les autorisations existantes au niveau de l'organisation et du document s'appliquent.

## Fonctionnalités déjà présentes dans VESTA

NOVA reprend également les fonctionnalités listées ci-dessous. Lorsque l'accès était auparavant limité à la bêta VESTA, la disponibilité standard fait partie de cette version NOVA et est prévue pour le correctif VESTA du 11 novembre 2026. La liste décrit les fonctionnalités antérieures, ainsi que les changements de disponibilité et les améliorations expliqués ci-dessus :

* L'Assistant de configuration original, sa recherche de documentation, le flux de base prévisualisation/confirmation/annulation et les alertes proactives de santé des imports e-mail/FTP.
* Les niveaux IA Fast, Full, Nexus et Auto ainsi que le paramètre de mode vision.
* Le contrôle de champ d'en-tête et le rapport d'origine des valeurs original.
* La première version de Touchless Intelligence, le diagnostic fournisseur, l'analyse en masse et le diagramme de décision des commandes d'achat.
* Les moteurs de règles sous-jacents de validation, de transformation et de sélection de disposition, les transformations après recherche de données de référence et le journal d'exécution de règles de base.
* Les améliorations antérieures de la recherche dans le tableau de bord, MFA, les domaines e-mail d'organisation vérifiés, la tolérance de facturation et l'augmentation de la limite d'exécution de workflow à 50.

Consultez le [correctif VESTA du 14 octobre](incremental-updates-14-october-2026.md), le [correctif du 15 septembre](incremental-updates-15-september-2026.md) et les [notes de version antérieures](README.md#vesta-hotfix-releases) pour l'historique des versions VESTA.

## Versions des services NOVA

Ce sont les versions et les horodatages de déploiement de l'**instantané du 16 octobre 2026**. Les horodatages décrivent des déploiements individuels de services, et non une date de publication distincte pour chaque fonctionnalité.

| Service | Version | Horodatage de déploiement |
| --- | --- | --- |
| API Service | `13.26.5` | 16.10.2026 11:57:49 |
| Auth Bridge | `0.5.11` | 08.10.2026 10:56:15 |
| Auth Service | `1.84.3` | 16.10.2026 12:19:50 |
| Auto Accounting | `1.23.6` | 15.09.2026 09:42:57 |
| Barcode Service | `1.20.3` | 15.10.2026 14:17:18 |
| Docflow Service | `2.13.9` | 15.10.2026 16:14:37 |
| Docnet Service | `1.59.1` | 12.10.2026 00:59:12 |
| Email Service | `1.44.4` | 16.10.2026 11:44:58 |
| Extraction Service | `1.63.1` | 15.10.2026 19:34:17 |
| FTP Service | `1.37.4` | 15.10.2026 10:42:01 |
| Fulltext Service | `1.46.1` | 12.10.2026 05:16:16 |
| Ideas Service | `0.5.6` | 14.10.2026 12:06:00 |
| OCR Service | `1.11.8` | 12.10.2026 01:00:00 |
| Operator Service | `1.45.0` | 12.10.2026 09:35:25 |
| PO Match Service | `1.65.7` | 14.10.2026 16:14:20 |
| Web App | `10.72.2` | 16.10.2026 12:04:41 |

Les numéros de version progressent indépendamment sur les deux canaux. Un numéro plus élevé ne signifie pas à lui seul qu'un service dispose d'une nouvelle fonctionnalité client. Les modifications examinées d'Auto Accounting, Barcode, Docnet, Fulltext, OCR et Operator sont des modifications de maintenance ou de fiabilité de traitement ; elles n'introduisent pas de workflow client distinct dans cette comparaison. Les mises à jour d'Auth Bridge améliorent la fiabilité de la synchronisation inter-régions des comptes.
