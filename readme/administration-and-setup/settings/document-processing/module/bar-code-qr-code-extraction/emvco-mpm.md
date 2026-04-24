# EMVCo MPM (QR apresentado pelo comerciante)

## Visão geral

**EMVCo MPM** (Merchant-Presented Mode) é a especificação global de QR codes mantida pela EMVCo — o mesmo organismo por trás dos padrões de cartões com chip e pagamentos por aproximação. Um único envelope TLV (Tag-Length-Value) é compartilhado por mais de uma dúzia de sistemas nacionais de pagamentos instantâneos, de modo que um único parser habilita **Pix** (Brasil), **UPI** (Índia), **PayNow** (Singapura), **PromptPay** (Tailândia), **QRIS** (Indonésia), **QR Ph** (Filipinas), **VietQR** (Vietnã), **FPS** (Hong Kong), **DuitNow** (Malásia), **NETS** (Singapura) e muitos outros.

### Visão geral da funcionalidade

Todo payload EMVCo MPM compartilha o mesmo envelope: começa com `000201` (Payload Format Indicator = 01) e termina com `6304<CRC>`, onde `<CRC>` é um checksum CRC16-CCITT-FALSE de 4 hex. Dentro, as tags 26–51 codificadas em TLV transportam templates de **Merchant Account Info** identificados por uma **sub-tag GUI** — essa tag GUI é como o DocBits detecta a qual esquema nacional o QR pertence. O CRC é validado e o resultado exposto como booleano, para que os comerciantes possam detectar QR codes adulterados.

#### Principais benefícios

* **Um extrator, muitos esquemas**: um único parser TLV genérico cuida de toda a família EMVCo MPM.
* **Esquemas nacionais identificados**: a saída inclui um esquema nomeado (p. ex. `pix`, `upi`, `paynow`), para que a lógica downstream ramifique de forma limpa.
* **Validade do CRC exposta**: `emvmpm_crc16_valid` revela QR codes adulterados ou corrompidos.
* **Normalização de moeda**: códigos numéricos ISO 4217 são mapeados automaticamente para alpha-3 (20+ moedas; códigos não mapeados passam inalterados).

***

### Detecção

- Forma mágica: começa com `000201` e termina com `6304<4-hex CRC16-CCITT-FALSE>`
- Um decodificador TLV genérico percorre cada tag
- Os esquemas nacionais são identificados através da **sub-tag GUI** dentro dos templates Merchant Account Info (tags 26–51)

### Esquemas nacionais reconhecidos

| Sub-tag GUI | Esquema | País |
|-------------|---------|------|
| `br.gov.bcb.pix` | **Pix** | Brasil |
| `UPI` | **UPI** | Índia |
| `SG.PAYNOW` | **PayNow / SGQR** | Singapura |
| `SG.COM.NETS` | **NETS** | Singapura |
| `HK.COM.HKICL.FPS` | **FPS** | Hong Kong |
| `ID.CO.QRIS.WWW` | **QRIS** | Indonésia |
| `COM.BDO.QRPH` / `COM.BPI.QRPH` / `PH.PPMI.P2MEMV` | **QR Ph** | Filipinas |
| `COM.QRCODE.TELLUSBANGKOK` + AID `A000000677010111` | **PromptPay** | Tailândia |
| `A000000727` | **VietQR** | Vietnã |

Valores GUI/AID não reconhecidos continuam sendo analisados — o extrator recai no conjunto genérico de campos EMVCo MPM.

### Campos extraídos

Todos os campos usam o prefixo `emvmpm_`:

| Campo | Descrição |
|-------|-----------|
| `emvmpm_scheme` | Esquema nacional detectado (p. ex. `pix`, `upi`, `paynow`, `qris`, `promptpay`, `vietqr`, `fps`, `qrph`, `nets`) ou `generic` |
| `emvmpm_merchant_name` | Nome do comerciante (tag 59) |
| `emvmpm_merchant_city` | Cidade do comerciante (tag 60) |
| `emvmpm_country_code` | Código de país ISO 3166 alpha-2 (tag 58) |
| `emvmpm_amount` | Valor da transação (decimal, tag 54) |
| `emvmpm_currency` | Moeda alpha-3 (convertida do código numérico da tag 53) |
| `emvmpm_additional_data` | Objeto aninhado: número da fatura, rótulo de referência, rótulo do terminal, finalidade da transação (sub-tags da tag 62) |
| `emvmpm_crc16_valid` | Booleano — `true` se o checksum CRC16 coincidir |

### Exemplo de resposta da API (Pix)

```json
{
  "emvmpm_scheme": "pix",
  "emvmpm_merchant_name": "ACME COMERCIO LTDA",
  "emvmpm_merchant_city": "SAO PAULO",
  "emvmpm_country_code": "BR",
  "emvmpm_amount": 125.00,
  "emvmpm_currency": "BRL",
  "emvmpm_additional_data": {
    "reference_label": "PEDIDO-2026-0427"
  },
  "emvmpm_crc16_valid": true
}
```

***

### Como habilitar a funcionalidade

A análise de EMVCo MPM é coberta pelo interruptor geral **Extração de códigos de barras / QR** — nenhuma configuração específica do padrão é necessária.

1. **Abra Configurações**:
   * No painel, vá para **Configurações**.
   * Selecione **Processamento de documentos** e depois **Módulo**.
2. **Ative a funcionalidade**:
   * Role até a opção **Extração de códigos de barras / QR**.
   * Mova o interruptor para ativá-la.

Para a lista completa de padrões de QR codes de pagamento, consulte a [página de Visão geral](./README.md).
