# AI Model

## Visão geral

A definição **AI Model** permite definir qual o modelo de IA usado por predefinição para a **extração de campos** e a **extração de tabelas** durante o processamento de documentos.\
Use o seletor de modelo atual e a tabela de preferências de modelo para rever a definição da organização e as sobreposições. Para custos, consulte as informações disponíveis no seu ambiente e as condições da sua subscrição.

## Como aceder

1.  Navegue para **Settings** → **Document Types** → **Classification and Extraction** → **General**

    <figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/site-complete-global-ai-model-options-en.png" alt="Definições de extração atuais e menu AI Model: Full, Fast, Nexus, Nexus Flash, Auto e Auto Nexus. Os valores privados da tabela estão ocultos; nenhum modelo foi selecionado nem nenhuma preferência eliminada."><figcaption><p>Definições de extração atuais e menu AI Model: Full, Fast, Nexus, Nexus Flash, Auto e Auto Nexus. Os valores privados da tabela estão ocultos; nenhum modelo foi selecionado nem nenhuma preferência eliminada.</p></figcaption></figure>
2.  Expanda **Extraction** e localize a definição **AI Model**.



## Opções de modelo de IA

O menu atual oferece **Full**, **Fast**, **Nexus**, **Nexus Flash**, **Auto** e **Auto Nexus**. São nomes de níveis de produto. As opções disponíveis, os modelos subjacentes e os custos em tokens podem mudar; verifique as informações do seu ambiente atual e as condições da sua subscrição em vez de confiar num nome histórico de modelo de fornecedor ou num preço fixo.

<figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/dbdc-3-six-model-options-en-20261031.png" alt="Menu pendente AI Model atual com Full, Fast, Nexus, Nexus Flash, Auto e Auto Nexus"><figcaption><p>Detalhe dos seis níveis de extração no menu atual do ambiente de desenvolvimento. Abrir e fechar o menu deixou a seleção existente inalterada.</p></figcaption></figure>

| Opção | O que verificar com documentos representativos |
| --- | --- |
| **Full** | Resultados de extração em layouts complexos, tempo de processamento e custo. |
| **Fast** | Resultados e tempo de processamento em documentos do dia a dia; o nome não é garantia para todos os documentos. |
| **Nexus** | Compare esta opção alternativa com a mesma amostra de documentos. |
| **Nexus Flash** | Verifique a qualidade e a latência nos seus layouts reais. |
| **Auto** | Verifique os resultados e os custos da seleção automática. |
| **Auto Nexus** | Verifique os resultados e os custos da opção de seleção automática Nexus. |

Quando o modelo de extração atual não tem sobreposição, a sua definição de modelo recorre à configuração da organização. Um valor específico do fornecedor não definido não significa universalmente Fast. Compare uma amostra fixa antes de mudar de modelo; uma mudança de modelo por si só não garante validação de campos, conciliação com encomendas, aprovação ou exportação bem-sucedida.



## Tabela de atribuição de modelos de IA

O **ecrã de validação** oferece um ponto de entrada para o modelo específico do fornecedor. A sua sobreposição é guardada para a organização e o modelo de extração atual (`tfidf_id`); não atualiza incondicionalmente todos os modelos nem documentos históricos do mesmo fornecedor.\
\
Para mais informações, consulte a documentação correspondente [aqui](../../../../end-user-and-partner-section/end-user-section/validation-screen/supplier-specific-ai-model-for-field-and-table-extraction.md).

A tabela de atribuição resume as preferências de extração relacionadas com o modelo. As colunas variam conforme a versão do produto; use os cabeçalhos atuais para inspecionar a associação de fornecedor, o modelo, as opções de extração e as informações de auditoria:

* **Supplier ID** – O identificador único do fornecedor
* **AI Model** – O nível configurado para esta entrada de modelo
* **Use Structured Extraction (AI)**, quando presente – A preferência de extração estruturada desta entrada
* **E-Text** – Indica se a funcionalidade E-Text está ativa
* **Created By / Modified By / Created On / Modified On** – Quem definiu a entrada e quando
* **Action** – Contém a opção para eliminar a entrada



### Eliminar entrada: remover sobreposições do modelo

Antes de um administrador eliminar uma entrada, deve identificar o respetivo modelo de extração e todas as preferências que contém. A eliminação pode remover várias sobreposições do modelo, não apenas a definição de modelo:

1.  Clique nos três pontos na coluna **Action**, junto à entrada do fornecedor, e selecione **Delete**.


2.  Aparece uma caixa de confirmação — confirme que pretende eliminar a entrada.



Após a eliminação, o processamento seguinte lê a configuração da organização aplicável e os valores de recurso para este modelo. Outros modelos associados ao mesmo fornecedor podem manter sobreposições independentes. A eliminação não reprocessa automaticamente documentos históricos. Para este guia não foi eliminada qualquer entrada nem realizada qualquer extração resultante.

## Definições e sobreposições

O Structured Output tem uma definição de organização/modelo separada do nível de modelo. Altere-a em More options no documento; a confirmação guarda a sobreposição e reinicia esse documento. Os indicadores na lista de definições são só de leitura. Eliminar uma entrada de preferência pode remover várias sobreposições de uma vez. [Structured Output para tabelas](../../../../end-user-and-partner-section/end-user-section/ai-table/structured-output.md).
