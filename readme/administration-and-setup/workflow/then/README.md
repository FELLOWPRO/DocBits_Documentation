# Then

## Aperçu des cartes d'action « Then… »

### **1. Actions sur les champs de document :**

* **Invert Checkbox :** cette action inverse l'état d'un champ de type case à cocher dans un document.
* **Set Checkbox :** définit l'état d'un champ de type case à cocher sur vrai (cochée) ou faux (décochée).
* **Set Field to Text :** cette action définit un champ de document donné sur une valeur texte spécifiée.

<figure><img src="../../../.gitbook/assets/then1.png" alt=""><figcaption></figcaption></figure>

### **2. Actions sur le document :**

* **Approve the Document :** marque un document comme approuvé dans le système.
* **Reject the Document :** marque un document comme rejeté.

<figure><img src="../../../.gitbook/assets/image (259).png" alt=""><figcaption></figcaption></figure>

### **3. Actions d'export :**

* **Export document with export configuration :** lance le processus d'export avec une configuration d'export spécifique.
* **Start Export :** lance le processus d'export.



<figure><img src="../../../.gitbook/assets/image (260).png" alt=""><figcaption></figcaption></figure>

### **4. Actions sur le statut :**



* **Change Status :** change le statut d'un document ou d'une tâche en un nouveau statut spécifié.

<figure><img src="../../../.gitbook/assets/then3.png" alt=""><figcaption></figcaption></figure>

### **5. Actions sur les tâches :**

* Attributions et notifications :
  * **Assign Task :** crée et assigne une tâche avec des détails précis à une personne ou à un groupe, avec la possibilité de les notifier par e-mail.
  * **Create a New Task :** similaire à l'attribution, mais axé sur la création d'une tâche entièrement nouvelle dans le système.

<figure><img src="../../../.gitbook/assets/then4.png" alt=""><figcaption></figcaption></figure>

### **6. Actions sur les tableaux :**

* **Calculate in Table :** effectue des calculs sur les données d'un tableau selon des conditions spécifiées et stocke les résultats dans une colonne désignée.
* **Change Entries :** met à jour les entrées d'un tableau selon des conditions spécifiées.

<figure><img src="../../../.gitbook/assets/then5.png" alt=""><figcaption></figcaption></figure>

### **7. Actions sur l'assigné :**

* **Assign User from Field :** assigne un utilisateur à une tâche ou à un document à partir des données utilisateur stockées dans un champ spécifique, avec une option d'utilisateur de repli si l'utilisateur principal n'est pas disponible.
* **Assign Document to User or Group :** assigne directement un document à un utilisateur ou à un groupe, garantissant que la responsabilité est correctement désignée.

<figure><img src="../../../.gitbook/assets/then6.png" alt=""><figcaption></figcaption></figure>

### **8. Actions d'interaction externe :**

* **Call API :** envoie une requête à une API externe, personnalisable avec des méthodes, des paramètres et des données spécifiques.
* **Send HTTPS Request :** similaire aux appels d'API, mais spécifiquement formaté pour les protocoles HTTPS.

<figure><img src="../../../.gitbook/assets/then7.png" alt=""><figcaption></figcaption></figure>

### **9. Traitement avancé :**

* **Run Workflow :** déclenche un autre workflow au sein du système, permettant un enchaînement complexe de processus.

#### Application pratique

Ces cartes d'action servent à automatiser des réponses en fonction de déclencheurs précis identifiés dans les parties précédentes de la configuration du workflow. Par exemple :

* Si un document est identifié comme nécessitant un examen, l'action « Approve the Document » peut être déclenchée automatiquement une fois qu'il satisfait toutes les conditions spécifiées.
* Pour les tâches de gestion des données, les actions « Set Checkbox » ou « Set Field to Text » garantissent la mise à jour automatique des champs de document, réduisant la saisie manuelle et le risque d'erreurs.
* Les tâches complexes telles que les interactions d'API ou les changements de statut rationalisent les interactions non seulement au sein du système ERP, mais aussi avec des services et outils externes, améliorant l'intégration et la fonctionnalité.

### Conclusion

La section « Then… » de votre système de workflow fournit des outils robustes pour définir des actions précises qui doivent se produire lorsque les conditions du workflow sont remplies. En utilisant efficacement ces actions, les entreprises peuvent automatiser les processus routiniers, garantir l'exactitude des données et réagir de manière dynamique aux évolutions des informations et des états du système. Comprendre comment configurer et exploiter ces actions est essentiel pour maximiser l'efficacité des capacités de workflow de votre système ERP.
