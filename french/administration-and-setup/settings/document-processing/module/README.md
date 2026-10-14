# Module

<figure><img src="../../../../.gitbook/assets/module_settings.png" alt="Paramètres Module"><figcaption><p>Page des paramètres Module</p></figcaption></figure>

La page Module vous permet d'activer ou de désactiver des fonctionnalités optionnelles dans DocBits. Chaque section regroupe des modules apparentés qui peuvent être activés ou désactivés.

## Purchase Order

Paramètres de PO Matching et de validation.

| Paramètre | Description |
|---------|-------------|
| **Auto Export if PO matched 100%** | Exporte automatiquement le document lorsque le rapprochement avec le bon de commande atteint 100 %. |
| **PO Dashboard** | Active le tableau de bord des bons de commande. Comprend un champ **PO Date Limit** pour restreindre les données de bons de commande par date. |
| **PO Shipment Order** | Active le traitement des ordres d'expédition liés aux bons de commande. |
| **Shipment Order Dashboard** | Active un tableau de bord dédié aux ordres d'expédition. |

## Auto Accounting

| Paramètre | Description |
|---------|-------------|
| **Auto Accounting** | Active la comptabilisation automatique des documents. Sélectionnez le type d'ERP (p. ex. LN, M3). |

## Dashboards

| Paramètre | Description |
|---------|-------------|
| **Advance Shipment Dashboard** | Tableau de bord pour le suivi des activités d'expédition avancées. |
| **Invoice Dashboard** | Tableau de bord pour le suivi et l'analyse des factures. |
| **Full Text Search** | Active la recherche en texte intégral dans les documents. |
| **Analytics Dashboard** | Active le tableau de bord de présentation des analyses. |

## Database Access

| Paramètre | Description |
|---------|-------------|
| **DB Access** | Active l'accès direct à la base de données pour l'organisation. |

## AI Dashboard

| Paramètre | Description |
|---------|-------------|
| **AI Document Warehouse** | Analyses de l'entrepôt de documents basées sur l'IA. |
| **Dashboard v2** | Tableau de bord mis à jour avec des fonctionnalités améliorées. |
| **Clickhouse Direct Access** | Active l'accès direct à la base de données Clickhouse. |
| **Supplier Statistics** | Active les statistiques et les rapports au niveau des fournisseurs. |

## Shipping & Supplier

| Paramètre | Description |
|---------|-------------|
| **Supplier Portal** | Active le portail fournisseurs pour la collaboration avec les fournisseurs. |

## Document Type

| Paramètre | Description |
|---------|-------------|
| **Workflow Builder** | Permet de créer et de personnaliser les workflows de traitement des documents. |
| **Annotation Mode** | Permet aux utilisateurs d'annoter les documents dans la vue de validation. |
| **Show Report** | Active la génération de rapports pour les documents. |
| **Inbound Emails** | Active la gestion des e-mails entrants par type de document. |
| **Models & Labels** | Gère les modèles d'IA et les libellés pour la reconnaissance des documents. |
| **Document Script** | Active les scripts personnalisés pour le traitement des documents. |
| **Document Scan** | Active la fonctionnalité de numérisation de documents. |
| **Bar-Code/QR Code Extraction** | Extrait les données des codes-barres/codes QR des documents. Sélectionnez les types de codes pris en charge. |
| **Custom Master Data** | Active les champs de données de base personnalisés. |
| **Tasks & Notifications** | Active les fonctionnalités de gestion des tâches et de notification. Comprend l'option **Dashboard Tasks Count**. |
| **DocBits Operator** | Active la fonctionnalité d'automatisation du navigateur DocBits Operator. |
| **DocNet** | Active la mise en réseau de documents DocNet. |
| **IDM ACL Updater** | Met à jour les listes de contrôle d'accès d'Infor Document Management. Téléversez un fichier ION-Mapping et configurez les correspondances entre Infor-Doctype et ACL. |
| **Barcode Assignment** | Active l'affectation de codes-barres aux documents. |
| **Set Negative Sign For Credit Notes** | Applique automatiquement le signe négatif aux montants des avoirs. |

## BOD Connection Stream

| Paramètre | Description |
|---------|-------------|
| **BOD Connection Stream** | Active l'intégration BOD (Business Object Document). Affiche le **Stream Name** utilisé pour la connexion. |

## Analytics

| Paramètre | Description |
|---------|-------------|
| **Use PostgreSQL for Quality Analytics** | Permet de basculer entre Prometheus (temps réel, réinitialisé à chaque déploiement) et PostgreSQL (persistant sur 90 jours, analyse des tendances, champs les moins performants). |

## Vertex Tax Integration

| Paramètre | Description |
|---------|-------------|
| **Vertex Tax Integration** | Active le calcul des taxes Vertex. Configurez **Base URL**, **Client ID** et **Client Secret**. Utilisez **Test Connection** pour vérifier. |
