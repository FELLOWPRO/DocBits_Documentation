# Detecção de duplicatas

## Detecte duplicatas e tome uma decisão informada

<figure><picture><source srcset="../../../../../.gitbook/assets/intro-process-02-dubletten-pt-dark-20261029.png" media="(prefers-color-scheme: dark)"><img src="../../../../../.gitbook/assets/intro-process-02-dubletten-pt-light-20261029.png" alt="Detecte duplicatas e tome uma decisão informada"></picture><figcaption><p>Detecte duplicatas e tome uma decisão informada</p></figcaption></figure>

DocBits compara os campos configurados dentro da janela de tempo selecionada. Quando uma correspondência for encontrada, abra o aviso de duplicata e compare os documentos antes de continuar ou arquivar. O bloqueio de exportações duplicadas é uma configuração separada; uma correspondência não arquiva automaticamente um documento.

Use a **Detecção de duplicatas** para marcar documentos que coincidem com outro documento em campos selecionados dentro de um período escolhido. As opções pertencem a cada tipo de documento.

## Abrir as configurações

1. Abra **Configurações → Tipos de documentos**.
2. No tipo de documento que deseja configurar, selecione **Configurações**.
3. Em **Mais Configurações**, abra **Detecção de duplicatas**.

<figure><img src="../../../../../.gitbook/assets/more-settings-duplicate-document-handling-settings-off-pt-20261111.png" alt="Mais Configurações da fatura com a secção Detecção de duplicatas aberta e a deteção de documentos duplicados desativada"><figcaption><p>A secção mostra quatro interruptores separados. Os seletores de campos e de intervalo aparecem apenas quando a deteção está ativada.</p></figcaption></figure>

## Escolher o que conta como duplicata

1. Ative **Detecção de documentos duplicados**. Os seletores **Campos de detecção duplicados** e **Intervalo de detecção de duplicatas** aparecem.
2. Selecione os campos que devem coincidir. A lista oferece **Número da fatura**, **Data**, **Nome do Fornecedor**, **ID do fornecedor**, **Montante total** e **Número do pedido**; escolha os campos que distinguem os documentos no seu próprio processo.
3. Escolha um intervalo: **1 mês**, **3 meses (recomendado)**, **6 meses** ou **1 ano**. Um intervalo mais longo verifica um período maior e pode demorar mais a carregar.

Cada alteração é guardada ao fazê-la; não existe um botão Guardar separado nesta secção. Se desativar a deteção, os seletores de campos e de intervalo ficam ocultos.

<figure><img src="../../../../../.gitbook/assets/more-settings-duplicate-document-handling-settings-on-pt-20261111.png" alt="Detecção de documentos duplicados ativada, com os seletores de campos e de intervalo visíveis"><figcaption><p>Com a deteção ativada, os campos de comparação e o intervalo de tempo ficam visíveis.</p></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/more-settings-duplicate-document-handling-field-options-pt-20261111.png" alt="Lista aberta dos campos disponíveis para a deteção de documentos duplicados"><figcaption><p>A lista mostra todos os campos que podem ser comparados. Selecione os que identificam um documento de forma única no seu processo.</p></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/more-settings-duplicate-document-handling-interval-options-pt-20261111.png" alt="Menu do Intervalo de detecção de duplicatas com um mês, três meses, seis meses e um ano"><figcaption><p>O intervalo de três meses está assinalado como recomendado no menu.</p></figcaption></figure>

Para o tipo de documento Fatura, esta secção oferece também **Detecção de faturas duplicadas**, **Exportação de documentos duplicados em bloco** e **Ignorar linha livre de impostos**. São interruptores separados; ative apenas o comportamento de que o seu processo de faturas necessita. Os interruptores adicionais não aparecem para os outros tipos de documento.

## Rever um documento marcado

Quando o DocBits encontra uma correspondência, a linha do documento no **Painel** mostra um ícone de duplicata. Selecione o ícone para comparar os registos correspondentes no painel lateral. O ícone aparece apenas quando existe uma correspondência.

Ao abrir um documento marcado, o aviso de duplicata oferece **Ver duplicata**, **Continuar mesmo assim** e, se o documento ainda não tiver sido arquivado, **Arquivar**. Reveja os registos correspondentes antes de escolher uma ação. Consulte [o guia do Painel](../../dashboard/README.md) para a lista de documentos.

Ao rever possíveis duplicatas, compare o número da fatura, o fornecedor, a data e o montante. Utilize o aviso de duplicata e os detalhes do documento correspondente para decidir o que precisa de correção.
