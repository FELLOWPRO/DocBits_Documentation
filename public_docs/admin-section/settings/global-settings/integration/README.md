# Integração

<figure><img src="../../../../.gitbook/assets/Bildschirmfoto 2024-05-08 um 08.39.14.png" alt=""><figcaption></figcaption></figure>

## Chave da API

* **Chave**: Este é o identificador único usado por aplicações externas para acessar a API do Docbits. É crucial para autenticar solicitações feitas ao Docbits por outros softwares.
* Ações como visualizar, regenerar ou copiar a chave da API podem ser realizadas aqui, dependendo das necessidades específicas e dos protocolos de segurança.

## Configurações do Provedor de Serviços SSO (Single Sign-On)

* **ID da Entidade**: Este é o identificador do Docbits como provedor de serviços na configuração SSO. Ele identifica de forma única o Docbits dentro do framework SSO.
* **URL de SLO (Logout Único)**: A URL para a qual as sessões SSO são enviadas para fazer logout simultaneamente de todas as aplicações conectadas via SSO.
* **URL de SSO**: A URL usada para iniciar o processo de login único.
* Ações como "Baixar Certificado" e "Baixar Metadados" estão disponíveis para obter os certificados de segurança necessários e informações de metadados usadas na configuração e manutenção da integração SSO.

{% hint style="info" %}
Veja [Configuração do SSO](../../../setup/sso-configuration/)
{% endhint %}

## Configurações do Provedor de Serviços de Identidade

* **ID do Locatário**: Isso pode ser usado quando o Docbits se integra com serviços em nuvem que requerem um identificador de locatário para gerenciar dados e configurações de acesso específicas da empresa que usa o Docbits.
* **Enviar arquivo**: Permite ao administrador enviar arquivos de configuração ou outros arquivos necessários que facilitam a integração com um provedor de identidade.
* **Configurar**: Um botão para aplicar ou atualizar as configurações após fazer alterações ou enviar novas configurações.
