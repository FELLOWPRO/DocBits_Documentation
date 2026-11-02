# DocFlow MCP

O DocFlow expõe um servidor **Model Context Protocol (MCP)** que permite que assistentes de IA gerenciem workflows e cards de parceiros de forma programática. Qualquer cliente compatível com MCP — Claude Code, Claude Desktop, OpenAI Codex ou integrações personalizadas — pode se conectar e usar essas ferramentas.

## O Que Você Pode Fazer?

Com o DocFlow MCP você pode:

- **Listar, criar, atualizar e excluir** workflows avançados
- **Testar workflows** com documentos reais ou simulados
- **Criar cards personalizados** usando o Partner Card SDK
- **Validar, testar, aprovar e gerenciar** submissões de cards de parceiros
- **Importar cards** diretamente de repositórios GitHub

## Visão Geral das Ferramentas

O DocFlow MCP fornece **18 ferramentas** em quatro categorias:

### Gerenciamento de Workflows

| Ferramenta | Descrição |
|------|-------------|
| `list_workflows` | Listar todos os workflows da organização atual |
| `get_workflow` | Obter detalhes de um workflow específico por ID |
| `delete_workflow` | Excluir um workflow por ID |

### Teste de Workflows

| Ferramenta | Descrição |
|------|-------------|
| `test_advanced_workflow` | Testar a execução de um workflow avançado com documento opcional |
| `list_test_scenarios` | Listar todos os cenários de teste de workflow |
| `list_cards` | Listar cards/ações de workflow disponíveis |

### Gerenciamento do Card SDK

| Ferramenta | Descrição |
|------|-------------|
| `sdk_list_submissions` | Listar todas as submissões de cards de parceiros |
| `sdk_get_submission_status` | Obter o status de validação de uma submissão |
| `sdk_approve_card` | Aprovar um card de parceiro validado (admin) |
| `sdk_reject_card` | Rejeitar uma submissão de card de parceiro (admin) |
| `sdk_delete_submission` | Desativar ou excluir uma submissão (admin) |
| `sdk_list_cards_picker` | Listar todos os cards habilitados com flags de função |

### Desenvolvimento do Card SDK

| Ferramenta | Descrição |
|------|-------------|
| `sdk_create_card` | Criar um novo card de parceiro a partir de código-fonte |
| `sdk_validate_card` | Executar validação em 5 etapas sem salvar |
| `sdk_test_card` | Executar um card em um ambiente isolado (sandbox) |
| `sdk_import_github` | Importar um app de parceiro do GitHub |

## Primeiros Passos

1. [Configure seu cliente MCP](setup-and-configuration.md)
2. Aprenda sobre as [Ferramentas de Workflow](workflow-tools.md)
3. Explore as [Ferramentas do Card SDK](card-sdk-tools.md)
4. Siga os [Exemplos](examples.md) completos

{% hint style="info" %}
O DocFlow MCP usa transporte **Streamable HTTP**. O endpoint do servidor é `/api/mcp/` no seu host da API DocBits.
{% endhint %}
