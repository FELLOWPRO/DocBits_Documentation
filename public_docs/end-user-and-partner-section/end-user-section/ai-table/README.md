# AI Table

Com AI Table, você revisa posições extraídas, corrige colunas e salva instruções para um layout de fornecedor. Escolha a orientação adequada. Structured Output tem seu próprio guia com Padrão/Sim/Não, valores específicos, prévia e um exemplo completo.

* [Configurações e valores específicos](configuration.md)
* [Structured Output para tabelas](structured-output.md)
* [Colunas e correções](columns-and-corrections.md)
* [Instruções de IA](ai-instructions.md)
* [Tags e instruções da tabela de IA](ai-table-tags.md)
* [Explicar a extração e diagnosticar](explain-extraction.md)
* [Assistente e permissões](assistant-and-permissions.md)

## Quando você obtém a tabela de IA

* Um administrador ativou a **Extração de tabela de IA** (Configurações → Processamento de documentos → Tipos de documentos → Classificação e Extração, veja [Configurações para administradores](#configuracoes-para-administradores)). Se ela estiver desativada, a área da tabela mostra *A tabela AI será exibida aqui. Habilite em*.
* Verifique o texto legível ou a entrada Vision escolhida. Regras clássicas salvas ainda podem determinar o caminho efetivo; confirme [qual caminho foi realmente usado](../../../overview-and-basics/faq/document-processing/which-extraction-path-was-used.md).
* Cada coluna tem uma escolha Use AI de três estados. Confira também a fonte efetiva e as regras do fornecedor; Structured Output não substitui todas as tabelas baseadas em regras.

O nível de IA que lê a tabela (Fast, Full, Nexus) é definido por organização e pode ser substituído por fornecedor, veja Modelo de IA Específico do Fornecedor para Extração de Campos e Tabelas.

## A tabela de IA em resumo

<figure><img src="../../../.gitbook/assets/ai-table-overview-pt.png" alt="Tabela extraída de IA com seus cabeçalhos de coluna e quatro linhas"><figcaption><p>As duas abas, a Tabela extraída de IA e seus cabeçalhos de coluna.</p></figcaption></figure>

* **Abas.** *Tabela extraída de IA* é o que a IA leu. *Tabela extraída* é a tabela clássica, vinda de regras treinadas. A aba de IA abre por padrão quando o documento tem uma tabela de IA.
* **Cabeçalho da coluna.** Cada coluna mostra seu nome, um pequeno símbolo de **origem** (passe o mouse sobre ele: *IA · mapeamento*, *IA · sinônimo* e assim por diante indicam como a IA associou a coluna), um menu de **três pontos** e, para uma coluna mapeada, um **botão com o nome** em que você pode clicar para mudar qual coluna ela é.
* **Botões da linha.** O **x** no início de uma linha remove essa linha. Clique com o botão direito em uma linha para *Selecione como custo adicional* / *Remover como custo adicional*.
* **Barra de ferramentas do rodapé.** Os ícones na parte inferior da tela adicionam ou ocultam colunas e linhas, veja [Barra de ferramentas do rodapé](#barra-de-ferramentas-do-rodape).
* **Cartão Instruções para a IA** abaixo da tabela: prompt, colunas adicionais, **Alteração de teste**, **Aplicar**, **Salvar como treinamento**, **Excluir**, **Exportar**, veja [Dar instruções à IA](#dar-instrucoes-a-ia).

{% hint style="info" %}
Os controles de coluna só funcionam quando você pode editar o documento. Se estiverem acinzentados, o documento é somente leitura ou está bloqueado em outra sessão. Quando o banner vermelho informa que o documento está bloqueado pelo seu próprio usuário em outra sessão, **Desbloquear** assume o bloqueio.
{% endhint %}


## Configurações para administradores

Continue aqui: [Configurações e valores específicos](configuration.md).

### Usar IA por coluna

Continue aqui: [Structured Output para tabelas](structured-output.md).

<a id="escolher-a-coluna-certa-remapear"></a>
<a id="o-menu-de-três-pontos"></a>
<a id="o-menu-de-tres-pontos"></a>
<a id="barra-de-ferramentas-do-rodapé"></a>
<a id="barra-de-ferramentas-do-rodape"></a>

## Alterar uma coluna

Continue aqui: [Colunas e correções](columns-and-corrections.md).

<a id="sugerir-com-o-nexus"></a>
<a id="testar-aplicar-salvar-o-que-cada-botão-faz"></a>
<a id="testar-aplicar-salvar-o-que-cada-botao-faz"></a>

## Dar instruções à IA

Continue aqui: [Instruções de IA](ai-instructions.md).


## Ver o que a IA fez

Continue aqui: [Explicar a extração e diagnosticar](explain-extraction.md).


## Exemplos práticos

Continue aqui: [Explicar a extração e diagnosticar](explain-extraction.md).

<a id="sugerir-uma-regra-ao-seu-administrador"></a>

## O Assistente e a tabela de IA

Continue aqui: [Assistente e permissões](assistant-and-permissions.md).


## Quem pode fazer o quê

Continue aqui: [Assistente e permissões](assistant-and-permissions.md).

## Páginas relacionadas

* [Tags e instruções da tabela de IA](ai-table-tags.md)
* [Treinamento de campos de linha / Treinamento de tabelas](../../../administration-and-setup/setup/document-training/training-line-fields-table-training/README.md)
* [Touchless Intelligence](../../../administration-and-setup/touchless-intelligence.md)
