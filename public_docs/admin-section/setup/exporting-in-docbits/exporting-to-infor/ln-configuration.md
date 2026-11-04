# Configuração LN

## Pré-requisitos

Você criou:

* Um Ponto de Extremidade da API ION
* Um Arquivo de API ION
* Um Arquivo de Mapeamento BOD
* Um Arquivo de Mapeamento IDM

## Importar Arquivos de Mapeamento

Antes de configurar o fluxo de dados, você precisa importar os arquivos de mapeamento para o InforOS

No ION Desk → Conectar e abrir Mapeamentos

![](https://lh7-us.googleusercontent.com/fAUUcBUSxIWqLjYEHH78O2Mfq0P4d4D42OgCNFPdpUQTM5ZHu_BcKz9DmWe0AlHe3--ff7z9mfYTrt7oAkf2uknBwkV2VWayEpiJ_aAIxcJil5LNiep4U6KZr3_tBfs1RRwXoW749q3FUxurXy_pT_k)

Clique no ícone de Importar

![](https://lh7-us.googleusercontent.com/d_KYA9LgiiW1A95CH9hwU1AC1u5x25T4ET-4sAqpZkVOexHc4WcbwPXUaKt3O9fR3Btvv-NEGbCWwnnb8SfomnnO22M8YTIqWdvan-SkbG0cu1MWkjwOn_Vd_b6rJaQng8A92JTa5YKBms4RuIvwmb0)

* Aqui você precisa selecionar os vários arquivos de mapeamento que você precisará, incluindo: SyncCaptDoc_SyncSuppInv, SyncSupplierInvoice_LoadSupplierInvoice e LoadSupplierInvoice_ProcessSupplierInvoice.
* Após importar todos os arquivos de mapeamento, certifique-se de aprovar cada um deles clicando no ícone de marca de seleção dentro de cada um dos quadrados no painel de Mapeamento.

## DocBits para LN

O próximo passo é configurar o Fluxo de Dados no ION Desk, navegue até a aplicação ION Desk e selecione Fluxo de Dados → + ADICIONAR → Fluxo de Documento como abaixo

![](https://lh7-us.googleusercontent.com/rjPVR1EFKw_gZI1Ztg9Aqt4pFw10rii7WU-yddLIz22a_Fn3s1HSYDRmQVvgZtX_85nb2ipNqJ1JU49NIE8a57TIur7jqoMuKFKlb-RrfnRFxiA1TefzofKPJ32fzIdDWI8PmnD-aDw4qhQj4e0dd9I)

Você verá então esta página, aqui é onde você irá construir o fluxo de informações de DocBits para M3

![](https://lh7-us.googleusercontent.com/9C7BaoiHWRaav0ytCbYkxEYG12f-64qyagsl8H2eq5TXUySRE1s3x_-lVRbK6tpTxvbRYKvwyWO_6ASSQ6Rn62LQR9ZvMRpRXq9UymZLS0I8IZ-hOzX58iYtTruqSo5WdgIXwEPjMlb1dnuFuhN8IS8)

Um fluxo de dados LN será semelhante ao mostrado abaixo (existem vários caminhos devido a cada caminho individual ser destinado a um tipo de documento específico, para esta explicação vamos focar no fluxo de dados de fatura).

![](https://lh7-us.googleusercontent.com/gltDE9JxeGb7Ufg9Ldl-JIJ95zfWHnQtyOqys2QKCiTlIn_PdAyBLFYmTVCh9c-TxF5xNQR3G8Hmn4EXK94t6MJ-1WzlZg1Zl7HNoxfR56zC8dT1skmxLTj7rtnSl0JTQJD_3myQY4Qcd9motySYh9U)

Todas as partes da cadeia são arrastadas e soltas da seção superior

Na cadeia, DocBits e LN são ambas Aplicações, enquanto entre elas existem mapeamentos que convertem os dados em uma forma que pode ser entendida pela próxima seção do fluxo de dados e "mapeiam" as informações para que vão para onde são necessárias ou destinadas.

![](https://lh7-us.googleusercontent.com/Gwk0C0gsnMSlgEwRx0_1GDMJEu8Z1TAhKo8gxHN8GxFFKGgb257a684Hj0eNSLTIK5v8F7yzJ1hIHrC_3I9RLY0S-u3ZDhmkD6iJbYAvtCAeFPWHBVLOqyCH7FKsl2SKAfXL-AdtNowqdol9PzS4qJM)

### Aplicação DocBits

Dê a ela o nome apropriado, como "DocBits", em seguida, selecione o sinal de adição e procure pelo ponto de conexão que você criou anteriormente, como DocBits_Export ou similar e clique nele.

Para criar este ponto de conexão, vá para ION Desk → Conectar → Pontos de Conexão

![](https://lh7-us.googleusercontent.com/1SZJN-GW7BP-fvUHZ-tCJ4xNXx0ABRP3J9eMzF3BTKIY54J-pK4bYy4fOVHCaI6A2sdrYekWJsY9ky8dXz36l_FwwzzEnO1IjxNkMqlV-Y4UvyFIei73Z9C19m9bzTr3gCL3IpTUqiV280id1vJE530)

Clique em "+ Adicionar"

![](https://lh7-us.googleusercontent.com/ZJ1212Gwdk-b2-LVbEd2ZDzc_AqaEEYtIN0fC6d6P4EaWdTKj6nOzGDbA5sxdBtMcTrWopfDmd7GTahbwkDpj3uvmMYgvEUQa6qmi58NFGvtcgAtIwYr952Yu7Lcj802iHtQ_vj_-XPdegP1P0ySdos)

Selecione "IMS via API Gateway" e preencha as seguintes informações

![](https://lh7-us.googleusercontent.com/H4YCH-324EzrxKkrbRs0SFTsHch5eK74gXleSpfI03uJ5frIEFjwofu7p6bsYO1lS7sVqamWDZMXrGfEgewdROyhTYLkn7MuCgwb7oQxOLJoH3NsnMsqTOgT3WxlihUkJdNy-WTai5kPz8ZjdtTDQ9I)

O ID do Cliente da API ION está no Arquivo de API ION que você criou em Como Criar um Arquivo de API ION sob o valor "ci".

Mude para a aba de documento e adicione o BOD Sync.CaptureDocument ao ponto de conexão DocBits como abaixo.

![](https://lh7-us.googleusercontent.com/Wy2BIr1z_RqU-yMkXo6vOu64QC6c66OdHOxdI6PPy0yJv1jIAJF0OYITULxTFoPUK93SK3jvNm67tcxqjiEBIk0Wbu1Q1s-mSIUuPjJorcYyXY7vjsHOnoutn6tE8r6yE_333uCWuKvKiVoo99FrXVg)

Em seguida, salve o ponto de conexão pressionando o ícone de disco no canto superior esquerdo.

Volte para a seção de Fluxo de Dados do ION Desk para acessar seu fluxo de dados. Sua aplicação DocBits deve se parecer com o que é mostrado abaixo.

![](https://lh7-us.googleusercontent.com/cDWHmRP85YNLu7JRzq4CSezncTgP2ZOkEfZSqXK9JEq4bSwsddU7VKg8leoxaJ5zeFAbDzXrNkztmeWDIXbHwjxfUa_IpATDDwykv-OlZ2zaOVGHVqRZZpVLJ5Cq5Qla1pZk5sBV39I98lUfGao65Mw)
### Mapeamento 1

O primeiro nó de mapeamento deve ser assim

![](https://lh7-us.googleusercontent.com/9tlIun_ipbTp15aMX3xN2DGlDjAZ1oI4AFWXwbP7yoFLeQNqcw_L3Z1djaqcbxP1tsp1R-nq6ZJqEzsoKe1-SmLrJNmYrJ4HJircLEwMxfmif-p2T8nqbuuxHLLLzQJ6E6tNG6MzghOpoEAt41ea2GY)

### Mapeamento 2

O segundo nó de mapeamento deve ser assim

![](https://lh7-us.googleusercontent.com/ZDYzTAfm3MHnEIKHa2tDl7NPbjzxv8jH-KL8O0pRhi1JYtqiiVz0-GQv5N4roVWi1STopQkFV9YHbEXdyzwYxK2Oq6mUv6tuqKDp-2bc-aPVgEXdEBd2hmW-6j6JRhEympyw9yUTrCDQRKlDQ41C5Ao)

### Aplicação LN

Deve haver um ponto de conexão LN ou similar (para a empresa LN apropriada) criado no INFOR, então, assim como a Aplicação DocBits, você o seleciona clicando no sinal “+” e deve parecer assim

![](https://lh7-us.googleusercontent.com/mRXL11f68EtQHHjl40QmCisy7S1aUezqCzufPTZWgYHhWLK2Yw0UY82O_dgbAhBChFHHYUMBDSWWb-PEKyohJWOp5gvufat431ezpA2cIHMtry7XEDxhnNzPB68uSMkFAXhX1x4GyiH6Cxp-USxDnHE)

### BODs

![](https://lh7-us.googleusercontent.com/de8OyDF4yMoHaXsxM9weJdm8mKDzL97kFRr00fhoHAxxKXb2BgMcMM2shyxi1S7cBwzSAUy2u8bZV4sJOVqgXt8Mcge6L2CXxbfVGiqXUwKwF6A5mgt4zfGPYltaZuLazOJYu2u7arszJE6IonMOskk)

As seguintes configurações devem parecer assim:

#### Primeiro

![](https://lh7-us.googleusercontent.com/rj_qpiML1a2dNxj6ItiRxescymVtD6LHIAum3UPrPERAavhkt81lpjcyAFmn_lmxtqUDVTm_kiZ9f02Lqh9w-SAWmcxvGuxWITVvhv9qg04HaJXGH7VfRiO4Iv1LtDxfKYFyUWPLzCE4L3yP4hcdGnY)

#### Segundo

![](https://lh7-us.googleusercontent.com/TCxMS-RhoJcUyBko36Lfpa8D71qk-ZSN-lME7Oq8cfPACVV0Ci7Lnv6y_MF_53U763ZA74xq6icEfgDUwYYJ9UJK0kCiLHQZpJYmc_ywjB32UGrpDnh7AjoHpI5AtWd3yZR3RsMaki1AYenpdG4X9X8)

#### Terceiro

![](https://lh7-us.googleusercontent.com/VPYJyfpO0RZueW46s2Y8W2H-tQFlMfIdP1Sf8qMB8BfTxefgQ5dhsaAxL36R7cdvmKR26Q_epAj9_i6CzUO6C-PHjStEynBDkjtwId4BSuH6-zJklmsr25XcNH2AY7pSwOQ_rbCCixhWcaJg2kHyyYw)

O último ícone deve estar vazio, pois não está carregando nenhum documento ou informação.

Depois de adicionar todos os nós necessários ao fluxo de dados, pressione este botão para ativar o fluxo de dados

![](https://lh7-us.googleusercontent.com/WjQeGz_effl_RlkWC4CdJS9Dg_9DpsIz3meKOsa7GbU9RFSrYMw3PpbXFat6cGsA4gvEGS-0D-YFrZj9K2wK3Irap-30mcQ5kr5k4Gy2gm7DLJdYpzJgeBRVInyAYfGmGXu2dCQvmX9ballRbSwyq3o)
