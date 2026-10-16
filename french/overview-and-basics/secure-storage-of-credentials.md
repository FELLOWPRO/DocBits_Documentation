---
description: Hachage des mots de passe, stockage des clés API, TLS, accès aux identifiants et récupération de compte dans DocBits.
---

# Stockage sécurisé des identifiants

DocBits traite les mots de passe de connexion, les clés API DocBits, les informations de compte et les identifiants des systèmes connectés selon leur usage. Cette page décrit leur protection et les modalités de récupération de l'accès.

## Mots de passe de connexion

DocBits stocke les mots de passe de connexion sous forme de **hachages salés à sens unique**. Lors de l'authentification, le mot de passe saisi est vérifié par rapport au hachage enregistré. Le mot de passe d'origine n'est pas stocké sous une forme permettant de le déchiffrer et de le récupérer.

Les administrateurs et le support DocBits ne peuvent donc pas retrouver le mot de passe existant en clair à partir du hachage stocké. En cas d'oubli, l'utilisateur doit réinitialiser son mot de passe pour pouvoir à nouveau se connecter par mot de passe.

### Réinitialisation du mot de passe

1. Sélectionnez **Mot de passe oublié ?** sur l'écran de connexion.
2. Saisissez l'adresse e-mail associée au compte.
3. Ouvrez le lien de réinitialisation envoyé à cette adresse.
4. Définissez un nouveau mot de passe et connectez-vous avec celui-ci.

Les liens de réinitialisation expirent. Si un lien a expiré, demandez-en un nouveau. La procédure définit un nouveau mot de passe ; elle ne révèle pas l'ancien. Consultez les instructions complètes dans [Obtenir un accès et se connecter](../end-user-and-partner-section/end-user-section/getting-access-and-signing-in.md).

Les comptes disposant du SSO ou d'une clé d'accès (passkey) peuvent utiliser cette autre méthode de connexion. Pour le SSO, la récupération du mot de passe relève du fournisseur d'identité. Voir [Authentification à deux facteurs](two-factor-authentication.md).

## Clés API DocBits

Les clés créées dans la **Gestion des clés API** ne sont affichées intégralement qu'une seule fois, lors de leur création. DocBits stocke un hachage à sens unique de la clé et un court préfixe d'identification. Le préfixe et les métadonnées restent visibles dans la liste de gestion ; la clé complète d'origine ne peut pas être récupérée à partir de son hachage.

Ni les administrateurs ni le support DocBits ne peuvent consulter la clé complète après sa création. Si une clé est perdue, révoquez-la et créez-en une nouvelle. Chaque clé peut avoir une date d'expiration et être révoquée séparément. Voir [Gestion des clés API](../administration-and-setup/settings/global-settings/integration/api-key-management.md).

## Informations de compte et identifiants des systèmes connectés

Les noms, adresses e-mail, rôles et états des comptes sont des informations que les administrateurs autorisés de l'organisation peuvent consulter et gérer. Elles sont distinctes du secret utilisé pour s'authentifier. Voir [Utilisateurs](../administration-and-setup/settings/global-settings/groups-users-and-permissions/users/README.md).

Les identifiants fournis pour les systèmes connectés, comme un compte de service ERP, une boîte mail ou un serveur SFTP, sont également distincts d'un mot de passe DocBits ou d'une clé API émise par DocBits. Un connecteur peut avoir besoin du secret utilisable pour s'authentifier auprès du système externe. Son stockage et ses contrôles d'accès doivent donc être évalués pour chaque connecteur.

L'impossibilité de retrouver un mot de passe ou une clé API DocBits stockée sous forme de hachage **ne signifie pas** que toutes les informations de compte ou tous les secrets d'intégration sont inaccessibles au fournisseur. Toute assurance concernant l'accès du personnel aux identifiants d'intégration nécessite la confirmation des contrôles d'accès opérationnels concernés.

## Chiffrement en transit

Les points d'accès publics DocBits ci-dessous prennent en charge **TLS 1.2 et TLS 1.3** sur HTTPS. Les vérifications du **16 octobre 2026** ont confirmé le rejet de TLS 1.0 et TLS 1.1.

| Point d'accès | Usage | Versions TLS vérifiées |
| --- | --- | --- |
| `app.docbits.com` | Application web | TLS 1.2 et TLS 1.3 |
| `auth.docbits.com` | Service d'authentification | TLS 1.2 et TLS 1.3 |
| `api.docbits.com` | API | TLS 1.2 et TLS 1.3 |

### Quels types de chiffrement sont pris en charge en transit ?

| Question | Réponse pour les points d'accès publics ci-dessus |
| --- | --- |
| TLS 1.1 est-il pris en charge ? | **Non.** Les connexions utilisant TLS 1.1 sont rejetées. |
| TLS 1.2 est-il pris en charge ? | **Oui.** |
| TLS 1.3 est-il pris en charge ? | **Oui.** |

Les méthodes suivantes ont été négociées avec succès sur **les trois points d'accès**, lors de tests avec validation des certificats le 16 octobre 2026 :

| Méthode de chiffrement | Longueur de la clé symétrique | Versions TLS vérifiées |
| --- | --- | --- |
| AES-128-GCM | 128 bits | TLS 1.2 et TLS 1.3 |
| AES-256-GCM | 256 bits | TLS 1.2 et TLS 1.3 |
| ChaCha20-Poly1305 | 256 bits | TLS 1.3 |

Ces méthodes assurent un chiffrement authentifié qui protège la confidentialité et l'intégrité des données en transit. La méthode négociée dépend des capacités et de la configuration du client et du serveur. Les longueurs indiquées concernent les clés symétriques de chiffrement des données, indépendamment de la taille des clés des certificats. Les suites cryptographiques TLS 1.2 testées utilisent ECDHE pour l'échange de clés éphémères.

Cette vérification couvre les connexions à ces points d'accès publics, y compris celles provenant de clients ou d'autres serveurs. Elle n'établit pas les paramètres de protocole ou de chiffrement de chaque connexion interne entre services, connexion à une base de données, point d'accès régional ou intégration externe. Ces connexions nécessitent une confirmation propre au déploiement et à l'intégration concernés.

## Chiffrement des informations de compte stockées

Le hachage des mots de passe et des clés API est une mesure distincte du chiffrement des bases de données, volumes de stockage, objets et sauvegardes. Les contrôles décrits ne démontrent pas que chaque nom d'utilisateur, champ de compte ou secret d'intégration est chiffré individuellement, ni que toutes les données stockées utilisent un algorithme de chiffrement particulier.

Pour une exigence portant sur toutes les informations des comptes clients, demandez à FELLOWPRO AG une déclaration propre au déploiement couvrant les espaces de stockage et sauvegardes concernés, les méthodes de chiffrement, la gestion des clés et l'accès du personnel. Un modèle d'hébergement cloud ou serverless ne suffit pas à établir ces propriétés.

## Répondre au questionnaire de sécurité d'un client

Le texte suivant décrit le périmètre confirmé :

> Les mots de passe de connexion DocBits sont stockés sous forme de hachages salés à sens unique. Les administrateurs et le support DocBits ne peuvent pas retrouver le mot de passe d'origine en clair à partir du hachage stocké. En cas d'oubli, l'utilisateur doit définir un nouveau mot de passe via la procédure de réinitialisation par e-mail pour se reconnecter par mot de passe. Le SSO ou les clés d'accès configurés offrent d'autres moyens de connexion.
>
> Les clés créées dans la Gestion des clés API DocBits ne sont affichées qu'une seule fois et sont stockées sous forme de hachages à sens unique. Ni les administrateurs ni le support DocBits ne peuvent récupérer la clé complète par la suite. Les clés perdues doivent être révoquées et remplacées.
>
> Les points d'accès publics de l'application web, de l'authentification et de l'API DocBits indiqués ci-dessus prennent en charge HTTPS avec TLS 1.2 et TLS 1.3 ; TLS 1.0 et TLS 1.1 ont été rejetés lors des vérifications du 16 octobre 2026. Les méthodes vérifiées sont AES-128-GCM avec 128 bits et AES-256-GCM avec 256 bits sous TLS 1.2 et TLS 1.3, ainsi que ChaCha20-Poly1305 avec 256 bits sous TLS 1.3. Cette déclaration couvre les connexions à ces points d'accès. Le chiffrement de toutes les informations de compte stockées et des sauvegardes, la protection de chaque connexion interne entre serveurs et l'accès du personnel aux identifiants d'intégrations tierces nécessitent une confirmation distincte pour le déploiement concerné.
