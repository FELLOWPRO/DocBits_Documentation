# Modèle d'IA

## Aperçu

Le paramètre **Modèle d'IA** vous permet de définir quel modèle d'IA est utilisé par défaut pour l'**extraction des champs** et l'**extraction de tableau** lors du traitement des documents.\
Dans cette section, vous pouvez consulter le coût en tokens pour chaque modèle et voir quel modèle est actuellement assigné à chaque fournisseur.

## Comment accéder

1.  Naviguez vers **Paramètres** → **Traitement des documents** → **Classification et extraction**

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_classification_and_extraction.png)
2.  Faites défiler vers le bas jusqu'à la section **Extraction de tableau**

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ai_model_1.png)

## Options du Modèle d'IA

DocBits propose trois options de modèle d'IA pour l'extraction de champs et de tableaux. Elles diffèrent par l'équilibre entre **précision d'extraction**, **vitesse de traitement** et **coût en tokens par document** — vous pouvez ainsi adapter l'option au type de documents que vous traitez. Survolez l'icône d'information à côté du paramètre pour voir le coût en tokens de l'option actuellement sélectionnée.

* **Full** – L'option la plus complète, avec la plus haute précision d'extraction. Idéale pour les mises en page complexes, les scans de mauvaise qualité ou les documents où la précision prime. En tant qu'option la plus puissante, elle est aussi la plus lente, à **2 tokens par document**.
* **Fast** – Une option équilibrée qui combine une bonne précision à un traitement plus rapide et à moindre coût. C'est l'option par défaut recommandée pour la plupart des documents courants, à **1 token par document**.
* **Turbo** – L'option la plus rapide et la plus économique. La mieux adaptée aux gros volumes de documents simples, propres et bien structurés, où la vitesse et le faible coût importent plus que la précision maximale, à **1 token par document**.

| Option | Idéale pour | Précision | Vitesse | Coût en tokens |
|--------|-------------|-----------|---------|----------------|
| **Full** | Mises en page complexes, scans médiocres, haute précision | La plus élevée | La plus lente | 2 / document |
| **Fast** | Documents courants (option par défaut recommandée) | Élevée | Rapide | 1 / document |
| **Turbo** | Gros volumes de documents simples et propres | Bonne | La plus rapide | 1 / document |

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ai_model_2.png)

## Tableau d'Attribution du Modèle d'IA

Vous pouvez également configurer des **modèles d'IA** spécifiques au fournisseur directement dans l'écran de **Validation**, ce qui vous permet d'affiner la précision de l'extraction pour des fournisseurs individuels.\
\
Pour plus d'informations, veuillez consulter la documentation correspondante [ici](../../../../end-user-and-partner-section/end-user-section/validation-screen/supplier-specific-ai-model-for-field-and-table-extraction.md).

Le tableau d'attribution affiche les paramètres du modèle d'IA pour chaque fournisseur et comprend les détails suivants :

* **Supplier ID** – L'identifiant unique du fournisseur
* **AI Model** – Le modèle d'IA actuellement assigné au fournisseur
* **E-Text** : Indique si la fonctionnalité E-Text est activée
* **Action** – Contient l'option de supprimer l'entrée

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ai_model_3.png)

### Supprimer l'entrée – Réinitialiser les paramètres spécifiques au fournisseur

Pour réinitialiser le paramètre du modèle d'IA d'un fournisseur à la valeur par défaut :

1.  Cliquez sur l'icône de la corbeille dans la colonne **Action** à côté de l'entrée du fournisseur.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ai_model_4.png)
2.  Une boîte de dialogue de confirmation apparaîtra—confirmez que vous souhaitez supprimer l'entrée.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ai_model_5.png)

Une fois supprimé, le fournisseur reviendra à l'utilisation du **modèle d'IA** par défaut pour l'**extraction des champs** et l'**extraction de tableau**.
