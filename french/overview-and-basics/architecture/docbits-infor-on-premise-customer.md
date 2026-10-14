# DocBits Infor sur le client sur site

Pour envoyer des données au client Infor sur site, nous proposons deux méthodes : Site à Site avec IPsec ou [WatchDog](https://github.com/Fellow-Consulting-AG/docbits/tree/fr/readme/overview-and-basics/architecture/broken-reference/README.md)

Envoi de données au client Infor sur site

Pour envoyer des données à un client Infor sur site, nous proposons deux méthodes : VPN Site-à-Site avec IPsec.

## Configuration du VPN Site-à-Site IPsec (Internet Protocol Security)

### Pour un VPN site-à-site IPsec, vous devez configurer et ouvrir les ports suivants :

1\. Port UDP 500 : Utilisé pour l'échange de clés Internet (IKE) phase 1 et phase 2.

2\. Port UDP 4500 : Utilisé pour le passage à travers NAT (NAT-T), permettant au trafic VPN de passer à travers les dispositifs de traduction d'adresses réseau (NAT).

## Accès à Infor OS

• URL d'authentification : https://inforos.CustomerXYZad.net/

• URL de données : https://inforos.CustomerXYZad.net:7443/

## Résumé :

Pour configurer un VPN site-à-site IPsec, assurez-vous que les ports et protocoles ci-dessus sont configurés et ouverts.

Utilisez les URL fournies pour accéder à Infor OS pour l'authentification et les données.
