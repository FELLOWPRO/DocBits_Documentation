# Vérifier le paramètre de société logistique en cas d'écarts de réception de marchandises

Dans les processus d'achat à grande échelle, il n'est pas rare que certaines données ne concordent pas comme prévu. Par exemple, vous pouvez voir un message d'erreur tel que :

**« Delivery Note L1234, Order Type: Purchase, Order 100000211, Position 10, Subsequent Number 1, Logistic Company&#x20;**<mark style="color:red;">**XXXX**</mark>**, Goods Receipt WE0000293 and Entry Position 10 not found in direct debit. »**

Ce type de message indique souvent une incohérence ou des informations manquantes dans la configuration de votre société logistique. La société logistique est un élément essentiel des systèmes de planification des ressources d'entreprise (ERP), en particulier dans les chaînes d'approvisionnement complexes qui s'étendent sur plusieurs entités juridiques ou logistiques.

**Pourquoi cela se produit-il ?**

Dans les environnements multi-entités, chaque transaction (achat, réception de marchandises ou lancement de paiements) doit être correctement affectée à la bonne société logistique. La « société logistique » est bien plus qu'un simple identifiant : elle détermine quel entrepôt, centre de distribution ou nœud du réseau d'approvisionnement est responsable de la commande et des tâches d'exécution. Si le numéro de société ne correspond pas à l'entité attendue, les processus en aval, tels que la vérification de la réception de marchandises ou les règlements par prélèvement, peuvent échouer.

## **Vérifications essentielles à effectuer :**

### 1. Vérifier la société logistique affectée :

Contrôlez les enregistrements de données de base pour vous assurer que la société logistique référencée (ici, <mark style="color:red;">XXXX</mark>) est bien l'entité appropriée pour la commande concernée. <mark style="color:red;">XXXX</mark> est-il le bon code société pour traiter les achats auprès de ce fournisseur ou pour cette gamme de produits ?

### 2. Examiner la configuration du bon de commande (PO) :

Vérifiez que la société logistique du bon de commande correspond au lieu de réception prévu. Il arrive qu'une commande soit créée sous une société logistique, mais que les marchandises soient réceptionnées sous une autre si la configuration n'est pas cohérente.

### 3. Recouper la réception de marchandises et les enregistrements d'entrepôt :

Consultez la réception de marchandises (WE0000293) et assurez-vous qu'elle a été enregistrée dans l'entrepôt de la bonne société. Si l'entrepôt appartient à une autre société logistique, vous devrez peut-être corriger la configuration ou effectuer un transfert vers la bonne entité.

### 4. Vérifier la cohérence de l'intégration et des données de base :

Les points d'intégration entre les différents modules (achats, entreposage, finance) reposent sur des codes cohérents. Assurez-vous que la société logistique est définie de manière uniforme dans tous les modules concernés.

### 5. Consulter la documentation et le support :

Si les vérifications internes ne permettent pas de résoudre le problème, consultez la documentation de votre système ou contactez votre équipe de support ERP. Elle pourra vous aider à vérifier si le code de la société logistique est correctement configuré ou si des étapes de configuration supplémentaires sont nécessaires.
