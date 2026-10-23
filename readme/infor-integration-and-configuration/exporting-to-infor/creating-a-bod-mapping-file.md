# Créer un fichier de mappage BOD

Téléchargez un fichier de mappage BOD et ouvrez-le dans l'éditeur de fichiers applicable de votre choix pour le modifier. Pour cette procédure pas à pas, VSCode est utilisé.

## Modifier le fichier de mappage

Remplacez l'entreprise par la bonne (SFV\_AccountingEntityID) et modifiez l'emplacement ID si nécessaire.

![Fichier de mappage BOD ouvert dans VSCode avec SFV_AccountingEntityID et d'autres mappages clé-valeur de SyncCaptureDocumentType](https://lh7-us.googleusercontent.com/eJQI1CKlxEkS\_Pwp0VH2hgS220b-q8NSFG5iJKpLOL457qTN3CbUB8IHTw1lRinbB\_kP00UUNgepWNsbh3\_Ko-SExObePjqmxP7ee\_lQnADTtDmxEtRM\_S7AONMbcpjwtnHTakYd1Q06GVm2G0o-UDA)

Vérifiez le code du document en accédant aux paramètres de champ du type de document que vous essayez d'exporter (trouvés dans URL des paramètres de champ du type de document dans DocBits comme ci-dessous

![Page des paramètres de champs de DocBits pour le type de document facture dans le navigateur avec l'URL affichant le code du document](https://lh7-us.googleusercontent.com/AhU3i27qFS7BMCgpNQnmLWAjcIWHXHOlxMKqd2Yob5RQKa8qysQQsSsacr6zao4cnAh3DISPgYu1GnjubIJpgtAdiBR\_0vy3WJZXPY-HeEfVQkWnlRI9UEJWMPQ7DbWYLQhz339BOlbd4KgxU9B\_CPE)

Enfin, modifiez le SFV\_LogicalID qui se trouve dans INFOR ION DESK → Connecter → Points de connexion et sélectionnez le DocBits\_Export ou un point de connexion similaire et dans cette page, vous trouverez l’ID logique dont vous avez besoin.

![Page Connect d'ION Desk avec la liste des Connection Points et DocBits-Prod-Export sélectionné](https://lh7-us.googleusercontent.com/f50i7pzRuZULJ6shehba0lWIWFBTsPZyip-LQxAYJpYDXK66SlzdGOpdEG-wqLQfqXMgMMhm5SAvj57UOCvF6xf2OMCXtFiEEKr9yiQr4xtv8vbV-NGcLuJwuQ9zHMBBKfTktAp1nSfBJhdPeAu3RWc)

![Page Connection Point DocBits-Prod-Export dans ION Desk avec API Client Id et Logical ID infor.ims.docbits-prod-export](https://lh7-us.googleusercontent.com/qyEt4iYRIjOZCCrVbImeK6EdZGun2YrAy8li8u3tulcD8bwzl\_sl1TiEXKqbik-4MxnbV\_MCwltvuA2WAgzzvDpTVd7W52he9QD9IK0qijoz3ZihUYcWJlqlD5kbcsRTj3SfP1CDqcyhoFfBeiE1Xfo)

## Créer un ID logique (point de connexion)

Si ce Point de Connexion n'existe pas encore, vous devez en créer un.

Tout d’abord, allez dans ION Desk → Connect → Connection Points et cliquez sur le bouton “+ Add”

![Menu Connect de ION Desk avec la navigation Connection Points, Mappings et File Templates ouverte](https://lh7-us.googleusercontent.com/fQPmV8KgffyWhM0i0cQlyh7fyQe37p8uR6C\_pVD5SboEx2emIJX2212GXqk\_KT71DfYMKSjkfYFFTARqgLLxoOPNQFXHxUOo9vMXH2pmDN469VgbQkV-JjRtCevZJsbvS8vbfUtasN83xN25tX6\_S5U)

Sélectionnez ensuite l'option “IMS via API Gateway”

![Liste des Connection Points dans ION Desk avec l'option IMS via API Gateway mise en évidence parmi les types de points de connexion disponibles](https://lh7-us.googleusercontent.com/uPLiiLHp6Z3jPCzYBOzHVuI8sGY5XQuUfv66fZYH0HndSBL7yvzFHh3lJjEMxteJfXsVMhUe3U\_38xZHDRFSn0jeiMZUQBJJLzZ2oaIQAixY7wUPd6D0PJwg7wvC8XBeZxPmjNoiUvP3ImoG\_aOhFmY)

![Boîte de dialogue Infor Application Connection Point pour IMS via API Gateway avec les sections Authorization et IMS Endpoint](https://lh7-us.googleusercontent.com/VhyMDEuglPfxeX-3cATu6ZFB\_Mz2Y7C-yJ99EvBvrhD8IoVzGd4ksjrWAE0mIPub2PX5\_Zua10ZHQeWI82QbJ8ZgJKN-tVpVrYGvMdfQOj3Uco5efsPT6JYkDyPu\_lkeR9aTGhh5-q2bzZztXuTUixM)

Vous serez redirigé vers l'écran ci-dessus où vous devez maintenant remplir les informations nécessaires, le nom doit être quelque chose comme “DocBits\_export” ou similaire.

Pour “ION API Client ID”, vous entrez le même ID client que vous avez obtenu précédemment pour le fichier de mappage ION.

Sélectionnez ensuite l'onglet Document du menu de création de Point de Connexion et ajoutez les documents suivants en appuyant sur le signe “+”, cela ne deviendra utile que plus tard.

![Page Infor Application Connection Point DocBits-Sandbox-Export avec l'ID logique infor.ims.docbits-sandbox-export](https://lh7-us.googleusercontent.com/GtHlTliePV-JIDLP9YNGlXELKuWIU2VSlUt4mvWO4q\_XM54MSL9zTmtxPMdeOl24VFtNC0pQ-nbXyHb9PaeMkKvgzpCOo5kLdL3A8Bw54ILniwIdTyfxFhPuzRUGKs2hRi5ioKvfkdsPMgq4x6EHOtM)

Une fois que vous aurez enregistré ce point de connexion, vous obtiendrez l’ID logique comme indiqué ci-dessous

![Page de création de Connection Point avec le nom DocBits-Sandbox et le champ Logical ID Type](https://lh7-us.googleusercontent.com/P7cihsQT2Qcq\_XGL08dTV2jHMUK7YCMQyXsJudkVDXDh73GZ-hS61IoAKSHptPyX4C5e\_xPKP0yZGzpQOwCFw6BppPlzZuFWZ\_VGIrOUmJH2egxaCEXMoVBHBM6lkZeb3gPYWYdMYpuNqFFPC-4Qol0)

Insérez ensuite ce ID logique dans la section appropriée du fichier de mappage BOD et enregistrez le fichier.

## Importer un fichier dans DocBits

Faites glisser et déposez le fichier dans votre configuration d'exportation dans DocBits. Ceci est disponible dans Paramètres → Exporter.

![Page Export Settings de DocBits avec les colonnes Title, Document Type, Sub-Organizations, Export Method et Actions](https://lh7-us.googleusercontent.com/AqCo7QgC-kaAxbaIJD8MYeKGLBXbwGVJPGx9\_2yfUp3R2MYxJPowVAjnO80uxQ9qMDxNoXy1eY3WH-mEpaeWwatwi91edm\_0lS9Hg93FSAjQGtDAR5y7Ptce-ARfetSiXIBJKiGwujSggVXXHUhG77U)
