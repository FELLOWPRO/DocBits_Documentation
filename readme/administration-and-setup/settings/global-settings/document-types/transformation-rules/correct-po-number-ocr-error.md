# Corrigir um erro de OCR num número de encomenda

O terceiro caráter de `06O123` é a **letra O**. Se a extração produzir `060123`, utilize uma transformação condicional de prefixo para corrigir este padrão conhecido sem um script personalizado.

## Configurar a correção do prefixo

1. Abra **Definições → Tipos de documento → roda dentada → Regras de transformação → Gerir regras de transformação**. Um administrador da organização tem de ativar a função para o tipo selecionado.
2. Crie uma regra de **campo de cabeçalho** com **Número de encomenda (`Purchase Order`)** como destino. Leia do **próprio campo**.
3. Na execução condicional, selecione o número de encomenda, **começa por** e `060`.
4. Remova o passo inicial de remoção de espaços. Adicione **Afixo → Remover prefixo → `060`**, seguido de **Afixo → Adicionar prefixo → `06O`**. Introduza a letra O maiúscula no segundo passo. A condição limita ambos os passos ao prefixo afetado; os restantes caracteres mantêm-se.
5. Verifique a pré-visualização, guarde a regra e volte a abri-la. Teste um documento, guarde-o e volte a carregá-lo para verificar o número de encomenda persistido.

## Verificar o resultado

| Entrada de exemplo | Resultado esperado | Motivo |
| --- | --- | --- |
| `060123` | `06O123` | Prefixo afetado |
| `060987` | `06O987` | Outro valor afetado; sufixo preservado |
| `06O123` | `06O123` | Já está correto; a condição não corresponde |
| `160123` | `160123` | Prefixo diferente; a condição não corresponde |
| `1060123` | `1060123` | `060` no interior do valor não é um prefixo correspondente |

Este exemplo corrige um padrão de extração conhecido. Não comprova a precisão do OCR, a existência da encomenda nem o sucesso da correspondência. Utilize a regra apenas quando a convenção de numeração exigir `06O`: também seria alterado um prefixo `060` legítimo. Adicione condições de fornecedor se a convenção se aplicar apenas a determinados fornecedores.

## Porquê dois passos de afixo?

O editor atual exige um campo de origem separado para passos dependentes da posição, como **Localizar e substituir**, mesmo com **Executar apenas uma vez por documento** ativo. Os dois passos do prefixo funcionam no mesmo campo. Após a correção, o valor já não começa por `060`, pelo que a condição impede novas alterações nos próximos guardamentos.
