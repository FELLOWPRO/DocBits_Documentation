---
description: "Cinq chapitres en français sur les workflows avancés et leurs journaux, avec sous-titres et transcriptions."
---

# Vidéos Advanced Workflow

Les cinq chapitres proposent une narration en français, un fichier de sous-titres et une transcription. Le premier montre la création du workflow de démonstration étape par étape ; les suivants approfondissent les différents sujets.

Les trois premiers chapitres montrent le véritable concepteur DocBits avec des brouillons de démonstration. L’aperçu de recherche montre le traitement réel des documents et les commandes des journaux avec des résultats vides. Le chapitre de diagnostic utilise encore des schémas pédagogiques identifiés comme illustrations.

Chaque vidéo propose des sous-titres WebVTT et une transcription dépliable.

1. [Constructeur et canevas](#builder-and-canvas) · 5:06
2. [Nœuds et chemins](#nodes-and-routes) · 1:49
3. [Variables, tests et activation](#variables-tests-and-activation) · 1:53
4. [Trouver l’exécution pertinente](#find-the-relevant-execution) · 1:45
5. [Suivre les nœuds et diagnostiquer](#trace-nodes-and-diagnose) · 1:47

## Constructeur et canevas {#builder-and-canvas}

Rencontrez Alain et suivez ses explications dans la véritable interface française de DocBits. Il vérifie le tableau de bord, la liste des workflows et la licence, puis ouvre un brouillon non enregistré dans le concepteur. Il nomme le workflow, configure le contrôle du montant et deux actions, dispose les cartes et relie les deux chemins, étape par étape. Il présente ensuite la préparation des tests avec un document ou des données personnalisées. Le compte de démonstration ne dispose pas d’abonnement Advanced Workflow et bloque la validation ; le brouillon reste non enregistré et inactif.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-small-monitor-d/fr.mp4" %}

[Ouvrir la vidéo](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-small-monitor-d/fr.mp4) · [Sous-titres (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-small-monitor-d/fr.vtt) · [Transcription (texte)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-small-monitor-d/fr.txt) · 5:06

| Dans cette vidéo | Début |
| --- | --- |
| Présentation de l’administrateur | [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-small-monitor-d/fr.mp4#t=0) |
| Vérifier l’accès | [0:10](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-small-monitor-d/fr.mp4#t=10) |
| Nommer le workflow | [0:43](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-small-monitor-d/fr.mp4#t=43) |
| Configurer le contrôle du montant | [1:02](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-small-monitor-d/fr.mp4#t=62) |
| Ajouter l’action Approval | [1:37](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-small-monitor-d/fr.mp4#t=97) |
| Ajouter l’action Standard | [2:06](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-small-monitor-d/fr.mp4#t=126) |
| Organiser les cartes | [2:34](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-small-monitor-d/fr.mp4#t=154) |
| Relier les chemins | [3:06](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-small-monitor-d/fr.mp4#t=186) |
| Préparer les tests | [3:51](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-small-monitor-d/fr.mp4#t=231) |
| Valider, enregistrer et activer | [4:29](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-small-monitor-d/fr.mp4#t=269) |

<details>
<summary>Transcription</summary>

**Présentation de l’administrateur**

Je m’occupe de DocBits ici. Je vous montre comment créer un contrôle de facture avec deux chemins.

**Vérifier l’accès**

Je commence dans le tableau de bord des workflows et j’ouvre la liste. Ensuite, je vérifie la licence. Workflow et Advanced Workflow doivent tous les deux disposer d’un accès actif. Lorsque ces accès sont actifs, Nouveau workflow propose Advanced Workflow. Ce compte de documentation n’a pas de licence workflow active. Je continue donc avec un aperçu non enregistré dans le concepteur.

**Nommer le workflow**

Je travaille dans le véritable concepteur DocBits. Je donne d’abord un nom clair au brouillon. Nous vérifierons un montant de facture et utiliserons deux actions simples pour montrer les chemins possibles. Cette démonstration reste non enregistrée.

**Configurer le contrôle du montant**

J’ouvre le menu d’ajout et je choisis une carte de condition. Dans la catégorie Champ de document, je sélectionne la condition Docfield. Je renseigne le champ total_amount. Puis je choisis le comparateur supérieur à. Et je saisis mille. Utilisez votre propre identifiant de champ. Un montant égal à mille ne satisfait pas cette comparaison.

**Ajouter l’action Approval**

J’ajoute maintenant une carte d’action de la catégorie Champ de document. Cette action définit la valeur d’un champ du document. J’utilise la clé de démonstration approval_route. Et je saisis la valeur Approval. Cela identifie le chemin. Un véritable processus d’approbation nécessite ses propres actions métier.

**Ajouter l’action Standard**

J’ajoute une deuxième carte avec la même action. Cette fois, le champ de démonstration reçoit la valeur Standard. Les deux cartes sont configurées. Leurs connexions doivent encore déterminer quelle action sera exécutée.

**Organiser les cartes**

Je déplace les cartes pour obtenir une disposition lisible. Les deux actions vont à droite. La condition est au centre et Start à gauche. Déplacer une carte change sa position. Cela ne crée aucune connexion.

**Relier les chemins**

Je relie la sortie de Start à l’entrée de la condition. Le chemin de succès rejoint Approval par une connexion bleue. Le chemin orange de condition non satisfaite rejoint Standard. La sortie rouge d’erreur est distincte et traite les erreurs d’évaluation. Ici, elle reste sans connexion. Dans un workflow de production, définissez comment traiter ces erreurs.

**Préparer les tests**

Le bouton de test dans la barre d’outils ouvre la sélection d’un document de test. Je peux choisir un document de démonstration ou préparer des données personnalisées complètes. Testez des montants supérieurs, inférieurs et égaux à mille. Vérifiez aussi un montant absent. Ce compte n’a pas de licence Advanced Workflow. Je montre la préparation du test, pas un résultat exécuté.

**Valider, enregistrer et activer**

La validation vérifie les connexions et les paramètres des cartes. Ici, l’absence de licence bloque cette validation. Avec un compte autorisé, j’enregistrerais explicitement le workflow sur le serveur. Ensuite, je vérifierais séparément l’activation. L’interrupteur est désactivé avant le premier enregistrement. L’indicateur de brouillon automatique désigne une copie locale du navigateur. Il ne signifie pas que le workflow est enregistré ou activé.

</details>

## Nœuds et chemins {#nodes-and-routes}

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_logic/v2/fr.mp4" %}

[Ouvrir la vidéo](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_logic/v2/fr.mp4) · [Sous-titres (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_logic/v2/fr.vtt) · 1:49

<details>
<summary>Transcription</summary>

**Le rôle de chaque nœud**

Start lance manuellement. When définit un événement. Aucun des deux ne reçoit de connexion entrante. And vérifie une condition. Then exécute une action. Les deux constructeurs partagent le catalogue de cartes. Les notes expliquent sans être exécutées.

**Trois résultats distincts**

Reliez une sortie à l’entrée suivante. Dans le concepteur, bleu signifie succès, orange condition fausse, rouge erreur. And possède trois résultats ; Then, succès et erreur. Les vues d’exécution affichent le succès en vert.

**Construisez une alternative**

Vérifiez si une facture dépasse le seuil. Reliez bleu à l’approbation, orange au traitement normal et rouge à la gestion des erreurs. Une condition fausse continue par son chemin connecté ; elle n’arrête pas toutes les branches.

**Joindre avec Wait ALL**

Wait ALL réunit des branches. Chaque nœud source doit avoir suivi un chemin relié à la jonction. Connectez les deux contrôles requis et l’action suivante. Un chemin non sélectionné ne fournit pas le résultat attendu.

**Alternatives avec ANY et OR**

Wait ANY et OR réunissent les branches si au moins une source suit un chemin connecté. OR exige deux nœuds sources distincts. Ces jonctions ne rendent pas les choix exclusifs et n’annulent pas d’autres actions. Testez le graphe entier.

**Gardez un graphe exécutable**

Rendez les nœuds accessibles depuis une entrée. Évitez les cycles et les connexions entrantes vers Start ou When. Incluez une action Then et validez les chemins. Les nœuds Delay importés exigent une durée positive ; Ajouter ne propose pas Delay.

</details>

## Variables, tests et activation {#variables-tests-and-activation}

Suivez le workflow de facture connecté dans le véritable concepteur DocBits. Ouvrez Variables, comparez les types et la référence de document, repérez Valider, préparez des tests avec document ou données personnalisées, puis identifiez Enregistrer et l’activation. Les scènes de test montrent la configuration des données d’exemple ; elles ne montrent pas de résultat exécuté.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_testing/v3/fr.mp4" %}

[Ouvrir la vidéo](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_testing/v3/fr.mp4) · [Sous-titres (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_testing/v3/fr.vtt) · 1:57

<details>
<summary>Transcription</summary>

**Choisissez le type**

Ouvrez Variables avec les accolades. Choisissez texte, nombre, oui ou non, ou document. Recherchez les noms. Document contient une référence définie par une action dédiée ; ce formulaire n’accepte pas de valeur documentaire.

**Portée de l’organisation**

Choisissez un nom unique, un type et une valeur initiale. Création, modification et suppression sont enregistrées immédiatement dans l’organisation. D’autres workflows partagent ces valeurs. Enregistrer ou abandonner le canevas n’annule pas ces changements.

**Validez la structure**

Cliquez sur Valider. Examinez erreurs et avertissements au-dessus du canevas. Un message cible son nœud. Vérifiez actions, entrées, sorties, cycles et jonctions. Une structure valide ne garantit pas des données correctes.

**Choisissez le contexte**

La lecture dans la barre ouvre le choix du document. Choisissez document, données personnalisées ou test sans document pour les cartes indépendantes. Start lance directement. Les tests incluent les modifications non enregistrées et simulent les actions destructrices.

**Préparer et vérifier les scénarios de test**

Préparez des tests au-dessus, au-dessous et exactement à mille, puis sans données. Après exécution, vérifiez les messages et les durées : vert signifie réussite, orange faux, rouge erreur, gris ignoré. Retestez les corrections. Le gestionnaire de tests permet de répéter les scénarios.

**Enregistrez avant d’activer**

Le brouillon local est enregistré automatiquement environ toutes les trente secondes après modification. Enregistrez explicitement sur le serveur. Activez après le premier enregistrement. Vérifiez l’état dans la liste avant d’attendre une exécution automatique.

</details>

## Trouver l’exécution pertinente {#find-the-relevant-execution}

{% hint style="info" %}
Aperçu à tester : véritables écrans DocBits avec actions du document, flux de documents, durée des étapes, journaux vides et filtres de statut et de date. Le document ne contient aucune exécution Advanced Workflow enregistrée. Cet aperçu ne montre pas encore les lignes d’exécution, la pagination ni le diagnostic des nœuds.
{% endhint %}

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_search/v3/fr.mp4" %}

[Ouvrir la vidéo](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_search/v3/fr.mp4) · [Sous-titres (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_search/v3/fr.vtt) · 1:46

<details>
<summary>Transcription</summary>

**Commencer par le document**

Dans le tableau de bord des documents, ouvrez le menu des actions et choisissez le flux de documents. L’historique réel montre l’importation et l’OCR. Ouvrez une étape pour examiner les temps d’attente et de traitement. Ces étapes sont distinctes des nœuds Advanced Workflow.

**Lire les compteurs réels**

Voici les journaux de workflow du même document. Le bleu indique le total, le rouge les erreurs, le jaune les conditions non remplies et le vert les réussites. Ce document de démonstration ne contient aucune exécution enregistrée. Les quatre compteurs affichent donc zéro.

**Vérifier les colonnes des exécutions**

Les colonnes indiquent le nom du workflow, la date de création, la durée et le résultat. Distinguez les exécutions répétées grâce à l’horodatage. Ce document ne contient aucune ligne à ouvrir.

**Ouvrir les filtres de statut**

L’icône des filtres ouvre le véritable menu. Triez par nom ou date de création, dans l’ordre croissant ou décroissant. Le statut propose réussite, condition non remplie et erreur.

**Choisir les dates et effacer les filtres**

Choisissez une période avec les dates de début et de fin ou le calendrier. Le format est année, mois et jour. Appliquer demande les résultats. Effacer les filtres réinitialise la sélection. Effacez la recherche séparément. Dans cette version, les mois du calendrier restent en anglais.

**Aperçu : une exécution enregistrée manque encore**

Cet aperçu permet de vérifier l’accès au document, les détails du traitement et les commandes des journaux. Une exécution Advanced Workflow enregistrée manque encore pour montrer les lignes réelles, la pagination, les routes et les messages des nœuds. Ces résultats ne sont pas simulés dans la vidéo.

</details>

## Suivre les nœuds et diagnostiquer {#trace-nodes-and-diagnose}

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_diagnosis/v2/fr.mp4" %}

[Ouvrir la vidéo](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_diagnosis/v2/fr.mp4) · [Sous-titres (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_diagnosis/v2/fr.vtt) · 1:47

<details>
<summary>Transcription</summary>

**Développez une exécution**

Développez la ligne du workflow. Une exécution avancée affiche le graphe à gauche et les messages à droite ; un workflow standard montre une suite de cartes. Ces données décrivent cette exécution et peuvent différer du concepteur actuel.

**Sélectionnez un nœud**

Déplacez ou zoomez le graphe, puis cliquez sur un nœud. Card Logs affiche ses messages. Wait ALL et Wait ANY peuvent aussi avoir des messages de nœud. Reliez le message au nœud sélectionné et à l’horodatage.

**Distinguez les états**

Vert signifie succès ; orange, condition fausse ; rouge, erreur ; gris, ignoré. Un nœud ignoré n’a pas été exécuté. Avant de le modifier, vérifiez si une autre branche a été choisie ou si une entrée de jonction manque.

**Suivez la première divergence**

Suivez le chemin réel depuis l’entrée. Pour un contrôle de montant faux, examinez orange ; pour une erreur, lisez le message et examinez rouge. Le traitement d’erreur peut réussir tandis que l’exécution conserve l’erreur initiale.

**Vérifiez les jonctions**

Pour Wait ALL, contrôlez chaque source et résultat connecté. Pour ANY ou OR, cherchez une source correspondante. Deux sorties du même nœud ne constituent pas des approbations indépendantes. Une condition orange peut être voulue.

**Corrigez et vérifiez**

Notez workflow, référence documentaire, horodatage, nœud et message exact. Corrigez données ou configuration, puis testez un scénario reproductible. Enregistrez et vérifiez l’activation. Comparez une nouvelle exécution à l’ancienne ; les anciens journaux conservent le comportement antérieur.

</details>
