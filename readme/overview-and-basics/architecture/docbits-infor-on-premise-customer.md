# DocBits Cliente Infor On-Premise

Para enviar dados para um cliente Infor on-premise, oferecemos duas maneiras: Site2Site com IPsec ou [WatchDog](https://docs.docbits.com/administration-and-setup/setup/watchdog)

Envio de dados para o cliente Infor On-Premise

Para enviar dados para um cliente Infor on-premise, oferecemos duas maneiras: VPN Site-to-Site com IPsec.

## Configuração da VPN Site-to-Site IPsec (Internet Protocol Security)

### 1. Informações de configuração:

| **Configuração da VPN IPSEC**  |                                                                 |
| ------------------------------ | --------------------------------------------------------------- |
|                                | **Endpoint B**                                                  |
| **Cliente**                    | _**FELLOWPRO AG**_                                              |
| **Nome do contato**            | _**Daniel Lopez**_                                              |
| **E-mail**                     | [daniel.lopez@fellowpro.com](mailto:daniel.lopez@fellowpro.com) |
| **Hardware/Software do endpoint** | _**StrongWAN**_                                              |
| **Localização do firewall**    | _**Frankfurt**_                                                 |
| **IP do endpoint**             | _**46.101.133.158**_                                            |
| **Rede/Host 1**                | _**10.135.0.0/16**_                                             |

### 2. Para uma VPN site-to-site IPsec, você precisa configurar e abrir as seguintes portas:

1\. Porta UDP 500: usada para a troca de chaves da Internet (IKE) fase 1 e fase 2.

2\. Porta UDP 4500: usada para a travessia de NAT (NAT-T), permitindo que o tráfego VPN passe por dispositivos de NAT (Network Address Translation).

## Acessando o Infor OS

• URL de autenticação: https://inforos.CustomerXYZad.net/

• URL de dados: https://inforos.CustomerXYZad.net:7443/

## Resumo:

Para configurar uma VPN site-to-site IPsec, certifique-se de que as portas e os protocolos acima estejam configurados e abertos.

Use as URLs fornecidas para acessar o Infor OS para autenticação e dados.
