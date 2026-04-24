# Extração de códigos de barras / QR

## **Visão geral**

Esta funcionalidade permite a extração automática de informações a partir de **códigos de barras e códigos QR** incorporados em documentos. É uma configuração tudo-ou-nada — ativá-la habilita a extração para ambos os tipos.

## Como habilitar a Extração de códigos de barras / QR

Para ativar a funcionalidade, siga estes passos:

1. **Abra Configurações**:
   * No painel, vá para **Configurações**.
   * Selecione **Processamento de documentos** e depois **Módulo**.
2. **Ative a funcionalidade**:
   * Role até a opção **Extração de códigos de barras / QR**.
   *   Mova o interruptor para ativar a extração.\
       \


       <figure><img src="../../../../../.gitbook/assets/image (445).png" alt=""><figcaption></figcaption></figure>

## **Tipos de código suportados**

O DocBits suporta a extração dos seguintes tipos de código:

* **QR-CODE**
* **EAN-2**, **EAN-5**, **EAN-8**, **EAN-13**
* **UPC-A**, **UPC-E**
* **ISBN-10**, **ISBN-13**
* **COMPOSITE**
* **I25**&#x20;
* **DATABAR**, **DATABAR-EXP**
* **CODABAR**
* **CODE-39**, **CODE-93**, **CODE-128**
* **PDF-417**
* **SQ-CODE**

## Padrões de QR codes de pagamento

Além da decodificação genérica de QR, o DocBits reconhece **sete padrões distintos de QR codes de pagamento** e extrai automaticamente seus campos de pagamento para a resposta da API do documento. Os clientes não precisam mais decodificar manualmente essas strings — cada padrão inclui seu próprio prefixo de campo (p. ex. `swissqr_*`, `girocode_*`), de modo que os valores fluem diretamente para matching, validação e exportação.

| # | Padrão | Região | Prefixo de campo | Uso típico |
|---|--------|--------|------------------|------------|
| 1 | [Swiss QR Bill](swiss-qr-code.md) | Suíça | `swissqr_*` | Toda fatura suíça desde 2020 |
| 2 | [GiroCode (EPC069-12)](girocode.md) | DE, AT, NL, BE, FI | `girocode_*` | Pagamentos SEPA |
| 3 | [SPAYD / SPD](spayd.md) | CZ, parcialmente SK | `spayd_*` | Padrão da Associação Bancária Tcheca |
| 4 | [PagoPA](pagopa.md) | IT (administração pública) | `pagopa_*` | Obrigatório em faturas da PA italiana |
| 5 | [URIs de pagamento cripto](crypto-uris.md) | Global (cripto) | `crypto_*` | Bitcoin, Lightning, Ethereum, Zcash, Litecoin |
| 6 | [EMVCo MPM](emvco-mpm.md) | BR, IN, SG, TH, MY, ID, PH, VN, HK e outros | `emvmpm_*` | Pix, UPI, PayNow, PromptPay, QRIS, QR Ph, VietQR, FPS |
| 7 | [ZATCA Fatoora](zatca-fatoora.md) | Arábia Saudita | `zatca_*` | Obrigatório em toda fatura do KSA |

**A detecção é automática.** Cada string QR decodificada é inspecionada pelo seu prefixo mágico (p. ex. `SPC\n0200` para Swiss QR Bill v2.0 ou `PAGOPA|002|` para PagoPA); apenas padrões reconhecidos são analisados em campos estruturados.

### **Páginas relacionadas**

[Detalhes da Extração de códigos de barras](bar-code-extractions.md)
