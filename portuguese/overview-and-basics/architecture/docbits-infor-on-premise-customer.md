# DocBits Infor on Premise Customer

Para enviar dados para o cliente Infor onPremise, oferecemos duas maneiras: Site2Site com IPsec ou [WatchDog](https://github.com/Fellow-Consulting-AG/docbits/tree/pt/readme/overview-and-basics/architecture/broken-reference/README.md)

Enviando Dados para o Cliente Infor On-Premise

Para enviar dados para um cliente Infor on-premise, oferecemos duas maneiras: VPN Site-to-Site com IPsec.

## Configuração da VPN Site-to-Site IPsec (Internet Protocol Security)

### Para uma VPN site-to-site IPsec, você precisa configurar e abrir as seguintes portas:

1\. Porta UDP 500: Usada para a troca de chaves da Internet (IKE) fase 1 e fase 2.

2\. Porta UDP 4500: Usada para a travessia NAT (NAT-T), permitindo que o tráfego VPN passe por dispositivos de tradução de endereços de rede (NAT).

## Acessando Infor OS

• URL de autenticação: https://inforos.CustomerXYZad.net/

• URL de dados: https://inforos.CustomerXYZad.net:7443/

## Resumo:

Para configurar uma VPN site-to-site IPsec, certifique-se de que as portas e protocolos acima estejam configurados e abertos.

Use as URLs fornecidas para acessar o Infor OS para autenticação e dados.
