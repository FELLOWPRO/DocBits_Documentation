# Fornecedores e pedidos de compra do Infor LN

Este exemplo descreve a rota do Infor ION para os BODs de fornecedores e de ordens de compra e onde verificá-los no DocBits. As quatorze capturas de tela do Infor abaixo são exemplos históricos de um tenant. Confirme os pontos de conexão, os nomes das chamadas de API e as opções de publicação do LN com o administrador da integração; eles não foram verificados em um tenant Infor para esta atualização. Nenhum BOD foi publicado ou importado durante esta atualização.

O Infor descreve o [publicador de dados mestres logísticos do LN](https://docs.infor.com/ln/latest/en-us/lnolh/tcolh/help/tc/bod/tcbod0200m000.html) e o [publicador transacional do Order Management](https://docs.infor.com/ln/2025.x/en-us/lnolh/tdolh/help/td/bod/tdbod0200m000.html). Seus modos têm efeitos diferentes: **Count** informa os totais de registros sem publicar; **Simulate** gera um resultado de teste sem confirmar a publicação; **Publish** envia os dados selecionados. A publicação pode alcançar todos os assinantes, portanto verifique o intervalo de empresas e os assinantes antes de executá-la.

## **Ponto de ligação**

Você precisará criar o connection point da API do DocBits para poder criar o fluxo de dados mais adiante.

Primeiro, no InforOS, acesse ION Desk → Connect → Connection Points

<figure><img src="https://lh7-us.googleusercontent.com/852EogukgFvteFTdg6_a6MPLaBUUqDw1J4x4H2q9BMjaVzZIGlpASC_fImhvAxe-nPBvIvOPFTI0oG8D3RlkAHiFDbLsVrsjaJMD1B5otXyIzPDkvoJvrj-JvMEHao73jgcZ5aKLAP4fCpkP7XV08JE" alt="Navegação histórica do Infor ION Desk com Connect expandido e Connection Points destacado."><figcaption><p>Exemplo de navegação histórico: ION Desk → Connect → Connection Points.</p></figcaption></figure>

Nessa tela, você precisará criar um novo connection point.

<figure><img src="https://lh7-us.googleusercontent.com/eh1NyUDTS0k-59ePv89PjZpfh5IT0iyFPoV5M9xmo3fmai-Iz0ptQFXgI9onZM-sTICHii32MkAw22AhZZAT5iKs_Hjw3_NDT49XG_KRONAvyK4OuL-bX667F9UGr-juckRmcE2hATOkSQ5x8QlugxU" alt="Tela histórica de Connection Points com uma seta verde apontando para Add."><figcaption><p>Escolha Add para criar um connection point; a anotação verde marca a ação nesta interface histórica.</p></figcaption></figure>

**Selecione API**

Dê ao connection point um nome e uma descrição que indiquem sua natureza e seu ambiente. Na guia Connection, importe a conta de serviço que você criou para o ambiente com o qual está trabalhando.

<figure><img src="https://lh7-us.googleusercontent.com/WZKJSckXWzztmEHmySnz6oDSbgFDvPmxku48HCiDJn7O1vTUcpUBYnwDHMT_Ja8aSGd8sFm-YQQYzyn5DnYLw77PQeFwTxcOV6C9aPWHyj2VofevH4S6ciyduIUy5YaNvmuNV6WgVJKOZ89_6oJjuq0" alt="Connection point de API histórico DocBits-DEV-Demo-Import com Connection selecionado e um controle Import da conta de serviço."><figcaption><p>Guia Connection histórica. Os nomes da conta de serviço e da conexão exibidos pertencem ao ambiente de exemplo.</p></figcaption></figure>

Em seguida, passe para a guia Documents. Você precisará adicionar os seguintes BODs ao connection point.

<figure><img src="https://lh7-us.googleusercontent.com/3Q4XIpxXLixaDqXhh7CRKPl0yUwBce34CqLfw0BGS1UFXsvFIaxD6XelEgbnwfYFUCa5En-C1oAZR74C4lQ15as_M7JIQ20Nf9ZVmrVK8zCGuLS2YtphX4bgQ5uOwS2-MJLLZvsflDC31XLrTZzTKCg" alt="Guia Dokumente (Documents) histórica em alemão, listando as chamadas de API Ack-SupplierInvoice, Sync.PurchaseOrder e Sync.ReceiveDelivery e os BODs recebidos."><figcaption><p>Guia Dokumente (Documents) histórica. Este recorte mostra três rotas; não mostra a configuração completa de fornecedores.</p></figcaption></figure>

* Ack-SupplierInvoice

Este BOD serve para sinalizar ao DocBits que ocorreu um erro no Infor. A rota Acknowledge.SupplierInvoice mostrada abaixo é um exemplo de confirmação de faturas. Confirme o nome da chamada de API e se essa rota é necessária para o seu fluxo de fornecedores e ordens de compra.

<figure><img src="https://lh7-us.googleusercontent.com/vmcVsltij144O3NeysAS2YduFNds98X_VJOpn6v356vAZI3v10SO8-ZMBd7zWyBUJKR9-UMQgGcT2U34HdGgpQ8rhtbFxsmuhgwJ_K6qXbtu04AP67G8jrNwkdj32LCgAhy_m4tnFQJApQehnfX8w5Y" alt="Guia ION API histórica em alemão para Ack-SupplierInvoice com uma operação POST selecionada."><figcaption><p>Rota de confirmação histórica. Ack-SupplierInvoice é um nome de chamada de API de exemplo; Acknowledge.SupplierInvoice é o BOD recebido.</p></figcaption></figure>

* Sync.PurchaseOrder

O exemplo histórico abaixo mostra uma operação de recebimento; confirme a operação e o formato da requisição atuais para o seu ambiente.

<figure><img src="https://lh7-us.googleusercontent.com/LPmOwFuzOnYNjwcKDfpI2S-IYJPKhjHYy4xKSUtB7EXSmPGfnG1lDfR-q6fdk4Uh9QBr-PIWjkpW3clbq31z8BP4_CGgoryKguS4GhR44gCG8xt6FJxRvqV-1i5Ul_3-wFjmiroYcchb5Ou5wBA0DF0" alt="Guia ION API histórica com Send to API selecionado para Sync.PurchaseOrder e uma operação POST configurada."><figcaption><p>Rota histórica de ordens de compra. Verifique a operação de recebimento do seu ambiente DocBits em vez de copiar o caminho antigo do proxy.</p></figcaption></figure>

* Sync.ReceiveDelivery

O exemplo histórico abaixo mostra uma operação de recebimento; confirme a operação e o formato da requisição atuais para o seu ambiente.

<figure><img src="https://lh7-us.googleusercontent.com/75TPWASsqnzrWdeoyHZ4T23Zm5DbctQLOZKVe4N05ni32ecs0kZmBAihWnr7j0J7TisLvF2lncmUbEGGF9dKz8glVcRe7pmCvmEx8TMTesh0zGeewNpveNIsQqw-gkHvcITTF4a067MhoMgY8Jp6Prc" alt="Guia ION API histórica em alemão para Sync.ReceiveDelivery com uma operação POST configurada."><figcaption><p>Rota histórica de dados de recebimento. Confirme se ReceiveDelivery é necessário para a sua integração e qual operação o recebe.</p></figcaption></figure>

Depois de configurar esses BODs, você pode salvar o connection point pressionando o ícone à direita do botão Voltar.

## **Fluxo de dados**

O fluxo de dados terá um aspecto semelhante ao seguinte

<figure><img src="https://lh7-us.googleusercontent.com/yhSunSyXrzx2Q0VIulIa6b989LxG36g5-kyYXGwniU0okKb3cJWDe65GYhpOfkHWTYJR4xdT85Us2Ba7tHhoJsE51I-g-82ZQ2bRM5zkgF5VmaRSno8M5bfhMCbUAw4-xx5oEudkqZWYoeIUUYhJPDU" alt="Fluxo documental histórico de um nó LN por uma divisão paralela até quatro nós da API do DocBits, seguido de uma junção e do fim."><figcaption><p>Fluxo histórico com quatro ambientes. A divisão e a junção são visíveis; o número e os destinos dos nós dependem do seu projeto de integração.</p></figcaption></figure>

Os vários nós da API do DocBits neste exemplo histórico representam ambientes separados. Seu projeto de produção pode usar um número diferente de nós; nunca encaminhe dados de teste para uma organização de produção.

A ilustração a seguir usa quatro ambientes apenas como exemplo.

### **LN**

O início do fluxo de dados é a sua aplicação LN

### **API do DocBits**

Aqui você adicionará uma aplicação e selecionará as APIs do DocBits que criou anteriormente

### **Documentos**

Revise a lista de documentos atribuída ao fluxo. As mensagens de fornecedor mostradas aqui também precisam de rotas de recebimento correspondentes no connection point da API. A configuração das chamadas de API delas não aparece no recorte das três rotas anterior; confirme as operações necessárias com o administrador da integração.

<figure><img src="https://lh7-us.googleusercontent.com/OEG6wQFd9LT6J_Ttcsdj7GgM2bTxrS-dpO2EbcVx4vGH1NLtZyaRTbYnr4-SDIWL2hk1zeVGr3bjuebNmwAMEx0S0U7xmNGztp-8HVjRLYyc-3lbQBL8lDU_TahhNxBugX_Bnu3QjZsKHX0Pafae-zU" alt="Área de desenho histórica do fluxo com o painel Dokumente em alemão abaixo, listando Sync.PurchaseOrder, Sync.ReceiveDelivery, Sync.RemitToPartyMaster e Sync.SupplierPartyMaster."><figcaption><p>Lista de documentos histórica do fluxo. As mensagens de fornecedor aparecem aqui junto com as mensagens de ordem de compra e de recebimento.</p></figcaption></figure>

## **Acionamento de BOD no LN**

Depois que o administrador da integração tiver verificado o connection point, as rotas de documentos e o fluxo de dados ativo, use a sessão de publicação apropriada do LN. Acompanhe cada identificador de teste pelo LN, pelo ION e pelo DocBits; acionar um BOD sozinho não prova que um registro chegou.

<figure><img src="https://lh7-us.googleusercontent.com/b6IsSx-x5Ri0cfYU9TTpgipqsoCkDPTxXdKoMBPaumyaopp-NRAJhoNnBfksnVVdz9Y26M0KlfdcKP4S1n_PjcTYKIu3MbVMQIfuIaTYYAL2ctyYsp29mEOrVh2TxmLPkUofeqJQ8nvBQbTOwj0-V0Y" alt="Página inicial histórica do Infor LN em alemão com uma lista de favoritos; o menu Publish BODs não está aberto."><figcaption><p>Página inicial histórica do LN. Use a navegação descrita abaixo para encontrar a sessão de publicação apropriada.</p></figcaption></figure>

### **PurchaseOrder**

No menu acima, na aba de menu à esquerda, selecione Common → BOD-Messaging → Publish BODs → Publish Order Management Transactional Data

Selecione a aba PurchaseOrder e marque a caixa.

<figure><img src="https://lh7-us.googleusercontent.com/UJlicSuDjbEVtr_pzOeqkP8kkiBJIdAgzPK46FlhubqIIHiaJRYp27B__08e9IcNHdcctrBeBfZ6vFPQI3Xf3duL6R2Hu-iaL9dY7hANmy8ukiL61CTxcel0jd_66GAySp3dC1ptYKBaqLqaP1TwJco" alt="Sessão histórica Publish Order Management Transactional Data com a aba PurchaseOrder e a caixa marcadas e os campos de intervalo de ordens visíveis."><figcaption><p>Seleção histórica de PurchaseOrder. Verifique o intervalo de ordens e os status antes de publicar.</p></figcaption></figure>

### **Fornecedores**

Na página inicial do LN, na aba de menu à esquerda, acesse Common → BOD-Messaging → Publish BODs → Publish Logistics Master Data

Selecione a aba PartyMaster e marque a caixa Supplier → Buy-from ou SupplierPartyMaster.

<figure><img src="https://lh7-us.googleusercontent.com/KY_cFaUegEZmqAlcsBLVOTaxKOkkBkMeaQUbv996H946oOa-jvxB3lDqrkWV-17elt0mZDGews6Lr_6ojbFXtReDnV1PmqzwLXfE-IX5fKJr2IeJkAdnf1R9Sk5WYoxOLGolgo2MPQ3SNeoPnQ-ysy0" alt="Sessão histórica Publish Logistic Master Data com PartyMaster selecionado e a caixa Supplier Buy-from marcada."><figcaption><p>Seleção histórica de fornecedores em PartyMaster. Escolha as funções de parceiro exigidas pela sua integração e verifique o intervalo de seleção.</p></figcaption></figure>

### **Acionamento do BOD**

Depois de marcar para publicação todos os BODs corretos, selecione a aba Options.

Revise as opções do seu tenant. O exemplo histórico destaca Publish e Use Process/Sync Verb; elas não são configurações válidas para toda integração.

<figure><img src="https://lh7-us.googleusercontent.com/7KpYALL1XL0pqWLRCPFng8-WT8IWI4o9lEtrp2zAN5bOBnYdz-6EHfAPc_StaY9raJTWbfrksra9UUxyQAQdtg4nOZggpHox3AV3C_cL9xhDAdHV4n79yyCfbyGH2NmS30fQGfsLTe_4_tXKy54nI8U" alt="Aba Options histórica do LN com Publish e Use Process/Sync Verb destacados e um intervalo de empresas visível."><figcaption><p>Exemplo histórico da aba Options. Publish e Use Process/Sync Verb estão selecionados aqui; verifique modo, intervalo de empresas e assinantes para a sua execução.</p></figcaption></figure>

Antes de **Process**, use **Count** ou **Simulate** e inspecione a contagem de registros e o intervalo de empresas quando a sua versão do LN oferecer esses modos. Publique apenas com a aprovação do administrador da integração. Uma confirmação de que os BODs foram acionados não prova a entrega ao DocBits.

<figure><img src="https://lh7-us.googleusercontent.com/BPX5vIBHIFv641srJPwW-19Dx1N1T2QnadGwVMQu-6pBZUxnUdOjdY1olMqorIyN_oeTBqz_1knMoYsSxEA-_NtGVx_j9dBixvOfic8rKJDT91tYqwSSLNpk8YkMW8ndelpH9_fzrTZUCMs_vnoxbvM" alt="Aba Options histórica do LN com o botão Process destacado antes da execução."><figcaption><p>Ação Process histórica antes da execução. Esta captura não contém resultado de publicação nem confirmação de que o DocBits recebeu dados.</p></figcaption></figure>

## Verificar no DocBits

Verifique no Infor ION se a entrega para a organização do DocBits pretendida foi bem-sucedida. Depois abra **Configurações → Processamento de documentos → Pesquisar Dados Mestres**. Em **Dados de entrada do BOD**, abra **Fornecedor**. Escolha o campo identificador em **Pesquisar por coluna**, informe um número ou nome de fornecedor conhecido em **Procurar Texto** e use a lupa para pesquisar. Abra **Ordem de compra** e pesquise um número de ordem conhecido. Verifique também **Cabeçalho do pedido de compra** se o seu mapeamento separa cabeçalho e linhas. Compare os identificadores e a empresa com o LN; não conclua que todos os registros chegaram apenas porque a mensagem de publicação foi bem-sucedida. Na interface em português, os cabeçalhos das colunas da tabela continuam em inglês, por exemplo Supplier Id e Supplier Name.

<figure><img src="../../../../.gitbook/assets/dbdc-1149-supplier-pt-20261112.png" alt="Vista Fornecedor de Pesquisar Dados Mestres no DocBits em português, com os campos Pesquisar por coluna e Procurar Texto e dez linhas de fornecedor de exemplo inventadas de SUP-1001 a SUP-1010."><figcaption><p>Vista de verificação de fornecedores na versão 11.27.7 do sandbox com linhas de exemplo inventadas. Pesquise um identificador de teste conhecido e compare com o LN e o ION.</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/dbdc-1149-purchase-order-pt-20261112.png" alt="Vista Ordem de compra de Pesquisar Dados Mestres no DocBits em português, com as abas Fornecedor e Ordem de compra, os mesmos campos de pesquisa e dez linhas de ordem de exemplo inventadas de PO-4500 a PO-4509."><figcaption><p>Vista de verificação de ordens de compra na versão 11.27.7 do sandbox com linhas de exemplo inventadas. As linhas não provam nenhuma importação do LN.</p></figcaption></figure>

As vistas em inglês no Dev foram verificadas em 29 de outubro de 2026 sem publicar BOD, importar arquivo ou alterar dados mestres; nessas imagens as linhas de registro ficaram fora do recorte. As duas capturas em português vêm da versão 11.27.7 do sandbox e mostram linhas de exemplo inventadas em vez de dados mestres reais; elas ilustram onde verificar, não uma transferência do LN concluída. Se o registro esperado estiver faltando, verifique os logs de publicação do LN, o roteamento do ION, a organização e o mapeamento dos BODs antes de tentar novamente.
