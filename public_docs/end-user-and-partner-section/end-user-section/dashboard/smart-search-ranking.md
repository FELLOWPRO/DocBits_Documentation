# Smart Search Ranking

O Smart Search Ranking coloca os documentos que procura no topo de uma pesquisa no painel. Uma pesquisa por palavra-chave encontra todos os documentos que contêm a sua palavra; o Smart Search Ranking acrescenta um passo: uma IA lê os melhores resultados e coloca primeiro os documentos que são mesmo sobre a sua pesquisa. As correspondências exatas — números de fatura, números de encomenda, nomes de fornecedores — ficam sempre no topo.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/features/smart-search-ranking/preview/pt.mp4" %}
Smart Search Ranking no painel (narração em português). [Leitor com legendas](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/features/smart-search-ranking/preview/pt.html) · [Transcrição](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/features/smart-search-ranking/preview/pt.txt)
{% endembed %}

## O que muda

| | Ordem por palavra-chave | Com Smart Search Ranking |
| --- | --- | --- |
| Que documentos são encontrados | Os mesmos | Os mesmos |
| Ordem dos resultados | Por correspondência da palavra-chave | Primeiro os documentos sobre a sua pesquisa |
| Correspondências exatas (n.º de fatura, n.º de encomenda, fornecedor) | Primeiro | Primeiro |
| Ordenação por coluna, pesquisas `ocr:` e por campo | Sem alteração | Sem alteração — mantêm a sua própria ordem |

## Exemplo

Oito faturas de teste contêm a palavra *parafuso*: parafusos em aço inoxidável, um conjunto de chaves de fendas, a manutenção de um compressor de parafuso, massa parafuso, uma planta, dossiers de parafusos, trava-roscas e uma mala sortido de parafusos.

* Pesquise **parafuso**. Na ordem por palavra-chave, o conjunto de chaves de fendas é o primeiro resultado e a fatura de parafusos fica em quinto. Com o Smart Search Ranking, os parafusos passam para o topo — primeiro a mala sortido, depois os parafusos inox — e o conjunto de chaves de fendas desce para sétimo.
* Pesquise **chave de fendas**. Na ordem por palavra-chave, o conjunto de chaves de fendas é o primeiro. Com o Smart Search Ranking, as chaves de fendas profissionais passam para primeiro e o conjunto fica logo a seguir, porque desta vez são mesmo chaves de fendas; o brinquedo desce.

## Onde se aplica

* Na [Pesquisa rápida](quick-search.md) do painel com texto simples (não nos chips de campo `campo:`).
* O topo da lista de resultados é reordenado; mais abaixo, as listas longas mantêm a ordem por palavra-chave.
* Se o serviço de ordenação não responder dentro do seu tempo, a pesquisa mostra a ordem normal por palavra-chave. Nada é escondido e nenhum resultado é removido.

## Como se ativa

O Smart Search Ranking é ativado pela DocBits por organização. Peça ao seu contacto DocBits que o ative. Aplica-se a todos os utilizadores da organização dentro de um minuto, sem alterar a forma como pesquisa.
