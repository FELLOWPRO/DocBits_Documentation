# Canais PDP/PPF Obrigatórios – PEPPOL Apenas como Transporte na Fatura Eletrônica de 2026 da França

## PDP ou PPF obrigatório para faturas eletrônicas B2B nacionais

De acordo com a obrigatoriedade da fatura eletrônica na França em 2026, as empresas não podem depender exclusivamente da rede PEPPOL para trocar faturas B2B nacionais. A lei exige que todas as faturas entre empresas francesas registradas para fins de IVA sejam encaminhadas por uma plataforma privada certificada (PDP) ou pelo portal público de faturamento do Estado (PPF) para atender aos [requisitos](https://www.ey.com/en_gl/technical/tax-alerts/france-revises-schedule-for-adopting-e-invoicing-reform) legais. Em outras palavras, as empresas deixarão de enviar faturas diretamente aos clientes: elas deverão transmiti-las por uma plataforma de faturamento eletrônico aprovada (uma PDP) ou pelo [portal](https://www.avalara.com/blog/en/europe/2022/09/france-publishes-updated-specifications-for-e-invoicing-and-e-reporting.html) do governo. Isso garante que a autoridade fiscal receba os dados exigidos em tempo real. Simplesmente trocar faturas pela PEPPOL sem envolver uma PDP/PPF credenciada não atenderia às obrigações de relatório e de transmissão exigidas.

<figure><img src="../../.gitbook/assets/Picture 1.png" alt=""><figcaption></figcaption></figure>

### Introdução à oferta de serviço

O modo API permite que os usuários acessem todos os recursos disponíveis para eles a partir das ferramentas de TI já implantadas nas estruturas dos parceiros. Há dois métodos de integração:

### ·       Integração aos sistemas de informação (SI):

As APIs são integradas diretamente aos sistemas de informação ou aos softwares de gestão das partes que emitem e recebem faturas, ou de seus operadores de desmaterialização (ODs). Assim, os usuários podem acessar diretamente os recursos da solução e suas atualizações a partir de suas ferramentas de TI habituais, internas ou oferecidas pelo seu OD.

As APIs também podem ser integradas ao SI das PDPs para lhes dar mais flexibilidade (em comparação com o modo EDI), com algumas APIs dedicadas a esse uso.

### ·       Integração a softwares de terceiros:

Os desenvolvedores de software poderão oferecer soluções baseadas nas APIs. Dependendo do modo escolhido pelo desenvolvedor, a conexão pode ser feita por ele ou pelo próprio cliente durante a instalação ou a implantação em seu SI. Esse software de terceiros complementará o sistema de informação do cliente, adicionando uma camada de comunicação com o PPF.

<figure><img src="../../.gitbook/assets/Picture 6.png" alt=""><figcaption></figcaption></figure>

## PEPPOL usada apenas como camada de interoperabilidade

A França está adotando a PEPPOL como parte de sua infraestrutura, mas apenas como camada de transporte dentro da estrutura das PDPs, e não como uma via de conformidade independente.  A autoridade fiscal francesa (DGFiP) está se tornando a Peppol Authority para padronizar a forma como as PDPs se [interconectam](https://www.avalara.com/blog/en/europe/2025/01/e-invoicing-reform-france.html). Todas as PDPs certificadas devem se interconectar pela rede PEPPOL para trocar [faturas](https://nymus.be/fr/facturation-electronique-en-france/).  Isso significa que a PEPPOL facilitará a interoperabilidade entre plataformas autorizadas, sem substituir a necessidade dessas plataformas.  Na prática, uma empresa só pode usar a PEPPOL por meio de uma PDP (ou do PPF, atuando em seu papel limitado) que utilize a PEPPOL para enviar ou receber faturas. Isso foi confirmado em orientações oficiais: o portal público se concentra na coleta de dados, enquanto a distribuição das faturas ocorrerá exclusivamente por meio das PDPs, que utilizarão redes como a [PEPPOL](https://edicomgroup.com/blog/status-of-b2b-electronic-invoicing-in-france) para a [troca](https://nymus.be/fr/facturation-electronique-en-france/).

\


<figure><img src="../../.gitbook/assets/Picture 2.png" alt=""><figcaption></figcaption></figure>

## Conexão de um hub:

O hub oferece aos seus clientes uma solução web ou de aplicação para que possam fazer as diversas chamadas de API. **Portanto, é o hub que faz as chamadas de API em nome de todos os seus clientes**. Nesse caso, cada parceiro deve ter uma conta técnica, mas apenas o hub precisa de uma aplicação no PISTE e de uma conexão com o PPF.

<figure><img src="../../.gitbook/assets/Picture 5.png" alt=""><figcaption></figcaption></figure>



Fonte: o Artigo 91 da Lei de Finanças de 2024 da França (resumido pela EY) determina que as faturas eletrônicas sejam enviadas por uma PDP certificada ou pelo portal do Estado.  As atualizações da autoridade fiscal francesa esclarecem ainda que, após as reformas de 2024, as empresas devem usar uma PDP registrada para a fatura eletrônica B2B (o PPF deixará de funcionar como plataforma de troca gratuita).  A PEPPOL está sendo implementada para conectar essas PDPs, e não como um canal alternativo fora do sistema.  Isso confirma que usar apenas a rede PEPPOL não é suficiente: a conformidade com o regime de fatura eletrônica de 2026 na França exige a integração com o PPF ou com uma PDP certificada, com a PEPPOL servindo apenas como a rede de entrega subjacente entre essas plataformas.

<div><figure><img src="../../.gitbook/assets/Picture 3.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/Picture 4.png" alt=""><figcaption></figcaption></figure></div>
