# Journaux de workflow

Pour des explications commentées de la vue avancée des journaux, regardez [Find the relevant execution](advanced-workflow-builder/videos.md#find-the-relevant-execution) et [Trace nodes and diagnose](advanced-workflow-builder/videos.md#trace-nodes-and-diagnose). Les deux chapitres sont disponibles en anglais et en allemand, avec fichiers de sous-titres et transcriptions.

## **Aperçu**

Les **Workflow Logs** permettent aux utilisateurs d'analyser quels Workflows ont été exécutés pour un document, de comprendre les résultats d'exécution et d'examiner les détails au niveau des conditions pour le débogage ou la validation.

## **Accès aux Workflow Logs**

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.mp4" %}

**Vidéo :** Lire les journaux de workflow · 1:34 · [Captions (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.vtt)

<details>

<summary>Transcription</summary>

**Ouvrir les journaux de workflow** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.mp4#t=0.25)

Chaque document conserve les journaux des Workflows qui se sont exécutés sur lui. Dans le Dashboard des documents, ouvrez les actions d'un document et choisissez Workflow Logs.

**Exécutions et leurs résultats** · [0:12](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.mp4#t=12.15)

En haut, vous voyez combien d'exécutions ont eu lieu et combien se sont terminées par une erreur, une condition non remplie ou un succès. En dessous, chaque exécution est listée avec son Workflow, son heure, sa durée et son résultat.

**Le chemin d'une exécution** · [0:25](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.mp4#t=25.716)

Faites glisser le séparateur vers la gauche pour donner plus de place aux journaux. Cliquez ensuite sur une exécution pour voir le chemin qu'elle a suivi. Chaque carte affiche son résultat : vert pour un succès, orange pour une condition non remplie, rouge pour une erreur. Ici, la carte And s'est terminée par une condition non remplie, donc la carte Then qui la suit ne s'est pas exécutée.

**Pourquoi une carte s'est terminée ainsi** · [0:45](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.mp4#t=45.35)

Sélectionnez une carte pour lire son journal. Il indique ce que la carte a comparé et pourquoi elle s'est terminée ainsi. Ici, le document est prêt pour la validation, mais la carte attend le statut « deuxième approbation en attente ».

**Une erreur et sa raison** · [0:58](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.mp4#t=58.283)

Une exécution qui se termine par une erreur affiche en rouge la carte en échec. Ici, la carte And n'a pas pu lire l'adresse de livraison dans le document. Une donnée manquante est toujours une erreur, donc la carte Then qui la suit ne s'est pas exécutée.

**Trouver des exécutions** · [1:13](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.mp4#t=73.216)

Lorsque les exécutions sont nombreuses, utilisez la recherche pour trouver un Workflow par son nom, et le bouton de filtre pour réduire la liste par statut ou par date.

**Note sur la limite d'exécution** · [1:23](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.mp4#t=83.116)

Une note apparaît en haut lorsqu'un Workflow a atteint sa limite d'exécution sur ce document. La vidéo sur les limites d'exécution l'explique.

</details>

Pour accéder aux Workflow Logs :

1. Naviguez jusqu'au **Dashboard**.
2. Cliquez sur le **Actions menu** (icône à trois points) à côté du document souhaité.
3. Sélectionnez **Workflow Logs** dans le menu.
   * <mark style="color:red;">**Note**</mark> : la fonctionnalité Workflow doit être activée pour accéder à cette option.
4.  Un **side panel** s'ouvre et présente un résumé des Workflows exécutés.\\

    <div align="left"><figure><img src="../../.gitbook/assets/image (5).png" alt="Dashboard with the workflow logs side panel showing summary counters and a table of executed workflows with result icons" width="563"><figcaption></figcaption></figure></div>

## **Ouvrir un journal sur sa propre page**

Le side panel masque la liste des documents. Pour un document dont vous examinez le Workflow pendant un certain temps, ouvrez le même journal dans une page complète : sélectionnez l'icône de nouvelle fenêtre dans l'en-tête du panneau. Cette page a l'adresse `/workflows/logs/<document id>`, vous pouvez donc la garder ouverte dans une deuxième fenêtre du navigateur ou envoyer l'adresse à un collègue qui a accès au document.

La page affiche les mêmes compteurs de résumé, le même tableau des Workflows exécutés et la même vue détaillée que le panneau.

## **Passer à un autre document**

Sur la page complète, un champ de recherche au-dessus de la liste trouve un document par son nom ou par son ID. Les résultats affichent la date d'import, l'assigné et le statut de chaque document, ce qui vous permet de distinguer des documents aux noms similaires. La sélection d'un résultat charge son journal de Workflow et place le document dans l'adresse. La recherche couvre les documents de votre organisation que vos autorisations vous permettent de voir ; lorsque rien ne correspond, DocBits l'indique sous le champ au lieu d'afficher une liste vide.

## **Composants du panneau Workflow Logs**

#### **1. Compteurs de résumé des Workflows**

Situés en haut du panneau des journaux :

* **Bleu** : nombre total de Workflows exécutés.
* **Rouge** : Workflows qui se sont terminés par des **erreurs**.
* **Jaune** : Workflows qui n'ont **pas été terminés** en raison de conditions non remplies.
* **Vert** : Workflows **exécutés** avec succès.

#### **2. Tableau des exécutions de Workflow**

Chaque ligne du tableau représente une exécution de Workflow et comprend :

* **Workflow Name**
* **Timestamp** (Created On)
* **Runtime** (en secondes)
* **Result Icon** :
  * Coche verte : le Workflow a été exécuté avec succès.
  * Croix rouge : le Workflow a été exécuté avec une erreur.
  * Tiret orange : l'exécution a été arrêtée car une condition n'était pas remplie

Cliquer sur la **flèche** à gauche de chaque ligne développe la **vue détaillée du Workflow**.

<div align="left"><figure><img src="../../.gitbook/assets/workflow_test9_match_check_overview.png" alt="Expanded workflow log row showing When and And condition cards with green checks and a grayed card that was not met, plus card logs" width="563"><figcaption></figcaption></figure></div>

### **Vue détaillée du Workflow**

Cliquer sur une ligne de Workflow spécifique ouvre son **journal d'exécution détaillé**, qui affiche :

#### **Évaluation des conditions**

* Bloc **When...** : condition initiale.
* Bloc(s) **And...** : conditions supplémentaires.
* Bloc(s) **Then...** : actions effectuées lorsque toutes les conditions sont remplies.

Chaque ligne de condition indique :

* **Coche verte** : la condition était remplie.
* **Tiret orange** : la condition n'était pas remplie.
* **Croix rouge** : la condition a échoué **en raison d'une erreur**

### **Note importante sur le comportement**

Si une condition d'un Workflow n'est **pas remplie**, le système **cesse d'évaluer les autres cartes de Workflow** de ce Workflow. Ce comportement évite un traitement inutile\
Comme indicateur visuel, la carte qui **ne remplit pas sa condition** s'affiche en **gris**, et toutes les **cartes suivantes** du même Workflow apparaissent également en **gris**, ce qui indique qu'elles n'ont **pas été exécutées**.
