---
description: "e-SLOG 1.6 et 2.0 possèdent des entrées distinctes."
---

# Slovénie

Utilisez ce guide pour identifier la famille configurée et le périmètre des versions avant de tester un fichier source.

[Tous les pays et périmètre de prise en charge](../README.md)

## Variantes et limites de version

e-SLOG 1.6 et 2.0 possèdent des entrées distinctes.

**Syntaxe:** XML

Les deux versions ont des structures XML différentes. Faites correspondre le schéma source au lieu de choisir une règle d’après le nom du fichier.

Les tableaux consignent une vérification du catalogue de développement effectuée le 17 octobre 2026 et du code de traitement correspondant. Ils décrivent les règles et composants de configuration disponibles, sans certifier chaque fichier, exigence légale ou déploiement en production. Votre organisation peut remplacer les valeurs par défaut.

## Matrice des règles et composants examinés

| Libellé exact du format | Clé de document de la règle | Composants disponibles |
| --- | --- | --- |
| `E-SLOG 1.6` | `INVOICE` | C / T / P / E |
| `E-SLOG 2.0` | `INVOICE` | C / T / P / E |

C = classification, T = Transformation, P = Preview, E = Extraction Paths. La clé de document sert à rechercher la règle ou la configuration ; elle ne garantit pas la valeur finale enregistrée de invoice_type. Une transformation peut classifier un avoir au moyen d’une correspondance INVOICE.

Un tiret signifie que la vérification de l’état n’a pas signalé de composant dédié pour cette combinaison exacte de format et de clé de document. Cela n’exclut pas une correspondance partagée ou de repli. Vérifiez le mécanisme de résolution effectivement utilisé et un fichier représentatif avant de vous appuyer sur ce chemin.

## Trouver la correspondance dans DocBits

<figure><img src="../../../../../../../.gitbook/assets/edocs-support-slovenia-fr.png" alt="Slovénie: E-SLOG 2.0"><figcaption><p>Interface réelle de développement : le format représentatif et ses composants de configuration disponibles. Les autres versions figurent dans la matrice.</p></figcaption></figure>

## Vidéo explicative du pays

La narration localisée et les sous-titres WebVTT expliquent le choix du format, la configuration et les vérifications d’acceptation.

{% file src="../../../../../../../.gitbook/assets/edocs-support-slovenia-fr.mp4" %}
Slovénie — Vidéo explicative du pays
{% endfile %}

{% file src="../../../../../../../.gitbook/assets/edocs-support-slovenia-fr.vtt" %}
WebVTT
{% endfile %}

## Vérifications d’acceptation

La vérification d’un composant confirme la présence d’une configuration. Ce n’est pas un test de traitement de bout en bout pour chaque version. Testez le contenu exact et le chemin de traitement de facture ou d’avoir requis par votre intégration.

## Vérifier un format dans votre organisation

1. Conservez le XML d’origine ou le PDF avec son XML intégré. Relevez l’espace de noms, le schéma ou l’identifiant de personnalisation, ainsi que la version et le profil déclarés.

2. Ouvrez Paramètres → Types de documents → E-Doc pour le document métier concerné. Recherchez le format exact de document électronique indiqué dans le guide.

3. Vérifiez la source Default ou Custom effectivement utilisée et sa version de configuration active. Examinez Transformation, Preview et Extraction Paths. Enregistrer un brouillon ne l’active pas.

4. Testez des fichiers source représentatifs pour chaque syntaxe, version et document métier dont vous avez besoin. Vérifiez les champs clés, les montants, les taxes, la classification facture/avoir et l’export ERP.

5. Confirmez séparément la politique de validation et le transport. Préservez les correspondances personnalisées et vérifiez les approbations ainsi que l’historique des exports avant de relancer des documents existants.
