# Appearance

O **Appearance** permite a um administrador dar à cópia do DocBits da organização um aspeto próprio: cores, raio dos cantos, densidade e tipo de letra. Todos os membros da organização veem o resultado — em modo claro e escuro — após o próximo recarregamento. Nunca altera o layout nem o que uma funcionalidade faz, apenas a forma como é desenhada.

> **Acesso:** o Appearance é uma página exclusiva para administradores. Abra **Settings → Organization & Access → Appearance**.

<!-- screenshot: /settings/appearance light -->

## Quem pode alterá-lo

Apenas os administradores da organização podem abrir **Settings → Appearance** e guardar ou repor um tema. Todos os outros membros da organização veem apenas o resultado.

## O que existe na página

A página divide-se num editor à esquerda e numa pré-visualização em direto à direita.

| Área | O que contém |
|---|---|
| **General** | O nome do tema, o tipo de letra, o raio dos cantos e a densidade. |
| **Colors** | Os separadores Light e Dark, um seletor de cor mais um campo hexadecimal por cor, agrupados em Surfaces, Brand, Neutrals, Status e Charts. Um painel «Derived colours» só de leitura por baixo mostra as cores que o DocBits calcula para si (estados de hover, anéis de foco e semelhantes) a partir das cores acima. |
| **Advanced overrides** | Uma linha `--token: value` por entrada, para o caso raro de os controlos de cor, raio, densidade e tipo de letra acima não serem suficientes — ver [Advanced overrides](#advanced-overrides). |

### Alterar cores

Cada cor tem uma amostra (clique nela para abrir o seletor de cores do navegador) e ao lado um campo hexadecimal onde pode escrever ou colar. Deixe uma cor vazia para manter a predefinição do DocBits para esse token — a amostra mostra então um contorno tracejado. Alterne entre os separadores **Light** / **Dark** acima da lista de cores para definir o outro modo; uma cor que não definir no modo escuro mantém a sua própria predefinição do DocBits para escuro e não copia o valor claro.

{% hint style="info" %}
As cores são introduzidas em hexadecimal (`#2388ae` ou `#2388aeaa` com alfa). Não existe introdução por nome de cor nem `rgb()`.
{% endhint %}

### Raio dos cantos, densidade e tipo de letra

* **Corner radius** — `None`, `Small`, `Medium` (predefinido), `Large` ou `Extra large`. Controla o arredondamento de cartões, botões, campos de entrada e caixas de diálogo em toda a aplicação.
* **Density** — `Compact`, `Comfortable` (predefinido) ou `Spacious`. Controla a altura de botões, campos de entrada e linhas de tabela, e o tamanho base do texto.
* **Font** — uma lista curta de tipos de letra incluídos (Geist é o predefinido do DocBits; também Inter, Roboto, IBM Plex Sans, Source Sans 3, Nunito Sans, Manrope, Kanit, ou o tipo de letra do sistema do visitante). Todos os tipos de letra já estão incluídos, não há nada para carregar.

### Advanced overrides

Para um design token que os controlos acima não expõem diretamente (por exemplo, uma altura específica de linha de tabela), adicione uma linha em **Advanced overrides**:

```
--table-row-h: 30px
```

Uma sobreposição por linha, `--token: value`. Uma linha inválida — um token desconhecido, um token que não pode ser personalizado ou um valor que não se adequa ao que o token espera — é apresentada como erro por baixo da caixa e não é aplicada; tudo o resto na página é guardado normalmente.

## Pré-visualização

Cada alteração atualiza imediatamente o painel **Preview** à direita, sem afetar o que os outros veem — nunca toca na aplicação em execução nem no tema guardado. A pré-visualização tem separadores próprios: uma visão geral com claro e escuro lado a lado e, depois, páginas dedicadas a botões, campos de formulário, superfícies e indicadores de estado, para poder verificar o contraste e a legibilidade nas partes da interface mais sensíveis à cor.

<!-- screenshot: /settings/appearance dark -->

Se uma alteração tornar o tema inválido (ver abaixo), a pré-visualização continua a mostrar a última versão válida em vez de falhar.

## Guardar e repor

* **Save** grava o tema para toda a organização. Fica desativado até algo ter mudado realmente e o tema ser válido.
* **Reset** pede confirmação e depois remove completamente o tema da organização e devolve todos ao tema predefinido do DocBits. Isto não pode ser anulado a partir da página — as cores têm de ser introduzidas novamente à mão (ou reimportadas, ver abaixo) se a organização as quiser de volta.
* Um guardar ou repor que falhe (por exemplo, por um problema de validação) apresenta o problema acima do editor e deixa a página como estava; nada é aplicado.

Não existem verificações de contraste antes de guardar — ver [Dicas](#dicas) abaixo.

## Exportar e importar

* **Export** descarrega o tema atualmente apresentado no editor (guardado ou não) como ficheiro `.json`, com o nome do tema.
* **Import** lê um ficheiro de tema `.json` e carrega-o no editor. Ainda tem de ser revisto e guardado para produzir efeito — a importação por si só não altera o que alguém vê. Um ficheiro inválido ou demasiado grande (mais de 32 KB) é rejeitado com um erro e nada muda.

Exportar é uma forma prática de guardar um tema antes de experimentar, ou de copiar o aspeto de uma organização para outra.

## O que os utilizadores veem

Depois de guardado, o tema aplica-se a toda a aplicação — todas as páginas, em modo claro e escuro — a todos os membros da organização, após o próximo recarregamento (não imediatamente noutras sessões abertas). Um utilizador que nunca carregou a organização vê a predefinição do DocBits até as definições da organização terem sido carregadas uma vez; depois o tema assume o controlo.

Repor devolve todos ao aspeto predefinido do DocBits no próximo recarregamento, exatamente como se nunca tivesse existido um tema da organização.

## Dicas

* **Verifique o contraste nos dois modos.** O editor não avisa sobre combinações de baixo contraste (por exemplo, uma cor de marca clara com texto claro). Use os painéis claro e escuro da pré-visualização para confirmar que o texto continua legível antes de guardar.
* **Não altere as cores de estado sem uma razão para isso.** Destructive (erros), success, warning e info mantêm o seu significado em toda a aplicação — alterá-las pode fazer com que um erro pareça um sucesso à primeira vista. Altere a cor de marca e deixe as cores de estado nos valores predefinidos, a menos que a organização precise de mais do que o habitual vermelho/verde/âmbar/azul.
* **Comece com uma paleta completa.** Exportar o tema atual ou começar na predefinição do DocBits dá a cada cor base um valor a partir do qual editar, em vez de adivinhar que tokens existem.
* **Uma alteração de tema afeta todos os utilizadores da organização no próximo recarregamento.** Não existe um passo de pré-visualização só para um subconjunto de utilizadores; teste o resultado em claro e escuro antes de dizer à equipa que está pronto.
