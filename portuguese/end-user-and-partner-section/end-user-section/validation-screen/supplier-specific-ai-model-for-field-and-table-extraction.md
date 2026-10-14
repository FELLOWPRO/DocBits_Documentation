# Modelo de IA Específico do Fornecedor para Extração de Campos e Tabelas

Na seção de ferramentas da **Tela de validação**, você pode escolher o modelo de IA usado para **Extração de campos** e **Extração de tabelas**.\ O **modelo de IA** selecionado é aplicado apenas a todos os documentos do fornecedor atual.

Para alterar o modelo, abra o menu de opções clicando no botão **Mais opções** (três pontos) no lado direito da tela e escolha um dos modelos disponíveis:<br>

* **Full** – Maior precisão; custa 2 tokens por documento
* **Fast** – Nível predefinido; custa 1 token por documento
* **Nexus** – Custa 1 token por documento
* **Nexus Flash** – Nível mais rápido da família Nexus; custa 1 token por documento
* **Auto** – O DocBits decide por documento se o Fast é suficiente ou se é necessário o Full; custa 1 token por documento
* **Auto Nexus** – Como o Auto, mas restrito à família de modelos Nexus; custa 1 token por documento

<figure><img src="../../../.gitbook/assets/dbdc865-supplier-ai-model-menu-pt-20261012.png" alt="Menu de opções da tela de validação com o seletor Modelo de IA"><figcaption><p>Abra o menu de opções e escolha o modelo de IA para este fornecedor.</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/dbdc865-supplier-ai-model-options-pt-20261012.png" alt="Lista Modelo de IA aberta com Full, Fast, Nexus, Nexus Flash, Auto e Auto Nexus"><figcaption><p>A lista <strong>Modelo de IA</strong> com as seis opções disponíveis.</p></figcaption></figure>

Se os resultados da **extração de campos** ou **extração de tabelas** não forem satisfatórios, tente mudar para outro modelo para melhorar a precisão.

Para configurar o modelo de IA **globalmente para fornecedores sem modelo personalizado** ou para **gerenciar qual modelo está ativo para cada fornecedor**, consulte a documentação correspondente [**aqui**](../../../administration-and-setup/settings/document-processing/classification-and-extraction/ai-model.md).
