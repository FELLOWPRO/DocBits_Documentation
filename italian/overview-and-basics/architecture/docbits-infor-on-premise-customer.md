# Cliente DocBits con Infor in locale

Per inviare dati al cliente Infor onPremise offriamo due modalità: Site2Site con IPsec o [WatchDog](https://docs.docbits.com/administration-and-setup/setup/watchdog)

Invio Dati al Cliente Infor On-Premise

Per inviare dati a un cliente Infor on-premise, offriamo due modalità: VPN Site-to-Site con IPsec.

## Configurazione VPN Site-to-Site IPsec (Internet Protocol Security)

### 1. Informazioni di configurazione:

| **Configurazione IPSEC VPN**   |                                                                 |
| ------------------------------ | --------------------------------------------------------------- |
|                                | **Endpoint B**                                                  |
| **Cliente**                    | _**FELLOWPRO AG**_                                              |
| **Nome del contatto**          | _**Daniel Lopez**_                                              |
| **Email**                      | [daniel.lopez@fellowpro.com](mailto:daniel.lopez@fellowpro.com) |
| **Hardware/Software endpoint** | _**StrongWAN**_                                                 |
| **Ubicazione del firewall**    | _**Francoforte**_                                               |
| **IP dell'endpoint**           | _**46.101.133.158**_                                            |
| **Rete/Host 1**                | _**10.135.0.0/16**_                                             |

### 2. Per una VPN site-to-site IPsec, è necessario configurare e aprire le seguenti porte:

1\. Porta UDP 500: Utilizzata per l'Internet Key Exchange (IKE) fase 1 e fase 2.

2\. Porta UDP 4500: Utilizzata per la traversata NAT (NAT-T), consentendo al traffico VPN di passare attraverso i dispositivi NAT (Network Address Translation).

## Accesso a Infor OS

• URL di autenticazione: https://inforos.CustomerXYZad.net/

• URL dei dati: https://inforos.CustomerXYZad.net:7443/

## Riepilogo:

Per configurare una VPN site-to-site IPsec, assicurati che le porte e i protocolli sopra indicati siano configurati e aperti.

Utilizza gli URL forniti per accedere a Infor OS per l'autenticazione e i dati.
