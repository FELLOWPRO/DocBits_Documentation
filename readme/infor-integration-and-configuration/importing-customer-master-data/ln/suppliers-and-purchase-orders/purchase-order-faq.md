# Pedido de Compra - FAQ

**Onde verifico se as atualizações de sincronização do PurchaseOrderBOD estão implementadas corretamente?**

Acesse a sessão _BOD Implementation Registration (bobod1100m000)_ no LN. Essa sessão permite revisar, modificar e registrar implementações de BOD padrão e personalizadas, incluindo o PurchaseOrderBOD.

\


<figure><img src="../../../../.gitbook/assets/PO.png" alt=""><figcaption></figcaption></figure>

**Como identifico a implementação de BOD específica que preciso verificar?**

Procure os campos BOD Implementation Identifier e BOD Name. O BOD Name normalmente indica o tipo de BOD (por exemplo, PurchaseOrderBOD). O BOD Implementation Identifier é um identificador único dessa configuração de BOD.

\


**O que significa a caixa de seleção ‘Public’ na sessão BOD Implementation Registration?**

A caixa de seleção Public indica se a implementação do BOD está disponível para comunicação externa.

• Marcada: o BOD pode ser trocado fora do LN (interface pública e protegida).

• Desmarcada: o BOD é usado apenas no processamento interno do LN (interface protegida).

\


**Vejo um campo ‘Parent BOD Name’. Para que ele serve?**

O campo Parent BOD Name mostra o BOD pai, caso o BOD atual seja uma versão derivada ou dependente. Se a caixa de seleção Public estiver marcada, esse campo ficará vazio. Caso contrário, ele ajuda a entender a hierarquia das implementações de BOD.

\


**Como sei se a implementação do BOD é padrão ou personalizada?**

Verifique a caixa de seleção Standard.

• Marcada: o BOD é uma implementação padrão, fornecida pelo LN.

• Desmarcada: o BOD é uma implementação personalizada, definida pela sua equipe ou por um parceiro.

\


**Qual é a finalidade da caixa de seleção ‘Staging’?**

Se a caixa de seleção Staging estiver marcada, os BODs são primeiro colocados em área de preparação (staging), em vez de serem publicados imediatamente. Depois, eles podem ser publicados pela sessão _Publish Staged BODs (bobod2200m000)_.

Observação: para o ProjectBudgetBOD, o staging é obrigatório e não pode ser alterado. Para os BODs padrão de dados mestres, o staging pode ser ativado manualmente e, para BODs personalizados, ele sempre pode ser configurado.

\


**Como a caixa de seleção ‘Synchronous Processing’ afeta o tratamento de BODs recebidos?**

O Synchronous Processing determina a ação a ser tomada caso um processo subsequente falhe após o recebimento de um BOD.

• Marcada: o BOD recebido e o processo subsequente precisam ser bem-sucedidos; caso contrário, nenhum dos dois será processado.

• Desmarcada: o BOD recebido é processado, mas, se o processo subsequente falhar, ele deverá ser tratado manualmente.

\


**Onde verifico se o recurso ‘Stage’ está ativo ou não para o meu BOD?**

Na sessão _BOD Implementation Registration (bobod1100m000)_, verifique a caixa de seleção Staging. Se ela não estiver marcada, o staging não está ativo para esse BOD específico.

\


**Se o PurchaseOrderBOD não for acionado em todas as atualizações, o que mais devo considerar?**

• Confirme se a opção Staging está definida conforme o pretendido. Se o staging estiver desativado, o BOD deve ser publicado imediatamente.

• Verifique se a configuração de Synchronous Processing está correta para o seu fluxo de trabalho.

• Certifique-se de que o BOD Implementation Identifier e o BOD Name estão corretos e de que você está trabalhando na configuração de BOD adequada.

• Verifique se o BOD é padrão ou personalizado e se alguma configuração personalizada substitui o comportamento padrão.

\


**Existem cenários em que eu possa não ver as atualizações do PurchaseOrderBOD como esperado?**

Sim. Se o BOD não estiver configurado corretamente (configurações erradas em Public, Staging ou Synchronous Processing) ou se for uma implementação de BOD personalizada que não esteja alinhada aos requisitos do seu processo, as atualizações podem não ser acionadas como esperado. Revise sua configuração na sessão _bobod1100m000_ e verifique se todos os parâmetros correspondem ao fluxo de processo desejado.
