# Encaminhamento de notificações

<figure><img src="../../../../.gitbook/assets/edoc_notification_routing.png" alt="Rotas de notificação"><figcaption><p>Associação dos resultados de validação a agentes</p></figcaption></figure>

A página **Encaminhamento de notificações** (**Documentos eletrónicos → Ações**) associa os resultados de validação aos **agentes do AI Workforce**. Cada resultado bloqueante aciona exatamente um agente — aquele cujo prefixo de código corresponde por mais tempo. Tudo o que não corresponde recai no agente de notificação ao fornecedor predefinido.

## Rotas de notificação

Escolha quem trata cada tipo de problema de fatura. Tudo o que não estiver listado vai para o agente predefinido:

| Rota | Resultados que abrange |
|------|------------------------|
| **Regras de negócio colombianas** | Resultados de regras de negócio específicas da Colômbia. |
| **Regras de negócio alemãs** | Resultados de regras de negócio específicas da Alemanha. |
| **Verificações de IBAN / conta bancária** | Resultados sobre dados de pagamento (dígito de controlo do IBAN, comprimento, país). |
| **Verificações de NIF/IVA** | Resultados sobre o formato do NIF/IVA. |
| **Tudo o resto** | O recurso predefinido para tudo o que não corresponde acima. |

Para cada rota, escolha o agente responsável no menu pendente. **Avançado (regras de código personalizadas)** permite encaminhar por um código de resultado exato quando precisa de um controlo mais fino.

## Agentes disponíveis

<figure><img src="../../../../.gitbook/assets/edoc_notification_agents.png" alt="Registo de agentes disponíveis"><figcaption><p>Registo só de leitura dos agentes do AI Workforce</p></figcaption></figure>

A secção **Agentes disponíveis** é um registo só de leitura dos agentes do AI Workforce fornecidos com a sua implementação, por exemplo:

| Agente | Finalidade |
|--------|------------|
| **Notificação ao fornecedor predefinida** | E-mail genérico de notificação ao fornecedor; o agente abrangente quando nenhum agente mais específico corresponde. |
| **Banking Bot** | Modelo especializado para resultados de dados de pagamento (correções de IBAN/BIC). |
| **Tax Bot** | Notificação ao fornecedor específica para NIF/IVA. |
| **Compliance Bot** | Trata os resultados de conformidade. |

Cada agente mostra a respetiva tarefa Celery e os prefixos de código de resultado que trata por predefinição.
