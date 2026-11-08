# Appearance

**Appearance** permet à un administrateur de donner à la copie de DocBits de l'organisation son propre aspect : couleurs, rayon d'angle, densité et police. Tous les membres de l'organisation voient le résultat — en mode clair comme sombre — après leur prochain rechargement. Cela ne change jamais la mise en page ni ce que fait une fonction, seulement la manière dont elle est dessinée.

> **Accès :** Appearance est une page réservée aux administrateurs. Ouvrez **Settings → Organization & Access → Appearance**.

<!-- screenshot: /settings/appearance light -->

## Qui peut le modifier

Seuls les administrateurs de l'organisation peuvent ouvrir **Settings → Appearance** et enregistrer ou réinitialiser un thème. Tous les autres membres de l'organisation ne voient que le résultat.

## Contenu de la page

La page se divise en un éditeur à gauche et un aperçu en direct à droite.

| Zone | Ce qu'elle contient |
|---|---|
| **General** | Le nom du thème, la police, le rayon d'angle et la densité. |
| **Colors** | Les onglets Light et Dark, un sélecteur de couleur plus un champ hexadécimal par couleur, regroupés en Surfaces, Brand, Neutrals, Status et Charts. Un panneau « Derived colours » en lecture seule en dessous montre les couleurs que DocBits calcule pour vous (états de survol, anneaux de focus et similaires) à partir des couleurs ci-dessus. |
| **Advanced overrides** | Une ligne `--token: value` par entrée, pour le cas rare où les contrôles de couleur, de rayon, de densité et de police ci-dessus ne suffisent pas — voir [Advanced overrides](#advanced-overrides). |

### Modifier les couleurs

Chaque couleur dispose d'un échantillon (cliquez dessus pour ouvrir le sélecteur de couleur du navigateur) et d'un champ hexadécimal à côté dans lequel vous pouvez saisir ou coller une valeur. Laissez une couleur vide pour conserver la valeur DocBits par défaut de ce token — l'échantillon affiche alors une bordure pointillée. Basculez entre les onglets **Light** / **Dark** au-dessus de la liste des couleurs pour régler l'autre mode ; une couleur que vous ne définissez pas en mode sombre conserve sa propre valeur DocBits par défaut pour le sombre et ne reprend pas la valeur claire.

{% hint style="info" %}
Les couleurs sont saisies en hexadécimal (`#2388ae` ou `#2388aeaa` avec alpha). Il n'y a pas de saisie de nom de couleur ni de `rgb()`.
{% endhint %}

### Rayon d'angle, densité et police

* **Corner radius** — `None`, `Small`, `Medium` (par défaut), `Large` ou `Extra large`. Contrôle l'arrondi des cartes, boutons, champs de saisie et boîtes de dialogue, dans toute l'application.
* **Density** — `Compact`, `Comfortable` (par défaut) ou `Spacious`. Contrôle la hauteur des boutons, des champs de saisie et des lignes de tableau, ainsi que la taille de texte de base.
* **Font** — une courte liste de polices intégrées (Geist est celle par défaut de DocBits ; également Inter, Roboto, IBM Plex Sans, Source Sans 3, Nunito Sans, Manrope, Kanit, ou la police système du visiteur). Chaque police est déjà intégrée, il n'y a rien à téléverser.

### Advanced overrides

Pour un token de design que les contrôles ci-dessus n'exposent pas directement (par exemple une hauteur de ligne de tableau précise), ajoutez une ligne sous **Advanced overrides** :

```
--table-row-h: 30px
```

Une surcharge par ligne, `--token: value`. Une ligne invalide — un token inconnu, un token qui ne peut pas être personnalisé, ou une valeur qui ne correspond pas à ce que le token attend — est signalée comme erreur sous la zone et n'est pas appliquée ; tout le reste de la page s'enregistre normalement.

## Aperçu

Chaque modification met immédiatement à jour le panneau **Preview** à droite, sans affecter ce que voient les autres — il ne touche jamais l'application en cours d'utilisation ni le thème enregistré. L'aperçu a ses propres onglets : une vue d'ensemble avec le clair et le sombre côte à côte, puis des pages dédiées aux boutons, aux champs de formulaire, aux surfaces et aux indicateurs de statut, pour vérifier le contraste et la lisibilité dans les parties de l'interface les plus sensibles à la couleur.

<!-- screenshot: /settings/appearance dark -->

Si une modification rend le thème invalide (voir ci-dessous), l'aperçu continue d'afficher la dernière version valide au lieu de casser.

## Enregistrer et réinitialiser

* **Save** écrit le thème pour toute l'organisation. Le bouton est grisé tant que rien n'a réellement changé et que le thème n'est pas valide.
* **Reset** demande une confirmation, puis supprime entièrement le thème de l'organisation et ramène tout le monde au thème DocBits par défaut. Cela ne peut pas être annulé depuis la page — les couleurs doivent être saisies à nouveau à la main (ou réimportées, voir ci-dessous) si l'organisation les veut de retour.
* Un enregistrement ou une réinitialisation qui échoue (par exemple à cause d'un problème de validation) affiche le problème au-dessus de l'éditeur et laisse la page telle quelle ; rien n'est appliqué.

Il n'y a pas de contrôle de contraste avant l'enregistrement — voir [Conseils](#conseils) ci-dessous.

## Exporter et importer

* **Export** télécharge le thème actuellement affiché dans l'éditeur (enregistré ou non) au format `.json`, nommé d'après le thème.
* **Import** lit un fichier de thème `.json` et le charge dans l'éditeur. Il doit encore être vérifié et enregistré pour prendre effet — importer seul ne change pas ce que voit qui que ce soit. Un fichier invalide ou trop volumineux (plus de 32 Ko) est rejeté avec une erreur et rien ne change.

L'export est un moyen pratique de sauvegarder un thème avant d'expérimenter, ou de copier l'aspect d'une organisation vers une autre.

## Ce que voient les utilisateurs

Une fois enregistré, le thème s'applique à toute l'application — chaque page, en mode clair et sombre — pour chaque membre de l'organisation, après son prochain rechargement (pas immédiatement pour les autres sessions ouvertes). Un utilisateur qui n'a jamais chargé l'organisation voit la valeur DocBits par défaut jusqu'à ce que les paramètres de l'organisation aient été chargés une fois ; ensuite le thème prend le relais.

La réinitialisation ramène tout le monde à l'aspect DocBits par défaut lors du prochain rechargement, exactement comme si aucun thème d'organisation n'avait jamais été défini.

## Conseils

* **Vérifiez le contraste dans les deux modes.** L'éditeur n'avertit pas des combinaisons à faible contraste (par exemple une couleur de marque claire avec du texte clair). Utilisez les panneaux clair et sombre de l'aperçu pour vérifier que le texte reste lisible avant d'enregistrer.
* **Ne modifiez les couleurs de statut que si vous avez une raison de le faire.** Destructive (erreurs), success, warning et info gardent leur signification dans toute l'application — les modifier peut faire passer une erreur pour un succès au premier coup d'œil. Changez la couleur de marque et laissez les couleurs de statut à leurs valeurs par défaut, sauf si l'organisation a besoin de plus que le rouge/vert/ambre/bleu habituel.
* **Partez d'une palette complète.** Exporter le thème actuel ou partir de la valeur DocBits par défaut donne une valeur à modifier pour chaque couleur de base, plutôt que de deviner quels tokens existent.
* **Un changement de thème affecte chaque utilisateur de l'organisation dès son prochain rechargement.** Il n'y a pas d'étape d'aperçu réservée à un sous-ensemble d'utilisateurs ; testez vous-même le résultat en clair et en sombre avant de dire à l'équipe que c'est prêt.
