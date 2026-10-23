# Contabilidade automática

Depois de configurar a contabilidade automática, teste as funcionalidades para preparar a utilização do ambiente DocBits.&#x20;

## Como ativar a contabilidade automática

* No painel, abra Configurações → Processamento de documentos → Módulo.
* No separador Pedido de compra / Contabilidade automática, ative a funcionalidade e selecione LN ou M3 na lista suspensa.

&#x20;![Página do módulo Settings com a alternância Auto accounting e a opção Auto Export if PO matched no separador Purchase Order Auto Accounting](https://lh7-us.googleusercontent.com/c3aUKad-\_Wl1-wdhTGAweIe4LGsYZx5Bor8FDKAhALTm8UeO544o7w3VwDBYFSCgzzq37Jce5yKbRaQytI0nz95Ja73rLEAZHIuoTk0V7tn6q7F6Efx6pPlHll1Ek1ZItnmcnGUtgm3Y0GA8pbbshYU)

## Aceder à contabilidade automática

Depois de carregar o documento e abrir o ecrã de validação, selecione o ícone seguinte para entrar na contabilidade automática.

![Painel de detalhes da fatura no ecrã de validação de FELLOWPRO AG com Rechnung Nr e dados de pagamento](https://lh7-us.googleusercontent.com/y-GgwfK7QdmuvVLGxaLhzgA-AhUNHaWfEin8iEdOFCJQE9brJzoXdIIa6B\_E0B2fXR9ahQ7ukllz\_rmI72P4Sujv0cWjEns-u0ro2EqthuwHGN8XVVnaP9or\_c3XzTQ46ZUKf84LMxvl\_yOc5BBE3qc)

Será apresentado o ecrã seguinte, desde que a tabela esteja treinada para distinguir corretamente os itens de linha.

![Ecrã de validação de uma fatura da FELLOWPRO mostrando onde abrir a vista de auto accounting](https://lh7-us.googleusercontent.com/1z8qvnZJoqk2bhjah6HJ7E9Z\_Dhrmi6kTZuXAKSmXT7T-pWnI176DQbliroCPvCEIIhYYnezL5ae\_Az\_O2MWTeOTC6qZvtJ5rlThPYnKnDTIHoDIi6zsahnUuvsD7YtZROXZ4U44L2aWufBsE7QqbiA)

Tem duas opções:

* Repartir a fatura pelo valor total
* Repartir a fatura por cada item de linha

Clique na opção pretendida para a selecionar.

![Ecrã de divisão da fatura com Split by total selecionado e os totais Recorded bookings e Unsettled amount abaixo](https://lh7-us.googleusercontent.com/Mbusr1kisZSjyU\_YJJ-8sLfwcyBOutRPUymIuuiynvEjjD1-iY\_3kACHdf9g3VcfYtHS6\_eMSFX-3RuA2Wyhq3JDjw7VsuxOijT2q9ey6DWrLzBAK7wPFXUiyapbSEK97E2Rpbop42ZAvW4zJkD-Rz4)

## Pré-requisitos

A contabilidade automática exige a configuração de determinados dados. O botão «Validate Setup» (validar configuração), indicado abaixo, ajuda a identificar o que está em falta.

![Ecrã de Auto accounting com os totais de Recorded bookings para uma fatura da FELLOWPRO](https://lh7-us.googleusercontent.com/zCqiu\_\_deFqdYih9yBGQhxbgXYuBvLFhSd48k-gA9sQoxoBibeyUAEc9k9HQCnmuddIU2Bws7IfK3JCuXylCo6sCdyuUNOeUHRLGGH3Jvz5MJRJU5cmsyzrH5lTo0eH\_ygFTuXc9dI3BZ\_wW-ybzHKw)

Ao clicar, o DocBits verifica se o ambiente está configurado corretamente.

Aparecerá um menu semelhante ao seguinte.

![Resultados da configuração do Validate listando as verificações de chart of accounts, dimensions e dimensions options com as respetivas colunas necessárias](https://lh7-us.googleusercontent.com/v2UhbvTVO7pw29xeRb1kjWlVq8xPmYQNeoXpUZpztcvuWdpFR01u46yRaS3rKeTIhr9k0wor46wwUcoOaOwoP49CGW5VlsLI6fd15DvfnykRC9lFJkY8RN\_Y6DlHP7t4ldPROsdCqIjgg7e3dIK5J9s)

Os elementos com marca de verificação verde estão configurados e operacionais. A imagem é apenas um exemplo: não copie as configurações item a item, porque cada organização tem contas, dimensões e opções de dimensão próprias.

Repartir valores

Clique no ícone seguinte, junto ao total ou ao item de linha específico.

![Itens de configuração do Auto accounting com marcas de verificação verdes, as linhas Position, Accounts e Amount e o total Recorded bookings](https://lh7-us.googleusercontent.com/SzOTCQ8pox0UPXhlCeSLuqzeD\_gOfmFBkxzmae4Ms2JYLU\_GeQPgd5iITPiedpV12bNozVTFI8Z3cRtacEogkb5OU5OAiKJ4HV7li2HqDsZjYzES8WcCpPDWlYPjRrPfBo5LCGaxtd8uerJqUbmMQcg)

Ao selecionar o ícone de repartição, aparece um novo menu por baixo do item.

![Menu Split amounts mostrando as colunas Position, Accounts e Amount com as linhas Total e Unsettled amount](https://lh7-us.googleusercontent.com/NMyfsDFrPh7NwQNXF1FHP-oHDkBTUqoniwq48Pri7ULHiZRHuYVJ\_RTiSqt12LG1Q7ut9UTmmlQC0-y2Le5cMJ-c\_OwpWJ7s09r3kHS8I2wca75EiKfa4u2uBkYudgJ-gkEC7yK8OtweSyuqOZ2hh2Y)

Contas

O primeiro bloco tem uma lista suspensa para selecionar as contas ou departamentos previamente configurados pelos quais pretende repartir o valor. O DocBits agrupa tipos de conta semelhantes para facilitar a pesquisa.

Valores

O segundo bloco permite introduzir manualmente os valores em que o montante original será repartido.

Repartição por percentagem

O terceiro bloco permite introduzir a percentagem de repartição. O valor inicial é 50%, mas pode alterá-lo. Quando introduz uma percentagem, o montante correspondente é calculado no segundo bloco.

O novo montante só é calculado depois de premir Enter. As outras percentagens não são alteradas automaticamente, pelo que a soma pode diferir do montante original. O indicador «Unsettled amount» (valor por repartir), descrito adiante, ajuda a detetar a diferença.

Outras funcionalidades

Adicionar linha

O ícone de adição, junto ao ícone de repartição, permite repartir um montante por mais de duas contas ou departamentos.

![Tabela de divisão de montantes com as entradas Position, Accounts e Amount mais os contadores Recorded bookings e Unsettled amount](https://lh7-us.googleusercontent.com/AzrPkawLROoACG3XpIpXXyRgVXa8giIkgOZ8sYc4LAHwuZRqmoiFas-oYUbR04vtPWiTPAwV\_tu-idfLG57VfaC9fvQl3Zpjdm-tNxVW7YK6-Kf-UeuYpkIenmJbQhdWfg71UezLIIG5\_4bhoSRZdtk)

Eliminar linha

O ícone de caixote do lixo elimina linhas incorretas ou desnecessárias.

![Tabela de divisão com duas linhas adicionadas de 50 por cento cada e os totais Recorded bookings e Unsettled amount](https://lh7-us.googleusercontent.com/2gAuz4KkU3xQuYZ-6w5p8T43JTJu\_aUdYfWHGBpQc\_LNPXjNu7BgN3maRgfqCzSsWyZ27j8BNn7PNzA2Tj6ZZx5T5rcJjmaFlPQZ5ioXRMoB8zSbGDawsopPoxlX2yZU\_-rh-\_D02iuzCjWDYOCJ7KE)

Valor por repartir

O indicador «Unsettled amount» na parte inferior apresenta qualquer valor do montante original ainda por repartir.

![Tabela de divisão contabilística com as colunas Position, Accounts e Amount e o indicador Unsettled amount abaixo](https://lh7-us.googleusercontent.com/xZ2RqteuST79CFiKJRBDLwIBBLMa2E\_vdaMmpTM3NN2qxuwCr8j208wZVHgY1Q9bg46EhRPeQpM\_K1V85yIzU88D7tGRPiP3pkpzXUBv\_vZbPrIM1S41ZeRcMMVW60nf5Whngnpbluw9M30bjDwcoQ0)
