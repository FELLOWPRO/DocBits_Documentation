# Códigos de imposto

## **Criar os pontos de ligação do DocBits**

Abra ION Desk → Connect → Connection Points.

![Infor ION Desk com o menu Connect aberto na visão geral dos Connection Points](https://lh7-us.googleusercontent.com/QLQB17W\_hywZWBqme8Wio-orbdOdFHXLv5zTd89B3EkeS0WCuuo5Pv1CndLRQ2rFUefvQYM95U2Unhrl3YU3WAR23Ij\_tDw\_TOEVenWjyCh-9H8CPFSezF2gmED7u5QTR7q9WV4CSXRvDqkmKJYPqAI)

Este fluxo de dados requer quatro pontos de ligação: três pontos API para as categorias de imposto normal, reduzido e isento e um ponto de aplicação que representa a sua empresa LN.

&#x20;Para criar pontos de ligação, selecione o botão «+ADD».

![Página Connection Points no ION Desk com o botão Add na barra de ferramentas](https://lh7-us.googleusercontent.com/cECLuIswRSK3WWhUMi1n3tm2AIcrksZdpz7ZCO6-H\_MzaKe9CDT0w1b7GKJ8GtT\_d6nvvDe4ukLJfWcMocbHZ5dSSCw25Ky7-JUdrYb893GYYyaHL9tTjG1ZniORJPLSu1zJxL3c-1VQRw4IC0LpYuA)

Selecione «API» no final da lista de opções.

![Menu de tipos de ponto de ligação com a opção API na parte inferior](https://lh7-us.googleusercontent.com/bpeLxdmi8b10LLMGy02vMRXuLoic9kFLywnpd6SSYV0fNv82dQahyvaA85mC1PEVScNW4m63fOw89vkhQr0-ou8VWOSjkwGWG5GnP7GQl77THtjXWP3YNo8LUzAstpCs0Q5fOjxaoT\_\_ZKM4jciHA5I)

Será apresentada a página seguinte.

![Página de novo ponto de ligação API no ION Desk com os campos Name, Description e conta de serviço](https://lh7-us.googleusercontent.com/4pcN0B7aibjn\_Qn8nMgkzRc\_NiXev-c1wJudDKo2V5r0ORuajVzfzAWnWu0Wt68hKMKSLYkieUhOYChkcZuCZDWkg-F22Rq2WvVqgPweSg3by2TGrrJHweKWTlf\_DK1X2pCkoNU4yoGo3DyHsoqcGjg)

Introduza aqui os dados do ponto de ligação TaxCode. Para cada um dos três pontos de ligação, efetue os passos seguintes.

* Introduza um nome: TaxCodeFull, TaxCodeReduced ou TaxCodeFree.
* Description (descrição): pode ser igual ou semelhante ao nome.
* Importe uma conta de serviço criada anteriormente.

Abra o separador «Documents» e selecione o ícone de adição para acrescentar o BOD necessário, como no exemplo abaixo.

![Separador Documents do ponto de ligação com o ícone mais e as opções de direção BOD Get from API, Send to API e Trigger API](https://lh7-us.googleusercontent.com/byhA18LzkcY9ZyfnzyDlru5qBx88E8U1yggMNNkoHGsYVCbNkflNFXGVvJwMvE\_104VCjoYOM0SQIJVniyBBdn5UKasVR0uat6UvmCmpzz9ZYsY2Wv14B4ElOwqcg2qklxYAQVU84UOG70l3fMLRrwo)

Procure o BOD.

![Diálogo Input Document foreground process para o pedido da ION API com os separadores Request Parameters, Request Body e Settings](https://lh7-us.googleusercontent.com/DAKzvEsjCmk1jy7L6GwrVY2DWg3\_InluNftWnR7hGlnyeBxSDW6XTDPBMLqtJuUc9Lq3Nga6-EKS4tZpOjE09h5FUJaTm\_E70UdA4l17jWGQ6BSr121lC3LzhffUXi6Bsk5EZEz4XHyjekk1Njb3H4I)

Procure «Sync.LnTaxCode», selecione-o e prima «OK» para adicionar o BOD.

![Lista de seleção de BOD com Sync.LnTaxCode selecionado e o botão OK](https://lh7-us.googleusercontent.com/7BLwrq8kr9OTHleI2anmAr2-4ChksQ0pptddwm1quFHquGfnMBEW32RFx31ETGbrxf0KGVr-VzlZC9h9heD3ymTq9L5NZEV1b9E67IIR0is18UGBCoJ5j7KIMmF533EDMvZzgi4LXqAkV9zgCyl0\_Lk)

Na secção ION API, pode utilizar o nome do BOD, Sync.LnTaxCode, no campo API Call Name.

Prima «SELECT».

![Página do ponto de ligação com a secção ION API, o campo API Call Name e o botão SELECT](https://lh7-us.googleusercontent.com/7MukO6oUAzVBFMPhFepwMvugqnhDDMhX9j7wZRU7BU0OusW3CKpMgqQNC7uNlehPp6eFniVxrX3DxjgsGZ\_Tmt\_cQOWGGiBfXAQfCC85amOGp1VY8RGo3nPABCiwzaIkYmnQF6t3FPVZ1fPV6fLazNc)

Selecione a API configurada para o ambiente em que está a trabalhar e procure a API indicada abaixo. Selecione-a e prima «OK».

![Diálogo ION API Operation que lista as operações de pesquisa de dados mestres do DocBits, como Import Xml File e Import Xml Data](https://lh7-us.googleusercontent.com/IpUUqJaXF0MmIeR6gtE9GDCccLfNsQLZ-RSHhQGVwJEj8WJwI-twgiHpFomBKhbnTUUKrhxJ0EUZ7F\_21MCSBjNS2VQq3azprekoxctRJZ-NJUHhb4J9rHUSRDoR\_OCzDHTG5q5KTwWMHOR5qNoNd38)

Abra o separador Request Body.

Os mapeamentos de campos variam ligeiramente entre os pontos de ligação das diferentes categorias de imposto.

![Separador Request Body com o corpo JSON e a entrada field_mappings para o código de imposto](https://lh7-us.googleusercontent.com/f4c-1M9mgCci2jjxkhaCDFX9bRWzMDaRwVv4XiaUH7BpHchPklvMnWoP\_ILSm6VB7GoFJNJzHsEPzk3eCFyLm1Kc3QI8OufjQ1mr7PqowjzViFDWc2opiNE1ODICtI9yEyUOi\_d\_hzN8CGo8gu6Ec84)

Na linha field\_mappings, na coluna de valor, introduza o mapeamento específico da categoria do ponto de ligação: normal, reduzido ou isento. Os mapeamentos estão disponíveis em https://docbits.com/doc/field-mappings/.

O resultado deve ser semelhante à imagem acima. Depois, clique em SAVE no local indicado.

![Menu no ION Desk com a opção SAVE para o ponto de ligação](https://lh7-us.googleusercontent.com/LSYrbElw6BgQbbIdSstbakfwLENZ\_09WQcQhjO7kbb2U3jSK\_\_wFnr43tIj2hTHYegQ9lrSZBuJ9N7MNewr2W3yjPCrrVLeP9UAZjvrKKBzeY9h-q6FrVd5gPtlH0iP0GpMcvhGxjAnHN7BlY8CmT3c)

## **Configurar o fluxo de dados**

Abra ION Desk → Connect → Data Flows.

![Infor ION Desk com o menu Connect aberto na descrição geral dos Data Flows](https://lh7-us.googleusercontent.com/cpWAepQyLP8V0b-Oj7djzl21eZLU2JdnJPEMPs53Uq-adZbaCegl35RjguLx8rsP2E87ZmwbNgISFIpAy6kOeahaBCSygDVSJzmv1GQGn1w1MgR8N08mnnfhb02XjsLnt\_rVJKr4Y0UtiTf14NqTHLQ)

Clique em «+ADD» e selecione o fluxo de documentos.

![Página Data Flows no ION Desk com o menu ADD e a opção document flow](https://lh7-us.googleusercontent.com/HYqc\_P2DQjBoc-mpsyZ\_nlPFNiU17ZCLHfiOa282-Sa5JSA3Hv1XlwFjmlPhVGnAaEAqqalJ5ka43AJOzEO3uljwVAogAHkTVer7Q9JgI0WaOVX2Uo5Z8KGEqoa3BH\_zZwup7Bh4lKe4O5kr6hmAZm4)

Crie o fluxo de dados seguinte, arrastando os componentes do menu superior.

![Editor de fluxo de documentos com os componentes de aplicação, documento, filtro e API dispostos numa cadeia](https://lh7-us.googleusercontent.com/V\_aJHPhFJssPUQ4mAHU20SVPSfhqhjU8BOQ2Ws1MtaauKp6OVAENLXod2uQe6Zbuc5JKZx6Bp3WyJtkQtkbnDluZZS5GLMGcaC9EuCrV8cn2aJk2y-Cih3PP2dg-umW0iDhak5UXNUuPxwkgqVg-mvk)

### **Aplicação (LN)**

![Configurações de decisão de filtro no ION Desk com os ramos Yes e No e os nós End](https://lh7-us.googleusercontent.com/2CCNlz0S-Z8p\_l9kPPUMqPkreoO3aLy8MkqY6UFMIABJRNFXGTFMXbaw78E42g8fEO4ZxFL\_oJMf2QnWn2xZLtS4zjN8AzCS\_B2i2x-tjWmmjyVLa1jSLQAnSB8-EhNfNISzf2uuX9kcqN-QixUUXvw)

Selecione aqui a sua empresa LN. O resultado deverá ser semelhante ao seguinte.

![Fluxo de dados com o componente de aplicação LN e a respetiva empresa selecionados](https://lh7-us.googleusercontent.com/b5pb4YfbZMCSi2X-xT4mj-Yw\_Uu77zNyJGl3rntVdqf907PwgX6Z9uQJIoHA2FS5M\_mVbdQgkh0HWgsOgtkoySmtrT7W8CrqsqlCnPEt6hv\_yODGulfp1qdxXvrB1HL-en3W9bY285fC3kARLZfSfck)

### **Documento**

![Seleção de documento para o nó da aplicação com o BOD Sync.LnTaxCode escolhido da lista Documents](https://lh7-us.googleusercontent.com/U8cqu3jABU3RQLGEGsS5qCnDkc-boTpAdZEVIUA9AlmD9Oz33JvnzD43SBTmLY55i8Bsr4lbi6udeIimCcRG1NgWbynv6OllCLaJPC50kJ0gPq7rsR5Rvj50yKngMiNvnYoLLT\_Hzn5cyhp18jq\_IyI)

Adicione aqui o BOD Sync.LnTaxCode referido anteriormente. O resultado será:

![Fluxo de dados com o componente de documento Sync.LnTaxCode adicionado após a aplicação](https://lh7-us.googleusercontent.com/bgC1y3NtmX09XBjng\_pKmP5VQ5w0E\_VuFOfMF1rYs3iGGL5OaMHkKoyQJNtcVtbS6bEvF4KdtFNaX0VxT9MF0P-zTDnOnt5mhA0Gxcs4eMcRLtbXl5a\_8y84XyLyvh61-LdoQ7f15j-wE1nl\_TSYSDg)

### **Filtros**

![Tela de fluxo de dados no ION Desk com três nós de filtro e os respetivos ramais Yes e No encaminhados para o fim](https://lh7-us.googleusercontent.com/1Cv1XxqdpiNfonz6jdFgz9zGibQTRLd\_0ONFHf3FvzPB9-sQuX4lTUyuDWzm-RffuPf5jDmZAZwUqbXX-1kers1sEb9ykRMHeYYP6zGgF8yZ247Dx0nG04kSYUTTKSwt3NLS-3TwXA5tbvy5z8HA2bw)

#### **Filtro 1 (superior) — Normal**

O nome e a descrição dependem do ambiente e das suas preferências.

![Diálogo de propriedades do filtro para o filtro completo de código de imposto com os campos Name e Description](https://lh7-us.googleusercontent.com/WVKWUme9uUjRRn7dZ5c\_RyPk\_GCTFEfiNxU\_H5aA979k5hOv2coDYEJHu4K1EaTLUf8\_Pd9ffOk757DaflF0Se0gZ1ZYvRk4QHlpKP0IeirfNr-L6JU3Z\_xFZJ2eeFI-Rhcctwk9QOHRORGNt1oIEpE)

![Painel Filter Properties no ION Desk com a condição em LnTaxCode e o caminho de documento RateNumeric](https://lh7-us.googleusercontent.com/1gCPbUtC7KknzEHVZqIMKyjQGmNyNnR4c1mJ5x0LCJnAjd8D3SdW3W6nPMTsLokL-W2-XjoSM9MU1mJ77K12g887r\_jHoHBwquN1Ore2AmyjCaf\_YVT78KiKtY\_itlr-vyMvJrU7YV6ErgVSYbw5SEU)

![Painel Filter Properties no ION Desk com a condição COMBI como TaxFull OR Tax16 OR Tax20 em RateNumeric](https://lh7-us.googleusercontent.com/ijzGaLt9Uhzw6Wf66ah3auWo5TbkCnM-xGDYezsXXjPEkdCe5RO1wWfhhhG0qRuKbojijLKUm-WUV21eRdq36moWu9Ft0ujexe\_1lTUUEQbfXPvtrzP7iudkSaG\_oiX\_LV7AqZRGlNAp0OXnN8BXRIM)

#### **Filtro 2 (central) — Reduzido**

O nome e a descrição dependem do ambiente e das suas preferências.

![Diálogo de propriedades do filtro para o filtro do código de imposto reduzido com os campos Name e Description](https://lh7-us.googleusercontent.com/pKLo6q5zCQOZQhiRppyd8M-nlIrX5leGUiCct4Xn-4teIZTip5GAJVP0EFc2PrJ6EeDmU2KVOHRKVCaaML4sK8jCnsgTmxbTYjc-9CNd6bOfU-WD9tySeKL7gSRltjzoTEI5Ozrd\_s-7qj2KVNOWN7s)

![Painel Filter Properties no ION Desk com o caminho de documento LnTaxCode e o atributo RateNumeric](https://lh7-us.googleusercontent.com/87PoQQ5q\_35buL\_VNcvz3v-um1upk1U579LDASCJptnnC8ip5mwXxz89d1YmtIK59dOUhl9dfz6BrXBLSNUy6EnWU5uPmUEzbLQv-MwzR0dDkuM1BJ477yre-X4QeJzkkzprF9y5wCWY4zvaooMwIZ0)

![Painel Filter Properties no ION Desk com a condição COMBI2 como Tax7 OR Tax5 OR Tax10 sobre RateNumeric](https://lh7-us.googleusercontent.com/Pa19AN6Mhxbn6bHSc5qKEGM0xRsEV6v77ooyeg5-91i8qGhaThb4328nr\_g6a\_z-7BOCJmWpo8Gbd2twl9FQkOf1Q8QZqOkJmxsIxaTP0R6dASgZdIV6z7p8PFYPYUJ1eKp8btYOBapliANstQSUgAQ)

#### **Filtro 3 (inferior) — Isento**

O nome e a descrição dependem do ambiente e das suas preferências.

![Diálogo de propriedades do filtro para o filtro livre de código de imposto com os campos Name e Description](https://lh7-us.googleusercontent.com/c\_SuWaZ3gF-FbOPWkxB\_eFgkT-TGJEYwV\_fQT05wGWHFNzI9SDZRQfauVMeBl0rn79QdU-W3kRgN-hWsYkfdMSevlYyiNPxxT\_3RxXcETo-lkjvI5TCygUag91PFJycrRdMA5hSQJCuzt8FekMwpu98)

![Painel Filter Properties no ION Desk com a condição em LnTaxCode para o código de imposto gratuito](https://lh7-us.googleusercontent.com/HGZ8fR6XgYtZ46i8Rov8xIr5J4z8DmGFfJkeovDGzT7S68VYI-OdG5jpMdoOiROIZckYMbVIlPQmS\_kWQazJVbco1t4ZH5Sr73b4xePlisnbm9ZLJrOPwtXn7-90F1FcFH99P6ZKI0hCWdI6z4d7qNA)

![Painel Filter Properties no ION Desk com a condição Tax0 e RateNumeric igual a 0](https://lh7-us.googleusercontent.com/\_APmMO6A2AG2km4H4em-ZMrn6\_XRpO3zxRhZwftiaKi5uoDhv3TTzCBfi8WVDCf6mOQNgtcEJ-z-BmP28J86noGJ5dgqVni2QIxePaO5-LU8fdwRqySUQt\_6wmFWiOFzTMmItcClQPRaSKUaosgWwNk)

### **APIs**

![Fluxo de dados com os três componentes de API para os pontos de ligação do código de imposto](https://lh7-us.googleusercontent.com/XDhVCKHYaxrRIFyYfq0guXwnZH6jK-WZIFj2i0Wkr4kxyNcdCH1TzKd0Pb3-H6qs-b7JZ3UUIGm0BVHiUL7Aya-D7YOSV8p8tnwQeAfBN30T4fW5-ANePN1TcvUr1gzLJPwj7rRO4Hw4ziuyYrqZBX8)

Selecione os pontos de ligação API criados anteriormente através da lista «Select ION API Connector».

#### **API 1 (superior) — Normal**

O nome e a descrição dependem do ambiente e das suas preferências.

![Configurações de API no fluxo de dados com o menu suspenso Select ION API Connector para o código de imposto completo](https://lh7-us.googleusercontent.com/90c2E47fMC9CKNVY8DtgyaNUAqAnQmfErZm\_R-njUlEdIX6mafMUOk3GcAooaWfCzD4-OmdPUq5VSuMXmTSNjVEc924ASIPqmTxAQXqsq6eKs5y82rvwHxqnsT4S-sEm2mQRNwleiubkwIO\_kS9Vwzg)

#### **API 2 (central) — Reduzido**

O nome e a descrição dependem do ambiente e das suas preferências.

![Configurações de API no fluxo de dados com a lista pendente Select ION API Connector para o código de imposto reduzido](https://lh7-us.googleusercontent.com/vw1hM3W4eCt\_8OG7Ht203tckaWarPOLi463WvQzGgixTMnfk7iC27JzL3iNgd5LmvBzWTFnYa3QNy5y\_oNSHJ9R-Ck5CAgLoBmGurbCn1RZ32jiSJr-LUnL3b0nhHctBqcCx\_25L1Ce-\_va3ZgfKXY8)

#### **API 3 (inferior) — Isento**

O nome e a descrição dependem do ambiente e das suas preferências.

![Configurações de API no fluxo de dados com o menu suspenso Select ION API Connector para o código de imposto livre](https://lh7-us.googleusercontent.com/C0wmqAkrlgyXlMjKsGMOqre4MPLuHawrZB1oYDzkGFocperUB5dKea7kx44hrA\_Kz6Ptx495cQbwq\_EHfEGNvvpr\_0dvCuUS2zz0-SARyuNbf2gKsK3vTdd4Sfg3jWtE1YAN3o0VpoK\_HRn7T-fFOR8)

Depois de concluir os passos anteriores, guarde e ative o fluxo de dados com os botões seguintes.

![Barra de ferramentas do fluxo de dados com os botões SAVE e ACTIVATE para o fluxo de documentos](https://lh7-us.googleusercontent.com/f8gkYY1Z\_W1if2h1es9vbjebtDX0zGiqY4p9OD68gKSAcNU6si-guvyIg8hzdjP7TulZ6Yq8NcbT2EyuHleVeNxpY\_6TDlbgIUaxDJ72ILcy8kVvFuSja7FT6gpYhMLFGw7wv-r0XyFN8xIrQ3OuUGI)

## **Publicar os BODs no LN**

Abra o LN na Infor.

![Página inicial do Infor no browser com as entradas Home, Master Data e Publish Logistic Master Data na navegação](https://lh7-us.googleusercontent.com/aAKRLInqsogQLv9nye2rHLtVFlW4yaCpnQ8A4cKG5A2145Tl6poOxthfo2InYimNk5dd8RabYrX9xP7sPO0aJ5ThF07ZVfKvUXBqVoxRJg53IhpeOeiA4B\_CGOpeLKWlPbCf4EaFXjgzmBOcezocF9k)

Abra Common → BOD Messaging → Publish BODs → Publish Financial Master Data.

![Menu do Infor LN com Common, BOD Messaging, Publish BODs e Publish Financial Master Data](https://lh7-us.googleusercontent.com/pMAgPzyhBNrEsFkTm8-iniHBhEXIPswoJ8URt\_v0fv\_7dSayrS8UkN7F9WMAOZQB9Q6sCe9faRl4rRDDft3VdrzfNUT-IbWxE6GyWPPKZh4R67JRmXmJ2NsTVPdjLo6uJdCpki7QDpgiY\_azWtqaqKA)

Selecione MORE e clique em LnTaxCode.

![Lista de colunas em Publish Financial Master Data com LnTaxCode junto às entradas de AccountingBookDefinition e AccountingEntity](https://lh7-us.googleusercontent.com/MtjE7Glgv7e\_F\_CJ4LXMuWk6SaInmNFlKzhGJu71iGgxRWtjI96lX5J0gqxRcj3y1u4E6Aq-xNEpuf83dsjHh6op0qeH89oBMvlVTTD\_VhGs10-gjuIb0eyc9b3dcCk75Wa5sASreXKW6SbQPYrs8sM)

Marque a caixa para selecionar os BODs LnTaxCode.

![Diálogo Publish Financial Master Data com a coluna LnTaxCode e os botões PROCESS, CLOSE, SELECT ALL e CLEAR ALL](https://lh7-us.googleusercontent.com/VTFntcBK0GVsUdr\_fZBUaN8rXYdufObLE7PnwwNg9QU69zYwKHvwFZ7En9WZ6p\_WGIkVdqEjBBYeIYSuHHJWBWYonwd6Edtr0ZZuGsX3qhNMDWQWefOaGfrYxrq\_yLm6\_gEw967PGp3HK0hzO-G2XiQ)

Volte ao separador OPTIONS. A configuração deve ser semelhante à seguinte.

![Separador OPTIONS em Publish Financial Master Data com a configuração dos BOD LnTaxCode](https://lh7-us.googleusercontent.com/2tr7VHNOLActJCiLGC6jyWsdyqwZV7Je6UsekeoBo57qNpOBDYtOQuoelKOdvLMRo6uQJWn1S4ir\_zRZHAx2C96NyKp4ZjIUyFCYt58T59TqO3ml0ZfiEtSLwdRPp9g8pkMemN0xDS5ao8DL5xgosWE)

Quando pretender publicar os BODs, selecione PROCESS.

No final, deverá obter uma tabela semelhante no seu ambiente DocBits.

![Tabela do DocBits com as linhas de códigos de imposto importados a mostrar os códigos BE_NAVL, BE_NAVLRP e BE_NAVM com as suas taxas](https://lh7-us.googleusercontent.com/4wK-mfKl0UNqvp5ngolE54miiwAKxAcOERO2mSDWzZ5t838VhFZrZGzCMeIyg7WDPpHvNzkeWRJV7ZZdsaxwXiFS9uxm29QZUYHhs9gU2v6QgSz07vfjpHXW3oTb5ZiiiTjI93gmV9MDTHbNWJmrvHY)
