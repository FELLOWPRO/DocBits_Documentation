# Accès SQL

<figure><img src="../../.gitbook/assets/sql_direct_access_settings.png" alt="Paramètres d'accès SQL direct"><figcaption></figcaption></figure>

## Aperçu

Dans le module des paramètres de DocBits, les administrateurs peuvent accéder directement à la base de données BI à l'aide de SQL. Cette fonctionnalité est destinée à la gestion avancée des données et aux besoins de reporting personnalisés.

### Accéder à l'accès SQL direct

Accédez à la section SQL Direct Access dans le module des paramètres. Vous y trouverez les identifiants et les informations d'accès, notamment le nom d'utilisateur, le mot de passe, le nom de la base de données et les informations sur l'hôte.

* **Nom d'utilisateur :** user\_23f3d6
* **Mot de passe :** _Chiffré_
* **Base de données :** demo
* **Hôte :** voir la capture d'écran

## **Exemple de détails d'accès :**

```sql
SELECT
    COUNT(*),
    status,
    invoice_type
FROM dashboard
GROUP BY
    status,
    invoice_type

```

#### Résultats d'une requête d'exemple

Les résultats suivants affichent le nombre de documents par statut et par type de facture :

* **Ready for Validation :** 71 factures, 6 non spécifiés
* **Pending Confirmation :** 1 non spécifié
* **Finished :** 3 non spécifiés, 1 facture
* **Error :** 2 non spécifiés

#### Utiliser clickhouse-client pour l'accès par terminal

Pour les développeurs qui préfèrent utiliser le terminal, l'accès peut être établi via `clickhouse-client` :

```bash
clickhouse-client --host <hostname_or_ip> --port <port> --user <username> --password <your_password> --database <database_name>

```

### Créer des vues matérialisées

Nous recommandons de créer des vues matérialisées pour précalculer les données et améliorer les performances dans les outils d'analyse tels que PowerBI :

```sql
SELECT toStartOfWeek(created_on) as week_start, sum(toFloat64OrZero(field_value)) as total_sum
FROM document_extracted_data
WHERE field_name = 'total_amount'
GROUP BY week_start

```

Cet exemple montre comment regrouper les montants totaux par semaine de création, ce qui est utile pour les synthèses financières hebdomadaires ou les pistes d'audit.

## Ressources supplémentaires

Pour obtenir de l'aide ou des configurations avancées, veuillez contacter notre équipe d'assistance ou consulter notre formation vidéo complète disponible dans la section d'aide.
