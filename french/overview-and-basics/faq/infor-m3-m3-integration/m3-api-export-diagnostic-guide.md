# Guide de diagnostic d'exportation de l'API M3

### 1. Configuration initiale

Avant de commencer le dépannage, assurez-vous de bien connaître les entrées attendues pour le point de terminaison M3 avec lequel vous travaillez.

#### 1.1 Accéder à la documentation de l'API M3

* Connectez-vous à **M3**.
* Accédez à la **Section API → Documentation de l'API**.
* Localisez et sélectionnez le point de terminaison pertinent (par exemple, `APS450MI` pour les exportations liées aux factures).
* Choisissez la fonction appropriée (par exemple, `Add`).

#### 1.2 Comprendre les exigences de l'API

* Passez en revue tous les **champs requis** dans la documentation de l'API.
* Faites attention aux champs importants tels que :
  * `DIVI`
  * `ACDT` (date comptable)
  * `CUCD` (code de devise)
  * `SINO` (numéro de facture fournisseur)
* Confirmez les **types de données** des champs, la **casse** et les **règles de formatage** (par exemple, `AAAA-MM-JJ` pour les dates).

### 2. Tester les appels API directement dans M3

Cette étape vérifie que l'API M3 se comporte comme prévu en utilisant des entrées manuelles.

#### 2.1 Générer une demande de test dans M3

* Dans l'outil de documentation de l'API M3 :
  * Remplissez les données de test pour les champs requis.
  * Cliquez sur **Exécuter** pour exécuter la demande.
  * Copiez le **cURL** et le **corps JSON** résultants.

#### 2.2 Déboguer en utilisant Postman

* Ouvrez **Postman** et créez une nouvelle demande **POST**.
* Collez le corps JSON ou le cURL.
* Ajoutez les en-têtes nécessaires (par exemple, autorisation).
* Cliquez sur **Envoyer** et observez le résultat :
  * `200 OK` : La demande a réussi.
  * Erreur : Vérifiez le message pour plus de détails sur ce qui s'est mal passé.

### 3. Comparer l'API M3 avec le mappage DocBits

Une fois que vous avez confirmé que l'API fonctionne avec des données de test, comparez-la à ce que DocBits envoie réellement.

#### 3.1 Exporter des données d'exemple depuis DocBits

*   Ouvrez la **documentation de l'API DocBits** :

    Utilisez le point de terminaison **/export/get\_infor\_export\_api\_json**.
* Entrez l'**ID du document** d'un document problématique.
* Exécutez l'exportation pour visualiser la **charge JSON** que DocBits enverra à M3.

#### 3.2 Comparer les charges utiles de l'API

* Placez le **JSON de test M3** et le **JSON d'exportation DocBits** côte à côte.
* Vérifiez :
  * **Noms de champs** : Assurez-vous que les noms correspondent _exactement_, y compris la casse (`DIVI` ≠ `divi`).
  * **Types de données** : Vérifiez que les chaînes, les nombres et les dates sont correctement formatés.
  * **Champs manquants** : Identifiez les champs présents dans la demande de M3 mais absents dans DocBits.

### 4. Dépannage des problèmes courants

| Problème                                   | Cause probable                               | Solution                                                                       |
| ------------------------------------------ | -------------------------------------------- | ------------------------------------------------------------------------------ |
| Erreur de champ manquant                   | Un champ requis n'est pas mappé dans DocBits | Ajoutez le champ manquant dans la configuration d'exportation de DocBits.      |
| Incompatibilité de casse de champ (`DIVI`) | M3 est sensible à la casse                   | Utilisez la casse correcte dans le mappage des champs.                         |
| Format de `accountingDate` invalide        | Date incorrecte ou manquante                 | Ajustez au format attendu par M3 (par exemple, `AAAA-MM-JJ`).                  |
| Erreur API inattendue                      | Champs supplémentaires ou non reconnus       | Comparez avec des charges de travail connues et nettoyez les données inutiles. |

### 5. Si les problèmes persistent

Si le problème n'est pas résolu après avoir suivi les étapes ci-dessus :

1. **Documentez** le problème :
   * Message d'erreur et code d'état
   * Demande M3 d'exemple et JSON d'exportation de DocBits
2. **Résumez** votre dépannage :
   * Ce que vous avez essayé
   * Différences clés observées entre les charges de test et les échecs
3. **Escaladez** vers un développeur :
   * Incluez toutes les données et conclusions
   * Mettez en évidence les zones de problème suspectées
