# Solução de problemas

## Não encontro o Testing em Configurações

A página só é exibida para os administradores da organização. Peça a um administrador da organização da sua organização.

## A página diz que o Testing está desativado

Um administrador da organização deve ativar **Habilitar o Testing para a organização** no alto da página.
Até lá, nada é executado, nem a partir de um assistente de IA nem de fora.

## Minha execução falhou

Abra o registro na aba **Registros** e veja a primeira etapa com falha e o seu código de erro:

| O que você vê | Normalmente significa | O que fazer |
|---|---|---|
| Um elemento não foi encontrado ou não está visível | A página é diferente na sua organização ou carrega devagar | Abra a página você mesmo e confira; ajuste o seu próprio modelo ou verifique os valores da entrada |
| Um campo ou status não corresponde | O documento tem um valor diferente do que a entrada espera | Verifique o documento; corrija o valor esperado na entrada |
| A página não pôde ser aberta | ID de documento incorreto ou falta de permissão | Verifique o ID na entrada e as permissões do usuário que iniciou a aba |
| Tempo limite excedido | A etapa ou o teste inteiro demorou demais | Execute novamente; se o problema persistir, verifique o desempenho da página |
| Bloqueado pelo ambiente | O teste grava dados em um ambiente de cliente | Confirme o início ou execute-o em um ambiente de teste |

## Minha execução está "Bloqueado"

A execução não pôde ser avaliada: algumas etapas foram ignoradas (por exemplo, uma etapa de captura de tela, que o navegador não consegue fazer)
ou falta uma confirmação. Uma execução bloqueada nunca é contada como aprovada. Remova a etapa do seu próprio modelo ou
inicie-a novamente com a confirmação.

## "Registre uma sessão do navegador para iniciar" / nenhuma aba aceita inícios

Os inícios a partir de um assistente de IA ou de fora precisam de uma aba do navegador com **Permitir inícios a partir de fora** ativado. Abra
a aba Entradas em uma aba que permaneça aberta, ative a opção e use o seu ID de sessão. Um recarregamento encerra o registro.

## A execução parou ou mostra Cancelado / Não entregue

A aba que executava o teste foi recarregada, fechada ou perdeu a conexão, ou nenhuma aba respondeu a tempo. Mantenha a aba aberta
e em primeiro plano até a execução terminar e depois inicie novamente. Um teste com uma etapa **Recarregar página** também termina assim se a página não voltar em cerca de dois minutos
(veja [Recarregar e retomar](reload-and-resume.md)).

## "Os modelos do Playwright ainda não podem ser iniciados aqui"

Os modelos cujo **Executado por** é **Playwright** são executados pela sua automação de testes. Você pode salvar entradas para eles, mas não
pode iniciá-los a partir desta página.

## Não consigo excluir um modelo

Somente os modelos próprios da sua organização (**personalizado**) podem ser excluídos. Os modelos integrados e padrão não podem; use
**Editar uma cópia** para obter a sua própria versão.
