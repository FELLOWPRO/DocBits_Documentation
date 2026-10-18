---
description: "Cinq chapitres en français sur les workflows avancés et leurs journaux, avec sous-titres et transcriptions."
---

# Vidéos Advanced Workflow

Apprenez à créer, tester et diagnostiquer un workflow avancé. Les cinq chapitres sont commentés en français.

Les trois premiers chapitres montrent l’interface réelle de DocBits. Les deux chapitres sur les journaux utilisent des schémas pédagogiques identifiés comme illustrations. Les captures montrent des brouillons de démonstration non enregistrés.

Chaque vidéo propose des sous-titres WebVTT et une transcription dépliable.

1. [Constructeur et canevas](#builder-and-canvas) · 1:52
2. [Nœuds et chemins](#nodes-and-routes) · 1:49
3. [Variables, tests et activation](#variables-tests-and-activation) · 1:53
4. [Trouver l’exécution pertinente](#find-the-relevant-execution) · 1:45
5. [Suivre les nœuds et diagnostiquer](#trace-nodes-and-diagnose) · 1:47

## Constructeur et canevas {#builder-and-canvas}

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas/v2/fr.mp4" %}

[Sous-titres (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas/v2/fr.vtt) · 1:52

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

[Sous-titres (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_logic/v2/fr.vtt) · 1:49

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

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_testing/v2/fr.mp4" %}

[Sous-titres (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_testing/v2/fr.vtt) · 1:53

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

**Examinez les résultats**

Examinez messages et durées : vert, succès ; orange, condition fausse ; rouge, erreur ; gris, ignoré. Corrigez et retestez. Le gestionnaire de tests permet des scénarios reproductibles : succès, alternatives, données absentes et erreurs.

**Enregistrez avant d’activer**

Le brouillon local est enregistré automatiquement environ toutes les trente secondes après modification. Enregistrez explicitement sur le serveur. Activez après le premier enregistrement. Vérifiez l’état dans la liste avant d’attendre une exécution automatique.

</details>

## Trouver l’exécution pertinente {#find-the-relevant-execution}

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_search/v2/fr.mp4" %}

[Sous-titres (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_search/v2/fr.vtt) · 1:45

<details>
<summary>Transcription</summary>

**Ouvrez les journaux**

Dans le tableau de bord documentaire, ouvrez Workflow Logs depuis Actions. L’accès aux workflows doit être activé. Ces journaux concernent le document choisi. Les tests du concepteur et les journaux d’événements ou d’activité de l’organisation sont distincts.

**Lisez les compteurs**

Bleu compte les exécutions affichées ; rouge, les erreurs ; jaune, les conditions fausses ; vert, les succès. Les compteurs représentent des exécutions, pas des définitions de workflow ni des nœuds. Les filtres modifient ces nombres.

**Choisissez le bon passage**

Chaque ligne affiche nom du workflow, date de création, durée en secondes et résultat. Un workflow peut s’exécuter plusieurs fois sur un document. Comparez les horodatages. Une durée brève peut être arrondie à zéro virgule zéro zéro seconde.

**Affinez les résultats**

Recherchez un workflow. L’icône de réglage ouvre sens et critère de tri, état, date de début et date de fin. Triez par nom ou création. Entrez les dates dans l’ordre année, mois, jour, puis appliquez.

**Vérifiez pages et filtres**

La pagination donne accès aux résultats anciens. Effacer les filtres recharge la liste sans sélections. Effacez la recherche séparément. Sans résultat, vérifiez document, dates et état. Une liste vide ne prouve pas un échec.

**États particuliers**

Un bandeau et une icône de blocage signalent la limite d’exécutions du document. Examinez les déclenchements répétés avant de modifier cette limite. Le téléchargement vidéo DocOperator apparaît uniquement si un enregistrement existe ; il concerne cette exécution.

</details>

## Suivre les nœuds et diagnostiquer {#trace-nodes-and-diagnose}

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_diagnosis/v2/fr.mp4" %}

[Sous-titres (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_diagnosis/v2/fr.vtt) · 1:47

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
