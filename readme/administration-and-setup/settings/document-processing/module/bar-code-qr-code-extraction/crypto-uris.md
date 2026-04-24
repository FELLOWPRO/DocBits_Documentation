# URIs de pagamento cripto (BIP21 / BIP321)

## Visão geral

URIs de pagamento cripto são o padrão informal, mas amplamente adotado, para codificar solicitações de pagamento em criptomoedas dentro de QR codes. O DocBits reconhece tanto **BIP21** (a URI de pagamento Bitcoin original) quanto **BIP321** (a extensão modernizada de 2024), nas cinco blockchains mais usadas: **Bitcoin**, **Lightning Network**, **Zcash**, **Ethereum** e **Litecoin**.

### Visão geral da funcionalidade

Um payload QR cripto é uma URI com um esquema (`bitcoin:`, `lightning:`, `zcash:`, `ethereum:`, `litecoin:`), um endereço de destinatário e um conjunto de parâmetros estilo URL. O DocBits extrai todos os parâmetros BIP21 padrão (`amount`, `label`, `message`) e as extensões mais recentes BIP321 (`lightning=` fallback, `pj=` / `pjos=` endpoints de payjoin). Conforme a especificação BIP21, parâmetros com prefixo `req-` podem ser rejeitados por consumidores se não suportados — o DocBits os mantém, portanto, em um campo separado (`crypto_required_params`) para que clientes decidam como tratá-los.

#### Principais benefícios

* **Suporte multi-chain**: Bitcoin, Lightning, Zcash, Ethereum e Litecoin em um único extrator.
* **BIP21 + BIP321**: ambas as versões reconhecidas; a versão é exposta na saída.
* **Esquema insensível a maiúsculas/minúsculas**: `BITCOIN:` e `bitcoin:` são tratados de forma idêntica.

***

### Detecção

- Detecção baseada em esquema (insensível a maiúsculas/minúsculas): `bitcoin:`, `lightning:`, `zcash:`, `ethereum:`, `litecoin:`
- Formato URI padrão: `<scheme>:<address>?<param>=<value>&<param>=<value>`

### Parâmetros suportados

**Parâmetros base do BIP21:**
- `amount` — valor solicitado na unidade nativa
- `label` — rótulo legível do destinatário
- `message` — texto livre

**Extensões do BIP321:**
- `lightning=<BOLT11>` — fatura Lightning como fallback
- `pj=<endpoint>` / `pjos=<endpoint>` — endpoints de payjoin
- `req-*` — parâmetros obrigatórios (preservados em `crypto_required_params`)

### Campos extraídos

Todos os campos usam o prefixo `crypto_`:

| Campo | Descrição |
|-------|-----------|
| `crypto_scheme` | `bitcoin`, `lightning`, `zcash`, `ethereum` ou `litecoin` |
| `crypto_address` | Endereço do destinatário |
| `crypto_amount` | Valor solicitado (decimal) |
| `crypto_currency` | Símbolo da moeda nativa (`BTC`, `ETH`, `LTC`, `ZEC`) |
| `crypto_label` | Rótulo do destinatário (se definido) |
| `crypto_message` | Texto livre (se definido) |
| `crypto_lightning_fallback` | Fatura BOLT11 Lightning (do BIP321 `lightning=`) |
| `crypto_payjoin_endpoint` | Endpoint de payjoin (de `pj=` / `pjos=`) |
| `crypto_required_params` | Todos os parâmetros `req-*`, preservados para decisão do cliente |
| `crypto_uri_version` | `bip21` ou `bip321` |

### Exemplo de resposta da API

```json
{
  "crypto_scheme": "bitcoin",
  "crypto_address": "bc1q9h6mksxrsfnd4ymr8mu2w2v3v0sylgkfghxwzm",
  "crypto_amount": 0.00254,
  "crypto_currency": "BTC",
  "crypto_label": "Acme Invoice 2026-042",
  "crypto_message": "Payment for invoice 2026-042",
  "crypto_uri_version": "bip21"
}
```

***

### Como habilitar a funcionalidade

A análise de URIs cripto é coberta pelo interruptor geral **Extração de códigos de barras / QR** — nenhuma configuração específica do padrão é necessária.

1. **Abra Configurações**:
   * No painel, vá para **Configurações**.
   * Selecione **Processamento de documentos** e depois **Módulo**.
2. **Ative a funcionalidade**:
   * Role até a opção **Extração de códigos de barras / QR**.
   * Mova o interruptor para ativá-la.

Para a lista completa de padrões de QR codes de pagamento, consulte a [página de Visão geral](./README.md).
