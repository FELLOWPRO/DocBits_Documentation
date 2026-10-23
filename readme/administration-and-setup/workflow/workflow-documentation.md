# Attribution et statut — Exemples pratiques

Pour garder une vue d'ensemble, vous pouvez donner aux flux de travail différents intitulés afin de savoir immédiatement de quelle tâche ce flux de travail traite.

Créer un nouveau flux de travail : Cliquez sur + ADD WORKFLOW

![Canevas Workflow Builder avec le modèle Test Simple Workflow, trois lignes Wenn, Und et Dann et un bouton Karte hinzufügen sous chacune](<../../.gitbook/assets/workflow_add_button.png>)

Vous pouvez utiliser ces flux de travail (Test 1, 2, 3) pour assigner automatiquement divers documents au bon employé de l'entreprise.

![Tableau de bord Workflow List avec la ligne Test Simple Workflow et les colonnes Name, Type, Workflow Execution Order, Updated By, Created On et Last Mod](<../../.gitbook/assets/workflow_list_overview.png>)

Si une facture ou un autre document dépasse un certain montant total qui nécessite un examen et une approbation préalables, ces documents peuvent être immédiatement assignés à la bonne personne.

<figure><img src="../../.gitbook/assets/workflow_amount_check.png" alt="Vérification du montant du flux de travail"><figcaption></figcaption></figure>

**Test 1 : Logic Card**

When : **Assignee is:** Responsable de réception

And : **Document type is:** Invoice

Then : **Assign document to:** Réviseur des factures

![](<../../.gitbook/assets/3 (1).png>)

**Test 2 : Logic Card**

When : **Assignee is:** Responsable de réception

Et : **Le type de document est :** Bon de livraison

Then : **Assign document to:** Réviseur des livraisons

![](<../../.gitbook/assets/4 (1).png>)

**Test 3 : Logic Card**

**When :** **Assignee is:** Responsable de réception

**And :** **Document type is:** Order Confirmation

**Then :** **Assign document to:** Réviseur des commandes

![](<../../.gitbook/assets/5 (1).png>)

Il est également possible, si le document n'est pas assigné à une seule personne, de l'assigner dès le départ à un employé spécifique.

<figure><img src="../../.gitbook/assets/workflow_assign_to_employee_start.png" alt="Assigner le flux de travail à un employé dès le départ" width="375"><figcaption></figcaption></figure>

Pour avoir une vue d'ensemble plus facile de ce qui doit arriver à un document, vous pouvez définir le statut des documents entrants dans ce flux de travail. Ce flux de travail permet de voir immédiatement s'il y a, par exemple, une approbation en attente.

**Test 4 : Logic Card**

**Quand :Le type de document est :** Bon de livraison

**And :** **Assignee is:** Responsable de réception

**Puis :Changer le statut en :** En attente d'approbation

<figure><img src="../../.gitbook/assets/s150-workflow_test4_delivery_note_status-fr.png" alt="Brouillon non enregistré d’un workflow de changement de statut."><figcaption><p>Brouillon non enregistré d’un workflow de changement de statut.</p></figcaption></figure>

![](<../../.gitbook/assets/8 (1).png>)

**Test 5 : Logic Card**

When : **Document type is:** Invoice

And : **Assignee is:** Réviseur des factures

Ensuite : **Changer le statut en :** En attente de la deuxième approbation

<figure><img src="../../.gitbook/assets/workflow_test5_invoice_approval_status.png" alt="Statut d'approbation de la facture du test 5 du flux de travail"><figcaption></figcaption></figure>

![](<../../.gitbook/assets/10 (1).png>)

Si une facture ou un autre document dépasse un certain montant total qui nécessite un examen et une approbation préalables, ces documents peuvent être immédiatement assignés à la bonne personne.

![](<../../.gitbook/assets/11 (1).png>)

**Test 6 : Logic Card**

When : **Assignee is:** Responsable de réception

Et : Docfield **total\_amount** est **Supérieur à 500**

Then : **Assign document to:** Responsable des approbations

<figure><img src="../../.gitbook/assets/workflow_test6_total_amount_assign.png" alt="Assignation par montant total du test 6 du flux de travail"><figcaption></figcaption></figure>

![](<../../.gitbook/assets/13 (1).png>)

Il est également possible de saisir le statut dans le flux de travail, afin que la personne assignée puisse voir immédiatement quel est le statut de ce document et ce qui doit lui arriver ensuite.

**Test 7 : Logic Card**

**When :** **Assignee is:** Responsable de réception

**Et :** Docfield **total\_amount** est **Supérieur à 500**

**Then :** **Assign document to:** Responsable des approbations

**Changer le statut en :** En attente d'approbation

<figure><img src="../../.gitbook/assets/s150-workflow_test7_status_update-fr.png" alt="Action de changement de statut dans un brouillon de workflow."><figcaption><p>Action de changement de statut dans un brouillon de workflow.</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/15 (1).png" alt="Concepteur de workflows avec trois cartes logiques attribuant des documents par responsable et type de document au Invoice reviewer, Delivery-note reviewer et Order reviewer"><figcaption></figcaption></figure>

Par exemple, si certaines informations ou des informations importantes manquent dans un document, mais qu'elles sont importantes et doivent être incluses pour un traitement ultérieur, vous pouvez configurer le flux de travail de sorte que ces documents soient immédiatement transmis à l'acheteur et à un remplaçant (substitut).

<figure><img src="../../.gitbook/assets/workflow_test8_missing_info.png" alt="Informations manquantes du test 8 du flux de travail"><figcaption></figcaption></figure>

**Test 9 :**

Le flux de travail avec ces logic cards est conçu pour vérifier automatiquement que la quantité, le prix unitaire ou la remise détaillés dans une confirmation de commande correspondent aux chiffres correspondants de la commande d'achat. Cette vérification garantit la cohérence et l'exactitude entre ce qui a été commandé et ce que le fournisseur confirme livrer.

Vous pouvez donner à ces documents un statut spécifique ou les assigner à un employé spécifique.

<div align="center"><figure><img src="../../.gitbook/assets/s150-workflow_test9_match_check_overview-fr.png" alt="Brouillon de workflow avec une condition de comparaison de commande."><figcaption><p>Brouillon de workflow avec une condition de comparaison de commande.</p></figcaption></figure></div>

<figure><img src="../../.gitbook/assets/s150-workflow_test9_match_check_detail-fr.png" alt="Sélection des conditions de comparaison avec une commande."><figcaption><p>Sélection des conditions de comparaison avec une commande.</p></figcaption></figure>

**Carte Logique : Quantité ou Prix Unitaire ou Correspondance de Remise**

Cette logic card est conçue pour vérifier automatiquement que la quantité, le prix unitaire ou la remise détaillés dans une confirmation de commande correspondent aux chiffres correspondants de la commande d'achat. Cette vérification garantit la cohérence et l'exactitude entre ce qui a été commandé et ce que le fournisseur confirme livrer.

**Condition de déclenchement**

La logique est activée lorsque l'une des conditions suivantes est remplie dans une confirmation de commande par rapport à la commande d'achat d'origine :

* **Tolérance de quantité** : La quantité d'articles commandés correspond à la quantité confirmée par le fournisseur.
* **Tolérance de prix unitaire** : Le prix par article convenu correspond à la confirmation du fournisseur.
* **Rabais** : Toutes les remises appliquées sont cohérentes entre la commande d'achat et la confirmation de commande.
* **Définir les paramètres de comparaison** : Configurez les champs spécifiques (quantité, prix unitaire, remise) que la logic card vérifiera pour une correspondance.
* **Automatiser la vérification** : Configurez le système pour comparer automatiquement ces détails à la réception d'une confirmation de commande.
* **Personnaliser les alertes** : Décidez du flux de travail pour la gestion des divergences, y compris la personnalisation des alertes pour révision manuelle.

Cette logic card est essentielle pour garantir que les détails d'une confirmation de commande correspondent à la commande d'achat d'origine, préservant l'intégrité du cycle d'approvisionnement.

**Test 10 :**

Si vous avez un calcul différent pour les surcharges, ou si vous ne les avez que sur certains articles, vous pouvez utiliser les cartes génériques de calcul de tableau ; certaines d'entre elles permettent également de filtrer par expressions régulières.

<figure><img src="../../.gitbook/assets/19 (1).png" alt="Carte de calcul pour la colonne MTZ avec une règle Material Surcharge et un filtre regex Item Number pour les numéros d'article commençant par 01, 06, 9, 001 ou 000"><figcaption></figcaption></figure>

Ci-dessus se trouve un exemple de calcul pour MTZ avec un filtre pour les numéros d'article commençant par 01, 06, 9, 001 ou 000.

Avec une configuration manuelle, il est conseillé de séparer les calculs qui dépendent de nouvelles colonnes dans un flux de travail distinct. Pour poursuivre le calcul, vous pouvez utiliser la carte Run Workflow.

**Exécuter le flux**

<figure><img src="../../.gitbook/assets/20 (1).png" alt="Carte Run workflow Mtz Into Discount du générateur de workflows avec une section Conditions pour exécuter un workflow de suivi"><figcaption></figcaption></figure>

Avec cette carte, vous pouvez spécifier le nom d'un flux de travail à exécuter après le flux de travail actuel si ses conditions sont remplies, et après les cartes then précédentes du flux de travail actuel. Bien qu'elle priorise les flux de travail exécutables et actifs, elle vous permet également d'exécuter des flux de travail désactivés si le document remplit les conditions du flux de travail.

### **Ajouter des surcharges calculées dans une colonne existante** <a href="#pekg4i18rshn" id="pekg4i18rshn"></a>



Si vous souhaitez ajouter toutes les surcharges comme une remise négative dans la colonne de remise, vous pouvez utiliser la carte de calcul. Il peut y avoir des entrées dans cette colonne ; vous pouvez la définir comme l'une des variables de la carte, y soustraire le MTZ et ajouter le résultat à nouveau dans cette colonne. Au cas où il y aurait des champs vides (surcharges uniquement pour certains articles), il supposera une valeur de 0 pour son calcul.

**Notifier un utilisateur pour qu'il autorise la confirmation de commande dans DocBits**

Après avoir calculé les surcharges, vous pouvez vouloir notifier un utilisateur spécifique pour qu'il autorise la confirmation de commande. Pour cela, vous pouvez utiliser la carte de notification.

<figure><img src="../../.gitbook/assets/workflow_notification_card_overview.png" alt="Carte de notification du flux de travail"><figcaption></figcaption></figure>

Selon les paramètres, l'utilisateur se voit assigner une nouvelle tâche dans DocBits et, en option, un e-mail pour l'informer de sa nouvelle tâche.

Les images actualisées montrent des brouillons non enregistrés de conditions et d’actions. Adaptez les rôles et conditions à votre organisation.
