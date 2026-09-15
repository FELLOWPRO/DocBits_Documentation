# Tela de Validação

{% embed url="https://youtu.be/CmmQIxOaF6E?si=gYE-U-Jv4dLPi2xT" %}

## Visão Geral

<figure><img src="../../../.gitbook/assets/validation_screen1.png" alt=""><figcaption></figcaption></figure>

### Origem do Documento (Document Origin)

{% embed url="https://youtu.be/-m45XGiIeig" %}
DocBits Origin Setting Explained: Country Standards for Dates & Number Formats
{% endembed %}

Na Tela de Validação, você pode selecionar a Origem do documento no topo da tela. Com base na sua escolha, o DocBits aplica automaticamente os padrões regionais para:
*   **Formatos de data**
*   **Separadores numéricos** (vírgula vs ponto)

Quando você altera a origem, o documento será reiniciado para reaplicar a formatação e garantir que as regras regionais corretas sejam usadas.

### **Botão Salvar:**

<figure><img src="../../../.gitbook/assets/validation_screen2.png" alt=""><figcaption></figcaption></figure>

* **Botão Salvar:**
  * **Propósito:** Salva o estado atual do documento ou script em que se está trabalhando.
  * **Caso de Uso:** Após fazer alterações ou anotações em um documento, use este botão para garantir que todas as modificações sejam salvas.

### **Adicionar Regras Especiais:**

<figure><img src="../../../.gitbook/assets/validation_screen3.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/validation_screen4.png" alt=""><figcaption></figcaption></figure>

* **Adicionar Regras Especiais / Adicionar Script em DocBits:**
  * **Propósito:** Permite que os usuários implementem regras ou scripts específicos que personalizam como os documentos são processados.
  * **Caso de Uso:** Use este recurso para automatizar tarefas como extração de dados ou validação de formato, aumentando a eficiência do fluxo de trabalho.

{% hint style="info" %}
Veja aqui adicionar [Script em DocBits](../../../administration-and-setup/settings/global-settings/document-types/script/scripting-in-docbits/)
{% endhint %}

### **Campos Fuzzy:**

<figure><img src="../../../.gitbook/assets/validation_screen5.png" alt=""><figcaption></figcaption></figure>

* **Campos Fuzzy:**
  * **Propósito:** Ajuda a identificar e corrigir campos onde os dados podem não ser uma correspondência perfeita, mas são suficientemente próximos.
  * **Caso de Uso:** Útil em processos de validação de dados onde correspondências exatas nem sempre são possíveis, como nomes ou endereços levemente incorretos.

### **Campos Obrigatórios:**

<figure><img src="../../../.gitbook/assets/validation_screen6.png" alt=""><figcaption></figcaption></figure>

Existem campos que são obrigatórios para edições futuras, estes podem ser editados nas configurações.

Use a dica de ferramenta para descobrir se:

* É um campo obrigatório (required)
* Validação necessária
* Baixa confiança
* Descompasso no valor total de impostos

**Campos Obrigatórios:**

* **Propósito:** Identifica campos obrigatórios dentro dos documentos que devem ser preenchidos ou corrigidos antes de um processamento adicional.
* **Caso de Uso:** Garante que dados essenciais sejam capturados com precisão, mantendo a integridade dos dados e conformidade com as regras de negócios.

## Tabela extraída (itens de linha)

<figure><img src="../../../.gitbook/assets/validation_screen_line_items_table.png" alt="Tabela de itens de linha no ecrã de validação com a barra de ferramentas da tabela"><figcaption><p>A tabela extraída por baixo dos campos de cabeçalho</p></figcaption></figure>

Por baixo dos campos de cabeçalho, o DocBits mostra a tabela de itens de linha do documento: uma linha por linha da fatura, uma coluna por [coluna de tabela](../../../administration-and-setup/settings/global-settings/document-types/table-columns.md) configurada para o tipo de documento. Quando um tipo de documento tem várias tabelas (por exemplo, artigos e encargos), cada tabela tem o seu próprio separador por cima da grelha.

### De onde vem a tabela

Por cima da grelha existe um separador por cada caminho de extração que a organização ativou:

| Separador | Significado |
|---|---|
| **Tabela extraída** | Extração baseada em regras (definição *Extração de tabelas*). Para um fornecedor com tabela treinada, estas linhas vêm das regras guardadas e são extraídas da mesma forma em todos os documentos desse fornecedor; para um fornecedor sem treino, o separador pode estar vazio. |
| **Tabela extraída por IA** | A extração de tabelas por IA (definição *Extração de tabelas por IA*). Preenchida quando o fornecedor não tem regras guardadas e, para as colunas marcadas como *Usar IA*, mesmo quando existem regras. Uma dica *AI table not found* no separador significa que a IA não devolveu nada para este documento. |
| **PO Tables** | Apenas no construtor de layouts: as linhas da ordem de compra usadas para a correspondência. |

Se nenhum dos separadores aparecer, ambas as definições de tabela estão desativadas para a organização (Definições → Processamento de Documentos → Classificação e Extração). O nível de IA que lê a tabela é definido por organização e pode ser substituído por fornecedor, ver [Modelo de IA específico do fornecedor](supplier-specific-ai-model-for-field-and-table-extraction.md).

### Trabalhar na tabela

* **Editar uma célula**: clique nela e escreva. As colunas de valor, número e data são validadas enquanto escreve.
* **Adicionar nova linha à tabela**: acrescenta uma linha vazia no fim. Use-a quando uma linha não foi reconhecida.
* **Eliminar uma linha**: o ícone do caixote do lixo no fim da linha.
* **Adicionar colunas mapeadas vazias**: mostra as colunas configuradas que a IA deixou vazias, para que as possa preencher manualmente.
* **Restaurar coluna da tabela**: repõe uma coluna que removeu da vista neste documento.
* **Eliminar tabela**: limpa todas as linhas desta tabela neste documento. A configuração não é alterada.
* **Adicionar nova coluna de tabela** (administradores): a mesma caixa de diálogo das definições de colunas da tabela, sem sair do documento.
* **Tags** (apenas tabela de IA): breves indicações em texto para a IA, por exemplo *"a última coluna é o valor líquido"*. Ver [Tags da tabela de IA](../ai-table/ai-table-tags.md).
* **Aplicar** / **Guardar** / **Eliminar** ao lado das tags: *Aplicar* volta a executar a tabela de IA neste documento com as tags e as alterações de colunas que fez, sem guardar nada (se o documento tiver linhas com correspondência de PO, o DocBits avisa que as correspondências são removidas); *Guardar regras* guarda o mapeamento de colunas e as tags atuais para este fornecedor; *Eliminar regras* remove-os e volta a executar a extração por IA neste documento.
* **Exportar**: descarrega a tabela como ficheiro CSV.
* **Ir para a vista de extração de tabelas**: abre o treino de tabelas para este documento. Use-a quando o mesmo fornecedor sai sempre errado: desenhe a tabela uma vez, mapeie as colunas e clique em *Guardar regras*; a partir daí, as linhas aparecem no separador *Tabela extraída*. Ver [Treino de campos de linha / Treino de tabelas](../../../administration-and-setup/setup/document-training/training-line-fields-table-training/README.md).

{% hint style="info" %}
Se a tabela foi extraída pela IA e abrir o treino de tabelas, o DocBits pergunta *Table is already extracted by AI. Do you want to train manually?* Depois de guardar regras, a tabela de IA deixa de ser usada para este fornecedor.
{% endhint %}

### Extrair novamente a tabela

* **Mesmo documento, tabela de IA:** adicione ou altere tags e clique em **Aplicar**; a tabela de IA é reconstruída apenas para este documento. Para descartar também as tags e a formatação guardadas do fornecedor, clique em **Eliminar** (*Eliminar regras*): o DocBits confirma *Rules has been deleted successfully* e volta a executar a extração por IA.
* **Mesmo documento, regras treinadas:** abra *Ir para a vista de extração de tabelas*, corrija a tabela e clique em *Guardar e extrair novamente*.
* **Documento inteiro de novo (cabeçalho e tabela):** Dashboard → menu do documento → *Reiniciar*. Necessário depois de um administrador alterar as colunas da tabela ou as definições de extração.

### O que bloqueia a aprovação

A tabela é verificada quando guarda ou aprova. Uma célula a vermelho ou uma mensagem por baixo da tabela significa uma destas situações:

| Mensagem | Causa | O que fazer |
|---|---|---|
| Coluna obrigatória vazia | Uma coluna marcada como *Obrigatória* não tem valor nesta linha. | Preencha a célula ou pergunte a um administrador se a coluna tem mesmo de ser obrigatória. |
| *Line total does not match quantity x unit price (expected …, got …)* | `quantidade × preço unitário + encargos − desconto` difere do total da linha em mais de 0,02. Muitas vezes, um dos quatro valores foi lido para a coluna errada. | Corrija o valor que está errado face ao documento; se uma coluna como *Encargos* é sistematicamente preenchida com o valor errado, informe o seu administrador (ver a secção Resolução de problemas em [Colunas da Tabela](../../../administration-and-setup/settings/global-settings/document-types/table-columns.md)). |
| *Line items add up to … but the net total is …* | A soma dos totais das linhas difere do valor líquido no cabeçalho. | Procure uma linha em falta ou duplicada, ou um valor do cabeçalho lido incorretamente. |
| *Line Item Table is missing Mandatory column for PO* | A correspondência de PO precisa de número do artigo, preço unitário, quantidade e valor total; uma dessas colunas está oculta. | Administrador: torne a coluna visível em Colunas da Tabela. |

Um administrador pode desativar todas as verificações de tabela de um tipo de documento com *Ignorar validação da tabela* (Tipos de Documento → Mais definições); as discrepâncias nas linhas e as colunas obrigatórias vazias deixam então de ser comunicadas.

Mais sobre as verificações: [Verificações automáticas no ecrã de validação](automatic-checks-on-the-validation-screen.md) e [Resolução de Problemas de Extração de Tabelas](../../../overview-and-basics/faq/document-processing/table-extraction-troubleshoot.md).

### **Lupa:**

<figure><img src="../../../.gitbook/assets/validation_screen7.png" alt="" width="118"><figcaption></figcaption></figure>

* **Lupa:**
  * **Propósito:** Fornece uma visão ampliada de uma área selecionada do documento.
  * **Caso de Uso:** Ajuda a examinar detalhes finos ou texto pequeno em documentos, garantindo precisão na entrada ou revisão de dados.

<figure><img src="../../../.gitbook/assets/validation_screen8.png" alt="" width="329"><figcaption></figcaption></figure>

### **Abrir nova janela:**

<figure><img src="../../../.gitbook/assets/validation_screen9.png" alt="" width="130"><figcaption></figcaption></figure>

* **Abrir Nova Janela:**
  * **Propósito:** Abre uma nova janela para comparação lado a lado de documentos ou multitarefa.
  * **Caso de Uso:** Útil ao comparar dois documentos ou ao consultar informações adicionais sem sair do documento atual.

### **Atalhos de teclado:**

<figure><img src="../../../.gitbook/assets/validation_screen10.png" alt="" width="145"><figcaption></figcaption></figure>

* **Atalhos de Teclado:**
  * **Propósito:** Permite que os usuários realizem ações rapidamente usando combinações de teclado.
  * **Caso de Uso:** Aumenta a velocidade e eficiência na navegação e processamento de documentos, minimizando a dependência da navegação com o mouse.

<figure><img src="../../../.gitbook/assets/validation_screen11.png" alt="" width="239"><figcaption></figcaption></figure>

### **Tarefas:**

<figure><img src="../../../.gitbook/assets/validation_screen12.png" alt="" width="55"><figcaption></figcaption></figure>

Para compartilhar informações internas, você pode criar tarefas e atribuí-las a um funcionário específico ou grupo dentro da empresa.

* **Tarefas:**
  * **Propósito:** Permite que os usuários criem tarefas relacionadas a documentos e as atribuam a membros da equipe.
  * **Caso de Uso:** Facilita a colaboração e gestão de tarefas dentro das equipes, garantindo que todos saibam suas responsabilidades.

<figure><img src="../../../.gitbook/assets/validation_screen13.png" alt="" width="218"><figcaption></figcaption></figure>

### **Modo de Anotação:**

<figure><img src="../../../.gitbook/assets/validation_screen_annotation_mode.png" alt="Annotation Mode Button" width="187"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/annotation_mode_example.png" alt="Annotation Mode Example"><figcaption></figcaption></figure>

{% embed url="https://youtu.be/ay0gGtwlqRE" %}
DocBits Annotation Mode Tutorial: Add Notes in Validation & Download With/Without Annotations
{% endembed %}

You can leave annotations on a document. This can be helpful to leave information for other users who further edit this document.

* **Modo de Anotação:**
  * **Propósito:** Permite que os usuários deixem notas ou anotações diretamente no documento.
  * **Caso de Uso:** Útil para fornecer feedback, instruções ou notas importantes para outros membros da equipe que trabalharão no documento mais tarde.

### **Mesclar:**

<figure><img src="../../../.gitbook/assets/validation_screen16.png" alt="" width="60"><figcaption></figcaption></figure>

Documentos podem ser mesclados aqui, por exemplo, se uma página de uma fatura estava faltando, essas páginas podem ser mescladas posteriormente desta forma sem que o documento inteiro precise ser excluído ou reenviado.

* **Mesclar Documentos:**
  * **Propósito:** Combina vários documentos em um único arquivo.
  * **Caso de Uso:** Útil em cenários onde partes de um documento são digitalizadas separadamente e precisam ser consolidadas.

### **Visualização OCR:**

<figure><img src="../../../.gitbook/assets/validation_screen17.png" alt="" width="77"><figcaption></figcaption></figure>

Na visualização OCR, o texto é automaticamente filtrado do documento. Isso é usado para reconhecer características relevantes, como o código postal, número do contrato, número da fatura e a ordenação de um documento.

* **Visualização OCR:**
  * **Propósito:** Reconhece automaticamente o texto dentro dos documentos usando tecnologia de Reconhecimento Óptico de Caracteres.
  * **Caso de Uso:** Simplifica o processo de digitalização de textos impressos ou manuscritos, tornando-os pesquisáveis e editáveis.

<figure><img src="../../../.gitbook/assets/validation_screen18.png" alt=""><figcaption></figcaption></figure>

### **Criar ticket:**

<figure><img src="../../../.gitbook/assets/validation_screen19.png" alt="" width="97"><figcaption></figcaption></figure>

Ao contrário das tarefas que são passadas internamente dentro da empresa, este ticket de suporte é importante para nos notificar e criar imediatamente um ticket em caso de erros e/ou discrepâncias. Isso torna o processo muito mais fácil porque você pode enviar imediatamente o bug com o documento apropriado. Também há a opção de definir prioridade, tirar uma captura de tela do documento ou fazer upload de uma.

* **Criar Ticket:**
  * **Propósito:** Permite que os usuários relatem problemas ou discrepâncias criando um ticket de suporte.
  * **Caso de Uso:** Essencial para a rápida resolução de problemas e bugs, ajudando a manter a integridade e o funcionamento suave do sistema.

<figure><img src="../../../.gitbook/assets/validation_screen20.png" alt="" width="237"><figcaption></figcaption></figure>

### **Logs de Script do Documento:**

<figure><img src="../../../.gitbook/assets/validation_screen21.png" alt="" width="160"><figcaption></figcaption></figure>

Scripts podem ser criados nas configurações sob Tipos de Documento; esta informação será então exibida aqui.

* **Logs de Script do Documento:**
  * **Propósito:** Exibe logs relacionados a scripts que foram implementados para diferentes tipos de documentos.
  * **Caso de Uso:** Útil para rastrear e depurar ações de script em documentos, ajudando os usuários a entender os processos automatizados e corrigir quaisquer problemas.

<figure><img src="../../../.gitbook/assets/validation_screen22.png" alt=""><figcaption></figcaption></figure>

### **Mais configurações:**

<figure><img src="../../../.gitbook/assets/docbits_validation_screen_more_settings_menu.jpg" alt="Docbits Validation Screen More Settings Menu"><figcaption></figcaption></figure>

### **Fluxo do Documento:**

Lá você encontrará o fluxo do documento

* **Propósito:** Mostra a sequência e progressão do processamento de documentos dentro do sistema.
* **Caso de Uso:** Ajuda a rastrear o status do documento através de diferentes estágios, garantindo que todas as etapas necessárias de processamento sejam seguidas.

### **Ir para o Modelo de Layout:**

* Com esta opção você será redirecionado e poderá editar seu layout ou usar o modelo padrão
* **Ir para o Modelo de Layout:**
  * **Propósito:** Redireciona os usuários para um editor de layout onde eles podem modificar modelos existentes ou aplicar um padrão.
  * **Caso de Uso:** Permite a personalização dos layouts de documentos para atender a necessidades ou preferências específicas de negócios, melhorando o alinhamento visual e funcional do documento com os padrões da empresa.

### Use E-Text if Available

* **Propósito:** Permite que o DocBits utilize e-text para todos os documentos de um fornecedor específico, se disponível, melhorando a precisão da extração.
* **Caso de Uso:** Melhora a extração de texto aproveitando o texto incorporado em vez de OCR, o que pode levar a resultados mais precisos para este fornecedor.

### [Modelo de IA Baseado no Fornecedor](supplier-specific-ai-model-for-field-and-table-extraction.md)

* **Propósito:** Permite a seleção entre três modelos de IA diferentes para otimizar os resultados de extração para um fornecedor específico.
* **Caso de Uso:** Garante melhor precisão na extração ao escolher o modelo de IA mais adequado para a estrutura e conteúdo dos documentos de cada fornecedor.
