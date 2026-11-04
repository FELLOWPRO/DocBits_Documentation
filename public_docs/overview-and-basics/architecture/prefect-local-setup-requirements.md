# Requisitos para a Configuração Local do Prefect

#### Requisitos

Verifique se os itens a seguir estão instalados no sistema host:

* **Docker Engine**
* **Docker Compose v2**&#x20;

#### Compatibilidade com o sistema operacional do host

* **Linux**: recomendado e totalmente compatível.
* **Windows**: funciona com o Docker Desktop (WSL2). Os mapeamentos de volumes podem causar problemas.
* **macOS**: compatível por meio do Docker Desktop. Comportamento semelhante ao do Windows.

#### Requisitos do sistema

* **RAM**: 1 a 2 GB por contêiner. Para vários fluxos: 2 a 4 GB.
* **CPU**: 1 a 2 núcleos por contêiner. Para fluxos simultâneos: 2 a 4 núcleos.
* **Disco**: 2 a 3 GB para a imagem e os logs&#x20;
