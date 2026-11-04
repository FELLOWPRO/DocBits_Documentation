# O ecrã de erro de uma fatura eletrónica rejeitada

> Nesta versão, alguns textos da interface podem ainda estar em inglês ou ter traduções incorretas. A documentação explica o significado; as capturas mostram a interface sem alterações.

Quando carrega uma fatura eletrónica incorreta, o DocBits não a perde. O documento fica com o estado **Erro** e o ecrã de erro diz-lhe o que está errado, onde, e o que fazer a seguir. Esta página mostra dois exemplos: um ficheiro XML que não está bem formado e uma fatura que viola uma regra de negócio.

> Uma fatura só fica com o estado **Erro** quando a validação está **ativada** e em **bloqueio** para o seu tipo de documento. Ver [Validação para cada tipo de documento](validation-per-document-type.md).

## Exemplo 1: o ficheiro XML está danificado

Um fornecedor envia um ficheiro XML em que uma etiqueta de fecho não corresponde à etiqueta de abertura. O ficheiro não pode ser lido, por isso o DocBits para na primeira verificação, **L1 · Bem-formado**.

<figure><img src="../../../../.gitbook/assets/einvoice-error-xml-malformed-pt-20261104-v2.png" alt="Ecrã de erro de um XML fictício com uma etiqueta de fecho danificada intencionalmente. Nesta versão, alguns textos da interface podem ainda estar em inglês ou ter traduções incorretas. A documentação explica o significado; as capturas mostram a interface sem alterações."><figcaption><p>Ecrã de erro de um XML fictício com uma etiqueta de fecho danificada intencionalmente. Nesta versão, alguns textos da interface podem ainda estar em inglês ou ter traduções incorretas. A documentação explica o significado; as capturas mostram a interface sem alterações.</p></figcaption></figure>

O ecrã tem dois lados:

* **Esquerda: o ficheiro XML.** O DocBits mostra o ficheiro com números de linha. A linha com o problema está marcada a vermelho. Use os botões acima do ficheiro para copiar o XML ou abri-lo num novo separador.
* **Direita: a explicação.** O cartão **Rejeitado por** indica a verificação que parou o ficheiro (aqui **L1 · Bem-formado**) e o código da regra (aqui `XML-PARSE`). Abaixo vê um título em linguagem simples (*O XML não está bem formado*), uma explicação curta e o bloco **Próximo passo**.

Selecione **Ver detalhes da validação** para abrir o [relatório de validação](validation-report.md) completo.

<figure><img src="../../../../.gitbook/assets/einvoice-report-xml-malformed-pt-20261104-v2.png" alt="Relatório do ficheiro XML fictício danificado."><figcaption><p>Relatório do ficheiro XML fictício danificado.</p></figcaption></figure>

O relatório indica a posição exata (a linha e a coluna constam do relatório) e dá a mensagem técnica do analisador de XML. Selecione **Mostrar em XML** para saltar para essa linha. A dica **Como corrigir** diz-lhe para pedir ao remetente um ficheiro corrigido.

## Exemplo 2: a fatura viola uma regra de negócio

O XML está correto, mas falta um campo obrigatório. Por exemplo, o vendedor não pode ser identificado porque não existe identificador do vendedor, identificador de registo nem identificador de IVA (regra `BR-CO-26`).

<figure><img src="../../../../.gitbook/assets/einvoice-error-view-pt-20261104-v2.png" alt="Ecrã de erro de uma fatura de exemplo inteiramente fictícia. Nesta versão, alguns textos da interface podem ainda estar em inglês ou ter traduções incorretas. A documentação explica o significado; as capturas mostram a interface sem alterações."><figcaption><p>Ecrã de erro de uma fatura de exemplo inteiramente fictícia. Nesta versão, alguns textos da interface podem ainda estar em inglês ou ter traduções incorretas. A documentação explica o significado; as capturas mostram a interface sem alterações.</p></figcaption></figure>

O cartão mostra o primeiro resultado bloqueante. O relatório completo também inclui o código `BR-CO-26` e os restantes resultados da fatura.

## Os botões por baixo do cartão

| Botão | O que faz |
| --- | --- |
| **Reiniciar processamento** | Executa de novo o processamento do documento, por exemplo depois de alterar uma definição. A verificação usa as definições atuais. |
| **Ver DocFlow** | Mostra o fluxo de trabalho do documento. |
| **Copiar detalhes** | Copia os detalhes do erro, por exemplo para uma mensagem ao seu administrador. |
| **Criar pedido de suporte** | Abre um pedido de suporte com os detalhes do erro. |

Selecione **Mostrar detalhes técnicos** no cartão para ver a informação técnica em bruto.

## O que fazer a seguir

* **Erros:** peça ao remetente uma fatura corrigida ou [rejeite o documento](validation-next-step-and-reject.md). Uma fatura corrigida é um novo documento.
* **Apenas avisos:** o documento não fica bloqueado. Pode continuar.

## Páginas relacionadas

* [Relatório de validação](validation-report.md): todos os resultados, nível a nível.
* [Próximo passo e rejeitar um documento](validation-next-step-and-reject.md)
* [Validação para cada tipo de documento](validation-per-document-type.md): ative a validação e defina o bloqueio.
