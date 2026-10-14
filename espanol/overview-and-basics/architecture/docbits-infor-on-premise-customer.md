# DocBits Infor Cliente On Premise

Para enviar datos al cliente Infor onPremise, ofrecemos dos formas: Site2Site con IPsec o [WatchDog](https://github.com/Fellow-Consulting-AG/docbits/tree/es/readme/overview-and-basics/architecture/broken-reference/README.md)

Envío de Datos al Cliente Infor On-Premise

Para enviar datos a un cliente Infor on-premise, ofrecemos dos formas: VPN Site-to-Site con IPsec.

## Configuración de VPN Site-to-Site IPsec (Internet Protocol Security)

### Para una VPN site-to-site IPsec, necesita configurar y abrir los siguientes puertos:

1\. Puerto UDP 500: Utilizado para el Intercambio de Claves de Internet (IKE) fase 1 y fase 2.

2\. Puerto UDP 4500: Utilizado para la traversía NAT (NAT-T), permitiendo que el tráfico VPN pase a través de dispositivos NAT (Traducción de Direcciones de Red).

## Accediendo a Infor OS

• URL de autenticación: https://inforos.CustomerXYZad.net/

• URL de datos: https://inforos.CustomerXYZad.net:7443/

## Resumen:

Para configurar una VPN site-to-site IPsec, asegúrese de que los puertos y protocolos anteriores estén configurados y abiertos.

Utilice las URL proporcionadas para acceder a Infor OS para autenticación y datos.
