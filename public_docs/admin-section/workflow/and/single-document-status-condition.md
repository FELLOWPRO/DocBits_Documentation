# Condição de Status de Documento Único

<figure><img src="../../../.gitbook/assets/userlmn_928e514bc0e2aa775894e4ec5f992bd9.png" alt=""><figcaption></figcaption></figure>

**Propósito**

Este cartão de fluxo de trabalho é projetado para gerenciar operações em documentos com base em um único status de documento especificado. Ao simplificar a condição para um único status, o cartão é focado em acionadores de fluxo de trabalho muito específicos, tornando-o ideal para atividades direcionadas de processamento de documentos dentro de um sistema ERP.

**Componentes do Cartão**

1. **Operador**
* **Descrição**: Especifica o método para avaliar o status do documento em relação à condição selecionada.
* **Opções**:
* **é**: Aciona a operação se o status atual do documento corresponder ao status selecionado.
* **não é**: Aciona a operação se o status atual do documento não corresponder ao status selecionado.
2. **Status**
* **Descrição**: Permite a seleção de um único status de documento para definir a condição.
* **Exemplos de Status**: "Erro", "Erro de Exportação", "Pronto para Validação", "Pronto para Revisão", "Aguardando Aprovação", "Aguardando Segunda Aprovação".
* **Detalhe**: Os usuários escolhem um status em um menu suspenso ou em um conjunto de botões de rádio. Esse status então serve como critério para a operação do cartão.

**Funcionalidade**

* **Identificação do Status do Documento**: Identifica o status atual de um documento à medida que é processado pelo sistema ERP.
* **Avaliação da Condição**:
* Com base no operador selecionado (`é` ou `não é`), o cartão verifica se o status atual do documento está alinhado com o critério de status escolhido.
* **Execução da Ação**:
* **Condição Verdadeira**: Se o status corresponder (ou não corresponder, com base no operador), a ação correspondente é iniciada. Isso pode ser encaminhamento para processamento adicional, geração de notificação ou outros fluxos de trabalho predefinidos.
* **Condição Falsa**: Se a condição não for atendida, nenhuma ação é tomada ou um caminho alternativo é acionado.
* **Integração com Outros Fluxos de Trabalho**: Mesmo sendo projetado para avaliação de um único status, este cartão pode ser integrado efetivamente em sequências de fluxo de trabalho mais amplas para garantir o manuseio preciso de documentos.

**Interações do Usuário**

* **Configuração e Configuração**: Os usuários configuram o cartão selecionando um operador e, em seguida, escolhendo um status entre as opções disponíveis. Esse processo de seleção é direto e projetado para evitar confusão.
* **Monitoramento e Relatórios**: Permite o monitoramento por meio de relatórios gerados pelo sistema ou painéis que acompanham o processamento de documentos com base em seu status, ajudando a supervisionar a eficácia dos fluxos de trabalho implementados.
* **Tratamento de Erros e Notificações**: Configurável para alertar os usuários sobre quaisquer anomalias de processamento ou para sinalizar documentos que não atendem às condições estabelecidas, garantindo atenção e resolução rápidas.

#### Conclusão

O cartão de fluxo de trabalho "Condição de Status de Documento Único" simplifica a gestão de documentos ao focar em condições de status individuais. Essa especificação ajuda em casos em que é necessária um controle preciso sobre os fluxos de documentos, especialmente em ambientes com critérios de processamento rigorosos. Documentar claramente esta versão do cartão garantirá que os usuários compreendam totalmente sua aplicação e possam integrá-lo efetivamente em suas operações diárias, aprimorando tanto a conformidade quanto a eficiência no processamento de documentos.
