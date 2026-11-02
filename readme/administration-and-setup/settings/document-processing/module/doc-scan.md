---
description: Crie documentos no DocBits com um scanner local e o Doc Scan.
---

# Doc Scan

## Transferir e instalar o software do scanner

No painel do DocBits, clique em Scan Document.

<figure><img src="../../../../.gitbook/assets/image (203).png" alt="Botão Scan Document no painel do DocBits"><figcaption></figcaption></figure>

Se o software local do scanner não estiver instalado, o DocBits apresenta um pedido de transferência. Escolha a transferência correspondente ao seu sistema operativo.

<figure><img src="../../../../.gitbook/assets/image (204).png" alt="Pedido de transferência do software local do scanner"><figcaption></figcaption></figure>

Abra o ficheiro de instalação transferido. O instalador ilustrado destina-se ao macOS; siga as instruções para o seu sistema operativo.

<figure><img src="../../../../.gitbook/assets/image (205).png" alt="Início do instalador do software do scanner"><figcaption></figcaption></figure>

No instalador ilustrado, clique em Continue, aceite a licença de software com Agree e prossiga. Verifique o destino e o espaço necessário e clique em Install. Os 33,6 MB apresentados aplicam-se a essa versão do instalador; o espaço necessário pode variar consoante a versão.

Quando a instalação terminar, feche o instalador.

<figure><img src="../../../../.gitbook/assets/image (206).png" alt="Instalação do software do scanner concluída"><figcaption></figcaption></figure>

Abra https://local.polydocs.io:12500/ no navegador para testar o serviço local. Se o navegador não conseguir aceder ao serviço e utilizar uma FRITZ!Box, verifique as definições de proteção contra DNS rebinding descritas abaixo.

<figure><img src="../../../../.gitbook/assets/image (207).png" alt="Erro do navegador durante o teste do serviço local do scanner"><figcaption></figcaption></figure>

Quando a página do serviço local aparecer, clique em DocBits para abrir o DocBits.

<figure><img src="../../../../.gitbook/assets/image (208).png" alt="Página do serviço local do scanner após uma ligação bem-sucedida"><figcaption></figcaption></figure>

Inicie sessão na página de acesso do DocBits para abrir o seu painel.

<figure><img src="../../../../.gitbook/assets/image (209).png" alt="Página de início de sessão do DocBits aberta a partir do serviço local"><figcaption></figcaption></figure>

Ative o Doc Scan nas definições, em Módulos.

<figure><img src="../../../../.gitbook/assets/image (210).png" alt="Definição do módulo Doc Scan"><figcaption></figcaption></figure>

## Definições de rede da FRITZ!Box

Se https://local.polydocs.io:12500/ estiver inacessível porque uma FRITZ!Box bloqueia respostas DNS com endereços privados, o navegador pode indicar que o tempo de espera de DNS foi excedido. A FRITZ!Box utiliza esta proteção contra DNS rebinding. Adicione uma exceção de nome de anfitrião para este serviço local:

1. Na interface alemã da FRITZ!Box, abra Heimnetz (rede doméstica) e, depois, Netzwerk (rede).
2. Abra o separador Netzwerkeinstellungen (definições de rede).
3. Em DNS-Rebind-Schutz (proteção contra DNS rebinding), adicione local.polydocs.io às exceções de nomes de anfitrião.
4. Clique em Übernehmen (aplicar) e volte a testar o serviço local.

## Desinstalar o Doc2Scan Service Manager

Para desinstalar o Doc2Scan Manager no macOS, execute:

```bash
sudo bash /Library/doc2scan/uninstall.sh
```

## Compatibilidade de scanners

O sane-airscan é um backend SANE para Apple AirScan/eSCL e Microsoft WSD (WS-Scan, Web Services for Devices). Estes são protocolos de digitalização em rede.

Consulte as [informações de compatibilidade mantidas pelo sane-airscan](https://github.com/alexpevzner/sane-airscan) para conhecer os dispositivos e protocolos cujo suporte foi comunicado. A disponibilidade de um protocolo ou um relato sobre o sane-airscan não garante que todas as funções do dispositivo funcionem no Doc Scan. Teste o scanner com o fluxo de trabalho do Doc Scan de que necessita.
