# XRechnung

{% embed url="https://youtu.be/AxrHNEmmXtg" %}
Tutorial de faturação eletrónica do DocBits: processar XRechnung / ZUGFeRD (Factur-X), validar dados e automatizar fluxos de trabalho
{% endembed %}

## Visão geral

No painel de administração do XRechnung, encontrará os seguintes componentes principais:

## 1. Transformação

### Finalidade

A transformação converte dados em bruto, normalmente em XML, num formato estruturado que cumpre requisitos específicos, por exemplo para gerar uma fatura. No XRechnung, isto é feito sobretudo com XSLT (Extensible Stylesheet Language Transformations), uma linguagem que transforma documentos XML noutros documentos XML, HTML ou texto simples.

### Como funciona

• Modelo XSLT: o ficheiro XSLT define como os dados XML são processados e qual deve ser o resultado. Aplica regras e modelos para extrair, alterar e apresentar os dados do documento XML.

• Elementos e atributos: o ficheiro XSLT contém elementos e atributos que controlam a transformação. Por exemplo, \<xsl:value-of> extrai o valor de um nó específico do documento XML.

### Opções do administrador

• Alterar o XSLT:

• Editar modelos existentes: um administrador pode alterar os modelos XSLT existentes para mudar a transformação dos dados XML de entrada. Por exemplo, pode acrescentar regras ao ficheiro XSLT para extrair informação adicional.

• Criar novas versões: quando forem necessárias alterações, um administrador pode criar uma nova versão do modelo XSLT. As versões anteriores ficam preservadas para consulta ou para reposição, se necessário.

### Exemplo:

Suponha que o modelo XSLT extrai o identificador da fatura através de:

```xml
<xsl:value-of select="//INVOICE/INVOICE_ID/text()" />
```

Se for necessário extrair um novo campo, como um número de referência do cliente, o administrador pode acrescentar:

```xml
<xsl:value-of select="//INVOICE/CUSTOMER_REFERENCE_NUMBER/text()" />
```

## 2. Pré-visualização

### Finalidade

A pré-visualização permite aos administradores verificar o resultado da transformação XSLT antes de a finalizar. Este passo ajuda a confirmar que as regras funcionam corretamente e que o resultado cumpre as normas exigidas.

### Como funciona

• Validação em tempo real: a pré-visualização mostra como os dados transformados ficarão num documento real, como uma fatura. Isto ajuda a detetar erros de conteúdo ou de formatação numa fase inicial.

• Ajustes: se a pré-visualização mostrar divergências ou erros, é possível corrigi-los diretamente no ficheiro de transformação XSLT.

### Opções do administrador

• Personalizar a pré-visualização:

• Alterar as configurações de pré-visualização: o administrador pode escolher as partes da transformação a apresentar, por exemplo para se concentrar numa secção do documento ou testar novas regras do modelo XSLT.

• Guardar e repetir: depois de ajustar o ficheiro, atualize a pré-visualização para verificar as alterações. Repita o processo até obter o resultado pretendido.

### Exemplo:

Se o administrador verificar que o formato da data está incorreto, por exemplo YYYY-MM-DD em vez de DD-MM-YYYY, pode alterar o XSLT para formatar a data e verificar imediatamente o resultado na pré-visualização.

## 3. Caminhos de extração

### Finalidade

Os caminhos de extração indicam onde procurar dados numa estrutura XML ou JSON. Permitem isolar a informação específica do documento que será utilizada na transformação ou noutras etapas de processamento.

### Como funciona

• XPath e JSONPath: os caminhos de extração utilizam XPath para XML ou JSONPath para JSON para indicar a localização dos dados no documento. Estas expressões dizem ao sistema onde encontrar e como extrair a informação necessária.

### Opções do administrador

• Definir e alterar caminhos:

• Alterar caminhos existentes: o administrador pode adaptar os caminhos de extração se a estrutura dos dados mudar ou se for necessário extrair mais informação, alterando as expressões XPath ou JSONPath.

• Adicionar novos caminhos: para novos campos ou dados, o administrador pode definir caminhos de extração que indiquem a localização correta no documento XML ou JSON.

### Exemplo:

Numa fatura XML, se o caminho para o identificador da fatura estiver definido como:

```json
"invoice_id": "//INVOICE/INVOICE_ID/text()"
```

E for necessário acrescentar um novo campo, como a morada de entrega, o administrador pode adicionar:

```json
"shipping_address": "//INVOICE/SHIPPING/ADDRESS/text()"
```

## Regras efetivas e ativação

As regras específicas da organização têm prioridade sobre as predefinições do formato eDoc detetado. Verifique a TRANSFORMATION ativa e verifique qual o nó que fornece invoice_type no XML transformado; o caminho depende do formato. Save guarda um rascunho; utilize a marca de verificação para o ativar após os testes. Uma Preview renderizada não comprova o tipo de documento guardado. Consulte o [guia de resolução de problemas de classificação](../credit-note-recognized-as-invoice.md) para obter informações sobre os códigos 381/261, os scripts posteriores e as precauções de reprocessamento.
