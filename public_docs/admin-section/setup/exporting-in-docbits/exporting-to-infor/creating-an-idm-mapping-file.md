# Création d'un fichier de mappage IDM

Une fois obtenu, ouvrez le fichier dans l'éditeur de fichiers de votre choix. Pour cette démonstration, VSCode sera utilisé.

## Modifier le fichier de mappage

Vérifiez que le code du type de document est tel qu'il est dans DocBits (comme avec le fichier de mappage BOD, il doit correspondre au nom du type de document dans l'URL des paramètres de champ) et vérifiez également le nom du type de document tel qu'il doit être dans Document Manager (IDM) dans Infor.

![](https://lh7-us.googleusercontent.com/WHO0vg2W36yVFBq0ay0wBMFVzMfT6pNvHklt0o8N4tqUpM03jXJm2fykuYjyZh0z4wFTO4Eaeh39-D03re3a9utegrdVdsjHBfucmALA3B7YBWd92-9bcYr543G4MWftv0RosvTgFP3J6NNmLZAz5Dc)

**FYI**: Il est indiqué que le nom du type de document dans IDM est M3\_SupplierInvoice, ceci est dû à un exemple d'une instance M3. Cela peut changer en fonction de l'utilisation de LN ou M3, ainsi que de votre configuration IDM spécifique.

Vérifiez l'ID de l'entreprise, et vérifiez l'ID de l'entité (SF\_MDS\_EntityType) cette valeur doit être la même que dans le fichier de mappage BOD.

Assurez-vous que IndexFieldFromDocBits=IDMAttributeID (vérifiez si DocBits à gauche dans les paramètres de champ correspond à IDM à droite dans Type de document → Attributs).

### Gestionnaire de documents dans Infor

Accédez au Gestionnaire de documents et sélectionnez le nom du type de document actuel que vous essayez d'exporter, par exemple, Facture Fournisseur.

![](https://lh7-us.googleusercontent.com/EV3uw3R1L6\_RRANB7FRLwtUFMbv\_KGtL4x6kAk6lEYhwI90UeG2uWqFD2Azpxv-SRFl9zfvdratOZbXxp2D1-SryLo3Boj2x9Xc4PQXJ6vUhX5c9pvhv4XHuCk-qMK51DZ885vRUJ5dwES7k84uhoyk)

Cliquez sur l'icône ci-dessus, puis sur Administration → Type de document et trouvez le type de document dont vous avez besoin dans la liste.

![](https://lh7-us.googleusercontent.com/ldsuINS9SCUQm3E57s8j\_95gzBGwHQFavcf6d3myg6tuVxRoQHtq8R-6we5OEJ63swDxwPc9w7hbySWqWdfaMsGdQpn99m6EchPY5f5DzXEj-8mjocwPNtdJVNP34CuPvw0JIImDgFX1Q05M8-ogZo8)

Comme indiqué ci-dessous, vous verrez ensuite le nom du type de document tel qu'il est dans INFOR.

![](https://lh7-us.googleusercontent.com/KSreWGS7TqdMP64BqtufM24xk0RDnNDHUZapnPsSuRj\_umPJ3icll89KI2RYpbtet2F6ccL8QfYbl27-2j1nQPwQ0z-Nq873c4Tv72ee9AJhKMxynIUxmJKKsQQCupW\_dpRfw\_5BXm0WvAnw4HOALmw)

Assurez-vous que c'est ainsi que le nom est affiché dans le fichier de mappage IDM.

## Téléverser le fichier sur DocBits

Une fois le fichier préparé, téléversez-le dans votre configuration d'exportation dans DocBits. Cela est disponible dans Paramètres → Exportation.

![](https://lh7-us.googleusercontent.com/rUHhvImiWamK6JxnWSPL4JEioAJq3AmvdsubJDo-DoDV9F\_i5mZ42YDnjqZUYKYSJu1Cetc\_4fLwlvvmoZXYIzmBf3hoyW6RjfP9HQ8FkNDhW1IbLHvNTCHWFRaeCECdZ97u79-Eu37TvzqnqGPEayM)
