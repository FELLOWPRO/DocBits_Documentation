---
description: "Chile DTE possède des entrées de facture, d’avoir et de guide d’expédition."
---

# Chili

Utilisez ce guide pour identifier la famille configurée et le périmètre des versions avant de tester un fichier source.

[Tous les pays et périmètre de prise en charge](../README.md)

## Vidéo explicative du pays

La narration localisée et les sous-titres WebVTT expliquent le choix du format, la configuration et les vérifications d’acceptation.

Cette visite en lecture seule montre la configuration existante du pays dans DocBits. Vérifiez la source utilisée et la version active, puis testez des factures, des avoirs et des exports représentatifs dans votre organisation.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/edocs_country_chile/v2/fr.mp4" %}

[Chili — Vidéo explicative du pays](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/edocs_country_chile/v2/fr.mp4)

[WebVTT](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/edocs_country_chile/v2/fr.vtt)

## Variantes et limites de version

Chile DTE possède des entrées de facture, d’avoir et de guide d’expédition.

**Syntaxe:** XML

Sélectionnez le type de document métier avant de vérifier les champs. La facture, l’avoir et les informations de livraison utilisent des correspondances différentes.

Les tableaux consignent une vérification du catalogue de développement effectuée le 17 octobre 2026 et du code de traitement correspondant. Ils décrivent les règles et composants de configuration disponibles, sans certifier chaque fichier, exigence légale ou déploiement en production. Votre organisation peut remplacer les valeurs par défaut.

## Matrice des règles et composants examinés

| Libellé exact du format | Clé de document de la règle | Composants disponibles |
| --- | --- | --- |
| `CHILE DTE FACTURA` | `INVOICE` | C / T / P / E |
| `CHILE DTE GUIA DESPACHO` | `DELIVERY_NOTE` | C / T / P / E |
| `CHILE DTE NOTA CREDITO` | `CREDIT_NOTE` | C / T / P / E |

C = classification, T = Transformation, P = Preview, E = Extraction Paths. La clé de document sert à rechercher la règle ou la configuration ; elle ne garantit pas la valeur finale enregistrée de invoice_type. Une transformation peut classifier un avoir au moyen d’une correspondance INVOICE.

Un tiret signifie que la vérification de l’état n’a pas signalé de composant dédié pour cette combinaison exacte de format et de clé de document. Cela n’exclut pas une correspondance partagée ou de repli. Vérifiez le mécanisme de résolution effectivement utilisé et un fichier représentatif avant de vous appuyer sur ce chemin.

### Libellés de configuration supplémentaires

Ces libellés possèdent des entrées de configuration, mais aucune règle de classification autonome dans le catalogue examiné. Une famille générique ou une identification plus précise peut sélectionner un chemin compatible. Leur seule présence ne prouve pas la détection automatique de cette publication ou de ce profil.

- `CHILE DTE`
- `CHILE FACTURA ELECTRONICA`

## Trouver la correspondance dans DocBits

<figure><img src="../../../../../../../.gitbook/assets/edocs-support-chile-fr.png" alt="Chili: CHILE DTE FACTURA"><figcaption><p>Interface réelle de développement : le format représentatif et ses composants de configuration disponibles. Les autres versions figurent dans la matrice.</p></figcaption></figure>

## Vérifications d’acceptation

La vérification d’un composant confirme la présence d’une configuration. Ce n’est pas un test de traitement de bout en bout pour chaque version. Testez le contenu exact et le chemin de traitement de facture ou d’avoir requis par votre intégration.

## Vérifier un format dans votre organisation

1. Conservez le XML d’origine ou le PDF avec son XML intégré. Relevez l’espace de noms, le schéma ou l’identifiant de personnalisation, ainsi que la version et le profil déclarés.

2. Ouvrez Paramètres → Types de documents → E-Doc pour le document métier concerné. Recherchez le format exact de document électronique indiqué dans le guide.

3. Vérifiez la source Default ou Custom effectivement utilisée et sa version de configuration active. Examinez Transformation, Preview et Extraction Paths. Enregistrer un brouillon ne l’active pas.

4. Testez des fichiers source représentatifs pour chaque syntaxe, version et document métier dont vous avez besoin. Vérifiez les champs clés, les montants, les taxes, la classification facture/avoir et l’export ERP.

5. Confirmez séparément la politique de validation et le transport. Préservez les correspondances personnalisées et vérifiez les approbations ainsi que l’historique des exports avant de relancer des documents existants.

## Référence de format associée

- [🇨🇱 CHILE DTE](../chile-dte.md)
