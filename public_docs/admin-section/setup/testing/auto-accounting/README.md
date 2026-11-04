# Contabilidade Automática

Depois de configurar a contabilidade automática para o seu ambiente DocBits, é muito importante testar todas as funcionalidades para garantir um processo de entrega tranquilo.&#x20;

## Como Habilitar a Contabilidade Automática

* No Painel, vá para Configurações → Processamento de Documentos → Módulo.
* Na guia Ordem de Compra / Contabilidade Automática, você encontrará o controle deslizante para habilitar o recurso, bem como uma caixa suspensa para selecionar LN ou M3

&#x20;![](https://lh7-us.googleusercontent.com/c3aUKad-\_Wl1-wdhTGAweIe4LGsYZx5Bor8FDKAhALTm8UeO544o7w3VwDBYFSCgzzq37Jce5yKbRaQytI0nz95Ja73rLEAZHIuoTk0V7tn6q7F6Efx6pPlHll1Ek1ZItnmcnGUtgm3Y0GA8pbbshYU)

## Acessando a Contabilidade Automática

Após carregar seu documento e entrar na tela de validação, selecione o ícone a seguir para acessar a contabilidade automática.

![](https://lh7-us.googleusercontent.com/y-GgwfK7QdmuvVLGxaLhzgA-AhUNHaWfEin8iEdOFCJQE9brJzoXdIIa6B\_E0B2fXR9ahQ7ukllz\_rmI72P4Sujv0cWjEns-u0ro2EqthuwHGN8XVVnaP9or\_c3XzTQ46ZUKf84LMxvl\_yOc5BBE3qc)

Você será levado para esta tela, isso só ocorrerá se a tabela tiver sido treinada corretamente para distinguir corretamente entre os vários itens de linha.

![](https://lh7-us.googleusercontent.com/1z8qvnZJoqk2bhjah6HJ7E9Z\_Dhrmi6kTZuXAKSmXT7T-pWnI176DQbliroCPvCEIIhYYnezL5ae\_Az\_O2MWTeOTC6qZvtJ5rlThPYnKnDTIHoDIi6zsahnUuvsD7YtZROXZ4U44L2aWufBsE7QqbiA)

A partir daqui, você tem duas opções:

* Dividir a fatura usando o valor total
* Dividir a fatura por cada item de linha individual

Essa seleção é feita clicando na opção desejada

![](https://lh7-us.googleusercontent.com/Mbusr1kisZSjyU\_YJJ-8sLfwcyBOutRPUymIuuiynvEjjD1-iY\_3kACHdf9g3VcfYtHS6\_eMSFX-3RuA2Wyhq3JDjw7VsuxOijT2q9ey6DWrLzBAK7wPFXUiyapbSEK97E2Rpbop42ZAvW4zJkD-Rz4)

## Pré-requisitos

Para que o recurso de Contabilidade Automática funcione, certos dados e informações devem ser configurados. Para ajudar nesse processo ou informar sobre a configuração que está faltando, criamos um botão "Validar Configuração" que está localizado conforme mostrado abaixo.

![](https://lh7-us.googleusercontent.com/zCqiu\_\_deFqdYih9yBGQhxbgXYuBvLFhSd48k-gA9sQoxoBibeyUAEc9k9HQCnmuddIU2Bws7IfK3JCuXylCo6sCdyuUNOeUHRLGGH3Jvz5MJRJU5cmsyzrH5lTo0eH\_ygFTuXc9dI3BZ\_wW-ybzHKw)

Ao pressionar, o DocBits executará uma verificação em seu ambiente para ver se tudo está configurado corretamente.

Um menu que parecerá como a seguir aparecerá

![](https://lh7-us.googleusercontent.com/v2UhbvTVO7pw29xeRb1kjWlVq8xPmYQNeoXpUZpztcvuWdpFR01u46yRaS3rKeTIhr9k0wor46wwUcoOaOwoP49CGW5VlsLI6fd15DvfnykRC9lFJkY8RN\_Y6DlHP7t4ldPROsdCqIjgg7e3dIK5J9s)

Todos os itens com o marcador de verificação verde na frente deles significam que estão configurados e funcionando, a imagem acima deve ser usada apenas como exemplo e não deve ser seguida item por item para o seu ambiente. Isso ocorre porque cada usuário tem seu próprio conjunto de contas, dimensões e opções de dimensão conforme categorizado acima.

Divisão de Valores

Isso é feito clicando no ícone a seguir ao lado do valor total ou item de linha específico

![](https://lh7-us.googleusercontent.com/SzOTCQ8pox0UPXhlCeSLuqzeD\_gOfmFBkxzmae4Ms2JYLU\_GeQPgd5iITPiedpV12bNozVTFI8Z3cRtacEogkb5OU5OAiKJ4HV7li2HqDsZjYzES8WcCpPDWlYPjRrPfBo5LCGaxtd8uerJqUbmMQcg)

Depois de selecionar o ícone de divisão, um novo menu aparecerá abaixo do item selecionado

![](https://lh7-us.googleusercontent.com/NMyfsDFrPh7NwQNXF1FHP-oHDkBTUqoniwq48Pri7ULHiZRHuYVJ\_RTiSqt12LG1Q7ut9UTmmlQC0-y2Le5cMJ-c\_OwpWJ7s09r3kHS8I2wca75EiKfa4u2uBkYudgJ-gkEC7yK8OtweSyuqOZ2hh2Y)

Contas

O primeiro bloco do novo menu dá acesso a uma lista suspensa onde você pode selecionar uma conta/departamento de suas contas/departamentos pré-configurados para os quais deseja dividir o valor. O DocBits agrupará tipos de contas semelhantes, facilitando a localização de determinados tipos de contas ou contas relacionadas entre si.

Valores

O segundo bloco permite que você digite manualmente os valores respectivos nos quais o valor pai será dividido.

Divisão Percentual

O terceiro e último bloco permite que você insira manualmente a divisão percentual desejada para o valor pai ser dividido, o valor é automaticamente definido como 50% ao entrar no menu de divisão, mas pode ser alterado para atender às suas preferências. Se você inserir um valor percentual no bloco, o valor será calculado automaticamente no segundo bloco.

Lembre-se de que o novo valor só será calculado quando você pressionar a tecla 'Enter' em seu teclado e que os outros percentuais não são alterados por essa mudança, o que pode resultar em valores que não somam o valor pai. Por esse motivo, criamos um contador de "Valor não liquidado" neste menu, que é discutido posteriormente.

Outras Funcionalidades

Adicionar Linha

Um ícone de adição ao lado do ícone de divisão, isso pode ser usado em situações em que um valor precisa ser dividido entre mais de dois contas/departamentos.

![](https://lh7-us.googleusercontent.com/AzrPkawLROoACG3XpIpXXyRgVXa8giIkgOZ8sYc4LAHwuZRqmoiFas-oYUbR04vtPWiTPAwV\_tu-idfLG57VfaC9fvQl3Zpjdm-tNxVW7YK6-Kf-UeuYpkIenmJbQhdWfg71UezLIIG5\_4bhoSRZdtk)

Excluir Linha

Um ícone de lixeira usado para excluir linhas indesejadas ou incorretas

![](https://lh7-us.googleusercontent.com/2gAuz4KkU3xQuYZ-6w5p8T43JTJu\_aUdYfWHGBpQc\_LNPXjNu7BgN3maRgfqCzSsWyZ27j8BNn7PNzA2Tj6ZZx5T5rcJjmaFlPQZ5ioXRMoB8zSbGDawsopPoxlX2yZU\_-rh-\_D02iuzCjWDYOCJ7KE)

Valor Não Liquidado

Um indicador de "Valor não liquidado" na parte inferior em caso de algum valor não contabilizado ou valor pendente do valor pai.
![](https://lh7-us.googleusercontent.com/xZ2RqteuST79CFiKJRBDLwIBBLMa2E_vdaMmpTM3NN2qxuwCr8j208wZVHgY1Q9bg46EhRPeQpM_K1V85yIzU88D7tGRPiP3pkpzXUBv_vZbPrIM1S41ZeRcMMVW60nf5Whngnpbluw9M30bjDwcoQ0)
