# Fonctionnement de la recherche dans la documentation

Le Settings Assistant recherche des informations pertinentes dans les pages publiques de [docs.docbits.com](https://docs.docbits.com). Les résultats peuvent contenir un titre de page, un court passage et un lien vers la page source. Ouvrez le lien lorsque vous avez besoin des instructions complètes ou d'une capture d'écran.

## Trouver la bonne page

La recherche combine la correspondance de mots et la correspondance par le sens. Cela aide lorsque votre question utilise des mots différents de ceux d'un titre de page. L'assistant peut aussi utiliser la page de paramètres que vous consultez pour rendre la réponse plus pertinente.

Si la recherche par le sens est temporairement indisponible, la recherche dans la documentation peut encore utiliser la correspondance de mots. Une question précise contenant le nom du paramètre est la meilleure façon de réessayer.

## Langues

La recherche dans la documentation utilise actuellement les index des pages d'aide en **anglais** et en **allemand**. Si l'interface DocBits utilise une autre langue, l'assistant se rabat sur des résultats de documentation en anglais. La page liée affiche sa propre langue ; vérifiez-la avant de suivre des étapes ou de comparer des captures.

## Quand les changements deviennent consultables

L'index de recherche est actualisé lorsque des changements de la documentation anglaise ou allemande sont publiés depuis le dépôt de documentation. Une réconciliation régulière supprime aussi les liens vers des pages qui ne figurent plus dans la navigation de la documentation. Une page nouvellement publiée peut mettre un peu de temps à apparaître dans l'assistant.

### Aperçu technique pour les administrateurs

Les pages d'aide publiées sont découpées en sections et stockées dans un **OpenSearch documentation index** propre à chaque langue prise en charge. Cet index est distinct des index utilisés pour les documents téléversés d'une organisation. Lorsqu'une page change, les sections inchangées peuvent être ignorées et les sections modifiées sont réindexées. Les pages supprimées sont retirées de l'index de documentation.

Pour une question, le service combine des correspondances de mots-clés avec une similarité vectorielle, puis ordonne les passages les plus pertinents. Si le service d'embeddings n'est pas disponible, la recherche par mots-clés reste disponible. Le Settings Assistant reçoit des liens sources et de courts passages de cette recherche documentaire ; il ne lit pas l'index de documents d'une organisation pour cela.

Si vous ne trouvez pas de page, recherchez directement sur [docs.docbits.com](https://docs.docbits.com), essayez une question plus précise ou contactez le support DocBits.

{% hint style="info" %}
Cette recherche couvre les pages d'aide DocBits. La fonction [Fulltext Search](../document-processing/module/fulltext-search.md) recherche dans les documents de votre organisation et dispose de ses propres paramètres.
{% endhint %}

Revenir à [l'utilisation du Settings Assistant](README.md).
