# Resolução de Problemas de Extração de Tabelas

{% embed url="https://youtu.be/LFw-JXqYWzw" %}
DocBits Tables Explained: AI Table Extraction vs Standard Extraction (When to Use Which)
{% endembed %}

{% embed url="https://youtu.be/5XqEP-5fq6M" %}
DocBits OCR & E-Text Explained: OCR View, Debug Mode, Quality Settings, Deskew & Header Extraction
{% endembed %}

## **Passo 1: Abrir Visualização OCR para Resultados de Extração Ruins**

Se os resultados do treinamento de extração de tabelas não estiverem bons:

1. Abra a **Visualização OCR** clicando no ícone de lupa com **OCR** escrito nele.
2. Revise os resultados da extração e veja se o processo OCR pode melhorar a captura de dados.
3. Se os resultados ainda parecerem ruins, tente um documento diferente para verificar se o problema é específico do documento.
4. Se o problema for específico do documento, use outro documento para extração.
   * Se o problema persistir, siga para os próximos passos.

## **Passo 2: Verificar Disponibilidade de E-Text**

1. Verifique se o documento possui **e-text** disponível.
   * Você pode verificar isso usando uma ferramenta como o **Adobe Acrobat**.
   * Se o documento contiver e-text, siga para o **Passo 3**.
   * Se o documento não contiver e-text, siga para o **Passo 4**.

## **Passo 3: Ativar Extração de E-Text**

Se o documento contiver e-text, você tem duas opções:

1. **Ativar extração de e-text apenas para este fornecedor**:
   * Volte para a **Validação de Campos de Documentos**.
   * Clique no quadrado com os três pontos na barra de ferramentas do lado esquerdo.
   * Aqui, ative a opção **Usar E-text se disponível** para ativá-la apenas para este fornecedor.
2. **Ativar extração de e-text para todos os fornecedores**:
   * Vá para **Configurações** > **Processamento de Documentos** > **Configurações OCR**.
   * Nesta seção, você encontrará a opção **Usar E-text se disponível** e poderá ativá-la para todos os fornecedores.
3. Após ativar a extração de e-text, tente novamente o **treinamento de extração de tabelas**.
   * Se os resultados melhorarem, o problema estará resolvido.
   * Se os resultados ainda não estiverem bons, prossiga para o **Passo 4**.

## **Passo 4: Sem E-Text Disponível - Alterar Versão do OCR de IA**

Se o documento não tiver e-text disponível:

1. Vá para **Configurações** > **Processamento de Documentos** > **Configurações OCR**.
2. Altere a **Versão do OCR de IA** para uma versão diferente.
3. Volte para o **Treinamento de Extração de Tabelas** e tente novamente.
4. Se o resultado for melhor:
   * Verifique outros documentos de fornecedores diferentes para garantir que os resultados de extração para esses fornecedores não sejam afetados por essa alteração.
   * **Seja cauteloso, pois essa alteração pode afetar os resultados de extração de outros fornecedores.**
   * Essa alteração pode impactar outros fornecedores, então verifique minuciosamente os resultados para garantir que não afete negativamente as extrações de documentos de outros fornecedores.
5. Se o resultado não melhorar após alterar a versão do OCR de IA, entre em **contato conosco** para obter mais assistência.

## Mensagens na tabela

A extração pode parecer correta e, ainda assim, o documento recusar-se a ser aprovado. Estas são as mensagens que o DocBits mostra na tabela de itens de linha ou por baixo dela, o que as desencadeia e como as resolver.

| Mensagem | Causa | Correção |
|---|---|---|
| **Coluna obrigatória vazia** (célula assinalada a vermelho, nome da coluna na dica) | Uma coluna marcada como *Obrigatória* nas definições de colunas da tabela não tem valor nesta linha. | Preencha a célula. Se o valor nunca existir para este tipo de documento, um administrador desmarca *Obrigatória* em Definições → Tipos de Documento → Colunas da Tabela e reinicia o documento. |
| **Line total does not match quantity x unit price (expected …, got …)** | O DocBits verifica cada linha: `TOTAL_AMOUNT = QUANTITY × UNIT_PRICE + CHARGES`, menos `DISCOUNT`, ou × (100 − `DISCOUNT_PERCENT`) / 100, ou menos `DISCOUNT_PER_UNIT × QUANTITY`, consoante a coluna de desconto preenchida. Uma diferença superior a 0,02 gera a mensagem. A verificação só corre quando a quantidade, o preço unitário e o total estão todos preenchidos. | Compare os quatro valores com o documento. Normalmente um deles foi lido para a coluna errada; um valor de encargos ou de desconto na célula errada é o caso mais comum. Corrija a célula; a mensagem desaparece ao guardar. |
| **Line total does not match quantity x unit price minus discount / minus percentage discount / minus per-unit discount** | A mesma verificação, com a coluna de desconto que está preenchida. | Como acima; verifique primeiro a célula do desconto. |
| **Line items add up to … but the net total is …** (aviso) | A soma de todas as células `TOTAL_AMOUNT` difere do valor líquido no cabeçalho. | Procure uma linha em falta, uma linha duplicada ou um valor líquido do cabeçalho lido incorretamente. Um aviso não bloqueia a aprovação. |
| **Total does not add up: expected …, got …** (cabeçalho) | Líquido + imposto (+ portes nos layouts dos EUA) difere do total do cabeçalho. | Verificação do cabeçalho, não é um problema da tabela: corrija os valores do cabeçalho. |
| **Line Item Table is missing Mandatory column for PO like (Item Number, Unit Price, Quantity and Total amount)** | A correspondência de PO precisa dessas quatro colunas predefinidas e uma delas está oculta ou foi substituída por uma coluna personalizada. | Administrador: torne a coluna predefinida visível em Colunas da Tabela, ou mapeie o valor para ela no treino de tabelas. |
| **Table is already extracted by AI. Do you want to train manually?** | Abriu o treino de tabelas para um fornecedor cuja tabela vem da IA. | Confirme para treinar; as regras guardadas substituem então a tabela de IA para este fornecedor. Cancele para manter a tabela de IA. |
| **AI Table will display here. Enable in …** | A extração de tabelas por IA está desativada para a organização. | Administrador: Definições → Processamento de Documentos → Classificação e Extração → *Extração de tabelas por IA*. |
| **No line items yet** | Nada foi extraído: não há regras para este fornecedor e a IA não encontrou tabela, ou o documento não tem texto legível. | Siga os Passos 1 a 4 acima (Visualização OCR, E-Text). Depois, treine a tabela uma vez ou adicione linhas manualmente com *Adicionar nova linha à tabela*. |

### A IA continua a preencher uma coluna com o valor errado

Exemplo visto na prática: a IA escreve o total da linha em `CHARGES`. Todas as linhas falham então a verificação do total da linha, porque os encargos são somados a quantidade × preço unitário.

1. Se o fornecedor tiver regras guardadas, desmarque *Usar IA* nessa coluna (Definições → Tipos de Documento → Colunas da Tabela) para que sejam as regras a preenchê-la.
2. Se o fornecedor não tiver regras, treine a tabela uma vez para que a coluna fique associada à sua posição na página, ou oculte a coluna se o fornecedor nunca imprimir esse valor.
3. Adicione uma [tag da tabela de IA](../../../end-user-and-partner-section/end-user-section/ai-table/ai-table-tags.md) como *"a coluna de encargos está vazia neste fornecedor"*; as tags são guardadas por fornecedor.

### Desativar as verificações da tabela

Definições → Tipos de Documento → *o seu tipo* → Mais definições → **Ignorar validação da tabela** marca a tabela de todos os documentos desse tipo como válida: as discrepâncias no total da linha e as colunas obrigatórias vazias deixam de ser comunicadas. As verificações do cabeçalho (total = líquido + imposto) mantêm-se. Use-a apenas para tipos de documento cujas tabelas são informativas e não são exportadas para o ERP.
