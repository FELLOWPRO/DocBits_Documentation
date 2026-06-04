# Workflow Documentation

**Workflow Documentation**

Para manter uma visão geral, pode atribuir aos fluxos de trabalho diferentes títulos, de modo a saber imediatamente a que tarefa se refere cada fluxo de trabalho.

Criar um novo fluxo de trabalho: Clique em + ADD WORKFLOW

![](<../../../.gitbook/assets/0 (1).png>)

Pode utilizar estes fluxos de trabalho (Test 1,2,3) para atribuir automaticamente vários documentos ao colaborador certo na empresa.

![](<../../../.gitbook/assets/1 (1).png>)

Se uma fatura ou outro documento exceder um determinado montante total que exija revisão e aprovação prévias, estes documentos podem ser imediatamente atribuídos à pessoa correta.

<figure><img src="../../../.gitbook/assets/docbits_error_approval.png" alt="DocBits Erro Aprovação"><figcaption></figcaption></figure>

**Test 1:              Logic Card**

When:             **Assignee is:**                    Amier Haider

And:                **Document type is:**        Invoice

Then:              **Assign document to:**   Stefan Reppermund

![](<../../../.gitbook/assets/3 (1).png>)

**Test 2:              Logic Card**

When:              **Assignee is:**                    Amier Haider

And:                 **Document type is:**        Delivery Note

Then:               **Assign document to:**   James Edwards

![](<../../../.gitbook/assets/4 (1).png>)

**Test 3:             Logic Card**

**When:**             **Assignee is:**                    Amier Haider

**And:**                **Document type is:**        Order Confirmation

**Then:**              **Assign document to:**   Anian Sollinger

![](<../../../.gitbook/assets/5 (1).png>)





Também é possível, caso o documento não seja atribuído a uma única pessoa, atribuí-lo desde o início a um colaborador específico.

<figure><img src="../../../.gitbook/assets/docbits_workflow_purchase_order_6.png" alt="DocBits Fluxo de trabalho Compra Pedido 6" width="375"><figcaption></figcaption></figure>





Para uma visão geral mais fácil do que deve acontecer a um documento, pode definir o estado dos documentos recebidos neste fluxo de trabalho. Este fluxo de trabalho permite ver imediatamente se existe, por exemplo, uma aprovação pendente.



**Test 4:             Logic Card**

**When:**             **Document type is:**         Delivery Note

**And:**                **Assignee is:**                     Amier Haider

**Then:**              **Change Status to:**         Pending Approval

<figure><img src="../../../.gitbook/assets/docbits_workflow_purchase_order_7.png" alt="DocBits Fluxo de trabalho Compra Pedido 7"><figcaption></figcaption></figure>

![](<../../../.gitbook/assets/8 (1).png>)



**Test 5:                Logic Card**

When:                **Document type is:**           Invoice

And:                   **Assignee is:**                       Stefan Reppermund

Then:                 **Change Status to:**           Pending Second Approval

<figure><img src="../../../.gitbook/assets/docbits_approval_supplier.png" alt="DocBits Aprovação Fornecedor"><figcaption></figcaption></figure>

![](<../../../.gitbook/assets/10 (1).png>)





Se uma fatura ou outro documento exceder um determinado montante total que exija revisão e aprovação prévias, estes documentos podem ser imediatamente atribuídos à pessoa certa.

![](<../../../.gitbook/assets/11 (1).png>)



**Test 6:                    Logic Card**

When:                   **Assignee is:**                   Amier Haider

And:                      Docfield        **total\_amount**     is      **Greater than       500**

Then:                    **Assign document to:**   Asad Usman Khan

<figure><img src="../../../.gitbook/assets/docbits_purchase_order_table.png" alt="DocBits Compra Pedido Tabela"><figcaption></figcaption></figure>

![](<../../../.gitbook/assets/13 (1).png>)



Também é possível introduzir o estado no fluxo de trabalho, para que a pessoa atribuída possa ver imediatamente em que estado se encontra o documento e o que deve acontecer a seguir com ele.



**Test 7:                 Logic Card**

**When:** **Assignee is:**                     Amier Haider

**And:**                   Docfield           **total\_amount**      is        **Greater then      500**

**Then:**                 **Assign document to:**     Asad Usman Khan

&#x20;                            **Change Status to:**          Pending Approval

<figure><img src="../../../.gitbook/assets/docbits_approval.png" alt="DocBits Aprovação"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/docbits_workflow_purchase_order_2.png" alt="DocBits Fluxo de trabalho Compra Pedido 2"><figcaption></figcaption></figure>





Por exemplo, se faltarem informações específicas ou importantes num documento, mas que sejam relevantes e tenham de ser incluídas para processamento adicional, pode configurar o fluxo de trabalho de modo a que estes documentos sejam imediatamente encaminhados para o comprador e para um substituto (suplente).

<figure><img src="../../../.gitbook/assets/docbits_settings_workflow_2.png" alt="DocBits Configurações Fluxo de trabalho 2"><figcaption></figcaption></figure>



**Test 9:**

O fluxo de trabalho com estes cartões lógicos foi concebido para verificar automaticamente se a quantidade, o preço unitário ou o desconto indicados numa confirmação de encomenda correspondem aos valores correspondentes na ordem de compra. Esta verificação garante a consistência e a exatidão entre aquilo que foi encomendado e aquilo que o fornecedor confirma entregar.

Pode atribuir a estes documentos um estado específico ou atribuí-los a um colaborador específico.

<div align="center">

<figure><img src="../../../.gitbook/assets/docbits_approval_2.png" alt="DocBits Aprovação 2"><figcaption></figcaption></figure>

</div>

<figure><img src="../../../.gitbook/assets/docbits_error_email.png" alt="DocBits Erro E-mail"><figcaption></figcaption></figure>

**Logic Card: Quantity or Unit Price or Discount Match**

Este cartão lógico foi concebido para verificar automaticamente se a quantidade, o preço unitário ou o desconto indicados numa confirmação de encomenda correspondem aos valores correspondentes na ordem de compra. Esta verificação garante a consistência e a exatidão entre aquilo que foi encomendado e aquilo que o fornecedor confirma entregar.



**Trigger Condition**

A lógica é ativada quando qualquer uma das seguintes condições é cumprida numa confirmação de encomenda relativamente à ordem de compra original:

* **Quantity**: A quantidade de artigos encomendados corresponde à quantidade confirmada pelo fornecedor.
* **Unit Price**: O preço por artigo acordado corresponde à confirmação do fornecedor.
* **Discount**: Quaisquer descontos aplicados são consistentes entre a ordem de compra e a confirmação da encomenda.



* **Define Comparison Parameters**: Configure os campos específicos (quantidade, preço unitário, desconto) que o cartão lógico irá verificar para uma correspondência.
* **Automate Verification**: Configure o sistema para comparar automaticamente estes detalhes aquando da receção de uma confirmação de encomenda.
* **Customize Alerts**: Decida o fluxo de trabalho para o tratamento de discrepâncias, incluindo a personalização de alertas para revisão manual.

Este cartão lógico é vital para garantir que os detalhes de uma confirmação de encomenda estão em conformidade com a ordem de compra original, salvaguardando a integridade do ciclo de aquisição.



**Test 10:**

Se tiver um cálculo diferente para sobretaxas, ou apenas as tiver em alguns artigos, pode utilizar os cartões genéricos de cálculo de tabelas; alguns deles permitem também filtrar por expressões regulares.

<figure><img src="../../../.gitbook/assets/docbits_table_invoice.png" alt="DocBits Tabela Fatura"><figcaption></figcaption></figure>

Acima encontra-se um exemplo de cálculo para MTZ com um filtro para números de artigo que começam por 01, 06, 9, 001 ou 000.



Numa configuração manual, é aconselhável separar os cálculos que dependem de novas colunas num fluxo de trabalho distinto. Para continuar com o cálculo, pode utilizar o cartão Run Workflow.

**Run Workflow**

<figure><img src="../../../.gitbook/assets/docbits_workflow_2.png" alt="DocBits Fluxo de trabalho 2"><figcaption></figcaption></figure>

Com este cartão, pode especificar o nome de um fluxo de trabalho a executar após o fluxo de trabalho atual, caso as suas condições sejam cumpridas e após os cartões "then" anteriores do fluxo de trabalho atual. Embora dê prioridade a fluxos de trabalho executáveis e ativos, também permite executar fluxos de trabalho desativados se o documento cumprir as condições desses fluxos de trabalho.

### **Adding calculated surcharges into an existing column** <a href="#pekg4i18rshn" id="pekg4i18rshn"></a>

<figure><img src="https://lh7-us.googleusercontent.com/XYY1xsFpp7_-Bi0WOSbotiVzspDLdaufx_xgoopMHmxdZnSDhroLpb0AE_si5PhwMq1jHfndc9FwOte9MOoCoTP5_JUYawO5cr4uIctIDHmwVjz3KacQrLJd8iBQy5KY4N-dMaWEi3IeTcc5OBRNJk4" alt=""><figcaption></figcaption></figure>

Se quiser adicionar todas as sobretaxas como um desconto negativo na coluna de desconto, pode utilizar o cartão de cálculo. Poderá haver entradas nesta coluna; pode defini-la como uma das variáveis no cartão, subtrair-lhe a MTZ e adicionar novamente o resultado a esta coluna. Caso existam campos vazios (sobretaxas apenas para alguns artigos), o sistema assumirá um 0 para o seu cálculo.

**Notify user to authorize the order confirmation in DocBits**

Após calcular as sobretaxas, poderá querer notificar um utilizador específico para autorizar a confirmação da encomenda. Para isso, pode utilizar o cartão de notificação.

<figure><img src="../../../.gitbook/assets/docbits_email_settings.png" alt="DocBits E-mail Configurações"><figcaption></figcaption></figure>

Dependendo das definições, o utilizador recebe uma nova tarefa no DocBits e, opcionalmente, um e-mail para o notificar da sua nova tarefa.
