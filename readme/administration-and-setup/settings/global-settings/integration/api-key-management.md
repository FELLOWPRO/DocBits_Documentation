---
description: >-
  Comment trouver et créer les clés API qui donnent à d'autres systèmes l'accès à
  DocBits
---

# API Key Management

Une API key permet à un autre système — votre ERP, un script ou une application partenaire — de dialoguer avec DocBits sans qu'un utilisateur se connecte. Votre organisation peut détenir autant de clés que nécessaire, et chacune se gère séparément : donnez-lui son propre nom, décidez si elle expire, et révoquez-la individuellement si elle venait à être exposée.

Comme chaque intégration peut avoir sa propre clé, vous pouvez en désactiver une sans perturber les autres.

## Ouvrir la gestion des clés API

Allez dans **Settings** et sélectionnez **Integration & SSO** sous **System & Administration**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/api-key-settings-overview.png)

La section **API Key** en haut de la page liste toutes les clés que possède votre organisation.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/api-key-list.png)

## Comprendre la liste

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/api-key-list-row.png)

| Colonne | Ce qu'elle vous indique |
| --- | --- |
| **Key** | Les premiers caractères de la clé, suivis de `****`. Le reste n'est plus jamais affiché après la création — voir [Créer une clé API](#creer-une-cle-api). |
| **Name** | Le nom que vous avez donné à la clé, avec sa description en dessous. |
| **Expires** | La date à laquelle la clé cesse de fonctionner, ou **Never** si vous n'en avez pas défini. |
| **Last Used** | Quand une requête est arrivée pour la dernière fois avec cette clé. **Never used** signifie qu'aucun système ne l'a encore utilisée — utile pour repérer les clés que vous pouvez retirer sans risque. |
| **Status** | **Active** signifie que la clé fonctionne. Une clé révoquée est désactivée définitivement. |
| **Actions** | Le menu à trois points, où vous pouvez révoquer la clé. |

Si vous avez plus de clés qu'il n'en tient sur une page, utilisez les commandes de pagination au bas de la liste.

{% hint style="info" %}
**Last Used** est le moyen le plus rapide de trouver les clés dont plus personne n'a besoin. Une clé qui n'a jamais servi, ou qui n'a pas servi depuis des mois, est une bonne candidate à la révocation.
{% endhint %}

## Créer une clé API

1. Cliquez sur **+ Create API Key** en haut à droite de la section API Keys.
2. Remplissez la boîte de dialogue :

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/api-key-create-dialog.png)

| Champ | Ce qu'il faut saisir |
| --- | --- |
| **Key Name** | Obligatoire. Nommez-la d'après le système qui l'utilisera — `M3 Production`, `Invoice Import Script` — pour pouvoir savoir plus tard à quelle intégration une clé appartient. |
| **Description** | Facultatif. De la place pour une note sur l'usage de la clé ou sur qui l'a mise en place. |
| **Expiration** | Choisissez une date d'expiration, ou laissez **Never expires**. Une date d'expiration est le choix le plus sûr : la clé se retire d'elle-même si l'intégration venait à être oubliée. |

3. Cliquez sur **Create**. DocBits vous montre la nouvelle clé :

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/api-key-created.png)

4. Copiez la clé à l'aide de l'icône de copie et collez-la directement dans le système qui l'utilisera, ou dans votre gestionnaire de mots de passe.
5. Cochez **I have copied and saved this key** et cliquez sur **Done**.

{% hint style="danger" %}
**La clé complète n'est affichée qu'une seule fois.** DocBits la stocke sous une forme chiffrée qui ne peut pas être ramenée à l'original : personne — ni vos administrateurs, ni le support DocBits — ne peut la retrouver ensuite. Si vous la perdez, révoquez la clé et créez-en une nouvelle.
{% endhint %}

Traitez la clé comme un mot de passe. Quiconque la détient peut agir sur les documents et les données de votre organisation.
