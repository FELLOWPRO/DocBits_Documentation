---
description: Hashes de palavras-passe, armazenamento de chaves API, TLS, acesso a credenciais e recuperação de contas no DocBits.
---

# Armazenamento seguro de credenciais

O DocBits trata as palavras-passe de início de sessão, as chaves API do DocBits, as informações de conta e as credenciais de sistemas ligados de acordo com a sua finalidade. Esta página descreve a proteção e a recuperação do acesso para cada categoria.

## Palavras-passe de início de sessão

O DocBits armazena as palavras-passe de início de sessão como **hashes unidirecionais com salt**. A autenticação verifica a palavra-passe introduzida em relação ao hash armazenado. A palavra-passe original não é guardada num formato que permita decifrá-la e recuperá-la.

Por isso, os administradores e o suporte do DocBits não podem recuperar a palavra-passe existente em texto simples a partir do hash armazenado. Se um utilizador se esquecer da palavra-passe, tem de a redefinir para voltar a iniciar sessão com uma palavra-passe.

### Redefinir a palavra-passe

1. Selecione **Esqueceu sua senha** no ecrã de início de sessão.
2. Introduza o endereço de e-mail associado à conta.
3. Abra a ligação de redefinição enviada para esse endereço.
4. Defina uma nova palavra-passe e inicie sessão com ela.

As ligações de redefinição expiram. Se uma ligação tiver expirado, solicite uma nova. O procedimento define uma nova palavra-passe; não revela a anterior. Consulte as instruções completas em [Obter acesso e iniciar sessão](../end-user-and-partner-section/end-user-section/getting-access-and-signing-in.md).

As contas com SSO ou uma chave de acesso (passkey) configurados podem utilizar esse método alternativo. No caso de SSO, a recuperação da palavra-passe é gerida pelo fornecedor de identidade. Consulte [Autenticação de dois fatores](two-factor-authentication.md).

## Chaves API do DocBits

As chaves criadas através da **Gestão de chaves API** são mostradas na íntegra apenas uma vez, no momento da criação. O DocBits guarda um hash unidirecional da chave e um prefixo curto para identificação. O prefixo e os metadados continuam visíveis na lista de gestão; a chave original completa não pode ser recuperada a partir do hash.

Nem os administradores nem o suporte do DocBits podem consultar a chave completa após a criação. Se perder uma chave, revogue-a e crie uma nova. Cada chave pode ter uma data de expiração e ser revogada separadamente. Consulte [Gestão de chaves API](../administration-and-setup/settings/global-settings/integration/api-key-management.md).

## Dados da conta e credenciais de sistemas ligados

Nomes, endereços de e-mail, funções e estados das contas são informações que os administradores autorizados da organização podem consultar e gerir. São distintos do segredo utilizado para a autenticação. Consulte [Utilizadores](../administration-and-setup/settings/global-settings/groups-users-and-permissions/users/README.md).

As credenciais fornecidas para sistemas ligados, como uma conta de serviço ERP, uma caixa de correio ou um servidor SFTP, também são distintas de uma palavra-passe do DocBits ou de uma chave API emitida pelo DocBits. Um conector pode precisar do segredo utilizável para se autenticar no sistema externo. O seu armazenamento e os controlos de acesso devem, por isso, ser avaliados para cada conector.

A impossibilidade de recuperar uma palavra-passe ou uma chave API do DocBits armazenada como hash **não** significa que todas as informações de conta ou todos os segredos de integração sejam inacessíveis ao fornecedor. Qualquer garantia sobre o acesso do pessoal às credenciais de integração exige a confirmação dos respetivos controlos operacionais de acesso.

## Cifragem durante a transmissão

Os pontos de acesso públicos do DocBits abaixo indicados suportam **TLS 1.2 e TLS 1.3** através de HTTPS. As verificações de **16 de outubro de 2026** confirmaram a rejeição de TLS 1.0 e TLS 1.1.

| Ponto de acesso | Finalidade | Versões TLS verificadas |
| --- | --- | --- |
| `app.docbits.com` | Aplicação web | TLS 1.2 e TLS 1.3 |
| `auth.docbits.com` | Serviço de autenticação | TLS 1.2 e TLS 1.3 |
| `api.docbits.com` | API | TLS 1.2 e TLS 1.3 |

### Que tipos de cifragem são suportados durante a transmissão?

| Pergunta | Resposta para os pontos de acesso públicos acima indicados |
| --- | --- |
| O TLS 1.1 é suportado? | **Não.** As ligações que utilizam TLS 1.1 são rejeitadas. |
| O TLS 1.2 é suportado? | **Sim.** |
| O TLS 1.3 é suportado? | **Sim.** |

Os seguintes métodos de cifragem foram negociados com sucesso nos **três pontos de acesso**, em testes com validação dos certificados realizados a 16 de outubro de 2026:

| Método de cifragem | Comprimento da chave simétrica | Versões TLS verificadas |
| --- | --- | --- |
| AES-128-GCM | 128 bits | TLS 1.2 e TLS 1.3 |
| AES-256-GCM | 256 bits | TLS 1.2 e TLS 1.3 |
| ChaCha20-Poly1305 | 256 bits | TLS 1.3 |

Estes métodos fornecem cifragem autenticada, protegendo a confidencialidade e a integridade dos dados durante a transmissão. O método negociado depende das capacidades e da configuração do cliente e do servidor. Os comprimentos indicados referem-se às chaves simétricas de cifragem dos dados, independentemente do tamanho das chaves dos certificados. Os conjuntos de cifras TLS 1.2 testados utilizam ECDHE para a troca de chaves efémeras.

Esta verificação abrange as ligações a estes pontos de acesso públicos, incluindo as de clientes ou outros servidores. Não estabelece as definições de protocolo ou cifragem de cada ligação interna entre serviços, ligação a bases de dados, ponto de acesso regional ou integração externa. Estas ligações exigem confirmação para a instalação e a integração em causa.

## Cifragem das informações de conta armazenadas

DigitalOcean Managed Databases utiliza cifragem de volumes completos com LUKS e AES-256-XTS; as suas cópias geridas utilizam AES-256-CTR. Spaces utiliza AES-XTS de 256 bits nos discos físicos. [Cifragem em repouso](../security/encryption-at-rest.md) descreve métodos, gestão de chaves e cobertura das cópias.

O hashing de palavras-passe e chaves API é uma medida distinta da cifragem de bases de dados, volumes de armazenamento, objetos e cópias de segurança. Os controlos descritos não demonstram que cada nome de utilizador, campo de conta ou segredo de integração é cifrado individualmente, nem que todos os dados armazenados utilizam um algoritmo de cifragem específico.

Para um requisito que abranja todas as informações das contas de clientes, solicite à FELLOWPRO AG uma declaração específica da instalação sobre os repositórios de dados e as cópias de segurança pertinentes, os métodos de cifragem, a gestão de chaves e o acesso do pessoal. Um modelo de alojamento na nuvem ou serverless, por si só, não demonstra estas propriedades.

## Resposta a um questionário de segurança de um cliente

O texto seguinte descreve o âmbito confirmado:

> As palavras-passe de início de sessão do DocBits são guardadas como hashes unidirecionais com salt. Os administradores e o suporte do DocBits não podem recuperar a palavra-passe original em texto simples a partir do hash armazenado. Os utilizadores que se esqueçam da palavra-passe têm de definir uma nova através do procedimento de redefinição por e-mail para voltar a iniciar sessão com palavra-passe. SSO ou chaves de acesso configurados oferecem métodos alternativos de início de sessão.
>
> As chaves criadas através da Gestão de chaves API do DocBits são mostradas apenas uma vez e guardadas como hashes unidirecionais. Nem os administradores nem o suporte do DocBits podem recuperar a chave completa posteriormente. As chaves perdidas devem ser revogadas e substituídas.
>
> Os pontos de acesso públicos da aplicação web, da autenticação e da API do DocBits acima indicados suportam HTTPS com TLS 1.2 e TLS 1.3; TLS 1.0 e TLS 1.1 foram rejeitados nas verificações de 16 de outubro de 2026. Foram verificados AES-128-GCM com 128 bits e AES-256-GCM com 256 bits em TLS 1.2 e TLS 1.3, bem como ChaCha20-Poly1305 com 256 bits em TLS 1.3. Esta declaração abrange as ligações a esses pontos de acesso. A cifragem de todas as informações de conta armazenadas e das cópias de segurança, a proteção de cada ligação interna entre servidores e o acesso do pessoal às credenciais de integrações externas exigem confirmação separada para a instalação em causa.
