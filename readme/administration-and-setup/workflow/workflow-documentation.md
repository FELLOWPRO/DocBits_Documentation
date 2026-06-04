# Documentation des flux de travail

**Documentation des flux de travail**

Pour garder une vue d'ensemble, vous pouvez donner aux flux de travail différents intitulés afin de savoir immédiatement de quelle tâche ce flux de travail traite.

Créer un nouveau flux de travail : Cliquez sur + ADD WORKFLOW

![](<../../../.gitbook/assets/0 (1).png>)

Vous pouvez utiliser ces flux de travail (Test 1, 2, 3) pour assigner automatiquement divers documents au bon employé de l'entreprise.

![](<../../../.gitbook/assets/1 (1).png>)

Si une facture ou un autre document dépasse un certain montant total qui nécessite un examen et une approbation préalables, ces documents peuvent être immédiatement assignés à la bonne personne.

<figure><img src="../../../.gitbook/assets/docbits_error_approval.png" alt="DocBits Erreur Approbation"><figcaption></figcaption></figure>

**Test 1 :              Logic Card**

When :             **Assignee is:**                    Amier Haider

And :                **Document type is:**        Invoice

Then :              **Assign document to:**   Stefan Reppermund

![](<../../../.gitbook/assets/3 (1).png>)

**Test 2 :              Logic Card**

When :              **Assignee is:**                    Amier Haider

And :                 **Document type is:**        Delivery Note

Then :               **Assign document to:**   James Edwards

![](<../../../.gitbook/assets/4 (1).png>)

**Test 3 :             Logic Card**

**When :**             **Assignee is:**                    Amier Haider

**And :**                **Document type is:**        Order Confirmation

**Then :**              **Assign document to:**   Anian Sollinger

![](<../../../.gitbook/assets/5 (1).png>)





Il est également possible, si le document n'est pas assigné à une seule personne, de l'assigner dès le départ à un employé spécifique.

<figure><img src="../../../.gitbook/assets/docbits_workflow_purchase_order_6.png" alt="DocBits Workflow Achat Commande 6" width="375"><figcaption></figcaption></figure>





Pour avoir une vue d'ensemble plus facile de ce qui doit arriver à un document, vous pouvez définir le statut des documents entrants dans ce flux de travail. Ce flux de travail permet de voir immédiatement s'il y a, par exemple, une approbation en attente.



**Test 4 :             Logic Card**

**When :**             **Document type is:**         Delivery Note

**And :**                **Assignee is:**                     Amier Haider

**Then :**              **Change Status to:**         Pending Approval

<figure><img src="../../../.gitbook/assets/docbits_workflow_purchase_order_7.png" alt="DocBits Workflow Achat Commande 7"><figcaption></figcaption></figure>

![](<../../../.gitbook/assets/8 (1).png>)



**Test 5 :                Logic Card**

When :                **Document type is:**           Invoice

And :                   **Assignee is:**                       Stefan Reppermund

Then :                 **Change Status to:**           Pending Second Approval

<figure><img src="../../../.gitbook/assets/docbits_approval_supplier.png" alt="DocBits Approbation Fournisseur"><figcaption></figcaption></figure>

![](<../../../.gitbook/assets/10 (1).png>)





Si une facture ou un autre document dépasse un certain montant total qui nécessite un examen et une approbation préalables, ces documents peuvent être immédiatement assignés à la bonne personne.

![](<../../../.gitbook/assets/11 (1).png>)



**Test 6 :                    Logic Card**

When :                   **Assignee is:**                   Amier Haider

And :                      Docfield        **total\_amount**     is      **Greater than       500**

Then :                    **Assign document to:**   Asad Usman Khan

<figure><img src="../../../.gitbook/assets/docbits_purchase_order_table.png" alt="DocBits Achat Commande Tableau"><figcaption></figcaption></figure>

![](<../../../.gitbook/assets/13 (1).png>)



Il est également possible de saisir le statut dans le flux de travail, afin que la personne assignée puisse voir immédiatement quel est le statut de ce document et ce qui doit lui arriver ensuite.



**Test 7 :                 Logic Card**

**When :** **Assignee is:**                     Amier Haider

**And :**                   Docfield           **total\_amount**      is        **Greater then      500**

**Then :**                 **Assign document to:**     Asad Usman Khan

&#x20;                            **Change Status to:**          Pending Approval

<figure><img src="../../../.gitbook/assets/docbits_approval.png" alt="DocBits Approbation"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/docbits_workflow_purchase_order_2.png" alt="DocBits Workflow Achat Commande 2"><figcaption></figcaption></figure>





Par exemple, si certaines informations ou des informations importantes manquent dans un document, mais qu'elles sont importantes et doivent être incluses pour un traitement ultérieur, vous pouvez configurer le flux de travail de sorte que ces documents soient immédiatement transmis à l'acheteur et à un remplaçant (substitut).

<figure><img src="../../../.gitbook/assets/docbits_settings_workflow_2.png" alt="DocBits Paramètres Workflow 2"><figcaption></figcaption></figure>



**Test 9 :**

Le flux de travail avec ces logic cards est conçu pour vérifier automatiquement que la quantité, le prix unitaire ou la remise détaillés dans une confirmation de commande correspondent aux chiffres correspondants de la commande d'achat. Cette vérification garantit la cohérence et l'exactitude entre ce qui a été commandé et ce que le fournisseur confirme livrer.

Vous pouvez donner à ces documents un statut spécifique ou les assigner à un employé spécifique.

<div align="center">

<figure><img src="../../../.gitbook/assets/docbits_approval_2.png" alt="DocBits Approbation 2"><figcaption></figcaption></figure>

</div>

<figure><img src="../../../.gitbook/assets/docbits_error_email.png" alt="DocBits Erreur E-mail"><figcaption></figcaption></figure>

**Logic Card : Quantity or Unit Price or Discount Match**

Cette logic card est conçue pour vérifier automatiquement que la quantité, le prix unitaire ou la remise détaillés dans une confirmation de commande correspondent aux chiffres correspondants de la commande d'achat. Cette vérification garantit la cohérence et l'exactitude entre ce qui a été commandé et ce que le fournisseur confirme livrer.



**Condition de déclenchement**

La logique est activée lorsque l'une des conditions suivantes est remplie dans une confirmation de commande par rapport à la commande d'achat d'origine :

* **Quantity** : La quantité d'articles commandés correspond à la quantité confirmée par le fournisseur.
* **Unit Price** : Le prix par article convenu correspond à la confirmation du fournisseur.
* **Discount** : Toutes les remises appliquées sont cohérentes entre la commande d'achat et la confirmation de commande.



* **Définir les paramètres de comparaison** : Configurez les champs spécifiques (quantité, prix unitaire, remise) que la logic card vérifiera pour une correspondance.
* **Automatiser la vérification** : Configurez le système pour comparer automatiquement ces détails à la réception d'une confirmation de commande.
* **Personnaliser les alertes** : Décidez du flux de travail pour la gestion des divergences, y compris la personnalisation des alertes pour révision manuelle.

Cette logic card est essentielle pour garantir que les détails d'une confirmation de commande correspondent à la commande d'achat d'origine, préservant l'intégrité du cycle d'approvisionnement.



**Test 10 :**

Si vous avez un calcul différent pour les surcharges, ou si vous ne les avez que sur certains articles, vous pouvez utiliser les cartes génériques de calcul de tableau ; certaines d'entre elles permettent également de filtrer par expressions régulières.

<figure><img src="../../../.gitbook/assets/docbits_table_invoice.png" alt="DocBits Tableau Facture"><figcaption></figcaption></figure>

Ci-dessus se trouve un exemple de calcul pour MTZ avec un filtre pour les numéros d'article commençant par 01, 06, 9, 001 ou 000.



Avec une configuration manuelle, il est conseillé de séparer les calculs qui dépendent de nouvelles colonnes dans un flux de travail distinct. Pour poursuivre le calcul, vous pouvez utiliser la carte Run Workflow.

**Run Workflow**

<figure><img src="../../../.gitbook/assets/docbits_workflow_2.png" alt="DocBits Workflow 2"><figcaption></figcaption></figure>

Avec cette carte, vous pouvez spécifier le nom d'un flux de travail à exécuter après le flux de travail actuel si ses conditions sont remplies, et après les cartes then précédentes du flux de travail actuel. Bien qu'elle priorise les flux de travail exécutables et actifs, elle vous permet également d'exécuter des flux de travail désactivés si le document remplit les conditions du flux de travail.

### **Ajouter des surcharges calculées dans une colonne existante** <a href="#pekg4i18rshn" id="pekg4i18rshn"></a>

<figure><img src="https://lh7-us.googleusercontent.com/XYY1xsFpp7_-Bi0WOSbotiVzspDLdaufx_xgoopMHmxdZnSDhroLpb0AE_si5PhwMq1jHfndc9FwOte9MOoCoTP5_JUYawO5cr4uIctIDHmwVjz3KacQrLJd8iBQy5KY4N-dMaWEi3IeTcc5OBRNJk4" alt=""><figcaption></figcaption></figure>

Si vous souhaitez ajouter toutes les surcharges comme une remise négative dans la colonne de remise, vous pouvez utiliser la carte de calcul. Il peut y avoir des entrées dans cette colonne ; vous pouvez la définir comme l'une des variables de la carte, y soustraire le MTZ et ajouter le résultat à nouveau dans cette colonne. Au cas où il y aurait des champs vides (surcharges uniquement pour certains articles), il supposera une valeur de 0 pour son calcul.

**Notifier un utilisateur pour qu'il autorise la confirmation de commande dans DocBits**

Après avoir calculé les surcharges, vous pouvez vouloir notifier un utilisateur spécifique pour qu'il autorise la confirmation de commande. Pour cela, vous pouvez utiliser la carte de notification.

<figure><img src="../../../.gitbook/assets/docbits_email_settings.png" alt="DocBits E-mail Paramètres"><figcaption></figcaption></figure>

Selon les paramètres, l'utilisateur se voit assigner une nouvelle tâche dans DocBits et, en option, un e-mail pour l'informer de sa nouvelle tâche.
