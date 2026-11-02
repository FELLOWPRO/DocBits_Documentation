# Validação e Testes

Enquanto constrói um Advanced Workflow, dois controlos na barra de ferramentas permitem-lhe verificá-lo sem sair do construtor. Estes destinam-se a *verificações rápidas durante a construção* — para testes guardados e repetíveis, use o [Test Manager](../test-manager.md).

## Validate

Clique no controlo **Validate** (o ícone de círculo de verificação, ou prima <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>V</kbd>). A validação verifica o grafo em busca de problemas — nós não ligados, configuração em falta e ligações inválidas — e assinala-os para que os possa corrigir antes de o fluxo de trabalho ser executado em documentos reais.

## Test

Clique no controlo **Test** (o ícone de reprodução, ou prima <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>T</kbd>) para executar o fluxo atual contra uma amostra e observar o seu comportamento, sem afetar documentos em produção. Esta é a forma mais rápida de verificar uma alteração que acabou de fazer na tela.

## Quando usar qual

- **Validate / Test no construtor** (esta página) — feedback instantâneo enquanto desenha o fluxo.
- **[Test Manager](../test-manager.md)** — guarde o cenário para o poder voltar a executar mais tarde (e em conjunto com todos os seus outros cenários) para detetar regressões após alterações futuras.

## Próximos passos

- Reveja os tipos de nós e ligações em [Nós](nodes.md).
- Veja todos os controlos da barra de ferramentas e da tela em [Barra de ferramentas e Tela](toolbar-and-canvas.md).
