# Atualizar Status do Pedido de Compra do Documento



## Visão Geral

Quando ativado, a coluna **Status do PO** no painel é atualizada automaticamente sempre que o status do pedido de compra é alterado.

## Onde Ativar

1. Acesse: **Configurações** → **Configurações Globais** → **Tipo de Documento**
2.  Selecione o tipo de documento desejado e clique em **Mais Configurações**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fsd3ebb3IETh7wNSA5flh%252Fimage.png%3Falt%3Dmedia%26token%3D6f1d286b-e006-4b23-9866-9ed37bf2bdaa\&width=768\&dpr=4\&quality=100\&sign=b0f0b121\&sv=2)
3.  Na seção **Pedido de Compra**, vá para a opção **Atualizar Status do Pedido de Compra do Documento**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FSsFkQ46Jd4tn0WGqNSjk%252Fimage.png%3Falt%3Dmedia%26token%3D51ee4f2d-76ae-42b4-a748-f0e9d340b329\&width=768\&dpr=4\&quality=100\&sign=e0f4b1af\&sv=2)

## Como Funciona

Quando essa configuração está ativada, a coluna **Status do PO** no painel refletirá automaticamente o status atual do pedido de compra. Por exemplo, se o status do PO for atualizado para _Recebido_ ou _Faturado_, a coluna do painel será atualizada para mostrar esse novo status.

<div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FmWZIOi5pqWyeagCfiXgy%252FStatus%2520on%2520Dashboard.jpg%3Falt%3Dmedia%26token%3D3aad59e7-d249-4f07-afa3-c68429128cec&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=6cde440e&#x26;sv=2" alt="" width="375"></div>

## Configurando

1. **Ative a Configuração** Acesse o local mencionado acima e ative a configuração.
2. **Adicione a Coluna de Status do PO (se não estiver visível)** Se a coluna **Status do PO** não estiver visível no painel:
   *   Acesse: **Configurações Avançadas** → **Definir Colunas da Tabela para Organizações**

       ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fn6GyECCtvUeKLYd6FkEH%252Fimage.png%3Falt%3Dmedia%26token%3Da023deba-748f-4140-bb33-17483c91f2cf\&width=768\&dpr=4\&quality=100\&sign=164eb544\&sv=2)
   * Adicione o campo do tipo de documento pesquisando por **Status do PO**
3. **Configurar configuração de pesquisa**
   *   Configure o campo de Status no cabeçalho do pedido de compra da seguinte forma:

       ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Folrh285NuJO787Udc80C%252Fimage.png%3Falt%3Dmedia%26token%3Def5abe46-fe94-4946-a893-66f7ca21322b\&width=768\&dpr=4\&quality=100\&sign=415e657e\&sv=2)
   * **Observação:** **O pedido de compra precisa estar no Acionador Automático, caso contrário as atualizações de status podem não ser feitas corretamente**
   * Não sabe como **Configurar configuração de pesquisa? Aqui está o** [**guia de configuração de pesquisa**](../../../../../setup/document-types/fuzzy-data-configuration-with-master-data.md)
4. **Verificar** Receba ou fature um PO e verifique no painel se o status foi atualizado corretamente.
