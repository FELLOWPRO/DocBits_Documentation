# Guia do arquivo Structure Descriptor de EDI

## 1. Visão geral

O **Structure Descriptor File** é um arquivo **JSON** que define como segmentos EDI repetidos (por exemplo, `N1`–`N4`) são agrupados em uma saída estruturada. Ele é a primeira etapa do processamento de EDI:

* **Interpretação precisa** de segmentos relacionados como unidades únicas.
* **Saída consistente** para a [Transformation](../edi-transformation-file-guide.md) e os sistemas downstream.

_Para um exemplo completo com os detalhes dos segmentos, consulte_ [_Structure Descriptor Example_](edi-structure-descriptor.md)_._

## 2. Acesso e edição básica

#### **Acessando o arquivo**

1. Acesse **Settings** → **Document Types** e abra **E-Doc** para o tipo de documento que você deseja configurar (por exemplo, _Purchase Order_). Você precisa de acesso de administrador na sua organização para editar esses arquivos.

    <!-- dbdc-139-edi-sd-list-en.png --><figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/dbdc-139-edi-sd-list-en.png" alt="Página E-Doc do Sandbox em inglês com o formato EDI expandido e a linha JSON STRUCTURE DESCRIPTOR listada acima de TRANSFORMATION, PREVIEW e EXTRACTION PATHS"><figcaption>Abra o E-Doc do seu tipo de documento; o formato EDI lista seus arquivos de configuração.</figcaption></figure>

2. Expanda o formato **EDI**. Seus arquivos de configuração são listados juntos: **STRUCTURE DESCRIPTOR**, **TRANSFORMATION**, **PREVIEW** e **EXTRACTION PATHS**.
3. Clique na linha **STRUCTURE DESCRIPTOR**, marcada como **JSON**, para abri-la.

#### **Gerenciamento de rascunhos**

A coluna da esquerda mostra a lista de **Version** do arquivo. A versão marcada como **Active** é a que o DocBits utiliza.

* **Criar um rascunho**: clique no ícone de lápis ✏️ ao lado da versão ativa para começar a editar. O arquivo ativo não pode ser editado diretamente.
* **Excluir rascunhos**: use o ícone de lixeira 🗑️ para remover os rascunhos que não estão em uso.
* **Ativar alterações**: clique no ícone de confirmação ✅ em um rascunho para aprovar e publicar suas alterações.
  * <mark style="color:red;">**Nota**</mark>: ao ativar uma nova versão, a anterior é **desativada automaticamente**.

<!-- dbdc-139-edi-sd-detail-en.png --><figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/dbdc-139-edi-sd-detail-en.png" alt="Editor JSON do Structure Descriptor no Sandbox em inglês, com a lista de versões à esquerda mostrando a versão 1 marcada como Active e um ícone de lápis para criar um rascunho"><figcaption>O arquivo Structure Descriptor com sua lista de versões; o ícone de lápis cria um rascunho que você pode editar.</figcaption></figure>

## 3. Função Preview (visualizar a saída interpretada)

A **função Preview** permite testar como um arquivo EDI enviado é interpretado com o Structure Descriptor exibido no momento, antes de ativar qualquer alteração.

#### Uso

* Envie um arquivo EDI pelo fluxo de upload padrão.
* Copie o **Document ID** do arquivo enviado.
* Abra o arquivo **Structure Descriptor** conforme descrito acima.
* Clique em **Preview** no canto superior direito para abrir o painel de teste.

    <div align="left"><!-- dbdc-139-edi-sd-preview-en.png --><figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/dbdc-139-edi-sd-preview-en.png" alt="Página do Structure Descriptor no Sandbox em inglês com o painel de teste Preview aberto, mostrando o campo de entrada Document Id e o botão Test" width="560"><figcaption>O painel de teste: informe um Document ID e pressione Test.</figcaption></figure></div>

* Informe o **Document ID** no campo e pressione **Test**.
* A **saída estruturada** resultante é exibida ao lado do editor.

Isso é especialmente útil para depurar mapeamentos e validar agrupamentos estruturais em tempo real. É necessário um documento EDI representativo do seu próprio formato; o resultado exibido depende do arquivo enviado.

## 4. Passo a passo em vídeo

Um guia em vídeo para este tipo de arquivo está disponível na [página de vídeos.](../edi-videos.md)\
Use-o para acompanhar a configuração, a edição e a visualização.

As telas mostram uma configuração e uma versão existentes. As configurações variam conforme o tipo de documento e o formato. Valide as alterações em um rascunho antes de ativá-las.
