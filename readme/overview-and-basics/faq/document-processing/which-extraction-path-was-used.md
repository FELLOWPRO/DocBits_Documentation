# Qual foi o caminho de extração utilizado?

"Porque é que esta tabela tem este aspeto?" responde-se descobrindo *o que* o DocBits fez com este documento: regras guardadas, a tabela de IA, qual o nível de IA e onde correu mal. Esta página é a lista de verificação que o suporte e os parceiros usam antes de alterar qualquer configuração.

## 1. Observe os separadores no ecrã de validação

Abra o documento e observe os separadores por cima da tabela de itens de linha:

| O que vê | Caminho |
|---|---|
| Linhas no separador **Tabela extraída** | Caminho baseado em regras. O fornecedor tem uma tabela treinada; as linhas vêm das regras de coordenadas guardadas e a IA não participou (exceto nas colunas marcadas como *Usar IA*). |
| Linhas no separador **Tabela extraída por IA**, campo *Tags* por baixo | Caminho de IA. Nenhuma regra guardada correspondeu; a extração de tabelas por IA produziu as linhas, usando o nível de IA da organização ou o nível definido para este fornecedor em *Mais definições* → *Modelo de IA baseado no fornecedor*. |
| Dica *AI table not found* no separador de IA | O caminho de IA correu e não devolveu nada para este documento. |
| Nenhum separador de tabela | Ambas as definições de tabela estão desativadas para a organização; nada extraiu a tabela. |
| *No line items yet* | O caminho correu, mas não encontrou linhas (sem texto legível, sem tabela na página, ou as regras não corresponderam a este layout). |

Os campos de cabeçalho têm o seu próprio distintivo de origem ao lado do valor: *Extracted using AI*, *Learned from validated AI extraction*, *Extracted using saved rules (FELLOW_KV2)*, *Extracted from electronic document*, *Calculated from vendor master data*. Estes distintivos descrevem o campo de cabeçalho, não a tabela.

## 2. Verifique a configuração do fornecedor

* **Definições → Processamento de Documentos → Classificação e Extração → Modelo de IA**: a tabela por baixo do seletor lista todos os fornecedores com um modelo guardado ou treino. Um fornecedor nesta lista com *dados de treino* tem regras guardadas; *repor os dados de treino* remove-as.
* **Definições → Processamento de Documentos → Definições OCR**: *Usar E-Text, se disponível* e *Usar dados de IA para tabelas* alteram o texto que a extração vê. Um fornecedor pode substituir a definição de E-Text em *Mais definições* no ecrã de validação.
* **Definições → Definições Globais → Tipos de Documento → Colunas da Tabela**: as opções oculta, obrigatória e *Usar IA*. Uma coluna oculta nunca é preenchida; uma coluna *Usar IA* é preenchida pela IA mesmo para fornecedores com regras.

## 3. Reproduza sem a interface (API / MCP)

Com acesso à API ou ao MCP, pode fazer as mesmas perguntas de forma programática:

| Pergunta | Ferramenta |
|---|---|
| Esta tabela foi produzida pela IA? | `get_extracted_tables(doc_id)`: cada tabela inclui `is_ai_table: true/false`. |
| O que dão as regras e o que dá a IA? | `get_table_extraction_report(doc_id, mode="nonai")` e novamente com `mode="ai"`; o relatório mostra a estrutura configurada, as linhas extraídas e a pré-visualização da página para cada caminho. Compare os dois. |
| Quais as colunas configuradas e com que opções? | `get_table_config(doc_type)` |
| O nível de IA faz diferença? | `compare_table_extraction_models(doc_id)`, executa dois níveis no mesmo documento (requer um documento com número de fornecedor). |
| Repetir a extração neste documento | `extract_table_ai(doc_id)` (IA) ou `restart_document(doc_id)` (pipeline completo). |
| O que registou o pipeline para este documento? | `get_document_logs(doc_id)` |

As ferramentas do DocBits MCP estão descritas na secção *DocBits MCP* da documentação.

## 4. Leia os registos

**Definições → Definições de registos** (Registo de atividade) mostra os eventos de todos os serviços. Para uma questão de tabela:

* Filtre pelo nome de ficheiro ou pelo ID do documento em *Pesquisar registos*.
* Use o filtro *Serviço*: a extração propriamente dita corre no serviço de extração e nos workers Celery, não no serviço `api`. Se só vir linhas de `api`, alargue o filtro.
* Uma execução normal regista, por ordem: documento recebido → OCR / E-Text → classificação → extração de campos → extração de tabelas (consulta das regras e, depois, IA quando nenhuma regra corresponde) → validação → mudança de estado. O passo que falta ou que comunica um erro é aquele a analisar.

## 5. Decida: configuração, dados ou bug

| Sintoma | Mais provável | Próximo passo |
|---|---|---|
| Tabela correta para o fornecedor A, errada para o fornecedor B, mesmo tipo de documento | Por fornecedor: B não tem regras, ou tem regras antigas que já não correspondem ao layout de B | Treine a tabela de B uma vez (ou elimine as regras de B para que a IA assuma). |
| Tabela errada para todos os fornecedores desde uma certa data | Uma definição da organização foi alterada (nível de IA, extração estruturada, vision, colunas da tabela) | Compare as definições com a data da alteração; reinicie um documento para confirmar. |
| Mesmo documento: caminho de regras vazio, caminho de IA correto | As regras não correspondem a esta variante de layout | Volte a treinar com este documento ou elimine as regras. |
| Mesmo documento: ambos os caminhos vazios | Sem texto legível (digitalização sem texto OCR, PDF apenas com imagem) | Visualização OCR no ecrã de validação; ative o E-Text se o PDF tiver camada de texto; experimente outra versão de OCR. |
| Uma coluna errada em todas as linhas, o resto correto | Mapeamento de colunas ou opção *Usar IA* | Definições de Colunas da Tabela; remapeie no treino de tabelas. |
| Linhas em falta nas quebras de página ou depois de um subtotal | Layout que a IA ou as regras não acompanharam | Treine a tabela com um documento de várias páginas; adicione uma tag como *"a tabela continua na página 2"*. |
| Passo de extração ausente nos registos, documento preso em *running* | Infraestrutura (fila de workers), não configuração | Verifique as tarefas pendentes (`get_pending_tasks_detail` via MCP) e contacte o suporte com o ID do documento. |

## O que enviar ao suporte

* ID do documento e organização
* Qual o separador que contém as linhas (Tabela extraída / Tabela extraída por IA / nenhum) e o nível de IA em uso
* Se o fornecedor tem regras guardadas e quando foram guardadas pela última vez
* Um documento de exemplo em que funciona e outro em que não funciona, se tiver ambos

## Páginas relacionadas

* [Resolução de Problemas de Extração de Tabelas](table-extraction-troubleshoot.md): qualidade da extração, OCR, E-Text, mensagens da tabela
* [Treino de campos de linha / Treino de tabelas](../../../administration-and-setup/setup/document-training/training-line-fields-table-training/README.md)
* [Tabela de IA](../../../end-user-and-partner-section/end-user-section/ai-table/README.md)
* [Definições de registos](../../../administration-and-setup/settings/log-settings/README.md)
