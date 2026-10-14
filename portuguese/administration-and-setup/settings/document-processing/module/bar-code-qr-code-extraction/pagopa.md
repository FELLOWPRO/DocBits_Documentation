# PagoPA

## Visão geral

**PagoPA** é o padrão de QR code de pagamento da administração pública italiana. Toda fatura emitida por um órgão da PA italiana (municípios, universidades, saúde, autoridades fiscais) traz um QR code PagoPA. O DocBits decodifica o payload e retorna os quatro campos de pagamento obrigatórios na resposta da API do documento.

### Visão geral da funcionalidade

Os payloads PagoPA são compactos e rigidamente estruturados: exatamente **cinco campos separados por pipe** em uma única linha. Os valores são codificados em **centavos** (inteiro) e convertidos automaticamente pelo extrator em euros decimais. Os zeros à esquerda do `codice_avviso` (aviso de pagamento de 18 dígitos) são preservados — ele nunca deve ser interpretado como inteiro, pois é um identificador de largura fixa.

#### Principais benefícios

* **Cobertura obrigatória** para faturas da PA italiana: `codice_avviso` e código fiscal do credor extraídos para campos nomeados.
* **Tratamento numérico seguro**: o `codice_avviso` de 18 dígitos mantém os zeros à esquerda; o valor em centavos também é exposto como float em euros.

***

### Detecção

- Prefixo mágico: `PAGOPA|002|`
- Exatamente **5 campos separados por pipe** após o prefixo: `PAGOPA|002|<codice_avviso>|<fiscal_code_creditor>|<amount_cents>|<auth>`
- **Apenas EUR** — nenhuma outra moeda é válida segundo a especificação

### Campos extraídos

Todos os campos usam o prefixo `pagopa_`:

| Campo | Descrição |
|-------|-----------|
| `pagopa_codice_avviso` | Aviso de pagamento de 18 dígitos — zeros à esquerda preservados (string) |
| `pagopa_fiscal_code_creditor` | Código fiscal de 11 dígitos do credor (string) |
| `pagopa_amount_cents` | Valor em centavos (inteiro) |
| `pagopa_amount` | Valor em euros (decimal, derivado de `pagopa_amount_cents`) |
| `pagopa_auth` | Indicador opcional de auth/versão do payload |

### Exemplo de resposta da API

```json
{
  "pagopa_codice_avviso": "301234567890123456",
  "pagopa_fiscal_code_creditor": "80012345678",
  "pagopa_amount_cents": 12050,
  "pagopa_amount": 120.50
}
```

***

### Como habilitar a funcionalidade

A análise de PagoPA é coberta pelo interruptor geral **Extração de códigos de barras / QR** — nenhuma configuração específica do padrão é necessária.

1. **Abra Configurações**:
   * No painel, vá para **Configurações**.
   * Selecione **Processamento de documentos** e depois **Módulo**.
2. **Ative a funcionalidade**:
   * Role até a opção **Extração de códigos de barras / QR**.
   * Mova o interruptor para ativá-la.

Para a lista completa de padrões de QR codes de pagamento, consulte a [página de Visão geral](./README.md).
