# DocBits Infor on Premise Klant

Om gegevens naar de Infor onPremise klant te verzenden, bieden we twee manieren: Site2Site met IPsec of WatchDog

Gegevens verzenden naar Infor On-Premise Klant

Om gegevens naar een Infor on-premise klant te verzenden, bieden we twee manieren: Site-to-Site VPN met IPsec.

## IPsec (Internet Protocol Security) Site-to-Site VPN Configuratie

### Voor een IPsec site-to-site VPN moet je de volgende poorten configureren en openen:

1\. UDP poort 500: Gebruikt voor Internet Key Exchange (IKE) fase 1 en fase 2.

2\. UDP poort 4500: Gebruikt voor NAT-traversal (NAT-T), waardoor VPN-verkeer door NAT (Network Address Translation) apparaten kan passeren.

## Toegang tot Infor OS

• Authenticatie URL: https://inforos.CustomerXYZad.net/

• Gegevens URL: https://inforos.CustomerXYZad.net:7443/

## Samenvatting:

Voor het opzetten van een IPsec site-to-site VPN, zorg ervoor dat de bovenstaande poorten en protocollen zijn geconfigureerd en geopend.

Gebruik de verstrekte URL's om toegang te krijgen tot Infor OS voor authenticatie en gegevens.
