# Mapeamento de Campos ZUGFeRD + Swiss QR Code

## Visão Geral

Ao processar faturas em PDF que contêm tanto dados XML ZUGFeRD quanto um Swiss QR Code, o DocBits extrai dados de ambas as fontes e os mescla de forma inteligente.

## Como Funciona

1. **Extração XML ZUGFeRD** - O DocBits extrai primeiro os campos do XML ZUGFeRD incorporado
2. **Detecção de Swiss QR Code** - O barcode detecta e analisa códigos Swiss QR
3. **Mesclagem Inteligente (Smart Merge)** - Campos vazios são preenchidos com dados do Swiss QR (campos com valores são preservados)
4. **Trilha de Auditoria (Audit Trail)** - Dados completos do código QR são armazenados em `qr_code_data` para verificação

## Tabela de Mapeamento de Campos

### Mapeamento de Campos Swiss QR Code → DocBits

| Campo Swiss QR | Campo DocBits | Descrição |
| :--- | :--- | :--- |
| IBAN | `supplier_iban` | IBAN do credor (ex: CH9300762011...) |
| Amount | `total_amount` | Valor do pagamento (ex: 1234.56) |
| Currency | `currency` | Código da moeda (CHF ou EUR) |
| Reference | `payment_reference` / `esr_reference` | Referência QR ou número ESR |
| Creditor.Name | `supplier_name` | Nome da empresa fornecedora |
| Creditor.AddressLine1 | `supplier_address` | Endereço (rua) |
| Creditor.PostalCode | `supplier_plz` | Código postal |
| Creditor.City | `supplier_city` | Cidade |
| Creditor.Country | `supplier_country` | Código do país (CH) |
| Debtor.Name | `company_name` | Nome da empresa destinatária |
| Debtor.AddressLine1 | `company_street` | Endereço do destinatário |
| Debtor.PostalCode | `company_plz` | Código postal do destinatário |
| Debtor.City | `company_city` | Cidade do destinatário |

## Exemplo: Processamento de Fatura de Amostra

### Documento de Entrada

*   **PDF**: Fatura com XML ZUGFeRD 1.0 incorporado + código de barras Swiss QR Code

### Dados Extraídos do Swiss QR Code

```json
{
  "supplier_iban": "CH9300762011623852957",
  "amount_to_pay": 1234.56,
  "currency": "CHF",
  "esr_reference": "210000000003139471430009017",
  "supplier_name": "Sample Company GmbH",
  "supplier": {
    "name": "Sample Company GmbH",
    "address_line_1": "Musterstrasse",
    "address_line_2": "123",
    "postal_code": "8000",
    "city": "Zürich",
    "country": "CH"
  },
  "recipient": {
    "name": "Demo Customer AG",
    "address_line_1": "Beispielweg 45",
    "postal_code": "3000",
    "city": "Bern",
    "country": "CH"
  }
}
```

### Resultados da Extração de Campos

| Campo | Valor | Fonte | Método |
| :--- | :--- | :--- | :--- |
| `supplier_iban` | CH9300762011623852957 | ZUGFeRD XML | ED |
| `total_amount` | 1234.56 | ZUGFeRD XML | ED |
| `currency` | CHF | ZUGFeRD XML | ED |
| `supplier_name` | Sample Company GmbH | ZUGFeRD XML | ED |
| `supplier_address` | Musterstrasse 123 | ZUGFeRD XML | ED |
| `payment_reference` | 210000000003139471430009017 | Swiss QR | SWISS_QR |
| `supplier_plz` | 8000 | Swiss QR | SWISS_QR |
| `supplier_city` | Zürich | Swiss QR | SWISS_QR |

## Métodos de Extração

| Código do Método | Descrição |
| :--- | :--- |
| **ED** | Documento Eletrônico (ZUGFeRD/XRechnung/PEPPOL XML) |
| **SWISS_QR** | Extração de código de barras Swiss QR Code |
| **OCR** | Reconhecimento Óptico de Caracteres |
| **ML** | Extração por Machine Learning |

## Prioridade de Mesclagem (Merge)

1.  **ZUGFeRD XML** tem a maior prioridade (dados estruturados e confiáveis)
2.  **Swiss QR Code** preenche campos vazios (garantido como preciso para dados de pagamento)
3.  **OCR/ML** usado para campos não presentes em fontes eletrônicas

## Versões de Swiss QR Code Suportadas

*   Formato Swiss QR Bill (ISO 20022)
*   Formato QR-IBAN (começa com 30, 31)
*   Formato IBAN Padrão
*   Com/sem referência estruturada (QRR, SCOR)

## Requisito de Versão

Este recurso requer **api versão 10.95.6** e **barcode versão 1.0.5** ou superior.

### Versões dos Componentes (Ambiente Dev)

| Componente | Versão | Descrição |
| :--- | :--- | :--- |
| `api` | 10.95.6 | API principal com suporte à extração ZUGFeRD 1.0 |
| `barcode` | 1.0.5 | Detecção e análise de Swiss QR Code |
| `Auth` | 1.48.8 | Serviço de autenticação |

