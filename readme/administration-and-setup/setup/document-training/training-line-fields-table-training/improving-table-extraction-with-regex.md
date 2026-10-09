# Estruturação e Melhoria da Extração de Tabelas no DocBits

Uma vez que uma tabela é extraída e o mapeamento inicial das colunas é concluído, você pode aprimorar a qualidade e estrutura dos dados usando várias ferramentas integradas. Este guia o conduz por:

* Agrupamento de linhas
* Seleção manual de linhas
* Mapeamento de colunas
* Refinamento de cabeçalho usando regex

Essas ferramentas são especialmente úteis ao lidar com layouts de documentos complexos ou inconsistentes.

## 1. Agrupamento de Linhas

Documentos como faturas ou confirmações de pedidos frequentemente contêm entradas de tabela onde uma coluna (por exemplo, uma descrição) abrange várias linhas, enquanto outras colunas (por exemplo, quantidade ou preço) usam apenas uma linha.

Considere este exemplo de fatura alemã — a coluna "Bezeichnung" (descrição) abrange várias linhas:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-improving-table-extraction-with-regex-multiline-doc-pt-20261009.png" alt="Tabela de uma fatura alemã em que a descrição (Bezeichnung) de cada item abrange várias linhas."><figcaption><p>Uma coluna de descrição que abrange várias linhas.</p></figcaption></figure>

Inicialmente, o DocBits extrai cada linha separadamente:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-improving-table-extraction-with-regex-initial-extraction-pt-20261009.png" alt="Tabela extraída na visualização Extração de Tabela em que cada linha de texto da descrição se tornou uma linha própria."><figcaption><p>O DocBits extrai cada linha separadamente no início.</p></figcaption></figure>

Em seguida, você pode **agrupar linhas com base em uma coluna**, como "Posição". Isso mescla linhas relacionadas em uma entrada única e estruturada:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-improving-table-extraction-with-regex-grouped-result-pt-20261009.png" alt="Tabela extraída em que as linhas de descrição agrupadas por Posição formam uma entrada por posição."><figcaption><p>Após o agrupamento por Posição, as linhas relacionadas formam uma única entrada.</p></figcaption></figure>

Quantas sublinhas são mescladas em uma entrada e como o agrupamento se comporta você define nas [Configurações Avançadas](advanced-settings.md) em **Mínimo de Linhas Agrupadas** e **Agrupamento Reverso**.

## 2. Seleção Manual de Linhas

Em alguns casos, o texto em um documento está distribuído por várias colunas em uma única linha, tornando difícil a atribuição automática.

Aqui está um exemplo em que a linha "PRAEF" se sobrepõe a **Bezeichnung**, **Menge**, **ME** e **Preis in EUR**:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-improving-table-extraction-with-regex-row-misalignment-pt-20261009.png" alt="Tabela de uma fatura com uma linha PRAEF cujo texto atravessa várias colunas."><figcaption><p>Uma linha PRAEF que não se alinha à estrutura de colunas.</p></figcaption></figure>

### Como Atribuir Valores Manualmente:

1.  **Ativar o Modo de Treinamento**

    <figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-improving-table-extraction-with-regex-training-mode-pt-20261009.png" alt="Tela de Extração de Tabela com o Modo de treinamento ativado."><figcaption><p>Modo de treinamento ativado.</p></figcaption></figure>
2.  **Ativar o Modo de Edição de Linha**

    <figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-improving-table-extraction-with-regex-row-edit-mode-pt-20261009.png" alt="Tela de Extração de Tabela com o modo Edição de dados de linha: Ativado e a dica de ferramenta correspondente visível."><figcaption><p>Modo de edição de linha ativado.</p></figcaption></figure>
3.  **Selecionar e Mapear Texto**\
    Clique na parte correta do texto e atribua-a a um cabeçalho de coluna **azul**.

    <figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-improving-table-extraction-with-regex-editable-columns-pt-20261009.png" alt="Tabela extraída no modo de edição de linha com os cabeçalhos de coluna azuis, ainda vazios, que podem ser atribuídos manualmente."><figcaption><p>Os cabeçalhos de coluna azuis podem ser preenchidos manualmente.</p></figcaption></figure>

> Nota: As colunas de cor violeta já estão mapeadas pelo sistema e não podem ser editadas manualmente.

Esse trabalho acontece no **modo de edição de dados de linha** (**Edição de dados de linha: Ativado**). O que você pode fazer nele e quando usá-lo em vez do **Modo de Treinamento** está descrito em [Training Line Fields/Table Training](README.md).

## 3. Mapeamento de Colunas

O mapeamento de colunas vincula seus dados extraídos aos cabeçalhos de coluna esperados, garantindo consistência e capacidade de exportação.

Para mapear ou remapear uma coluna:

1. Clique no cabeçalho da coluna na visualização de extração.
2. Escolha a coluna de destino correta no menu suspenso.

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-improving-table-extraction-with-regex-mapping-dropdown-pt-20261009.png" alt="Tabela extraída com o menu suspenso do cabeçalho de coluna aberto, listando as colunas de destino Descrição, Número do item, Valor líquido, Posição, Quantidade, Montante total, Unidade e Preço unitário."><figcaption><p>Escolha a coluna de destino no menu suspenso do cabeçalho.</p></figcaption></figure>

Você pode ajustar o mapeamento quantas vezes forem necessárias.

Veja [Definindo Tabelas e Colunas](defining-tables-and-columns.md) para mais informações sobre a criação de tabelas e colunas.

## 4. Extrair de Acima / Abaixo

Alguns documentos são estruturados de forma que os valores relevantes da tabela não aparecem na mesma linha que outros dados. Nestes casos, o DocBits permite que você controle **de onde os dados devem ser extraídos**:

* **Extrair de Acima**: Use isso quando o valor para a linha atual aparece **na linha acima**.
* **Extrair de Abaixo**: Use isso quando o valor aparece **na linha abaixo** da linha atual.

**Onde Encontrar**

1. Entre no **Modo de Treinamento**.
2. Clique nos três pontos (⋯) em um cabeçalho de coluna.
3. Sob a opção **"Extrair De"**, escolha `Acima` ou `Abaixo` dependendo do layout do documento.

## 5. Formato de Quantidade

Algumas colunas, como **Quantidade** ou **Preço Unitário**, contêm valores numéricos ou de data que podem seguir convenções de formatação diferentes, dependendo da origem ou localidade do documento. O DocBits permite que você especifique o formato que esses valores devem seguir para garantir uma extração e interpretação precisas.

**Opções de Formato de Quantidade:**

* Defina o formato numérico ou de data esperado para a coluna, como EUA (MM/DD/AAAA, decimal com ponto), Polônia (DD.MM.AAAA, decimal com vírgula), Alemanha e outros.
* Isso ajuda o DocBits a analisar e padronizar corretamente os valores, mesmo que o documento use um formato regional diferente.

**Onde Encontrar**

1. Entre no **Modo de Treinamento**.
2. Clique nos três pontos (⋯) no cabeçalho de uma coluna suportada (por exemplo, Quantidade, Preço Unitário).
3. Sob a opção **Formato de Quantidade**, selecione o formato desejado que corresponda à localidade do seu documento.

## 6. Melhorando a Extração de Tabelas com Regex

## **O que Faz**

Essa funcionalidade permite que você defina um regex para cada cabeçalho de tabela, melhorando a precisão da extração e garantindo resultados corretos.

## **Como Usar**

1. Abra um documento do fornecedor para o qual deseja definir um regex.
2.  Navegue até a visualização de **Extração de Tabela**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FDdlNrO6hG6jnEeWU9DuZ%252Fimage.png%3Falt%3Dmedia%26token%3Dca11a537-27a4-4b00-b3e7-f77540c28c2b\&width=768\&dpr=4\&quality=100\&sign=fd47355a\&sv=2)
3. Ative o **Modo de Treinamento**.
4.  Selecione o cabeçalho da tabela que deseja refinar e escolha **Regex**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fes6PsB9sHHXp0CNRj6YF%252Fimage.png%3Falt%3Dmedia%26token%3D6e31e4db-fd2f-487c-ac19-f1d6add81ad1\&width=768\&dpr=4\&quality=100\&sign=32264560\&sv=2)
5.  Uma janela pop-up aparecerá onde você pode inserir e definir seu regex.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FWB7hjuuyVVAewRqrnhYj%252FiScreen%2520Shoter%2520-%2520Google%2520Chrome%2520-%2520250303135020.jpg%3Falt%3Dmedia%26token%3D6a31253d-18d7-4d8f-a00e-acd89a744127\&width=768\&dpr=4\&quality=100\&sign=d8d2d94a\&sv=2)
6.  Clique em **Validar** para verificar o regex, depois em **Salvar Alterações** para aplicá-lo.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FC4R2o2W10ct1o0oesTLZ%252FiScreen%2520Shoter%2520-%2520Google%2520Chrome%2520-%2520250303135153.jpg%3Falt%3Dmedia%26token%3D43e53a05-53fe-4503-ba51-55c85910bd82\&width=768\&dpr=4\&quality=100\&sign=9ec6eb7b\&sv=2)
7. **Salve a regra e confirme** para aplicar as alterações.

Para salvar ou excluir regras treinadas de forma permanente, veja [Salvar e Excluir Regras](save-and-delete-rules.md).

## Quando Usar Cada Recurso

Use essas ferramentas para aumentar a precisão da extração e reduzir o trabalho manual:

* **Agrupamento**: Quando uma descrição ou qualquer coluna abrange várias linhas e precisa ser combinada para clareza.
* **Seleção Manual de Linhas**: Quando as linhas não estão estruturadas de forma limpa e partes do conteúdo caem nas colunas erradas.
* **Mapeamento de Colunas**: Quando os nomes das colunas detectados automaticamente não correspondem à sua estrutura ou precisam de refinamento.
* **Regras de Regex**: Quando os cabeçalhos de tabela variam ligeiramente entre documentos do mesmo fornecedor ou o OCR introduz inconsistências.

Guias relacionados nesta área:

* [Configurações Avançadas](advanced-settings.md) – agrupamento, linhas de cabeçalho e tratamento de linhas extras.
* [Definindo Tabelas e Colunas](defining-tables-and-columns.md) – criar tabelas e colunas para o treinamento.
* [Salvar e Excluir Regras](save-and-delete-rules.md) – aplicar ou remover permanentemente um layout treinado.
