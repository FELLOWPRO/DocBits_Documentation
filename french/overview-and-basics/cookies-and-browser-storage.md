# Cookies et stockage du navigateur

Vérifié le **16 octobre 2026** pour la question **4.15**. Le site public, l'application DocBits et cette documentation utilisent des cookies et des services différents.

## Politique et finalités

La [Politique de confidentialité de DocBits](https://docbits.com/en/privacy-policy/) contient les sections **Cookies** et **Consent with Borlabs Cookie**. Elle décrit le consentement, les fonctions essentielles, la protection contre les robots, Google Analytics, la publicité et Leadfeeder. Les analyses peuvent produire des rapports sur les visites, pages, interactions et performances, mais la collecte ne se limite pas à des données anonymes agrégées. Cette politique ne définit pas à elle seule l'inventaire de l'application.

## Inventaire des cookies

**Observé** désigne une nouvelle visite sans connexion ni sélection d'un consentement facultatif. **Code** désigne du code ou des paramètres d'infrastructure examinés, sans confirmer les attributs de chaque réponse en production.

| Cookie / périmètre | Finalité et durée | Preuve et attributs de sécurité |
| --- | --- | --- |
| `__cf_bm` / site et application | Protection Cloudflare contre les robots ; 30 minutes d'inactivité | Observé : `Secure`, `HttpOnly`, `SameSite=None`. [Cloudflare](https://developers.cloudflare.com/fundamentals/reference/policies-compliances/cloudflare-cookies/) chiffre les informations relatives aux robots, sauf les informations temporelles. |
| `pll_language` / site | Préférence linguistique ; environ un an | Observé : `Secure`, lisible par JavaScript, `SameSite=Lax`. |
| `_lfa` / site | Analyse des visiteurs et entreprises par Leadfeeder ; environ un an | Observé : lisible par JavaScript, `SameSite=Lax`, **sans attribut `Secure`** lors de cette visite. |
| Cookie de consentement Borlabs / site | Enregistre les consentements et retraits | Déclaré dans la politique ; nom, attributs déployés et durée non vérifiés lors de cette visite. |
| `session` / authentification | État de session des parcours d'authentification | Valeurs par défaut du code : `Secure`, `HttpOnly`, `SameSite=None` ; données Flask signées, non chiffrées. Le déploiement peut modifier ces valeurs. |
| `dbx_td` / authentification | Mémorise un appareil de confiance si choisi après une MFA réussie ; 30 jours | Code : `Secure`, `HttpOnly`, `SameSite=None` ; jeton aléatoire dont le hachage est stocké côté serveur. |
| `prod-sticky` / répartition en production | Oriente les requêtes vers le même backend ; durée configurée de 300 secondes | Paramètre d'infrastructure vérifié ; attributs du navigateur non vérifiés. |
| `dontAsk` / application | Mémorise une préférence pour une invite ; aucune expiration explicite dans l'appel examiné | Code : lisible par JavaScript ; aucune option explicite `Secure` ou `SameSite` dans cet appel. |

Aucun cookie n'a été observé lors d'une nouvelle visite de la documentation. Il s'agit d'un constat daté, pas d'un inventaire exhaustif des parcours connectés, fonctions facultatives ou contenus intégrés tiers. La politique cite d'autres services d'analyse/publicité dont les cookies n'ont pas été confirmés. L'inventaire complet et l'application du consentement demandent une vérification distincte de ces parcours.

## Sécurité et analyses

`Secure` limite l'envoi à HTTPS. `HttpOnly` empêche la lecture par JavaScript. `SameSite` contrôle l'envoi entre sites. Ces attributs ne chiffrent pas le contenu. Affirmer que tous les cookies sont chiffrés ou protégés de façon identique serait inexact. Les endpoints publics prennent en charge TLS 1.2 et 1.3 ; voir [Stockage sécurisé des identifiants](secure-storage-of-credentials.md).

Le stockage du navigateur est aussi utilisé indépendamment des cookies. La configuration Grafana Faro prévoit le suivi persistant des sessions, les erreurs, mesures de performance et traces, avec des identifiants d'utilisateur et d'organisation lorsqu'ils sont disponibles. La collecte dépend du collecteur déployé. Elle ne doit pas être présentée comme une simple analyse anonyme et agrégée des cookies. Les préférences linguistiques utilisent aussi le stockage local.

Vous pouvez supprimer cookies et stockage dans le navigateur ; cela peut effacer des préférences et la mémorisation des appareils de confiance. Pour un inventaire actuel ou des questions de confidentialité : **compliance@fellowpro.com**.
