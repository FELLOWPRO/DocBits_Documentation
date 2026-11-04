# Extraction de tableaux pour le calcul des coûts

<figure><img src="../../../.gitbook/assets/docbits_m3_costing_element_table_fr.jpg" alt="Docbits M3 Costing Element Table Fr"><figcaption></figcaption></figure>

Pour activer l'extraction de tableau pour l'élément de coût, vous devrez importer le tableau m3costingelement dans DocBits.

Depuis la page d'accueil de M3, tapez Commande + r et recherchez l'invite “PPS280”.

Sélectionnez l'une des lignes qui vous sont affichées. Dans le menu suivant, sélectionnez OUTILS et “Exporter vers Excel”.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FI8SYWm-JwpyYRHFUp2obGtXcsa7m_blJ_lTrnhczztRIXIN5gfxCt3eRw6ZI42fH6AwnsKyv4ux5-rhaT505PsyDFFI_anUNvmACFyx_ssgxaqWq25vLt_E5s310HNoiPPLf35qJlYtstjpj5Cc4aB4\&width=768\&dpr=4\&quality=100\&sign=5aa04ccf\&sv=2)

Sélectionnez “Exporter toutes les lignes” puis appuyez sur EXPORTER.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FwtjHI9L4YUhf-yJFjcPGu218Vis_zELtCIfpmkIUKgasfrdfNW-dr_J1DqXlfD-SBrnVduDrMLAIAQh6UTlzBqEP_JPXP48elGMyGj0ByZbX7TpqlnIfRZ4ZoD0pyCo-AKigeKjlHN6cFcdpeClZ9L4\&width=768\&dpr=4\&quality=100\&sign=7cf7a274\&sv=2)

Une fois téléchargé, vous devrez modifier le fichier Excel avant de le convertir en fichier CSV.

Vous devrez ouvrir le fichier Excel, il ressemblera à ce qui est montré ci-dessous.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FmR6GtTDYMGf48yc3GCau%252Fimage.png%3Falt%3Dmedia%26token%3Daf52d75f-bdb9-4b18-a4b0-572b76e14309\&width=768\&dpr=4\&quality=100\&sign=57660254\&sv=2)

À partir de cette feuille Excel, vous avez besoin des colonnes A, B, H, J, K et I, modifiez la feuille Excel de sorte que le résultat final ressemble à ce qui suit.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FajTC0UO55QZRMDyhBxm1%252Fimage.png%3Falt%3Dmedia%26token%3D5b29b038-8156-4e67-8536-e0bcb65c35ff\&width=768\&dpr=4\&quality=100\&sign=5e46e6c2\&sv=2)

Une fois cela fait, enregistrez le fichier au format CSV.

Une fois que vous avez votre fichier CSV, allez sur la page web suivante. Cela dépend de l'environnement que vous utilisez :

* Prod : http://api.docbits.com/
* Sandbox : http://sandbox.api.docbits.com/
* Stage : http://stage.api.docbits.com/
* Démo : http://demo.api.docbits.com/
* Dev : http://dev.api.docbits.com/

Ici, vous téléchargerez manuellement le tableau CostingElement via une API. Cliquez sur le bouton Autoriser.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FtyzOq3BR2QqTguQFKicxo0dE5j5hGsP-BhfVbS81O_mxN5bSVp40jYfgsVJcE_rBLFMDJNvbPkPIdjPqaqoNbHBBM-9hx0i-U4VAH9ISBYhpwKgqQeUEd67VV1E4izwNyxbAwwrhCmrAo1uIKhLherY\&width=768\&dpr=4\&quality=100\&sign=188f5712\&sv=2)

Ici, vous devrez insérer la clé API de votre environnement DocBits. Cela se trouve dans les Paramètres sous Intégration.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2F4ADnevq6kq_vbxUJpyPbHNcGvRvpO-l9Gwd8ZaYf_vO4uWhSl1jmKNpddmHGc9ZHMMbXCgLOElLDYbNwB3INmBDETecPrDnpI601IUOZQlT7tc7OLSPXwkooOJFNwML2i_gvBPuE8CvfwRpX-ZIlb_g\&width=768\&dpr=4\&quality=100\&sign=dedfcaaf\&sv=2)

Une fois terminé, recherchez l'API appelée master\_data\_lookup/import\_data et remplissez les informations requises. Une fois terminé, cliquez sur EXÉCUTER pour déclencher l'API.

### data\_type doit être costing\_element

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2F8UD4FhFv2dRB4cMjCDL4G9ndjH7laVMKWqdeMaJGgEo48-UVvucB1uOydzNdfFy0yPM5bb66mZB4k9uJR7TTiEREGFaV2EqW01gxJpTyuUfGNh5QmBjySkyhZ56gWV8sYs8WI5RnHcENtXgjTU0vg0Q\&width=768\&dpr=4\&quality=100\&sign=7c9f4dbb\&sv=2)

Si cela est fait correctement, le tableau M3CostingElement devrait maintenant être dans votre environnement DocBits. L'extraction de tableau pour les éléments de coût a maintenant été configurée pour votre environnement.
