# Scripts de Exemplo

Scripts de exemplo prontos para produção para casos de uso comuns de automação no DocBits. Cada exemplo inclui o script completo, uma explicação passo a passo e links para as funções utilizadas.

## Exemplos por Caso de Uso

### Validação de Dados
- [Validação de Fornecedor por Lookup](lookup-supplier-validation.md) — Validar fornecedor contra dados mestre
- [Validação da Soma da Tabela](table-sum-validation.md) — Verificar se os totais dos itens de linha correspondem ao valor líquido

### Automação
- [Correspondência Automática de OC](auto-po-matching.md) — Acionar correspondência automática de OC
- [Auto-Exportação por Condições](status-auto-export.md) — Saltar validação para faturas de baixo risco
- [Cálculo da Data de Vencimento](due-date-calculation.md) — Calcular condições de pagamento com salto de fins de semana

### Regras de Negócio
- [Detecção de Código Fiscal](tax-code-detection.md) — Determinar código fiscal a partir do texto completo e valores
- [Tarefa para Valor Elevado](task-high-amount.md) — Criar tarefa de aprovação para faturas grandes
- [Campos Obrigatórios Dinâmicos](dynamic-required-fields.md) — Ajustar campos obrigatórios com base na moeda

### Pesquisa Fulltext e Vetorial
- [Detecção de Faturas Duplicadas](duplicate-invoice-detection.md) — Encontrar faturas duplicadas usando pesquisa fulltext
- [Detecção de Documentos Semelhantes](similar-document-detection.md) — Sinalizar documentos semelhantes usando pesquisa vetorial
- [Pesquisa de Texto de Conformidade](compliance-text-search.md) — Pesquisar palavras-chave de conformidade (ex: Reverse Charge)
- [Validação de Fornecedor ERP](erp-vendor-validation.md) — Validar fornecedor contra dados mestre do ERP
- [Preencher Campos Ausentes do Histórico](fill-missing-fields-from-history.md) — Preencher automaticamente campos a partir de documentos anteriores semelhantes

### Exemplos Legados
- [Cálculo de Encargos Totais](calculating-total-charges-script-for-docbits-1.md) — Somar valores de frete e embalagem
- [Eliminar Linhas Vazias](delete-lines-with-empty-quantity-and-amount.md) — Remover linhas com quantidade/valor zero
- [Números de Certificado de Exportação](formatting-export-certificate-reference-numbers-script-for-docbits.md) — Preencher números de referência com zeros à esquerda
- [Números de Fatura Estendidos](generating-extended-invoice-numbers-script-for-docbits-1.md) — Concatenar ID da fatura e número da OC
- [USD como Moeda Padrão](usd-as-default-currency.md) — Definir USD como moeda padrão
