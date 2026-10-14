# Swiss QR Bill

## Visão geral

O **Swiss QR Bill** é o padrão nacional de comprovante de pagamento que, desde 30 de junho de 2020, substituiu os tradicionais boletos laranja e vermelho suíços. Toda fatura nacional suíça — de concessionárias, seguradoras ou parceiros comerciais — traz hoje um código Swiss QR Bill. O DocBits decodifica esses códigos automaticamente e expõe cada campo de pagamento na resposta da API.

### Visão geral da funcionalidade

As Swiss QR Bills seguem o padrão de pagamentos **ISO 20022** e são emitidas em duas versões: **v1.0** (lançamento inicial) e **v2.0** (atual). O extrator do DocBits suporta ambas. Os payloads reconhecidos são decodificados em um conjunto completo de campos — credor, devedor, IBAN / QR-IBAN, valor, moeda, tipo de referência (QRR, SCOR ou NON), mensagens estruturadas e livres, e esquemas de pagamento alternativos.

<figure><img src="../../../../../.gitbook/assets/image (6) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### Principais benefícios

* **Zero entrada manual** para faturas suíças: IBAN, valor, referência e credor fluem diretamente para o documento.
* **Ambas as versões cobertas**: v1.0 e v2.0 são detectadas automaticamente.
* **Tipos de referência preservados**: QRR, SCOR e NON são mantidos exatamente como impressos, o que mantém a conciliação downstream funcionando.

***

### Detecção

- Prefixo mágico: `SPC\n0100` (v1.0) ou `SPC\n0200` (v2.0)
- Compatível com ISO 20022
- O parser também expõe `alt-schemes` (esquemas de pagamento alternativos) quando presentes

### Campos extraídos

Todos os campos usam o prefixo `swissqr_`:

| Campo | Descrição |
|-------|-----------|
| `swissqr_account` | IBAN ou QR-IBAN do credor |
| `swissqr_creditor_name` | Nome do credor |
| `swissqr_creditor_street` | Rua / linha de endereço do credor |
| `swissqr_creditor_city` | Cidade do credor |
| `swissqr_creditor_postal_code` | CEP do credor |
| `swissqr_creditor_country` | País do credor (ISO 3166 alpha-2) |
| `swissqr_debtor_name` | Nome do devedor (se impresso) |
| `swissqr_debtor_street`, `swissqr_debtor_city`, `swissqr_debtor_postal_code`, `swissqr_debtor_country` | Endereço do devedor |
| `swissqr_amount` | Valor (decimal) |
| `swissqr_currency` | Moeda (ISO 4217) — normalmente `CHF` ou `EUR` |
| `swissqr_reference` | Referência estruturada (QRR ou SCOR) |
| `swissqr_reference_type` | `QRR`, `SCOR` ou `NON` |
| `swissqr_unstructured_message` | Texto livre de mensagem |
| `swissqr_bill_information` | Informações de cobrança estruturadas (S1 / Swico) |
| `swissqr_alt_schemes` | Procedimentos alternativos (se presentes) |

### Exemplo de resposta da API

```json
{
  "swissqr_account": "CH4431999123000889012",
  "swissqr_creditor_name": "Robert Schneider AG",
  "swissqr_creditor_street": "Rue du Lac 1268",
  "swissqr_creditor_city": "Biel",
  "swissqr_creditor_postal_code": "2501",
  "swissqr_creditor_country": "CH",
  "swissqr_amount": 1949.75,
  "swissqr_currency": "CHF",
  "swissqr_reference": "210000000003139471430009017",
  "swissqr_reference_type": "QRR",
  "swissqr_unstructured_message": "Bill No. 3139 for services 2026"
}
```

***

### Como habilitar a funcionalidade

A análise do Swiss QR Bill é coberta pelo interruptor geral **Extração de códigos de barras / QR** — nenhuma configuração específica do padrão é necessária.

1. **Abra Configurações**:
   * No painel, vá para **Configurações**.
   * Selecione **Processamento de documentos** e depois **Módulo**.
2. **Ative a funcionalidade**:
   * Role até a opção **Extração de códigos de barras / QR**.
   * Mova o interruptor para ativá-la.

<figure><img src="../../../../../.gitbook/assets/image (444).png" alt=""><figcaption></figcaption></figure>

Para a lista completa de padrões de QR codes de pagamento, consulte a [página de Visão geral](./README.md).
