# Criar um endpoint da API ION da Infor para as exportações do DocBits

Um administrador da Infor configura o endpoint do API Gateway para o **ambiente e a organização específicos do DocBits**. As imagens antigas nesta página mostravam um tenant histórico da Infor, um exemplo fixo de `api.docbits.com` e um formulário de exportação mais antigo do DocBits. Use a URL de destino, a chave de API e o documento OpenAPI aprovados para o seu ambiente real. Nenhum tenant da Infor foi conectado nem nenhum endpoint foi salvo para esta atualização.

## Antes de começar

Reúna com o administrador da integração a URL de destino da API do DocBits, a chave de API aprovada e o nome do seu cabeçalho, a URL do OpenAPI e os ambientes pretendidos da Infor e do DocBits. Mantenha as chaves e os arquivos `.ionapi` fora de tickets, capturas de tela e do repositório Git. Confirme que um endpoint de teste não pode encaminhar para produção.

## Configurar o Infor API Gateway

1. Em **Available APIs**, crie um pacote de API **Custom or Non-Infor** para o ambiente de destino. Consulte as [instruções da Infor sobre pacotes de API](https://docs.infor.com/inforos/2025.x/en-us/useradminlib_cloud/apigatewayag_cloud/gyy1489512842881.html).
2. Adicione um endpoint ao pacote com a **Target Endpoint URL** aprovada. Selecione o tipo de autenticação exigido por esse endpoint. Para **API Key**, a Infor pede um **Key Name** e um **Key Value**; use o nome especificado no contrato da API do DocBits e a chave emitida para esta organização. Consulte os [campos do endpoint](https://docs.infor.com/inforos/2024.x/en-us/useradminlib_cloud/apigatewayag_cloud/bmg1489588707659.html) da Infor. Não copie uma chave de outro ambiente.
3. Adicione a URL de OpenAPI/Swagger do ambiente nas configurações de **Documentation** do endpoint, seguindo as [instruções da Infor sobre documentação](https://docs.infor.com/inforos/2025.x/en-us/useradminlib_cloud/apigatewayag_cloud/tzr1489597424134.html). Verifique se o endpoint aparece nos [metadados da API](https://docs.infor.com/inforos/2025.x/en-us/useradminlib_cloud/apigatewayag_cloud/tdr1489674063627.html).
4. Junto com o administrador da Infor, verifique a URL de destino, a autenticação, o caminho do proxy e uma chamada segura fora de produção antes de usar o endpoint em um fluxo de documentos ION. Salvar um pacote de API sozinho não prova que um documento foi entregue.

## Configurar a exportação no DocBits

Na organização pretendida do DocBits, abra **Configurações → Exportar** e selecione **Novo**. Os dados das configurações existentes estão cobertos na imagem.

<figure><img src="../../.gitbook/assets/dbdc-40-export-list-pt-20261031.png" alt="Lista atual de exportações em português com Novo, o aviso de execução sequencial e os cabeçalhos da tabela; os dados das configurações estão cobertos."><figcaption><p>Novo abre uma configuração ainda não salva. Os dados das configurações existentes estão cobertos nesta captura nativa atual.</p></figcaption></figure>

Preencha **Título da configuração**, escolha **Tipo de documento** e, se necessário, **Suborganização**. Em **Exportar**, escolha o valor exibido **Infor** correspondente a Infor; em **Tipo de Infor**, selecione **Infor IDM + ION BOD**. O exemplo usa **Fatura**.

Em **Tipo de implantação**, selecione a implantação em nuvem ou local adequada ao ambiente. O formulário apresenta **Arquivo da API ION** (`.ionapi`, obrigatório), **Arquivo de mapeamento IDM** (`.properties`) e **Arquivo de mapeamento de DBO** (`.properties`). Solicite ao administrador os arquivos específicos do tenant. O título, a suborganização e os três campos de envio estão vazios na imagem.

<figure><img src="../../.gitbook/assets/dbdc-40-export-ion-bod-pt-20261031.png" alt="Formulário atual em português Infor IDM + ION BOD com Fatura, opções de implantação e três campos de envio de arquivos vazios."><figcaption><p>Formulário nativo atual Infor IDM + ION BOD: Fatura e a opção de nuvem estão selecionados; título, suborganização e os três envios estão vazios. O formulário foi fechado com Cancelar, sem salvar.</p></figcaption></figure>

Depois que o administrador validar a rota ION, salve a configuração e teste um documento fora de produção. Verifique seu status no DocBits e no Infor ION. Um formulário salvo ou uma entrada nos metadados da API não prova uma exportação bem-sucedida.

A verificação da documentação consultou apenas a lista e o novo formulário. Nenhum arquivo foi enviado, nenhuma configuração foi salva ou ativada e nenhum teste de conexão, login em tenant Infor ou exportação real de documento foi executado.
