# Configuração M3

## Pré-requisitos

Você criou:

* Um Ponto de Extremidade da API ION
* Um Arquivo de API ION
* Um Arquivo de Mapeamento BOD
* Um Arquivo de Mapeamento IDM

## Importar Arquivos de Mapeamento

Antes de configurar o fluxo de dados, você precisa importar os arquivos de mapeamento para o InforOS.

No ION Desk → Conectar e abrir Mapeamentos

![](https://lh7-us.googleusercontent.com/EV8z6b_W9tjTgML0j3qJAYHCTYLd4N5yLrArdIECftYpMOCRTRJ_a7eADEzljFM4XHxMUJ6Nx9Z6EN3Hmzote5F0HrM5zd4p1BS0NYicUWDnkhQFX-_3MGbblEYi6x2a1K25SclYYttgW3cWQbOjvfQ)

Clique no ícone de Importar

![](https://lh7-us.googleusercontent.com/agBHtjNitneogoZsSG1791QAARbvesv9eSriAkw0HL9Fy372Ty6SmQG1sKJjOYZCuE0SnGT3agHAFRJYjgGNxJrN1CMJj9L-fSPhNmXxN78iDKqrrdgEVYFHxsNwy9XLiUFpBCQ1wnWlwyeFH08DsWI)

A partir daqui, você precisa selecionar os vários arquivos de mapeamento que você precisará, que incluem: SyncCaptDoc_SyncSuppInv, SyncSupplierInvoice_LoadSupplierInvoice e LoadSupplierInvoice_ProcessSupplierInvoice.

Depois de importar todos os arquivos de mapeamento, certifique-se de aprovar cada um deles clicando no ícone de marca de seleção dentro de cada um dos seus quadrados no painel de Mapeamento.

## DocBits para M3

O próximo passo é configurar o Fluxo de Dados no ION Desk, navegue até a aplicação ION Desk e selecione Fluxo de Dados → + ADICIONAR → Fluxo de Documento como abaixo

![](https://lh7-us.googleusercontent.com/Kkro7w2LPfnwf-JPMmPI2DzrSRNEi_F9aWW02KDtBvAZz_R7j9DZ71Nqw3ETPSQqDuxBzJ1TU8Uuzz5jU9rOO_tvDBf9abVF-FDSxln_pjr-HMRdYBnGMwgcM6hg-pC2B7FgdBkXibivMB4PptvZ6fk)

Você verá então esta página, aqui é onde você irá construir o fluxo de informações do DocBits para o M3

![](https://lh7-us.googleusercontent.com/K0B1lC_KLO5RZqGqAltp6JnZZ1sfZG4wg-i_nxZCnLjML33yvViRUHOInK3iHYbzbV4I0uqDY8JpsZMxssD8bbJy24A1zKr9PfQEyqVxewx_L87RCIwzn5MDRjMqgx4X42vkKthbyz--5DDe1H0rvHQ)

Um fluxo de dados M3 terá uma aparência semelhante ao que é mostrado abaixo (existem 3 aplicações e APIs DocBits devido a serem usadas para 3 ambientes separados).

![](https://lh7-us.googleusercontent.com/6Oy_UBzYNml-7_sayDEKhqYF92yDzlUNzmGLQSWZOfDT-avvfg3oNUnv_DtXNSP0XF43D-zgIizIuTrCXl6ockLU2uQLYFJna72fzL5BP-T89xjF4oWz2eAz9w0hsoVieyTpgSw_Prvj--89Kc4Kqoo)

Todas as partes da cadeia são arrastadas e soltas da seção superior

Na cadeia, DocBits e M3 são ambas Aplicações, enquanto entre eles existem mapeamentos que convertem os dados em uma forma que pode ser entendida pela próxima seção do trem e "mapeiam" as informações para que elas vão para onde são necessárias ou destinadas.

![](https://lh7-us.googleusercontent.com/1kjgKNmIQ-NbM_JukcPsj7qmyiMB9b693ixg6Dh1kOlZ6NKgBXViYwn0MNUBHt0WKKWf_1gpRvxgqjIaqpqcy-SyXoYjhJLt3m_bv7wbVADzqHRsx8TYXWyIQO82X-Ixfl5b7iI7nxTRkw06sX3xsBM)

### Aplicação DocBits

Dê a ela o nome apropriado, como "DocBits", em seguida, selecione o sinal de adição e procure pelo ponto de conexão que você criou anteriormente, como DocBits_Export ou similar e clique nele.

Para criar este ponto de conexão, vá para ION Desk → Conectar → Pontos de Conexão

![](https://lh7-us.googleusercontent.com/8qsMIUKMrgmcYqqJPL2zF4GVeHuvSHvn8Z7dfonRuvKFPcXmN4hx2PIrXko4lvW7ayD7s2VRFOMvWkQSxfAH5tTuhg0XhzYmSzlsgnowWRw8GmQC2y5BjcS9X2MjDzLSutgoHg2VN59kCYRunMSxkIY)

Clique em "+ Adicionar"

![](https://lh7-us.googleusercontent.com/-3-3TzgEQppYmX64-clxjp1JBjNz9fsA2FDPqirgNF0wL8DsDJACzUBuSw5wBL2k9JanqvMzAG352CWafOdtjhMfZalJnBFVSjaWA1AszhCjKtCsTvLUUqq1WwMfF-PqL-u7LRo4TPbj4fP2_j48240)

Selecione "IMS via API Gateway" e preencha as seguintes informações

![](https://lh7-us.googleusercontent.com/wImUEi9mXiQjW5O6mp7_IrKk4CTaHFs903DJ6TXqUEcjGq45TnUWdusFTGH1jzpBPP_TC7rokyjrkYWmh3emSKBQs05qYbO80TO87De0C5OveVURykQMCLFRRYakEMoFHpoeXzxH5QIbKJdjxujeY98)

O ID do Cliente da API ION está no Arquivo de API ION que você criou em Como Criar um Arquivo de API ION, isso pode ser encontrado pelo valor "ci".

Mude para a aba de documento e adicione o BOD Sync.CaptureDocument ao ponto de conexão do DocBits como abaixo.

![](https://lh7-us.googleusercontent.com/ga1q0Uwdi2GNwuiz22NvDtCzGL0krSkBPLsEVxE-mtoMV7CtEU8TPO0PhF40oB9NB9iv7DCJi9niLnsKjpqarWJsgGRdc1W0pFl9rTDm7i2_BSLj3JOrzR7iclPdqOdpztgCxWZG2Teg1gWljaMUq2E)

Em seguida, salve o ponto de conexão pressionando o ícone de disco no canto superior esquerdo.

Volte para a seção de Fluxo de Dados do ION Desk para acessar seu fluxo de dados. Sua aplicação DocBits deve se parecer com o que é mostrado abaixo.

![](https://lh7-us.googleusercontent.com/fBzKL6RU0XvGpn1cKFZIyAp2amKonBWc8ilbAq5u_r867xywWWAD7EjP-g-wjlwUsrG4Wz0lS6Ujdnu8P3vc8Q3FbtbRR4qSBmbSLoICfX-aHITMDdHp07bESefC9TuUUUQiHGb1j00HNtB_7A3iDFs)
### Mapeamento 1

O primeiro nó de mapeamento deve ser assim

![](https://lh7-us.googleusercontent.com/F9AcE4V-s9vs-0kRz8BcCtdHUUQoaooyK3GqOj8pAQWuvIguoUO-tJx7WBEW6\_GmzwNsJp8VUYezGCiLPXvPhEynac3FPh\_NJOvqs1SXtMIUsF5\_HjWmcvY3VC-eZsjG0ZE8HmsKsFhocadr96drSbY)

### Mapeamento 2

O segundo nó de mapeamento deve ser assim

![](https://lh7-us.googleusercontent.com/8M\_V2BtkOGyqV-828ct5c2QvSs5n5\_RtLjlH717kspZwlgtfjbz6tpOJCCXDelruBenMjxsJPqncQ5hUw2bQkM3ya7\_WrVyEBz3UnaU-C9oVOWB8nNtXA20RBYgO3EBMon2TfgpefY0lSPBzF9NoTeU)

### Mapeamento 3

O terceiro nó de mapeamento deve ser assim

![](https://lh7-us.googleusercontent.com/x9QUHTgQrNaeKnTeMIUflkWjcBr2c3LgsYe2BZBjv01hXiEkvsLtU0GzYt5KppcE12ZqxWeBJ1kbLOC6qA3yKHhujCZt3sFpDNE5yERkHHMJJEjFl0jJE90nQ-iXeMLbR-Bk6G0NIL8AqG3U48Seiuc)

### Aplicação M3

Deve haver um ponto de conexão M3 ou similar criado no INFOR, assim como a Aplicação DocBits, você o seleciona clicando no sinal “+” e deve parecer assim

![](https://lh7-us.googleusercontent.com/JTXIN5QxidvFJyjegxSw8kA7yVfHfuypxi5yX21CsSlGtOVgykc52U2r0077-cKqNhc0B4zSSZotlipFesmLo371kho3wUSRPzmwEir-stbxyZV1PwCDXkq6qJMm4PNXt\_wGarDMixGIU0tu-eAqV5Y)

### API DocBits

Você primeiro precisa criar esta API como um ponto de conexão que é feito por:

ION Desk → Conectar → Pontos de Conexão

![](https://lh7-us.googleusercontent.com/VOXW6LixmcKjHW0CTOO5L8fK6r-4k3jqk0AnoR6DEVoGgJMbx65hS3yKSgMWItypdz4Ha82T-bKCN0aMv34gif-b0Aw7zpDFPBK9G-K6x9\_csrM9xyKcpmWam15tKqO1\_rwKtMsJ2CSoWqdpLxCD5tA)

Clique em “+ Adicionar” e selecione API

![](https://lh7-us.googleusercontent.com/c1RAUNoA3YBhvf6FLJ\_L3ouyZwHK-3bBRU83eL3oAQXjG6SjWEO9O-gDKPItPm8AI\_YhadaCZU-GxY-qUXNuQMiRiKUhBYUtJ8kOFVg\_YYpzJDSoJ68NYSaEtHBSyyfnq0VbHUdWY1e8lBQ0j\_G5xvI)

As informações que você preencher devem parecer com o seguinte

![](https://lh7-us.googleusercontent.com/h2KU6pKeKl9wX8oyul0KmbL\_kg-iPQJpBqbf29l64ED2e-Z4tNj8-m4hBN\_4SSiNPf2TrE92TD4H0-0AZ0eWxMFmDV22IdPlU9NO4XlQF9k0Swg0X3Sm1HMsSPvWi7Q1HUr8uy8j3aDRheFxZqZ2Gbc)

Mude para a aba de documento e adicione a seguinte configuração

![](https://docbits.com/wp-content/uploads/2023/09/DocBits\_Exp\_M3\_api\_docs1-1024x279.png)

**Acknowledge.SupplierInvoice**

A configuração para este BOD é a seguinte

![](https://docbits.com/wp-content/uploads/2023/09/DocBits\_Exp\_M3\_ack\_11.png)

Certifique-se de ter selecionado a opção “Enviar para API” no menu acima.

![](https://docbits.com/wp-content/uploads/2023/09/DocBits\_Exp\_M3\_ack\_2-1024x338.png)

Por fim, garanta que você também altere o corpo da solicitação para ficar assim.

![](https://docbits.com/wp-content/uploads/2023/09/DocBits\_Exp\_M3\_ack\_3-1024x260.png)

Repita este processo para o restante dos BODs, cada configuração é mostrada abaixo.

**Sync.PurchaseOrder**

A configuração para este BOD é a seguinte

![](https://docbits.com/wp-content/uploads/2023/09/DocBits\_Exp\_M3\_po\_1.png)![](https://docbits.com/wp-content/uploads/2023/09/DocBits\_Exp\_M3\_po\_2-1024x359.png)![](https://docbits.com/wp-content/uploads/2023/09/DocBits\_Exp\_M3\_po\_3-1024x297.png)

**Sync.RemitToPartyMaster**

A configuração para este BOD é a seguinte

![](https://docbits.com/wp-content/uploads/2023/09/DocBits\_Exp\_M3\_remit\_1-1.png)![](https://docbits.com/wp-content/uploads/2023/09/DocBits\_Exp\_M3\_remit\_2-1024x351.png)![](https://docbits.com/wp-content/uploads/2023/09/DocBits\_Exp\_M3\_remit\_3-1024x299.png)

**Sync.SupplierPartyMaster**

A configuração para este BOD é a seguinte

![](https://docbits.com/wp-content/uploads/2023/09/DocBits\_Exp\_M3\_sup\_1.png)![](https://docbits.com/wp-content/uploads/2023/09/DocBits\_Exp\_M3\_sup\_2.png)![](https://docbits.com/wp-content/uploads/2023/09/DocBits\_Exp\_M3\_sup\_3-1024x295.png)

### BODs

![](https://lh7-us.googleusercontent.com/zaDSnm844wXqyefN58Y1DvuJOnMaoOrYQ\_12Z5ZSng8-TPy38Th2ZPdAD6hyIYCOvBKGPDSvGpTmtBPq4K5IwyGtsKyMvk-CKOuY-hzD-RL7UrsG39qLN7m3\_IDcDS66KeIQF5e70OWlHO1cbVvQUXM)

As seguintes configurações devem parecer assim:
#### Primeiro

![](https://lh7-us.googleusercontent.com/5gLpbQEYYW90dVLkSc5V60LeToMe2wcOcHHtwTdIdT0o0Gktu8T_7i7zfNikjgETM3QmzAsJAknlEGeB0W0YFLLi56g2PKPwyr2zPcHaKdu8XJWHgaC1u4--_CHNYfd1wQ__3kZpv1_PwyZty3JEyak)

#### Segundo

![](https://lh7-us.googleusercontent.com/xbWTcP8hYA72Ijt7_IV6l-9jKeSalbRPvTn7aNVcnWYMQcD2RDjM-EzKpBKjSIKF_-r8BaxmmCo9uz6-E-vC9flKb4toU3SH24EPLgbXc-VcfJeDdJKglf5P6WV6XYZg0cZVWAoyvS8qgtuR6ZqJYlI)

#### Terceiro

![](https://lh7-us.googleusercontent.com/F8wVWXuHkLLW2kuu_7Dxe9LhyYdm04tl__Sp6FjeTyk_JFUzhCIUhVlKS_cq3I3FP_h2ksV4zEJHFC_KXK6sSZ5iz5yhTFZcPnH1HS_RvZb2Nr-UXYQ1H316UMoj6eRv6wMn3wHX842B5WVfPHVnJ74)

#### Quarto

![](https://lh7-us.googleusercontent.com/myhi9y2sCvS5ZFkIJa5ysLbu7p0X6CYqbiuJ3sQ5-O-2QWlfAseunjwhXK0kakmAofplm0zmh_H1Np7bA559w0-jdurQUsZwYF9CyKYSKSeGnQaIit0HQ5iN-3Xv8CIC-5nk6mMj3JTDS97SlzbsOFE)

#### Quinto

![](https://lh7-us.googleusercontent.com/c-5iaUhhx0swH-mQfXE5Mdwe4J0skGt7mst4kJdOpjL3Uat329TZmKM5Af-lGQWmcmBht-ib_aUj4dVG7GaUAHHULjly3jxsR8MJNnLDcu5eZB268Vy-dXPxHmkVB8dMZTRhU5SUB59AREurJlW-K6o)

O último ícone deve estar vazio, pois não contém nenhum documento ou informação.

Depois de adicionar todos os nós necessários ao fluxo de dados, pressione este botão para ativar o fluxo de dados (após salvar o fluxo de dados pressionando o ícone do disco rígido).

![](https://lh7-us.googleusercontent.com/WIecHktG7e5dbVScLbR8hUcZUdCEWXBW4xWDEuq0IqTMmguA_Ih_oRymvpk6CzowWFG5TTSCPIH-68ICnPSOPxeZksc-n4bmpvuH8dvHuHFU1DlppGRno3PKjCSJiK12p9bNlo_9cN2t9Ps3nbqF3xE)
