# Relatório de validação

> Nesta versão, alguns textos da interface podem ainda estar em inglês ou ter traduções incorretas. A documentação explica o significado; as capturas mostram a interface sem alterações.

Quando o DocBits rejeita uma fatura eletrónica, pode ler exatamente porquê. O **relatório de validação** lista cada resultado em linguagem simples, diz-lhe o que corrigir e mostra o próximo passo. Abre-o a partir do documento, não das definições. O ecrã onde o encontra está descrito em [O ecrã de erro de uma fatura eletrónica rejeitada](validation-error-screen.md).

Esta página é para quem processa faturas. Os administradores definem as regras na página [Validação de faturas eletrónicas](./) e escolhem, por tipo de documento, se uma verificação falhada bloqueia a fatura, ver [Validação para cada tipo de documento](validation-per-document-type.md).

## Quando um documento fica com erro

Se a validação estiver **ativada** e em **bloqueio** para o tipo de documento, uma fatura com um resultado bloqueante fica com o estado **Error**. Uma fatura rejeitada pelo próprio validador tem, em vez disso, o estado dedicado de validação de e-invoice, ver [O ecrã de erro de uma fatura eletrónica rejeitada](validation-error-screen.md). Abra o documento no painel. A vista de erro mostra o XML à esquerda e o motivo à direita.

<figure><img src="../../../../../.gitbook/assets/einvoice-error-view-pt.png" alt="Ecrã de erro de uma fatura de exemplo inteiramente fictícia. Nesta versão, alguns textos da interface podem ainda estar em inglês ou ter traduções incorretas. A documentação explica o significado; as capturas mostram a interface sem alterações."><figcaption><p>Ecrã de erro de uma fatura de exemplo inteiramente fictícia. Nesta versão, alguns textos da interface podem ainda estar em inglês ou ter traduções incorretas. A documentação explica o significado; as capturas mostram a interface sem alterações.</p></figcaption></figure>

O cartão à direita indica a camada que rejeitou a fatura (por exemplo **L3 · Business Rules**), o código da regra (por exemplo `BR-CO-26`), uma explicação curta e um **Next step**. Selecione **View validation details** para abrir o relatório completo.

## Ler o relatório

<figure><img src="../../../../../.gitbook/assets/einvoice-report-top-pt.png" alt="Relatório da fatura fictícia com os dados do ficheiro e o resultado."><figcaption><p>Relatório da fatura fictícia com os dados do ficheiro e o resultado.</p></figcaption></figure>

O relatório começa com os factos sobre o ficheiro:

| Campo | O que mostra |
| --- | --- |
| **Reference** | O nome do ficheiro da fatura. |
| **Time of check** | Quando o DocBits executou a verificação. Um relatório guardado não muda depois. |
| **Document type / profile** | O formato da fatura, por exemplo CII e EN 16931. |
| **Rule sets** | A versão dos conjuntos de regras que o DocBits usou. |
| **Seller** | O vendedor, lido do XML. |
| **Number / date** | O número e a data da fatura, lidos do XML. |

Abaixo dos dados do ficheiro vê o **veredicto**, por exemplo **Not conformant**, com o número de erros, avisos e mensagens de informação. Se a sua organização alterou a gravidade de uma regra, uma segunda linha **Organisation severity** mostra as contagens segundo as definições da sua organização.

> O veredicto apresenta **Rejected** em vez de uma palavra de conformidade quando o documento foi rejeitado na validação de e-invoice, e o veredicto passa então a ter um ícone de cancelamento. O passo seguinte remete para a lista de erros. Um relatório cujo resultado não é legível nunca apresenta a fatura como conforme.

### Resultado por nível

A tabela **Result per level** mostra quantos erros, avisos e mensagens de informação cada verificação encontrou. As verificações assentam umas nas outras:

| Nível | O que verifica |
| --- | --- |
| **1 Syntax** | O XML está bem formado. |
| **2 Schema** | A estrutura segue o esquema XML oficial. |
| **3 Business rules** | Os campos obrigatórios estão presentes e corretos (regras `BR-…`). |
| **4 Cross-check rules** | Os campos são coerentes entre si, por exemplo os totais. |
| **5 CIUS rules (XRechnung)** | As regras alemãs adicionais do XRechnung. |
| **Other rules** | Outras regras, por exemplo as regras PEPPOL. |
| **Value checks of DocBits** | Verificações que o DocBits acrescenta, por exemplo IBAN e IVA. |

> Nas faturas com perfil EN 16931 ou EXTENDED, as regras específicas do XRechnung aparecem como **avisos**, não como erros.

## Os resultados

<figure><img src="../../../../../.gitbook/assets/einvoice-report-findings-pt.png" alt="Cada resultado tem um código, um nível, um texto legível e uma indicação de como corrigir"><figcaption><p>Cada resultado tem um código, um nível, um texto legível e uma indicação de como corrigir</p></figcaption></figure>

Cada resultado é uma linha:

* **Pos** e **Code**: a posição no relatório e o código da regra, por exemplo `BR-CO-26`.
* **Level**: **Error**, **Warning** ou **Information**.
* **Your organisation**: o nível segundo as definições da sua organização. Um traço significa que a sua organização não alterou o nível.
* **Field and text**: o problema em linguagem simples, o campo a que diz respeito (por exemplo *BT-29*), a mensagem técnica do validador e **How to fix**.
* **Line** e **Show in XML**: selecione **Show in XML** para fechar o relatório e saltar para a linha no visualizador de XML.

O DocBits tem textos em linguagem simples para as regras mais comuns. Para uma regra sem esse texto, o relatório mostra a mensagem técnica do validador.

## Trabalhar com um relatório longo

Uma fatura pode violar muitas regras ao mesmo tempo. O relatório mantém o veredicto e as contagens num cabeçalho fixo enquanto as conclusões deslizam, para que veja sempre quanto vale a fatura inteira.

* **Filtrar por nível.** Os botões de filtro acima das conclusões reduzem a lista a erros, avisos ou mensagens informativas. As linhas **Result per level** também funcionam como filtro: selecione um nível para ver apenas as suas conclusões.
* **Pesquisar.** Um campo de pesquisa filtra a lista aberta por texto, por exemplo um código de regra, um nome de campo ou uma palavra da mensagem.
* **Expandir e recolher.** As conclusões abrem sozinhas quando são erros ou quando o relatório tem no máximo três linhas. Use as ações de expandir e recolher para toda a lista; cada linha também abre individualmente.
* **Copiar um código ou um XPath.** As conclusões têm uma ação de cópia para o código da regra e para o XPath do elemento com erro, por exemplo para uma mensagem ao seu administrador.
* **Abrir os detalhes quando precisar.** Os detalhes do documento começam recolhidos. Os detalhes técnicos, como o número de verificação e o XPath, ficam na conclusão, enquanto a linha em si mostra o nome compreensível da verificação e o código da regra como referência.
* **Voltar ao seu lugar.** Quando seleciona **Show in XML** e abre o relatório de novo, as linhas abertas, o filtro e a posição de deslocamento ficam como os deixou.
* **Transferir ou imprimir.** A ação **Download** no rodapé do relatório oferece impressão e um PDF, além dos ficheiros HTML e XML do relatório. O nome do ficheiro, a data de exportação e o número de página aparecem no PDF.
* **Rejeitar a partir do relatório.** A ação de rejeição fica à esquerda no rodapé, separada da ação de transferência, para não rejeitar uma fatura enquanto procura o PDF.

Num ecrã estreito, por exemplo num telemóvel, cada conclusão passa a ser um cartão em vez de uma linha.

## A seguir

* [Próximo passo e rejeitar um documento](validation-next-step-and-reject.md): o que fazer depois de ler o relatório.

## Páginas relacionadas

* [Validação de faturas eletrónicas](./): versões aceites, perfis e a gravidade de cada regra.
* [Validação para cada tipo de documento](validation-per-document-type.md): ative a validação e defina o bloqueio.
* [Encaminhamento de notificações](../notification-routing.md): quem trata cada resultado.
