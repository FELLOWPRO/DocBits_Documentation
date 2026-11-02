# Fornecedores e Pedidos de Compra

## **Ponto de ligação**

Você precisará criar o connection point da API do DocBits para poder criar o data flow mais adiante.

Primeiro, no InforOS, acesse ION Desk → Connect → Connection Points

![Navegação do ION Desk com o grupo Connect expandido e as entradas Data Flows, API Flows, Mappings, Connection Points e File Templates](https://lh7-us.googleusercontent.com/852EogukgFvteFTdg6_a6MPLaBUUqDw1J4x4H2q9BMjaVzZIGlpASC_fImhvAxe-nPBvIvOPFTI0oG8D3RlkAHiFDbLsVrsjaJMD1B5otXyIzPDkvoJvrj-JvMEHao73jgcZ5aKLAP4fCpkP7XV08JE)

Nessa tela, você precisará criar um novo connection point.

![Página Connection Points do ION Desk com o grupo Connect aberto na navegação e o caminho Home e Connection Points](https://lh7-us.googleusercontent.com/eh1NyUDTS0k-59ePv89PjZpfh5IT0iyFPoV5M9xmo3fmai-Iz0ptQFXgI9onZM-sTICHii32MkAw22AhZZAT5iKs_Hjw3_NDT49XG_KRONAvyK4OuL-bX667F9UGr-juckRmcE2hATOkSQ5x8QlugxU)

**Selecione API**

Dê ao connection point um nome e uma descrição que indiquem sua natureza e seu ambiente. Na guia Connection, importe a conta de serviço que você criou para o ambiente com o qual está trabalhando.

![Janela API Connection Point DocBits-DEV-Demo-Import com os separadores Usage, Connection e Documents, o nome DocBits-DEV-Demo-Import, a entrada de autenticação DocBits-DEV-Demo-Import Service Account e o Logical ID infor.api.docbits-dev-demo-import](https://lh7-us.googleusercontent.com/WZKJSckXWzztmEHmySnz6oDSbgFDvPmxku48HCiDJn7O1vTUcpUBYnwDHMT_Ja8aSGd8sFm-YQQYzyn5DnYLw77PQeFwTxcOV6C9aPWHyj2VofevH4S6ciyduIUy5YaNvmuNV6WgVJKOZ89_6oJjuq0)

Em seguida, passe para a guia Documents. Você precisará adicionar os seguintes BODs ao connection point.

![Separador Documents do ponto de ligação com as linhas Ack-SupplierInvoice, Sync.PurchaseOrder e Sync.ReceiveDelivery, cada uma com a direção In e o BOD com o mesmo nome](https://lh7-us.googleusercontent.com/3Q4XIpxXLixaDqXhh7CRKPl0yUwBce34CqLfw0BGS1UFXsvFIaxD6XelEgbnwfYFUCa5En-C1oAZR74C4lQ15as_M7JIQ20Nf9ZVmrVK8zCGuLS2YtphX4bgQ5uOwS2-MJLLZvsflDC31XLrTZzTKCg)

* Ack-SupplierInvoice

Este BOD é usado para sinalizar ao DocBits que ocorreu um erro no Infor. A configuração desses dois BODs deve ser semelhante à seguinte (o API Call Name muda em cada um)

![Configuração do BOD com os separadores Input Document, ION API, Request Parameters, Request Body e Settings e o API Call Name Ack-SupplierInvoice](https://lh7-us.googleusercontent.com/vmcVsltij144O3NeysAS2YduFNds98X_VJOpn6v356vAZI3v10SO8-ZMBd7zWyBUJKR9-UMQgGcT2U34HdGgpQ8rhtbFxsmuhgwJ_K6qXbtu04AP67G8jrNwkdj32LCgAhy_m4tnFQJApQehnfX8w5Y)

* Sync.PurchaseOrder

A configuração deste BOD deve ser semelhante à seguinte

![Configuração do BOD com os separadores Input Document, ION API, Request Parameters, Request Body e Settings e os campos API Call Name Sync.PurchaseOrder, Product DocBits-DEV e a operação POST CustomerApi/DocBits-DEV/prod/import/purchase_order_bod](https://lh7-us.googleusercontent.com/LPmOwFuzOnYNjwcKDfpI2S-IYJPKhjHYy4xKSUtB7EXSmPGfnG1lDfR-q6fdk4Uh9QBr-PIWjkpW3clbq31z8BP4_CGgoryKguS4GhR44gCG8xt6FJxRvqV-1i5Ul_3-wFjmiroYcchb5Ou5wBA0DF0)

* Sync.ReceiveDelivery

A configuração deste BOD deve ser semelhante à seguinte

![Configuração do BOD com os separadores Input Document, ION API, Request Parameters, Request Body e Settings e o API Call Name Sync.ReceiveDelivery](https://lh7-us.googleusercontent.com/75TPWASsqnzrWdeoyHZ4T23Zm5DbctQLOZKVe4N05ni32ecs0kZmBAihWnr7j0J7TisLvF2lncmUbEGGF9dKz8glVcRe7pmCvmEx8TMTesh0zGeewNpveNIsQqw-gkHvcITTF4a067MhoMgY8Jp6Prc)

Depois que esses BODs estiverem configurados, você pode salvar o connection point clicando no ícone localizado à direita do botão Voltar.

## **Fluxo de dados**

O data flow será semelhante ao seguinte

![Fluxo de dados no ION Desk com um nó de ponto de ligação DocBits à esquerda e o nó End à direita](https://lh7-us.googleusercontent.com/yhSunSyXrzx2Q0VIulIa6b989LxG36g5-kyYXGwniU0okKb3cJWDe65GYhpOfkHWTYJR4xdT85Us2Ba7tHhoJsE51I-g-82ZQ2bRM5zkgF5VmaRSno8M5bfhMCbUAw4-xx5oEudkqZWYoeIUUYhJPDU)

(O motivo de haver várias APIs do DocBits é que cada conexão representa um ambiente diferente; ou seja, dependendo da quantidade de ambientes que você tem, o seu data flow pode ser um pouco diferente)

Para esta explicação, usaremos o exemplo de quatro ambientes separados.

### **LN**

O início do data flow é a sua aplicação LN

### **API DocBits**

Aqui você adicionará uma aplicação e selecionará a(s) API(s) do DocBits que criou anteriormente

### **Ficheiros**

A configuração deve ser a seguinte

![Detalhe do fluxo de dados com o nó DocBits DocBits-DEV-P, os marcadores Start e Ende e um segundo nó DocBits ao centro, e o painel Dokumente com Sync.PurchaseOrder, Sync.ReceiveDelivery, Sync.RemitToPartyMaster e Sync.SupplierPartyMaster](https://lh7-us.googleusercontent.com/OEG6wQFd9LT6J_Ttcsdj7GgM2bTxrS-dpO2EbcVx4vGH1NLtZyaRTbYnr4-SDIWL2hk1zeVGr3bjuebNmwAMEx0S0U7xmNGztp-8HVjRLYyc-3lbQBL8lDU_TahhNxBugX_Bnu3QjZsKHX0Pafae-zU)

## **Acionamento de BODs no LN**

Depois de concluir todas as etapas acima, você precisará acessar o Infor LN e acionar os BODs para que os diversos dados mestres necessários para Fornecedores e Pedidos de Compra cheguem ao DocBits.

![Página inicial do Infor LN com o painel de favoritos à esquerda e os mosaicos de encomendas, faturas e ordens de armazém](https://lh7-us.googleusercontent.com/b6IsSx-x5Ri0cfYU9TTpgipqsoCkDPTxXdKoMBPaumyaopp-NRAJhoNnBfksnVVdz9Y26M0KlfdcKP4S1n_PjcTYKIu3MbVMQIfuIaTYYAL2ctyYsp29mEOrVh2TxmLPkUofeqJQ8nvBQbTOwj0-V0Y)

### **PurchaseOrder**

No menu acima, na guia de menu à esquerda, selecione Common → BOD-Messaging → Publish BODs → Publish Order Management Transactional Data

Selecione a guia PurchaseOrder e marque a caixa de seleção.

![Janela Publish Order Management Transactional Data com os botões PROCESS, CLOSE, SELECT ALL e CLEAR ALL, o separador PurchaseOrder selecionado e a árvore à esquerda com BOD Messaging e Publish BODs expandidos](https://lh7-us.googleusercontent.com/UJlicSuDjbEVtr_pzOeqkP8kkiBJIdAgzPK46FlhubqIIHiaJRYp27B__08e9IcNHdcctrBeBfZ6vFPQI3Xf3duL6R2Hu-iaL9dY7hANmy8ukiL61CTxcel0jd_66GAySp3dC1ptYKBaqLqaP1TwJco)

### **Fornecedores**

Na página inicial do LN, na guia de menu à esquerda, acesse Common → BOD-Messaging → Publish BODs → Publish Logistics Master Data

Selecione a guia PartyMaster e marque a caixa Supplier → Buy-from ou SupplierPartyMaster.

![Janela Publish Logistic Master Data com os botões PROCESS, CLOSE, SELECT ALL e CLEAR ALL, o separador PartyMaster selecionado e a grelha com as colunas Supplier, Buy-from PartyMaster, Pay-to PartyMaster, Pay-from PartyMaster e Remit-to PartyMaster](https://lh7-us.googleusercontent.com/KY_cFaUegEZmqAlcsBLVOTaxKOkkBkMeaQUbv996H946oOa-jvxB3lDqrkWV-17elt0mZDGews6Lr_6ojbFXtReDnV1PmqzwLXfE-IX5fKJr2IeJkAdnf1R9Sk5WYoxOLGolgo2MPQ3SNeoPnQ-ysy0)

### **Acionamento dos BODs**

Depois de marcar todos os BODs corretos para publicação, selecione a guia Options.

As opções a seguir devem ser selecionadas.

![Janela Publish Logistic Master Data com o seletor Mode, a secção Selection Range com a empresa 0051 e a secção BOD Messaging Settings](https://lh7-us.googleusercontent.com/7KpYALL1XL0pqWLRCPFng8-WT8IWI4o9lEtrp2zAN5bOBnYdz-6EHfAPc_StaY9raJTWbfrksra9UUxyQAQdtg4nOZggpHox3AV3C_cL9xhDAdHV4n79yyCfbyGH2NmS30fQGfsLTe_4_tXKy54nI8U)

Depois disso, clique no botão PROCESS e os BODs serão acionados. Uma mensagem será exibida na tela para informar que os BODs foram acionados.

![Janela Publish Logistic Master Data com as caixas Show Verb, Logical IDxs, Use ProcessSync Verb e Logging na secção BOD Messaging Settings e os botões PROCESS, CLOSE, SELECT ALL e CLEAR ALL](https://lh7-us.googleusercontent.com/BPX5vIBHIFv641srJPwW-19Dx1N1T2QnadGwVMQu-6pBZUxnUdOjdY1olMqorIyN_oeTBqz_1knMoYsSxEA-_NtGVx_j9dBixvOfic8rKJDT91tYqwSSLNpk8YkMW8ndelpH9_fzrTZUCMs_vnoxbvM)

Se tudo correu bem, as tabelas de Fornecedores e de Pedidos de Compra agora devem estar disponíveis em Configurações → Master Data Lookup.

\\
