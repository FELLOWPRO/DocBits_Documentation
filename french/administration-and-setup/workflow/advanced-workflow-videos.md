---
description: "Cinq chapitres en français sur les workflows avancés et leurs journaux, avec sous-titres et transcriptions."
---

# Vidéos Advanced Workflow

Apprenez à créer, tester et diagnostiquer un workflow avancé. Les cinq chapitres sont commentés en français.

Les trois premiers chapitres montrent le véritable concepteur DocBits avec des brouillons de démonstration. L’aperçu de recherche montre le traitement réel des documents et les commandes des journaux avec des résultats vides. Le chapitre de diagnostic utilise encore des schémas pédagogiques identifiés comme illustrations.

Chaque vidéo propose des sous-titres WebVTT et une transcription dépliable.

1. [Constructeur et canevas](#builder-and-canvas) · 1:52
2. [Nœuds et chemins](#nodes-and-routes) · 1:49
3. [Variables, tests et activation](#variables-tests-and-activation) · 1:53
4. [Trouver l’exécution pertinente](#find-the-relevant-execution) · 1:45
5. [Suivre les nœuds et diagnostiquer](#trace-nodes-and-diagnose) · 1:47

## Constructeur et canevas {#builder-and-canvas}

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas/v2/fr.mp4" %}

[Ouvrir la vidéo](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas/v2/fr.mp4) · [Sous-titres (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas/v2/fr.vtt) · 1:52

<details>
<summary>Transcription</summary>

**Une facture, deux chemins**

Voici un véritable workflow avancé dans DocBits. Un contrôle du montant de la facture mène à deux actions. Les connexions déterminent l’action exécutée. Cet exemple utilise un brouillon non enregistré et des champs de démonstration.

**Configurer le contrôle du montant**

Ouvrez Ajouter, choisissez And et sélectionnez une condition de champ du document. Indiquez le champ du montant, choisissez Supérieur à et saisissez mille. Utilisez la clé exacte du champ définie dans votre configuration documentaire.

**Configurer les actions**

Ajoutez deux cartes Then. Chacune renseigne le champ de démonstration approval route. L’une écrit Approval, l’autre Standard. Ces valeurs identifient le chemin. Configurez vos actions métier pour un workflow de production.

**Relier les sorties**

Reliez Start à l’entrée de la condition. Reliez la sortie bleue de succès à Approval et la sortie orange de condition fausse à Standard. La sortie rouge traite séparément les erreurs d’évaluation. La position des cartes ne crée pas de chemin.

**Préparer les cas de test**

Ouvrez Tester dans la barre d’outils. Choisissez un document de test ou saisissez ses données complètes au format JSON. Vérifiez les montants supérieurs, inférieurs et égaux à mille, ainsi que les valeurs absentes. Examinez les résultats des nœuds après exécution.

**Valider, enregistrer et activer**

Validez les connexions et les paramètres des cartes. Enregistrez explicitement sur le serveur, puis vérifiez l’activation séparément. Les brouillons automatiques du navigateur ne remplacent pas l’enregistrement. L’exécution et les journaux nécessitent le module et l’abonnement appropriés.

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
