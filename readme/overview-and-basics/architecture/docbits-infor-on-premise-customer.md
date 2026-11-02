# DocBits Infor sur le client sur site

Pour envoyer des données à un client Infor sur site, nous proposons deux méthodes : Site à Site avec IPsec ou [WatchDog](https://docs.docbits.com/administration-and-setup/setup/watchdog)

Envoi de données à un client Infor sur site

Pour envoyer des données à un client Infor sur site, nous proposons deux méthodes : VPN Site-à-Site avec IPsec.

## Configuration du VPN Site-à-Site IPsec (Internet Protocol Security)

### 1. Informations de configuration :

| **Configuration du VPN IPSEC** |                                                                 |
| ------------------------------ | --------------------------------------------------------------- |
|                                | **Point de terminaison B**                                      |
| **Client**                     | _**FELLOWPRO AG**_                                              |
| **Nom du contact**             | _**Daniel Lopez**_                                              |
| **E-mail**                     | [daniel.lopez@fellowpro.com](mailto:daniel.lopez@fellowpro.com) |
| **Matériel/logiciel du point de terminaison** | _**StrongWAN**_                                  |
| **Emplacement du pare-feu**    | _**Francfort**_                                                 |
| **IP du point de terminaison** | _**46.101.133.158**_                                            |
| **Réseau/Hôte 1**              | _**10.135.0.0/16**_                                             |

### 2. Pour un VPN site-à-site IPsec, vous devez configurer et ouvrir les ports suivants :

1\. Port UDP 500 : utilisé pour l'échange de clés Internet (IKE) phase 1 et phase 2.

2\. Port UDP 4500 : utilisé pour le passage à travers NAT (NAT-T), permettant au trafic VPN de traverser les dispositifs NAT (Network Address Translation).

## Accès à Infor OS

• URL d'authentification : https://inforos.CustomerXYZad.net/

• URL de données : https://inforos.CustomerXYZad.net:7443/

## Résumé :

Pour configurer un VPN site-à-site IPsec, assurez-vous que les ports et protocoles ci-dessus sont configurés et ouverts.

Utilisez les URL fournies pour accéder à Infor OS pour l'authentification et les données.
