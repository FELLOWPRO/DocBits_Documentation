---
description: Chiffrement au repos de DocBits sur DigitalOcean, avec bases de données, Spaces, couverture des sauvegardes et question 4.8.
---

# Chiffrement au repos

DocBits utilise DigitalOcean Managed Databases et DigitalOcean Spaces. La vérification du **16 octobre 2026** a confirmé des services gérés PostgreSQL, OpenSearch et Valkey pour la production de l’UE à Francfort. La [FAQ Sécurité et conformité](security-and-compliance-faq.md) documente l’utilisation de Spaces pour le stockage.

Cette page décrit les mesures de chiffrement publiées par DigitalOcean pour ces services. Les installations sur site et les copies stockées dans d’autres systèmes nécessitent leur propre évaluation.

## Méthodes de chiffrement et périmètre

| Service de stockage | Chiffrement au repos | Couverture |
| --- | --- | --- |
| Managed Databases : PostgreSQL, OpenSearch, Valkey | Chiffrement intégral des volumes par LUKS ; `aes-xts-plain64:sha256` avec 512 bits de matériel de clé XTS | Les volumes sous-jacents du service de base de données, y compris les données qui y sont stockées. Cette protection au niveau du stockage ne signifie pas que chaque champ est chiffré séparément. |
| Sauvegardes de Managed Databases | AES-256 en mode CTR, avec HMAC-SHA256 pour l’intégrité ; clés par fichier protégées par RSA-3072 | Sauvegardes créées par le service de base de données gérée. Les exports et copies supplémentaires nécessitent une vérification distincte. |
| DigitalOcean Spaces | Chiffrement intégral des disques par AES-XTS 256 bits | Données sur les disques physiques de stockage. Cette mesure est distincte du chiffrement facultatif par objet ou côté client. |
| DigitalOcean Volumes, lorsqu’ils sont utilisés | Chiffrement LUKS du cluster de stockage | Données sur ces volumes de stockage en blocs ; les instantanés de volume héritent du chiffrement. |

XTS utilise deux clés AES. Les 512 bits de matériel de clé XTS combiné du service de base de données gérée correspondent à deux clés AES de 256 bits (AES-256-XTS), et non à un chiffrement AES avec une clé de 512 bits.

Les informations sur les bases de données et les sauvegardes proviennent du [modèle de sécurité de Managed Databases](https://www.digitalocean.com/security/shared-responsibility-model-managed-databases). Le [modèle de sécurité de Spaces](https://www.digitalocean.com/security/shared-responsibility-model-spaces) confirme le chiffrement au repos ; le [modèle de sécurité d’App Platform](https://www.digitalocean.com/security/shared-responsibility-model-app-platform) précise l’utilisation d’AES-XTS 256 bits pour les disques physiques de Spaces. Les [fonctionnalités de Volumes](https://docs.digitalocean.com/products/volumes/details/features/) décrivent la couverture des volumes et instantanés.

## Gestion des clés et accès autorisés

DigitalOcean gère le chiffrement d’infrastructure décrit ci-dessus. Pour Managed Databases, le fournisseur documente une clé aléatoire par instance et volume, supprimée à la destruction de l’instance. Les sauvegardes de bases de données gérées utilisent une clé aléatoire par fichier, protégée par une paire de clés RSA propre au service.

Le chiffrement du stockage protège les données sur les supports. Les applications et utilisateurs autorisés de la base de données peuvent toujours lire les données via le service. Cela ne démontre ni que le personnel du fournisseur ne peut accéder aux informations de compte, ni que chaque champ est chiffré au niveau applicatif. Le hachage des mots de passe et des clés API constitue une mesure distincte ; voir [Stockage sécurisé des identifiants](secure-storage-of-credentials.md).

Spaces prend également en charge [SSE-C avec des clés fournies par le client](https://docs.digitalocean.com/products/spaces/reference/s3-compatibility/). Cette possibilité facultative ne prouve pas que DocBits utilise SSE-C ou des clés de chiffrement gérées par le client.

## Couverture des sauvegardes

Les sauvegardes de bases de données gérées, les instantanés de volumes et les sauvegardes d’images de Droplets sont des produits différents. Les [limites des sauvegardes de Droplets](https://docs.digitalocean.com/products/backups/details/limits/) indiquent que ces sauvegardes d’images ne sont pas chiffrées au repos. Cette vérification n’a pas établi que DocBits utilise ce produit de sauvegarde.

Les mesures ci-dessus permettent donc une déclaration limitée aux services nommés. Les dumps de bases de données, fichiers exportés, archives à long terme et copies de reprise après sinistre supplémentaires nécessitent de confirmer la destination de stockage, le chiffrement et la gestion des clés avant d’étendre la garantie à toutes les copies. Un calendrier de sauvegarde ou une architecture cloud/serverless ne suffit pas à établir cette couverture.

## 4.8 — Types de chiffrement au repos

Le texte suivant peut être utilisé pour le périmètre documenté :

> DocBits utilise DigitalOcean Managed Databases et Spaces. Les données des bases de données gérées sont chiffrées au repos au niveau des volumes complets avec LUKS et AES-256-XTS (512 bits de matériel de clé XTS combiné). Les sauvegardes de ces bases utilisent AES-256-CTR avec HMAC-SHA256 pour l’intégrité et RSA-3072 pour protéger les clés de chiffrement propres à chaque fichier. Spaces applique un chiffrement intégral des disques par AES-XTS 256 bits sur son stockage physique.
>
> Ces mesures au niveau du stockage couvrent les données des volumes et disques protégés ; elles n’impliquent pas un chiffrement séparé de chaque champ de la base de données. DigitalOcean gère les clés de chiffrement d’infrastructure. Cette déclaration couvre les services gérés nommés. Le chiffrement et la gestion des clés des exports, archives et copies de sauvegarde supplémentaires nécessitent une confirmation distincte pour le déploiement concerné.
