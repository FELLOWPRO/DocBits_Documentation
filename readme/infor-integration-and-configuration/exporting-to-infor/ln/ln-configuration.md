# Configuração do LN

## Pré-requisitos

Já criou:

* Um endpoint da API ION
* Um ficheiro da API ION
* Um ficheiro de mapeamento BOD
* Um ficheiro de mapeamento IDM

## Importar ficheiros de mapeamento

Antes de configurar o fluxo de dados, importe os ficheiros de mapeamento no InforOS.

No ION Desk → Connect, abra Mappings.

![Navegação do ION Desk com o grupo Connect expandido e as entradas Data Flows, API Flows, Connection Points, File Templates e Enterprise Locations](https://lh7-us.googleusercontent.com/fAUUcBUSxIWqLjYEHH78O2Mfq0P4d4D42OgCNFPdpUQTM5ZHu\_BcKz9DmWe0AlHe3--ff7z9mfYTrt7oAkf2uknBwkV2VWayEpiJ\_aAIxcJil5LNiep4U6KZr3\_tBfs1RRwXoW749q3FUxurXy\_pT\_k)

Clique no ícone de importação.

![Barra de ferramentas da página Mappings no ION Desk com o ícone redondo verde de importação](https://lh7-us.googleusercontent.com/d\_KYA9LgiiW1A95CH9hwU1AC1u5x25T4ET-4sAqpZkVOexHc4WcbwPXUaKt3O9fR3Btvv-NEGbCWwnnb8SfomnnO22M8YTIqWdvan-SkbG0cu1MWkjwOn\_Vd\_b6rJaQng8A92JTa5YKBms4RuIvwmb0)

* Selecione os ficheiros necessários: SyncCaptDoc\_SyncSuppInv, SyncSupplierInvoice\_LoadSupplierInvoice e LoadSupplierInvoice\_ProcessSupplierInvoice.
* Depois de importar os ficheiros, aprove cada um através do ícone de verificação no respetivo bloco do painel de mapeamentos.

## Do DocBits para o LN

Para configurar o fluxo de dados, abra o ION Desk e selecione Data Flow → + ADD → Document Flow, como no exemplo abaixo.

![Página Data Flows no ION Desk com a navegação à esquerda, o fluxo DF_SLTStAPI na lista e as entradas de menu Document Flow e Data Lake Flow](https://lh7-us.googleusercontent.com/rjPVR1EFKw\_gZI1Ztg9Aqt4pFw10rii7WU-yddLIz22a\_Fn3s1HSYDRmQVvgZtX\_85nb2ipNqJ1JU49NIE8a57TIur7jqoMuKFKlb-RrfnRFxiA1TefzofKPJ32fzIdDWI8PmnD-aDw4qhQj4e0dd9I)

Nesta página, irá construir o fluxo de informação do DocBits para o LN.

![Novo Document Flow com o painel de propriedades vazio e as mensagens Document flow name must be specified e The document flow has no activities](https://lh7-us.googleusercontent.com/9C7BaoiHWRaav0ytCbYkxEYG12f-64qyagsl8H2eq5TXUySRE1s3x\_-lVRbK6tpTxvbRYKvwyWO\_6ASSQ6Rn62LQR9ZvMRpRXq9UymZLS0I8IZ-hOzX58iYtTruqSo5WdgIXwEPjMlb1dnuFuhN8IS8)

O fluxo LN será semelhante ao seguinte. Os vários percursos correspondem a diferentes tipos de documento; neste exemplo, iremos seguir o fluxo da fatura.

![Tela do fluxo de dados com vários caminhos para tipos de documento diferentes, cada caminho composto por um ponto de conexão DocBits, um mapeamento e um ponto de conexão LN](https://lh7-us.googleusercontent.com/gltDE9JxeGb7Ufg9Ldl-JIJ95zfWHnQtyOqys2QKCiTlIn\_PdAyBLFYmTVCh9c-TxF5xNQR3G8Hmn4EXK94t6MJ-1WzlZg1Zl7HNoxfR56zC8dT1skmxLTj7rtnSl0JTQJD\_3myQY4Qcd9motySYh9U)

Arraste os componentes da secção superior para construir a cadeia.

Na cadeia, o DocBits e o LN são aplicações. Entre eles, os mapeamentos convertem os dados para um formato compreendido pela etapa seguinte e encaminham a informação para os destinos corretos.

![Detalhe da tela do fluxo de dados com os nós DocBits-DEV, MappingDeliver, Load Supplier, PurchaseOrder e os pontos de conexão LN-200-41 e LN-200-4](https://lh7-us.googleusercontent.com/Gwk0C0gsnMSlgEwRx0\_1GDMJEu8Z1TAhKo8gxHN8GxFFKGgb257a684Hj0eNSLTIK5v8F7yzJ1hIHrC\_3I9RLY0S-u3ZDhmkD6iJbYAvtCAeFPWHBVLOqyCH7FKsl2SKAfXL-AdtNowqdol9PzS4qJM)

### Aplicação DocBits

Atribua um nome como «DocBits», selecione o ícone de adição e procure o ponto de ligação criado anteriormente, como DocBits\_Export. Selecione-o.

Para criar este ponto de ligação, abra ION Desk → Connect → Connection Points.

![Navegação do ION Desk com o grupo Connect expandido e as entradas Data Flows, API Flows, Mappings e Connection Points](https://lh7-us.googleusercontent.com/1SZJN-GW7BP-fvUHZ-tCJ4xNXx0ABRP3J9eMzF3BTKIY54J-pK4bYy4fOVHCaI6A2sdrYekWJsY9ky8dXz36l\_FwwzzEnO1IjxNkMqlV-Y4UvyFIei73Z9C19m9bzTr3gCL3IpTUqiV280id1vJE530)

Clique em «+ Add».

![Página Connection Points no ION Desk com o grupo Connect aberto na navegação](https://lh7-us.googleusercontent.com/ZJ1212Gwdk-b2-LVbEd2ZDzc\_AqaEEYtIN0fC6d6P4EaWdTKj6nOzGDbA5sxdBtMcTrWopfDmd7GTahbwkDpj3uvmMYgvEUQa6qmi58NFGvtcgAtIwYr952Yu7Lcj802iHtQ\_vj\_-XPdegP1P0ySdos)

Selecione «IMS via API Gateway» e preencha os dados seguintes.

![Janela Infor Application Connection Point para IMS via API Gateway com o nome DocBits-Sandbox-Export, o ION API Client Id e o Logical ID infor.ims.docbits-sandbox-export](https://lh7-us.googleusercontent.com/H4YCH-324EzrxKkrbRs0SFTsHch5eK74gXleSpfI03uJ5frIEFjwofu7p6bsYO1lS7sVqamWDZMXrGfEgewdROyhTYLkn7MuCgwb7oQxOLJoH3NsnMsqTOgT3WxlihUkJdNy-WTai5kPz8ZjdtTDQ9I)

O ION API Client ID encontra-se no valor «ci» do ficheiro da API ION criado no guia de criação desse ficheiro.

Abra o separador Document e adicione o BOD Sync.CaptureDocument ao ponto de ligação DocBits, como no exemplo abaixo.

![Ponto de conexão DocBits-Sandbox-Export com o separador Documents aberto e o documento Sync.CaptureDocument atribuído](https://lh7-us.googleusercontent.com/Wy2BIr1z\_RqU-yMkXo6vOu64QC6c66OdHOxdI6PPy0yJv1jIAJF0OYITULxTFoPUK93SK3jvNm67tcxqjiEBIk0Wbu1Q1s-mSIUuPjJorcYyXY7vjsHOnoutn6tE8r6yE\_333uCWuKvKiVoo99FrXVg)

Guarde o ponto de ligação no ícone de disquete no canto superior esquerdo.

Volte à secção Dataflow do ION Desk para abrir o fluxo de dados. A aplicação DocBits deve ser semelhante à seguinte.

![Painel Application Activity Properties da aplicação DocBits com o nome DocBits-Sandbox-Export e a descrição DocBits-Sandbox-Export](https://lh7-us.googleusercontent.com/cDWHmRP85YNLu7JRzq4CSezncTgP2ZOkEfZSqXK9JEq4bSwsddU7VKg8leoxaJ5zeFAbDzXrNkztmeWDIXbHwjxfUa\_IpATDDwykv-OlZ2zaOVGHVqRZZpVLJ5Cq5Qla1pZk5sBV39I98lUfGao65Mw)

### Mapeamento 1

O primeiro nó de mapeamento deve ser semelhante ao seguinte.

![Painel Mapping Properties do primeiro nó de mapeamento com os campos Name e Description e a lista pendente Mapping](https://lh7-us.googleusercontent.com/9tlIun\_ipbTp15aMX3xN2DGlDjAZ1oI4AFWXwbP7yoFLeQNqcw\_L3Z1djaqcbxP1tsp1R-nq6ZJqEzsoKe1-SmLrJNmYrJ4HJircLEwMxfmif-p2T8nqbuuxHLLLzQJ6E6tNG6MzghOpoEAt41ea2GY)

### Mapeamento 2

O segundo nó de mapeamento deve ser semelhante ao seguinte.

![Painel Mapping Properties do segundo nó de mapeamento com os campos Name e Description e a lista pendente Mapping](https://lh7-us.googleusercontent.com/ZDYzTAfm3MHnEIKHa2tDl7NPbjzxv8jH-KL8O0pRhi1JYtqiiVz0-GQv5N4roVWi1STopQkFV9YHbEXdyzwYxK2Oq6mUv6tuqKDp-2bc-aPVgEXdEBd2hmW-6j6JRhEympyw9yUTrCDQRKlDQ41C5Ao)

### Aplicação LN

Deverá existir na Infor um ponto de ligação LN, ou equivalente, para a empresa LN correta. Tal como na aplicação DocBits, selecione-o no ícone «+». O resultado deve ser semelhante ao seguinte.

![Painel Application Activity Properties da aplicação LN com o nome LN-200 e a descrição In01_0200 LN Farm](https://lh7-us.googleusercontent.com/mRXL11f68EtQHHjl40QmCisy7S1aUezqCzufPTZWgYHhWLK2Yw0UY82O\_dgbAhBChFHHYUMBDSWWb-PEKyohJWOp5gvufat431ezpA2cIHMtry7XEDxhnNzPB68uSMkFAXhX1x4GyiH6Cxp-USxDnHE)

### BODs

![Tela do fluxo de dados com os nós DocBits-DEV, MappingDeliver, Load Supplier, PurchaseOrder, SalesOrder e AdvancedShip acima da entrada End](https://lh7-us.googleusercontent.com/de8OyDF4yMoHaXsxM9weJdm8mKDzL97kFRr00fhoHAxxKXb2BgMcMM2shyxi1S7cBwzSAUy2u8bZV4sJOVqgXt8Mcge6L2CXxbfVGiqXUwKwF6A5mgt4zfGPYltaZuLazOJYu2u7arszJE6IonMOskk)

As configurações devem ser semelhantes às seguintes:

#### Primeiro

![Lista pendente Documents do primeiro nó com a entrada Sync.CaptureDocument](https://lh7-us.googleusercontent.com/rj\_qpiML1a2dNxj6ItiRxescymVtD6LHIAum3UPrPERAavhkt81lpjcyAFmn\_lmxtqUDVTm\_kiZ9f02Lqh9w-SAWmcxvGuxWITVvhv9qg04HaJXGH7VfRiO4Iv1LtDxfKYFyUWPLzCE4L3yP4hcdGnY)

#### Segundo

![Lista pendente Documents do segundo nó com a entrada Load.SupplierInvoice](https://lh7-us.googleusercontent.com/TCxMS-RhoJcUyBko36Lfpa8D71qk-ZSN-lME7Oq8cfPACVV0Ci7Lnv6y\_MF\_53U763ZA74xq6icEfgDUwYYJ9UJK0kCiLHQZpJYmc\_ywjB32UGrpDnh7AjoHpI5AtWd3yZR3RsMaki1AYenpdG4X9X8)

#### Terceiro

![Lista pendente Documents do terceiro nó com a entrada Process.SupplierInvoice](https://lh7-us.googleusercontent.com/VPYJyfpO0RZueW46s2Y8W2H-tQFlMfIdP1Sf8qMB8BfTxefgQ5dhsaAxL36R7cdvmKR26Q\_epAj9\_i6CzUO6C-PHjStEynBDkjtwId4BSuH6-zJklmsr25XcNH2AY7pSwOQ\_rbCCixhWcaJg2kHyyYw)

O último ícone deve estar vazio, porque não transporta documentos nem informação.

Depois de adicionar os nós necessários, prima este botão para ativar o fluxo de dados.

![Barra de ferramentas do Document Flow com os botões para adicionar e remover pontos de conexão e o botão para ativar o fluxo de dados, sob o nome DocBits-Export-M3](https://lh7-us.googleusercontent.com/WjQeGz\_effl\_RlkWC4CdJS9Dg\_9DpsIz3meKOsa7GbU9RFSrYMw3PpbXFat6cGsA4gvEGS-0D-YFrZj9K2wK3Irap-30mcQ5kr5k4Gy2gm7DLJdYpzJgeBRVInyAYfGmGXu2dCQvmX9ballRbSwyq3o)
