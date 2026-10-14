# Integração da API DocBits com Infor OS



{% embed url="https://youtu.be/0aeSDWi9cV8" %}



## Importando a API do DocBits no Infor OS — use a especificação Swagger 2.0

Quando você conecta o Infor OS à API do DocBits (por exemplo, ao criar um aplicativo personalizado ou um fluxo de API no Infor OS), o Infor importa a especificação da API do DocBits. **Para o Infor OS, use a especificação Swagger 2.0 — e não a OpenAPI 3.0.**

O DocBits publica sua especificação de API em dois dialetos:

| Especificação | Caminho | Use para |
| --- | --- | --- |
| OpenAPI 3.0 / 3.1 | `/openapi.json` | Clientes de API padrão, geração de SDK, a documentação normal da API |
| **Swagger 2.0** | `/openapi-swagger2.json` | **Infor OS** (e qualquer outra ferramenta que use um swagger-ui mais antigo) |

{% hint style="warning" %}
**Por que Swagger 2.0 para o Infor?** O Infor OS usa uma versão mais antiga do swagger-ui, que não consegue montar uma requisição de upload de arquivo a partir da representação moderna do OpenAPI 3.0 (um `requestBody` com `format: binary`). Ele envia o upload **sem um boundary multipart**, e a API o rejeita com:

`400 — Missing boundary in multipart`

A especificação Swagger 2.0 declara os uploads de arquivos como `in: formData, type: file`, que o swagger-ui do Infor monta corretamente (com um boundary). Mesmos endpoints, mesmos dados — apenas o dialeto da especificação é diferente.
{% endhint %}

### Como obter a URL do Swagger 2.0

1. Abra a documentação da API do DocBits no seu navegador (por exemplo, `https://api.docbits.com/docs`).
2. No topo da página, abra a **lista suspensa de especificações** e selecione **Swagger 2.0 (Infor OS)**.
3. Copie a URL exibida para essa especificação — ela é a URL base da API do DocBits seguida de `/openapi-swagger2.json`.

Use essa URL sempre que o Infor OS pedir a especificação da API / Swagger. Copiá-la da lista suspensa garante o host correto para a sua região e o seu ambiente.

{% hint style="info" %}
Todo o restante da integração — autenticação (chave de API / token), endpoints e payloads — permanece inalterado. Apenas o dialeto da especificação que você importa no Infor é diferente.
{% endhint %}
