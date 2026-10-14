# Origin Layouts

{% embed url="https://youtu.be/-m45XGiIeig" %}
Paramètre Origin de DocBits expliqué : Normes de pays pour les formats de date et de nombre
{% endembed %}

DocBits excelle dans l'adaptation des mises en page de documents en fonction de leurs origines géographiques tout en standardisant des éléments tels que les formats de devise en fonction des paramètres du navigateur de l'utilisateur. Explorons comment vous pouvez utiliser le Layout Builder pour personnaliser les mises en page pour différentes origines, comme les États-Unis et l'Allemagne.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/origin_layout_1.png)

## **Comprendre la personnalisation basée sur l'origine**

* Standardisation de la devise et du format : Quelle que soit la devise ou le format du document original, DocBits convertit ces éléments en un format ISO standardisé sur le serveur, conformément aux paramètres du navigateur de l'utilisateur.
* Personnalisation de la mise en page géographique : Le système permet la personnalisation des mises en page de documents en fonction de leur origine géographique. Cela signifie que vous pouvez définir des champs et des formats spécifiques pour des documents de différents pays.

## **Exemple : Mises en page États-Unis vs Allemagne**

* Mise en page États-Unis : Pour une facture américaine, vous pourriez inclure des champs pour la taxe municipale (city tax), conformément à la structure fiscale courante aux États-Unis.
* Mise en page Allemagne : En revanche, une mise en page de facture allemande peut omettre le champ de taxe municipale, car ce n'est pas une charge standard en Allemagne.

## **Utilisation du Layout Builder**

* Sélectionner l'Origin Layout : Dans le Layout Builder, choisissez la mise en page de base correspondant à l'origine du document.
* Personnaliser les champs : Adaptez la mise en page en ajoutant ou en supprimant des champs. Par exemple, incluez 'City Tax' pour une mise en page américaine.
* Appliquer et tester : Une fois personnalisé, appliquez la mise en page à vos documents et testez pour garantir l'exactitude.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/origin_layout_2.svg)

## **Conseils pour une personnalisation efficace**

* Comprendre les différences régionales : Familiarisez-vous avec les nuances fiscales et de format des différentes régions.
* Mises à jour cohérentes : Mettez régulièrement à jour vos mises en page pour refléter tout changement dans les réglementations régionales.
* Retours des utilisateurs : Utilisez les retours des utilisateurs de différentes régions pour affiner davantage les mises en page.

## Appliquer la mise en page par défaut à plusieurs Origins

Lorsque vous souhaitez appliquer la mise en page par défaut à plusieurs origines, appuyez sur **Appliquer la disposition par défaut à Origins**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/origin_layout_3.png)

Une fenêtre contextuelle apparaîtra où vous pouvez sélectionner les origines auxquelles vous souhaitez appliquer la mise en page par défaut. Vous pouvez utiliser **Tout sélectionner** ou **Tout désélectionner** pour gérer rapidement votre sélection. La fenêtre contextuelle affiche le nombre d'origines actuellement sélectionnées.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/origin_layout_4.png)

Après avoir fait votre sélection, cliquez sur **Appliquer aux Origins**. Un message de succès confirmera que les origines ont été mises à jour.
