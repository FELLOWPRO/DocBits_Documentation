# Configuração do LN

Este guia combina exemplos históricos do Infor ION com o formulário de exportação LN atual do DocBits. As imagens do Infor ilustram os passos individuais; os nomes de empresas, os nomes de mapeamentos e a disposição nessas imagens são exemplos. Antes de ativar um fluxo, peça ao administrador do Infor que confirme os pontos de ligação, o pacote de mapeamentos e as permissões BOD para a sua empresa LN. Nesta atualização da documentação não foi testada nenhuma ligação a uma empresa Infor nem a exportação de uma fatura.

## Pré-requisitos

Já criou:

* Um endpoint da API ION
* Um ficheiro da API ION
* Um ficheiro de mapeamento BOD
* Um ficheiro de mapeamento IDM

## Importar ficheiros de mapeamento

Antes de configurar o fluxo de dados, importe os ficheiros de mapeamento no InforOS.

No ION Desk, abra **Connect → Mappings**.

<figure><img src="https://lh7-us.googleusercontent.com/fAUUcBUSxIWqLjYEHH78O2Mfq0P4d4D42OgCNFPdpUQTM5ZHu_BcKz9DmWe0AlHe3--ff7z9mfYTrt7oAkf2uknBwkV2VWayEpiJ_aAIxcJil5LNiep4U6KZr3_tBfs1RRwXoW749q3FUxurXy_pT_k" alt="Exemplo histórico: navegação do ION Desk com o grupo Connect expandido e as entradas Data Flows, API Flows, Connection Points, File Templates e Enterprise Locations."><figcaption><p>Exemplo histórico: navegação do ION Desk com o grupo Connect expandido e as entradas Data Flows, API Flows, Connection Points, File Templates e Enterprise Locations. Confirme as definições correspondentes na sua empresa Infor.</p></figcaption></figure>

Clique no ícone de importação.

<figure><img src="https://lh7-us.googleusercontent.com/d_KYA9LgiiW1A95CH9hwU1AC1u5x25T4ET-4sAqpZkVOexHc4WcbwPXUaKt3O9fR3Btvv-NEGbCWwnnb8SfomnnO22M8YTIqWdvan-SkbG0cu1MWkjwOn_Vd_b6rJaQng8A92JTa5YKBms4RuIvwmb0" alt="Exemplo histórico: barra de ferramentas da página Mappings no ION Desk, com o ícone de importação assinalado."><figcaption><p>Exemplo histórico: barra de ferramentas da página Mappings no ION Desk, com o ícone de importação assinalado. Confirme as definições correspondentes na sua empresa Infor.</p></figcaption></figure>

* Selecione os ficheiros de mapeamento necessários: SyncCaptDoc\_SyncSuppInv, SyncSupplierInvoice\_LoadSupplierInvoice e LoadSupplierInvoice\_ProcessSupplierInvoice.
* Depois de importar todos os ficheiros de mapeamento, aprove cada um clicando no ícone de confirmação no respetivo bloco do painel de mapeamentos.

## Do DocBits para o LN

O passo seguinte é configurar o fluxo de dados no ION Desk. Abra a aplicação ION Desk e selecione **Data Flow → + ADD → Document Flow**, como no exemplo abaixo.

<figure><img src="https://lh7-us.googleusercontent.com/rjPVR1EFKw_gZI1Ztg9Aqt4pFw10rii7WU-yddLIz22a_Fn3s1HSYDRmQVvgZtX_85nb2ipNqJ1JU49NIE8a57TIur7jqoMuKFKlb-RrfnRFxiA1TefzofKPJ32fzIdDWI8PmnD-aDw4qhQj4e0dd9I" alt="Exemplo histórico: página Data Flows no ION Desk com a navegação à esquerda, o fluxo DF_SLTStAPI na lista e as entradas de menu Document Flow e Data Lake Flow."><figcaption><p>Exemplo histórico: página Data Flows no ION Desk com a navegação à esquerda, o fluxo DF_SLTStAPI na lista e as entradas de menu Document Flow e Data Lake Flow. Confirme as definições correspondentes na sua empresa Infor.</p></figcaption></figure>

Nesta área de trabalho irá construir o fluxo de informação do DocBits para o LN.

<figure><img src="https://lh7-us.googleusercontent.com/9C7BaoiHWRaav0ytCbYkxEYG12f-64qyagsl8H2eq5TXUySRE1s3x_-lVRbK6tpTxvbRYKvwyWO_6ASSQ6Rn62LQR9ZvMRpRXq9UymZLS0I8IZ-hOzX58iYtTruqSo5WdgIXwEPjMlb1dnuFuhN8IS8" alt="Exemplo histórico: novo Document Flow com o painel de propriedades vazio e as mensagens Document flow name must be specified e The document flow has no activities."><figcaption><p>Exemplo histórico: novo Document Flow com o painel de propriedades vazio e as mensagens Document flow name must be specified e The document flow has no activities. Confirme as definições correspondentes na sua empresa Infor.</p></figcaption></figure>

O fluxo de dados LN será semelhante ao seguinte. Existem vários percursos porque cada um se destina a um tipo de documento específico; neste exemplo seguimos o fluxo de dados da fatura.

<figure><img src="https://lh7-us.googleusercontent.com/gltDE9JxeGb7Ufg9Ldl-JIJ95zfWHnQtyOqys2QKCiTlIn_PdAyBLFYmTVCh9c-TxF5xNQR3G8Hmn4EXK94t6MJ-1WzlZg1Zl7HNoxfR56zC8dT1skmxLTj7rtnSl0JTQJD_3myQY4Qcd9motySYh9U" alt="Exemplo histórico: área do fluxo de dados com vários percursos para diferentes tipos de documento, cada percurso composto por um ponto de ligação DocBits, um mapeamento e um ponto de ligação LN."><figcaption><p>Exemplo histórico: área do fluxo de dados com vários percursos para diferentes tipos de documento, cada percurso composto por um ponto de ligação DocBits, um mapeamento e um ponto de ligação LN. Confirme as definições correspondentes na sua empresa Infor.</p></figcaption></figure>

Todos os elementos da cadeia são arrastados a partir da secção superior.

Na cadeia, o DocBits e o LN são aplicações e, entre eles, os mapeamentos convertem os dados para um formato compreendido pela etapa seguinte e encaminham a informação para onde é necessária.

<figure><img src="https://lh7-us.googleusercontent.com/Gwk0C0gsnMSlgEwRx0_1GDMJEu8Z1TAhKo8gxHN8GxFFKGgb257a684Hj0eNSLTIK5v8F7yzJ1hIHrC_3I9RLY0S-u3ZDhmkD6iJbYAvtCAeFPWHBVLOqyCH7FKsl2SKAfXL-AdtNowqdol9PzS4qJM" alt="Exemplo histórico: paleta de atividades e fluxo do ION, em que as atividades de aplicação representam o DocBits e o LN, com atividades de mapeamento entre elas."><figcaption><p>Exemplo histórico: paleta de atividades e fluxo do ION, em que as atividades de aplicação representam o DocBits e o LN, com atividades de mapeamento entre elas. Confirme as definições correspondentes na sua empresa Infor.</p></figcaption></figure>

### Aplicação DocBits

Atribua-lhe um nome adequado, como «DocBits», selecione o sinal de adição e procure o ponto de ligação que criou anteriormente, como DocBits\_Export, e clique nele.

Para criar este ponto de ligação, abra **ION Desk → Connect → Connection Points**.

<figure><img src="https://lh7-us.googleusercontent.com/1SZJN-GW7BP-fvUHZ-tCJ4xNXx0ABRP3J9eMzF3BTKIY54J-pK4bYy4fOVHCaI6A2sdrYekWJsY9ky8dXz36l_FwwzzEnO1IjxNkMqlV-Y4UvyFIei73Z9C19m9bzTr3gCL3IpTUqiV280id1vJE530" alt="Exemplo histórico: navegação do ION Desk com o grupo Connect expandido e as entradas Data Flows, API Flows, Mappings e Connection Points."><figcaption><p>Exemplo histórico: navegação do ION Desk com o grupo Connect expandido e as entradas Data Flows, API Flows, Mappings e Connection Points. Confirme as definições correspondentes na sua empresa Infor.</p></figcaption></figure>

Clique em **+ Add**.

<figure><img src="https://lh7-us.googleusercontent.com/ZJ1212Gwdk-b2-LVbEd2ZDzc_AqaEEYtIN0fC6d6P4EaWdTKj6nOzGDbA5sxdBtMcTrWopfDmd7GTahbwkDpj3uvmMYgvEUQa6qmi58NFGvtcgAtIwYr952Yu7Lcj802iHtQ_vj_-XPdegP1P0ySdos" alt="Exemplo histórico: página Connection Points no ION Desk com o grupo Connect aberto na navegação."><figcaption><p>Exemplo histórico: página Connection Points no ION Desk com o grupo Connect aberto na navegação. Confirme as definições correspondentes na sua empresa Infor.</p></figcaption></figure>

Selecione **IMS via API Gateway** e preencha as informações seguintes.

<figure><img src="https://lh7-us.googleusercontent.com/H4YCH-324EzrxKkrbRs0SFTsHch5eK74gXleSpfI03uJ5frIEFjwofu7p6bsYO1lS7sVqamWDZMXrGfEgewdROyhTYLkn7MuCgwb7oQxOLJoH3NsnMsqTOgT3WxlihUkJdNy-WTai5kPz8ZjdtTDQ9I" alt="Exemplo histórico: ponto de ligação IMS via API Gateway com um identificador lógico de exemplo e o campo ION API Client Id ocultado."><figcaption><p>Exemplo histórico: ponto de ligação IMS via API Gateway com um identificador lógico de exemplo e o campo ION API Client Id ocultado. Confirme as definições correspondentes na sua empresa Infor.</p></figcaption></figure>

O Client ID da ION API é o valor `ci` do seu ficheiro `.ionapi`. Obtenha o ficheiro específico da sua empresa junto do administrador do Infor autorizado. O ficheiro contém credenciais; mantenha-o fora de capturas de ecrã, tickets e Git. Consulte a [explicação dos campos de credenciais da ION API na documentação do Infor](https://docs.infor.com/crm/9.4.x/en-us/webclient/upi1639111995644.html).

Mude para o separador de documentos e adicione o BOD **Sync.CaptureDocument** ao ponto de ligação DocBits, como abaixo.

<figure><img src="https://lh7-us.googleusercontent.com/Wy2BIr1z_RqU-yMkXo6vOu64QC6c66OdHOxdI6PPy0yJv1jIAJF0OYITULxTFoPUK93SK3jvNm67tcxqjiEBIk0Wbu1Q1s-mSIUuPjJorcYyXY7vjsHOnoutn6tE8r6yE_333uCWuKvKiVoo99FrXVg" alt="Exemplo histórico: ponto de ligação DocBits-Sandbox-Export com o separador Documents aberto e o documento Sync.CaptureDocument associado."><figcaption><p>Exemplo histórico: ponto de ligação DocBits-Sandbox-Export com o separador Documents aberto e o documento Sync.CaptureDocument associado. Confirme as definições correspondentes na sua empresa Infor.</p></figcaption></figure>

Guarde o ponto de ligação com o ícone de disquete no canto superior esquerdo.

Volte à secção Dataflow do ION Desk para abrir o seu fluxo de dados. A aplicação DocBits deverá ficar semelhante à seguinte.

<figure><img src="https://lh7-us.googleusercontent.com/cDWHmRP85YNLu7JRzq4CSezncTgP2ZOkEfZSqXK9JEq4bSwsddU7VKg8leoxaJ5zeFAbDzXrNkztmeWDIXbHwjxfUa_IpATDDwykv-OlZ2zaOVGHVqRZZpVLJ5Cq5Qla1pZk5sBV39I98lUfGao65Mw" alt="Exemplo histórico: Application Activity Properties com o nome da aplicação DocBits-Sandbox e o ponto de ligação DocBits-Sandbox-Export selecionado."><figcaption><p>Exemplo histórico: Application Activity Properties com o nome da aplicação DocBits-Sandbox e o ponto de ligação DocBits-Sandbox-Export selecionado. Confirme as definições correspondentes na sua empresa Infor.</p></figcaption></figure>

### Mapeamento 1

O primeiro nó de mapeamento deverá ficar como se segue:

<figure><img src="https://lh7-us.googleusercontent.com/9tlIun_ipbTp15aMX3xN2DGlDjAZ1oI4AFWXwbP7yoFLeQNqcw_L3Z1djaqcbxP1tsp1R-nq6ZJqEzsoKe1-SmLrJNmYrJ4HJircLEwMxfmif-p2T8nqbuuxHLLLzQJ6E6tNG6MzghOpoEAt41ea2GY" alt="Exemplo histórico: propriedades do primeiro mapeamento, Capture2sync, com o mapeamento de exemplo LN_CaptureDocumentToSupplierInvoice_1."><figcaption><p>Exemplo histórico: propriedades do primeiro mapeamento, Capture2sync, com o mapeamento de exemplo LN_CaptureDocumentToSupplierInvoice_1. Confirme as definições correspondentes na sua empresa Infor.</p></figcaption></figure>

### Mapeamento 2

O segundo nó de mapeamento deverá ficar como se segue:

<figure><img src="https://lh7-us.googleusercontent.com/ZDYzTAfm3MHnEIKHa2tDl7NPbjzxv8jH-KL8O0pRhi1JYtqiiVz0-GQv5N4roVWi1STopQkFV9YHbEXdyzwYxK2Oq6mUv6tuqKDp-2bc-aPVgEXdEBd2hmW-6j6JRhEympyw9yUTrCDQRKlDQ41C5Ao" alt="Exemplo histórico: propriedades do segundo mapeamento, Load2Process, com o mapeamento de exemplo LoadSupplierToProcessSupplierInvoice."><figcaption><p>Exemplo histórico: propriedades do segundo mapeamento, Load2Process, com o mapeamento de exemplo LoadSupplierToProcessSupplierInvoice. Confirme as definições correspondentes na sua empresa Infor.</p></figcaption></figure>

### Aplicação LN

Deve já existir no Infor um ponto de ligação chamado LN ou com um nome semelhante, criado para a empresa LN correta. Tal como na aplicação DocBits, selecione-o clicando no sinal «+» e o resultado deverá ficar como se segue:

<figure><img src="https://lh7-us.googleusercontent.com/mRXL11f68EtQHHjl40QmCisy7S1aUezqCzufPTZWgYHhWLK2Yw0UY82O_dgbAhBChFHHYUMBDSWWb-PEKyohJWOp5gvufat431ezpA2cIHMtry7XEDxhnNzPB68uSMkFAXhX1x4GyiH6Cxp-USxDnHE" alt="Exemplo histórico: Application Activity Properties da aplicação LN com o nome de exemplo LN-200 e a ligação de aplicação In01_0200 selecionada."><figcaption><p>Exemplo histórico: Application Activity Properties da aplicação LN com o nome de exemplo LN-200 e a ligação de aplicação In01_0200 selecionada. Confirme as definições correspondentes na sua empresa Infor.</p></figcaption></figure>

### BODs

<figure><img src="https://lh7-us.googleusercontent.com/de8OyDF4yMoHaXsxM9weJdm8mKDzL97kFRr00fhoHAxxKXb2BgMcMM2shyxi1S7cBwzSAUy2u8bZV4sJOVqgXt8Mcge6L2CXxbfVGiqXUwKwF6A5mgt4zfGPYltaZuLazOJYu2u7arszJE6IonMOskk" alt="Exemplo histórico: área do fluxo de dados com os nós DocBits-DEV, MappingDeliver, Load Supplier, PurchaseOrder, SalesOrder e AdvancedShip acima da entrada End."><figcaption><p>Exemplo histórico: área do fluxo de dados com os nós DocBits-DEV, MappingDeliver, Load Supplier, PurchaseOrder, SalesOrder e AdvancedShip acima da entrada End. Confirme as definições correspondentes na sua empresa Infor.</p></figcaption></figure>

As configurações seguintes deverão ficar como se segue:

#### Primeiro

<figure><img src="https://lh7-us.googleusercontent.com/rj_qpiML1a2dNxj6ItiRxescymVtD6LHIAum3UPrPERAavhkt81lpjcyAFmn_lmxtqUDVTm_kiZ9f02Lqh9w-SAWmcxvGuxWITVvhv9qg04HaJXGH7VfRiO4Iv1LtDxfKYFyUWPLzCE4L3yP4hcdGnY" alt="Exemplo histórico: lista de documentos do primeiro passo com Sync.CaptureDocument."><figcaption><p>Exemplo histórico: lista de documentos do primeiro passo com Sync.CaptureDocument. Confirme as definições correspondentes na sua empresa Infor.</p></figcaption></figure>

#### Segundo

<figure><img src="https://lh7-us.googleusercontent.com/TCxMS-RhoJcUyBko36Lfpa8D71qk-ZSN-lME7Oq8cfPACVV0Ci7Lnv6y_MF_53U763ZA74xq6icEfgDUwYYJ9UJK0kCiLHQZpJYmc_ywjB32UGrpDnh7AjoHpI5AtWd3yZR3RsMaki1AYenpdG4X9X8" alt="Exemplo histórico: lista de documentos do segundo passo com Load.SupplierInvoice."><figcaption><p>Exemplo histórico: lista de documentos do segundo passo com Load.SupplierInvoice. Confirme as definições correspondentes na sua empresa Infor.</p></figcaption></figure>

#### Terceiro

<figure><img src="https://lh7-us.googleusercontent.com/VPYJyfpO0RZueW46s2Y8W2H-tQFlMfIdP1Sf8qMB8BfTxefgQ5dhsaAxL36R7cdvmKR26Q_epAj9_i6CzUO6C-PHjStEynBDkjtwId4BSuH6-zJklmsr25XcNH2AY7pSwOQ_rbCCixhWcaJg2kHyyYw" alt="Exemplo histórico: lista de documentos do terceiro passo com Process.SupplierInvoice."><figcaption><p>Exemplo histórico: lista de documentos do terceiro passo com Process.SupplierInvoice. Confirme as definições correspondentes na sua empresa Infor.</p></figcaption></figure>

O último ícone deverá estar vazio, porque não transporta nenhum documento nem informação.

Depois de o administrador do Infor ter verificado todos os nós, mapeamentos e subscrições de documentos, utilize o controlo de ativação do fluxo pretendido. A imagem histórica abaixo assinala esse controlo; o nome antigo do fluxo nela visível contém M3 e não deve ser usado como nome nem como destino da sua configuração LN.

<figure><img src="https://lh7-us.googleusercontent.com/WjQeGz_effl_RlkWC4CdJS9Dg_9DpsIz3meKOsa7GbU9RFSrYMw3PpbXFat6cGsA4gvEGS-0D-YFrZj9K2wK3Irap-30mcQ5kr5k4Gy2gm7DLJdYpzJgeBRVInyAYfGmGXu2dCQvmX9ballRbSwyq3o" alt="Exemplo histórico: barra de ferramentas do Document Flow com o controlo de ativação assinalado. O fluxo de exemplo antigo chama-se DocBits-Export-M3; escolha o fluxo LN correto na sua empresa."><figcaption><p>Exemplo histórico: barra de ferramentas do Document Flow com o controlo de ativação assinalado. O fluxo de exemplo antigo chama-se DocBits-Export-M3; escolha o fluxo LN correto na sua empresa. Confirme as definições correspondentes na sua empresa Infor.</p></figcaption></figure>

## Configurar a exportação no DocBits

Na organização DocBits pretendida, abra **Configurações → Exportar**. A lista mostra as configurações de exportação existentes, com as colunas Tipo, Suborganizações, Título, Método De Exportação e Ações. Selecione **Novo** para preparar uma nova configuração.

<figure><img src="../../../.gitbook/assets/dbdc1114-export-list-pt-20261112.png" alt="Lista de exportação atual do DocBits em português, com o botão Novo, as colunas Tipo, Suborganizações, Título, Método De Exportação e Ações e a mensagem de que não existe nenhuma configuração."><figcaption><p>Neste exemplo a lista está vazia e mostra a mensagem «Nenhuma configuração encontrada. Crie sua primeira configuração para começar.» O botão Novo abre o formulário de configuração; nenhuma configuração guardada foi aberta ou alterada. Todos os dados são um exemplo inventado da aplicação 11.27.7.</p></figcaption></figure>

Em **Informações básicas**, introduza um **Título da configuração** e selecione o **Tipo de documento** (no exemplo, uma fatura). Preencha a **Suborganização** apenas se a sua configuração o exigir. Em **Exportar**, escolha **Infor** e, em **Tipo de Infor**, escolha **Infor IDM + LN**.

Em **Configuração de exportação**, forneça os três ficheiros necessários para uma nova configuração LN: **Arquivo da API ION** (`.ionapi`), **Arquivo de mapeamento IDM** (`.properties`) e **Arquivo de mapeamento LN** (`.properties`). Clique em **Clique para fazer o upload** ou arraste o ficheiro para o campo. Obtenha os ficheiros desta empresa e da empresa LN junto do administrador do Infor autorizado. A imagem abaixo deixa deliberadamente todos os campos de upload vazios e não contém dados de acesso.

<figure><img src="../../../.gitbook/assets/dbdc1114-export-ln-pt-20261112.png" alt="Formulário LN atual do DocBits em português, com as secções Informações básicas e Configuração de exportação, Exportar definido como Infor, Tipo de Infor definido como Infor IDM + LN, o Título da configuração e o Tipo de documento vazios e os três campos de upload vazios."><figcaption><p>O formulário LN atual separa os três campos de upload: Arquivo da API ION, Arquivo de mapeamento IDM e Arquivo de mapeamento LN. Neste exemplo não foi selecionado nenhum tipo de documento, não foi carregado nenhum ficheiro e não foi guardada nenhuma configuração. Todos os dados são um exemplo inventado da aplicação 11.27.7.</p></figcaption></figure>

Depois de o administrador confirmar o fluxo ION e os ficheiros, guarde a configuração com **Salvar** e teste uma fatura autorizada fora do ambiente de produção. Verifique o resultado no DocBits, no Infor ION e no LN. Uma configuração guardada, por si só, não prova que o LN recebeu a fatura. Se estiver apenas a consultar os campos disponíveis, feche o formulário com **Cancelar**.

Para saber o papel dos pontos de ligação e dos fluxos de documentos, consulte a [explicação do Infor ION](https://docs.infor.com/ln/10.8/en-us/lnesolh/lnoshybridng/wxa1699288671147.html).
