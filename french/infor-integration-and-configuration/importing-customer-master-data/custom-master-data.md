---
description: Comment importer des données de base directement dans DocBits.
---

# Données de base personnalisées

#### Activer les données de base personnalisées <a href="#activating-custom-master-data" id="activating-custom-master-data"></a>

Depuis le tableau de bord, accédez à Settings → Document Processing → Module.

![](<../../.gitbook/assets/DocBits_CMD_1 (1).png>)

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_2.png" alt="" width="375"><figcaption></figcaption></figure></div>

Dans Module, activez Custom Master Data en cliquant sur le curseur, comme illustré ci-dessous.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_3.png" alt="" width="375"><figcaption></figcaption></figure></div>

#### Aperçu de la fonctionnalité <a href="#feature-overview" id="feature-overview"></a>

Pour ajouter vos propres données de base dans DocBits, accédez à Master Data Lookup dans Settings.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_4.png" alt="" width="375"><figcaption></figcaption></figure></div>

Cliquez sur « Custom Master Data ».

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_5.png" alt="" width="375"><figcaption></figcaption></figure></div>

Vous pouvez ensuite choisir de créer un Template ou un Endpoint.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_6.png" alt="" width="375"><figcaption></figcaption></figure></div>

#### Créer un Template <a href="#create-a-template" id="create-a-template"></a>

La première étape consiste à choisir entre utiliser le fichier API ION de votre organisation ou utiliser OAuth2 et saisir les données nécessaires.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_7.png" alt="" width="375"><figcaption></figcaption></figure></div>

Nous allons ensuite configurer les préréglages. Vous y saisirez le nom de la table de données de base et l'URL de l'appel d'API.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_8.png" alt="" width="375"><figcaption></figcaption></figure></div>

Vous devrez ensuite saisir le chemin JSON en notation pointée ; pour plus d'informations sur la notation pointée, cliquez [ici](https://docs.hevodata.com/sources/engg-analytics/streaming/rest-api/writing-jsonpath-expressions/).

Enfin, vous devrez mapper les données vers les colonnes que vous souhaitez créer, comme dans l'exemple ci-dessous.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_9.png" alt="" width="375"><figcaption></figcaption></figure></div>

Cela fait, cliquez sur Done pour que vos nouvelles données de base soient créées et alimentées.

#### Créer un Endpoint <a href="#create-an-endpoint" id="create-an-endpoint"></a>

La première étape consiste à choisir entre utiliser le fichier API ION de votre organisation, utiliser OAuth2, ou laisser ce champ vide et saisir les données nécessaires.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_10.png" alt="" width="375"><figcaption></figcaption></figure></div>

Nous allons ensuite configurer les préréglages. Vous y saisirez le nom de la table de données de base et l'URL de l'appel d'API.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_8.png" alt="" width="375"><figcaption></figcaption></figure></div>

Vous devrez ensuite saisir le chemin JSON en notation pointée ; pour plus d'informations sur la notation pointée, cliquez [ici](https://docs.hevodata.com/sources/engg-analytics/streaming/rest-api/writing-jsonpath-expressions/).

Enfin, vous devrez mapper les données vers les colonnes que vous souhaitez créer, comme dans l'exemple ci-dessous.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_9.png" alt="" width="375"><figcaption></figcaption></figure></div>

Cela fait, cliquez sur Done pour que vos nouvelles données de base soient créées et alimentées.
