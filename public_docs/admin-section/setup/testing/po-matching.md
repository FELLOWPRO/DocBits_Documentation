# Correspondance des bons de commande (PO)

Lorsqu'il s'agit de tester votre configuration de correspondance des bons de commande (PO), vous devrez créer un bon de commande dans LN/M3 afin de vérifier si INFOR est synchronisé avec DocBits.

## Création d'un bon de commande dans INFOR

* LN: [Documentation LN](https://docs.infor.com/ln/10.4/en-us/lnolh/docs/ln\_10.4\_procpoug\_\_en-us.pdf)
* M3: [Documentation M3](https://docs.infor.com/m3udi/16.x/en-us/m3beud/default.html?helpcontent=ois610.html)

Une fois que vous avez créé votre bon de commande, allez dans Paramètres → Recherche de données maîtres et recherchez le numéro de bon de commande du bon de commande que vous venez de créer, car il devrait maintenant apparaître dans vos données maîtres de bon de commande dans DocBits.

![](https://lh7-us.googleusercontent.com/JKGJdww6uF6U5mc1s1X\_uCcEMPYeqcikfrFOFjxpxpuaNjw-XmzNmIV2G2x6R-ZpwN2KlZACQe5Hs\_UB26klGU5XZyu6srVVLPVkS9AgEDZ1SO75YF-4ZTIt-aAuxoyyoW5sNPLsl0UxXwk193QNrFs)

Vous devriez voir votre numéro de bon de commande unique ici, ce qui signifie que DocBits et INFOR sont correctement synchronisés.

Maintenant, téléchargez votre facture qui correspond aux quantités et aux prix unitaires du bon de commande que vous avez créé. Validez le document et sélectionnez la Correspondance des bons de commande à l'écran de validation.

Les éléments de ligne du bon de commande et de la facture devraient correspondre automatiquement, il vous suffit ensuite de sélectionner l'option d'exportation et de vérifier si le document est exporté sans erreurs. Si vous rencontrez une erreur d'exportation, créez un ticket pour l'équipe de support de DocBits pour obtenir de l'aide. Si vous ne savez pas comment créer un ticket dans DocBits, veuillez consulter notre documentation générale de DocBits pour obtenir de l'aide.
