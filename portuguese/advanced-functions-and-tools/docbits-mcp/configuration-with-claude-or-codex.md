# Configurar o DocBits com Claude ou Codex

Descreva o resultado desejado, deixe o assistente ler a configuração, reveja a proposta e aplique a alteração acordada. O DocBits MCP disponibiliza estas ferramentas no Claude e no Codex com as permissões da conta DocBits ligada. Alterações de configuração exigem as permissões de administrador correspondentes.

Este guia descreve um procedimento. Não comprova uma correção já realizada num cliente nem um teste de exportação bem-sucedido.

## 1. Ligar à organização correta

Escolha região e ambiente no [guia de endpoints e início de sessão](setup-and-configuration.md). Os comandos usam o **sandbox da UE**; substitua o URL se a organização de teste usar outro endpoint. Execute-os no computador do assistente, inicie sessão e autorize o acesso ao DocBits no navegador.

{% tabs %}
{% tab title="Claude Code" %}
```bash
claude mcp add --transport http docbits https://eu.sandbox.api.docbits.com/v3/mcp
claude mcp login docbits
```
{% endtab %}
{% tab title="Codex CLI" %}
```bash
codex mcp add docbits --url https://eu.sandbox.api.docbits.com/v3/mcp
codex mcp login docbits
```
{% endtab %}
{% endtabs %}

Na aplicação Codex, use as definições MCP ou a configuração partilhada com a CLI no mesmo computador. No Claude Desktop, use um conector remoto personalizado se o seu plano o permitir, com o mesmo endpoint HTTP. Inicie uma conversa nova se as ferramentas não aparecerem. Instruções atuais: [Codex MCP](https://developers.openai.com/codex/mcp) e [Claude MCP](https://code.claude.com/docs/en/mcp).

```text
Apenas leitura. Verifica o ambiente e a organização DocBits ligados com
get_api_info e get_current_user. Lista as ferramentas de configuração.
Mostra o ID da organização e o host API, sem tokens nem fragmentos de chaves.
Não alteres definições nem processes documentos.
```

Se a organização ainda não estiver resolvida, leia a configuração relevante e verifique o `org_id` da resposta. Pare se não corresponder à organização pretendida. Os nomes podem ter prefixos de cliente/servidor; use as ferramentas e os esquemas de argumentos anunciados pela ligação.

## 2. Alterar uma definição simples

```text
Encontra com find_setting a definição de extração de códigos QR desta
organização de teste. Mostra o setting_key exato e o valor atual. Se houver
vários resultados, pergunta qual pretendo. Se apply_setting suportar a
definição, prepara uma pré-visualização da ativação. Mostra current_value
e proposed_value; espera a minha confirmação antes de confirm_setting_change.
```

`apply_setting` cria apenas uma pré-visualização. Após confirmar essa proposta concreta, `confirm_setting_change(preview_id)` guarda a alteração. Volte a ler o valor e conserve o `undo_id`: `undo_setting_change` permite revertê-la dentro do prazo devolvido. Normalmente a pré-visualização expira após 5 minutos e a reversão após 15. Se o valor mudou ou a pré-visualização expirou, crie e reveja outra.

Para alterações estruturadas suportadas: `preview_settings_action` → `confirm_settings_action` → `undo_settings_action`. Leia primeiro os tipos de ação disponíveis. Se não existir uma ação de escrita suportada, peça o `app_path` e altere a definição no DocBits. Não invente uma chave de preferência nem substitua o processo por uma chamada genérica a `set_preference`.

## 3. Investigar uma nota de crédito guardada como Invoice

Uma transformação Custom pode produzir sempre `<INVOICE_TYPE>Invoice</INVOICE_TYPE>`, mesmo quando o XML original contém um código de nota de crédito. É o cenário do [guia de diagnóstico com vídeo da interface real do DocBits](../../administration-and-setup/settings/global-settings/document-types/edi/credit-note-recognized-as-invoice.md).

```text
Apenas leitura. Para o XML original e ID de documento fornecidos, identifica
família eDoc, sintaxe, versão/perfil e código de tipo original. Lista atributos
Custom e Default. Lê TRANSFORMATION e EXTRACTION_PATHS efetivos e predefinidos
com get_edoc_attribute_source. Regista attribute_id, active_version
e active_value_id e lê o histórico de versões.
Segue TypeCode -> XML transformado -> invoice_type -> campo guardado,
pré-visualização de exportação e scripts posteriores. Mostra provas e dúvidas.
Não atives, elimines, reinicies, aproves nem exportes nada.
```

Use a **etiqueta exata do formato detetado**, sem adivinhar a versão ZUGFeRD ou Factur-X. O `doc_type_key` técnico pode continuar a ser `INVOICE`; o valor funcional investigado é `invoice_type`.

| Leitura | Ferramenta MCP |
| --- | --- |
| Atributos Custom e Default | `list_edoc_custom_attributes` |
| Fonte efetiva ou predefinida e IDs ativos | `get_edoc_attribute_source`, com `source: "effective"` ou `"default"` |
| Histórico e rascunhos | `list_edoc_attribute_versions`, com `include_values: true` se necessário |
| Campos guardados, registos, pré-visualização de exportação | `get_extracted_fields`, `get_document_logs`, `get_export_preview` |

A versão ativa hoje não prova qual processou um documento antigo. Se os registos não o estabelecerem, mantenha essa incerteza. Uma pré-visualização PDF não comprova o tipo guardado nem os montantes exportados.

<figure><img src="../../.gitbook/assets/edocs-transformation-pt.png" alt="Exemplo de desenvolvimento apenas de leitura: editor de fonte e versões do DocBits. Leia a sua própria fonte efetiva e valor ativo por MCP; a imagem não demonstra uma alteração guardada."><figcaption><p>Exemplo de desenvolvimento apenas de leitura: editor de fonte e versões do DocBits. Leia a sua própria fonte efetiva e valor ativo por MCP; a imagem não demonstra uma alteração guardada.</p></figcaption></figure>

## 4. Pré-visualizar a correção mínima

```text
Propõe a alteração mínima da nossa transformação Custom existente para
que 381 produza Credit Note. Preserva os outros mapeamentos e códigos de
nota de crédito já suportados. Não classifiques 383 nem 384 como Credit Note.
Mostra o diff. Testa o candidato nos documentos de teste sem o guardar.
Mostra INVOICE_TYPE transformado e montantes relevantes, indicando os testes em falta.
```

Para um **atributo existente da própria organização**, chame `preview_edoc_custom_xslt` com o candidato completo:

```json
{
  "attribute_id": "<custom_attribute_id_from_response>",
  "candidate_value": "<complete_candidate_xslt>",
  "doc_id": "<test_document_id_in_this_org>"
}
```

Substitua todos os marcadores por valores das suas respostas. O XSLT/JSON deve conter a fonte completa com escape JSON correto. A ferramenta usa um documento existente da mesma organização. Devolve **XML** para `TRANSFORMATION`, campos/tabelas para `EXTRACTION_PATHS` e **PDF** para `PREVIEW`, sem guardar o candidato. Para comparar com a transformação predefinida, teste a sua fonte como outro candidato com o mesmo atributo Custom e documento.

`compare_edoc_extraction` compara **EXTRACTION_PATHS** e exige um atributo personalizado de caminhos de extração. Não compara duas transformações. Não crie uma personalização desnecessária só para usar esta ferramenta.

Sem um atributo Custom, pare antes de o criar em produção: `create_edoc_custom_attribute` cria a primeira versão **imediatamente ativa**, sem opção de apenas rascunho. Prepare a nova personalização numa organização de teste ou use o processo de criação/pré-visualização suportado pelo editor DocBits. Não tente alterar globalmente as regras predefinidas partilhadas.

## 5. Guardar um rascunho e ativá-lo deliberadamente

Depois de rever diff e resultado, volte a ler a fonte ativa. Se mudou entretanto, compare novamente. Para um atributo Custom existente, use `update_edoc_custom_attribute`:

```json
{
  "attribute_id": "<custom_attribute_id_from_response>",
  "new_value": "<complete_reviewed_xslt>",
  "activate": false
}
```

Indique sempre `activate: false` neste passo; o valor predefinido da ferramenta é `true`. Registe o ID do valor de versão devolvido e confirme com `list_edoc_attribute_versions` que a versão anterior continua ativa. Um rascunho guardado não afeta o processamento normal.

Após os testes, o administrador confirma organização, atributo, diff e versão concretos. Ative com `activate_edoc_attribute_version`:

```json
{
  "attribute_id": "<custom_attribute_id_from_response>",
  "draft_id": "<value_id_of_reviewed_version>"
}
```

`draft_id` é o **ID do valor da versão**, não o número de versão nem o ID do atributo. Volte a ler fonte efetiva e histórico para confirmar que esse valor está ativo. O eDocs usa estas ferramentas diretamente, sem o fluxo genérico de definições com `preview_id`. Leia os IDs no ambiente de destino; os IDs do sandbox não podem ser reutilizados em produção.

## 6. Verificar classificação, montantes e exportação

`test_electronic_document` testa a configuração **atualmente ativa** sem guardar um documento. Não permite selecionar candidato ou rascunho. Por MCP HTTP remoto, envie o XML original como `file_content_base64` com `file_name`; o servidor não pode ler um `file_path` local do seu computador. Para testar todo o processamento do candidato, ative-o primeiro explicitamente na organização de teste. A pré-visualização XSLT não testa scripts posteriores nem exportações.

| Código original | Verificação esperada |
| --- | --- |
| 380 | Invoice mantém-se Invoice |
| 381 | Nota de crédito passa a Credit Note |
| 261 | Preservar o comportamento de nota de crédito quando o formato/mapeamento o suporta |
| 383 | Nota de débito não passa a Credit Note por ajustar uma fatura |
| 384 | Fatura corrigida não passa a Credit Note por corrigir uma fatura |

Verifique também campos personalizados, linhas, totais e a definição de sinal negativo. Processe um **novo documento de teste** numa organização isolada com exportações automáticas controladas. Compare `invoice_type` guardado, painel e `get_export_preview`. Uma exportação real para o sistema de destino exige um teste acordado separadamente; nem o teste sem persistência nem a pré-visualização comprovam entrega ao ERP.

`validate_all_edocs` testa sem persistência os ficheiros de teste disponíveis no servidor; `verify_electronic_documents` **carrega e processa** ficheiros de teste. Não substituem os seus documentos representativos e verificações posteriores. Se faltarem ficheiros ou ferramentas, use exemplos fornecidos.

## 7. Reverter e tratar documentos antigos separadamente

Para reverter, chame `activate_edoc_attribute_version` com o `active_value_id` anterior como `draft_id` e verifique a fonte efetiva. Não elimine toda a personalização para corrigir um campo: perderia outros mapeamentos e seriam usadas as regras predefinidas.

Não reinicie documentos históricos em massa. O reinício pode apagar dados extraídos e registos de exportação e repetir aprovações ou exportações. Reveja por documento o estado de exportação, aprovações e alterações manuais antes de decidir.

Para outras configurações, comece por `find_setting` ou `run_config_checks` e peça a ação suportada ou o caminho na interface. Conserve proposta antes/depois, resultados de testes, IDs de valores ativos e referência de reversão no registo da alteração.
