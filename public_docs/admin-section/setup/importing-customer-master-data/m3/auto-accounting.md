# Contabilidade Automática

## **Pré-requisitos**

* Fluxo de dados funcionando de M3 para DocBits
* Ambiente DocBits configurado corretamente

## **Configuração Infor**

No Infor, abra a aplicação ION Desk. Na aba esquerda, vá para Conectar → Pontos de Conexão

&#x20;

![](https://lh7-us.googleusercontent.com/Gl49rTfnpYQjXjpUNF3SEouZiJ4pPeHVk60d7dyHizfPLT6sn4AoKVQPPvpgg2cD4ts40hDeWQRs3BqmKW-CAco7Dt0oWKF7ukQJUVDBgSUoMNHt\_gRkqLxkF5CC\_CNGpVRzrNs7rfF1msK320\_J02g)

Aqui é onde você irá criar o ponto de conexão necessário para importar seus dados do M3 que são necessários para a Contabilidade Automática.

Clique em "+ADICIONAR" para criar um novo ponto de conexão, selecione a opção API como abaixo

![](https://lh7-us.googleusercontent.com/ctE76pck6mGmBVxRIMhHyn0TbSKKsiGjO7rO185fjndTIo7qYyvSZS3neUdV2CWPqBSangpJ4oG\_g946\_KyOwWyJvacZe5htWiQLTZQLzfNHvsHDhmMQmjh7MrGsqKp6sm-XPcGmEwrH2ZMYCd0bUl8)

Você precisará configurar o ponto de conexão da API chamado:

* PlanoDeContas

### **PlanoDeContas**

A aba de conexão para o seu ponto de conexão de PlanoDeContas deve se parecer com o ilustrado abaixo. Dê ao ponto de conexão um nome e descrição apropriados, além de importar a Conta de Serviço que você criou.

![](https://lh7-us.googleusercontent.com/p-jly6\_S96TsCmpFg9oOob0h7Q7NBlTxRKgNCphiy5QfbK\_lrLMAR2miVUQh-fXrCfGdZr17ongp5c9bnK6HuHCVuDArHhYcmKDlAyO52tGcxg-VXBLXZ1ka8yqZ4DWnxFFMxUKkE7jgvCgr7P-nzdU)

![](https://lh7-us.googleusercontent.com/GkX20Q23htKae7OOcGnJ5J6f0L4I69vOU9jYBpY1m9bpDPdtsD584mh\_9IaZF37Ne1OY2uOPgFxYYjwTrBOoZqahpJLlY3n3qmBn0sgzC0eVu91wE0NWBvESBFJmeVTITQoqUTEU56tHEj47-LQmI6E)

Você precisará adicionar dois BODs nesta seção para este ponto de conexão. Sendo eles Sync.PlanoDeContas e Sync.DefiniçãoDeCódigo, para adicionar esses BODs faça o seguinte:

#### **Sync.PlanoDeContas**

* Clique no ícone de MAIS (+)

![](https://lh7-us.googleusercontent.com/hFWg7-4Osuy9Q0uZYqT9yfAPFYsBi7yitHj7BBxQ94vbsDVg-GuCeTBakvV2eQNjqMGwDAF90nO5h-OxFR8HtYEiYcALdBq5Fdj\_Gl-wU8QePGV4Wr3\_78OK22nUY35dfCQhUPQIp\_qkdHN0wr7V-VY)

* Selecione "Enviar para API"

![](https://lh7-us.googleusercontent.com/jA97YupOjXJlRFRxduo\_tYO4YYDZoT0mHxWaPWfJGyU4RTNSVNRAIAsR5mzRyLh1iusHl0cBKUxhYj3hQMzacGdN2QGsvPGy1vHeq\_JNhDqxc-SI5HtZh\_Z\_zmaSjyJwmr2337tzYSWfqDl3JGkjBqY)

* Procure pelo BOD Sync.PlanoDeContas

![](https://lh7-us.googleusercontent.com/hzuwy-VU8xpgQ85NGHAk9u-m-\_Sw4iffT0SNtWTJw9iWHRIsIvGTEYQgJYi7CUoYC7\_Yp2KDtsohRQkNtIgr1VutFbR8mTkT\_5HmJ7ecgW8pcGuZTuwxtPDOlJpWuONq3WPIupRRBxBJPlsYQ9w-bxo)

![](https://lh7-us.googleusercontent.com/6p8nXaRAI0ucRzmyKfYYg3J8MmHXVgHs-KxcItxeZ6wbefK1YdMrYSblHwnXkSiajApB5ds\_EgpJJWYjfbKOjHdsh-H49jG45weOX9v0YBSAqdXmKgoaBcP7A4zDyINMNVt7RWgbQ51WxNTsfBllvQ4)

* Mude para a aba ION API, copie o nome da API e procure a Chamada da API pressionando o botão SELECIONAR

![](https://lh7-us.googleusercontent.com/aRXjuD3nkYsFNM2eYkfmHrshU3ycmN5G4OGSFFadbSToy3pHKYWMw6apbyMhJ9o-5xB6UDA4rbdPjZWAdP-OCH8gQFWV5vWXp0rqLxP9DozP4yMS074\_nsHzirJUgBfkBkQ8Ydp\_WjImf2bx3pDnLPE)

* No produto, selecione o Endpoint da API que você criou para o ambiente com o qual está trabalhando, que você criou no ION API. Procure pela seguinte chamada de API, selecione a chamada de API e pressione OK.

![](https://lh7-us.googleusercontent.com/LQWk7uiEPCxJcohMmIuRrg2p\_wwE\_h5GoEEP3Y2IdpKARppHoGB4Rt1KRM\_2AiXyG0-ieIV7BM51IRN5exKkhG8eLTkKCftm88j2NLc15X50VLu9t1sZZnQ7DsIIvgUsxz7oryzVIkfmifw-m3qkLDY)

* Em seguida, mude para a aba Corpo da Solicitação

![](https://lh7-us.googleusercontent.com/0tnYxKvtW5Fw7yJfW0QBMclidw5kKJB4oi6M932hGO8ROokbMXbyFcjPQq\_LSVe8hv3ZyVVWqjDO4vMMRgPm1L2iXV3pSoiyzrxGLvBTx4kwt5uo6XtHEt25PRVdM6aIddhHDrT7HGzx3JaZ1F02-YI)

* Aqui é onde você irá configurar o mapeamento de campos para este BOD, sua configuração deve se parecer com a seguinte. Os mapeamentos de campos estão disponíveis aqui.

![](https://lh7-us.googleusercontent.com/3giuZYeQjdZZHAg7W-pcAHB\_69KP8Ukh\_0NhATYBxvrS\_Qy3yH58fQyrp6GKfOzi1xJms5KV-XVNnAWtX6VmIBwdxSVum9JA6-H9W3XIUYKiTEK3IWoKA560a5I2lwmYd0kitdfC4pRkQVULyWp9PpA)

Após concluir as etapas acima, você terá configurado com sucesso o BOD Sync.PlanoDeContas. Clique no ícone de MAIS para adicionar o próximo e último BOD.
#### **Sync.CodeDefinition**

A guia de conexão para o seu ponto de conexão CodeDefinition deve se parecer com o ilustrado abaixo. Dê ao ponto de conexão um nome e descrição apropriados, bem como importe a Conta de Serviço que você criou.

* Selecione "Enviar para API"

![](https://lh7-us.googleusercontent.com/YLaFsc0K1Lzruo84Np3EdCTF1xsaQOLRypNpgZB7L9keTh1TwPOMnjBxJYnBOj8GrNSG\_URcRGgv\_p70-pjhBed-wvURRW08YtEWjmACMc3CleRPrHia6nihWQwVOUaZ3qHD\_zLy2W\_iMQ0I77cY\_Bs)

* Procure pelo BOD Sync.CodeDefinition

![](https://lh7-us.googleusercontent.com/f3ikl4jh0PBhYmP3r80BrHuGGu9w9MHe-E0VmyXOCmFEkkK92cxgVimwyP8RF0kF2GruVaeDjiYRKuONX5bQ2ZBRmdKFx8Bf9cHvX5q-xYnXNH0a2xnR4eg1ynyWbRRRoY5xn28HJ\_ziRiKcTN43aHQ)

![](https://lh7-us.googleusercontent.com/nXQZ1LLZsrndggHkAmRtMlV7YzFemnjC9CnS4AdUVDits4zNfzlaqKdHnNcLyTtDkQSX3SB8R3fnZhGBPd-By8C364IIYc4vE2VXNXzoa4LfHP6irTiAg\_N\_2BHSYBLzaQyMCN1w5LdFiiqeiiwAXuk)

* Mude para a guia ION API, copie o nome da API e procure a Chamada da API pressionando o botão SELECIONAR

![](https://lh7-us.googleusercontent.com/LbHmVr1PimQkPu-t6VMvNVk9wVXeQBHOu-X4pW-9vGm-dON2buizVGbKekGL7tY1t4OkwQtzhl7uDhq908UxCfDCJaRDEukpk-07pJjLO-ezRUHgblp3REm0qrKF9wOtMkNWJlVVNVhmfzZ0TtUsqQQ)

![](https://lh7-us.googleusercontent.com/K-kDDTSaZiothC4o3JDihhVJFNt0PiBnLK7kF6RcBOX9EpzutfLHGstzvywBBqaEqm4WqOSQSxtvxRPtbVafPlhtf\_YMVkXjhTkvnGwLzwH\_p-YgRCGAu-DzA94MHjqQoAYTSBPgojcGlJs7tBRcpME)

* Em seguida, mude para a guia Corpo da Solicitação

![](https://lh7-us.googleusercontent.com/DfT6FtrbW7LbK4b4I6ssYDWOaPgUxkWsuTDpvQGw549tPFxgEU\_gmh3UwXTbyKHZR8SOHXPHDdobEhA91RIMB57ZAVatrZEsad2QW6QHiUkdZoyW\_yE\_iIGDgs2IrY0I6qL1JTZxksYoaLKu0Il8smU)

* Aqui é onde você irá configurar o mapeamento de campos para este BOD, sua configuração deve se parecer com o seguinte. Os mapeamentos de campos estão disponíveis aqui.

![](https://lh7-us.googleusercontent.com/nqK7x1Km4wIP9aWnvMlSHl1\_omw22GRKONfB-zc8ikn\_rSsl60Ksml0oQacs8UNmPSLFSKPD7Eo9FsH42RjDo4oragvHZJHFW\_yv62KXDrF3SKnDN2-X6vqYJ5a-3bYkkvPDlNJSxFylvtAFr-2Kt8Y)

Depois de concluir as etapas acima, você terá configurado com sucesso o BOD Sync.CodeDefinition para a tabela de dados mestre M3FlexDimensions.

## **Fluxo de Dados**

Você precisará configurar o seguinte fluxo de dados para Auto Accounting:

* ChartOfAccounts

### **ChartOfAccounts**

Uma visão geral deste fluxo de dados é mostrada abaixo (a quantidade de pontos de conexão da API DocBits no final depende da quantidade de ambientes diferentes que você está configurando).

![](https://lh7-us.googleusercontent.com/RfkP8xiF2vDzQhBNa66L0NQHk7TGjj52aK3hWoisEnWbdG3l-SZKKw8mYJ3b28ShXZ9omPS6WdNiXaCpYRQzwfges0SKznwQal7K2ElILbGBJNYu3VFm6gDQJMHYRItAFX0cdRZjXgCk2FQqHJ4iSjY)

### **M3 Company**

![](https://lh7-us.googleusercontent.com/tqYoI-gLUpe0c0x1T-WhP0\_FolVzPGHhFY8m52Fw38mJNzsDvjb7stRrBfWVjXLnFrJTTy2lyd9Dmva3\_EPG5eRWyf5ATA2cTWvCj3Ksa4Fu4pHF6rNFjfd3Cjei0UlibT0HAQYE0V22bdTStjY61zk)

A configuração para este ponto de conexão depende da empresa M3 que contém os dados mestres que você deseja importar para o DocBits, a sua deve se parecer com o que é mostrado abaixo.

![](https://lh7-us.googleusercontent.com/wpSluEs21T5wXG0egZPfUCYBP6X\_uUm6XAh-PyD8RrojTuIztzRJzhVYdzcNI5dQGGDsrhSKx\_K2-y0JDmK9w41fVUXWcW1N2lz5rizXcMnn5BuiaGRy-TEOBryGxvP9mBGJTZ16lMisoC\_YumwpS9Q)

### **Documentos**

![](https://lh7-us.googleusercontent.com/uR6XaFI7TPQ4L8Suom25PBdtXdL4i100Juz7kRBxT5rdxhejZW7nPtVIlEGjWWnZLbo9ipx7G95NBFV8dd-g4vw\_vM-uPApJ02QdxvCmX27bwAW\_qUWUXajV6BFVmIfzTQ46Zj4DybsYKKblXjuWc6w)

Os seguintes documentos precisam ser adicionados ao fluxo de dados:

* Sync.ChartOfAccounts
* Sync.CodeDefinition

![](https://lh7-us.googleusercontent.com/6Bq-yQ9Yaf2OJwjBxyFvqAMUitcovquo\_iU4hc-pgag1iDwLcstggVjLsdY3bRl9XWNc3mKOwZrY1FSlu47IzxxUQHFkjIAl1r08Iw9UbKaaMh4WiWrqFuSObdTjEvCEI5IDvD\_Pys8jAydydJgbsK8)
### **Filtro**

![](https://lh7-us.googleusercontent.com/LyKGzQUEswTD1XfpNDPSHjChgqNFfs4guXfM0KNuW2fPoiaeUo4uPrlGgwt3RepWUGQmu\_trUMiWb68cUjUAwXU9IRoWOsv9M2l5v4zFfBkEcioz5ok7Eoss7I-tBKtpD7wVUkGWi3U3ySrIQ\_fDPiY)

Para a segunda rota do fluxo de dados (de acordo com o roteamento no fluxo de dados), aplicamos um filtro com a seguinte configuração.

![](https://lh7-us.googleusercontent.com/7xdqGdo9bS6\_IIzTVYF\_08woBXvhIVkA-c6-ZrDpDEzmEDFzDZSuxZ5LYHKVUhJqYq4Wlq1FXPfr5myjKFUsMbnJrefc\_L7URD7AbEq\_D90jEw7o8Yrhg5XZwLdU83OwlZVXqlYla61b0LyISXeBLWk)

![](https://lh7-us.googleusercontent.com/OdI-0FaqDaPKy2g9Mr8HUx\_oGRZkDrkeI6P1rWqOounpDauMThaqzs2wOawmw3RwcMlQHgI6wj16RXQDAP\_JNMGkxvmiEnPJ\_bvse2CvMegPwinSIJRLmXaCzfjxtB1FDqnqPOMwrMYNKJyiC2sGUe8)

![](https://lh7-us.googleusercontent.com/RMPIV6ZWsUcBA6klny6Ln-\_nhMGl1zdEHfUKK56owelabcG-6gM1S\_eqWAVLTeOHdec3D5D6xVJeC5evnJC61L8daV6IbJbCmMashkWXSK4Tv4RdE\_erjR-Mk2RihPodIG4HrqSOQ8hi7SG3xctXd-E)

### **DocBits (PlanoDeContas)**

![](https://lh7-us.googleusercontent.com/Npm92rS\_EO5roSy3tldC88hFIyiDnZjHnnVSkkKyfmNrOcbuVj4LPNrcsWvOT8IHNQKGMqIZymG9q3VMGG6RwvuRBqZgmhHxqXn1oieajDmz8giQxSr8wOFzb8TQTJJWwj912-sDRtkrDAXCr7ne-pk)

Aqui é onde você adiciona o ponto de conexão da API do Plano de Contas que você criou anteriormente, a configuração para isso deve se parecer com isso

![](https://lh7-us.googleusercontent.com/Dw4y6OMuMAYHZjH1etj\_FqdsaFxaRhQyk6\_PaxXrWLhrNirEn7xQc5uIpbDT6Wz85XvZgY02aNuWfbYKBzo6W9aavN\_Asu5ENfr2dszWYQqs9sy6zl4o0NxRe3IPXodLIGf9JkbK2\_UtYe4dVii0JbM)

## **Desencadeamento de BOD**

Depois de concluir tudo acima, você precisará navegar até o Infor M3 e acionar os BODs para que os vários dados mestres necessários para a Contabilidade Automática cheguem ao DocBits.

Comece pressionando Command + r, para abrir o menu de prompt, digite "evs006" e pressione enter.

![](https://lh7-us.googleusercontent.com/pzAL0cnM94AUE4KmTyBV8OPU9ft\_g9o0-KB9Ib0AjrvG7Q59GHT-2biP4n7yFyXRxQ0gjy85G6MWMWUeMIWJcTQ9TKwzCEywd7I\_6\_vV-muepobkW0O-4-CZxsmjOEQ7uM1frZpTLqlLS3aSYkEuwAw)

O seguinte menu será exibido para você

![](https://lh7-us.googleusercontent.com/Wx41TNpg1zuaf1rXIBvSCVzSRf6q74rdLs91el21iErqQnDiF4cv7X0nyDaS2Gjimj7xbfAK-7mo6sXN6fkK934mHnCnivFTz9NqHi6dBoMYiRT\_vLrkVUlFd\_T4Oan3Zkq3WKLoI-kmsElHSKO7zY0)

Para adicionar os vários BODs, você precisará inserir os substantivos e nomes de tabela de cada BOD individualmente.

![](https://lh7-us.googleusercontent.com/5gVWRDm\_8CSyoQRkq-7LuI8MLU1BjRN6Z6YCcVZp7G3Be62nQBht-eUNZreTzV2rFWYK\_RcKiyzwTTlT5y5X8eGf-Z7qDavDyHML0zv6Yt6jGu2z9d-nL0K-m446nDZa2-aiFLnnzjAwk8pTT4RQK6Q)

Os BODs que você precisa adicionar incluem:

* PlanoDeContas
* DefiniçãoDeCódigo
* DefiniçãoDeCódigoDimensãoContábil

Para adicionar o novo BOD, após inserir o Substantivo BOD e o Nome da Tabela, pressione o ícone pLUS indicado abaixo

![](https://lh7-us.googleusercontent.com/66wclj8g8RAYT9-UIgRMs0qnuA9srmWv21PdqdNm\_q5icGmabL17-DpLOSs4pm6Nj3xJN-9xt7io\_5GZGfzSQ2qt\_8Y--CJFou6FaOdufiuxOdKHrUUYELNdGy9e-gnWg\_hAMSfs\_NJa6zYBMpoyTVs)

Os substantivos e nomes de tabela dos BODs são os seguintes.

**PlanoDeContas**

* Substantivo BOD: PlanoDeContas
* Nome da Tabela: FCHACC

**DefiniçãoDeCódigo**

* Substantivo BOD: DefiniçãoDeCódigoDimensãoContábil
* Nome da Tabela: FCHACC

### **Publicar BODs**

Após adicionar cada BOD, clique com o botão direito no BOD que você adicionou, selecione Relacionado e depois Executar.

![](https://lh7-us.googleusercontent.com/225-ujyGzG\_RJOXgbx8NOh\_4s-Sn\_o80b\_h0DTsJqfr6OcyPUwkWLF2lfEyzFFFKddKmlWd32bb94qeYlOdVBTI8RL0r6ZfZKloVTrAYLNp-U5gL3aJhW4d72ExkkyM4AydLczsPvdE1cRDfGNKupdA)

Você será levado a esta tela.

Altere o Verbo BOD para "sincronizar" e pressione PRÓXIMO.

![](https://lh7-us.googleusercontent.com/3DyjXUSlAF7msQT1OAO3aCr1U9R68XZj0oE\_yJwsBrBj-FkiZR-oRYQYSClHG0iN0FXFdDdKQA1hOBlw3jc-lXQCWkiDFa0IweuQnoR8k-Mgyp1HeI5ImJqNogz-Q3b3P33ywb0B2o1pZ-TkZ7mAwZA)

Depois de pressionar PRÓXIMO, você receberá uma notificação indicando que o processo de publicação do BOD foi iniciado.
### **CostingElement**

Para importar a tabela m3costingelement para o DocBits, você precisa fazer o seguinte.

Na Página Inicial do M3, digite Command + r e pesquise o prompt “PPS280”.

Selecione uma das linhas exibidas para você. No próximo menu, selecione FERRAMENTAS e “Exportar para Excel”

![](https://lh7-us.googleusercontent.com/I8SYWm-JwpyYRHFUp2obGtXcsa7m\_blJ\_lTrnhczztRIXIN5gfxCt3eRw6ZI42fH6AwnsKyv4ux5-rhaT505PsyDFFI\_anUNvmACFyx\_ssgxaqWq25vLt\_E5s310HNoiPPLf35qJlYtstjpj5Cc4aB4)

Selecione “Exportar todas as linhas” e depois pressione EXPORTAR.

![](https://lh7-us.googleusercontent.com/wtjHI9L4YUhf-yJFjcPGu218Vis\_zELtCIfpmkIUKgasfrdfNW-dr\_J1DqXlfD-SBrnVduDrMLAIAQh6UTlzBqEP\_JPXP48elGMyGj0ByZbX7TpqlnIfRZ4ZoD0pyCo-AKigeKjlHN6cFcdpeClZ9L4)

Após o download, você precisará alterar o arquivo do Excel antes de convertê-lo em um arquivo CSV.

Você precisará abrir o arquivo do Excel, que se parecerá com o que é mostrado abaixo.

![](https://lh7-us.googleusercontent.com/l4WbidK-5zSEQ6rwqhknudPBmmDji0f1WwTh-kHomSkgEOA7s4m72cLw8z-4nflqBvPp\_2AajIEZDZz4dRLs8jlAeYHp4ee2tDysxYy8YBjj4ktHxdUXpxO\_Z34c8\_f0cNMX-9lp0lT5wOZoH1QUCgE)

Nesta planilha do Excel, você só precisa das duas primeiras colunas, altere a planilha do Excel para que o resultado final pareça como a seguir.

![](https://lh7-us.googleusercontent.com/QaNRlKHrU6kZWFqmwYR8C\_\_nLVOeqowAxJlvooSVBIAF5ayx2xZtUppsn0jzBcJVi90vemM3tZMZOjn549N3RzMuWuE3w911WLVS5NMuiUmnfXM\_xUXbqmzBtiQZstnpEYj1dUSbs\_IkAydlhBfdmcc)

Depois disso, salve o arquivo como um CSV.

Depois de ter seu arquivo CSV, vá para a seguinte página da web. Isso depende do ambiente que você está usando:

* Prod: http://api.docbits.com/
* Sandbox: http://sandbox.api.docbits.com/
* Stage: http://stage.api.docbits.com/
* Demo: http://demo.api.docbits.com/
* Dev: http://dev.api.docbits.com/

Aqui você fará o upload manual da tabela CostingElement via uma API. Clique no botão Autorizar.

![](https://lh7-us.googleusercontent.com/tyzOq3BR2QqTguQFKicxo0dE5j5hGsP-BhfVbS81O\_mxN5bSVp40jYfgsVJcE\_rBLFMDJNvbPkPIdjPqaqoNbHBBM-9hx0i-U4VAH9ISBYhpwKgqQeUEd67VV1E4izwNyxbAwwrhCmrAo1uIKhLherY)

Aqui você precisará inserir a Chave da API do seu ambiente DocBits. Isso está localizado em Configurações em Integração.

![](https://lh7-us.googleusercontent.com/4ADnevq6kq\_vbxUJpyPbHNcGvRvpO-l9Gwd8ZaYf\_vO4uWhSl1jmKNpddmHGc9ZHMMbXCgLOElLDYbNwB3INmBDETecPrDnpI601IUOZQlT7tc7OLSPXwkooOJFNwML2i\_gvBPuE8CvfwRpX-ZIlb\_g)

Uma vez concluído, procure a API chamada master\_data\_lookup/import\_data e preencha as informações necessárias. Depois de concluído, clique em EXECUTAR para acionar a API.

![](https://lh7-us.googleusercontent.com/8UD4FhFv2dRB4cMjCDL4G9ndjH7laVMKWqdeMaJGgEo48-UVvucB1uOydzNdfFy0yPM5bb66mZB4k9uJR7TTiEREGFaV2EqW01gxJpTyuUfGNh5QmBjySkyhZ56gWV8sYs8WI5RnHcENtXgjTU0vg0Q)

Se feito corretamente, a tabela M3CostingElement agora deve estar em seu ambiente DocBits. A Contabilidade Automática para M3 foi configurada para o seu ambiente.
