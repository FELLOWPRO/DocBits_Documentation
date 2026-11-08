# Como funciona a pesquisa na documentação

O Settings Assistant procura informações relevantes nas páginas públicas em [docs.docbits.com](https://docs.docbits.com). Os resultados podem incluir o título de uma página, uma passagem curta e uma ligação à página de origem. Abra a ligação quando precisar das instruções completas ou de uma captura de ecrã.

## Encontrar a página certa

A pesquisa combina correspondência de palavras com correspondência por significado. Isto ajuda quando a sua pergunta usa palavras diferentes das de um título de página. O assistente pode também usar a página de definições que está a ver para tornar a resposta mais relevante.

Se a pesquisa por significado estiver temporariamente indisponível, a pesquisa na documentação continua a poder usar a correspondência de palavras. Uma pergunta específica com o nome da definição é a melhor forma de tentar novamente.

## Idiomas

A pesquisa na documentação usa atualmente os índices das páginas de ajuda em **inglês** e **alemão**. Se a interface do DocBits usar outro idioma, o assistente recorre a resultados de documentação em inglês. A página ligada mostra o seu próprio idioma; verifique-o antes de seguir passos ou comparar capturas de ecrã.

## Quando as alterações ficam pesquisáveis

O índice de pesquisa é atualizado quando alterações à documentação inglesa ou alemã são publicadas a partir do repositório de documentação. Uma reconciliação regular também remove ligações a páginas que já não estão na navegação da documentação. Uma página recentemente publicada pode demorar algum tempo a aparecer no assistente.

### Visão técnica para administradores

As páginas de ajuda publicadas são divididas em secções e armazenadas num **OpenSearch documentation index** próprio por cada idioma suportado. Este índice é separado dos índices usados para os documentos carregados de uma organização. Quando uma página muda, as secções inalteradas podem ser ignoradas e as secções alteradas são reindexadas. As páginas removidas são eliminadas do índice de documentação.

Para uma pergunta, o serviço combina correspondências de palavras-chave com similaridade vetorial e depois ordena as passagens mais relevantes. Se o serviço de embeddings não estiver disponível, a pesquisa por palavras-chave continua disponível. O Settings Assistant recebe ligações de origem e passagens curtas desta pesquisa na documentação; não lê o índice de documentos de uma organização para este efeito.

Se não encontrar uma página, pesquise diretamente em [docs.docbits.com](https://docs.docbits.com), tente uma pergunta mais precisa ou contacte o suporte do DocBits.

{% hint style="info" %}
Esta pesquisa abrange as páginas de ajuda do DocBits. A funcionalidade [Fulltext Search](../document-processing/module/fulltext-search.md) pesquisa nos documentos da sua organização e tem definições próprias.
{% endhint %}

Voltar a [utilizar o Settings Assistant](README.md).
