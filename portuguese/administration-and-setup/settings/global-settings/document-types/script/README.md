# Script

<figure><img src="../../../../../.gitbook/assets/Bildschirmfoto%202024-05-08%20um%2009.43.25.png" alt=""><figcaption></figcaption></figure>

{% embed url="https://youtu.be/n8NpWWIjmlA" %}
DocBits Document Scripts Explained: Automate Custom Logic in Your Document Workflow
{% endembed %}

#### Visão Geral

Os scripts no DocBits são tipicamente escritos em uma linguagem de script suportada pelo sistema Python. Eles são acionados durante o fluxo de processamento de documentos para aplicar lógica de negócios complexa ou garantir a integridade e precisão dos dados antes que os dados sejam processados ou armazenados.

#### Recursos e Opções Principais

1. **Gerenciamento de Scripts**:
   * **Nome**: Cada script recebe um nome único para identificação.
   * **Tipo de Documento**: Associa o script a um tipo de documento específico, determinando em quais documentos o script será aplicado.
   * **Acionar Em**: Define quando o script é acionado (por exemplo, no upload do documento, antes da exportação de dados, após a validação de dados).
   * **Status Ativo/Inativo**: Permite que os administradores ativem ou desativem scripts sem excluí-los, proporcionando flexibilidade nos testes e implantação.
2. **Editor de Scripts**:
   * Fornece uma interface onde os scripts podem ser escritos e editados. O editor geralmente suporta realce de sintaxe, realce de erros e outras funcionalidades para auxiliar no desenvolvimento de scripts.
   * **Exemplo de Script**: Os scripts podem incluir operações como percorrer as linhas de fatura para validar totais ou remover entradas que não atendam a determinados critérios.

<figure><img src="../../../../../.gitbook/assets/Bildschirmfoto%202024-05-08%20um%2009.43.37.png" alt=""><figcaption></figcaption></figure>

{% @jira/embed url="https://fellowpro.atlassian.net/browse/DOCB-2498" %}
