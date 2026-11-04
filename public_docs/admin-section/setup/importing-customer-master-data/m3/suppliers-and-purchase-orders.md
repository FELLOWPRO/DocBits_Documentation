# Fornecedores e Ordens de Compra

## **Ponto de Conexão**

Você precisará criar o ponto de conexão da API DocBits para criar o fluxo de dados posteriormente.

No InforOS, acesse ION Desk → Conectar → Pontos de Conexão

![](https://lh7-us.googleusercontent.com/ySRjNzMXFzwSOYKx9hnlKLPHPuXpmfTvRADBfV6cpT8ajiEUbS4oXpd9InhXG09mHLakhqBTJMH4yQJNG5z9RXmbAjh8YbuGhxnXSeooIH\_r3RAGOvJE6Ok67ST\_272zFfhB\_TTFYg3b-NwFq0CAv2o)

Uma vez aqui, você precisará criar um novo ponto de conexão.

![](https://lh7-us.googleusercontent.com/ZDv-F3iayFqnsvVLlAE1kr0NNncsvuYtzcE\_WQj-0ONoE7McRl-f6\_DDH9ErQ0KLspZFFJ43t5EfnPBJjVg25YISMEQ--X4MmK6SVWzB60-Fq6mtwdhiOBwSnL-8vASXsto9iab0dnve6eeG8yuqNoI)

**Selecionar API**

Dê ao ponto de conexão um nome e descrição que descrevam sua natureza e seu ambiente. Na aba Conexão, importe a conta de serviço que você criou para o ambiente com o qual está trabalhando.

![](https://lh7-us.googleusercontent.com/UCuGTwKARn3auhYdDDUbQ78Ok3qBNE1KpGEMealfPvgRju4VRLn2AfKaL5tLDcAh00poLHNQU-Q6koBhG5RdxK4CJrrL6Qeb4D52qnhw3aG1LZniuzHRXwOyzGcJvRnQtLGbp6PIseXvWxHlk-AMlz0)

Em seguida, mude para a aba Documentos. Você precisará adicionar os seguintes BODs ao ponto de conexão, nem todos são necessários para os dados mestres de fornecedores e ordens de compra, mas serão úteis quando outras funcionalidades, como Contabilidade Automática, precisarem ser implementadas.

![](https://lh7-us.googleusercontent.com/25Hizkx23i1c8-QHSrE7mPAH7zW6ux9iHTcP8\_l6EJJy548CvuNPF1R86Fuqx5iYZP9HF-Z4G6hntkaUtlOMetHIzAVZyBM6VIQ-vsvy6P5YBuAj4yscdJe8ySOHwIRQwFpShRiFGC83v467LLBaXq8)

Por enquanto, vamos nos concentrar apenas nos BODs necessários, que são: Sync.RemitToPartyMasterData, Sync.SupplierPartyMaster e Sync.PurchaseOrder.

* Sync.RemitToPartyMasterData e Sync.SupplierPartyMaster

A configuração para esses dois BODs deve ser semelhante ao seguinte (Nome da Chamada da API alterando para cada um)

![](https://lh7-us.googleusercontent.com/1SeyL73b7K9vxkTzKk-pumRleoY1sx9MVwgEBMZ-oUf6GXG2C7fKIRMbnhWHHhIQhUDBS3oKQidrQIN08FZ\_7eKEt1Yp0cRqnsDlv1R5ShdZdNKmaXmU\_19DAVtiT3U0m2qm4cBOj9FcnT0eyawfJXk)

* Sync.PurchaseOrder

A configuração para este BOD deve ser semelhante ao seguinte

![](https://lh7-us.googleusercontent.com/ljXpQxwepI3u6kcITZfACV9yYL1ZZZtBbWimkXW6aWFTI-yd7Gajrxw2pwxdcF1Xv3KoGDalq72yXvaipjQ-OmbcTzJ0PUUKnmE0pBa5pASEPg0amqKSbU82ZDOKr5alWXynAd53IM2i9HgZ1CsYIB4)

Depois que esses BODs estiverem configurados, você pode salvar o ponto de conexão pressionando o ícone localizado à direita do botão voltar.

## **Fluxo de Dados**

O fluxo de dados será semelhante ao seguinte

![](https://lh7-us.googleusercontent.com/BtszuCXPwv-WYCGtnd\_beU9t0uNntEu6U2iCSstxu1GAziuCfFafQdy2LKZkYw4kbQVfzI5lBYYajOeNwXkn84xy7AXWlCFX4GLo6dukWtfkFPMsXaPga0EkbnrI0bHSKqezXsvYJKymemZYDySIfA8)

(O motivo de múltiplas APIs DocBits é devido a cada conexão representar um ambiente diferente, o que significa que, dependendo da quantidade de ambientes que você tem, seu fluxo de dados pode diferir ligeiramente)

Para fins desta explicação, usaremos o exemplo de ter quatro ambientes separados.

### **M3**

O início do fluxo de dados consiste em sua aplicação M3

### **Filtro**

A configuração do filtro é a seguinte

![](https://lh7-us.googleusercontent.com/-rMMaL3ToAoxqMFXybclIcd61H4S25HI90xnHANGl3J7ldZ374\_T2V0q\_\_QSwuNSuXfu829G7kYRCfVslx-l9b1j5LAVKonCQqO3aK2FuWNwmtyvytAF6PaIv8jiEJhhxSwU47eKEo1ozbzyndSW7BY)

![](https://lh7-us.googleusercontent.com/npa9V37wV661zRD-pccafrGqw4hRb-Tk7iZ84UyyjE0gtfAcI1ma6\_QWS3iEcBW35trveCG3CnXiZAnFIQyYM278XYJqIuzQh3SUmbAxLCmyTCHkiOhpDJwSfFDJtc8PlcbrmrBdZLACsK3B8sCSyDA)

![](https://lh7-us.googleusercontent.com/saiZJD9diyo2JC-XV0vYCboPZJP-87zDH7LIGuBNMNzhL5alDZkShpCARfYd21oroC8eYBfYdckJiONty9IuOc7zHkIIlUWNqoxnPfygEc1R1Tnjt1KPZpSTr7-RLaa5lqS3\_2DPj96aV0vLdZk2tzw)

(O ID da entidade contábil, é claro, sendo único para sua organização)

### **API DocBits**

Aqui você adicionará um aplicativo e selecionará a(s) API(s) DocBits que você criou anteriormente
### **Arquivos**

A configuração deve parecer da seguinte forma

![](https://lh7-us.googleusercontent.com/GLI8kFjQHePMo4ZBWIR1WPNAhkvmtG0BfYADpdlmNqEFMYJclMInVYmKPdaElPLyPR5qtkWOKTnqDFXMDV2pML3igNOFyFj3R9fj2XHRAs6-Rl3KWz4a8-ednk15wyLDJUziAR6ZT4GjuZO2ANw1ymY)

## **Acionamento do M3 BOD**

Acesse a aplicação Infor M3

Uma vez no menu principal, digite Command + R para abrir a caixa de pesquisa do prompt de comando. Em seguida, digite evs006 e pesquise.

![](https://lh7-us.googleusercontent.com/Vn2WD1-8RuDURsYmzrTARO4mBafwhBUvDImM3z2Nd\_hDnVRWjbHgOoplV8QhBC9QtslnWqZyJNIhudvGFGaEl5S-qgloKn0rpwQsF0EuVnrzVplg1urqvSQ9fNa5Qetx8TwLuxZzL3N7wHz9kX4xr\_o)

Uma vez nesta página, você precisará adicionar o SupplierPartyMaster, RemitToPartyMaster e PurchaseOrder à lista.

Substantivo BOD: SupplierPartyMaster

Tabela: CIDMAS

Substantivo BOD: RemitToPartyMaster

Tabela: CIDMAS

Substantivo BOD: PurchaseOrder

Tabela: MPHEAD

Para cada caso, você precisará pressionar o ícone de adição para adicioná-los à lista.

![](https://lh7-us.googleusercontent.com/3y5xAtk4nSc5Eqk-vOJLL59jQHc1w-Fmtn0PIjSiBWTeOo974zg4UjjrK890MjfnsU1a4UtiSqtwcNlHmr6el6GRBd8GrSN\_ZlPk3W\_IQIVcppHOYwnAzHEgRF22JmeRRkJSHotXvd3k\_94\_pYjt6Uw)

Depois de adicionar cada um dos BODs, clique com o botão direito no substantivo BOD do BOD e selecione Relacionado → Executar

![](https://lh7-us.googleusercontent.com/HjkKvk7khjPgpjXmfyTyOLE2vNeB2qt2oN9ShOmrQiYhhvokRlBaZ0rlPtbwWUld54EhUJZLK0OVNGH\_eIYzFj22XgFHZccEM9g2nVQ\_5BgouHYoMfzfWYQVwluSdcednqrjilSByCdt44ytHgfCNyo)

Você será levado ao menu a seguir, onde precisará alterar o verbo BOD para Sincronizar e depois pressionar PRÓXIMO para acionar os BODs.

![](https://lh7-us.googleusercontent.com/FoJTP89zGI0FwRTyLjkIKfW75MbCrvcvqD\_ka--G1SFdzIhBAp7dq63\_WKMIEC-ouCHWA7sRd25rWfWclZJmWd7SGIZLwnSQ4id3nq82hOuFV9-mzMHAtGlhfCKtYwcQnrLyMSsrTmKNyME7lpYSeNA)

Depois de acionar os BODs, você receberá uma notificação confirmando isso.

Se feito com sucesso, as tabelas de Fornecedor e Ordem de Compra devem agora estar disponíveis em Configurações → Consulta de Dados Mestres.
