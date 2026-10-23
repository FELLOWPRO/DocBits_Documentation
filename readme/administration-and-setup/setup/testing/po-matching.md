# Rapprochement des commandes fournisseur

Lorsqu'il s'agira de tester votre configuration de correspondance PO, vous devrez créer un bon de commande dans LN/M3 afin de vérifier si INFOR est synchronisé avec DocBits.

## Créer une commande fournisseur dans INFOR

{% embed url="https://youtu.be/hn_bkeUMxJg" %}
{% endembed %}


* LN: https://docs.infor.com/ln/10.4/en-us/lnolh/docs/ln\_10.4\_procpoug\_\_en-us.pdf&#x20;
* M3: https://docs.infor.com/m3udi/16.x/en-us/m3beud/default.html?helpcontent=ois610.html&#x20;

Une fois que vous avez créé votre bon de commande, allez dans Paramètres → Recherche de données de base et recherchez le numéro de bon de commande du PO que vous venez de créer tel qu'il devrait maintenant apparaître dans les données de base de votre bon de commande dans DocBits.

![Table Purchase order dans les données de base de DocBits avec les colonnes Warehouse Id, Supplier Name, Purchase Order Number, Line Number et Quantity](https://lh7-us.googleusercontent.com/JKGJdww6uF6U5mc1s1X\_uCcEMPYeqcikfrFOFjxpxpuaNjw-XmzNmIV2G2x6R-ZpwN2KlZACQe5Hs\_UB26klGU5XZyu6srVVLPVkS9AgEDZ1SO75YF-4ZTIt-aAuxoyyoW5sNPLsl0UxXwk193QNrFs)

Vous devriez voir votre numéro unique PO ici, cela signifie que DocBits et INFOR sont correctement synchronisés.

Téléversez maintenant votre facture qui correspond à la quantité et aux prix unitaires du bon de commande que vous avez créé. Validez le document et sélectionnez PO Matching sur l'écran de validation.

Les lignes de détail PO et de facture doivent automatiquement correspondre, puis sélectionnez simplement l'option d'exportation et vérifiez si le document est exporté ou non sans aucune erreur. Si vous rencontrez une erreur d'exportation, créez un ticket pour que l'équipe d'assistance DocBits vous aide. Si vous ne savez pas comment créer un ticket dans DocBits, veuillez consulter notre documentation de présentation DocBits pour obtenir de l'aide.

\
