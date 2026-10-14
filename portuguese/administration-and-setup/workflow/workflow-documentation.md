# Atribuição e status — Exemplos práticos

Para manter uma visão geral, você pode atribuir títulos diferentes aos workflows, de modo a saber imediatamente sobre qual tarefa cada workflow trata.

Criar um novo Workflow: Clique em + ADD WORKFLOW

![](<../../.gitbook/assets/workflow_add_button.png>)

Você pode usar esses workflows (Test 1,2,3) para atribuir automaticamente diversos documentos ao colaborador certo na empresa.

![](<../../.gitbook/assets/workflow_list_overview.png>)

Se uma fatura ou outro documento exceder um determinado valor total que exija revisão e aprovação prévias, esses documentos podem ser atribuídos imediatamente à pessoa correta.

<figure><img src="../../.gitbook/assets/workflow_amount_check.png" alt="Workflow Amount Check"><figcaption></figcaption></figure>

**Test 1: Logic Card**

When: **Assignee is:** Amier Haider

And: **Document type is:** Invoice

Then: **Assign document to:** Stefan Reppermund

![](<../../.gitbook/assets/3 (1).png>)

**Test 2: Logic Card**

When: **Assignee is:** Amier Haider

And: **Document type is:** Delivery Note

Then: **Assign document to:** James Edwards

![](<../../.gitbook/assets/4 (1).png>)

**Test 3: Logic Card**

**When:** **Assignee is:** Amier Haider

**And:** **Document type is:** Order Confirmation

**Then:** **Assign document to:** Anian Sollinger

![](<../../.gitbook/assets/5 (1).png>)

Também é possível, caso o documento não esteja atribuído a uma única pessoa, atribuí-lo a um colaborador específico desde o início.

<figure><img src="../../.gitbook/assets/workflow_assign_to_employee_start.png" alt="Workflow Assign to Employee Start" width="375"><figcaption></figcaption></figure>

Para uma visão geral mais fácil do que deve acontecer com um documento, você pode definir o status dos documentos recebidos neste workflow. Este workflow torna possível ver imediatamente se há, por exemplo, uma aprovação pendente.

**Test 4: Logic Card**

**When:** **Document type is:** Delivery Note

**And:** **Assignee is:** Amier Haider

**Then:** **Change Status to:** Pending Approval

<figure><img src="../../.gitbook/assets/workflow_test4_delivery_note_status.png" alt="Workflow Test 4 Delivery Note Status"><figcaption></figcaption></figure>

![](<../../.gitbook/assets/8 (1).png>)

**Test 5: Logic Card**

When: **Document type is:** Invoice

And: **Assignee is:** Stefan Reppermund

Then: **Change Status to:** Pending Second Approval

<figure><img src="../../.gitbook/assets/workflow_test5_invoice_approval_status.png" alt="Workflow Test 5 Invoice Approval Status"><figcaption></figcaption></figure>

![](<../../.gitbook/assets/10 (1).png>)

Se uma fatura ou outro documento exceder um determinado valor total que exija revisão e aprovação prévias, esses documentos podem ser atribuídos imediatamente à pessoa certa.

![](<../../.gitbook/assets/11 (1).png>)

**Test 6: Logic Card**

When: **Assignee is:** Amier Haider

And: Docfield **total\_amount** is **Greater than 500**

Then: **Assign document to:** Asad Usman Khan

<figure><img src="../../.gitbook/assets/workflow_test6_total_amount_assign.png" alt="Workflow Test 6 Total Amount Assign"><figcaption></figcaption></figure>

![](<../../.gitbook/assets/13 (1).png>)

Também é possível inserir o status no workflow, para que a pessoa atribuída possa ver imediatamente em qual status este documento se encontra e o que deve acontecer em seguida com ele.

**Test 7: Logic Card**

**When:** **Assignee is:** Amier Haider

**And:** Docfield **total\_amount** is **Greater then 500**

**Then:** **Assign document to:** Asad Usman Khan

**Change Status to:** Pending Approval

<figure><img src="../../.gitbook/assets/workflow_test7_status_update.png" alt="Workflow Test 7 Status Update"><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/15 (1).png" alt=""><figcaption></figcaption></figure>

Por exemplo, se faltarem informações específicas ou importantes em um documento, mas que sejam essenciais e devam ser incluídas para o processamento posterior, você pode configurar o workflow para que esses documentos sejam encaminhados imediatamente ao comprador e a um substituto (suplente).

<figure><img src="../../.gitbook/assets/workflow_test8_missing_info.png" alt="Workflow Test 8 Missing Info"><figcaption></figcaption></figure>

**Test 9:**

O Workflow com esses logic cards foi projetado para verificar automaticamente se a quantidade, o preço unitário ou o desconto detalhados em uma confirmação de pedido correspondem aos valores correspondentes no pedido de compra. Essa verificação garante consistência e precisão entre o que foi pedido e o que o fornecedor confirma entregar.

Você pode atribuir a esses documentos um status específico ou atribuí-los a um colaborador específico.

<div align="center"><figure><img src="../../.gitbook/assets/workflow_test9_match_check_overview.png" alt="Workflow Test 9 Match Check Overview"><figcaption></figcaption></figure></div>

<figure><img src="../../.gitbook/assets/workflow_test9_match_check_detail.png" alt="Workflow Test 9 Match Check Detail"><figcaption></figcaption></figure>

**Logic Card: Quantity or Unit Price or Discount Match**

Este logic card foi projetado para verificar automaticamente se a quantidade, o preço unitário ou o desconto detalhados em uma confirmação de pedido correspondem aos valores correspondentes no pedido de compra. Essa verificação garante consistência e precisão entre o que foi pedido e o que o fornecedor confirma entregar.

**Trigger Condition**

A lógica é ativada quando qualquer uma das seguintes condições é atendida em uma confirmação de pedido em relação ao pedido de compra original:

* **Quantity**: A quantidade de itens pedidos corresponde à quantidade confirmada pelo fornecedor.
* **Unit Price**: O preço por item acordado corresponde à confirmação do fornecedor.
* **Discount**: Quaisquer descontos aplicados são consistentes entre o pedido de compra e a confirmação de pedido.
* **Define Comparison Parameters**: Configure os campos específicos (quantidade, preço unitário, desconto) que o logic card verificará para uma correspondência.
* **Automate Verification**: Configure o sistema para comparar automaticamente esses detalhes ao receber uma confirmação de pedido.
* **Customize Alerts**: Decida sobre o fluxo de trabalho para lidar com discrepâncias, incluindo a personalização de alertas para revisão manual.

Este logic card é vital para garantir que os detalhes de uma confirmação de pedido estejam alinhados com o pedido de compra original, protegendo a integridade do ciclo de compras.

**Test 10:**

Se você tiver um cálculo diferente para sobretaxas, ou tiver sobretaxas apenas em alguns itens, você pode usar os generic table calculation cards; alguns deles também permitem filtrar por expressões regulares.

<figure><img src="../../.gitbook/assets/19 (1).png" alt=""><figcaption></figcaption></figure>

Acima está um exemplo de cálculo para MTZ com um filtro para números de item que começam com 01, 06, 9, 001 ou 000.

Com uma configuração manual, é recomendável dividir os cálculos que dependem de novas colunas em um workflow separado. Para continuar com o cálculo, você pode usar o card Run Workflow.

**Run Workflow**

<figure><img src="../../.gitbook/assets/20 (1).png" alt=""><figcaption></figcaption></figure>

Com este card você pode especificar o nome de um workflow que deve ser executado após o workflow atual, caso suas condições sejam atendidas, e após os then cards anteriores do workflow atual. Embora ele priorize workflows executáveis e ativos, também permite executar workflows desativados se o documento atender às condições do workflow.

### **Adding calculated surcharges into an existing column** <a href="#pekg4i18rshn" id="pekg4i18rshn"></a>

<figure><img src="https://lh7-us.googleusercontent.com/XYY1xsFpp7_-Bi0WOSbotiVzspDLdaufx_xgoopMHmxdZnSDhroLpb0AE_si5PhwMq1jHfndc9FwOte9MOoCoTP5_JUYawO5cr4uIctIDHmwVjz3KacQrLJd8iBQy5KY4N-dMaWEi3IeTcc5OBRNJk4" alt=""><figcaption></figcaption></figure>

Se você quiser adicionar todas as sobretaxas como um desconto negativo na coluna de desconto, você pode usar o calculation card. Pode haver entradas nesta coluna; você pode defini-la como uma das variáveis no card, ter o MTZ subtraído dela e adicionar o resultado de volta a esta coluna. Caso existam campos vazios (sobretaxas apenas para alguns itens), ele assumirá 0 para o seu cálculo.

**Notify user to authorize the order confirmation in DocBits**

Após calcular as sobretaxas, você pode querer notificar um usuário específico para autorizar a confirmação de pedido. Para isso, você pode usar o notification card.

<figure><img src="../../.gitbook/assets/workflow_notification_card_overview.png" alt="Workflow Notification Card"><figcaption></figcaption></figure>

Dependendo das configurações, o usuário recebe uma nova tarefa atribuída no DocBits e, opcionalmente, um e-mail para notificá-lo sobre sua nova tarefa.
