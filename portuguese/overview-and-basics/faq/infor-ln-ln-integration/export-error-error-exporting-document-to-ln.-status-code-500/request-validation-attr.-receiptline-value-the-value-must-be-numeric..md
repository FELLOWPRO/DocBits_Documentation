# o valor deve ser numérico.

## **Passo 1: Investigar o Pedido de Compra**

**1. Verificar o Pedido de Compra no Painel**

* Se o status do documento for **Erro de Exportação**:
  1. Localize o documento no painel.
  2. Clique nele e em seguida selecione o botão de **Validação de Campos** para voltar para a tela de validação de campos.
* Se o status do documento for **Pronto para Validação**:
  1. Clique no documento para prosseguir diretamente para a tela de **Validação de Campos**.
* Se o documento estiver no status de **Aguardando Aprovação**:
  1. Navegue até a **Tela de Aprovação**.
  2. Ao lado dos **Itens de Linha da Fatura**, localize a **Tabela de Pedido de Compra**.
  3. Vá para 3. Verifique o passo do Número de Entrega.

**2. Verificar o Pedido de Compra**

1. Na tela de **Validação de Campos**, certifique-se de que o Pedido de Compra correto está selecionado.
2. Uma vez confirmado o Pedido de Compra correto, clique no Pedido de Compra ao lado da tabela extraída, para abrir a visualização da **Tabela de Pedido de Compra**.

**3. Verificar o Número de Entrega**

* Na Tabela de Pedido de Compra, procure a coluna **Número de Entrega**:
  * **Se um Número de Entrega estiver presente**, prossiga para a **Tela de Aprovação** e verifique novamente se está presente, quando presente vá para o **Passo 3**.
  * **Se nenhum Número de Entrega estiver presente**, siga o **Passo 2** para resolver esse problema.

## Passo 2: Verificar o Pedido de Compra no LN

Antes de enviar o Pedido de Compra para o DocBits, verifique se o **Número de Entrega** está corretamente atribuído no **LN**. Verifique os detalhes do **Pedido de Compra** no **LN** para garantir que esteja completo e preciso. Se o **Número de Entrega** estiver ausente ou incorreto, isso pode ser a causa do erro de exportação.

Se o **Pedido de Compra** parecer correto e contiver os detalhes necessários, você pode prosseguir para o próximo passo.

## **Passo 3: Abrir as Configurações do DocBits**

1. Abra o **DocBits** e vá para a seção de **Configurações**.
2. Navegue até **Processamento de Documentos**.
3. Selecione **Exportação**.
4. Na seção de **Exportação**, clique no ícone dos **três pontos** ao lado da exportação que não está funcionando e selecione **Editar**.
5. No menu de **Editar Configurações de Exportação**, clique em **Baixar o arquivo de Mapeamento LN**.

## **Passo 3: Editar o Arquivo de Mapeamento LN**

1. Abra o arquivo de **Mapeamento LN** baixado.
2. Procure pelo campo **IRF\_ReceiptLine**.
   * Se o campo **IRF\_ReceiptLine** estiver presente e definido como **nada** (vazio), atualize-o para **TF\_delivery\_line**.
   * Se o campo **IRF\_ReceiptLine** **não estiver presente**, adicione-o ao arquivo e defina seu valor como **TF\_delivery\_line**.
3. Para o campo **Campos de Recebimento de Fatura**, adicione **ReceiptLine** aos valores.

Deve parecer com o seguinte:

<figure><img src="../../../../.gitbook/assets/ReceiptLine.png" alt="" width="563"><figcaption></figcaption></figure>

## **Passo 4: Adicionar o Arquivo Atualizado de Volta ao DocBits**

1. Volte para a seção de **Exportação** no DocBits onde você baixou anteriormente o arquivo de **Mapeamento LN**.
2. Faça o upload do arquivo de **Mapeamento LN** editado com as novas atualizações.

## Passo 5: Tentar a Exportação

Após confirmar que o **Pedido de Compra** possui um **Número de Entrega** e garantir que o **arquivo de exportação esteja correto**, siga estas etapas para tentar a exportação novamente:

1. **Retornar ao Painel:**
   * Volte ao painel e encontre o documento com o erro de exportação.
2. **Tentar o Processo de Exportação Novamente:**
   * Clique no documento com o erro de exportação.
   * Se o **Pedido de Compra** tiver um **Número de Entrega** válido e o **arquivo de exportação** estiver correto, prossiga para tentar a exportação novamente.
3. **Verificar o Resultado da Exportação:**
   * Após tentar novamente, verifique o processo de exportação novamente para ver se o problema foi resolvido e o documento não aparece mais como um erro de exportação.
   * Se a exportação for bem-sucedida, o problema deve estar resolvido.
4. **Investigação Adicional (se o problema persistir):**
   * Se o problema persistir após tentar novamente a exportação, entre em contato com o suporte para investigação adicional sobre possíveis problemas de configuração ou do sistema.
