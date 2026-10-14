# Integration & SSO

<figure><img src="../../../../.gitbook/assets/integration_sso.png" alt="Integration & SSO"><figcaption><p>Page Integration & SSO</p></figcaption></figure>

La page Integration & SSO permet de gérer les clés d'API pour l'accès programmatique, les identifiants d'organisation et la configuration de l'authentification unique (SSO).

## API Key

Gérez les clés d'API utilisées pour l'accès programmatique à DocBits.

| Colonne | Description |
|--------|-------------|
| **Key** | La valeur masquée de la clé d'API. Cliquez sur l'icône de copie pour copier la clé complète. |
| **Name** | Un nom descriptif pour la clé. |
| **Expires** | Date d'expiration (ou « Never »). |
| **Last Used** | Date de dernière utilisation de la clé. |
| **Status** | Active ou Inactive. |
| **Actions** | Menu à trois points pour révoquer ou supprimer. |

Cliquez sur **+ Create API Key** pour générer une nouvelle clé.

## ID

Affiche les identifiants de votre organisation :

| Champ | Description |
|-------|-------------|
| **Org ID** | L'identifiant unique de votre organisation. |
| **Sub Org ID** | L'identifiant de la sous-organisation actuellement sélectionnée. |

## SSO Service Provider Settings

Valeurs de configuration SSO de DocBits nécessaires pour configurer votre fournisseur d'identité (Identity Provider) :

| Champ | Description |
|-------|-------------|
| **Entity ID** | L'URL des métadonnées SAML de DocBits. |
| **SLO URL** | URL de déconnexion unique (Single Logout). |
| **SSO URL** | URL de l'Assertion Consumer Service. |

Vous pouvez également utiliser **Download Certificate** et **Download Metadata** pour la configuration de votre IdP.

## Identity Service Provider Settings

Configurez votre fournisseur d'identité (IdP) externe :

| Champ | Description |
|-------|-------------|
| **Tenant ID** | L'identifiant de tenant de votre IdP. |
| **Upload file** | Téléversez le fichier XML de métadonnées de votre IdP. |

Cliquez sur **Configure** pour enregistrer vos paramètres IdP.

* **Efficacité accrue :** L'intégration avec d'autres outils et services peut simplifier les flux de travail et accroître l'efficacité. Par exemple, des documents peuvent être échangés automatiquement entre DocBits et un système CRM, ce qui réduit la saisie manuelle et augmente la productivité
* **Cohérence des données :** L'intégration permet d'échanger des données sans rupture entre différents systèmes, ce qui améliore la cohérence et l'exactitude des données. Cela évite les incohérences ou les saisies en double qui pourraient entraîner des erreurs.
* **Mises à jour en temps réel** : L'intégration permet des mises à jour en temps réel entre différentes plateformes, de sorte que les utilisateurs disposent toujours des informations les plus récentes. C'est particulièrement important pour les processus métier critiques qui nécessitent des informations en temps réel.
* **Automatisation des tâches :** L'intégration permet d'automatiser les tâches de routine, ce qui fait gagner du temps et des ressources. Par exemple, des notifications peuvent être déclenchées automatiquement lorsqu'un événement donné se produit dans un autre système, sans intervention manuelle.
* **Meilleure expérience utilisateur :** Une intégration bien configurée garantit une expérience utilisateur fluide, car les utilisateurs n'ont pas à passer d'un système à l'autre pour accéder aux informations pertinentes. Cela améliore la satisfaction des utilisateurs et contribue à l'efficacité.

Pour configurer correctement les paramètres d'intégration, il est important de comprendre les exigences de l'organisation et de veiller à ce que l'intégration s'insère de manière fluide dans les flux de travail et processus existants. Cela exige une planification, une configuration et une surveillance rigoureuses de l'intégration afin de garantir son bon fonctionnement et la valeur attendue.
