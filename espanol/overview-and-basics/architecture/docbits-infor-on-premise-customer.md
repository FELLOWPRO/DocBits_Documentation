# DocBits Infor Cliente On Premise

Para enviar datos a un cliente Infor onPremise ofrecemos dos formas: Site2Site con IPsec o [WatchDog](https://docs.docbits.com/administration-and-setup/setup/watchdog)

Envío de datos a un cliente Infor On-Premise

Para enviar datos a un cliente Infor on-premise, ofrecemos dos formas: VPN Site-to-Site con IPsec.

## Configuración de VPN Site-to-Site IPsec (Internet Protocol Security)

### 1. Información de configuración:

| **Configuración de VPN IPSEC** |                                                                 |
| ------------------------------ | --------------------------------------------------------------- |
|                                | **Endpoint B**                                                  |
| **Cliente**                    | _**FELLOWPRO AG**_                                              |
| **Nombre del contacto**        | _**Daniel Lopez**_                                              |
| **Correo electrónico**         | [daniel.lopez@fellowpro.com](mailto:daniel.lopez@fellowpro.com) |
| **Hardware/Software del endpoint** | _**StrongWAN**_                                             |
| **Ubicación del firewall**     | _**Frankfurt**_                                                 |
| **IP del endpoint**            | _**46.101.133.158**_                                            |
| **Red/Host 1**                 | _**10.135.0.0/16**_                                             |

### 2. Para una VPN site-to-site IPsec, necesita configurar y abrir los siguientes puertos:

1\. Puerto UDP 500: utilizado para el Intercambio de Claves de Internet (IKE) fase 1 y fase 2.

2\. Puerto UDP 4500: utilizado para el NAT traversal (NAT-T), que permite que el tráfico VPN pase a través de dispositivos NAT (Network Address Translation, traducción de direcciones de red).

## Acceso a Infor OS

• URL de autenticación: https://inforos.CustomerXYZad.net/

• URL de datos: https://inforos.CustomerXYZad.net:7443/

## Resumen:

Para configurar una VPN site-to-site IPsec, asegúrese de que los puertos y protocolos anteriores estén configurados y abiertos.

Utilice las URL proporcionadas para acceder a Infor OS para la autenticación y los datos.
