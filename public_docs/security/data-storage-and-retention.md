# Armazenamento, retenção e eliminação de dados

Os seus dados estão em boas mãos com o DocBits. Operamos o DocBits em duas regiões, **Frankfurt am Main (UE)** e **São Francisco (EUA)**, e é você quem define nas suas configurações durante quanto tempo os documentos ficam connosco. Esta página aborda os locais de armazenamento, os períodos de retenção e a eliminação.

**Documentação em: 28 de outubro de 2026.**

## Em resumo

- **Você escolhe a região:** Frankfurt para clientes da UE, São Francisco para clientes dos EUA.
- **Os seus dados permanecem na sua região.** Os dados da UE são alojados em Frankfurt, os dados dos EUA em São Francisco. Não há mistura de dados entre regiões.
- **Você controla durante quanto tempo os seus documentos são conservados** em **Processamento de Documentos → Validade dos documentos** ([ir para a configuração](../administration-and-setup/settings/document-processing/documents-expiry.md)).
- **Os ficheiros temporários de OCR** são eliminados automaticamente após 90 minutos.
- **Teremos todo o gosto em ajudar:** a nossa equipa responde a perguntas e pedidos de eliminação em **compliance@fellowpro.com**.

## Onde ficam armazenados os seus dados?

| Região | Para quem | Local | Serviços utilizados |
| --- | --- | --- | --- |
| **UE** | Todos os clientes da UE | **Frankfurt am Main, Alemanha** | DigitalOcean Kubernetes (região `fra1`) com bases de dados geridas PostgreSQL, OpenSearch e Valkey (`fra1`), além do DigitalOcean Spaces para armazenamento de ficheiros |
| **EUA** | Clientes dos EUA | **São Francisco, EUA** | DigitalOcean Kubernetes (região `sfo2`) com bases de dados geridas PostgreSQL, OpenSearch e Valkey (`sfo2`) |

**Cópias de segurança na UE:** Frankfurt é o local principal das cópias de segurança e Amesterdão (Países Baixos) o secundário, pelo que as suas cópias de segurança também permanecem dentro da UE.

**Sistemas ligados:** se exportar documentos para o seu ERP, para o Infor IDM ou para outro sistema de destino, essas cópias ficam armazenadas nesse sistema, segundo as regras dele e no local onde ele se encontra. Isso fica nas suas mãos.

## Durante quanto tempo os dados são conservados?

| Tipo de dados | Retenção |
| --- | --- |
| **Documentos carregados e dados extraídos** | Controlada por si através de [Validade dos documentos](../administration-and-setup/settings/document-processing/documents-expiry.md) (ver abaixo). |
| **Ficheiros temporários de OCR** | Limpeza automática após **90 minutos**. Aplica-se apenas ao armazenamento temporário de OCR, não ao seu documento no DocBits. |
| **Registos acessíveis ao cliente** (consultáveis em [Registo de atividade](../administration-and-setup/settings/log-settings/README.md)) | **30 dias** |
| **Registos internos** | **3 meses** |
| **Cópias de segurança diárias da base de dados (geridas)** | **7 dias**; as cópias mais antigas são removidas automaticamente. |
| **Cópias de segurança diárias adicionais (SnapShooter)** | Para as bases de dados de produção e sandbox; a retenção é definida por ambiente. |
| **Cookies e armazenamento do navegador** | Varia consoante a finalidade, ver [Cookies e armazenamento do navegador](cookies-and-browser-storage.md). |

Fazemos também cópias de segurança diárias, semanais, trimestrais e anuais. A pedido, teremos todo o gosto em indicar-lhe os períodos de retenção exatos destes tipos de cópias de segurança para o seu ambiente.

## Como definir a retenção dos seus documentos

Nas Configurações, abra **Processamento de Documentos → Validade dos documentos**. Existem duas configurações:

- **Delete document after:** durante quanto tempo os documentos são conservados.
- **Delete finished document after:** durante quanto tempo são conservados os documentos concluídos, totalmente processados e exportados.

As opções são **Default**, **48 Hours**, **1 Week**, **2 Weeks** e **4 Weeks**. **Default** aplica o valor predefinido do sistema. Se quiser um período fixo, basta escolher uma das durações. Todos os detalhes estão no [guia Validade dos documentos](../administration-and-setup/settings/document-processing/documents-expiry.md).

## O que acontece quando os dados são eliminados?

A Validade dos documentos elimina automaticamente os seus documentos após o período que escolheu. Isto é independente da limpeza dos ficheiros temporários de OCR, da expiração dos registos e da retenção das cópias de segurança.

Bom saber:

- **As cópias de segurança expiram segundo o seu próprio calendário.** Por isso, eliminar um documento no sistema ativo não remove imediatamente as cópias de segurança, mas apenas quando termina o respetivo período de cópia de segurança.
- **As cópias exportadas são suas.** Quando o DocBits elimina um documento, a cópia no seu ERP ou arquivo mantém-se. Planeie aí a retenção de acordo com os seus próprios requisitos.

## Dúvidas ou pedidos de eliminação? Estamos ao seu dispor

Para obter informações sobre a sua implementação ou para um pedido de eliminação, escreva-nos para **compliance@fellowpro.com**. Indique-nos a sua organização, o ambiente em causa, o tipo de dados e o âmbito pretendido. Não envie palavras-passe nem chaves de API.

Teremos também todo o gosto em confirmar:

- A sua região ativa e as configurações de retenção em vigor, incluindo o valor predefinido do sistema.
- Quando começa o período de eliminação e com que frequência é executada a limpeza.
- O âmbito da eliminação para documentos, dados extraídos, índices de pesquisa e dados derivados.
- Os locais e os períodos de retenção de todos os tipos de cópias de segurança, inclusive após o fim do contrato.

## Mais informações de segurança

- [DocBits (FELLOWPRO AG) — Questionário de Segurança e Conformidade](security-and-compliance-faq.md)
- [Cifragem em repouso](encryption-at-rest.md)
- [Armazenamento seguro de credenciais](secure-storage-of-credentials.md)
- [Cookies e armazenamento do navegador](cookies-and-browser-storage.md)
