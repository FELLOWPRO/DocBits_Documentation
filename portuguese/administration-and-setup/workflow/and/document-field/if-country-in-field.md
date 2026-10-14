# If Country in Field

<figure><img src="../../../../.gitbook/assets/image (13) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito:**

Este cartão de fluxo de trabalho foi concebido para avaliar se um país especificado, localizado num campo designado, faz parte de uma determinada área comercial ou política (União Europeia, Espaço Schengen ou NAFTA). Com base nesta avaliação, o fluxo de trabalho pode continuar com uma condição verdadeira ou falsa, permitindo ações adicionais dentro do sistema. É particularmente útil para automatizar regras de negócio específicas de cada região, assegurar a conformidade ou acionar fluxos de trabalho específicos com base em afiliações geográficas.

## **Componentes do cartão:**

1. **Field Name**
   * **Descrição:** Especifica o campo do documento onde o nome ou código do país está armazenado.
   * **Detalhe:** Deve corresponder ao identificador exato do campo dos dados do país dentro do documento.&#x20;
2. **Operador**
   * **Descrição:** Especifica se o país no campo selecionado deve corresponder ou não à região ou acordo selecionado.
   * **Opções:**
     * **Is:** O país tem de fazer parte do acordo selecionado (UE, Schengen ou NAFTA) para que a condição seja verdadeira.
     * **Is Not:** O país não pode fazer parte do acordo selecionado para que a condição seja verdadeira.
3. **Country Comparison**
   * **Descrição:** Define se o país no campo é verificado face a um acordo político ou comercial específico.
   * **Opções:**
     * **European Union:** O cartão verifica se o país é membro da União Europeia.
     * **Schengen Area:** O cartão verifica se o país faz parte do Espaço Schengen.
     * **NAFTA:** O cartão verifica se o país é membro do acordo NAFTA.
4. **Boolean**
   * **Descrição:** Define o resultado da comparação. Se o país cumprir a condição, o fluxo de trabalho continua com o valor Boolean especificado.
   * **Opções:**
     * **True:** O fluxo de trabalho continua se a condição corresponder.
     * **False:** O fluxo de trabalho continua se a condição não corresponder.

## **Funcionalidade:**

* **Avaliação da condição:**
  * O sistema avalia se o país especificado no campo faz parte da região ou acordo escolhido (UE, Espaço Schengen ou NAFTA) com base no operador selecionado. Esta avaliação verifica o nome ou código do país face a uma lista predefinida de países que pertencem a cada grupo respetivo.
* **Execução da ação:**
  * **Condição Verdadeira:** Se o país no campo corresponder à região selecionada (de acordo com o operador), o fluxo de trabalho continua com a condição verdadeira especificada. Isto pode acionar ações adicionais, como encaminhar documentos, aplicar regras de processamento especiais ou ativar funcionalidades específicas de cada região.
  * **Condição Falsa:** Se o país não corresponder à região selecionada (de acordo com o operador), o fluxo de trabalho continua com a condição falsa especificada, permitindo a execução de ações alternativas ou a terminação do fluxo de trabalho consoante a configuração do sistema.

## **Configuração:**&#x20;

* Os utilizadores configuram o cartão selecionando o campo do documento que contém o país e especificando a região (União Europeia, Espaço Schengen ou NAFTA). O operador é depois escolhido a partir de uma lista pendente para definir se o país tem de fazer parte ou não da região selecionada. Por fim, os utilizadores definem a condição de continuação (verdadeira ou falsa), que determina o passo seguinte no fluxo de trabalho.

## **Conclusão:**

O cartão de fluxo de trabalho "Country in Field Comparison" é uma ferramenta essencial para automatizar processos que dependem de regras geográficas, como a conformidade com acordos comerciais ou afiliações políticas. Ao comparar os dados do país com regiões específicas como a União Europeia, o Espaço Schengen ou o NAFTA, este cartão assegura que o sistema aplica a lógica de processamento correta, melhorando a eficiência e garantindo uma execução precisa do fluxo de trabalho com base em condições geográficas.
