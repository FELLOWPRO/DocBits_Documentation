# Modelo de IA

## Visão Geral

A configuração do **Modelo de IA** permite que você defina qual modelo de IA é usado por padrão para a **extração de campo** e a **extração de tabela** durante o processamento de documentos.\
Nesta seção, você pode revisar o custo em tokens para cada modelo e ver qual modelo está atualmente atribuído a cada fornecedor.

## Como Acessar

1.  Navegue até **Configurações** → **Processamento de documentos** → **Classificação e Extração**

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_classification_and_extraction.png)
2.  Role para baixo até a seção **Extração de tabela**

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ai_model_1.png)

## Opções de Modelo de IA

O DocBits oferece três opções de modelo de IA para a extração de campos e tabelas. Elas diferem no equilíbrio entre **precisão de extração**, **velocidade de processamento** e **custo em tokens por documento** — assim você pode adequar a opção ao tipo de documentos que processa. Passe o mouse sobre o ícone de informação ao lado da configuração para ver o custo em tokens da opção atualmente selecionada.

* **Full** – A opção mais completa, com a maior precisão de extração. Ideal para layouts complexos, digitalizações de baixa qualidade ou documentos em que a precisão é o mais importante. Por ser a opção mais potente, também é a mais lenta, com **2 tokens por documento**.
* **Fast** – Uma opção equilibrada que combina boa precisão com processamento mais rápido e custo menor. É a opção padrão recomendada para a maioria dos documentos do dia a dia, com **1 token por documento**.
* **Turbo** – A opção mais rápida e econômica. Mais adequada para grandes volumes de documentos simples, limpos e bem estruturados, em que a velocidade e o baixo custo importam mais do que a precisão máxima, com **1 token por documento**.

| Opção | Ideal para | Precisão | Velocidade | Custo em tokens |
|-------|-----------|----------|------------|-----------------|
| **Full** | Layouts complexos, digitalizações ruins, alta precisão | Máxima | A mais lenta | 2 / documento |
| **Fast** | Documentos do dia a dia (padrão recomendado) | Alta | Rápida | 1 / documento |
| **Turbo** | Grandes volumes de documentos simples e limpos | Boa | A mais rápida | 1 / documento |

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ai_model_2.png)

## Tabela de Atribuição de Modelo de IA

Você também pode configurar **modelos de IA** específicos por fornecedor diretamente na tela de **Validação**, permitindo ajustar a precisão da extração para fornecedores individuais.\
\
Para mais informações, consulte a documentação correspondente [aqui](../../../../end-user-and-partner-section/end-user-section/validation-screen/supplier-specific-ai-model-for-field-and-table-extraction.md).

A tabela de atribuição exibe as configurações do modelo de IA para cada fornecedor e inclui os seguintes detalhes:

* **Supplier ID** – O identificador único do fornecedor
* **AI Model** – O modelo de IA atualmente atribuído ao fornecedor
* **E-Text**: Indica se o recurso E-Text está habilitado
* **Action** – Contém a opção de excluir a entrada

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ai_model_3.png)

### Excluir Entrada – Redefinir Configurações Específicas do Fornecedor

Para redefinir a configuração do modelo de IA de um fornecedor para o padrão:

1.  Clique no ícone da lixeira na coluna **Action** ao lado da entrada do fornecedor.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ai_model_4.png)
2.  Um diálogo de confirmação aparecerá—confirme que você deseja excluir a entrada.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ai_model_5.png)

Uma vez excluído, o fornecedor voltará a usar o **modelo de IA** padrão para a **extração de campo** e a **extração de tabela**.
