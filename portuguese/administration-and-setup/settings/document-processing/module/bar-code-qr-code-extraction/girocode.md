# GiroCode (EPC069-12)

## Visão geral

O **GiroCode** é o QR code de pagamento SEPA definido pelo European Payments Council na especificação **EPC069-12**. É o padrão de facto nas faturas de bancos alemães e austríacos (Sparkasse, VR-Banken, Deutsche Bank, Commerzbank, PSA Austria), e também é emitido nos Países Baixos, Bélgica e Finlândia. O DocBits decodifica ambas as revisões (**v001** e **v002**) e retorna o payload completo de pagamento SEPA na resposta da API do documento.

### Visão geral da funcionalidade

Um GiroCode contém tudo o que é necessário para iniciar uma transferência SEPA: BIC e IBAN do beneficiário, nome, valor, finalidade, e uma referência estruturada de credor ou um texto livre de remessa. O DocBits normaliza o payload para que **valores com `.` ou `,` como separador decimal** — um desvio comum dos geradores alemães em relação à especificação — sejam aceitos sem erro.

#### Principais benefícios

* **Ampla cobertura DE / AT**: todos os grandes bancos de varejo imprimem GiroCodes nas faturas de clientes.
* **Ambas as revisões suportadas**: v001 (BIC obrigatório) e v002 (BIC opcional no EEE).
* **Tolerante a separadores decimais**: `227.01` e `227,01` são aceitos de forma intercambiável.

***

### Detecção

- Prefixo mágico: `BCD\n001` (v001) ou `BCD\n002` (v002)
- Payload estruturado por linhas conforme EPC069-12
- **v002** torna o BIC opcional quando o IBAN está no Espaço Único de Pagamentos em Euros

### Campos extraídos

Todos os campos usam o prefixo `girocode_`:

| Campo | Descrição |
|-------|-----------|
| `girocode_bic` | BIC do beneficiário (obrigatório em v001, opcional em v002 no EEE) |
| `girocode_creditor_name` | Nome do beneficiário |
| `girocode_iban` | IBAN do beneficiário |
| `girocode_amount` | Valor (decimal) — `.` e `,` aceitos |
| `girocode_currency` | Moeda (normalmente `EUR`) |
| `girocode_purpose` | Código SEPA de finalidade |
| `girocode_structured_reference` | Referência estruturada de credor (ISO 11649 RF) |
| `girocode_unstructured_remittance` | Texto livre de remessa |
| `girocode_version` | `001` ou `002` |

### Exemplo de resposta da API

Exemplo real (fatura Dr. Meindl u. Partner):

```json
{
  "girocode_bic": "DAAEDEDDXXX",
  "girocode_creditor_name": "Dr. Meindl u. Partner",
  "girocode_iban": "DE69300606010006343686",
  "girocode_amount": 227.01,
  "girocode_currency": "EUR",
  "girocode_unstructured_remittance": "38710498001705 - QR",
  "girocode_version": "002"
}
```

***

### Como habilitar a funcionalidade

A análise de GiroCode é coberta pelo interruptor geral **Extração de códigos de barras / QR** — nenhuma configuração específica do padrão é necessária.

1. **Abra Configurações**:
   * No painel, vá para **Configurações**.
   * Selecione **Processamento de documentos** e depois **Módulo**.
2. **Ative a funcionalidade**:
   * Role até a opção **Extração de códigos de barras / QR**.
   * Mova o interruptor para ativá-la.

Para a lista completa de padrões de QR codes de pagamento, consulte a [página de Visão geral](./README.md).
