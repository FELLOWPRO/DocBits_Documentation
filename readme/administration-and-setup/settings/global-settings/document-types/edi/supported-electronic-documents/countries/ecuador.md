---
description: "Ecuador SRI possède des entrées génériques, 1.0.0, 1.1.0, 2.0.0 et 2.1.0. La retenue à la source est un type de document distinct."
---

# Équateur

Utilisez ce guide pour identifier la famille configurée et le périmètre des versions avant de tester un fichier source.

[Tous les pays et périmètre de prise en charge](../README.md)

## Vidéo explicative du pays

La narration localisée et les sous-titres WebVTT expliquent le choix du format, la configuration et les vérifications d’acceptation.

Cette visite en lecture seule montre la configuration existante du pays dans DocBits. Vérifiez la source utilisée et la version active, puis testez des factures, des avoirs et des exports représentatifs dans votre organisation.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/edocs_country_ecuador/v2/fr.mp4" %}

[Équateur — Vidéo explicative du pays](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/edocs_country_ecuador/v2/fr.mp4)

[WebVTT](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/edocs_country_ecuador/v2/fr.vtt)

## Variantes et limites de version

Ecuador SRI possède des entrées génériques, 1.0.0, 1.1.0, 2.0.0 et 2.1.0. La retenue à la source est un type de document distinct.

**Syntaxe:** XML

L’entrée de classification des avoirs ne possède pas d’ensemble d’extraction dédié dans l’état examiné. Vérifiez la correspondance effectivement utilisée et le type de document source.

Les tableaux consignent une vérification du catalogue de développement effectuée le 17 octobre 2026 et du code de traitement correspondant. Ils décrivent les règles et composants de configuration disponibles, sans certifier chaque fichier, exigence légale ou déploiement en production. Votre organisation peut remplacer les valeurs par défaut.

## Matrice des règles et composants examinés

| Libellé exact du format | Clé de document de la règle | Composants disponibles |
| --- | --- | --- |
| `ECUADOR SRI` | `CREDIT_NOTE` | C / — / — / — |
| `ECUADOR FACTURA ELECTRONICA` | `INVOICE` | C / T / P / E |
| `ECUADOR SRI` | `INVOICE` | C / T / P / E |
| `ECUADOR SRI 1.0.0` | `INVOICE` | C / T / P / E |
| `ECUADOR SRI 1.1.0` | `INVOICE` | C / T / P / E |
| `ECUADOR SRI 2.0.0` | `INVOICE` | C / T / P / E |
| `ECUADOR SRI 2.1.0` | `INVOICE` | C / T / P / E |
| `SRI RETENCION` | `WITHHOLDING` | C / T / P / E |

C = classification, T = Transformation, P = Preview, E = Extraction Paths. La clé de document sert à rechercher la règle ou la configuration ; elle ne garantit pas la valeur finale enregistrée de invoice_type. Une transformation peut classifier un avoir au moyen d’une correspondance INVOICE.

Un tiret signifie que la vérification de l’état n’a pas signalé de composant dédié pour cette combinaison exacte de format et de clé de document. Cela n’exclut pas une correspondance partagée ou de repli. Vérifiez le mécanisme de résolution effectivement utilisé et un fichier représentatif avant de vous appuyer sur ce chemin.

## Trouver la correspondance dans DocBits

<figure><img src="../../../../../../../.gitbook/assets/edocs-support-ecuador-fr.png" alt="Équateur: ECUADOR SRI 2.1.0"><figcaption><p>Interface réelle de développement : le format représentatif et ses composants de configuration disponibles. Les autres versions figurent dans la matrice.</p></figcaption></figure>

## Vérifications d’acceptation

La vérification d’un composant confirme la présence d’une configuration. Ce n’est pas un test de traitement de bout en bout pour chaque version. Testez le contenu exact et le chemin de traitement de facture ou d’avoir requis par votre intégration.

## Vérifier un format dans votre organisation

1. Conservez le XML d’origine ou le PDF avec son XML intégré. Relevez l’espace de noms, le schéma ou l’identifiant de personnalisation, ainsi que la version et le profil déclarés.

2. Ouvrez Paramètres → Types de documents → E-Doc pour le document métier concerné. Recherchez le format exact de document électronique indiqué dans le guide.

3. Vérifiez la source Default ou Custom effectivement utilisée et sa version de configuration active. Examinez Transformation, Preview et Extraction Paths. Enregistrer un brouillon ne l’active pas.

4. Testez des fichiers source représentatifs pour chaque syntaxe, version et document métier dont vous avez besoin. Vérifiez les champs clés, les montants, les taxes, la classification facture/avoir et l’export ERP.

5. Confirmez séparément la politique de validation et le transport. Préservez les correspondances personnalisées et vérifiez les approbations ainsi que l’historique des exports avant de relancer des documents existants.

## Référence de format associée

- [🇪🇨 Ecuador SRI](../ecuador-sri.md)
