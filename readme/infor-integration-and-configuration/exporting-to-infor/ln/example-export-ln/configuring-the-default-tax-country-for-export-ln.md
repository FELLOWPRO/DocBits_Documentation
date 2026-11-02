# Configurar o País de Imposto Padrão na Exportação para o LN

### Visão geral

O país de imposto (Tax Country) padrão da exportação é definido como **DE (Alemanha)** para evitar erros de exportação. Ele pode ser alterado no arquivo de mapeamento de uma destas formas:

* Definindo um valor estático diferente.
* Mapeando-o dinamicamente para um campo do DocBits.

<mark style="color:red;">**Observação:**</mark> se o campo especificado não existir ou estiver vazio, a exportação volta a usar **DE**.

### Etapas para alterar o país de imposto

#### 1. Obter o arquivo de mapeamento

* Acesse **DocBits → Configurações → Processamento de documentos → Exportação**.
* Abra a configuração de exportação que deseja alterar.
*   Clique em **Download** para obter o arquivo de mapeamento.\\

    <figure><img src="../../../../.gitbook/assets/iScreen Shoter - Google Chrome - 250220120028.jpg" alt="Diálogo do Infor LN para o tipo de documento Invoice com o título Invoice LN, caixas de seleção para ION-Mapping File, IDM Mapping File e LN-Mapping File e um botão DOWNLOAD"><figcaption></figcaption></figure>
* Abra o arquivo em um editor de texto.

#### 2. Alterar o arquivo de mapeamento

Escolha uma das duas opções abaixo e aplique as alterações necessárias.

**Opção 1: valor estático**

Para definir um valor estático para o país de imposto, siga estas etapas:

1.  Defina um novo campo estático adicionando `,TaxCountry` à linha `StaticFields`.

    ```properties
    StaticFields=FinancialCompany...,TaxCountry
    ```
2.  Defina o código do país adicionando a linha a seguir:

    ```properties
    SF_TaxCountry=CountryCode
    ```

    Substitua `CountryCode` pelo código real do país, por exemplo, `ES` para a Espanha ou `DE` para a Alemanha:

    ```properties
    SF_TaxCountry=ES
    ```

**Exemplo:**

```properties
StaticFields=FinancialCompany,TaxCountry
SF_TaxCountry=FR
```

<figure><img src="../../../../.gitbook/assets/image (415).png" alt="Excerto do ficheiro de mapeamento LN com StaticFields=FinancialCompany,RateDeterminer,ExternalRateFactor e entradas HeaderFields como HF_SupplierCode=supplier_id e HF_InvoiceCurrency=currency"><figcaption></figcaption></figure>

**Opção 2: mapeamento dinâmico a partir de um campo do DocBits**

Para mapear dinamicamente o país de imposto a partir de um campo do DocBits:

1.  Adicione `,TaxCountry` à linha `HeaderFields`:

    ```properties
    HeaderFields=SupplierCode,...,TaxCountry
    ```
2.  Defina o mapeamento de campo correspondente:

    ```properties
    HF_TaxCountry=DocBits_Field_name
    ```

    Substitua `DocBits_Field_Name` pelo nome real do campo no DocBits:

    ```properties
    HF_TaxCountry=tax_country_1
    ```

**Exemplo:**

```properties
HeaderFields=SupplierCode,TaxCountry
HF_TaxCountry=tax_country_1
```

<figure><img src="../../../../.gitbook/assets/image (411).png" alt="Excerto do ficheiro de mapeamento LN com TaxCountry adicionado à linha StaticFields e uma entrada HF_TaxCountry mapeada na lista HeaderFields"><figcaption></figcaption></figure>

### Resumo

* Se o país de imposto **não estiver definido ou o campo estiver vazio**, o valor padrão é **DE**.
* **Use um valor estático** se o país de imposto for o mesmo em todas as exportações.
* **Use um mapeamento de campo dinâmico** se o país de imposto variar de documento para documento.

Seguindo essas etapas, você pode alterar o mapeamento do país de imposto de acordo com as suas necessidades.
