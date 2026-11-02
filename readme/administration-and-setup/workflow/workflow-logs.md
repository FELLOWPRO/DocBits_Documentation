# Journaux de flux de travail

## Vidéo

La vidéo de recherche est un aperçu avec de véritables écrans DocBits. La vidéo de diagnostic utilise encore des schémas pédagogiques identifiés comme illustrations.
### Trouver l’exécution pertinente

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

### Suivre les nœuds et diagnostiquer

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

## **Aperçu**

Les **Journaux de flux de travail** permettent aux utilisateurs d'analyser quels flux de travail ont été exécutés pour un document, de comprendre les résultats de l'exécution et d'approfondir les détails au niveau des conditions pour le débogage ou la validation.

## **Accès aux journaux de flux de travail**

Pour accéder aux journaux de flux de travail :

1. Naviguez jusqu'au **Tableau de bord**.
2. Cliquez sur le **menu Actions** (icône à trois points) à côté du document souhaité.
3. Sélectionnez **Journaux de flux de travail** dans le menu.
   * <mark style="color:red;">**Remarque**</mark>**&#x20;:** La fonctionnalité de workflow doit être activée pour accéder à cette option.
4.  Un **panneau latéral** s'ouvre montrant un résumé des flux de travail exécutés.

    ![Page Export Configuration dans les réglages de DocBits avec les champs Basic Information ainsi que les zones de téléchargement du fichier ION API et du TOML Mapping File](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FAlgg3jnSVRVyuYxy4tAp%252Fimage.png%3Falt%3Dmedia%26token%3D4e8fcd63-6113-47eb-95a4-95a7821dc9b9\&width=768\&dpr=4\&quality=100\&sign=9e6ba9f5\&sv=2)

## **Composants du panneau des journaux de flux de travail**

#### **1. Compteurs de résumé de flux de travail**

Situation en haut du panneau des journaux :

* **Bleu** : Nombre total de flux de travail exécutés.
* **Rouge** : Flux de travail ayant abouti à des **erreurs**.
* **Jaune** : Flux de travail qui n'ont pas été **terminés** en raison de divergences de conditions.
* **Vert** : Flux de travail exécutés avec succès.

#### **2. Tableau d'exécution de flux de travail**

Chaque ligne dans le tableau représente une exécution de flux de travail et inclut :

* **Nom du flux de travail**
* **Horodatage** (Créé le)
* **Durée d'exécution** (en secondes)
* **Icône de résultat**:
  * Coche verte : Le flux de travail a été exécuté avec succès.
  * Croix rouge : Le flux de travail a été exécuté avec une erreur.
  * Tiret orange : L'exécution a été arrêtée en raison d'une condition non satisfaite.

En cliquant sur la **flèche** à gauche de chaque ligne, vous pouvez développer la **vue détaillée du flux de travail**.

<div align="left"><figure><img src="../../.gitbook/assets/workflow_test9_match_check_overview.png" alt="Vue détaillée du Workflow déployant le workflow Purchase Invoice - Approval avec des cartes When, And et Then et des résultats de conditions marqués de coches et de tirets" width="563"><figcaption></figcaption></figure></div>

### **Vue détaillée du flux de travail**

En cliquant sur une ligne de flux de travail spécifique, vous ouvrez son **journal d'exécution détaillé**, montrant :

#### **Évaluation des conditions**

* Bloc **Quand...** : Condition initiale.
* Bloc(s) **Et...** : Conditions supplémentaires.
* Bloc(s) **Alors...** : Actions effectuées lorsque toutes les conditions sont remplies.

Chaque ligne de condition montre :

* Coche **verte** : Condition remplie.
* Tiret **orange** : Condition non remplie.
* Croix **rouge** : La condition a échoué **en raison d'une erreur**

### **Note de comportement importante**

Si une condition dans un flux de travail n'est **pas remplie**, le système **arrête d'évaluer d'autres cartes de flux de travail** dans ce flux de travail. Ce comportement évite un traitement inutile. En tant qu'indicateur visuel, la carte qui **n'a pas rempli sa condition** est affichée en **gris**, et toutes les **cartes suivantes** dans le même flux de travail apparaîtront également en **gris**, indiquant qu'elles n'ont pas été **exécutées**.
