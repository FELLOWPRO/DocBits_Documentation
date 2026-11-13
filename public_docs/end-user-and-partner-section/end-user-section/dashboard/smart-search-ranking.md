# Smart Search Ranking

Smart Search Ranking place les documents que vous cherchez en tête d'une recherche du tableau de bord. Une recherche par mot-clé trouve chaque document qui contient votre mot ; Smart Search Ranking ajoute une étape : une IA lit les meilleurs résultats et place en premier les documents qui parlent vraiment de votre recherche. Les correspondances exactes — numéros de facture, numéros de commande, noms de fournisseurs — restent toujours en tête.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/features/smart-search-ranking/preview/fr.mp4" %}
Smart Search Ranking dans le tableau de bord (narration en français). [Lecteur avec sous-titres](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/features/smart-search-ranking/preview/fr.html) · [Transcription](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/features/smart-search-ranking/preview/fr.txt)
{% endembed %}

## Ce qui change

| | Ordre par mot-clé | Avec Smart Search Ranking |
| --- | --- | --- |
| Quels documents sont trouvés | Les mêmes | Les mêmes |
| Ordre des résultats | Par correspondance du mot-clé | Les documents qui parlent de votre recherche d'abord |
| Correspondances exactes (n° de facture, n° de commande, fournisseur) | En tête | En tête |
| Tri par colonne, recherches `ocr:` et par champ | Inchangés | Inchangés — ils gardent leur propre ordre |

## Exemple

Huit factures de test contiennent les lettres *vis* : des vis en inox, un jeu de tournevis, l'entretien d'un compresseur à vis, des bouteilles à bouchon à vis, une visite d'entretien, des classeurs à vis, du frein-filet et un coffret d'assortiment de vis.

* Recherchez **vis**. Dans l'ordre par mot-clé, le jeu de tournevis est le premier résultat et la facture de vis arrive en cinquième position. Avec Smart Search Ranking, la facture de vis passe en premier, puis l'assortiment de vis ; le jeu de tournevis descend en quatrième position.
* Recherchez **tournevis**. Dans l'ordre par mot-clé, le jeu de tournevis est premier. Avec Smart Search Ranking, les tournevis professionnels passent en tête et le jeu de tournevis reste dans le haut du classement, parce que cette fois, ce sont bien des tournevis ; le jouet descend.

## Où cela s'applique

* Dans la [Recherche rapide](quick-search.md) du tableau de bord avec du texte simple (pas dans les puces de champ `champ:`).
* Le haut de la liste de résultats est réordonné ; plus bas, les longues listes gardent leur ordre par mot-clé.
* Si le service de classement ne répond pas dans son délai, la recherche affiche l'ordre normal par mot-clé. Rien n'est masqué, aucun résultat n'est retiré.

## Comment l'activer

Smart Search Ranking est activé par DocBits pour chaque organisation. Demandez à votre contact DocBits de l'activer. Il s'applique à tous les utilisateurs de l'organisation en moins d'une minute, sans rien changer à votre façon de chercher.
