# não encontrado no débito direto

## **Passo 1: Verificar a Configuração do LN**

1. Faça login no **LN CE**.
2. Navegue até o menu **Opções** e selecione **Executar Programa**.
3. No campo de entrada, digite **Parâmetros ACP** e pressione Enter para abrir o programa.
4. Clique na seta ao lado do campo **Conjunto Atual** para expandir as configurações.
5. Vá para a seção **Correspondência**.
   * **Verificar a Configuração de Correspondência Automática:**
     * Se a **Correspondência Automática** estiver definida como **Correspondência com Recibo de Compra**, prossiga para o próximo passo.
     * Se não estiver definida como **Correspondência com Recibo de Compra**, mas você ainda recebeu este erro, entre em contato conosco.

## **Passo 2: Abrir Configurações do DocBits**

Se a **Correspondência Automática** estiver definida como **Correspondência com Recibo de Compra**, siga os seguintes passos no DocBits:

1. Abra o **DocBits** e vá para a seção **Configurações**.
2. Navegue até **Processamento de Documentos**.
3. Selecione **Exportar**.
4. Na seção **Exportar**, clique no ícone dos **três pontos** ao lado da exportação que não está funcionando e selecione **Editar**.
5. No menu **Editar Configurações de Exportação**, clique em **Baixar o arquivo de Mapeamento LN**.

## **Passo 3: Editar o Arquivo de Mapeamento LN**

1. Abra o arquivo de **Mapeamento LN** baixado.
2. Procure pelo campo **IRF\_PackingSlip**.
   * Se o campo **IRF\_PackingSlip** estiver presente e definido como **nada** (vazio), atualize-o para **TF\_packing\_slip**.
   * Se o campo **IRF\_PackingSlip** **não estiver presente**, adicione-o ao arquivo e defina seu valor como **TF\_packing\_slip**.
3. Para o campo **InvoiceReceiptFields**, adicione **PackingSlip** aos valores.

Deve ficar como o seguinte:

<figure><img src="../../../../.gitbook/assets/PackingSlip.png" alt=""><figcaption></figcaption></figure>

## **Passo 4: Adicionar o Arquivo Atualizado de Volta ao DocBits**

1. Volte para a seção **Exportar** no DocBits onde você baixou anteriormente o arquivo de **Mapeamento LN**.
2. Faça o upload do arquivo de **Mapeamento LN** editado com as novas atualizações.

## Se você ainda encontrar o **Erro ao exportar documento para LN** com o código de status **500**, entre em contato conosco
