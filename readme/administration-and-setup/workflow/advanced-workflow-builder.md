# Advanced Workflow

Le constructeur **Advanced Workflow** est un éditeur de graphe de nœuds pour les workflows nécessitant des branches, des chemins parallèles et un contrôle de flux — au-delà du modèle linéaire When/And/Then du constructeur Standard. Vous disposez des nœuds sur un canevas et les reliez pour définir le flux d'exécution.

## Vidéo : routage des factures dans DocBits

La vidéo présente un workflow configuré dans la véritable interface DocBits : contrôle du montant, deux actions, connexions et préparation des cas de test.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas/v2/fr.mp4" %}

[Sous-titres (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas/v2/fr.vtt)

Les captures montrent un brouillon de démonstration non enregistré. `total_amount` et `approval_route` sont des exemples de clés de champ. `Approval` et `Standard` identifient les chemins. Configurez les actions métier nécessaires à votre processus.

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

## Comment y accéder

Ouvrez le concepteur Advanced Workflow depuis la zone des workflows (le canevas du constructeur avancé). Vous partez d'un nœud **Start** et construisez le flux en ajoutant des nœuds.

<figure><img src="../../.gitbook/assets/workflow_advanced_canvas.png" alt="Canevas en graphe de nœuds de l'Advanced Workflow avec barre d'outils"><figcaption><p>Le canevas de l'Advanced Workflow — un graphe de nœuds avec des commandes de zoom, d'exécution, de grille et d'enregistrement. Donnez un nom au workflow dans la barre d'outils.</p></figcaption></figure>

## Ajouter des nœuds

Cliquez sur **+ Add** pour ouvrir le menu des nœuds. En plus des cartes habituelles **When**, **And** et **Then**, le constructeur avancé ajoute des nœuds de contrôle de flux :

<figure><img src="../../.gitbook/assets/workflow_advanced_add_menu.png" alt="Menu Add de l'Advanced Workflow avec les types de nœuds"><figcaption><p>Le menu de nœuds <strong>+ Add</strong> : When / And / Then ainsi que Wait ALL, Wait ANY, OR et Note.</p></figcaption></figure>

- **When / And / Then** — les mêmes cartes de condition et d'action que dans le constructeur Standard.
- **Wait ALL** — attend que *toutes* les branches entrantes soient terminées avant de continuer.
- **Wait ANY** — continue dès qu'une *quelconque* branche entrante est terminée.
- **OR** — fait bifurquer le flux vers des chemins alternatifs.
- **Note** — une annotation en texte libre sur le canevas (n'affecte pas l'exécution).

Exécutez le flux avec la commande de lecture, validez-le, puis enregistrez avec le bouton d'enregistrement de la barre d'outils.

## Étapes suivantes

- Découvrez ce que fait chaque carte dans la section **Cards**.
- Pour des automatisations linéaires simples, le constructeur **Standard Workflow** est plus rapide à configurer.
