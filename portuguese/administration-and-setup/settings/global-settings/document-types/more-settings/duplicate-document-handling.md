# Detecção de duplicatas

## Visão geral

No **DocBits**, você pode filtrar documentos duplicados especificando quais campos devem corresponder e definindo um intervalo de tempo durante o qual as duplicatas devem ser detectadas.

Esta página fornece um guia detalhado sobre como habilitar e usar o recurso **Detecção de duplicatas** de forma eficaz.

## Habilitando a Detecção de duplicatas

Para habilitar a detecção de documentos duplicados no **DocBits**, siga estas etapas:

1.  Navegue até **Configurações** → **Configurações globais** → **Tipos de documentos**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/Calculate_PO_unit_price_1.png)
2.  Selecione o **Tipo de documento** desejado e clique em **Mais configurações**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/Calculate_PO_unit_price_2.png)
3.  Vá para a seção **Detecção de duplicatas**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/DuplicateDocument_3.png)

DocBits fornece duas opções para identificar documentos duplicados:

1. **Detecção de documentos duplicados**:\
   Este recurso verifica documentos duplicados carregados no **DocBits** com base nos critérios selecionados. Se algum documento corresponder aos critérios selecionados em outros documentos, ele será sinalizado como duplicado.
2.  **Detecção de faturas duplicadas** (Disponível apenas para o tipo de documento **Fatura**):\
    Este recurso requer a sincronização de Faturas de Fornecedores do Infor para o DocBits. Ele compara os números das faturas no painel do DocBits com aqueles no Infor. Se o mesmo número de fatura aparecer mais de uma vez, ele será sinalizado como duplicado.

    <mark style="color:red;">**Nota**</mark>: O uso do recurso **Detecção de faturas duplicadas** resultará em uma cobrança adicional de crédito.

## Filtrar quais documentos devem ser detectados como duplicados

Uma vez que a **Detecção de duplicatas** esteja habilitada, dois menus suspensos estarão disponíveis para configuração:

*   **Campos de detecção duplicados**\
    Selecione os campos que devem ser usados para identificar duplicatas (por exemplo, ID do fornecedor, Data, Número da fatura, etc.). Documentos que corresponderem a esses campos serão sinalizados como duplicados.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/DuplicateDocument_4.png)
*   **Intervalo de detecção de duplicatas**

    Use esta configuração para definir o intervalo de tempo dentro do qual as duplicatas são detectadas. Documentos carregados dentro do intervalo selecionado serão comparados entre si com base nos campos selecionados.

    **Opções disponíveis:**

    * 1 mês
    * 3 meses (Recomendado)
    * 6 meses
    * 1 ano

    <mark style="color:red;">**Nota**</mark>: Um intervalo de 3 meses é recomendado para garantir desempenho ideal. Selecionar um intervalo mais longo pode levar a tempos de carregamento mais lentos no painel.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/DuplicateDocument_6.png)

## Visualizando Documentos Duplicados no Painel

Uma vez que a **Detecção de duplicatas** esteja habilitada, quaisquer documentos identificados como duplicados exibirão um ícone de indicador de duplicata no painel.

*   Clique neste ícone para abrir os registros correspondentes em uma visualização de tela dividida lado a lado para fácil comparação.\
    <mark style="color:red;">**Nota**</mark>: O ícone só aparecerá se pelo menos uma duplicata tiver sido detectada para o documento.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/DuplicateDocument_7.png)
*   Ao visualizar um documento sinalizado, uma barra de aviso aparecerá na parte superior, indicando que o documento é uma duplicata.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/DuplicateDocument_5.png)
