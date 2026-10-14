# Date or Time

<figure><img src="../../../../.gitbook/assets/image (5) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Objectif :**

Cette carte DocBits vérifie si une valeur de date/heure spécifiée se situe dans une plage définie. Elle permet aux workflows de se poursuivre ou de s'arrêter selon que la condition est satisfaite ou non, ce qui la rend adaptée aux opérations sensibles au temps ou à la planification des workflows.

## **Fonctionnalité :**

* **Validation de date/heure :** cette carte évalue si une date/heure donnée se situe dans une plage spécifiée à l'aide des conditions suivantes :
  * **Is :** vérifie si la date/heure se situe dans la plage de début et de fin définie (incluse).
  * **Is Not :** s'assure que la date/heure se situe en dehors de la plage définie.

**Plage de date/heure :** les utilisateurs spécifient les valeurs de date/heure de début et de fin pour définir la plage de comparaison.

## **Utilisation :**

Cette carte est idéale pour la planification, les contrôles de conformité ou la validation de conditions temporelles dans les workflows. Par exemple, elle peut servir à garantir que les tâches ne sont exécutées que pendant des plages horaires prédéfinies ou à vérifier des échéances.

## **Scénario d'exemple :**

* Un utilisateur configure la carte pour vérifier si la **date de soumission** d'une facture **se situe entre** le **« 2024-11-01 »** et le **« 2024-11-30 »**. Si la date de soumission se situe dans cette plage, le workflow se poursuit vers le traitement du paiement. Sinon, le workflow déclenche une notification pour un examen complémentaire.

En utilisant la carte « Date/Time Range Validation », les organisations peuvent garantir une planification précise, renforcer la conformité et rationaliser les workflows en respectant des contraintes temporelles prédéfinies.
