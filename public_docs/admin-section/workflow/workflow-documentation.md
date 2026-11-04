# Documentação do Fluxo de Trabalho

**Documentação do Fluxo de Trabalho**

Para manter uma visão geral, você pode dar aos fluxos de trabalho diferentes títulos para que você possa imediatamente saber sobre qual tarefa este fluxo de trabalho se trata.

Criar um novo Fluxo de Trabalho: Clique em + ADICIONAR FLUXO DE TRABALHO

![](<../../.gitbook/assets/0 (1).png>)

Você pode usar esses fluxos de trabalho (Teste 1, 2, 3) para atribuir automaticamente vários documentos ao funcionário correto na empresa.

![](<../../.gitbook/assets/1 (1).png>)

Se uma fatura ou outro documento exceder um determinado valor total que requer revisão e aprovação prévia, esses documentos podem ser imediatamente atribuídos à pessoa correta.

<figure><img src="../../.gitbook/assets/docbits_export_sftp.png" alt="DocBits Exportar Sftp"><figcaption></figcaption></figure>

**Teste 1:              Cartão Lógico**

Quando:             **Responsável é:**                    Amier Haider

E:                **Tipo de Documento é:**        Fatura

Então:              **Atribuir documento para:**   Stefan Reppermund

![](<../../.gitbook/assets/3 (1).png>)

**Teste 2:              Cartão Lógico**

Quando:              **Responsável é:**                    Amier Haider

E:                 **Tipo de Documento é:**        Nota de Entrega

Então:               **Atribuir documento para:**   James Edwards

![](<../../.gitbook/assets/4 (1).png>)

**Teste 3:             Cartão Lógico**

**Quando:**             **Responsável é:**                    Amier Haider

**E:**                **Tipo de Documento é:**        Confirmação de Pedido

**Então:**              **Atribuir documento para:**   Anian Sollinger

![](<../../.gitbook/assets/5 (1).png>)

Também é possível, se o documento não for atribuído a uma única pessoa, atribuí-lo a um funcionário específico desde o início.

<figure><img src="../../.gitbook/assets/docbits_db_access_creation.png" alt="Docbits Db Access Creation" width="375"><figcaption></figcaption></figure>

Para uma visão mais fácil do que deve acontecer com um documento, você pode definir o status para os documentos recebidos neste fluxo de trabalho. Este fluxo de trabalho permite ver imediatamente se há, por exemplo, uma aprovação pendente.

**Teste 4:             Cartão Lógico**

**Quando:**             **Tipo de Documento é:**         Nota de Entrega

**E:**                **Responsável é:**                     Amier Haider

**Então:**              **Alterar Status para:**         Aprovação Pendente

<figure><img src="../../.gitbook/assets/docbits_export_smb.png" alt="DocBits Exportar Smb"><figcaption></figcaption></figure>

![](<../../.gitbook/assets/8 (1).png>)

**Teste 5:                Cartão Lógico**

Quando:                **Tipo de Documento é:**           Fatura

E:                   **Responsável é:**                       Stefan Reppermund

Então:                 **Alterar Status para:**           Segunda Aprovação Pendente

<figure><img src="../../.gitbook/assets/docbits_workflow_test_9_replacement.png" alt="Docbits Workflow Test 9 Replacement"><figcaption></figcaption></figure>

![](<../../.gitbook/assets/10 (1).png>)

Se uma fatura ou outro documento exceder um determinado valor total que requer revisão e aprovação prévia, esses documentos podem ser atribuídos imediatamente à pessoa certa.

![](<../../.gitbook/assets/11 (1).png>)

**Teste 6:                    Cartão Lógico**

Quando:                   **Responsável é:**                   Amier Haider

E:                      Campo do Doc        **total\_amount**     é      **Maior que       500**

Então:                    **Atribuir documento para:**   Asad Usman Khan

<figure><img src="../../.gitbook/assets/image (8) (1).png" alt=""><figcaption></figcaption></figure>

![](<../../.gitbook/assets/13 (1).png>)

Também é possível inserir o status no fluxo de trabalho, para que a pessoa atribuída possa ver imediatamente qual é o status deste documento e o que deve acontecer em seguida com ele.

**Teste 7:                 Cartão Lógico**

**Quando:** **Responsável é:**                     Amier Haider

**E:**                   Campo do Doc           **total\_amount**      é        **Maior que      500**

**Então:**                 **Atribuir documento para:**     Asad Usman Khan

&#x20;                            **Alterar Status para:**          Aprovação Pendente

<figure><img src="../../.gitbook/assets/docbits_approval_2.png" alt="DocBits Aprovação 2"><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/docbits_workflow_purchase_order_2.png" alt="DocBits Fluxo de trabalho Compra Pedido 2"><figcaption></figcaption></figure>

Por exemplo, se faltar informações específicas ou importantes em um documento, mas forem importantes e devem ser incluídas para processamento adicional, você pode configurar o fluxo de trabalho para que esses documentos sejam imediatamente encaminhados ao comprador e a um substituto.

<figure><img src="../../.gitbook/assets/docbits_workflow_5.png" alt="DocBits Fluxo de trabalho 5"><figcaption></figcaption></figure>

**Teste 9:**

O Fluxo de Trabalho com esses cartões lógicos é projetado para verificar automaticamente se a quantidade, preço unitário ou desconto detalhados em uma confirmação de pedido correspondem às cifras correspondentes no pedido de compra. Essa verificação garante consistência e precisão entre o que foi pedido e o que o fornecedor confirma para entregar.

Você pode atribuir a esses documentos um status específico ou atribuí-los a um funcionário específico.

<div align="center">

<figure><img src="../../.gitbook/assets/docbits_approval_permission.png" alt="DocBits Aprovação Permissão"><figcaption></figcaption></figure>

</div>

<figure><img src="../../.gitbook/assets/docbits_purchase_order_4.png" alt="DocBits Compra Pedido 4"><figcaption></figcaption></figure>

**Cartão Lógico: Quantidade ou Preço Unitário ou Desconto Correspondente**

Este cartão lógico é projetado para verificar automaticamente se a quantidade, preço unitário ou desconto detalhados em uma confirmação de pedido correspondem às cifras correspondentes no pedido de compra. Essa verificação garante consistência e precisão entre o que foi pedido e o que o fornecedor confirma para entregar.

**Condição de Gatilho**

A lógica é ativada quando qualquer uma das seguintes condições é atendida em uma confirmação de pedido em relação ao pedido de compra original:

* **Quantidade**: A quantidade de itens pedidos corresponde à quantidade confirmada pelo fornecedor.
* **Preço Unitário**: O preço por item acordado corresponde à confirmação do fornecedor.
* **Desconto**: Quaisquer descontos aplicados são consistentes entre o pedido de compra e a confirmação do pedido.

* **Definir Parâmetros de Comparação**: Configure os campos específicos (quantidade, preço unitário, desconto) que o cartão lógico verificará para uma correspondência.
* **Automatizar Verificação**: Configure o sistema para comparar automaticamente esses detalhes ao receber uma confirmação de pedido.
* **Personalizar Alertas**: Decida sobre o fluxo de trabalho para lidar com discrepâncias, incluindo a personalização de alertas para revisão manual.

Este cartão lógico é vital para garantir que os detalhes de uma confirmação de pedido estejam alinhados com o pedido de compra original, protegendo a integridade do ciclo de compras.

**Teste 10:**

Se você tiver um cálculo diferente para sobretaxas, ou apenas tiver em alguns itens, você pode usar os cartões de cálculo de tabela genéricos, alguns deles também permitem filtrar por expressões regulares.

<figure><img src="../../.gitbook/assets/docbits_table_invoice.png" alt="DocBits Tabela Fatura"><figcaption></figcaption></figure>

Acima está um exemplo de cálculo para MTZ com um filtro para números de item começando com 01, 06, 9, 001 ou 000.

Com uma configuração manual, é aconselhável dividir os cálculos que dependem de novas colunas em um fluxo de trabalho separado. Para continuar com o cálculo, você pode usar o cartão Executar Fluxo de Trabalho.

**Executar Fluxo de Trabalho**

<figure><img src="../../.gitbook/assets/docbits_workflow_2.png" alt="DocBits Fluxo de trabalho 2"><figcaption></figcaption></figure>

Com este cartão, você pode especificar o nome de um fluxo de trabalho que será executado após o fluxo de trabalho atual se suas condições forem atendidas e após os cartões then anteriores do fluxo de trabalho atual. Embora priorize fluxos de trabalho executáveis e ativos, também permite executar fluxos de trabalho desativados se o documento atender às condições dos fluxos de trabalho.
### **Adicionar sobretaxas calculadas em uma coluna existente** <a href="#pekg4i18rshn" id="pekg4i18rshn"></a>

<figure><img src="https://lh7-us.googleusercontent.com/XYY1xsFpp7_-Bi0WOSbotiVzspDLdaufx_xgoopMHmxdZnSDhroLpb0AE_si5PhwMq1jHfndc9FwOte9MOoCoTP5_JUYawO5cr4uIctIDHmwVjz3KacQrLJd8iBQy5KY4N-dMaWEi3IeTcc5OBRNJk4" alt=""><figcaption></figcaption></figure>

Se você deseja adicionar todas as sobretaxas como um desconto negativo na coluna de desconto existente, você pode usar o cartão de cálculo. Pode haver entradas nesta coluna, você pode defini-la como uma das variáveis no cartão, ter o MTZ subtraído dela e adicionar o resultado de volta a esta coluna. No caso de campos vazios (sobretaxas apenas para alguns itens), ele assumirá um 0 para seu cálculo.

**Notificar o usuário para autorizar a confirmação do pedido no DocBits**

Após calcular as sobretaxas, você pode querer notificar um usuário específico para autorizar a confirmação do pedido. Para isso, você pode usar o cartão de notificação.

<figure><img src="../../.gitbook/assets/docbits_settings_email.png" alt="DocBits Configurações E-mail"><figcaption></figcaption></figure>

Dependendo das configurações, o usuário recebe atribuída uma nova tarefa no DocBits e, opcionalmente, um e-mail para notificá-lo de sua nova tarefa.
