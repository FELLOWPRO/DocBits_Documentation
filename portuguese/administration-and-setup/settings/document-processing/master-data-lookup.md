# Pesquisa de dados mestre

{% embed url="https://youtu.be/hn_bkeUMxJg" %}
{% endembed %}

A **Pesquisa de dados mestre** (barra lateral: **Lookup Master Data**) permite visualizar e gerir os dados mestre que o DocBits utiliza para validar os dados extraídos dos documentos relativamente ao seu sistema ERP. É essencial para um PO matching preciso, a validação de fornecedores e o preenchimento automático de campos. Abra-a a partir de **Definições → Processamento de documentos → Lookup Master Data**.

<figure><img src="../../../.gitbook/assets/master_data_lookup_overview.png" alt="Pesquisa de dados mestre"><figcaption><p>Página Pesquisa de dados mestre – fontes de dados e a tabela de dados</p></figcaption></figure>

## Fontes de dados

O painel esquerdo lista quatro categorias de fontes de dados:

| Fonte | Descrição |
|-------|-----------|
| **BOD Input Data** | Dados recebidos através de mensagens Infor BOD (Business Object Document). |
| **ERP API Data** | Dados obtidos diretamente do seu sistema ERP através de uma API. Clique no ícone de engrenagem para configurar a ligação à API. |
| **Imported** | Dados importados manualmente (por exemplo, através de carregamento de CSV). Clique no ícone **+** para adicionar novos dados. |
| **DocBits Master Data** | Dados mestre internos geridos dentro do DocBits. |

## Tabela de dados

Ao selecionar uma fonte de dados, os respetivos dados abrem-se à direita numa tabela pesquisável e ordenável:

* **Separadores** – cada separador é um tipo de dados mestre (por exemplo, Fornecedor, Ordem de compra, Artigo).
* **Pesquisa** – filtre por coluna (**Search by column**) ou pesquise por texto (**Search String**).
* **Ações** – atualizar etiquetas de colunas, ocultar colunas vazias, atualizar aliases ou transferir os dados como CSV.
* **Paginação** – navegue por grandes conjuntos de dados com os controlos de página.

As tabelas de Fornecedor e Ordem de compra incluem colunas como ID do fornecedor, Nome do fornecedor, Endereço, Bank Id, Número da OC, ID do artigo, Descrição, Quantidade, Preço unitário, Montante total, Moeda e Estado, além de quaisquer campos personalizados.

## Definições

Clique em **Settings** (ícone de engrenagem) no canto inferior esquerdo do painel de fontes de dados para abrir as definições de dados mestre.

<figure><img src="../../../.gitbook/assets/master_data_lookup_settings.png" alt="Definições da Pesquisa de dados mestre"><figcaption><p>Definições de Supplier BOD e eliminação de ordens de compra</p></figcaption></figure>

### Supplier BOD

**Allow Multiple Supplier Accounts Sync**

* **Ativado**: um único fornecedor pode ter vários elementos `<FinancialParty>` no BOD (frequentemente devido a vários IBAN ou contas financeiras). Todas as entradas `<FinancialParty>` são extraídas e guardadas na tabela de fornecedores, permitindo armazenar vários atributos financeiros.
* **Desativado**: apenas o último elemento `<FinancialParty>` encontrado para o fornecedor é extraído. Os atributos financeiros anteriores (por exemplo, IBAN adicionais) são ignorados e apenas os dados da última ocorrência são guardados.

### Purchase Order Deletion Assistant

**Delete Purchase Order After** – escolha quando as ordens de compra fechadas devem ser removidas. Após o período selecionado, os registos são eliminados automaticamente.

{% hint style="info" %}
Para saber como carregar dados mestre no DocBits, consulte [Importar dados mestre](../../../infor-integration-and-configuration/importing-customer-master-data/).
{% endhint %}
