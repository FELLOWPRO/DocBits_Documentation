# Fornecedores e pedidos de compra do Infor M3

Este exemplo liga os BOD de fornecedores e de pedidos de compra do M3 ao DocBits através do Infor ION. As quinze imagens do Infor apresentadas abaixo são exemplos históricos de um cliente e não constituem uma verificação atual da sua configuração do M3. Peça ao administrador do Infor que confirme os nomes dos BOD, as tabelas de origem, a empresa, a divisão, os nomes das chamadas à API e o ambiente de destino antes de executar uma tarefa. Para esta atualização não foi executada qualquer carga inicial do M3 nem qualquer importação para o DocBits.

O [guia de carga inicial](https://docs.infor.com/m3udi/16.x/en-us/m3beud/appfoundhs/spl1567531742751.html) do Infor explica as definições do EVS006, o verbo e a seleção do EVS007, a submissão e o histórico. Comece com uma seleção limitada; uma execução sem restrições pode gerar muitos eventos.

## **Ponto de ligação**

Crie primeiro o ponto de ligação da API do DocBits, que será utilizado no fluxo de dados.

No InforOS, abra ION Desk → Connect → Connection Points

<figure><img src="https://lh7-us.googleusercontent.com/ySRjNzMXFzwSOYKx9hnlKLPHPuXpmfTvRADBfV6cpT8ajiEUbS4oXpd9InhXG09mHLakhqBTJMH4yQJNG5z9RXmbAjh8YbuGhxnXSeooIH_r3RAGOvJE6Ok67ST_272zFfhB_TTFYg3b-NwFq0CAv2o" alt="Navegação histórica do ION Desk com o grupo Connect expandido e Connection Points realçado."><figcaption><p>Navegação histórica: ION Desk → Connect → Connection Points.</p></figcaption></figure>

Crie um novo ponto de ligação.

<figure><img src="https://lh7-us.googleusercontent.com/ZDv-F3iayFqnsvVLlAE1kr0NNncsvuYtzcE_WQj-0ONoE7McRl-f6_DDH9ErQ0KLspZFFJ43t5EfnPBJjVg25YISMEQ--X4MmK6SVWzB60-Fq6mtwdhiOBwSnL-8vASXsto9iab0dnve6eeG8yuqNoI" alt="Página histórica Connection Points com uma seta verde a apontar para Add."><figcaption><p>Ação histórica Add para criar um ponto de ligação.</p></figcaption></figure>

**Selecione API**

Atribua ao ponto de ligação um nome e uma descrição que indiquem a natureza e o ambiente. No separador Connection, importe a conta de serviço que criou para o ambiente com que está a trabalhar.

<figure><img src="https://lh7-us.googleusercontent.com/UCuGTwKARn3auhYdDDUbQ78Ok3qBNE1KpGEMealfPvgRju4VRLn2AfKaL5tLDcAh00poLHNQU-Q6koBhG5RdxK4CJrrL6Qeb4D52qnhw3aG1LZniuzHRXwOyzGcJvRnQtLGbp6PIseXvWxHlk-AMlz0" alt="Ponto de ligação histórico DocBits-DEV-Demo-Import da API com Connection selecionado e um controlo Import da conta de serviço."><figcaption><p>Separador histórico Connection. Os nomes apresentados referem-se ao ambiente de exemplo; utilize a sua própria conta de serviço.</p></figcaption></figure>

Abra o separador Documents. Tem de adicionar os BOD seguintes ao ponto de ligação; nem todos são necessários para os dados mestre de fornecedores e de pedidos de compra, mas serão úteis quando implementar outras funcionalidades, como a contabilidade automática.

<figure><img src="https://lh7-us.googleusercontent.com/25Hizkx23i1c8-QHSrE7mPAH7zW6ux9iHTcP8_l6EJJy548CvuNPF1R86Fuqx5iYZP9HF-Z4G6hntkaUtlOMetHIzAVZyBM6VIQ-vsvy6P5YBuAj4yscdJe8ySOHwIRQwFpShRiFGC83v467LLBaXq8" alt="Separador histórico Documents com os documentos Acknowledge.SupplierInvoice, Sync.ChartOfAccounts, Sync.PurchaseOrder, Sync.RemitToPartyMaster e Sync.SupplierPartyMaster."><figcaption><p>Lista histórica de documentos recebidos. O BOD de fornecedor apresentado é Sync.RemitToPartyMaster, sem o sufixo Data.</p></figcaption></figure>

Esta configuração histórica utiliza Sync.RemitToPartyMaster, Sync.SupplierPartyMaster e Sync.PurchaseOrder. Confirme os BOD necessários para o seu mapeamento do DocBits; a configuração pode variar consoante o cliente e a funcionalidade.

* Sync.RemitToPartyMaster e Sync.SupplierPartyMaster

A imagem histórica seguinte mostra Sync.SupplierPartyMaster. Configure cada BOD de fornecedor necessário com o nome da chamada à API e a operação de receção confirmados para o seu ambiente; a segunda rota de fornecedor não está representada.

<figure><img src="https://lh7-us.googleusercontent.com/1SeyL73b7K9vxkTzKk-pumRleoY1sx9MVwgEBMZ-oUf6GXG2C7fKIRMbnhWHHhIQhUDBS3oKQidrQIN08FZ_7eKEt1Yp0cRqnsDlv1R5ShdZdNKmaXmU_19DAVtiT3U0m2qm4cBOj9FcnT0eyawfJXk" alt="Separador histórico ION API com Send to API selecionado, o API Call Name Sync.SupplierPartyMaster e a operação POST."><figcaption><p>Rota histórica SupplierPartyMaster. A imagem mostra uma rota de fornecedor; confirme a operação de receção separadamente para cada BOD necessário.</p></figcaption></figure>

* Sync.PurchaseOrder

A imagem histórica seguinte mostra uma operação de receção de pedidos de compra. Confirme o endpoint e o formato do pedido atuais para o seu ambiente.

<figure><img src="https://lh7-us.googleusercontent.com/ljXpQxwepI3u6kcITZfACV9yYL1ZZZtBbWimkXW6aWFTI-yd7Gajrxw2pwxdcF1Xv3KoGDalq72yXvaipjQ-OmbcTzJ0PUUKnmE0pBa5pASEPg0amqKSbU82ZDOKr5alWXynAd53IM2i9HgZ1CsYIB4" alt="Separador histórico ION API com Send to API selecionado para Sync.PurchaseOrder e a operação POST."><figcaption><p>Rota histórica PurchaseOrder. O antigo caminho de proxy do API Gateway é um exemplo e não um endereço universal do DocBits.</p></figcaption></figure>

Depois de configurar estes BOD, guarde o ponto de ligação com o ícone situado à direita do botão de retroceder.

## **Fluxo de dados**

Este fluxo de dados histórico é uma das configurações possíveis; verifique as rotas e a organização recetora no seu próprio cliente.

<figure><img src="https://lh7-us.googleusercontent.com/BtszuCXPwv-WYCGtnd_beU9t0uNntEu6U2iCSstxu1GAziuCfFafQdy2LKZkYw4kbQVfzI5lBYYajOeNwXkn84xy7AXWlCFX4GLo6dukWtfkFPMsXaPga0EkbnrI0bHSKqezXsvYJKymemZYDySIfA8" alt="Fluxo histórico do M3 através de um filtro Yes/No e de uma divisão paralela para quatro nós da API do DocBits, com nós de junção e de fim."><figcaption><p>Fluxo histórico. O ramo No termina antes dos nós da API; o ramo Yes chega aos quatro ambientes de exemplo.</p></figcaption></figure>

Os vários nós da API do DocBits representam ambientes separados neste exemplo. A sua configuração pode ser diferente; verifique que as mensagens de teste não conseguem chegar à produção.

Os quatro ambientes são apresentados apenas como exemplo.

### **M3**

O início do fluxo de dados é a sua aplicação M3

### **Filtro**

A configuração do filtro é a seguinte

<figure><img src="https://lh7-us.googleusercontent.com/-rMMaL3ToAoxqMFXybclIcd61H4S25HI90xnHANGl3J7ldZ374_T2V0q__QSwuNSuXfu829G7kYRCfVslx-l9b1j5LAVKonCQqO3aK2FuWNwmtyvytAF6PaIv8jiEJhhxSwU47eKEo1ozbzyndSW7BY" alt="Painel histórico Filter Properties com Properties selecionado e Name e Description ambos definidos como Division."><figcaption><p>Nome e descrição históricos do filtro. O nome Division, por si só, não determina que registos são filtrados.</p></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/npa9V37wV661zRD-pccafrGqw4hRb-Tk7iZ84UyyjE0gtfAcI1ma6_QWS3iEcBW35trveCG3CnXiZAnFIQyYM278XYJqIuzQh3SUmbAxLCmyTCHkiOhpDJwSfFDJtc8PlcbrmrBdZLACsK3B8sCSyDA" alt="Separador histórico Attributes de Filter Properties com os atributos AccountingEntityID de ChartOfAccounts, PurchaseOrder, RemitToPartyMaster e SupplierPartyMaster."><figcaption><p>Atributos históricos: cada BOD tem um caminho AccountingEntityID. Reveja o caminho de cada documento no seu cliente.</p></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/saiZJD9diyo2JC-XV0vYCboPZJP-87zDH7LIGuBNMNzhL5alDZkShpCARfYd21oroC8eYBfYdckJiONty9IuOc7zHkIIlUWNqoxnPfygEc1R1Tnjt1KPZpSTr7-RLaa5lqS3_2DPj96aV0vLdZk2tzw" alt="Separador histórico Conditions de Filter Properties com ChartOfAccounts, Used Condition definido como Not Filtered e uma expressão de exemplo para AccountingEntityID_3."><figcaption><p>Exemplo histórico de Conditions. Used Condition apresenta Not Filtered apesar de existir uma expressão; verifique a condição selecionada e o seu efeito em vez de assumir que a expressão está ativa.</p></figcaption></figure>

(O identificador da entidade contabilística é, naturalmente, exclusivo da sua organização)

### **API do DocBits**

Aqui adiciona uma aplicação e seleciona a(s) API do DocBits que criou anteriormente

### **Documentos**

Selecione os documentos atribuídos ao nó de origem M3 e aos nós recetores. Confirme que os atributos do filtro e as rotas de receção abrangem todos os documentos necessários.

<figure><img src="https://lh7-us.googleusercontent.com/GLI8kFjQHePMo4ZBWIR1WPNAhkvmtG0BfYADpdlmNqEFMYJclMInVYmKPdaElPLyPR5qtkWOKTnqDFXMDV2pML3igNOFyFj3R9fj2XHRAs6-Rl3KWz4a8-ednk15wyLDJUziAR6ZT4GjuZO2ANw1ymY" alt="Fluxo histórico do M3 com o ícone do documento realçado e um painel Documents com Sync.ChartOfAccounts, Sync.PurchaseOrder, Sync.RemitToPartyMaster e Sync.SupplierPartyMaster."><figcaption><p>Seleção histórica de documentos para o fluxo do M3. Esta é uma lista de documentos BOD, não a configuração de um nó de ficheiro.</p></figcaption></figure>

## **Acionar os BOD no M3**

Abra a aplicação Infor M3

Abra o controlo **Search and Start** do M3, introduza **EVS006** e confirme o programa. Utilize a navegação suportada pelo seu cliente M3.

<figure><img src="https://lh7-us.googleusercontent.com/Vn2WD1-8RuDURsYmzrTARO4mBafwhBUvDImM3z2Nd_hDnVRWjbHgOoplV8QhBC9QtslnWqZyJNIhudvGFGaEl5S-qgloKn0rpwQsF0EuVnrzVplg1urqvSQ9fNa5Qetx8TwLuxZzL3N7wHz9kX4xr_o" alt="Caixa de diálogo histórica Search and Start do M3 com evs006 e um botão OK."><figcaption><p>Pesquisa histórica de programas: introduza EVS006 em Search and Start.</p></figcaption></figure>

No EVS006, defina os substantivos BOD necessários para o seu mapeamento aprovado. O exemplo histórico utiliza SupplierPartyMaster, RemitToPartyMaster e PurchaseOrder. Confirme os nomes das respetivas tabelas do M3 na sua versão antes de criar uma definição de carga inicial.

Substantivo BOD: SupplierPartyMaster

Tabela: CIDMAS

Substantivo BOD: RemitToPartyMaster

Tabela: CIDMAS

Substantivo BOD: PurchaseOrder

Tabela: MPHEAD

Utilize a ação de adição para cada definição aprovada. Verifique a empresa e a divisão antes de continuar.

<figure><img src="https://lh7-us.googleusercontent.com/3y5xAtk4nSc5Eqk-vOJLL59jQHc1w-Fmtn0PIjSiBWTeOo974zg4UjjrK890MjfnsU1a4UtiSqtwcNlHmr6el6GRBd8GrSN_ZlPk3W_IQIVcppHOYwnAzHEgRF22JmeRRkJSHotXvd3k_94_pYjt6Uw" alt="Recorte histórico da barra de ferramentas do EVS006 com Add realçado acima dos campos vazios BOD noun, BOD variant, BOD e Table."><figcaption><p>Ação histórica Add no EVS006. Este recorte não mostra definições de carga inicial preenchidas.</p></figcaption></figure>

Depois de adicionar cada um dos BOD, clique com o botão direito no substantivo BOD e selecione Related → Run

<figure><img src="https://lh7-us.googleusercontent.com/HjkKvk7khjPgpjXmfyTyOLE2vNeB2qt2oN9ShOmrQiYhhvokRlBaZ0rlPtbwWUld54EhUJZLK0OVNGH_eIYzFj22XgFHZccEM9g2nVQ_5BgouHYoMfzfWYQVwluSdcednqrjilSByCdt44ytHgfCNyo" alt="Menu de contexto histórico com Related expandido e Run realçado; History aparece por baixo."><figcaption><p>Ação histórica Related → Run. Utilize History mais tarde para inspecionar o resultado da carga inicial.</p></figcaption></figure>

A ação relacionada **Run** abre o EVS007. Escolha **Sync** apenas quando o fluxo ION recetor o exigir. Inspecione a seleção e os filtros antes da submissão final; passar ao ecrã seguinte não prova que os dados foram entregues.

<figure><img src="https://lh7-us.googleusercontent.com/FoJTP89zGI0FwRTyLjkIKfW75MbCrvcvqD_ka--G1SFdzIhBAp7dq63_WKMIEC-ouCHWA7sRd25rWfWclZJmWd7SGIZLwnSQ4id3nq82hOuFV9-mzMHAtGlhfCKtYwcQnrLyMSsrTmKNyME7lpYSeNA" alt="Ecrã histórico EVS007 Initial Load Job para CIDMAS e SupplierPartyMaster, estado Pending, com o menu do verbo BOD aberto e Sync anotado enquanto Show ainda é apresentado."><figcaption><p>Seleção histórica do verbo no EVS007 antes da execução. A imagem mostra uma tarefa pendente e a opção Sync anotada; não prova que Sync foi selecionado nem que os dados foram importados.</p></figcaption></figure>

Uma notificação de submissão confirma que a tarefa foi pedida. Em **History** do EVS006, verifique o número de registos processados e os erros. Depois, verifique a mensagem e o destino no Infor ION.

## Verificar no DocBits

Na organização do DocBits pretendida, abra **Configurações → Processamento de documentos → Pesquisar Dados Mestres → Dados de entrada do BOD → Fornecedor**. Escolha o campo identificador em **Pesquisar por coluna**, introduza um número ou nome de fornecedor conhecido em **Procurar Texto** e utilize a lupa para pesquisar. A opção **Ações** abre um menu com **Baixar como CSV**, **Atualizar alias** e **Ocultar colunas vazias**. Depois, abra **Ordem de compra** e pesquise um número de pedido de compra conhecido; verifique **Cabeçalho Do Pedido De Compra** se o seu mapeamento separar dados de cabeçalho e de linha. Compare os identificadores e a empresa com a origem M3. Um pedido EVS007 bem-sucedido, por si só, não prova que todos os registos chegaram.

<figure><img src="../../../.gitbook/assets/dbdc-1142-supplier-pt-20261112.png" alt="Vista portuguesa do DocBits em Pesquisar Dados Mestres com o separador Fornecedor, os campos Pesquisar por coluna e Procurar Texto, a opção Ações e dez linhas de fornecedores inventados de SUP-1001 a SUP-1010."><figcaption><p>Vista de fornecedores na versão 11.27.7 da sandbox, com linhas de exemplo inventadas. Pesquise um identificador de teste conhecido e compare-o com o M3 e o ION.</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/dbdc-1142-purchase-order-pt-20261112.png" alt="Vista portuguesa do DocBits em Pesquisar Dados Mestres com os separadores Fornecedor e Ordem de compra, os mesmos campos de pesquisa e dez linhas de pedidos de compra inventados de PO-4500 a PO-4509."><figcaption><p>Vista de pedidos de compra na versão 11.27.7 da sandbox, com linhas de exemplo inventadas. As linhas não provam qualquer importação do M3.</p></figcaption></figure>

As vistas Dev em inglês foram verificadas em 29 de outubro de 2026 sem executar qualquer tarefa do M3, importar qualquer ficheiro ou alterar dados mestre. As duas imagens portuguesas são da versão 11.27.7 da sandbox e mostram linhas de exemplo inventadas em vez de dados mestre reais; mostram onde verificar, não que uma transferência foi concluída. Se faltar um registo esperado, verifique o histórico do EVS006, o encaminhamento no ION, o mapeamento dos BOD e a organização do DocBits antes de voltar a executar.

