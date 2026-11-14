# PWA Cache Status

A página **PWA Cache Status** é uma ferramenta de diagnóstico para administradores que investigam uma **tela em branco** ou um aplicativo que carrega arquivos desatualizados. O DocBits pode usar Service Workers e caches do navegador para carregar os arquivos da aplicação. Esta página mostra a captura de diagnóstico atual do navegador e oferece ações de manutenção para problemas relacionados a cache. A captura, por si só, não estabelece a causa de uma tela em branco nem prova que uma instalação de PWA está saudável.

Os textos desta página de diagnóstico ainda estão disponíveis apenas em inglês; por isso, os rótulos citados abaixo aparecem exatamente como na aplicação.

## Como acessar

A página é destinada a administradores e não está ligada na barra lateral. Há duas formas de abri-la:

* Abra a URL diretamente: `https://app.docbits.com/debug/pwa-cache-status`
* Na aplicação principal (por exemplo, no Painel), pressione <kbd>Ctrl</kbd> + <kbd>K</kbd> (ou <kbd>Cmd</kbd> + <kbd>K</kbd> no macOS) para abrir a [Pesquisa Rápida Global](../global-quick-search.md), digite "PWA Cache Status" e pressione <kbd>Enter</kbd> no resultado.

<figure><img src="../../../.gitbook/assets/dbdc-995-pwa-cache-status-page-pt-20261111.png" alt="Página de diagnóstico PWA Cache com o status do Service Worker, as informações de versão, a lista de itens em cache e os quatro botões de ação"><figcaption><p>A página de diagnóstico PWA Cache numa sessão em português: painéis de status, as quatro ações e o aviso de depuração. Os textos desta página de diagnóstico permanecem em inglês, porque a aplicação ainda não os traduz. Os valores de versão e as contagens de registros e de caches variam conforme o navegador e o ambiente.</p></figcaption></figure>

## Ler os painéis de status

* **Service Worker** — **Available: Yes/No** informa se o navegador oferece suporte à API Service Worker. **Registrations** conta os registros na origem atual do navegador. Estes valores não provam que o DocBits esteja instalado como PWA, que um worker controle esta página ou que a instalação esteja saudável.
* **Version** — **Current** é a versão do aplicativo fornecida pela build carregada. **Stored** é a versão de referência salva no navegador para este pacote do aplicativo; não é um inventário das versões de todos os arquivos em cache. **Mismatch: Yes** aparece apenas quando os dois valores são conhecidos e diferentes. Uma versão atual vazia ou **Stored: Not set** não prova que os caches estejam atualizados, mesmo que **Mismatch** mostre _No_.
* **Cached Items** — lista os nomes de todos os caches de CacheStorage na origem atual, e não arquivos individuais nem apenas os caches do DocBits. A contagem é o número de nomes de cache. _No caches found_ significa que esta captura não contém nomes de cache do CacheStorage; isso não diz nada sobre outros armazenamentos do navegador nem sobre o cache HTTP comum.

Valores vazios ou uma contagem zero também podem resultar de APIs indisponíveis ou de leituras de diagnóstico que falharam; não provam que o navegador não tenha recursos em cache.

Uma origem é a combinação de protocolo, host e porta. Estas ferramentas atuam em todos os caches e registros dessa origem, incluindo os usados por outros caminhos da aplicação.

## As quatro ações

| Ação | O que a ação faz |
| --- | --- |
| **Reload Page** | Executa um recarregamento normal da página. Não apaga explicitamente os caches nem ignora um Service Worker. |
| **Clear All Caches** | Tenta apagar todos os caches de CacheStorage desta origem e atualiza a captura de diagnóstico. Os carregamentos seguintes podem precisar baixar os arquivos novamente. |
| **Unregister Service Workers** | Tenta cancelar o registro de todos os Service Workers desta origem e atualiza a captura de diagnóstico. Verifique o status resultante antes de presumir que a limpeza foi bem-sucedida. |
| **Emergency Cleanup** | Tenta apagar os caches e cancelar o registro dos Service Workers em conjunto e, em seguida, agenda um recarregamento normal da página. Só tenta salvar a versão de referência atual depois de as duas etapas de limpeza reportarem sucesso e de existir uma versão atual do aplicativo. Uma falha de armazenamento no navegador ainda pode impedir que a versão de referência seja salva. Se qualquer uma das etapas falhar, a versão de referência anterior é mantida. |

⚠️ **Aviso:** Estas ferramentas servem apenas para depuração. Use **Emergency Cleanup** apenas em caso de tela em branco. Apagar caches pode remover dados em cache e recursos offline de aplicações na mesma origem; não presuma que os caches contenham apenas arquivos descartáveis do aplicativo. O carregamento seguinte pode ser mais lento ou exigir uma conexão de rede funcional. Uma notificação de sucesso ou um recarregamento agendado, por si só, não prova que todas as operações de limpeza foram bem-sucedidas.

## Fluxo típico de resolução de problemas

1. Abra a página PWA Cache Status e anote **Current**, **Stored**, **Mismatch**, o número de registros e os nomes dos caches. Uma divergência é uma pista de diagnóstico, não um diagnóstico completo.
2. Se for adequado para a sua sessão de diagnóstico, experimente **Reload Page**. É um recarregamento comum e pode continuar a usar respostas em cache.
3. Se a tela continuar em branco, verifique a origem e o aviso acima antes de usar **Clear All Caches**, depois recarregue a página e inspecione o status novamente.
4. Use **Emergency Cleanup** apenas para um problema de tela em branco persistente. Tenta as duas operações de limpeza e agenda um recarregamento; a versão de referência só muda nas condições de sucesso descritas acima. Se a limpeza falhar, mantenha a versão de referência anterior como pista e entre em contato com o suporte em vez de presumir que o problema está resolvido.
5. Se nada disto ajudar, colete o diagnóstico com o **Debug Collector** (<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>) e envie-o ao suporte — consulte o [Debug Collector](../debug-collector.md). Verifique se o diagnóstico contém informações sensíveis antes de compartilhá-lo.
