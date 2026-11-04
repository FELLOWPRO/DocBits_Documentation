# Taxe dans le champ du document

<figure><img src="../../../../.gitbook/assets/image (268).png" alt="" width="563"><figcaption></figcaption></figure>

## **Objet :**

Cette carte de flux de travail est conçue pour évaluer si la valeur de la taxe dans un champ de document correspond à la valeur de la taxe dans un bon de commande, en tenant compte des tolérances basées sur l'ID de frais. La carte compare ces deux valeurs de taxe (une du champ de document et une du bon de commande) et vérifie si elles remplissent une condition spécifiée (par exemple, égale, supérieure à, inférieure à, etc.). Cela permet de s'assurer que les valeurs de taxe sont cohérentes et de signaler les divergences pour un examen ou une approbation plus approfondis dans les flux de travail d'achat.

## **Composants de la carte :**

1. **Nom du champ**
   * **Description :** Spécifie le champ du document qui contient la valeur de la taxe à comparer avec la valeur de la taxe dans le bon de commande.
   * **Détail :** Ce champ doit correspondre à l'identifiant exact de la valeur de la taxe dans le document.
2. **Opérateur**
   * **Description :** Définit la condition à appliquer à la comparaison entre la valeur de la taxe du document et la valeur de la taxe du bon de commande.
   * **Options :**
     * **Égal (=) :** Vérifie si la taxe dans le champ du document correspond à la taxe dans le bon de commande.
     * **Non égal (≠) :** Garantit que la taxe dans le champ du document ne correspond pas à la taxe dans le bon de commande.
     * **Supérieur à (>) :** Vérifie si la taxe dans le champ du document est supérieure à la taxe dans le bon de commande.
     * **Supérieur ou égal (≥) :** Vérifie si la taxe dans le champ du document est supérieure ou égale à la taxe dans le bon de commande.
     * **Inférieur à (<) :** Vérifie si la taxe dans le champ du document est inférieure à la taxe dans le bon de commande.
     * **Inférieur ou égal (≤) :** Vérifie si la taxe dans le champ du document est inférieure ou égale à la taxe dans le bon de commande.
3. **Table de recherche des données de référence**
   * **Description :** La table qui contient les détails du bon de commande, y compris l'ID de frais et les valeurs de taxe.
   * **Détail :** Cette table doit avoir une référence à l'ID de frais associé à la valeur de la taxe du bon de commande.
4. **Montant de la tolérance**
   * **Description :** Le montant seuil à l'intérieur duquel les valeurs de taxe peuvent varier. Ceci est utilisé pour tenir compte des écarts mineurs dans les calculs de taxe.
   * **Détail :** Le montant de la tolérance doit être une valeur numérique, définissant la différence maximale autorisée entre les valeurs de taxe.
5. **Type de tolérance**
   * **Description :** Spécifie le type de tolérance appliqué, soit une valeur absolue, soit un pourcentage.
   * **Options :**
     * **Valeur :** La tolérance est une valeur numérique fixe.
     * **Pourcentage :** La tolérance est calculée comme un pourcentage de la valeur de la taxe.

## **Fonctionnalité :**

* **Évaluation de la condition :** Le système évalue si la valeur de la taxe dans le champ du document remplit la condition spécifiée lorsqu'elle est comparée à la valeur de la taxe dans le bon de commande (avec la référence de l'ID de frais de la table des données de référence). Le montant et le type de tolérance sont pris en compte dans cette évaluation pour permettre des différences mineures dans les calculs de taxe.
* **Exécution de l'action :**
  * **Condition vraie :** Si la taxe dans le champ du document remplit la condition par rapport à la taxe du bon de commande (dans la limite du montant et du type de tolérance), le flux de travail se poursuit.
  * **Condition fausse :** Si la taxe dans le champ du document ne remplit pas la condition (soit elle n'est pas dans la plage de tolérance, soit la comparaison échoue), le flux de travail s'arrêtera.

## **Configuration et paramétrage :**

* Les utilisateurs doivent sélectionner le champ du document qui contient la valeur de la taxe à comparer. Ils choisiront ensuite l'opérateur de comparaison (par exemple, égal, supérieur à). Ensuite, les utilisateurs doivent spécifier la référence à la table des données de référence et définir le montant et le type de tolérance pour tenir compte des écarts de taxe mineurs.

## **Exemple de scénario :**

* Une facture indique un montant de taxe de 100 $. Le bon de commande correspondant, trouvé dans la table des données de référence, spécifie une valeur de taxe de 95 $. En utilisant l'opérateur "Supérieur à", le système compare la valeur de taxe du document (100 $) à la valeur de taxe du bon de commande (95 $) avec une tolérance de 10 $ (type de tolérance valeur absolue). Comme la différence de 5 $ se situe dans la plage de tolérance, le flux de travail se poursuit sans déclencher d'alertes.

## **Conclusion :**

La carte de flux de travail "Comparaison de la taxe dans le champ du document" garantit que les valeurs de taxe dans les documents correspondent aux détails du bon de commande, tout en permettant des écarts mineurs basés sur des tolérances spécifiées. En automatisant ce contrôle, les organisations peuvent minimiser les erreurs dans les calculs de taxe et simplifier les processus d'achat, réduisant ainsi le besoin d'intervention manuelle ou d'approbations.
