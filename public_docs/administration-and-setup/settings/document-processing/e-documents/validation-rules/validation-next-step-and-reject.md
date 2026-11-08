# Próximo passo e rejeitar um documento

> Nesta versão, alguns textos da interface podem ainda estar em inglês ou ter traduções incorretas. A documentação explica o significado; as capturas mostram a interface sem alterações.

Depois de ler o [relatório de validação](validation-report.md), o relatório diz-lhe o que fazer. Também pode rejeitar o documento.

## O que fazer a seguir

<figure><img src="../../../../../.gitbook/assets/einvoice-report-next-step-pt.png" alt="Avaliação, próximo passo e ações do relatório."><figcaption><p>Avaliação, próximo passo e ações do relatório.</p></figcaption></figure>

A **Assessment** diz numa frase se a fatura está em conformidade. O bloco **Next step** diz-lhe o que fazer:

| Resultado | Próximo passo |
| --- | --- |
| Pelo menos um **erro** | Peça ao remetente uma fatura corrigida, ou rejeite o documento. Uma fatura corrigida é um novo documento. |
| Apenas **avisos** | Pode continuar com o documento. |

Os botões no fim do relatório:

* **Reject document**: abre o diálogo de rejeição (ver abaixo).
* **Report (HTML)** e **Report (XML)**: transferem o relatório, por exemplo para o enviar ao fornecedor.
* **Close** (ou **Back to document**): volta ao documento.

## Rejeitar um documento

<figure><img src="../../../../../.gitbook/assets/einvoice-reject-dialog-pt.png" alt="Diálogo de rejeição da fatura fictícia. A rejeição foi cancelada."><figcaption><p>Diálogo de rejeição da fatura fictícia. A rejeição foi cancelada.</p></figcaption></figure>

1. No relatório, selecione **Reject document**.
2. Verifique o **Reason**. O DocBits preenche-o a partir dos erros do relatório. Pode editar o texto.
3. Selecione **Reject document** para confirmar. O estado muda para **Rejected**. O motivo é guardado como nota e o relatório permanece ligado ao documento.

Selecione **Cancel** para deixar o documento como está.

> Só os utilizadores com permissão para editar documentos veem **Reject document**. O botão fica oculto quando o documento já está rejeitado ou concluído.
