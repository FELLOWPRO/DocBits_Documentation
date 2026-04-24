# SPAYD / Short Payment Descriptor (Tcheco)

## Visão geral

**SPAYD** (Short Payment Descriptor), também conhecido como **SPD**, é o QR code de pagamento padrão definido pela Associação Bancária Tcheca. Ele é impresso em praticamente toda fatura comercial tcheca e é usado parcialmente na Eslováquia. O DocBits decodifica os payloads SPAYD e retorna a instrução de pagamento completa — incluindo os símbolos específicos tchecos (variable, specific, constant) — na resposta da API do documento.

### Visão geral da funcionalidade

Um payload SPAYD é uma lista de pares chave:valor separados por asteriscos. Os valores são codificados em percent-encoding, então nomes de destinatários e mensagens em UTF-8 são preservados. O DocBits suporta a variante comum `ACC` (IBAN mais BIC opcional, separados por `+`), `ALT-ACC` (IBANs alternativos, separados por vírgulas), e preserva quaisquer chaves específicas de fornecedor desconhecidas em um campo dedicado (`spayd_raw_pairs`), para que consumidores downstream nunca percam dados.

#### Principais benefícios

* **Cobertura completa de pagamentos tchecos**: IBAN/BIC e os símbolos VS/SS/KS são extraídos para campos nomeados.
* **Unicode-safe**: nomes de destinatários e mensagens UTF-8 em percent-encoding trafegam íntegros.
* **Compatível com o futuro**: chaves desconhecidas são preservadas em `spayd_raw_pairs`.

***

### Detecção

- Prefixo mágico: `SPD*1.0*`
- Payload é uma lista separada por `*` de pares `KEY:value`, p. ex. `SPD*1.0*ACC:CZ5508000000001234567899*AM:480.55*CC:CZK`
- Os valores são **percent-encoded** (RFC 3986)
- `ACC` pode carregar `IBAN+BIC` (separados por `+`); `ALT-ACC` carrega IBANs alternativos separados por vírgulas

### Campos extraídos

Todos os campos usam o prefixo `spayd_`:

| Campo | Descrição |
|-------|-----------|
| `spayd_iban` | IBAN principal (de `ACC`) |
| `spayd_bic` | BIC (de `ACC`, se presente) |
| `spayd_alt_ibans` | Lista de IBANs alternativos (de `ALT-ACC`) |
| `spayd_amount` | Valor (decimal, de `AM`) |
| `spayd_currency` | Moeda (de `CC`, normalmente `CZK`) |
| `spayd_variable_symbol` | Símbolo variável (`VS`) — número de fatura/referência |
| `spayd_specific_symbol` | Símbolo específico (`SS`) |
| `spayd_constant_symbol` | Símbolo constante (`KS`) |
| `spayd_recipient_name` | Nome do destinatário (de `RN`) |
| `spayd_due_date` | Data de vencimento (de `DT`, `YYYYMMDD`) |
| `spayd_message` | Mensagem livre (de `MSG`) |
| `spayd_raw_pairs` | Pares `KEY:value` desconhecidos ou específicos de fornecedores, preservados sem alteração |

### Exemplo de resposta da API

```json
{
  "spayd_iban": "CZ5508000000001234567899",
  "spayd_amount": 480.55,
  "spayd_currency": "CZK",
  "spayd_variable_symbol": "2026041720",
  "spayd_constant_symbol": "0308",
  "spayd_recipient_name": "Moje firma, s.r.o.",
  "spayd_due_date": "20260507",
  "spayd_message": "Platba za fakturu 2026041720"
}
```

***

### Como habilitar a funcionalidade

A análise de SPAYD é coberta pelo interruptor geral **Extração de códigos de barras / QR** — nenhuma configuração específica do padrão é necessária.

1. **Abra Configurações**:
   * No painel, vá para **Configurações**.
   * Selecione **Processamento de documentos** e depois **Módulo**.
2. **Ative a funcionalidade**:
   * Role até a opção **Extração de códigos de barras / QR**.
   * Mova o interruptor para ativá-la.

Para a lista completa de padrões de QR codes de pagamento, consulte a [página de Visão geral](./README.md).
