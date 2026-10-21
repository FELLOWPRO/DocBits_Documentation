# Si pays dans le champ

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-70b0b5860da5-fr.png" alt="Champs de la carte dans la version affichée. Les champs ne sont pas encore renseignés." width="563"><figcaption><p>Champs de la carte dans la version affichée. Les champs ne sont pas encore renseignés.</p></figcaption></figure>

## **Objectif :**

Cette carte de workflow est conçue pour évaluer si un pays spécifié, situé dans un champ désigné, fait partie d'une zone commerciale ou politique particulière (Union européenne, espace Schengen ou ALENA). Selon cette évaluation, le workflow peut se poursuivre avec une condition vraie ou fausse, permettant des actions supplémentaires au sein du système. Elle est particulièrement utile pour automatiser des règles métier propres à une région, garantir la conformité ou déclencher des workflows spécifiques en fonction d'appartenances géographiques.

## **Composants de la carte :**

1. **Nom du champ**
   * **Descriptif :** spécifie le champ de document où le nom ou le code du pays est stocké.
   * **Détail :** il doit correspondre à l'identifiant exact du champ des données de pays dans le document.
2. **Opérateur**
   * **Descriptif :** spécifie si le pays du champ sélectionné doit correspondre ou non à la région ou à l'accord sélectionné.
   * **Possibilités :**
     * **Is :** le pays doit faire partie de l'accord sélectionné (UE, Schengen ou ALENA) pour que la condition soit vraie.
     * **N'est-ce pas :** le pays ne doit pas faire partie de l'accord sélectionné pour que la condition soit vraie.
3. **Comparaison des pays**
   * **Descriptif :** définit si le pays du champ est vérifié par rapport à un accord politique ou commercial spécifique.
   * **Possibilités :**
     * **European Union :** la carte vérifie si le pays est membre de l'Union européenne.
     * **Schengen Area :** la carte vérifie si le pays fait partie de l'espace Schengen.
     * **NAFTA :** la carte vérifie si le pays est membre de l'accord ALENA.
4. **Booléen**
   * **Descriptif :** définit le résultat de la comparaison. Si le pays satisfait la condition, le workflow se poursuit avec la valeur booléenne spécifiée.
   * **Possibilités :**
     * **True :** le workflow se poursuit si la condition correspond.
     * **False :** le workflow se poursuit si la condition ne correspond pas.

## **Fonctionnalité :**

* **Évaluation de la condition :**
  * Le système évalue si le pays spécifié dans le champ fait partie de la région ou de l'accord choisi (UE, espace Schengen ou ALENA) en fonction de l'opérateur sélectionné. Cette évaluation vérifie le nom ou le code du pays par rapport à une liste prédéfinie de pays appartenant à chaque groupe.
* **Exécution de l'action :**
  * **Condition vraie :** si le pays du champ correspond à la région sélectionnée (selon l'opérateur), le workflow se poursuit avec la condition vraie spécifiée. Cela peut déclencher des actions supplémentaires, comme l'acheminement de documents, l'application de règles de traitement spéciales ou l'activation de fonctionnalités propres à une région.
  * **Condition fausse :** si le pays ne correspond pas à la région sélectionnée (selon l'opérateur), le workflow se poursuit avec la condition fausse spécifiée, permettant l'exécution d'actions alternatives ou l'arrêt du workflow selon la configuration du système.

## **Mise en place et configuration :**

* Les utilisateurs configurent la carte en sélectionnant le champ de document contenant le pays et en spécifiant la région (Union européenne, espace Schengen ou ALENA). L'opérateur est ensuite choisi dans une liste déroulante pour définir si le pays doit ou non faire partie de la région sélectionnée. Enfin, les utilisateurs définissent la condition de poursuite (vraie ou fausse), qui dicte l'étape suivante du workflow.

## **Conclusion :**

La carte de workflow « Country in Field Comparison » est un outil essentiel pour automatiser les processus qui dépendent de règles géographiques, comme la conformité aux accords commerciaux ou les appartenances politiques. En comparant les données de pays à des régions spécifiques telles que l'Union européenne, l'espace Schengen ou l'ALENA, cette carte garantit que le système applique la bonne logique de traitement, améliorant l'efficacité et garantissant une exécution précise du workflow en fonction des conditions géographiques.

<!-- workflow-card-practical-example-20261021 -->

## Exemple pratique

**Quand utiliser :** Séparez les documents par région.

**Configuration :** Choisissez un champ de pays de document contenant `DE`, sélectionnez la région contenant l'Allemagne et définissez l'option de suite sur `true`.

**Résultat attendu et contre-exemple :** Le code du pays allemand satisfait la région sélectionnée. Un code en dehors de cette région ne le fait pas ; testez l'option de continuation séparément lorsque vous avez besoin de la branche inverse.

Il s’agit d’une configuration illustrative et du résultat attendu. Utilisez les champs, utilisateurs et groupes configurés dans votre organisation de test ; cela ne veut pas dire que cet exemple a été exécuté.
