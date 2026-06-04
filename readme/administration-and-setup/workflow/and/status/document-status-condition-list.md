# Document Status Condition List

<figure><img src="../../../../.gitbook/assets/userlmn_e9d6da331deceed4f330358635d6b605 (1).png" alt="" width="521"><figcaption></figcaption></figure>

**Propósito**

Este cartão foi concebido para controlar as ações do fluxo de trabalho com base no estado atual de um documento, utilizando lógica condicional para acionar ou restringir determinados processos. Assegura que os documentos só avançam pelos fluxos de trabalho quando cumprem critérios de estado predefinidos.

**Componentes do cartão**

1. **Operador**
   * **Descrição**: Determina como o estado do documento será avaliado face a uma condição especificada.
   * **Opções**:
     * **is**: Aciona as ações associadas se o estado atual do documento corresponder a um dos estados especificados.
     * **is not**: Aciona as ações se o estado do documento não corresponder a nenhum dos estados especificados.
2. **Status ( List )**
   * **Descrição**: Lista os estados específicos com os quais o estado atual do documento será comparado.
   * **Exemplos**: "Error", "Export Error", "Ready in Validation", "Ready in Review", "Pending Approval", "Pending Second Approval". Estes representam diferentes fases ou condições em que um documento se pode encontrar dentro de um processo de fluxo de trabalho.

**Funcionalidade**

* **Identificação do estado**: Identifica automaticamente o estado atual de um documento à medida que ele avança pelo fluxo de trabalho do sistema ERP.
* **Avaliação da condição**: Aplica o operador escolhido (is ou is not) ao estado do documento em comparação com os estados listados:
  * Se for **is**, verifica se o estado do documento corresponde a algum estado da lista.
  * Se for **is not**, verifica se o estado do documento não aparece na lista.
* **Execução da ação**: Consoante o resultado da avaliação da condição:
  * **True**: Executa ações ou fluxos de trabalho predefinidos se a condição for cumprida.
  * **False**: Ignora ou aciona fluxos de trabalho alternativos se a condição não for cumprida.
* **Integração com o fluxo de trabalho**: Integra-se de forma transparente com outros componentes do fluxo de trabalho, assegurando que o tratamento de documentos é coordenado em todo o sistema.

**Interações do utilizador**

* **Configuração**: Os utilizadores configuram o cartão selecionando o operador e especificando os estados relevantes. Esta configuração pode envolver simples menus pendentes ou caixas de verificação para selecionar estados e operadores.
* **Monitorização e gestão**: Os utilizadores podem acompanhar a atividade do cartão através de um painel, que fornece informações sobre as condições de estado monitorizadas e as ações tomadas com base nessas condições.
* **Tratamento de erros e alertas**: Suporta a configuração de alertas para falhas de processo ou divergências nos estados de documento esperados, permitindo respostas rápidas a problemas operacionais.

#### Conclusão

O cartão de fluxo de trabalho "Document Status Condition" é vital para garantir que os documentos são processados corretamente de acordo com o seu estado atual, reforçando o controlo e a eficiência dentro do sistema ERP. Documentar este cartão com clareza no manual do sistema ajudará os utilizadores a implementá-lo e geri-lo eficazmente, aproveitando a sua funcionalidade para manter fluxos de documentos fluidos e conformes. Este cartão é particularmente útil na gestão dos ciclos de vida dos documentos e em assegurar que apenas os documentos que cumprem critérios específicos avançam para as fases subsequentes dos processos de negócio.
