# DocFlow MCP

O DocFlow expõe um servidor **Model Context Protocol (MCP)** que permite que assistentes de IA gerenciem workflows e cards de parceiros de forma programática. Qualquer cliente compatível com MCP — Claude Code, Claude Desktop, OpenAI Codex ou integrações personalizadas — pode se conectar e usar essas ferramentas.

## O Que Você Pode Fazer?

Com o DocFlow MCP você pode:

- **Listar, criar, atualizar e excluir** workflows avançados
- **Testar workflows** com documentos reais ou fictícios
- **Construir cards personalizados** usando o Partner Card SDK
- **Validar, testar, aprovar e gerenciar** submissões de cards de parceiros
- **Importar cards** diretamente de repositórios do GitHub

## Visão Geral das Ferramentas

O DocFlow MCP agrupa suas ferramentas nas seguintes categorias. A maioria das ferramentas Workflow e Card SDK espelha endpoints REST existentes — consulte lá a referência da API. As categorias abaixo cobrem a superfície específica do MCP e os conceitos de workflow necessários para usá-la.

### Gerenciamento de Workflows

| Ferramenta | Descrição |
|------|-------------|
| `list_workflows` | Listar todos os workflows da organização atual |
| `get_workflow` | Obter detalhes de um workflow específico por ID |
| `create_advanced_workflow` | Criar um novo workflow avançado com nós e arestas |
| `update_advanced_workflow` | Atualizar um workflow avançado existente |
| `delete_workflow` | Excluir um workflow por ID |

### Testes de Workflows

| Ferramenta | Descrição |
|------|-------------|
| `test_advanced_workflow` | Testar a execução de um workflow avançado, opcionalmente com documento |
| `list_test_scenarios` | Listar todos os cenários de teste de workflows |
| `list_cards` | Listar os cards / ações de workflow disponíveis |

### Gerenciamento do Card SDK

| Ferramenta | Descrição |
|------|-------------|
| `sdk_list_submissions` | Listar todas as submissões de cards de parceiros |
| `sdk_get_submission_status` | Obter o status de validação de uma submissão |
| `sdk_approve_card` | Aprovar um card de parceiro validado (admin) |
| `sdk_reject_card` | Rejeitar uma submissão de card de parceiro (admin) |
| `sdk_delete_submission` | Desativar ou excluir uma submissão (admin) |
| `sdk_list_cards_picker` | Listar todos os cards habilitados com flags de papel |

### Desenvolvimento do Card SDK

| Ferramenta | Descrição |
|------|-------------|
| `sdk_create_card` | Criar um novo card de parceiro a partir do código-fonte |
| `sdk_validate_card` | Executar a pipeline de validação sem salvar |
| `sdk_test_card` | Executar um card em um ambiente sandbox |
| `sdk_import_github` | Importar um app de parceiro do GitHub |

## Começando

1. [Configure seu cliente MCP](setup-and-configuration.md)
2. Conheça as [Workflow Tools](workflow-tools.md)
3. Explore as [Card SDK Tools](card-sdk-tools.md)
4. Siga os [exemplos](examples.md) de ponta a ponta

{% hint style="info" %}
O DocFlow MCP usa o transporte **Streamable HTTP**. O endpoint do servidor é `/v3/mcp/` no host DocFlow (ex.: `https://docflow.docbits.com/v3/mcp/`). Consulte [Configuração e Setup](setup-and-configuration.md) para a lista completa de URLs.
{% endhint %}
