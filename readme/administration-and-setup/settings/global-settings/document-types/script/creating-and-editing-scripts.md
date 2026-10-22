# Créer et modifier des scripts

{% embed url="https://youtu.be/n8NpWWIjmlA" %}
DocBits Explication des scripts de document : automatisez la logique personnalisée dans votre flux de travail de documents
{% endembed %}

## Pour créer un nouveau script dans DocBits, suivez ces instructions détaillées :

**Choisissez le langage de script :**

Choisissez un type de script et un langage réellement proposés par l’éditeur et l’environnement d’exécution de votre installation DocBits. Les types disponibles et les contextes d’exécution dépendent de la version déployée.

**Ouvrez l'environnement de développement de scripts :**

Connectez-vous à DocBits et accédez à l'environnement de développement de scripts. Il se trouve dans la zone d'administration.

<figure><img src="../../../../../.gitbook/assets/s150-bildschirmfoto-2024-05-08-um-09-43-25-fr.png" alt="Liste des scripts avec les noms, les dates et les données de l’organisation masqués."><figcaption><p>Liste des scripts avec les noms, les dates et les données de l’organisation masqués.</p></figcaption></figure>

**Créez un nouveau script :**

Cliquez sur le bouton « + New » pour ouvrir un nouvel éditeur de script.

<figure><img src="../../../../../.gitbook/assets/s150-bildschirmfoto-2024-05-08-um-09-43-37-fr.png" alt="Éditeur d’un nouveau script avec le modèle de départ fourni ; il est distinct de l’exemple Python autonome ci-dessous."><figcaption><p>Éditeur d’un nouveau script avec le modèle de départ fourni ; il est distinct de l’exemple Python autonome ci-dessous.</p></figcaption></figure>

**Écrivez le code :**

Utilisez l'éditeur pour écrire le code de votre script. Commencez par la syntaxe de base du langage de script choisi.

Par exemple, si vous utilisez Python, votre script pourrait ressembler à ceci :

## 1. Exemple de script en Python



## Fonction pour nettoyer les noms de patients

Cet exemple Python autonome illustre la syntaxe. Ce n’est pas un point d’accroche du cycle de vie DocBits dont le fonctionnement a été vérifié ; adaptez-le au contexte de script documenté avant utilisation.

```python
def clean_patient_name(name):
    cleaned_name = name.strip().title()
    return cleaned_name

if __name__ == "__main__":
    patient_name = " john doe "
    cleaned_name = clean_patient_name(patient_name)
    print("Cleaned patient name:", cleaned_name)
```

## 2. Exemple de script



**Testez le script :**

Vérifiez le code à la recherche d'erreurs et testez-le dans un environnement de test. Assurez-vous que le script produit les résultats attendus et fonctionne correctement.



**Enregistrez le script :**

Enregistrez le script dans DocBits et donnez-lui un nom explicite qui décrit son objectif.



**Associez le script aux types de documents :**

Une étape importante consiste à associer le script aux types de documents appropriés. Cela détermine quand et comment le script est appliqué. Cela peut généralement se faire via une interface de configuration dans DocBits, où vous pouvez affecter le script à un type de document précis et indiquer dans quelles conditions il doit être appliqué.



**Vérifiez et publiez :**

Après avoir créé, testé et associé le script, vérifiez-le à nouveau à la recherche d'erreurs et d'incohérences. Si tout est en ordre, vous pouvez publier le script dans l'environnement de production de DocBits.





Grâce à ces étapes, vous pouvez créer, tester et mettre en œuvre avec succès un nouveau script dans DocBits afin d'automatiser les processus et d'améliorer l'efficacité de la documentation médicale.
