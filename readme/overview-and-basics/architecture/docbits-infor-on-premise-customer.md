# DocBits Infor on Premise-klant

Om gegevens naar een Infor onPremise-klant te sturen bieden wij twee mogelijkheden: Site2Site met IPsec of [WatchDog](https://docs.docbits.com/administration-and-setup/setup/watchdog)

Gegevens verzenden naar een Infor On-Premise-klant

Om gegevens naar een Infor on-premise-klant te sturen bieden wij twee mogelijkheden: Site-to-Site VPN met IPsec.

## IPsec (Internet Protocol Security) Site-to-Site VPN-configuratie

### 1. Configuratiegegevens:

| **IPSEC VPN Setup**            |                                                                 |
| ------------------------------ | --------------------------------------------------------------- |
|                                | **Endpoint B**                                                  |
| **Customer**                   | _**FELLOWPRO AG**_                                              |
| **Name of Contact**            | _**Daniel Lopez**_                                              |
| **Mail**                       | [daniel.lopez@fellowpro.com](mailto:daniel.lopez@fellowpro.com) |
| **Eindpunthardware/software** | _**StrongWAN**_                                                 |
| **Location of Firewall**       | _**Frankfurt**_                                                 |
| **Endpoint IP**                | _**46.101.133.158**_                                            |
| **Network/Host 1**             | _**10.135.0.0/16**_                                             |

### 2. Voor een IPsec site-to-site VPN moet u de volgende poorten configureren en openen:

1\. UDP-poort 500: wordt gebruikt voor Internet Key Exchange (IKE) fase 1 en fase 2.

2\. UDP-poort 4500: wordt gebruikt voor NAT-traversal (NAT-T), waardoor VPN-verkeer door NAT-apparaten (Network Address Translation) kan gaan.

## Toegang tot Infor OS

• Authenticatie-URL: https://inforos.CustomerXYZad.net/

• Gegevens-URL: https://inforos.CustomerXYZad.net:7443/

## Samenvatting:

Zorg er voor het opzetten van een IPsec site-to-site VPN voor dat de bovenstaande poorten en protocollen zijn geconfigureerd en geopend.

Gebruik de opgegeven URL's om toegang te krijgen tot Infor OS voor authenticatie en gegevens.



