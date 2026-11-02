# ZATCA Fatoora (Arábia Saudita)

## Visão geral

**ZATCA Fatoora** é o QR code de faturamento eletrônico exigido pela Autoridade de Zakat, Impostos e Alfândega da Arábia Saudita. Desde **dezembro de 2021 (Fase 1)**, toda fatura B2C emitida no Reino deve conter um QR Fatoora com os cinco campos básicos da fatura, e desde **janeiro de 2023 (Fase 2)** o QR traz ainda um envelope de assinatura criptográfica. O DocBits decodifica ambas as fases e retorna cada campo de pagamento da Fase 1 como propriedade nomeada na resposta da API do documento.

### Visão geral da funcionalidade

ZATCA Fatoora usa um formato **TLV binário** (1 byte de ID de tag, 1 byte de comprimento, valor) embalado em **Base64**. Todo o texto é UTF-8, portanto nomes de vendedores em árabe são decodificados corretamente. O extrator expõe as tags 1–5 da Fase 1 como campos estruturados e — quando presentes — as tags 6–9 da Fase 2 como strings Base64 para ferramentas de compliance downstream. **A verificação de assinatura e hash está intencionalmente fora do escopo**; cabe a stacks dedicados de compliance de faturamento eletrônico.

#### Principais benefícios

* **Cobertura obrigatória de compliance**: toda fatura B2C saudita é analisada.
* **Suporte a árabe**: nomes de vendedores UTF-8 trafegam sem re-codificação.
* **Fase 1 e Fase 2**: ambas as fases são detectadas; a fase é exposta na saída.
* **Envelope da Fase 2 preservado**: hash, assinatura, chave pública e assinatura de certificado são mantidos como strings Base64 para ferramentas de compliance.

***

### Detecção

- TLV binário embalado em Base64 (tags 1–9, 1 byte de ID de tag + 1 byte de comprimento + valor)
- Detecção de fase: `zatca_phase = 1` quando apenas as tags 1–5 estão presentes; `zatca_phase = 2` quando as tags 6–9 também estão presentes

### Layout das tags TLV

| Tag | Fase | Conteúdo |
|-----|------|----------|
| 1 | 1 | Nome do vendedor (UTF-8, suporta árabe) |
| 2 | 1 | Número de registro de IVA |
| 3 | 1 | Timestamp da fatura (ISO 8601) |
| 4 | 1 | Total da fatura |
| 5 | 1 | Total de IVA |
| 6 | 2 | Hash da fatura XML (Base64) |
| 7 | 2 | Assinatura digital (Base64) |
| 8 | 2 | Chave pública (Base64) |
| 9 | 2 | Assinatura do certificado (Base64) |

### Campos extraídos

Todos os campos usam o prefixo `zatca_`:

| Campo | Descrição |
|-------|-----------|
| `zatca_seller_name` | Nome do vendedor (UTF-8) |
| `zatca_vat_number` | Número de registro de IVA |
| `zatca_invoice_timestamp` | Data/hora da fatura |
| `zatca_invoice_total` | Total da fatura (decimal) |
| `zatca_vat_total` | Total de IVA (decimal) |
| `zatca_phase` | `1` (Fase 1) ou `2` (Fase 2) |
| `zatca_invoice_hash` | Hash da fatura XML — apenas Fase 2, Base64 |
| `zatca_signature` | Assinatura digital — apenas Fase 2, Base64 |
| `zatca_public_key` | Chave pública — apenas Fase 2, Base64 |
| `zatca_certificate_signature` | Assinatura do certificado — apenas Fase 2, Base64 |

{% hint style="info" %}
**Fora do escopo**: O DocBits não verifica a assinatura criptográfica, o hash ou a cadeia de certificados. Essa verificação é uma responsabilidade de compliance dedicada e deve ser gerenciada por um stack de faturamento eletrônico certificado pela ZATCA.
{% endhint %}

### Exemplo de resposta da API (Fase 1)

```json
{
  "zatca_seller_name": "شركة أكمي التجارية",
  "zatca_vat_number": "300123456700003",
  "zatca_invoice_timestamp": "2026-04-24T10:00:00",
  "zatca_invoice_total": 115.00,
  "zatca_vat_total": 15.00,
  "zatca_phase": 1
}
```

***

### Como habilitar a funcionalidade

A análise de ZATCA Fatoora é coberta pelo interruptor geral **Extração de códigos de barras / QR** — nenhuma configuração específica do padrão é necessária.

1. **Abra Configurações**:
   * No painel, vá para **Configurações**.
   * Selecione **Processamento de documentos** e depois **Módulo**.
2. **Ative a funcionalidade**:
   * Role até a opção **Extração de códigos de barras / QR**.
   * Mova o interruptor para ativá-la.

Para a lista completa de padrões de QR codes de pagamento, consulte a [página de Visão geral](./README.md).
