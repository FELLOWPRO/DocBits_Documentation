# Fornecedores e pedidos de compra

## **Ponto de ligação**

Crie primeiro o ponto de ligação da API DocBits, que será utilizado no fluxo de dados.

No InforOS, abra ION Desk → Connect → Connection Points.

![Navegação do ION Desk com o grupo Connect expandido e as entradas Data Flows, API Flows, Mappings, Connection Points e File Templates](https://lh7-us.googleusercontent.com/ySRjNzMXFzwSOYKx9hnlKLPHPuXpmfTvRADBfV6cpT8ajiEUbS4oXpd9InhXG09mHLakhqBTJMH4yQJNG5z9RXmbAjh8YbuGhxnXSeooIH\_r3RAGOvJE6Ok67ST\_272zFfhB\_TTFYg3b-NwFq0CAv2o)

Crie um novo ponto de ligação.

![Página Connection Points do ION Desk com o grupo Connect aberto na navegação e o caminho Home e Connection Points](https://lh7-us.googleusercontent.com/ZDv-F3iayFqnsvVLlAE1kr0NNncsvuYtzcE\_WQj-0ONoE7McRl-f6\_DDH9ErQ0KLspZFFJ43t5EfnPBJjVg25YISMEQ--X4MmK6SVWzB60-Fq6mtwdhiOBwSnL-8vASXsto9iab0dnve6eeG8yuqNoI)

**Selecione API**

Atribua ao ponto de ligação um nome e uma descrição que identifiquem a finalidade e o ambiente. No separador Connection, importe a conta de serviço criada para esse ambiente.

![Janela API Connection Point DocBits-DEV-Demo-Import com os separadores Usage, Connection e Documents, o nome DocBits-DEV-Demo-Import, a entrada de autenticação DocBits-DEV-Demo-Import Service Account e o Logical ID infor.api.docbits-dev-demo-import](https://lh7-us.googleusercontent.com/UCuGTwKARn3auhYdDDUbQ78Ok3qBNE1KpGEMealfPvgRju4VRLn2AfKaL5tLDcAh00poLHNQU-Q6koBhG5RdxK4CJrrL6Qeb4D52qnhw3aG1LZniuzHRXwOyzGcJvRnQtLGbp6PIseXvWxHlk-AMlz0)

Abra o separador Documents e adicione os BODs seguintes. Nem todos são necessários para os dados mestre de fornecedores e pedidos de compra, mas serão úteis para funcionalidades como a contabilidade automática.

![Separador Documents do ponto de ligação com os BOD Acknowledge.SupplierInvoice, Sync.ChartOfAccounts, Sync.PurchaseOrder, Sync.RemitToPartyMaster e Sync.SupplierPartyMaster e uma caixa de seleção em cada linha](https://lh7-us.googleusercontent.com/25Hizkx23i1c8-QHSrE7mPAH7zW6ux9iHTcP8\_l6EJJy548CvuNPF1R86Fuqx5iYZP9HF-Z4G6hntkaUtlOMetHIzAVZyBM6VIQ-vsvy6P5YBuAj4yscdJe8ySOHwIRQwFpShRiFGC83v467LLBaXq8)

Por agora, concentre-se nos BODs necessários: Sync.RemitToPartyMasterData, Sync.SupplierPartyMaster e Sync.PurchaseOrder.

* Sync.RemitToPartyMasterData e Sync.SupplierPartyMaster

A configuração destes dois BODs deve ser semelhante à seguinte, alterando API Call Name para cada um.

![Configuração do BOD com os separadores Input Document, ION API, Request Parameters, Request Body e Settings e os campos API Call Name Sync.SupplierPartyMaster, Product DocBits-DEV e a operação POST CustomerApi/DocBits-DEV/prod/import/supplier_bod](https://lh7-us.googleusercontent.com/1SeyL73b7K9vxkTzKk-pumRleoY1sx9MVwgEBMZ-oUf6GXG2C7fKIRMbnhWHHhIQhUDBS3oKQidrQIN08FZ\_7eKEt1Yp0cRqnsDlv1R5ShdZdNKmaXmU\_19DAVtiT3U0m2qm4cBOj9FcnT0eyawfJXk)

* Sync.PurchaseOrder

A configuração deste BOD deve ser semelhante à seguinte.

![Configuração do BOD com os separadores Input Document, ION API, Request Parameters, Request Body e Settings e os campos API Call Name Sync.PurchaseOrder, Product DocBits-DEV e a operação POST CustomerApi/DocBits-DEV/prod/import/purchase_order_bod](https://lh7-us.googleusercontent.com/ljXpQxwepI3u6kcITZfACV9yYL1ZZZtBbWimkXW6aWFTI-yd7Gajrxw2pwxdcF1Xv3KoGDalq72yXvaipjQ-OmbcTzJ0PUUKnmE0pBa5pASEPg0amqKSbU82ZDOKr5alWXynAd53IM2i9HgZ1CsYIB4)

Depois de configurar os BODs, guarde o ponto de ligação no ícone à direita do botão de voltar.

## **Fluxo de dados**

O fluxo de dados será semelhante ao seguinte.

![Fluxo de dados no ION Desk com um nó M3 à esquerda, vários nós DocBits com os nomes DocBits-DEV-P, DocBits-DEV-S e DocBits-DEV-D ao centro, um nó End e uma condição com os ramos Yes e No](https://lh7-us.googleusercontent.com/BtszuCXPwv-WYCGtnd\_beU9t0uNntEu6U2iCSstxu1GAziuCfFafQdy2LKZkYw4kbQVfzI5lBYYajOeNwXkn84xy7AXWlCFX4GLo6dukWtfkFPMsXaPga0EkbnrI0bHSKqezXsvYJKymemZYDySIfA8)

(Existem várias APIs DocBits porque cada ligação representa um ambiente diferente. O fluxo poderá variar consoante o número de ambientes.)

Neste exemplo, utilizamos quatro ambientes separados.

### **M3**

O fluxo de dados começa na sua aplicação M3.

### **Filtro**

A configuração do filtro é a seguinte.

![Painel Filter Properties com os separadores Properties, Attributes e Conditions e os campos Name e Description vazios](https://lh7-us.googleusercontent.com/-rMMaL3ToAoxqMFXybclIcd61H4S25HI90xnHANGl3J7ldZ374\_T2V0q\_\_QSwuNSuXfu829G7kYRCfVslx-l9b1j5LAVKonCQqO3aK2FuWNwmtyvytAF6PaIv8jiEJhhxSwU47eKEo1ozbzyndSW7BY)

![Painel Filter Properties com o separador Attributes aberto e as linhas AccountingEntityID_3 para ChartOfAccounts, AccountingEntityID para PurchaseOrder, AccountingEntityID_1 para RemitToPartyMaster e AccountingEntityID_2 para SupplierPartyMaster, todas do tipo STRING com o caminho DataArea/*/AccountingEntityID](https://lh7-us.googleusercontent.com/npa9V37wV661zRD-pccafrGqw4hRb-Tk7iZ84UyyjE0gtfAcI1ma6\_QWS3iEcBW35trveCG3CnXiZAnFIQyYM278XYJqIuzQh3SUmbAxLCmyTCHkiOhpDJwSfFDJtc8PlcbrmrBdZLACsK3B8sCSyDA)

![Painel Filter Properties com o separador Conditions aberto, o documento ChartOfAccounts, a condição Not Filtered e a linha DIV780AAA com a expressão AccountingEntityID_3 igual a 780_AAA](https://lh7-us.googleusercontent.com/saiZJD9diyo2JC-XV0vYCboPZJP-87zDH7LIGuBNMNzhL5alDZkShpCARfYd21oroC8eYBfYdckJiONty9IuOc7zHkIIlUWNqoxnPfygEc1R1Tnjt1KPZpSTr7-RLaa5lqS3\_2DPj96aV0vLdZk2tzw)

(O identificador da entidade contabilística é específico da sua organização.)

### **API DocBits**

Adicione aqui uma aplicação e selecione as APIs DocBits criadas anteriormente.

### **Ficheiros**

A configuração deve ser semelhante à seguinte.

![Detalhe do fluxo de dados com o nó M3 à esquerda, o nó de condição e os nós DocBits, os marcadores Start e End e o painel Documents com Sync.ChartOfAccounts, Sync.PurchaseOrder, Sync.RemitToPartyMaster e Sync.SupplierPartyMaster](https://lh7-us.googleusercontent.com/GLI8kFjQHePMo4ZBWIR1WPNAhkvmtG0BfYADpdlmNqEFMYJclMInVYmKPdaElPLyPR5qtkWOKTnqDFXMDV2pML3igNOFyFj3R9fj2XHRAs6-Rl3KWz4a8-ednk15wyLDJUziAR6ZT4GjuZO2ANw1ymY)

## **Publicar os BODs no M3**

Abra a aplicação Infor M3.

No menu principal, prima Command + R para abrir a pesquisa de comandos. Introduza evs006 e pesquise.

![Janela Search and Start no Infor M3 com o campo de pesquisa de um comando](https://lh7-us.googleusercontent.com/Vn2WD1-8RuDURsYmzrTARO4mBafwhBUvDImM3z2Nd\_hDnVRWjbHgOoplV8QhBC9QtslnWqZyJNIhudvGFGaEl5S-qgloKn0rpwQsF0EuVnrzVplg1urqvSQ9fNa5Qetx8TwLuxZzL3N7wHz9kX4xr\_o)

Adicione SupplierPartyMaster, RemitToPartyMaster e PurchaseOrder à lista.

Substantivo BOD: SupplierPartyMaster

Tabela: CIDMAS

Substantivo BOD: RemitToPartyMaster

Tabela: CIDMAS

Substantivo BOD: PurchaseOrder

Tabela: MPHEAD

Em cada caso, prima o ícone de adição para acrescentar o elemento à lista.

![Cabeçalho do painel EVS006 com os menus ACTIONS, OPTIONS, RELATED e TOOLS e as colunas BOD noun, BOD variant e BOD description](https://lh7-us.googleusercontent.com/3y5xAtk4nSc5Eqk-vOJLL59jQHc1w-Fmtn0PIjSiBWTeOo974zg4UjjrK890MjfnsU1a4UtiSqtwcNlHmr6el6GRBd8GrSN\_ZlPk3W\_IQIVcppHOYwnAzHEgRF22JmeRRkJSHotXvd3k\_94\_pYjt6Uw)

Depois de adicionar os BODs, clique com o botão direito no respetivo substantivo e selecione Related → Run.

![Menu Related no Infor M3 com as entradas Drill down, Select, Run, Change, History, Copy, Delete, Display e os respetivos atalhos de teclado](https://lh7-us.googleusercontent.com/HjkKvk7khjPgpjXmfyTyOLE2vNeB2qt2oN9ShOmrQiYhhvokRlBaZ0rlPtbwWUld54EhUJZLK0OVNGH\_eIYzFj22XgFHZccEM9g2nVQ\_5BgouHYoMfzfWYQVwluSdcednqrjilSByCdt44ytHgfCNyo)

No menu seguinte, altere o verbo BOD para Sync e prima NEXT para acionar a publicação dos BODs.

![Painel EVS007 Initial Load Job Open com a tabela CIDMAS, o BOD noun SupplierPartyMaster, o número de tarefa 243249962976569068, o estado 1-Pending e o BOD verb definido como Sync](https://lh7-us.googleusercontent.com/FoJTP89zGI0FwRTyLjkIKfW75MbCrvcvqD\_ka--G1SFdzIhBAp7dq63\_WKMIEC-ouCHWA7sRd25rWfWclZJmWd7SGIZLwnSQ4id3nq82hOuFV9-mzMHAtGlhfCKtYwcQnrLyMSsrTmKNyME7lpYSeNA)

Receberá uma notificação a confirmar o acionamento dos BODs.

Se a operação for concluída com êxito, as tabelas de fornecedores e pedidos de compra estarão disponíveis em Configurações → Pesquisa de dados mestre.
