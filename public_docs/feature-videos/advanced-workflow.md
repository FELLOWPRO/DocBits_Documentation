---
description: "O seu processo. A sua lógica. Tudo ligado."
---

# DocBits Advanced Workflow

Crie fluxos documentais com cartões ligados. Escolha percursos por condições, reúna resultados e dê aos erros um percurso próprio, mantendo a visão do processo completo.

## Ver a apresentação

{% embed url="https://docbits-videos.fra1.digitaloceanspaces.com/settings-assistant/advanced-workflow-feature/v5/pt.mp4" %}

[Leitor com legendas](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-feature/v5/pt.html) · [Legendas](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-feature/v5/pt.vtt) · [Textos no ecrã](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-feature/v5/pt.txt) · 1:48 · Full HD

## Da fatura à próxima ação

Uma fatura recebida inicia o exemplo. Um valor total superior a 1.000 segue o percurso Approval; 1.000 ou menos segue Standard. O vídeo mostra depois testes reais com 1.500 e 500 no designer DocBits, incluindo os resultados.

## Três formas de controlar o fluxo

| Função | Na prática |
| --- | --- |
| **Escolher o percurso** | Ligue Start ou When a uma condição. Success, Failed Condition e Error têm saídas distintas. |
| **Reunir resultados ligados** | Wait ANY exige pelo menos uma fonte ligada correspondente. Wait ALL exige um resultado ligado correspondente de cada fonte. Nenhum cancela outras ações. |
| **Ligar a próxima ação** | Utilize percursos de erro, Call API e notas para ligar sistemas e explicar o desenho. As notas não executam ações. |

## Crie o seu próprio fluxo

<a href="../administration-and-setup/workflow/advanced-workflow-builder.md" class="button primary">Abrir o guia de Advanced Workflow</a>

[Converse sobre o seu processo com a DocBits](https://docbits.com/en/book-demo/)

{% hint style="info" %}
O vídeo combina cartões animados e gravações reais da interface Dev em inglês. Inclui música e textos em português, sem narração. As ações de teste definem o campo de exemplo `approval_route` como `Approval` ou `Standard`; um processo completo de aprovação humana exige as suas próprias ações de negócio. Esta demonstração não foi guardada nem ativada. As animações de junção mostram requisitos de resultados, não tempos de execução. Teste a acessibilidade e o percurso completo do documento; um teste parcial bem-sucedido não comprova o fluxo em produção.
{% endhint %}
