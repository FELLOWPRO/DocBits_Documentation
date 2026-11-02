# Assistant IA dans l'éditeur de scripts

L'éditeur de scripts dispose d'un **Assistant IA** intégré qui écrit et explique les scripts DocBits pour vous. Vous décrivez en langage courant ce que le script doit faire, et l'assistant répond avec du code Python que vous pouvez copier dans l'éditeur.

{% hint style="info" %}
L'Assistant IA fait partie de **DocNet**. Votre organisation a besoin d'un abonnement DocNet actif pour l'utiliser. Voir [Plan d'abonnement](../../subscription-plan/README.md) et [Module](../../../document-processing/module/README.md).
{% endhint %}

## Ouvrir l'assistant

1. Allez dans **Paramètres → Types de Documents**, ouvrez le type de document et cliquez sur **Scénarios**.
2. Cliquez sur **Nouveau**, ou ouvrez une version de script existante comme brouillon.
3. Cliquez sur l'icône de robot à côté du nom du script. Le panneau **Assistant IA** s'ouvre à droite de l'éditeur.

## Ce que l'assistant connaît

À chaque question, DocBits transmet à l'assistant :

* la **référence de scripting** (les fonctions décrites dans [Scripting dans DocBits](scripting-in-docbits/README.md)),
* le **type de document** du script,
* le **script actuel** de l'éditeur,
* les **noms de champs et colonnes de tableau** que votre organisation utilise pour ce type de document.

Grâce aux noms de champs, l'assistant utilise vos champs réels, par exemple `invoice_date` ou `purchase_order`, dans `get_field_value()` et `set_field_value()`.

## Écrire un script avec l'assistant

1. Saisissez votre demande dans la zone en bas du panneau, par exemple : *Définis la devise sur EUR si elle est vide.*
2. Appuyez sur **Entrée** ou cliquez sur l'icône d'envoi. La réponse s'affiche progressivement.
3. Cliquez sur l'icône de copie (info-bulle **Copie à l'éditeur**) à côté d'un bloc de code pour placer le code dans l'éditeur de scripts.
4. Relisez le code, donnez un nom au script et enregistrez-le comme brouillon.

Les questions de suivi fonctionnent dans le même panneau. Collez un message d'erreur ou demandez *Pourquoi ce script ne définit-il pas la date d'échéance ?* et l'assistant examine le script actuel de l'éditeur.

## Vérifiez toujours le résultat

{% hint style="warning" %}
L'assistant peut se tromper. Relisez le code généré, vérifiez que les noms de champs correspondent à votre type de document et testez le script avec un document de test avant de l'activer. Voir [Tester les scripts](testing-scripts.md).
{% endhint %}

Les scripts ne s'exécutent qu'avec les fonctions de script autorisées. Si un script appelle une fonction qui n'existe pas, DocBits le rejette avec le message *Unknown function*.

## Utilisation et limites

* Chaque réponse affiche sous la réponse le nombre de tokens utilisés (entrée, sortie et total).
* L'utilisation est enregistrée comme utilisation DocNet de votre organisation.
* DocBits rejette la demande lorsque l'abonnement DocNet est absent (*DocNet subscription required*), expiré (*DocNet subscription expired*) ou lorsque le quota est épuisé (*DocNet quota exhausted*).

## Pages associées

* [Créer et modifier des scripts](creating-and-editing-scripts.md)
* [Fonctions de Champ](scripting-in-docbits/field-functions.md)
* [Scripts d'Exemple](scripting-in-docbits/sample-scripts/README.md)
* [Activer et gérer les scripts](script-activation-and-management.md)
