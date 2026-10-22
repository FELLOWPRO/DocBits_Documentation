---
description: "P1: verificar chamadas API e uso posterior das respostas"
---

# P1: verificar chamadas API e uso posterior das respostas

**Call API** v2 acrescenta o caminho configurado à base API DocBits e usa o contexto organizacional atual. **Send HTTPS Request** v2 usa um URL externo e cabeçalhos próprios. Um URL externo completo não substitui um caminho Call API. Ambos os cartões simulam o envio em Advanced Test.

A ação HTTPS analisada regista estado e texto da resposta, mas não expõe armazenamento JSON com nome livre aos cartões seguintes. Call API converte o texto da resposta para booleano. HTTP 200, JSON válido e processamento posterior bem-sucedido precisam de provas distintas. Não invente sintaxe como `api.response.cost_center`.

Para uma resposta externa `{"cost_center":"4711"}`, defina escrita ou callback expressamente suportado para um campo documental. Verifique o campo guardado e leia-o na execução seguinte prevista. Transferência direta exige cartão ou extensão com contrato de saída documentado. JSON na configuração também não prova automaticamente os bytes JSON realmente enviados.

Use um destino próprio de teste e examine método, cabeçalhos, corpo real, estado e esquema. Cubra 4xx, 5xx, timeout, JSON inválido e evento duplicado. Repita escritas apenas depois de verificar a primeira receção. O URL de exemplo é um marcador reservado e não foi testado como serviço acessível.

## Cartões e parâmetros de exemplo

Os valores descrevem parâmetros de cartões, não um workflow completo importável. Substitua YOUR_* por seleções próprias de teste. O designer gere o ID oculto do chamador. Catálogo: Dev, DocFlow 2.10.38, 21 de outubro de 2026; confirme versões e permissões da organização.

### `call_api` · v2

Identidade: `6ca5e621-af72-4f55-aa2e-b3caa288722a`

| Parâmetro | Tipo / opções | Exemplo |
| --- | --- | --- |
| `params` | `params:str` | `"{}"` |
| `api_endpoint` | `api_endpoint:str` | `"YOUR_RELATIVE_API_PATH"` |
| `data` | `data:str` | `"{}"` |
| `method` | `put / post / delete / get` | `"get"` |

### `action_https_request` · v2

Identidade: `18d06ca4-3aca-4e49-b75c-566ade2fcb10`

| Parâmetro | Tipo / opções | Exemplo |
| --- | --- | --- |
| `data` | `data` | `"{}"` |
| `params` | `params` | `"{}"` |
| `url` | `url:str` | `"https://training.example.invalid/status"` |
| `headers` | `headers:str` | `"{}"` |
| `method` | `put / post / delete / get` | `"get"` |

## Casos de teste de negócio

| Caso | Entrada / configuração | Resultado esperado |
| --- | --- | --- |
| API-01 | Advanced Test | simulado; sem prova de entrega |
| API-02 | HTTPS: 4xx / 5xx | error |
| API-03 | timeout | verificar receção antes de repetir |
| API-04 | {"cost_center":"4711"} | sem api.response.cost_center automático |
| API-05 | POST × 2 | verificar duplicados no destino |

## Provas e limites

Parâmetros e comportamento foram comparados com o catálogo Dev e o código analisado. Os casos de negócio são uma orientação de aceitação. Não foram feitas aprovações pessoais, alterações reais nem entregas neste capítulo.

[Continuar a aprender](../workflow-learning-path.md) · [Pacote de formação](../workflow-training-kit.md)
