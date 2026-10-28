# Stockage, conservation et suppression des données

Vos données sont entre de bonnes mains avec DocBits. Nous exploitons DocBits dans deux régions, **Frankfurt am Main (UE)** et **San Francisco (États-Unis)**, et vous décidez dans vos paramètres combien de temps les documents restent chez nous. Cette page présente les lieux de stockage, les durées de conservation et la suppression.

**Documentation à jour au : 28 octobre 2026.**

## En un coup d’œil

- **Vous choisissez la région :** Frankfurt pour les clients de l’UE, San Francisco pour les clients américains.
- **Vos données restent dans votre région.** Les données de l’UE sont hébergées à Frankfurt, celles des États-Unis à San Francisco. Il n’y a aucun mélange de données entre les régions.
- **Vous contrôlez la durée de conservation de vos documents** sous **Traitement des documents → Expiration des documents** ([accéder au paramètre](../administration-and-setup/settings/document-processing/documents-expiry.md)).
- **Les fichiers OCR temporaires** sont supprimés automatiquement après 90 minutes.
- **Nous sommes là pour vous aider :** notre équipe répond à vos questions et à vos demandes de suppression à l’adresse **compliance@fellowpro.com**.

## Où vos données sont-elles stockées ?

| Région | Pour qui | Emplacement | Services utilisés |
| --- | --- | --- | --- |
| **UE** | Tous les clients de l’UE | **Frankfurt am Main, Allemagne** | DigitalOcean Kubernetes (région `fra1`) avec des bases de données gérées PostgreSQL, OpenSearch et Valkey (`fra1`), ainsi que DigitalOcean Spaces pour le stockage de fichiers |
| **États-Unis** | Clients américains | **San Francisco, États-Unis** | DigitalOcean Kubernetes (région `sfo2`) avec des bases de données gérées PostgreSQL, OpenSearch et Valkey (`sfo2`) |

**Sauvegardes dans l’UE :** Frankfurt est le site de sauvegarde principal et Amsterdam (Pays-Bas) le site secondaire, de sorte que vos copies de sauvegarde restent elles aussi au sein de l’UE.

**Systèmes connectés :** si vous exportez des documents vers votre ERP, Infor IDM ou un autre système cible, ces copies sont stockées dans ce système, selon ses règles et à son emplacement. Cela reste entièrement entre vos mains.

## Combien de temps les données sont-elles conservées ?

| Type de données | Conservation |
| --- | --- |
| **Documents importés et données extraites** | Contrôlée par vous via [Expiration des documents](../administration-and-setup/settings/document-processing/documents-expiry.md) (voir ci-dessous). |
| **Fichiers OCR temporaires** | Nettoyage automatique après **90 minutes**. Cela concerne uniquement le stockage OCR temporaire, pas votre document dans DocBits. |
| **Journaux accessibles aux clients** (consultables sous [Journal d’activité](../administration-and-setup/settings/log-settings/README.md)) | **30 jours** |
| **Journaux internes** | **3 mois** |
| **Sauvegardes quotidiennes de la base de données (gérées)** | **7 jours** ; les sauvegardes plus anciennes sont supprimées automatiquement. |
| **Sauvegardes quotidiennes supplémentaires (SnapShooter)** | Pour les bases de données de production et de sandbox ; la durée de conservation est définie par environnement. |
| **Cookies et stockage du navigateur** | Variable selon la finalité, voir [Cookies et stockage du navigateur](cookies-and-browser-storage.md). |

Nous effectuons également des sauvegardes quotidiennes, hebdomadaires, trimestrielles et annuelles. Sur demande, nous vous communiquons volontiers les durées de conservation exactes de ces types de sauvegarde pour votre environnement.

## Comment définir la durée de conservation de vos documents

Dans les paramètres, ouvrez **Traitement des documents → Expiration des documents**. Deux réglages sont disponibles :

- **Delete document after :** pendant combien de temps les documents sont conservés.
- **Delete finished document after :** pendant combien de temps les documents terminés, entièrement traités et exportés, sont conservés.

Les options sont **Default**, **48 Hours**, **1 Week**, **2 Weeks** et **4 Weeks**. **Default** applique la valeur par défaut du système. Si vous souhaitez une durée fixe, choisissez simplement l’une des durées proposées. Vous trouverez tous les détails dans le [guide Expiration des documents](../administration-and-setup/settings/document-processing/documents-expiry.md).

## Que se passe-t-il lorsque des données sont supprimées ?

Expiration des documents supprime automatiquement vos documents à l’issue de la période que vous avez choisie. Cela est indépendant du nettoyage des fichiers OCR temporaires, de l’expiration des journaux et de la conservation des sauvegardes.

Bon à savoir :

- **Les sauvegardes expirent selon leur propre calendrier.** La suppression d’un document dans le système actif n’efface donc pas immédiatement les copies de sauvegarde, mais seulement à la fin de la période de sauvegarde correspondante.
- **Les copies exportées vous appartiennent.** Lorsque DocBits supprime un document, la copie présente dans votre ERP ou votre archive reste en place. Prévoyez la conservation à cet endroit en fonction de vos propres exigences.

## Des questions ou des demandes de suppression ? Nous sommes là pour vous

Pour des informations sur votre déploiement ou pour une demande de suppression, écrivez-nous à **compliance@fellowpro.com**. Merci d’indiquer votre organisation, l’environnement concerné, le type de données et le périmètre souhaité. Merci de ne pas envoyer de mots de passe ni de clés API.

Nous nous ferons également un plaisir de vous confirmer :

- Votre région active et vos paramètres de conservation effectifs, y compris la valeur par défaut du système.
- Le moment où le délai de suppression commence et la fréquence des nettoyages.
- Le périmètre de suppression pour les documents, les données extraites, les index de recherche et les données dérivées.
- Les emplacements et les durées de conservation de tous les types de sauvegarde, y compris après la fin du contrat.

## Plus d’informations sur la sécurité

- [DocBits (FELLOWPRO AG) — Questionnaire de Sécurité et Conformité](security-and-compliance-faq.md)
- [Chiffrement au repos](encryption-at-rest.md)
- [Stockage sécurisé des identifiants](secure-storage-of-credentials.md)
- [Cookies et stockage du navigateur](cookies-and-browser-storage.md)
