# Configurações de dados mestre

## Visão geral

Na seção **Configurações de dados mestre** das **Campos** Configurações para um **Tipo de documento** específico, você pode visualizar e configurar mapeamentos de dados mestres para campos usados na validação de campos, usando dados de [**Consulta de Dados Mestres**](../../../document-processing/master-data-lookup.md).

Esses mapeamentos definem como os dados mestres são aplicados a campos individuais durante a validação. Esta página fornece um guia detalhado sobre como configurar e gerenciar esses mapeamentos.

## **Acessando** Configurações de dados mestre **Configurações**

Para acessar as **Configurações de dados mestre** Configurações:

1.  Vá para **Configurações → Configurações globais → Tipos de documentos**

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_document_types.png)
2.  Selecione o **Tipo de documento** desejado e clique em **Campos**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_document_types_fields.png)
3.  Clique em **Configurações de dados mestre**

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_1.png)

## Pesquisar Dados Mestres

Na seção **Pesquisar Dados Mestres**, você pode criar configurações de pesquisa a partir dos seus dados mestres para usar como mapeamentos de campo durante a validação de campos.

### Entradas padrão

Na seção **Pesquisar Dados Mestres**, determinadas entradas padrão são fornecidas pelo **DocBits**. Essas entradas:

* Não podem ser editadas ou excluídas
* Podem ser desativadas se não forem necessárias

As entradas padrão são claramente marcadas com uma **Default** tag para fácil identificação.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_2.png)

### **Criar configuração de pesquisa**

Para criar uma nova configuração de pesquisa para dados mestre:

1. Navegue até a seção **Pesquisar Dados Mestres**.
2.  Clique em **Criar configuração de pesquisa** no canto superior direito.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_3.png)
3. Configure as seguintes opções:
   * **Nome da pesquisa**\
     O nome da configuração de pesquisa.
   * **Nome do conjunto de dados de pesquisa**\
     Selecione o conjunto de dados que deve ser usado para esta configuração de pesquisa.
   * **Manipulador de conflitos**\
     Um conflito significa que a pesquisa encontrou mais de um registo. Esta definição decide o que acontece nesse caso:
     * **Best Score** – Usa a entrada que corresponde ao maior número de campos. Nunca deixa o campo vazio, por isso pode escolher o registo errado.
     * **Return None** – Deixa o campo vazio, para que um utilizador escolha o registo correto.
     * **Return First** – Usa o primeiro valor correspondente.
   *   **Tipo de contexto**

       Especifica onde no documento a configuração de pesquisa será aplicada. Escolha entre:

       **HEADER**

       A pesquisa é usada na validação de campos. Configure o seguinte:

       * **Combinar tudo**\
         Quando habilitado, um registo tem de corresponder a **todos** os campos usados. Quando desativado (predefinição), basta corresponder **um** campo, o que devolve uma lista mais longa.

       ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_4.png)

       \
       **LINE**

       A pesquisa é usada dentro de uma tabela do documento. Configure o seguinte:

       * **Detalhe do contexto**\
         Selecione a tabela específica à qual a pesquisa deve ser aplicada.
       * **Combinar tudo**\
         Quando habilitado, um registo tem de corresponder a **todos** os campos usados. Quando desativado (predefinição), basta corresponder **um** campo, o que devolve uma lista mais longa.

       ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_5.png)
{% hint style="info" %}
**Combinar tudo** e o **Manipulador de conflitos** funcionam em conjunto e decidem se um fornecedor é reconhecido automaticamente. A página de configuração explica ambos com exemplos:

{% content-ref url="../../../../setup/document-types/fuzzy-data-configuration-with-master-data.md" %}
[fuzzy-data-configuration-with-master-data](../../../../setup/document-types/fuzzy-data-configuration-with-master-data.md)
{% endcontent-ref %}
{% endhint %}

4.  Clique em **Salvar** para criar a configuração de pesquisa.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_6.png)

### Ações em uma configuração de pesquisa existente

Para gerenciar uma configuração de pesquisa existente, clique nos três pontos no canto superior direito da configuração que deseja modificar.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_7.png)

As seguintes ações estão disponíveis:

* **Ativar / Desativar**\
  Alterna o status da configuração de pesquisa.
  * Configurações com status Ativo são marcadas com uma **Ativo** tag.
  * Configurações com status Inativo são marcadas com uma **Inativo** tag.
*   **Duplicado**\
    Após inserir um nome e clicar em **Feito**, uma cópia da configuração de pesquisa selecionada é criada.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_8.png)
* **Editar/Visualizar**\
  Permite modificar a configuração de pesquisa selecionada.\
  Após fazer as alterações, clique em **Salvar** para aplicá-las.\
  <mark style="color:red;">**Observação**</mark>: As configurações de pesquisa padrão só podem ser visualizadas, não editadas. A opção **Editar** será substituída por **Visualizar**.
*   **Excluir**\
    Exclui permanentemente a configuração de pesquisa selecionada após confirmação.\
    <mark style="color:red;">**Observação**</mark>: Apenas configurações sem a **Default** tag podem ser excluídas.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_9.png)

### Criar novo Campo

Para adicionar um novo Campo à sua configuração de pesquisa:

1. Abra a configuração de pesquisa desejada.
2.  Clique em **Criar** no canto superior direito.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_10.png)
3. Configure as opções necessárias.
   * **Campo de pesquisa**\
     O Campo que será pesquisado dentro do conjunto de dados de pesquisa selecionado.
   * **Campo de Validação**\
     O Campo que será exibido durante a validação de campos.
   * **Campo Pai** (opcional)\
     Este Campo é usado para validar a correção do valor no **Campo de Validação**, garantindo que corresponda à entrada pai correspondente no conjunto de dados de pesquisa.
   * **Operador de pesquisa** (opcional)\
     Escolha como o **DocBits** pesquisa correspondências no conjunto de dados de pesquisa:
     * **Smart** – _(Default)_ Ignora espaços e pontuação e procura o termo em **qualquer lugar** do campo. Por isso "Meier" também encontra "Meier Bau GmbH".
     * **Contém** – Procura entradas que contenham o termo exato em qualquer lugar do Campo.
     * **Termina com** – Procura entradas que terminem com o termo especificado.
     * **exato** – Procura uma correspondência exata de todo o valor.
     * **Começa com** – Procura entradas que comecem com o termo especificado.
   * **Gatilho automático** (opcional)\
     Quando habilitado, o DocBits preencherá automaticamente todos os campos na configuração de pesquisa assim que este Campo for preenchido.
   *   **Pesquisável** (opcional)\
       Quando habilitado, os usuários podem pesquisar manualmente dados mestres durante a validação de campos **e** o campo participa na pesquisa automática. Deixe desmarcado se o campo não deve influenciar o resultado automático.

       ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_12.png)

       ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_13.png)
4.  Clique em **Salvar** para criar o novo Campo.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_11.png)

### Ações no Campo existente

Para gerenciar um Campo existente, clique nos três pontos na coluna **Ações** ao lado do Campo que deseja modificar.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_14.png)

As seguintes ações estão disponíveis:

* **Editar/Visualizar**\
  Permite modificar o Campo selecionado.\
  Após fazer suas alterações, clique em **Salvar** para aplicá-las.\
  <mark style="color:red;">**Observação**</mark>: Campos padrão só podem ser visualizados, não editados. Nesses casos, a opção **Editar** aparecerá como **Visualizar**.
*   **Excluir**\
    Exclui permanentemente o Campo selecionado após confirmação.\
    <mark style="color:red;">**Observação**</mark>: Apenas Campos sem a **Default** tag podem ser excluídos.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_9.png)

## Dados Mestres LOV

A seção **Dados Mestres LOV** permite criar configurações de lista suspensa usando valores dos seus dados mestres. Essas listas podem ser independentes ou dependentes de outras listas, permitindo filtragem dinâmica e seleções em cascata durante a validação de campos.

### Criar configuração de pesquisa Lov

Uma configuração de pesquisa lov define como as opções da lista suspensa são obtidas de uma tabela de dados mestres e como esses valores são exibidos e preenchidos nos campos do documento.

**Para criar uma nova configuração de pesquisa Lov:**

1. Navegue até a seção **Dados Mestres LOV**.
2.  Clique em **Criar configuração de pesquisa Lov** no canto superior direito.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_15.png)
3. Configure as seguintes opções:
   * **Pesquisar nome de amor**\
     O nome da configuração de pesquisa lov.
   * **Nome do conjunto de dados de pesquisa Lov**\
     Selecione a tabela de dados mestres que deve ser usada para esta configuração de pesquisa lov.
   *   **Tipo de contexto**\
       Especifica onde no documento a configuração de pesquisa lov será aplicada:

       **HEADER**

       A configuração de pesquisa lov é usada na validação de campos. Configure o seguinte:

       * **Campo de rótulo de pesquisa**\
         Selecione a coluna cujo valor será exibido na lista suspensa.
       * **Campo de valor de pesquisa**\
         Selecione a coluna cujo valor será armazenado internamente e usado para filtragem quando uma seleção for feita. Este valor não é exibido para o usuário.
       * **Fora do campo**\
         Define o Campo na validação de campos que receberá o rótulo selecionado na lista suspensa.

       ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_16.png)

       \
       **LINE**

       A configuração de pesquisa lov é usada dentro de uma tabela do documento. Configure o seguinte:

       * **Detalhe do contexto**\
         Selecione a tabela específica onde esta configuração de pesquisa lov deve estar ativa.
       * **Campo de rótulo de pesquisa**\
         A coluna cujo valor será exibido na lista suspensa.
       * **Campo de valor de pesquisa**\
         Selecione a coluna cujo valor será armazenado internamente e usado para filtragem quando uma seleção for feita. Este valor não é exibido para o usuário.
       * **Fora do campo**\
         Especifica o Campo de destino na tabela onde o rótulo selecionado será preenchido.

       ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_17.png)
4.  Clique em **Salvar** para criar a configuração de pesquisa lov.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_18.png)

### Ações na configuração de pesquisa lov existente

Para gerenciar uma configuração de pesquisa lov existente, clique nos três pontos no canto superior direito da configuração.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_19.png)

**Ações disponíveis:**

* **Ativar / Desativar**\
  Alterna o status da configuração de pesquisa lov.
  * Configurações com status **Ativo** são marcadas com uma **Ativo** tag.
  * Configurações com status **Inativo** são marcadas com uma **Inativo** tag.
*   **Duplicado**\
    Após inserir um nome e clicar em **Feito**, uma cópia da configuração de pesquisa lov selecionada é criada.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_21.png)
* **Editar / Visualizar**\
  Modifique a configuração selecionada. Após fazer alterações, clique em **Salvar**.
*   **Excluir**\
    Exclui permanentemente a configuração após confirmação.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_20.png)

### Criar novo Campo

Dentro de cada configuração de pesquisa lov, você pode definir Campos adicionais como listas suspensas que atuam como pré-filtros para a lógica principal do lov.

Esses Campos são avaliados antes que a lista suspensa principal do lov seja carregada. Com base nos valores selecionados nesses Campos, os resultados do Campo lov principal são filtrados dinamicamente — habilitando listas dependentes.\
Por exemplo, selecionar um país em um Campo de pré-filtro pode restringir as opções de cidade na lista suspensa principal do lov.

Além de criar novos Campos, você também pode usar Campos existentes como pré-filtros. Quando configurado dessa forma, o valor selecionado no Campo existente filtrará automaticamente a lista suspensa principal do lov.

**Para adicionar um novo Campo:**

1. Abra a configuração de pesquisa lov desejada.
2.  Clique em **Criar** no canto superior direito.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_22.png)
3.  Configure as opções necessárias.

    **Opções de configuração de Campo (aplica-se aos contextos HEADER e LINE):**

    * **Campo de pesquisa**\
      A coluna a ser pesquisada no conjunto de dados selecionado para valores da lista suspensa.
      * **Campo de filtro**\
        Especifica o Campo cujo valor é usado para pré-filtrar os resultados da configuração de pesquisa lov antes que a lista principal seja preenchida.
      * **Valor do filtro** (opcional)\
        Adicione filtros estáticos para restringir ainda mais os resultados da pesquisa.
      * **Obrigatório**\
        Quando habilitado, este Campo deve ser preenchido antes que quaisquer listas dependentes possam ser preenchidas.
4.  Clique em **Salvar** para criar o novo Campo.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_23.png)

### Ações no Campo existente

Para gerenciar um Campo existente dentro de uma configuração de pesquisa lov, clique nos três pontos na coluna **Ações** ao lado do Campo.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_24.png)

**Ações disponíveis:**

* **Editar**\
  Modifique o Campo selecionado. Após as alterações, clique em **Salvar** para aplicar.
*   **Excluir**\
    Remove permanentemente o Campo após confirmação.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_20.png)
