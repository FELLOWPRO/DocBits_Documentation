# Modèle d'IA Spécifique au Fournisseur pour l'Extraction de Champs et de Tableaux

Dans la section des outils de l'**Écran de validation**, vous pouvez choisir le modèle d'IA utilisé pour l'**Extraction de champs** et l'**Extraction de tableaux**.\
Le **modèle d'IA** sélectionné s'applique uniquement à tous les documents du fournisseur actuel.

Pour modifier le modèle, ouvrez le menu d'options en cliquant sur le bouton **Plus d'options** (les trois points) sur le côté droit de l'écran, puis choisissez l'un des modèles disponibles :<br>

* **Full** – Précision maximale ; coûte 2 tokens par document
* **Fast** – Niveau par défaut ; coûte 1 token par document
* **Nexus** – Coûte 1 token par document
* **Nexus Flash** – Niveau plus rapide de la famille Nexus ; coûte 1 token par document
* **Auto** – DocBits décide par document si Fast suffit ou si Full est nécessaire ; coûte 1 token par document
* **Auto Nexus** – Comme Auto, mais limité à la famille de modèles Nexus ; coûte 1 token par document

<figure><img src="../../../.gitbook/assets/dbdc861-supplier-ai-model-menu-fr-20261012.png" alt="Menu d&#x27;options de l&#x27;écran de validation avec le menu déroulant Modèle d&#x27;IA"><figcaption><p>Ouvrez le menu d'options et choisissez le modèle d'IA pour ce fournisseur.</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/dbdc861-supplier-ai-model-options-fr-20261012.png" alt="Menu déroulant Modèle d&#x27;IA ouvert avec Full, Fast, Nexus, Nexus Flash, Auto et Auto Nexus"><figcaption><p>Le menu déroulant Modèle d'IA avec les six options disponibles.</p></figcaption></figure>

Si les résultats de l'**extraction de champs** ou de l'**extraction de tableaux** ne sont pas satisfaisants, essayez de passer à un autre modèle pour améliorer la précision.

Pour configurer le modèle d'IA **globalement pour les fournisseurs sans modèle personnalisé** ou pour **gérer quel modèle est actif pour chaque fournisseur**, veuillez consulter la documentation correspondante [**ici**](../../../administration-and-setup/settings/document-processing/classification-and-extraction/ai-model.md).
