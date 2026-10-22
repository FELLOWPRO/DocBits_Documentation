# e-docs

{% embed url="https://youtu.be/AxrHNEmmXtg" %}
Tutorial de faturação eletrónica do DocBits: processar XRechnung / ZUGFeRD (Factur-X), validar dados e automatizar fluxos de trabalho
{% endembed %}

<figure><img src="../../../../../.gitbook/assets/site-all-edi-list-pt.png" alt="Formato EDI existente com os seus quatro atributos configurados."><figcaption><p>Formato EDI existente com os seus quatro atributos configurados.</p></figcaption></figure>

#### Visão geral

No DocBits, as configurações EDI permitem definir e gerir a estrutura e o formato das mensagens EDI correspondentes a vários tipos de documento, como faturas ou pedidos de compra. Estas configurações permitem adaptar as mensagens às normas e aos requisitos dos diferentes parceiros comerciais e setores.

#### Principais funcionalidades e opções

1. **Elementos da configuração EDI**:
   * **Descritor de estrutura**: define a estrutura básica do documento EDI, incluindo a ordem dos segmentos, os campos obrigatórios e os qualificadores necessários para que o documento seja válido.
   * **Transformação**: define as transformações que convertem os dados do documento numa mensagem EDI. Normalmente, inclui o mapeamento dos campos do documento para segmentos e elementos EDI.
   * **Pré-visualização**: permite aos administradores verificar o aspeto da mensagem EDI após a transformação, ajudando a confirmar a exatidão antes da transmissão.
   * **Caminhos de extração**: apresenta os caminhos utilizados para extrair os valores do documento que irão preencher a mensagem EDI.
2. **XSLT Editor**:
   * Permite editar e validar o XSLT (eXtensible Stylesheet Language Transformations) utilizado na transformação. O XSLT transforma documentos XML noutros documentos XML ou em formatos como HTML e texto.

<figure><img src="../../../../../.gitbook/assets/site-all-edi-detail-pt.png" alt="Atributo STRUCTUREDESCRIPTOR ativo: descritor de estrutura JSON no editor só de leitura."><figcaption><p>Atributo STRUCTUREDESCRIPTOR ativo: descritor de estrutura JSON no editor só de leitura.</p></figcaption></figure>

## Regras efetivas e ativação

Se uma nota de crédito eletrónica aparecer como Invoice, siga o [guia de resolução de problemas de classificação](credit-note-recognized-as-invoice.md). Este explica como verificar a origem personalizada ou predefinida efetivamente utilizada, os códigos de tipo, os Extraction Paths e a ativação segura.

## Guias por país

Consulte os guias por país para obter as designações exatas dos formatos, a sintaxe, os limites das versões e o estado da configuração examinada. [Formatos, versões e guias por país para eDocs](supported-electronic-documents/README.md).


As vistas mostram uma configuração e uma versão existentes. As definições variam consoante o tipo de documento e o formato. Valide as alterações num rascunho antes da ativação.

As imagens mostram as etapas em português e a versão ativa da configuração em modo só de leitura. Os nomes técnicos dos editores, os identificadores de atributos e o código de configuração mantêm-se como na versão ilustrada.
