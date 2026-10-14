# Painel

O **Workflow Dashboard** é a página inicial da área de workflows. Ele mostra o desempenho dos seus workflows — totais de execuções, taxas de sucesso e falha, um gráfico de execuções ao longo do tempo e a atividade recente — e dá acesso à lista de workflows, ao gerenciador de testes e ao Card SDK.

<figure><img src="../../.gitbook/assets/workflow_dashboard.png" alt="Workflow Dashboard com totais de execuções, taxas de sucesso e falha, o gráfico de execuções e a atividade recente"><figcaption><p>O Workflow Dashboard — totais de execuções, taxas de sucesso/falha e atividade recente de cada workflow.</p></figcaption></figure>

## Abas

- **Dashboard** — métricas de execução e atividade recente (mostrados acima).
- **Workflow List** — todos os workflows com tipo, ordem de execução e gatilho. Crie um novo com **New Workflow**.
- **Test Manager List** — cenários de teste que validam seus workflows; execute-os com **Run All Tests**.
- **License** — informações de licenciamento dos workflows.
- **Card SDK** — crie e envie cartões de workflow personalizados (consulte [Card SDK](card-sdk.md)).

A barra de ferramentas também oferece **Templates**, que abre a biblioteca de [Modelos de workflow](standard-workflow-builder.md#workflow-templates), e **Import Workflow**, que importa um workflow a partir de um arquivo JSON.

O **Test Manager** permite salvar cenários de teste por workflow e executá-los em conjunto, para confirmar que seus workflows continuam se comportando corretamente após alterações:

<figure><img src="../../.gitbook/assets/workflow_test_manager.png" alt="Workflow Test Manager List com cenários de teste e Run All Tests"><figcaption><p>A Test Manager List — cada cenário mostra um resultado de aprovação/reprovação; use <strong>Run All Tests</strong> para executar todos novamente.</p></figcaption></figure>

## Próximos passos

- Crie uma automação linear com o construtor **Standard Workflow**.
- Crie um fluxo com ramificações com o construtor **Advanced Workflow**.
