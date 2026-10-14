# Exportar códigos fiscais para LN

## **Visão Geral:**

\
Este guia irá orientá-lo através do processo de configuração para garantir que os códigos fiscais sejam corretamente exportados do DocBits para o LN.

## **Códigos Fiscais Únicos**

### **Passo 1: Configurar Lista de Valores**

1.  Vá para **Configurações** -> **Processamento de Documentos** -> **Lista de Valores**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FsOvkQi6jHPOqhlU2lCRO%252FTaxCodes_1.png%3Falt%3Dmedia%26token%3Dbf6cb4a5-9d82-40d0-8222-68788d44bf16\&width=768\&dpr=4\&quality=100\&sign=5145579e\&sv=2)
2.  Clique em **Novo**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fnnoys71KFjrJz97lPu2F%252FTaxCodes_2.png%3Falt%3Dmedia%26token%3D26c8ba44-7e3f-437e-abd6-d09993231f2a\&width=768\&dpr=4\&quality=100\&sign=20bede4e\&sv=2)
3.  Crie uma lista com o nome `Tax_Country` e clique em **Salvar**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FVH48FUS9K0rT7PoTNqnw%252FTaxCodes_3.png%3Falt%3Dmedia%26token%3Daf31c7a7-28d5-48cd-98b0-40a7a4370168\&width=768\&dpr=4\&quality=100\&sign=7627670e\&sv=2)
4.  Crie as seguintes três listas adicionais:

    * `Tax_Code_Full`
    * `Tax_Code_Reduced`
    * `Tax_Code_Free`

    <div><figure><img src="../../../.gitbook/assets/TaxCodes_28.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_29.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_30.png" alt=""><figcaption></figcaption></figure></div>
5.  Clique em uma das listas recém-criadas para abri-la. Em seguida, pressione o botão **Adicionar Linha** para adicionar uma nova linha.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FIQ9cEPZ9lnn2SP00Y63z%252FTaxCode_4.png%3Falt%3Dmedia%26token%3D52497d98-a1d9-4bbb-a097-36d065b5bbe6\&width=768\&dpr=4\&quality=100\&sign=c85a13ef\&sv=2)
6.  Insira os valores respectivos desejados do **LN** e pressione **Salvar** para salvar as alterações.

    * Se você tiver vários valores, pode clicar em **Adicionar Mais Valores** para adicioná-los.

    <div><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F2lnyo3G6vlowfPiN0Nb5%252FTaxCodes_5.png%3Falt%3Dmedia%26token%3D52280de9-dd51-4bee-baf8-2b77a2209675&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=fb8c44b8&#x26;sv=2" alt=""> <figure><img src="../../../.gitbook/assets/TaxCodes_27.png" alt=""><figcaption></figcaption></figure></div>

    * **NOTA:** Você pode encontrar os Códigos Fiscais no LN em: **Comum** → **Tributação** → **Dados Mestres** → **Códigos Fiscais** → **Códigos Fiscais por País**

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FdHRIH3zefU9umtuT7ziz%252FTaxCodes_LN.png%3Falt%3Dmedia%26token%3Debe5f21a-575f-492d-9797-01f4e706203f\&width=768\&dpr=4\&quality=100\&sign=ed632294\&sv=2)

### **Passo 2: Adicionar Campos no DocBits**

1.  Navegue até **Configurações** -> **Configurações Globais** -> **Tipos de Documentos**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FJFsiV4Pzbj8vIhqJfDaJ%252FTaxCodes_6.png%3Falt%3Dmedia%26token%3D203ddd31-195e-4cc3-87f7-d1b12fc3013c\&width=768\&dpr=4\&quality=100\&sign=a64ef7b9\&sv=2)
2.  Escolha o menu **Campos** correspondente ao Tipo de Documento onde você deseja adicionar os campos.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Ff653FGmIYXrNbhOzfSP8%252FTaxCodes_7.png%3Falt%3Dmedia%26token%3D1bd1abe5-8921-4e36-8e92-581c30c4bfbf\&width=768\&dpr=4\&quality=100\&sign=2b6009a0\&sv=2)
3.  Sob **IVA & Valores**, crie seis novos campos da seguinte forma:

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fl3HFRkxlZabhjj5loD6H%252FTaxCodes_8.png%3Falt%3Dmedia%26token%3D2c3f1ed1-4be7-4708-baa6-d7afe2b4b39a\&width=768\&dpr=4\&quality=100\&sign=5ffbe154\&sv=2)

<table data-header-hidden><thead><tr><th width="306"></th><th width="139"></th><th width="119"></th><th></th></tr></thead><tbody><tr><td><strong>Nome</strong></td><td><strong>Título</strong></td><td><strong>Tipo de Campo</strong></td><td><strong>Lista de Valores</strong></td></tr><tr><td><code>tax_country</code></td><td>Tax Country</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_country_2</code></td><td>Tax Country Reduced</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_country_3</code></td><td>Tax Country Free</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_code_without_country</code></td><td>Tax Code</td><td>Dropdown</td><td>Tax_Code_Full</td></tr><tr><td><code>tax_code_without_country_2</code></td><td>Tax Code Reduced</td><td>Dropdown</td><td>Tax_Code_Reduced</td></tr><tr><td><code>tax_code_without_country_3</code></td><td>Tax Code Free</td><td>Dropdown</td><td>Tax_Code_Free</td></tr></tbody></table>

<div><figure><img src="../../../.gitbook/assets/TaxCodes_10.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_11.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_12.png" alt=""><figcaption></figcaption></figure></div>

<div><figure><img src="../../../.gitbook/assets/TaxCodes_13.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_14.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_15.png" alt=""><figcaption></figcaption></figure></div>

4.  Após salvar cada campo, clique em **Salvar Configurações** para aplicar as alterações.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FGFJtph4tpOZIWglbHxrf%252FTaxCodes_20.png%3Falt%3Dmedia%26token%3Db2f950b0-5198-4b6c-ae28-aa1cdf2dad57\&width=768\&dpr=4\&quality=100\&sign=bf4f16b7\&sv=2)

### **Passo 3: Editar Layout**

1.  Vá para **Configurações** -> **Configurações Globais** -> **Tipos de Documentos**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FJFsiV4Pzbj8vIhqJfDaJ%252FTaxCodes_6.png%3Falt%3Dmedia%26token%3D203ddd31-195e-4cc3-87f7-d1b12fc3013c\&width=768\&dpr=4\&quality=100\&sign=a64ef7b9\&sv=2)
2.  Abra o menu **Editar Layout** para o Tipo de Documento que você deseja editar.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FnxkuI9bosmKKLPq0gIxC%252FTaxCodes_19.png%3Falt%3Dmedia%26token%3Db7163eab-5a37-4395-b433-537525d7b461\&width=768\&dpr=4\&quality=100\&sign=c04ece2f\&sv=2)
3.  Selecione a **Origem do Documento** apropriada para a qual você deseja aplicar os Códigos Fiscais.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FbkrJ56Qw3WawokWz2gnb%252FTaxCodes_26.png%3Falt%3Dmedia%26token%3Dc588a68a-6a33-4128-9f56-9912b544f85b\&width=768\&dpr=4\&quality=100\&sign=4a4bc036\&sv=2)
4.  Role para baixo até a seção **Tax Details**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FyzQhwyhrp9i4V9pb85lq%252FTaxCodes_21.png%3Falt%3Dmedia%26token%3D20ee020b-20a5-4d55-b8a6-960bda821625\&width=768\&dpr=4\&quality=100\&sign=d88578ee\&sv=2)
5. Expanda o menu suspenso **Elementos do Formulário**.
6.  Na seção **Tax Details**, use a ferramenta **Horizontal Separator**. Arraste e solte entre as sub-seções dentro da seção fiscal para separá-las claramente e reduzir a confusão.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FBrsp5xo81Rf6a9kwkR28%252FTaxCodes_22.png%3Falt%3Dmedia%26token%3D72786399-6f8b-485e-a787-c8d71333fe32\&width=768\&dpr=4\&quality=100\&sign=3c7d4cea\&sv=2)
7. Expanda o menu suspenso **Campos do Formulário**.
8.  Pesquise por **Tax Country** e arraste e solte o campo em sua área respectiva.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FUgaHNnPiXIEqbDMowdI4%252FTaxCodes_23.png%3Falt%3Dmedia%26token%3D6786a41c-cb53-485a-87e3-e9f9f12d4933\&width=768\&dpr=4\&quality=100\&sign=c6640ca2\&sv=2)
9.  Pesquise por **Tax Code** e arraste e solte o campo em sua área correspondente.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FCYpdEBqyN3Je081u19dF%252FTaxCodes_24.png%3Falt%3Dmedia%26token%3Dc1c5c1e1-9820-4927-b67d-e6dcfa8e094a\&width=768\&dpr=4\&quality=100\&sign=79372792\&sv=2)
10. Salve o modelo.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FnopUJhMG5tm2PAD4tLc5%252FTaxCodes_25.png%3Falt%3Dmedia%26token%3Dfbb05319-79f8-4a95-ad2c-1698dbbb597d\&width=768\&dpr=4\&quality=100\&sign=8a441477\&sv=2)

### Passo 4: Verifique se Tudo Funcionou

Após fazer o upload de um novo documento no DocBits com as configurações de documento corretas selecionadas, você agora deve ser capaz de selecionar os códigos fiscais que adicionou às listas no Passo 1.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FZs4N9eOyzwWLTYXkl63Z%252FTaxCodes_31.png%3Falt%3Dmedia%26token%3Db4379547-2624-423c-b239-d5b2cc649616\&width=768\&dpr=4\&quality=100\&sign=f7bb9465\&sv=2)

## Código Fiscal Múltiplo

### **Passo 1: Configurar Lista de Valores**

1.  Vá para **Configurações** -> **Processamento de Documentos** -> **Lista de Valores**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FsOvkQi6jHPOqhlU2lCRO%252FTaxCodes_1.png%3Falt%3Dmedia%26token%3Dbf6cb4a5-9d82-40d0-8222-68788d44bf16\&width=768\&dpr=4\&quality=100\&sign=5145579e\&sv=2)
2.  Clique em **Novo**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fnnoys71KFjrJz97lPu2F%252FTaxCodes_2.png%3Falt%3Dmedia%26token%3D26c8ba44-7e3f-437e-abd6-d09993231f2a\&width=768\&dpr=4\&quality=100\&sign=20bede4e\&sv=2)
3.  Crie uma lista com o nome `Tax_Country` e clique em **Salvar**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FVH48FUS9K0rT7PoTNqnw%252FTaxCodes_3.png%3Falt%3Dmedia%26token%3Daf31c7a7-28d5-48cd-98b0-40a7a4370168\&width=768\&dpr=4\&quality=100\&sign=7627670e\&sv=2)
4.  Crie as seguintes três listas adicionais:

    * `Tax_Code_Full`
    * `Tax_Code_Reduced`
    * `Tax_Code_Free`

    <div><figure><img src="../../../.gitbook/assets/TaxCodes_28.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_29.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_30.png" alt=""><figcaption></figcaption></figure></div>
5.  Clique em uma das listas recém-criadas para abri-la. Em seguida, pressione o botão **Adicionar Linha** para adicionar uma nova linha.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FIQ9cEPZ9lnn2SP00Y63z%252FTaxCode_4.png%3Falt%3Dmedia%26token%3D52497d98-a1d9-4bbb-a097-36d065b5bbe6\&width=768\&dpr=4\&quality=100\&sign=c85a13ef\&sv=2)
6.  Insira os valores respectivos desejados do **LN** e pressione **Salvar** para salvar as alterações.

    * Se você tiver vários valores, pode clicar em **Adicionar Mais Valores** para adicioná-los.

    <div><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F2lnyo3G6vlowfPiN0Nb5%252FTaxCodes_5.png%3Falt%3Dmedia%26token%3D52280de9-dd51-4bee-baf8-2b77a2209675&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=fb8c44b8&#x26;sv=2" alt=""> <figure><img src="../../../.gitbook/assets/TaxCodes_27.png" alt=""><figcaption></figcaption></figure></div>

    * **NOTA:** Você pode encontrar os Códigos Fiscais no LN em: **Comum** → **Tributação** → **Dados Mestres** → **Códigos Fiscais** → **Códigos Fiscais por País**

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FdHRIH3zefU9umtuT7ziz%252FTaxCodes_LN.png%3Falt%3Dmedia%26token%3Debe5f21a-575f-492d-9797-01f4e706203f\&width=768\&dpr=4\&quality=100\&sign=ed632294\&sv=2)

### **Passo 2: Adicionar Campos no DocBits**

1.  Navegue até **Configurações** -> **Configurações Globais** -> **Tipos de Documentos**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FJFsiV4Pzbj8vIhqJfDaJ%252FTaxCodes_6.png%3Falt%3Dmedia%26token%3D203ddd31-195e-4cc3-87f7-d1b12fc3013c\&width=768\&dpr=4\&quality=100\&sign=a64ef7b9\&sv=2)
2.  Escolha o menu **Campos** correspondente ao Tipo de Documento onde você deseja adicionar os campos.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Ff653FGmIYXrNbhOzfSP8%252FTaxCodes_7.png%3Falt%3Dmedia%26token%3D1bd1abe5-8921-4e36-8e92-581c30c4bfbf\&width=768\&dpr=4\&quality=100\&sign=2b6009a0\&sv=2)
3.  Sob **IVA & Valores**, crie seis novos campos da seguinte forma:

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fl3HFRkxlZabhjj5loD6H%252FTaxCodes_8.png%3Falt%3Dmedia%26token%3D2c3f1ed1-4be7-4708-baa6-d7afe2b4b39a\&width=768\&dpr=4\&quality=100\&sign=5ffbe154\&sv=2)

<table data-header-hidden><thead><tr><th width="306"></th><th width="139"></th><th width="119"></th><th></th></tr></thead><tbody><tr><td><strong>Nome</strong></td><td><strong>Título</strong></td><td><strong>Tipo de Campo</strong></td><td><strong>Lista de Valores</strong></td></tr><tr><td><code>tax_country</code></td><td>Tax Country</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_country_2</code></td><td>Tax Country Reduced</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_country_3</code></td><td>Tax Country Free</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_code_without_country</code></td><td>Tax Code</td><td>Dropdown</td><td>Tax_Code_Full</td></tr><tr><td><code>tax_code_without_country_2</code></td><td>Tax Code Reduced</td><td>Dropdown</td><td>Tax_Code_Reduced</td></tr><tr><td><code>tax_code_without_country_3</code></td><td>Tax Code Free</td><td>Dropdown</td><td>Tax_Code_Free</td></tr></tbody></table>

<div><figure><img src="../../../.gitbook/assets/TaxCodes_10.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_11.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_12.png" alt=""><figcaption></figcaption></figure></div>

<div><figure><img src="../../../.gitbook/assets/TaxCodes_13.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_14.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_15.png" alt=""><figcaption></figcaption></figure></div>

4.  Após salvar cada campo, clique em **Salvar Configurações** para aplicar as alterações.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FGFJtph4tpOZIWglbHxrf%252FTaxCodes_20.png%3Falt%3Dmedia%26token%3Db2f950b0-5198-4b6c-ae28-aa1cdf2dad57\&width=768\&dpr=4\&quality=100\&sign=bf4f16b7\&sv=2)

### **Passo 3: Editar Layout**

1.  Vá para **Configurações** -> **Configurações Globais** -> **Tipos de Documentos**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FJFsiV4Pzbj8vIhqJfDaJ%252FTaxCodes_6.png%3Falt%3Dmedia%26token%3D203ddd31-195e-4cc3-87f7-d1b12fc3013c\&width=768\&dpr=4\&quality=100\&sign=a64ef7b9\&sv=2)
2.  Abra o menu **Editar Layout** para o Tipo de Documento que você deseja editar.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FnxkuI9bosmKKLPq0gIxC%252FTaxCodes_19.png%3Falt%3Dmedia%26token%3Db7163eab-5a37-4395-b433-537525d7b461\&width=768\&dpr=4\&quality=100\&sign=c04ece2f\&sv=2)
3.  Selecione a **Origem do Documento** apropriada para a qual você deseja aplicar os Códigos Fiscais.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FbkrJ56Qw3WawokWz2gnb%252FTaxCodes_26.png%3Falt%3Dmedia%26token%3Dc588a68a-6a33-4128-9f56-9912b544f85b\&width=768\&dpr=4\&quality=100\&sign=4a4bc036\&sv=2)
4.  Role para baixo até a seção **Tax Details**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FyzQhwyhrp9i4V9pb85lq%252FTaxCodes_21.png%3Falt%3Dmedia%26token%3D20ee020b-20a5-4d55-b8a6-960bda821625\&width=768\&dpr=4\&quality=100\&sign=d88578ee\&sv=2)
5. Expanda o menu suspenso **Elementos do Formulário**.
6.  Na seção Tax Details, use a ferramenta **Sub Group**. Arraste e solte ao lado de um campo existente.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FbV9kR81GqllW9sClfE4o%252FTaxCodesMulti_1.png%3Falt%3Dmedia%26token%3D901d57c5-5a4f-4d2a-a82f-1630a8dadc1c\&width=768\&dpr=4\&quality=100\&sign=1cbd476f\&sv=2)
7.  Para nomear seu subgroup, clique no subgroup e insira o nome desejado no campo **Label**.

    <div><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FGZMoEWIEx1AGTV8XENRb%252FTaxCodesMulti_2.png%3Falt%3Dmedia%26token%3D546d1055-4f4c-4ea1-9834-52f538d506d6&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=3a874aed&#x26;sv=2" alt=""> <figure><img src="../../../.gitbook/assets/TaxCodesMulti_3.png" alt=""><figcaption></figcaption></figure></div>
8.  Arraste e solte os campos que correspondem a este grupo no campo **Sub Group**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FhN7BvWWdS2yXCJN5WQyM%252FTaxCodeMulti_4.png%3Falt%3Dmedia%26token%3D5c7b668b-a24e-488e-a89d-348ab9f20b48\&width=768\&dpr=4\&quality=100\&sign=41300825\&sv=2)
9. Expanda o menu suspenso **Campos**.
10. Pesquise por **Tax** e arraste e solte os campos respectivos, como **Tax Country** e **Tax Code**, no subgroup correspondente.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Ff1i9nvAjHZ2iElDkaD0L%252FTaxCodeMulti_5.png%3Falt%3Dmedia%26token%3D072cf596-0c91-42aa-8053-c5f3434fe8ed\&width=768\&dpr=4\&quality=100\&sign=ff055219\&sv=2)
11. Repita os passos 5 a 10 2 vezes para alcançar o seguinte estado:

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F7StBFYZdEU8XQN58eO7d%252FTaxCodeMulti_6.png%3Falt%3Dmedia%26token%3D00c529aa-534f-4c98-b84a-cc8d6f6ed34f\&width=768\&dpr=4\&quality=100\&sign=5b8f49db\&sv=2)
12. Salve o modelo.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fjhpi4S4uuglZn3S6SU7l%252FTaxCodeMulti_7.png%3Falt%3Dmedia%26token%3D70b00e37-bda9-4337-921a-0f54f9ad0167\&width=768\&dpr=4\&quality=100\&sign=82c81283\&sv=2)

### Passo 4: Verifique se Tudo Funcionou e as mudanças resultantes

Após fazer o upload de um novo documento no DocBits com as configurações de documento corretas selecionadas, você poderá selecionar os códigos fiscais que adicionou no Passo 1 e adicionar múltiplos códigos fiscais configurados no Passo 3.

* O documento começará com três seções distintas: uma para valores fiscais totais, uma para valores fiscais reduzidos e uma para valores fiscais isentos.
* Clicar no botão de mais dentro de uma seção criará um duplicado, permitindo múltiplas submissões na taxa fiscal selecionada.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FFtHUVmkPlVFR2iL65fvM%252FTaxCodeMulti_8.png%3Falt%3Dmedia%26token%3D05dc796e-f0a6-4f9d-ba1c-12fcd4428dfe\&width=768\&dpr=4\&quality=100\&sign=f8405568\&sv=2)

* Seções podem ser excluídas clicando no botão de remover.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FA8g22I76nvN1BN8DooAm%252FTaxCodeMulti_9.png%3Falt%3Dmedia%26token%3Df176fe91-d69b-4bc2-ad27-de1338c66b33\&width=768\&dpr=4\&quality=100\&sign=216696a1\&sv=2)

* Os Valores Totais serão calculados como uma soma de todas as seções.
* A Validação do Valor Total será modificada com base em todas as seções fiscais.
* Scripts para novas seções só podem ser aplicados uma vez que os campos tenham sido adicionados à visualização.

### Nota para LN:

No **LN**, a posição USt será preenchida com base no número da posição do menu suspenso Tax Code/Tax Country. Apenas o número da posição será enviado para exportação.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FO8vwWP4n8aQ9kipGvflH%252FTaxCodesLN_2.png%3Falt%3Dmedia%26token%3D8d4dca62-e8aa-47ac-923c-610db3f34364\&width=768\&dpr=4\&quality=100\&sign=91f8169f\&sv=2)

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F4zmzEqOYROmQplSlMD85%252FTaxCodesLN_3.png%3Falt%3Dmedia%26token%3D4f4f7ab0-1dbf-406c-98d3-4fba782e4e40\&width=768\&dpr=4\&quality=100\&sign=2af745d1\&sv=2)

#### **Mapeamento de Exportação**

Para vincular a Linha Fiscal com a Linha de Custo:

1. Adicione `TaxLine` à lista **InvoiceCostFields**.
2. Adicione a seguinte entrada, seguindo o exemplo abaixo:\
   `ICF_TaxLine = TF_position`

<figure><img src="../../../.gitbook/assets/TaxCodeMulti_10.png" alt=""><figcaption></figcaption></figure>
