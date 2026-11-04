# Contabilidade Automática

## **Pré-requisitos**

* Fluxo de dados LN para DocBits funcionando
* Ambiente DocBits configurado corretamente

## **Configuração do Infor**

### **ION Desk**

No Infor, abra a aplicação ION Desk. Na aba esquerda, vá para Conectar → Pontos de Conexão

![](https://lh7-us.googleusercontent.com/tOzuXMmjVxByy-GQHBnNbFgP15YKIR0GNGoqrcqz87S3_qBeZCvk92FA4PtD6UjLtUGBBKfmMd-W087C6TnORp7qptWzpDIEp4R2BbivWjQAsmStpZ4RcMgCY7s2CIV0AHErRtQDO2ePlMbNJSoIrmg)

Aqui é onde você irá criar os dois pontos de conexão necessários para importar seus dados do LN que são necessários para a Contabilidade Automática.

Clique em "+ADICIONAR" para criar um novo ponto de conexão, selecione a opção API como abaixo

![](https://lh7-us.googleusercontent.com/C8l4LJ2WHIoPU7E_uFhNIo8XakbizRx874hyTdJH9oHIW-PGd5tOhsnc1uJ6TW6P9BUQqmjoMrHL5WwQJ8IUJqufsbPFIdamKR9cF0EnnPOZD-TlJEQQAmcHKzoKrumCDQAexYZOQ1CpN1p_bAnLNzI)

Você precisará configurar dois pontos de conexão API separados, a saber:

* Plano de Contas
* Dimensões Flexíveis Finais

#### **Plano de Contas**

A aba de conexão para o seu ponto de conexão do Plano de Contas deve se parecer com o ilustrado abaixo. Dê ao ponto de conexão um nome e descrição apropriados, além de importar a Conta de Serviço que você criou.

![](https://lh7-us.googleusercontent.com/gJ1VStvYQ8cu1HBua2iA1Axo1M_lXTS0VGYuqqtSDx-mtu-4xQQBjasNsGyiNSgjuYYQ0yYQkJN79_HJcFF0vTyY4wLZWYIJQHC2oCColX43Va-g-E-KeCRyRQiV6eRDm932eFu6ic7g8OttWULPNUE)

![](https://lh7-us.googleusercontent.com/6zmLNSm7pLiS8dA9VceJv5pxwGpTE8WWZ1nmOt-UJA9qvW0wytcRZXB21jW2xa1BABB1YNNS5uWlxVWgEp4bWU5Rw4li3_qr9potqxxXTY99V0VQQrp3kz4YyFE4jmibHYAEusc1qRtb8E-x9ilbR8c)

Você precisará adicionar dois BODs nesta seção para este ponto de conexão. Sendo eles Sync.ChartOfAccounts e Sync.CodeDefinition, para adicionar esses BODs faça o seguinte:

**Sync.ChartOfAccounts**

* Clique no ícone PLUS (+)

![](https://lh7-us.googleusercontent.com/aWwQaVreFHJsv5jd8-ZrVt-FAMvt00aO9W3n1KZ2XmUyxtaCGkg6yS6adPOwXJrqRGdFGTDpG4QsXXJG9V6IJeCrWKsKh6SRjl7ZOacLy9-i5K3dA5mWs6Ps6a91K2TNvdUx98OPwEDWWadz3BwaPiQ)

* Selecione "Enviar para API"

![](https://lh7-us.googleusercontent.com/uT-PjpDfv7MGB7wwvkYu0M9muSRXtAqMSjk3LKz3xWdtduWHr_HT1m4ZoETyhP782zOaWBbnEiWxTC9PphoiqogrUNsM5e8PuYutjcwJPqQKAqAlXQMWHOpYru0b7nabzmt_WqgxEp2Naz2hXViNWzY)

* Procure pelo BOD Sync.ChartOfAccounts

![](https://lh7-us.googleusercontent.com/yQQ92Nn3koBsPG32cPv2Pv9sjdmScGE0WGJ062YSg9q9RDyHnIg-qbh1RA6i7yhfKBeBhgbYEi3uJmR_z6AdnR9pL49M41hvDoqzvijuPhGm3ZltHExmRtfXdccFc7Ogb44_Y4gA8VDBXwt5lJsYEW0)

![](https://lh7-us.googleusercontent.com/WcK_a7Lb61R-5fKGGqzVyR3lAAyyg9jgYunJYC8VNHCsU3Qopvz_d7EJwXo6RZsbcEos05hv_sILd-b29Ky4QVz9lNtzvoicT6bBykPKe-WIPPS-OtZ7yXg8VK6MHa5ZzNdqXvR1CUZmnR4WCu3MpSs)

* Mude para a aba ION API, copie o nome da API e procure pela Chamada da API pressionando o botão SELECIONAR

![](https://lh7-us.googleusercontent.com/364Jd0-EBMpWgpgPZukqcjdRlEoGfkgKkB_U-Y2d87DlB13_E-ovjnBaeRdPCi4rAMm6Ksc_MRHAm75y1BPY21HQ12Fjdr6Q0j1YDTBI0Fo5l3LiIHSwL3ITsKbQ-VIBc5aO6O_DaeKl1z8AUr8xhfo)

* No produto, selecione o Endpoint da API que você criou para o ambiente com o qual está trabalhando, que você criou no ION API. Procure pela seguinte chamada de API, selecione a chamada de API e pressione OK.

![](https://lh7-us.googleusercontent.com/NWfGZk5ttI0tWMli1DRZ4SdzC9xHa0LhGR1QbgaeJN1726FYoiqMg1Cb5_x0TvYu4MlTyJqS9n6c6EfW2veKhcUdvpY-bkK_uyfRJt6vESmRsVuIx93ipwuffd3YJr3y2sYX5fjFxjRNWEWzH9ojlr8)

* Em seguida, mude para a aba Corpo da Solicitação

![](https://lh7-us.googleusercontent.com/BNwExG0mPZ_enovlnQh_SWATS4wDEcOCXuyX98EJza80OxKvrhcFUZ_l4v88XVBBI-iIjg6eprynpO-zjjNeNsCpgulcUCG8OpGA1SzC-1h_OyPHTfHlF_ZsWkpUhT5hz39ruI-TNPo4lelSsvz4jrc)

* Aqui é onde você irá configurar o mapeamento de campos para este BOD, sua configuração deve se parecer com a seguinte. Os mapeamentos de campos estão disponíveis em https://docbits.com/doc/field-mappings/.

![](https://lh7-us.googleusercontent.com/0O76spiOI_ZofZiDYRtzuphCzPycktfvxzeEa9MTG3fxeI3bQPjREIyh2sVEwzyGthFzlwdHo1OPifIVpcSMS9yv2WjfIfacCdUQwgvCQu-dXf6aZutRYmrMSCoTFv4mCYtndtLL0-N8NjrlR6oIy-A)

Após concluir as etapas acima, você terá configurado com sucesso o BOD Sync.ChartOfAccounts. Clique no ícone PLUS para adicionar o próximo e último BOD.

**Sync.CodeDefinition (TotalFlexDimensions)**

A aba de conexão para o seu ponto de conexão do CodeDefinition deve se parecer com o ilustrado abaixo. Dê ao ponto de conexão um nome e descrição apropriados, além de importar a Conta de Serviço que você criou.

* Selecione "Enviar para API"
![](https://lh7-us.googleusercontent.com/h-HCsruFxSb6FVNKRRfLcbeiLnRXrQYDRmVH5cK\_N-PgIVkkA8zY1gd4T0w8Nq9f\_x7AFnR3D\_veVdI6In7DoIRebiFbXfIleXROV2AoAG\_\_C00UnvFapAFvPuGTwYxQfuZpeKk1yXsJE9\_dQ-mX2M4)

* Procure o BOD Sync.CodeDefinition

![](https://lh7-us.googleusercontent.com/WrXZYGIgQMRuWXG8pWHbI-6TQj6VyC9\_Opon05kup2gfDva-JwFShHzusw5sz78cq643hBF5dEJx4ZOqFXjUQm\_oqAB00O3Z\_Xd5Bdf\_4h\_Criq5g-8OeVIz69N6vqNraz\_zCfxZQur-37VT5VzWka0)

![](https://lh7-us.googleusercontent.com/5Mn6YBvca3Ejc9EIemE3UIHZ4sLzDObOr5RF4TsOucRPkFiIX-4ot7FSMb7TsspFsH\_ysbSZ8zB3xgM1zXboK5jBqqTbVDMNbsUEQOrwfzSkHfuhB44m2j9V0LRMalHJNtujOmz4FJd8Ey69VvdJ6EM)

* Mude para a aba ION API, copie o nome da API e procure a Chamada da API pressionando o botão SELECIONAR

![](https://lh7-us.googleusercontent.com/lQNNzs9RNxvf85YGk0pq3-8vuwqXgzkfl-W4a8qcuFdThRTf4r6aJEmo3IXGp0cykwy6cml3AIRWwR3N8GZRbpL8yUynqKPeoTlmJ5CiKeJSmxm7Ea1aU3L8KXecM\_yv2mhDobYA09zaSV8kKAVs70A)

![](https://lh7-us.googleusercontent.com/1bE6Zgval5nkr9xxBGLgL0tk2f5IKN-OYng-9BzrPqX4aGq06emYHtICMgaIlAtXjP9sjQ8KHeL3Pa8gBgGMLFwmiArb9Lh9iX-mZ3X59Oblo7HRfZvD29jrifb0\_pJA4FMtHThpZq\_Vi\_nTeXB1XUQ)

* Em seguida, mude para a aba Corpo da Solicitação

![](https://lh7-us.googleusercontent.com/0MVLj442YbPOa83BtT8VwV9WG-Jl3DajGm4MGKwzsdD6QZLwtFhwhghCUX7ShlsbDogDmflsa4C5CmoxNqrFqNh\_ngxQ-rwoNAnWif4tYbwzTdEmAVy7kGRMs8v2VTDaAWsXk5nbRHFoszXeuCp8DGk)

* Aqui é onde você irá configurar o mapeamento de campos para este BOD, sua configuração deve ser semelhante à seguinte. Os mapeamentos de campos estão disponíveis em https://docbits.com/doc/field-mappings/.

![](https://lh7-us.googleusercontent.com/tmDr3sAIr\_S7tRPebboyt9TPSGEBU4eC0zS04BcsDy4B4yQ3xdv8k-DlBjHXPy0P4slyLKYaRxM9s93Qx6Wf\_fI82St3XcmzsZwxKgRnXWHkzDcKj5oVYdtnW9I3dX8kM1rgxAYuRBIrWKSUhx8JZYk)

Após concluir as etapas acima, você terá configurado com sucesso o BOD Sync.CodeDefinition para a tabela de dados mestre TotalFlexDimensions.

#### **FinalFlexDimensions**

A aba de conexão para o seu ponto de conexão FinalFlexDimensions deve se parecer com o ilustrado abaixo. Dê ao ponto de conexão um nome e descrição apropriados, além de importar a Conta de Serviço que você criou.

![](https://lh7-us.googleusercontent.com/iOmkBrlLIeok6YuiHW\_qZl3jCr6HYB3-2FMiEtME1UUQFPHjjL1cBsRaHHtdpVveyQL3YHcV0FabTQWtQgS-gkB0q6ztI0QELrI5xX4fN1KfcGyjtOcmWbsFeHZ7tOw4ZjZjSJ4LXpTWGpVWZyBGji0)

![](https://lh7-us.googleusercontent.com/WOZFs6pSjqD3NFGMlv4PTu6UyZ9cHcAywiOccMn4h2TKqgF-Rz5ROXhCsFd97wPmtGtv0fvA902vcf6UUULhXAkyD22Vn3kUZwaLbCcOqjKbjeoKvPjcYemhi8qy\_pbc8hTNGhRj7oJCBBm8GOOenac)

Você precisará adicionar um BOD nesta seção para este ponto de conexão. Este sendo o Sync.CodeDefinition, para adicionar este BOD, faça o seguinte:

A aba de conexão para o seu ponto de conexão CodeDefinition deve se parecer com o ilustrado abaixo. Dê ao ponto de conexão um nome e descrição apropriados, além de importar a Conta de Serviço que você criou.

* Selecione "Enviar para API"

![](https://lh7-us.googleusercontent.com/TjKLqUUaxoJSg7dUvkjKWKz7OYLfTKdFJT3pjsI5KKBcwB\_lGNQJz1hYQvM6KW9xIjryZbBUvRXLg5bKr3zNSgOPmXt9fl0BN1489jxnxXqRnS4vt9n3iCott-JOtm\_qUmMq1T5xXFD-reH8GYEDzio)

* Procure o BOD Sync.CodeDefinition
* Em seguida, mude para a guia Corpo da Solicitação

![](https://lh7-us.googleusercontent.com/LRDKhs2rq92Zef63nYy9NNK6bapmlPKUX10NSrRGBhvhdXIgBRte4sGunmOBUzymgnWnAv1O\_qV0AKsULSXsGT1kvorG0Pl0vQFW0exV2sqyUXhgiBMthRYTQbB10c6oI4P6Z139A8VqZVeg6c2HkZ4)

* Aqui é onde você irá configurar o mapeamento de campos para este BOD, sua configuração deve ser semelhante ao seguinte. Os mapeamentos de campos estão disponíveis em https://docbits.com/doc/field-mappings/.

![](https://lh7-us.googleusercontent.com/bjoXs4ZSra4dgpf2rC8GwA-uB\_Qp6INkdCapR7M03EV7cuqKzeVPWRCq4EHTZVeKpL92sdesL0iuHTHD1Ed5WHpr7Z15XOJMkPBlWgfbapzD4ZjfSre29Ii2SLGOvjs9-85SougBpDGzzTseAcWNVUo)

Depois de concluir as etapas acima, você terá configurado com sucesso o BOD Sync.CodeDefinition para a tabela de dados mestre FinalFlexDimensions.

## **Fluxos de Dados**

Você precisará configurar dois fluxos de dados separados para Auto Accounting:

* ChartOfAccounts
* FinalFlexDimensions

### **ChartOfAccounts**

Uma visão geral deste fluxo de dados é mostrada abaixo (a quantidade de pontos de conexão da API DocBits no final depende da quantidade de ambientes diferentes que você está configurando).

![](https://lh7-us.googleusercontent.com/xog1wW9zE0PeVF\_SzaVS5qWxR2UuHKVR9cD4n6hxD9IAm\_jqJJHKGMCvmsF4V4bcVhd\_zaepEBrbK6wTd6kd7eqDL2Apwe799ewGo8TwMVrtRPwJcImuRjvWJxmcBiMvTjla0KgoGXhMD6oCeZFvOcM)

#### **Empresa LN**

![](https://lh7-us.googleusercontent.com/jaFn8KOdu907VI7vx2fkgtJZYiKw37LJ9ySqKWlgm5MLOuUcElJdOCpThwwa2NdE2eJ4iLWdfM\_Nlrkiq0BpIvrZDvyYJng94oZyaOpCIAhF5ZCTwQ0asfceY-KnIjZYrlQ5QsApnvU-hdMp8waQNeA)

A configuração deste ponto de conexão depende da empresa LN que contém os dados mestres que você deseja importar para o DocBits, a sua deve ser semelhante ao que é mostrado abaixo.

![](https://lh7-us.googleusercontent.com/k28OYp8vkZZcWCKJTiSFZkDE0SlfLgE\_S3o37OhuvNsOR7Tli3xCYzqN3fRTfrlgE9fF9tYkOXCiC7kZeweCGA86wEDEMj0wKRUO7Idba1d8mY-v15uJGpYlkhZEKSlUA83yPvSlp-aRn2e-pYckXyc)

#### **Documento**

![](https://lh7-us.googleusercontent.com/n9ABWRQI8k7SVDk6RsYcvI\_\_r5CWXdMDn49fKkAy3T\_0s3TTJp4aMV5K4hsiGh56YKrxcUaqmUZfj3\_QBSS2eSZ1TAPCoI5-LnJCC-JYv8K5XEOZsJLXX77EKGZCs37qtKiFHD9P9KpW2jhOEX4bu1Y)

Os seguintes documentos precisam ser adicionados ao fluxo de dados:

* Sync.ChartOfAccounts
* Sync.CodeDefinition

![](https://lh7-us.googleusercontent.com/c6Dhk5iR1fJXqjrXsbSMmkIDBl3eaRNoiijw9WMA69HSrXMKqOjMEKtRtqfXbHcy9fQH1etprR2IuZO6xpMBnY6EYuU6cyBCFjHx4yN2KxxRwTqX12TwSsUaF7wFySImLki86BUKRMW-0YKQJfQTWOw)

#### **DocBits (ChartOfAccounts)**

![](https://lh7-us.googleusercontent.com/JhBa8R1tRR\_GcoBmas\_mJ-QPT3XTNyGAdwh48N7pISM-fRNa3lfuZB7MhAScDbbCtpgGXtxx140w0bcEwgVdtMkGDh6S56uVsm039Z\_8FGA\_FwA2aSvJftr8MeHr3e9WPwRZqugKvRD\_kIVnQdexFek)

Aqui é onde você adiciona o ponto de conexão da API ChartOfAccounts que você criou anteriormente, a configuração para isso deve ser semelhante a esta

![](https://lh7-us.googleusercontent.com/yyq6JularNBP\_GpUbDLQ-KWu6utcEZefLXcoHboFa6rcmbN1e8QrdLkab9h2QBWuW-V-i7edmqpTWJwtqWg14GKLDnukyLGuljKXue\_XH\_bLmL2dNz5dECDI\_lkg9hO84nFIDyYWYatkzRkxAYyJe6w)

### **FinalFlexDimensions**

Uma visão geral deste fluxo de dados é mostrada abaixo (a quantidade de pontos de conexão da API DocBits no final depende da quantidade de ambientes diferentes que você está configurando).

![](https://lh7-us.googleusercontent.com/MQyQxEHmvG0vX4VXSnpntbXBGQBtC5uvMeNXklp-EETOIMLZNOJqwOlZp9xm\_\_Lj--o3bJETADpxgZkajW0H0xOE2Gvib9OeU3BeV-mj4lpKFqPQ8A4fymQJDjTZNI8fzrOxYqa595I0\_C3b8QkoTb0)

#### **Empresa LN**

A configuração deste ponto de conexão depende da empresa LN que contém os dados mestres que você deseja importar para o DocBits, a sua deve ser semelhante ao que é mostrado abaixo.

![](https://lh7-us.googleusercontent.com/D25DTQRX3yecDDMmp\_UvmS9b6AWPYue8LdUueurlCTYg0qWw\_SyM0lCx1sn3VSK0m5MOilgmGWJ261YLr1MlTm9G452QyDQXbyN7DXsQpmmINEbVL5g-OIhpYKN14XQk6oEMqwoTgvpLNKS9\_MkU-sk)

![](https://lh7-us.googleusercontent.com/rGMdEdvYixTZ5wmS5ptBiGcxoOT0abpASTeSDzEFH3SSx-G97gSxIniXja2R3erYP4oIxyVezvL7VjqXKcKd5i6caNZHI-1gVIi2jrKfy\_yVFQ5T80n3ZpR1wSiPWCh\_8affNONcGAcuokvN69-Urfg)
#### **Documento**

![](https://lh7-us.googleusercontent.com/WyltkYqwzyofXZpwm\_x1-SiM5MCbvDoKPQ9AVOT6nyxXnqXqQn4G-uM7BO2hNRJii91EODf5mjIwS85eOfJ\_UyATLAWqbXegd54leKsK\_zNlVWQNm79yoyTb\_Ok3605NEOM\_Hu\_ov-yaboAQ26PpmTk)

O seguinte documento precisa ser adicionado ao fluxo de dados:

* Sync.CodeDefinition

![](https://lh7-us.googleusercontent.com/YIvKeqyGUDBZIoi7I6jhTIlUYtsgYEMeKA3h4Xm9KHz5pYWssDuIaq7343RQdEsxMznTNnReWEB2OCqBQGvgzi7HEOVGlX5EqPa2JEO5sC1LpUF-OXvYLO5a7LMbE2h2YY1Bk2rRnNbCjAZqIMuIxGw)

**DocBits (FlexDimensions)**

![](https://lh7-us.googleusercontent.com/zNJteyBB\_TcRKGE7GL3iPPlFaOqbij5ag37NdNW5GcZBz0xMmb9iev8EktCSJDSNkeZPOnCf-5nImxJjn6RIBTg3x8xJrLK-Z0Z48VTXXLPNIO-3NnmDEVVF-9oHteOQWIjCIMhhzKLK7iCL\_jVsfEY)

Aqui é onde você adiciona o ponto de conexão da API FinalFlexDimensions que você criou anteriormente, a configuração para isso deve se parecer com isso

![](https://lh7-us.googleusercontent.com/ymjxWkOzchUu91ovhE1eE58mSRCyrclNKsNoK48gFcSwKRVuc9Zfy7QZzJ83ATXUWJO4sgPpcNEVPyYZX8dr-sJoEfYKez-WtScX\_hnmOfH-2wBcFKrhxy5wwBUSlKP-ayxcMnCiQ6DKrgqYkfL4xQg)

## **Desencadeamento BOD (M3)**

Depois que tudo acima estiver concluído, você precisará navegar até o Infor LN e acionar os BODs para que os vários dados mestres necessários para a Contabilidade Automática cheguem ao DocBits.

![](https://lh7-us.googleusercontent.com/OG5eKwuynVhgRagfTwylC2hT6lYMKIgn0ogn1RPShzv7gbE2IO4lC8YzKWDmHa6l6waMREGwVLZmhsCOhUWNrp\_7rkkdrVgo5Z8s84V475UO927BPujEwsX8SY7kRsZBt3R0GUWD13hogj0LdgqNotU)

No menu acima, na guia do menu esquerdo, selecione Comum → Mensagens BOD → Publicar BODs → Publicar Dados Mestres Financeiros. No menu seguinte, você encontrará os BODs FlexDimensions e ChartOfAccounts para publicar.

![](https://lh7-us.googleusercontent.com/KWv\_YZ0BuoZrBvnp2MRzXKRRH1pID7V0iwjCkT4xt7NcbHYoZnFS6wnM\_itC3RzNNGJ95565KynkMFuPb-1NjY0zOGjvlINvVQIrJBcm8daOZa3UiDIB0zBPlt5BS5KavsmYcXHWBQZ9NytMg6NJezs)

Selecione os seguintes BODs para publicar simplesmente marcando cada caixa, nenhuma outra alteração precisa ser feita, pois queremos publicar todos esses BODs para que os dados mestres estejam completos no DocBits.

![](https://lh7-us.googleusercontent.com/cp9CKdRYofwTrRodTNbZDfMmi\_Q23jchyt\_w7hFkGvvoBo89uhSRoKz0uD2cm2M0tLDmrkb6-8qq9z5EfX-ciEmraWqyytxH09jMK8jVVunb8zjK9EkvGhyl07Igoa4sf8hCLvyGnIlHMVjeLzMFrD8)

![](https://lh7-us.googleusercontent.com/cu8PW0WenwC5jBBFa4trAua-d8zYxi60S2syvKHoBoL2Tk9jdQAOQTvUvGZWSR3cpErwDUZ3WHkm4cDCwS1ZhSJyiQltf43\_Re05WddfxQwJ69C3E\_z\_0bMhEwbq3NasV3Q2waKJlfyBk1oIWdVDjps)

Depois de selecionar ambos os BODs acima, navegue até a guia Opções

![](https://lh7-us.googleusercontent.com/imBr628dcJJoNBknxVfKjoWindKT\_\_5AzmYDVXIaHF\_n0RWQUSiK07EHH1df0L2xxCOC5z36UQOfsknF4-GwUgZ9tDZcwDosjxChqFft0GGvVo1JAkPpK\_St-GB7NW1RlBgTszID4YQteYiZlFKPuz4)

Uma vez no menu Opções, selecione as seguintes opções e selecione PROCESSAR para publicar os BODs.

![](https://lh7-us.googleusercontent.com/3LH3Me8kacFfp1QH0VFMIfzQtWyFt12IgRQzcAcJByoPQtjhxDnQKE3EjNLO349WeW2WINoFwwrpQJIOoSXBBM\_tmIecJLJEyLipUHXel5yRw7H98OdfydXJdZcChaHvnnwc86wihiblnthMobZyu\_s)

Depois disso, você deve ver as três tabelas de dados mestres separadas em seu(s) ambiente(s) DocBits em Master Data Lookup:

* chartofaccounts
* totalflexdimensions
* finalflexdimensions
