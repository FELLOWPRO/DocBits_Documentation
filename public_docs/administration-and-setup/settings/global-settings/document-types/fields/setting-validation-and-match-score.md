# Definição de Validação e Pontuação de Correspondência

Em **Campos**, você pode definir os limites de validação e de reconhecimento de um tipo de documento. Esta página usa **Fatura** em uma organização de teste da documentação. Ela explica a caixa de seleção **FORÇAR VALIDAÇÃO** e os controles **PONTUAÇÃO DE CORRESPONDÊNCIA** atuais.

## Abrir as configurações dos campos

1. Vá para **Configurações → Tipos de Documentos → Fatura → Campos**.
2. Use **Pesquisar por nome** para localizar um campo, por exemplo `invoice_number` (exibido como **Número da fatura**).
3. Verifique a linha do campo antes de alterar uma configuração. **OBRIGATÓRIO**, **Somente Leitura**, **Escondido** e **FORÇAR VALIDAÇÃO** são caixas de seleção separadas.

<figure><img src="../../../../../.gitbook/assets/fields-validation-match-score-overview-pt-20261111.png" alt="Página Campos da Fatura em português, com as CONFIGURAÇÕES DE RECONHECIMENTO e os controles deslizantes OCR e PONTUAÇÃO DE CORRESPONDÊNCIA acima da lista de campos, as colunas OBRIGATÓRIO, Somente Leitura, Escondido, FORÇAR VALIDAÇÃO, Usar IA, OCR e PONTUAÇÃO DE CORRESPONDÊNCIA, e o botão Salvar configurações"><figcaption><p>As configurações de reconhecimento ficam acima da lista de campos.</p></figcaption></figure>

## FORÇAR VALIDAÇÃO

Selecione **FORÇAR VALIDAÇÃO** na linha do campo para aplicar uma validação mais rigorosa a esse campo. A caixa de seleção é separada de **OBRIGATÓRIO**: marcar um campo como obrigatório não seleciona FORÇAR VALIDAÇÃO automaticamente. A caixa de seleção pode ficar indisponível quando um campo está escondido ou é somente leitura. Depois de alterar a configuração do campo, clique em **Salvar configurações**.

As instruções antigas sugeriam inserir aqui limites numéricos ou expressões regulares. A tabela Campos atual não mostra um editor de regras na célula FORÇAR VALIDAÇÃO. Para regras específicas de um campo, consulte [Configurando Propriedades de Campo](configuring-field-properties-1.md).

## PONTUAÇÃO DE CORRESPONDÊNCIA

**PONTUAÇÃO DE CORRESPONDÊNCIA** é um limite numérico, não um valor de referência fixo. Os controles deslizantes **OCR** e **PONTUAÇÃO DE CORRESPONDÊNCIA** em **CONFIGURAÇÕES DE RECONHECIMENTO** aplicam seu valor às linhas de campos do tipo de documento; use as entradas **OCR** e **PONTUAÇÃO DE CORRESPONDÊNCIA** de uma linha de campo para um valor individual. No exemplo ilustrado, a linha `invoice_number` mostra **60** nas duas entradas. Revise os campos afetados e, em seguida, clique em **Salvar configurações**.

<figure><img src="../../../../../.gitbook/assets/fields-validation-match-score-invoice-number-pt-20261111.png" alt="Somente a linha do campo invoice_number, exibida como Número da fatura, após pesquisar por nome na interface em português: OBRIGATÓRIO e FORÇAR VALIDAÇÃO marcados, Usar IA em Sim · solicitado, OCR 60 e PONTUAÇÃO DE CORRESPONDÊNCIA 60"><figcaption><p>Pesquise um campo para verificar sua caixa FORÇAR VALIDAÇÃO e seu valor de PONTUAÇÃO DE CORRESPONDÊNCIA.</p></figcaption></figure>

**OCR** é um limite de reconhecimento separado, ao lado de PONTUAÇÃO DE CORRESPONDÊNCIA. **RESTAURAR PADRÕES** redefine as configurações; use-o apenas quando pretende descartar seus limites personalizados. Para outras opções de campos, consulte a visão geral de [Campos](README.md).

## Visão geral no nível do campo

<figure><img src="../../../../../.gitbook/assets/fields-validation-match-score-field-level-pt-20261111.png" alt="Parte inferior da lista de campos em português, com o grupo DETALHES DO FORNECEDOR e as linhas supplier_name, supplier_address e supplier_vat_id (Nome do Fornecedor, Endereço, VAT ID), cada uma com seus próprios valores nas colunas OCR e PONTUAÇÃO DE CORRESPONDÊNCIA"><figcaption><p>Cada campo tem sua própria configuração de validação e de reconhecimento.</p></figcaption></figure>

FORÇAR VALIDAÇÃO, OCR e PONTUAÇÃO DE CORRESPONDÊNCIA são configurações separadas. A pontuação de correspondência é um limite numérico; não é um texto de referência fixo nem um seletor de Match Value.
