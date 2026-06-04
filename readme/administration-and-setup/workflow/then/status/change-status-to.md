# Change Status to

<figure><img src="../../../../.gitbook/assets/image (283).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito:**

O cartão de fluxo de trabalho **"Change Status"** é utilizado para alterar o estado de um documento para um dos estados predefinidos — **Error, Rejected, Ready for Validation, Pending Approval, Pending Second Approval** — e, opcionalmente, acionar fluxos de trabalho associados com base na alteração de estado. Este cartão automatiza o processo de atualização de estados e de acionamento de fluxos de trabalho, assegurando uma gestão de documentos eficiente e um tratamento de erros adequado.

## **Componentes do cartão:**

1. **Status**
   * **Descrição**: Especifica o novo estado a aplicar ao documento.
   * **Opções**:
     * **Error**: Marca o documento como tendo encontrado um erro.
     * **Rejected**: Indica que o documento foi rejeitado e não prosseguirá.
     * **Ready for Validation**: Define o documento para ser revisto e validado pelo utilizador ou processo de sistema seguinte.
     * **Pending Approval**: Coloca o documento num estado pendente de aprovação.
     * **Pending Second Approval**: Coloca o documento em espera para um segundo nível de aprovação, se aplicável.
2. **Trigger Workflows**
   * **Descrição**: Determina se devem ser acionados quaisquer fluxos de trabalho subsequentes após a alteração de estado.
   * **Opções**:
     * **True**: Inicia quaisquer fluxos de trabalho relevantes com base na alteração de estado.
     * **False**: Impede a execução de fluxos de trabalho após a alteração de estado.

## **Funcionalidade:**

* **Avaliação da condição**: O sistema avalia as condições definidas nas secções **"Where"** e **"And Sections."** Se estas condições forem verdadeiras, o cartão procede à alteração do estado do documento para o valor selecionado.
* **Atualização de estado**: Uma vez cumpridas as condições, o estado do documento é atualizado para uma das opções predefinidas (Error, Rejected, Ready for Validation, Pending Approval, Pending Second Approval), consoante a seleção do utilizador.
* **Ação de acionamento de fluxos de trabalho**: Se **Trigger Workflows** estiver definido como **True**, o sistema inicia automaticamente quaisquer fluxos de trabalho associados após a atualização de estado. Se estiver definido como **False**, não são acionados fluxos de trabalho adicionais e o processo termina com a alteração de estado.

## **Configuração:**

Para configurar este cartão, os utilizadores precisam de:

1. Especificar o **Status** pretendido para o qual o documento será definido após a avaliação da condição (Error, Rejected, Ready for Validation, Pending Approval ou Pending Second Approval).
2. Escolher se devem **Trigger Workflows** após a alteração de estado, selecionando **True** ou **False**.
3. O cartão só executa a sua ação se ambas as condições nas secções **"Where"** e **"And Sections"** forem avaliadas como verdadeiras.

## **Conclusão:**

O cartão de fluxo de trabalho **"Change Status"** oferece uma abordagem simplificada para gerir os estados dos documentos e acionar fluxos de trabalho relacionados. Assegura que os documentos são automaticamente encaminhados para o estado correto e que as ações necessárias são tomadas, consoante a alteração de estado. Ao definir condições claras para a execução, reduz o esforço manual e aumenta a eficiência do fluxo de trabalho.
