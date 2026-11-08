# O ecrã de erro de uma fatura eletrónica rejeitada

> Nesta versão, alguns textos da interface podem ainda estar em inglês ou ter traduções incorretas. A documentação explica o significado; as capturas mostram a interface sem alterações.

Quando carrega uma fatura eletrónica incorreta, o DocBits não a perde. O documento fica com o estado **Error** e o ecrã de erro diz-lhe o que está errado, onde, e o que fazer a seguir. Esta página mostra dois exemplos: um ficheiro XML que não está bem formado e uma fatura que viola uma regra de negócio.

> Uma fatura só fica com o estado **Error** quando a validação está **ativada** e em **bloqueio** para o seu tipo de documento. Ver [Validação para cada tipo de documento](validation-per-document-type.md).

## Exemplo 1: o ficheiro XML está danificado

Um fornecedor envia um ficheiro XML em que uma etiqueta de fecho não corresponde à etiqueta de abertura. O ficheiro não pode ser lido, por isso o DocBits para na primeira verificação, **L1 · Well-formedness**.

<figure><img src="../../../../../.gitbook/assets/einvoice-error-xml-malformed-pt.png" alt="Ecrã de erro de um XML fictício com uma etiqueta de fecho danificada intencionalmente. Nesta versão, alguns textos da interface podem ainda estar em inglês ou ter traduções incorretas. A documentação explica o significado; as capturas mostram a interface sem alterações."><figcaption><p>Ecrã de erro de um XML fictício com uma etiqueta de fecho danificada intencionalmente. Nesta versão, alguns textos da interface podem ainda estar em inglês ou ter traduções incorretas. A documentação explica o significado; as capturas mostram a interface sem alterações.</p></figcaption></figure>

O ecrã tem dois lados:

* **Esquerda: o ficheiro XML.** O DocBits mostra o ficheiro com números de linha. A linha com o problema está marcada a vermelho. Use os botões acima do ficheiro para copiar o XML ou abri-lo num novo separador.
* **Direita: a explicação.** O cartão **Rejected by** indica a verificação que parou o ficheiro (aqui **L1 · Well-formedness**) e o código da regra (aqui `XML-PARSE`). Abaixo vê um título em linguagem simples (*O XML não está bem formado*), uma explicação curta e o bloco **Next step**.

Selecione **View validation details** para abrir o [relatório de validação](validation-report.md) completo.

<figure><img src="../../../../../.gitbook/assets/einvoice-report-xml-malformed-pt.png" alt="Relatório do ficheiro danificado: um erro no nível 1 Sintaxe, com a mensagem técnica e a posição"><figcaption><p>Relatório do ficheiro danificado: um erro no nível 1 Sintaxe, com a mensagem técnica e a posição</p></figcaption></figure>

O relatório indica a posição exata (aqui a linha 5, a coluna 4081) e dá a mensagem técnica do analisador de XML. Selecione **Show in XML** para saltar para essa linha. A dica **How to fix** diz-lhe para pedir ao remetente um ficheiro corrigido.

## Exemplo 2: a fatura viola uma regra de negócio

O XML está correto, mas falta um campo obrigatório. Por exemplo, o vendedor não pode ser identificado porque não existe identificador do vendedor, identificador de registo nem identificador de IVA (regra `BR-CO-26`).

<figure><img src="../../../../../.gitbook/assets/einvoice-error-view-pt.png" alt="Ecrã de erro de uma fatura de exemplo inteiramente fictícia: a camada L3 · Business Rules, o código da regra e um passo seguinte"><figcaption><p>Ecrã de erro de uma fatura de exemplo inteiramente fictícia: a camada L3 · Business Rules, o código da regra e um passo seguinte</p></figcaption></figure>

O cartão indica a camada **L3 · Business Rules** e o código `BR-CO-26`. O relatório enumera todos os resultados da fatura, consulte [Relatório de validação](validation-report.md).

## Os botões por baixo do cartão

| Botão | O que faz |
| --- | --- |
| **Restart Processing** | Executa de novo o processamento do documento, por exemplo depois de alterar uma definição. A verificação usa as definições atuais. |
| **View DocFlow** | Mostra o fluxo de trabalho do documento. |
| **Copy Details** | Copia os detalhes do erro, por exemplo para uma mensagem ao seu administrador. |
| **Create ticket** | Abre um pedido de suporte com os detalhes do erro. |

Selecione **Show technical details** no cartão para ver a informação técnica em bruto.

## O que fazer a seguir

* **Erros:** peça ao remetente uma fatura corrigida ou [rejeite o documento](validation-next-step-and-reject.md). Uma fatura corrigida é um novo documento.
* **Apenas avisos:** o documento não fica bloqueado. Pode continuar.

## Páginas relacionadas

* [Relatório de validação](validation-report.md): todos os resultados, nível a nível.
* [Próximo passo e rejeitar um documento](validation-next-step-and-reject.md)
* [Validação para cada tipo de documento](validation-per-document-type.md): ative a validação e defina o bloqueio.
