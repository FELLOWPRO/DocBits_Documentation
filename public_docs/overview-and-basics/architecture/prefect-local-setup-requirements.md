# Requisitos de la configuración local de Prefect

#### Requisitos

Asegúrese de que lo siguiente esté instalado en el sistema anfitrión:

* **Docker Engine**
* **Docker Compose v2**&#x20;

#### Compatibilidad del sistema operativo anfitrión

* **Linux**: recomendado y totalmente compatible.
* **Windows**: funciona con Docker Desktop (WSL2). Los montajes de volúmenes pueden causar problemas.
* **macOS**: compatible mediante Docker Desktop. Su comportamiento es similar al de Windows.

#### Requisitos del sistema

* **RAM**: 1–2 GB por contenedor. Para varios flujos: 2–4 GB.
* **CPU**: 1–2 núcleos por contenedor. Para flujos simultáneos: 2–4 núcleos.
* **Disco**: 2–3 GB para la imagen y los registros&#x20;
