# Validação e Testes

Antes de confiar num Advanced Workflow, utilize os controlos da barra de ferramentas para confirmar que está correto e se comporta como esperado.

## Validate

Clique no controlo **Validate** (o ícone de círculo com visto, ou prima <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>V</kbd>). A validação verifica o grafo à procura de problemas — nós não ligados, configuração em falta e ligações inválidas — para que os possa corrigir antes de o fluxo de trabalho ser executado em documentos reais.

## Test

Clique no controlo **Test** (o ícone de reprodução, ou prima <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>T</kbd>) para executar o fluxo de trabalho sobre uma amostra e ver como se comporta, sem afetar documentos ativos.

## Cenários de teste

Para verificações repetíveis, guarde **cenários de teste** no **Test Manager** (consulte o [Painel](../workflow-dashboard.md)). Cada cenário regista um resultado esperado e mostra um resultado de aprovação/reprovação, e **Run All Tests** executa-os novamente em conjunto — para que possa confirmar que os seus fluxos de trabalho continuam a comportar-se corretamente após uma alteração.

<figure><img src="../../../.gitbook/assets/workflow_test_manager.png" alt="Lista do Workflow Test Manager com cenários de teste e Run All Tests"><figcaption><p>O Test Manager — cenários guardados com resultados de aprovação/reprovação e **Run All Tests**.</p></figcaption></figure>

## Próximos passos

- Reveja os tipos de nó e as ligações em [Nós](nodes.md).
- Veja todos os controlos da barra de ferramentas e da tela em [Barra de ferramentas e Tela](toolbar-and-canvas.md).
