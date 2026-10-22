# Guia do Arquivo de Descritor de Estrutura EDI

## **1. Visão Geral**

O **Arquivo de Descritor de Estrutura** define como segmentos EDI repetidos (por exemplo, `N1`–`N4`) são agrupados em JSON estruturado. Ele garante:

* **Análise precisa** de elementos relacionados como unidades únicas.
* **Saída consistente** para sistemas downstream.

_Para um exemplo completo com detalhes de segmento, consulte_ [_Exemplo de Descritor de Estrutura_](edi-structure-descriptor.md)_._

## **2. Acesso e Edição Básica**

#### **Acessando o Arquivo**

1.  **Configurações** → **Tipo de Documento** → \[Seu Documento (por exemplo, _Ordem de Compra_)] → **E-Doc.**

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Ff6zyL0AvmqSvrogZdnox%252Fimage.png%3Falt%3Dmedia%26token%3D6bc9ab55-6ee9-43d1-b576-4c5833c208cf\&width=768\&dpr=4\&quality=100\&sign=a23de442\&sv=2)
2. Em **E-Doc**, selecione seu formato (por exemplo, _EDI_ ).
3.  Clique em **Descritor de Estrutura**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FOuNVhIuYBPJTu4PdMecy%252Fimage.png%3Falt%3Dmedia%26token%3Dd111b34e-0dd9-4436-9df4-f59490ac0d87\&width=768\&dpr=4\&quality=100\&sign=6e8e9f0e\&sv=2)

#### **Gerenciamento de Rascunho**

* **Criar um Rascunho**: Clique no ícone de lápis ✏️ para começar a editar.
* **Excluir Rascunhos**: Use o ícone de lixeira 🗑️ para remover rascunhos não utilizados.
* **Ativar Alterações**: Clique no ícone de marca de seleção ✅ para aprovar e publicar suas alterações.
  * **Nota**: Ativar uma nova versão irá **desativar automaticamente** a anterior.

## 3. Função de Visualização (Visualizar XML Analisado)

A **Função de Visualização** permite testar e visualizar como um arquivo EDI enviado é analisado usando o Arquivo de Descritor de Estrutura atual.

#### Uso

* Envie um arquivo EDI via fluxo de envio padrão.
* Copie o **ID do Documento** do arquivo enviado.
* Navegue até a interface do **Arquivo de Descritor de Estrutura**.
*   Abra a **Função de Visualização**.\


    <div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F9lddYJl2G4tzpdr9RD5F%252Fimage.png%3Falt%3Dmedia%26token%3Df7663f70-ef10-4e64-bbdc-41048ed8352a&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=36ce2b93&#x26;sv=2" alt="" width="375"></div>
* Insira o **ID do Documento** no campo e pressione **Testar**.
* A saída **XML estruturado resultante** será exibida.

Isso é especialmente útil para depurar mapeamentos e validar agrupamentos estruturais em tempo real.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FBXU6zeFapt7ZIVFl37Iz%252Fimage.png%3Falt%3Dmedia%26token%3D9d51e329-b781-4781-a527-3258f6f933c6\&width=768\&dpr=4\&quality=100\&sign=4ca17281\&sv=2)

## 6. Vídeo Tutorial

Um guia em vídeo para este tipo de arquivo está disponível na [página de Vídeos.](https://docs.docbits.com/administration-and-setup/settings/global-settings/document-types/edi/edi/edi-videos) Use-o para acompanhar a configuração, edição e visualização.


<figure><img src="../../../../../../../.gitbook/assets/site-all-edi-list-pt.png" alt="Formato EDI existente com os seus quatro atributos configurados."><figcaption><p>Formato EDI existente com os seus quatro atributos configurados.</p></figcaption></figure>

<figure><img src="../../../../../../../.gitbook/assets/site-all-edi-detail-pt.png" alt="Atributo STRUCTUREDESCRIPTOR ativo: descritor de estrutura JSON no editor só de leitura."><figcaption><p>Atributo STRUCTUREDESCRIPTOR ativo: descritor de estrutura JSON no editor só de leitura.</p></figcaption></figure>


As vistas mostram uma configuração e uma versão existentes. As definições variam consoante o tipo de documento e o formato. Valide as alterações num rascunho antes da ativação.

As imagens mostram as etapas em português e a versão ativa da configuração em modo só de leitura. Os nomes técnicos dos editores, os identificadores de atributos e o código de configuração mantêm-se como na versão ilustrada.
